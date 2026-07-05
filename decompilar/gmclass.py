package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gm extends ClickListener {
  gm(gb paramgb, int paramInt1, int paramInt2) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    try {
      al.a(3);
      if (this.dG == 0) {
        int i = this.dH;
        Label label = this.l.m;
        il il;
        (il = new il()).aj(111);
        il.aj(i);
        label.b(il.a());
      } else if (this.dG == 1) {
        int i = this.dH;
        Label label = this.l.m;
        il il;
        (il = new il()).aj(131);
        il.aj(i);
        label.b(il.a());
      } else {
        this.l.m.A(this.dH);
      } 
    } catch (Exception exception) {}
    this.l.br();
  }
}
