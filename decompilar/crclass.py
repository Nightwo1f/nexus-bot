package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;

public final class cr extends Game {
  public hs a;
  
  public final cq f = new cq();
  
  public final ax a;
  
  public cs a = (cs)new ax(this.f, this);
  
  public final void create() {
    cl.a(this);
    cj.d(this.f);
    this.f.ag();
    try {
      Gdx.graphics.setWindowedMode(this.f.a, this.f.b);
    } catch (Throwable throwable) {
      Gdx.app.error("Jtme", "Falha ao aplicar resolu, throwable);
    } 
    b.a();
    b.a(this.f);
    setScreen((Screen)new ij(this));
    Gdx.app.postRunnable(() -> {
          try {
            Class<?> clazz;
            if ((clazz = Class.forName("com.badlogic.gdx.backends.lwjgl3.Lwjgl3Graphics")).isInstance(Gdx.graphics)) {
              Object object;
              (object = clazz.getMethod("getWindow", new Class[0]).invoke(Gdx.graphics, new Object[0])).getClass().getMethod("setVisible", new Class[] { boolean.class }).invoke(object, new Object[] { Boolean.TRUE });
              long l = ((Long)object.getClass().getMethod("getWindowHandle", new Class[0]).invoke(object, new Object[0])).longValue();
              Class.forName("org.lwjgl.glfw.GLFW").getMethod("glfwSetWindowSizeLimits", new Class[] { long.class, int.class, int.class, int.class, int.class }).invoke(null, new Object[] { Long.valueOf(l), Integer.valueOf(800), Integer.valueOf(600), Integer.valueOf(-1), Integer.valueOf(-1) });
            } 
            return;
          } catch (Throwable throwable) {
            return;
          } 
        });
  }
  
  public final void render() {
    try {
      super.render();
      return;
    } catch (Throwable throwable) {
      cl.a(this, Thread.currentThread(), throwable);
      return;
    } 
  }
  
  public final void dispose() {
    if (Gdx.app.getType() == Application.ApplicationType.Desktop) {
      int i = Gdx.graphics.getWidth();
      int j = Gdx.graphics.getHeight();
      if (i >= 800 && j >= 600) {
        this.f.L(i);
        this.f.M(j);
        cj.f(this.f);
      } 
    } 
    super.dispose();
    b.d();
  }
}
