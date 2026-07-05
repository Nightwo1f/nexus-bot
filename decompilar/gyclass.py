package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gy extends ClickListener {
  gy(gb paramgb) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (this.x.a != hp.c)
      return; 
    this.x.bn();
    this.x.aQ = true;
    this.x.i.setText("");
    this.x.b.setVisible(true);
    this.x.i.setVisible(true);
    this.x.i.setDisabled(false);
    this.x.bi();
    this.x.bk();
    this.x.bj();
    this.x.bn();
    this.x.j.setKeyboardFocus((Actor)this.x.i);
  }
}
