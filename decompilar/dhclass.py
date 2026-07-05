package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class dh extends ChangeListener {
  dh(cx paramcx) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.j.a(() -> this.j.e.setScreen((Screen)new hy(this.j.e)));
  }
}
