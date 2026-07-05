package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class ia extends ChangeListener {
  ia(hy paramhy) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    if (this.b.ci < 0 || this.b.ci >= this.b.y.size())
      return; 
    al.a(3);
    ck ck = this.b.y.get(this.b.ci);
    this.b.q.setScreen((Screen)new eu(this.b.q, ck.L, ck.bv, this.b.n, this.b.k));
  }
}
