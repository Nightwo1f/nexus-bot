package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import java.util.Comparator;
import java.util.List;

final class fn extends ClickListener {
  fn(fj paramfj, be parambe) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.g.b.clear();
    this.g.f.clear();
    this.g.av = false;
    this.g.c = (Comparator)this.l;
    this.g.e = this.g.d(this.l) ? this.l : null;
    List list;
    if ((list = this.g.a.a(this.g.h.a(), this.l, true)) != null)
      this.g.b.addAll(list); 
    this.g.aL();
  }
}
