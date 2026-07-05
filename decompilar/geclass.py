package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class ge extends ClickListener {
  ge(gb paramgb) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    Actor actor = paramInputEvent.getTarget();
    if (!gb.a(actor, (Actor)this.d.b))
      if (!gb.a(actor, (Actor)this.d.i)) {
        if (!actor.isDescendantOf((Actor)this.d.d))
          if (!gb.a(actor, (Actor)this.d.d)) {
            if (this.d.b.isVisible()) {
              al.a(3);
              this.d.av();
              return;
            } 
            al.a(3);
            this.d.au();
            return;
          }  
        return;
      }  
  }
}
