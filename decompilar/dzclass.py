package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class dz extends InputListener {
  dz(dy paramdy, cr paramcr, br parambr, bf parambf) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 111 || paramInt == 4) {
      al.a(3);
      this.a.b(() -> paramcr.setScreen((Screen)new em(paramcr, parambr, parambf)));
      return true;
    } 
    if (paramInt == 66 || paramInt == 160) {
      this.a.f.setKeyboardFocus(null);
      Gdx.input.setOnscreenKeyboardVisible(false);
      this.a.aA();
      return true;
    } 
    return false;
  }
}
