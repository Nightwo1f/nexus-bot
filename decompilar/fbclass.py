package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class fb extends ChangeListener {
  fb(eu parameu) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    if (this.g.g != null)
      this.g.g.y(); 
    this.g.d(() -> this.g.k.setScreen((Screen)new hy((cr)this.g.k)));
  }
}
