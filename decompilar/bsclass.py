package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.utils.Timer;

final class bs extends Timer.Task {
  bs(br parambr) {}
  
  public final void run() {
    Gdx.app.postRunnable(() -> {
          Screen screen = this.c.b.getScreen();
          be be = null;
          if (screen instanceof fj)
            be = ((fj)screen).i; 
          if (be != null)
            ll.a((cr)this.c.b, (Stage)be, false); 
        });
  }
}
