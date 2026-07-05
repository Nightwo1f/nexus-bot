package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.utils.Timer;

final class bt extends Timer.Task {
  bt(br parambr) {}
  
  public final void run() {
    Gdx.app.postRunnable(() -> {
          Screen screen = this.d.b.getScreen();
          be be = null;
          if (screen instanceof fj)
            be = ((fj)screen).i; 
          if (be != null)
            ll.a((cr)this.d.b, (Stage)be, false); 
        });
  }
}
