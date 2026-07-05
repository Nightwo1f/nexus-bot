package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class dd extends ChangeListener {
  dd(cx paramcx) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.f.a(() -> this.f.e.setScreen((Screen)new hy(this.f.e)));
  }
}
