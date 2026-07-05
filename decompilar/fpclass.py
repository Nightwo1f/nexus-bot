package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import java.util.Comparator;
import java.util.List;

final class fp extends ClickListener {
  fp(fj paramfj, be parambe, az paramaz) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.i.aL();
    if (((cq)this.i.h).aa) {
      this.i.aX();
      this.i.b.clear();
      this.i.f.clear();
      this.i.av = false;
      this.i.e = null;
      this.i.f = null;
      be be1 = this.i.h.a();
      be be2;
      if ((be2 = this.i.a(be1, this.n)) != null) {
        if (!be2.equals(be1)) {
          List list;
          if ((list = this.i.a.a(be1, be2)) == null || !be2.equals(fj.a(be1, list))) {
            this.i.aw = false;
            this.i.d = null;
            return;
          } 
          this.i.c = (Comparator)be2;
          this.i.b.clear();
          this.i.b.addAll(list);
        } else {
          this.i.c = null;
          this.i.b.clear();
        } 
        this.i.aw = true;
        this.i.d = (Comparator)this.n;
      } 
      return;
    } 
    this.i.aX();
    try {
      this.i.l.C(this.a.ag);
      return;
    } catch (Exception exception) {
      Gdx.app.error("GameScreen", "Falha ao enviar ataque Ranged", exception);
      return;
    } 
  }
}
