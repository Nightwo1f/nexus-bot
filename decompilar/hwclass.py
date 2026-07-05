package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class hw extends ChangeListener {
  hw(hs paramhs) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    if (this.e.i != null)
      this.e.i.y(); 
    this.e.f(() -> this.e.o.setScreen((Screen)new hy(this.e.o)));
  }
}
