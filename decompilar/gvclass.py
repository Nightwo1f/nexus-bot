package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gv extends ClickListener {
  gv(gb paramgb) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.u.j.setVisible(false);
    this.u.aZ = false;
    this.u.bu();
  }
}
