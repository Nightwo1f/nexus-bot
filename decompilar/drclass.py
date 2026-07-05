package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class dr extends ClickListener {
  dr(dl paramdl) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.e.cd = (this.e.cd + 1) % 3;
    if (this.e.j != null)
      this.e.a(this.e.j.getWidth(), this.e.j.getHeight()); 
  }
}
