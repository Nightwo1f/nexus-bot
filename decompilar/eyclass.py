package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class ey extends ClickListener {
  ey(eu parameu) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    Actor actor = paramInputEvent.getTarget();
    while (actor != null) {
      if (actor instanceof com.badlogic.gdx.scenes.scene2d.ui.TextField)
        return; 
      if ("INPUT_WRAPPER".equals(actor.getName()))
        return; 
      Group group = actor.getParent();
    } 
    this.d.h.setKeyboardFocus(null);
    Gdx.input.setOnscreenKeyboardVisible(false);
  }
}
