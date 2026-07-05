package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gi extends ClickListener {
  gi(gb paramgb) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (paramInputEvent.getButton() != 0)
      return; 
    al.a(3);
    this.h.by();
  }
}
