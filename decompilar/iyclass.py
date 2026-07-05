package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class iy extends InputListener {
  iy(Runnable paramRunnable) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 111 || paramInt == 4) {
      if (this.b != null)
        this.b.run(); 
      return true;
    } 
    return false;
  }
}
