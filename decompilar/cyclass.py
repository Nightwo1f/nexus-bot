package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class cy extends InputListener {
  cy(cx paramcx, cr paramcr) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 111 || paramInt == 4) {
      al.a(3);
      this.a.a(() -> paramcr.setScreen((Screen)new hy(paramcr)));
      return true;
    } 
    if (paramInt == 66 || paramInt == 160) {
      this.a.c.setKeyboardFocus(null);
      Gdx.input.setOnscreenKeyboardVisible(false);
      this.a.am();
      return true;
    } 
    return false;
  }
}
