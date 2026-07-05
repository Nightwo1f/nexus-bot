package org.lwjgl.system;

import java.io.IOException;
import java.io.PrintStream;
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.nio.IntBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.function.BiPredicate;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;
import javax.annotation.Nullable;
import org.lwjgl.PointerBuffer;
import org.lwjgl.system.libffi.FFICIF;
import org.lwjgl.system.libffi.FFIType;
import org.lwjgl.system.libffi.LibFFI;
import org.lwjgl.system.linux.LinuxLibrary;
import org.lwjgl.system.macosx.MacOSXLibrary;
import org.lwjgl.system.windows.WindowsLibrary;

public final class APIUtil {
  public static final PrintStream DEBUG_STREAM = getDebugStream();
  
  private static final Pattern API_VERSION_PATTERN;
  
  static {
    String PREFIX = "[^\\d\\n\\r]*";
    String VERSION = "(\\d+)[.](\\d+)(?:[.](\\S+))?";
    String IMPLEMENTATION = "(?:\\s+(.+?))?\\s*";
    API_VERSION_PATTERN = Pattern.compile("^" + PREFIX + VERSION + IMPLEMENTATION + "$", 32);
  }
  
  private static PrintStream getDebugStream() {
    PrintStream debugStream = System.err;
    Object state = Configuration.DEBUG_STREAM.get();
    if (state instanceof String) {
      try {
        Supplier<PrintStream> factory = Class.forName((String)state).getConstructor(new Class[0]).newInstance(new Object[0]);
        debugStream = factory.get();
      } catch (Exception e) {
        e.printStackTrace();
      } 
    } else if (state instanceof Supplier) {
      debugStream = ((Supplier<PrintStream>)state).get();
    } else if (state instanceof PrintStream) {
      debugStream = (PrintStream)state;
    } 
    return debugStream;
  }
  
  public static void apiLog(CharSequence msg) {
    if (Checks.DEBUG)
      DEBUG_STREAM.print("[LWJGL] " + msg + "\n"); 
  }
  
  public static void apiLogMore(CharSequence msg) {
    if (Checks.DEBUG)
      DEBUG_STREAM.print("\t" + msg + "\n"); 
  }
  
  public static void apiLogMissing(String api, ByteBuffer functionName) {
    if (Checks.DEBUG) {
      String function = MemoryUtil.memASCII(functionName, functionName.remaining() - 1);
      DEBUG_STREAM.print("[LWJGL] Failed to locate address for " + api + " function " + function + "\n");
    } 
  }
  
  public static String apiFindLibrary(String start, String name) {
    String libName = Platform.get().mapLibraryName(name);
    try (Stream<Path> paths = Files.find(
          Paths.get(start, new String[0]).toAbsolutePath(), 2147483647, (path, attributes) -> 
          
          (attributes.isRegularFile() && path.getFileName().toString().equals(libName)), new java.nio.file.FileVisitOption[0])) {
      return paths
        .findFirst()
        .map(Path::toString)
        .orElse(name);
    } catch (IOException e) {
      return name;
    } 
  }
  
  public static SharedLibrary apiCreateLibrary(String name) {
    switch (Platform.get()) {
      case WINDOWS:
        return (SharedLibrary)new WindowsLibrary(name);
      case LINUX:
        return (SharedLibrary)new LinuxLibrary(name);
      case MACOSX:
        return (SharedLibrary)MacOSXLibrary.create(name);
    } 
    throw new IllegalStateException();
  }
  
  public static long apiGetFunctionAddress(FunctionProvider provider, String functionName) {
    long a = provider.getFunctionAddress(functionName);
    if (a == 0L)
      requiredFunctionMissing(functionName); 
    return a;
  }
  
  private static void requiredFunctionMissing(String functionName) {
    if (!((Boolean)Configuration.DISABLE_FUNCTION_CHECKS.get(Boolean.valueOf(false))).booleanValue())
      throw new NullPointerException("A required function is missing: " + functionName); 
  }
  
  public static long apiGetFunctionAddressOptional(SharedLibrary library, String functionName) {
    long a = library.getFunctionAddress(functionName);
    if (Checks.DEBUG_FUNCTIONS && a == 0L)
      optionalFunctionMissing(library, functionName); 
    return a;
  }
  
  private static void optionalFunctionMissing(SharedLibrary library, String functionName) {
    if (Checks.DEBUG)
      DEBUG_STREAM.print("[LWJGL] Failed to locate address for " + library.getName() + " function " + functionName + "\n"); 
  }
  
  @Nullable
  public static ByteBuffer apiGetMappedBuffer(@Nullable ByteBuffer buffer, long mappedAddress, int capacity) {
    if (buffer != null && MemoryUtil.memAddress(buffer) == mappedAddress && buffer.capacity() == capacity)
      return buffer; 
    return (mappedAddress == 0L) ? null : ((ByteBuffer)MemoryUtil.<ByteBuffer>wrap(MemoryUtil.BUFFER_BYTE, mappedAddress, capacity)).order(MemoryUtil.NATIVE_ORDER);
  }
  
  public static long apiGetBytes(int elements, int elementShift) {
    return (elements & 0xFFFFFFFFL) << elementShift;
  }
  
  public static long apiCheckAllocation(int elements, long bytes, long maxBytes) {
    if (Checks.DEBUG) {
      if (elements < 0)
        throw new IllegalArgumentException("Invalid number of elements"); 
      if (maxBytes + Long.MIN_VALUE < bytes + Long.MIN_VALUE)
        throw new IllegalArgumentException("The request allocation is too large"); 
    } 
    return bytes;
  }
  
  public static interface Encoder {
    ByteBuffer encode(CharSequence param1CharSequence, boolean param1Boolean);
  }
  
  public static class APIVersion implements Comparable<APIVersion> {
    public final int major;
    
    public final int minor;
    
    @Nullable
    public final String revision;
    
    @Nullable
    public final String implementation;
    
    public APIVersion(int major, int minor) {
      this(major, minor, null, null);
    }
    
    public APIVersion(int major, int minor, @Nullable String revision, @Nullable String implementation) {
      this.major = major;
      this.minor = minor;
      this.revision = revision;
      this.implementation = implementation;
    }
    
    public String toString() {
      StringBuilder sb = new StringBuilder(16);
      sb.append(this.major).append('.').append(this.minor);
      if (this.revision != null)
        sb.append('.').append(this.revision); 
      if (this.implementation != null)
        sb.append(" (").append(this.implementation).append(')'); 
      return sb.toString();
    }
    
    public boolean equals(Object o) {
      if (this == o)
        return true; 
      if (!(o instanceof APIVersion))
        return false; 
      APIVersion that = (APIVersion)o;
      return (this.major == that.major && this.minor == that.major && 
        
        Objects.equals(this.revision, that.revision) && 
        Objects.equals(this.implementation, that.implementation));
    }
    
    public int hashCode() {
      int result = this.major;
      result = 31 * result + this.minor;
      result = 31 * result + ((this.revision != null) ? this.revision.hashCode() : 0);
      result = 31 * result + ((this.implementation != null) ? this.implementation.hashCode() : 0);
      return result;
    }
    
    public int compareTo(APIVersion other) {
      if (this.major != other.major)
        return Integer.compare(this.major, other.major); 
      if (this.minor != other.minor)
        return Integer.compare(this.minor, other.minor); 
      return 0;
    }
  }
  
  @Nullable
  public static APIVersion apiParseVersion(Configuration<?> option) {
    APIVersion version;
    Object state = option.get();
    if (state instanceof String) {
      version = apiParseVersion((String)state);
    } else if (state instanceof APIVersion) {
      version = (APIVersion)state;
    } else {
      version = null;
    } 
    return version;
  }
  
  public static APIVersion apiParseVersion(String version) {
    Matcher matcher = API_VERSION_PATTERN.matcher(version);
    if (!matcher.matches())
      throw new IllegalArgumentException(String.format("Malformed API version string [%s]", new Object[] { version })); 
    return new APIVersion(
        Integer.parseInt(matcher.group(1)), 
        Integer.parseInt(matcher.group(2)), matcher
        .group(3), matcher
        .group(4));
  }
  
  public static void apiFilterExtensions(Set<String> extensions, Configuration<Object> option) {
    Object value = option.get();
    if (value == null)
      return; 
    if (value instanceof String) {
      String s = (String)value;
      if (s.indexOf('.') != -1) {
        try {
          Predicate<String> predicate = (Predicate<String>)Class.forName(s).newInstance();
          extensions.removeIf(predicate);
        } catch (Exception e) {
          throw new RuntimeException(e);
        } 
      } else {
        for (String extension : s.split(","))
          extensions.remove(extension); 
      } 
    } else if (value instanceof List) {
      List<String> list = (List<String>)value;
      extensions.removeAll(list);
    } else if (value instanceof Predicate) {
      Predicate<String> predicate = (Predicate<String>)value;
      extensions.removeIf(predicate);
    } else {
      throw new IllegalStateException("Unsupported " + option.getProperty() + " value specified.");
    } 
  }
  
  public static String apiUnknownToken(int token) {
    return apiUnknownToken("Unknown", token);
  }
  
  public static String apiUnknownToken(String description, int token) {
    return String.format("%s [0x%X]", new Object[] { description, Integer.valueOf(token) });
  }
  
  public static Map<Integer, String> apiClassTokens(@Nullable BiPredicate<Field, Integer> filter, @Nullable Map<Integer, String> target, Class<?>... tokenClasses) {
    if (target == null)
      target = new HashMap<>(64); 
    int TOKEN_MODIFIERS = 25;
    for (Class<?> tokenClass : tokenClasses) {
      if (tokenClass != null)
        for (Field field : tokenClass.getDeclaredFields()) {
          if ((field.getModifiers() & TOKEN_MODIFIERS) == TOKEN_MODIFIERS && field.getType() == int.class)
            try {
              Integer value = Integer.valueOf(field.getInt(null));
              if (filter == null || filter.test(field, value)) {
                String name = target.get(value);
                target.put(value, (name == null) ? field.getName() : (name + "|" + field.getName()));
              } 
            } catch (IllegalAccessException illegalAccessException) {} 
        }  
    } 
    return target;
  }
  
  public static long apiArray(MemoryStack stack, long... addresses) {
    PointerBuffer pointers = MemoryUtil.memPointerBuffer(stack.nmalloc(MemoryStack.POINTER_SIZE, addresses.length << MemoryStack.POINTER_SHIFT), addresses.length);
    for (long address : addresses)
      pointers.put(address); 
    return pointers.address;
  }
  
  public static long apiArray(MemoryStack stack, ByteBuffer... buffers) {
    PointerBuffer pointers = MemoryUtil.memPointerBuffer(stack.nmalloc(MemoryStack.POINTER_SIZE, buffers.length << MemoryStack.POINTER_SHIFT), buffers.length);
    for (ByteBuffer buffer : buffers)
      pointers.put(buffer); 
    return pointers.address;
  }
  
  public static long apiArrayp(MemoryStack stack, ByteBuffer... buffers) {
    long pointers = apiArray(stack, buffers);
    PointerBuffer lengths = stack.mallocPointer(buffers.length);
    for (ByteBuffer buffer : buffers)
      lengths.put(buffer.remaining()); 
    return pointers;
  }
  
  public static long apiArray(MemoryStack stack, Encoder encoder, CharSequence... strings) {
    PointerBuffer pointers = stack.mallocPointer(strings.length);
    for (CharSequence s : strings)
      pointers.put(encoder.encode(s, true)); 
    return pointers.address;
  }
  
  public static long apiArrayi(MemoryStack stack, Encoder encoder, CharSequence... strings) {
    PointerBuffer pointers = stack.mallocPointer(strings.length);
    IntBuffer lengths = stack.mallocInt(strings.length);
    for (CharSequence s : strings) {
      ByteBuffer buffer = encoder.encode(s, false);
      pointers.put(buffer);
      lengths.put(buffer.capacity());
    } 
    return pointers.address;
  }
  
  public static long apiArrayp(MemoryStack stack, Encoder encoder, CharSequence... strings) {
    PointerBuffer pointers = stack.mallocPointer(strings.length);
    PointerBuffer lengths = stack.mallocPointer(strings.length);
    for (CharSequence s : strings) {
      ByteBuffer buffer = encoder.encode(s, false);
      pointers.put(buffer);
      lengths.put(buffer.capacity());
    } 
    return pointers.address;
  }
  
  public static void apiArrayFree(long pointers, int length) {
    for (int i = length; --i >= 0;)
      MemoryUtil.nmemFree(MemoryUtil.memGetAddress(pointers + Integer.toUnsignedLong(i) * MemoryStack.POINTER_SIZE)); 
  }
  
  public static FFIType apiCreateStruct(FFIType... members) {
    MemoryUtil.MemoryAllocator allocator = MemoryUtil.getAllocator();
    PointerBuffer elementBuffer = PointerBuffer.create(allocator
        .malloc(((members.length + 1) * MemoryStack.POINTER_SIZE)), members.length + 1);
    for (int i = 0; i < members.length; i++)
      elementBuffer.put(i, (Pointer)members[i]); 
    elementBuffer.put(members.length, 0L);
    return FFIType.create(allocator.calloc(1L, FFIType.SIZEOF))
      .type((short)13)
      .elements(elementBuffer);
  }
  
  private static FFIType prep(FFIType type) {
    try (MemoryStack stack = MemoryStack.stackPush()) {
      FFICIF cif = FFICIF.calloc(stack);
      if (LibFFI.ffi_prep_cif(cif, LibFFI.FFI_DEFAULT_ABI, type, null) != 0)
        throw new IllegalStateException("Failed to prepare LibFFI type."); 
    } 
    return type;
  }
  
  public static FFIType apiCreateUnion(FFIType... members) {
    MemoryUtil.MemoryAllocator allocator = MemoryUtil.getAllocator();
    FFIType maxType = prep(members[0]);
    short maxAlignment = members[0].alignment();
    for (int i = 1; i < members.length; i++) {
      FFIType type = prep(members[i]);
      if (maxType.size() < type.size())
        maxType = type; 
      if (maxAlignment < type.alignment())
        maxAlignment = type.alignment(); 
    } 
    return FFIType.create(allocator.malloc(FFIType.SIZEOF))
      .size(maxType.size())
      .alignment(maxAlignment)
      .type((short)13)
      .elements(PointerBuffer.create(allocator.malloc((2 * MemoryStack.POINTER_SIZE)), 2)
        .put(0, (Pointer)maxType)
        .put(1, 0L));
  }
  
  public static FFIType apiCreateArray(FFIType type, int length) {
    MemoryUtil.MemoryAllocator allocator = MemoryUtil.getAllocator();
    PointerBuffer elementBuffer = PointerBuffer.create(allocator
        .malloc(((length + 1) * MemoryStack.POINTER_SIZE)), length + 1);
    for (int i = 0; i < length; i++)
      elementBuffer.put(i, (Pointer)type); 
    elementBuffer.put(length, 0L);
    return FFIType.create(allocator.calloc(1L, FFIType.SIZEOF))
      .type((short)13)
      .elements(elementBuffer);
  }
  
  public static FFICIF apiCreateCIF(int abi, FFIType rtype, FFIType... atypes) {
    MemoryUtil.MemoryAllocator allocator = MemoryUtil.getAllocator();
    PointerBuffer pArgTypes = PointerBuffer.create(allocator.malloc((atypes.length * MemoryStack.POINTER_SIZE)), atypes.length);
    for (int i = 0; i < atypes.length; i++)
      pArgTypes.put(i, (Pointer)atypes[i]); 
    FFICIF cif = FFICIF.create(allocator.malloc(FFICIF.SIZEOF));
    int errcode = LibFFI.ffi_prep_cif(cif, abi, rtype, pArgTypes);
    if (errcode != 0)
      throw new IllegalStateException("Failed to prepare libffi CIF: " + errcode); 
    return cif;
  }
  
  public static FFICIF apiCreateCIFVar(int abi, int nfixedargs, FFIType rtype, FFIType... atypes) {
    MemoryUtil.MemoryAllocator allocator = MemoryUtil.getAllocator();
    PointerBuffer pArgTypes = PointerBuffer.create(allocator.malloc((atypes.length * MemoryStack.POINTER_SIZE)), atypes.length);
    for (int i = 0; i < atypes.length; i++)
      pArgTypes.put(i, (Pointer)atypes[i]); 
    FFICIF cif = FFICIF.create(allocator.malloc(FFICIF.SIZEOF));
    int errcode = LibFFI.ffi_prep_cif_var(cif, abi, nfixedargs, rtype, pArgTypes);
    if (errcode != 0)
      throw new IllegalStateException("Failed to prepare libffi var CIF: " + errcode); 
    return cif;
  }
  
  public static int apiStdcall() {
    return (Platform.get() == Platform.WINDOWS && Pointer.BITS32) ? LibFFI.FFI_STDCALL : LibFFI.FFI_DEFAULT_ABI;
  }
  
  public static void apiClosureRet(long ret, boolean __result) {
    MemoryUtil.memPutAddress(ret, __result ? 1L : 0L);
  }
  
  public static void apiClosureRet(long ret, byte __result) {
    MemoryUtil.memPutAddress(ret, __result & 0xFFL);
  }
  
  public static void apiClosureRet(long ret, short __result) {
    MemoryUtil.memPutAddress(ret, __result & 0xFFFFL);
  }
  
  public static void apiClosureRet(long ret, int __result) {
    MemoryUtil.memPutAddress(ret, __result & 0xFFFFFFFFL);
  }
  
  public static void apiClosureRetL(long ret, long __result) {
    MemoryUtil.memPutLong(ret, __result);
  }
  
  public static void apiClosureRetP(long ret, long __result) {
    MemoryUtil.memPutAddress(ret, __result);
  }
  
  public static void apiClosureRet(long ret, float __result) {
    MemoryUtil.memPutFloat(ret, __result);
  }
  
  public static void apiClosureRet(long ret, double __result) {
    MemoryUtil.memPutDouble(ret, __result);
  }
}
