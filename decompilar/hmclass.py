package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener;

final class hm extends FocusListener {
  hm(gb paramgb) {}
  
  public final void keyboardFocusChanged(FocusListener.FocusEvent paramFocusEvent, Actor paramActor, boolean paramBoolean) {
    if (paramActor == this.K.i) {
      this.K.i.setStyle(paramBoolean ? this.K.t : this.K.s);
      this.K.i.invalidate();
      this.K.bk();
      this.K.bj();
    } 
  }
}
