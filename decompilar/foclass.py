package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import java.util.Comparator;
import java.util.List;

final class fo extends ClickListener {
  fo(fj paramfj, be parambe) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.h.aX();
    this.h.b.clear();
    this.h.f.clear();
    this.h.av = false;
    this.h.e = null;
    this.h.f = null;
    this.h.aw = true;
    this.h.d = (Comparator)this.m;
    be be1 = this.h.h.a();
    be be2;
    if ((be2 = this.h.a(be1, this.m)) != null) {
      if (!be2.equals(be1)) {
        List list;
        if ((list = this.h.a.a(be1, be2)) == null || !be2.equals(fj.a(be1, list))) {
          this.h.aw = false;
          this.h.d = null;
          this.h.aL();
          return;
        } 
        this.h.c = (Comparator)be2;
        this.h.b.clear();
        this.h.b.addAll(list);
      } else {
        this.h.c = null;
        this.h.b.clear();
      } 
      this.h.aw = true;
      this.h.d = (Comparator)this.m;
    } 
    this.h.aL();
  }
}
