package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class id extends InputListener {
  id(hy paramhy, int paramInt) {}
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    paramInputEvent.stop();
    al.a(3);
    cv.a(this.e.q, this.e.l, () -> {
          this.e.y.remove(paramInt);
          this.e.q.f.n.remove(paramInt);
          cj.f(this.e.q.f);
          if (this.e.ci == paramInt)
            this.e.ci = -1; 
          if (this.e.ci > paramInt)
            this.e.ci--; 
          hy hy1;
          if ((hy1 = this.e).s == null) {
            hy1.bY();
            return;
          } 
          hy1.z.clear();
          hy1.s.clearChildren();
          hy1.bY();
        });
    return true;
  }
}
