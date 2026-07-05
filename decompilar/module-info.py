module org.lwjgl.glfw {
  requires java.base;
  requires transitive org.lwjgl;
  requires org.lwjgl.egl;
  requires org.lwjgl.opengl;
  requires org.lwjgl.vulkan;
  
  exports org.lwjgl.glfw;
}
