package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class cz extends ClickListener {
  cz(cx paramcx, TextField paramTextField) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.b.c.setKeyboardFocus((Actor)this.c);
    Gdx.input.setOnscreenKeyboardVisible(true);
    this.c.setCursorPosition(this.c.getText().length());
  }
}
