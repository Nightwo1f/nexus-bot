package META-INF.versions.9.org.lwjgl;

import java.lang.module.ModuleDescriptor;
import org.lwjgl.Version;

final class VersionImpl {
  static String find() {
    Package org_lwjgl = Version.class.getPackage();
    String specVersion = org_lwjgl.getSpecificationVersion();
    String implVersion = org_lwjgl.getImplementationVersion();
    if (specVersion != null && implVersion != null)
      return Version.createImplementation(specVersion, implVersion); 
    Module module = Version.class.getModule();
    if ("org.lwjgl".equals(module.getName())) {
      String moduleVersion = module.getDescriptor().version().map(ModuleDescriptor.Version::toString).orElse(null);
      if (moduleVersion != null) {
        int plusIndex = moduleVersion.indexOf('+');
        if (plusIndex != -1)
          return Version.createImplementation(moduleVersion
              .substring(0, plusIndex), moduleVersion
              .substring(plusIndex + 1)); 
      } 
    } 
    String version = Version.findImplementationFromManifest();
    if (version != null)
      return version; 
    return "-snapshot";
  }
}
