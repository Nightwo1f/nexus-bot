package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class ib extends ChangeListener {
  ib(hy paramhy) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.c.q.setScreen((Screen)new em(this.c.q, this.c.n, this.c.k));
  }
}
