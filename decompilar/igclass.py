package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class ig extends ChangeListener {
  ig(hy paramhy, TextButton paramTextButton, String paramString) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.g.setDisabled(true);
    String str;
    if ((str = b.a(this.ao, "id_update_connecting")) == null)
      str = "Connecting..."; 
    this.g.setText(str);
    this.h.a(this.g);
  }
}
