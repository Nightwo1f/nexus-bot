package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.utils.Timer;

final class bu extends Timer.Task {
  bu(br parambr) {}
  
  public final void run() {
    if (this.e.z) {
      this.e.z = false;
      Gdx.app.postRunnable(() -> {
            Screen screen;
            if (screen = this.e.b.getScreen() instanceof fj)
              ((fj)screen).i(true); 
          });
    } 
  }
}
