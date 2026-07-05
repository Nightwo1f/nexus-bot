package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class jc extends ClickListener {
  jc(ju paramju) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    al.a(3);
    if (in.x != null && in.x.isVisible()) {
      in.ch();
      return;
    } 
    if (in.u != null && in.u.isVisible()) {
      in.ci();
      return;
    } 
    if (this.c.n != null)
      in.h(this.c.n); 
  }
}
