package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class ic extends ChangeListener {
  ic(hy paramhy) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.d.q.setScreen((Screen)new cx(this.d.q, this.d.n, this.d.k));
  }
}
