package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class hu extends ChangeListener {
  hu(hs paramhs) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(2);
    if (this.c.i != null)
      this.c.i.y(); 
    this.c.f(() -> this.c.o.setScreen((Screen)new hy(this.c.o)));
  }
}
