package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class dc extends ClickListener {
  dc(cx paramcx) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.e.c.setKeyboardFocus(null);
    Gdx.input.setOnscreenKeyboardVisible(false);
  }
}
