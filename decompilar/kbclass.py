package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

public final class kb extends InputListener {
  public kb(jz paramjz) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 111 || paramInt == 4) {
      this.d.cm();
      return true;
    } 
    return false;
  }
}
