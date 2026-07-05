package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class fe extends ChangeListener {
  fe(eu parameu) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    if (this.j.g != null)
      this.j.g.y(); 
    this.j.d(() -> this.j.k.setScreen((Screen)new hy((cr)this.j.k)));
  }
}
