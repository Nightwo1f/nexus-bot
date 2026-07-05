package META-INF.versions.16.org.lwjgl.system;

import org.lwjgl.system.APIUtil;
import org.lwjgl.system.MemoryUtil;

final class MultiReleaseMemCopy {
  static {
    APIUtil.apiLog("Java 16 memcpy enabled");
  }
  
  static void copy(long src, long dst, long bytes) {
    MemoryUtil.UNSAFE.copyMemory(null, src, null, dst, bytes);
  }
}
