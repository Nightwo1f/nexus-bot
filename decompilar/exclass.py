package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class ex extends ClickListener {
  ex(eu parameu, TextField paramTextField) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (paramInputEvent.getTarget() instanceof com.badlogic.gdx.scenes.scene2d.ui.ImageButton || paramInputEvent.getTarget().getParent() instanceof com.badlogic.gdx.scenes.scene2d.ui.ImageButton)
      return; 
    this.c.h.setKeyboardFocus((Actor)this.h);
    Gdx.input.setOnscreenKeyboardVisible(true);
    this.h.setCursorPosition(this.h.getText().length());
  }
}
