package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class fa extends ClickListener {
  fa(eu parameu) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.f.h.setKeyboardFocus(null);
    Gdx.input.setOnscreenKeyboardVisible(false);
  }
}
