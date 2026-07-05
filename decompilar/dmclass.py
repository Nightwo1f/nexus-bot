package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class dm extends ClickListener {
  dm(dl paramdl, cq paramcq, br parambr, Stage paramStage) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.a.af = false;
    ((cq)this.g).j = (float[])this.a.l.clone();
    ((cq)this.g).k = (float[])this.a.m.clone();
    ((cq)this.g).K = true;
    cj.f((cq)this.g);
    this.g.g(b.a(((cq)this.g).S, "id_msg_layout_saved"));
    this.a.a(this.d.getWidth(), this.d.getHeight());
  }
}
