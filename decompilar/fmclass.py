package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import java.util.Comparator;
import java.util.List;

final class fm extends ClickListener {
  fm(fj paramfj, be parambe) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.f.b.clear();
    this.f.f.clear();
    this.f.c = (Comparator)this.k;
    this.f.av = true;
    List list;
    if ((list = this.f.a.a(this.f.h.a(), this.k)) != null)
      this.f.b.addAll(list); 
    this.f.aL();
  }
}
