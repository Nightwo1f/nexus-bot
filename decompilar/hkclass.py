package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class hk extends ClickListener {
  hk(gb paramgb) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.I.a = (boolean[])hp.c;
    this.I.bl();
    if (this.I.aj == null) {
      this.I.aQ = true;
      this.I.au();
    } else {
      this.I.aQ = false;
      this.I.au();
    } 
    this.I.bi();
    this.I.bk();
    this.I.bn();
  }
}
