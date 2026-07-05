package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;

final class fi extends FocusListener {
  fi(eu parameu, TextField.TextFieldStyle paramTextFieldStyle1, TextField.TextFieldStyle paramTextFieldStyle2, Table paramTable) {}
  
  public final void keyboardFocusChanged(FocusListener.FocusEvent paramFocusEvent, Actor paramActor, boolean paramBoolean) {
    this.n.g.setStyle(paramBoolean ? this.q : this.r);
    this.l.setBackground((Drawable)new NinePatchDrawable(paramBoolean ? b.A : b.z));
  }
}
