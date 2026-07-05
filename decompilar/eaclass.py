package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class ea extends ClickListener {
  ea(dy paramdy, TextField paramTextField) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.b.f.setKeyboardFocus((Actor)this.f);
    Gdx.input.setOnscreenKeyboardVisible(true);
    this.f.setCursorPosition(this.f.getText().length());
  }
}
