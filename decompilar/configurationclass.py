package org.lwjgl.system;

import java.util.function.Function;
import javax.annotation.Nullable;

public class Configuration<T> {
  public static final Configuration<String> LIBRARY_PATH = new Configuration("org.lwjgl.librarypath", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> BUNDLED_LIBRARY_NAME_MAPPER = new Configuration("org.lwjgl.system.bundledLibrary.nameMapper", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> BUNDLED_LIBRARY_PATH_MAPPER = new Configuration("org.lwjgl.system.bundledLibrary.pathMapper", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> SHARED_LIBRARY_EXTRACT_DIRECTORY = new Configuration("org.lwjgl.system.SharedLibraryExtractDirectory", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> SHARED_LIBRARY_EXTRACT_PATH = new Configuration("org.lwjgl.system.SharedLibraryExtractPath", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> SHARED_LIBRARY_EXTRACT_FORCE = new Configuration("org.lwjgl.system.SharedLibraryExtractForce", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> EMULATE_SYSTEM_LOADLIBRARY = new Configuration("org.lwjgl.system.EmulateSystemLoadLibrary", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> LIBRARY_NAME = new Configuration("org.lwjgl.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> MEMORY_ALLOCATOR = new Configuration("org.lwjgl.system.allocator", (StateInit)StateInit.STRING);
  
  public static final Configuration<Integer> STACK_SIZE = new Configuration("org.lwjgl.system.stackSize", (StateInit)StateInit.INT);
  
  public static final Configuration<Integer> ARRAY_TLC_SIZE = new Configuration("org.lwjgl.system.arrayTLCSize", (StateInit)StateInit.INT);
  
  public static final Configuration<Integer> JNI_NATIVE_INTERFACE_FUNCTION_COUNT = new Configuration("org.lwjgl.system.JNINativeInterfaceSize", (StateInit)StateInit.INT);
  
  public static final Configuration<Boolean> DISABLE_CHECKS = new Configuration("org.lwjgl.util.NoChecks", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> DISABLE_FUNCTION_CHECKS = new Configuration("org.lwjgl.util.NoFunctionChecks", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> DEBUG = new Configuration("org.lwjgl.util.Debug", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> DEBUG_LOADER = new Configuration("org.lwjgl.util.DebugLoader", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Object> DEBUG_STREAM = new Configuration("org.lwjgl.util.DebugStream", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> DEBUG_MEMORY_ALLOCATOR = new Configuration("org.lwjgl.util.DebugAllocator", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> DEBUG_MEMORY_ALLOCATOR_INTERNAL = new Configuration("org.lwjgl.util.DebugAllocator.internal", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> DEBUG_MEMORY_ALLOCATOR_FAST = new Configuration("org.lwjgl.util.DebugAllocator.fast", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> DEBUG_STACK = new Configuration("org.lwjgl.util.DebugStack", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> DEBUG_FUNCTIONS = new Configuration("org.lwjgl.util.DebugFunctions", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> ASSIMP_LIBRARY_NAME = new Configuration("org.lwjgl.assimp.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> ASSIMP_DRACO_LIBRARY_NAME = new Configuration("org.lwjgl.assimp.draco.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> BGFX_LIBRARY_NAME = new Configuration("org.lwjgl.bgfx.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> CUDA_LIBRARY_NAME = new Configuration("org.lwjgl.cuda.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> CUDA_TOOLKIT_VERSION = new Configuration("org.lwjgl.cuda.toolkit.version", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> CUDA_TOOLKIT_PATH = new Configuration("org.lwjgl.cuda.toolkit.path", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> CUDA_NVRTC_LIBRARY_NAME = new Configuration("org.lwjgl.cuda.nvrtc.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> CUDA_NVRTC_BUILTINS_LIBRARY_NAME = new Configuration("org.lwjgl.cuda.nvrtc-builtins.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> CUDA_API_PER_THREAD_DEFAULT_STREAM = new Configuration("org.lwjgl.cuda.ptds", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Boolean> EGL_EXPLICIT_INIT = new Configuration("org.lwjgl.egl.explicitInit", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> EGL_LIBRARY_NAME = new Configuration("org.lwjgl.egl.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> EGL_EXTENSION_FILTER = new Configuration("org.lwjgl.egl.extensionFilter", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> FMOD_LIBRARY_NAME = new Configuration("org.lwjgl.fmod.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> FMOD_STUDIO_LIBRARY_NAME = new Configuration("org.lwjgl.fmod.studio.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> FMOD_FSBANK_LIBRARY_NAME = new Configuration("org.lwjgl.fmod.fsbank.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> FREETYPE_LIBRARY_NAME = new Configuration("org.lwjgl.freetype.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> GLFW_LIBRARY_NAME = new Configuration("org.lwjgl.glfw.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> GLFW_CHECK_THREAD0 = new Configuration("org.lwjgl.glfw.checkThread0", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<Object> HARFBUZZ_LIBRARY_NAME = new Configuration("org.lwjgl.harfbuzz.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> HWLOC_LIBRARY_NAME = new Configuration("org.lwjgl.hwloc.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> JAWT_LIBRARY_NAME = new Configuration("org.lwjgl.system.jawt.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> JEMALLOC_LIBRARY_NAME = new Configuration("org.lwjgl.system.jemalloc.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> KTX_LIBRARY_NAME = new Configuration("org.lwjgl.ktx.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> LLVM_LIBRARY_NAME = new Configuration("org.lwjgl.llvm.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> LLVM_CLANG_LIBRARY_NAME = new Configuration("org.lwjgl.llvm.clang.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> LLVM_LTO_LIBRARY_NAME = new Configuration("org.lwjgl.llvm.lto.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> NFD_LINUX_PORTAL = new Configuration("org.lwjgl.nfd.linux.portal", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> ODBC_LIBRARY_NAME = new Configuration("org.lwjgl.odbc.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> OPENAL_EXPLICIT_INIT = new Configuration("org.lwjgl.openal.explicitInit", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> OPENAL_LIBRARY_NAME = new Configuration("org.lwjgl.openal.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> OPENAL_EXTENSION_FILTER = new Configuration("org.lwjgl.openal.extensionFilter", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> OPENCL_EXPLICIT_INIT = new Configuration("org.lwjgl.opencl.explicitInit", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> OPENCL_LIBRARY_NAME = new Configuration("org.lwjgl.opencl.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> OPENCL_EXTENSION_FILTER = new Configuration("org.lwjgl.opencl.extensionFilter", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> OPENGL_EXPLICIT_INIT = new Configuration("org.lwjgl.opengl.explicitInit", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> OPENGL_LIBRARY_NAME = new Configuration("org.lwjgl.opengl.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> OPENGL_MAXVERSION = new Configuration("org.lwjgl.opengl.maxVersion", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> OPENGL_EXTENSION_FILTER = new Configuration("org.lwjgl.opengl.extensionFilter", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> OPENGLES_EXPLICIT_INIT = new Configuration("org.lwjgl.opengles.explicitInit", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> OPENGLES_LIBRARY_NAME = new Configuration("org.lwjgl.opengles.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> OPENGLES_MAXVERSION = new Configuration("org.lwjgl.opengles.maxVersion", (StateInit)StateInit.STRING);
  
  public static final Configuration<Object> OPENGLES_EXTENSION_FILTER = new Configuration("org.lwjgl.opengles.extensionFilter", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> OPENGLES_CONTEXT_API = new Configuration("org.lwjgl.opengles.contextAPI", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> OPENVR_LIBRARY_NAME = new Configuration("org.lwjgl.openvr.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> OPENXR_EXPLICIT_INIT = new Configuration("org.lwjgl.openxr.explicitInit", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> OPENXR_LIBRARY_NAME = new Configuration("org.lwjgl.openxr.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> OPUS_LIBRARY_NAME = new Configuration("org.lwjgl.opus.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> SHADERC_LIBRARY_NAME = new Configuration("org.lwjgl.shaderc.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<String> SPVC_LIBRARY_NAME = new Configuration("org.lwjgl.spvc.libname", (StateInit)StateInit.STRING);
  
  public static final Configuration<Boolean> VULKAN_EXPLICIT_INIT = new Configuration("org.lwjgl.vulkan.explicitInit", (StateInit)StateInit.BOOLEAN);
  
  public static final Configuration<String> VULKAN_LIBRARY_NAME = new Configuration("org.lwjgl.vulkan.libname", (StateInit)StateInit.STRING);
  
  private final String property;
  
  @Nullable
  private volatile T state;
  
  private static interface StateInit<T> extends Function<String, T> {
    public static final StateInit<Boolean> BOOLEAN;
    
    static {
      BOOLEAN = (property -> {
          String value = System.getProperty(property);
          return (value == null) ? null : Boolean.valueOf(Boolean.parseBoolean(value));
        });
    }
    
    public static final StateInit<Integer> INT = Integer::getInteger;
    
    public static final StateInit<String> STRING = System::getProperty;
  }
  
  Configuration(String property, StateInit<? extends T> init) {
    this.property = property;
    this.state = init.apply(property);
  }
  
  public String getProperty() {
    return this.property;
  }
  
  public void set(@Nullable T value) {
    this.state = value;
  }
  
  @Nullable
  public T get() {
    return this.state;
  }
  
  public T get(T defaultValue) {
    T state = this.state;
    if (state == null)
      state = defaultValue; 
    return state;
  }
}
