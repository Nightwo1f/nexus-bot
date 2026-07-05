package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class lo extends ClickListener {
  lo(cr paramcr) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    ll.cg();
    try {
      if (this.u.a != null) {
        if (this.u.a.a() != null)
          this.u.a.a().N(); 
        if (this.u.a.a() != null)
          this.u.a.a().y(); 
      } 
    } catch (Throwable throwable) {}
    this.u.setScreen((Screen)new hy(this.u));
  }
}
