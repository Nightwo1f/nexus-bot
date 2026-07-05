package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class ec extends InputListener {
  ec(dy paramdy) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 66 || paramInt == 160) {
      this.d.f.setKeyboardFocus(null);
      Gdx.input.setOnscreenKeyboardVisible(false);
      this.d.aA();
      return true;
    } 
    return false;
  }
}
