package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class db extends InputListener {
  db(cx paramcx) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 66 || paramInt == 160) {
      this.d.c.setKeyboardFocus(null);
      Gdx.input.setOnscreenKeyboardVisible(false);
      this.d.am();
      return true;
    } 
    return false;
  }
}
