package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class ez extends InputListener {
  ez(eu parameu) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 66 || paramInt == 160) {
      this.e.h.setKeyboardFocus(null);
      Gdx.input.setOnscreenKeyboardVisible(false);
      this.e.aF();
      return true;
    } 
    return false;
  }
}
