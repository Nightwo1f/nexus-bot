package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

public final class ki extends InputListener {
  public ki(kg paramkg, kr paramkr) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 111 || paramInt == 4) {
      if (this.a.L.isVisible()) {
        kg.a(this.a);
      } else {
        this.d.cq();
      } 
      return true;
    } 
    return false;
  }
}
