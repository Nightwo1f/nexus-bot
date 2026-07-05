package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class eg extends ChangeListener {
  eg(dy paramdy) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.h.b(() -> this.h.g.setScreen((Screen)new em((cr)this.h.g, this.h.h, (bf)this.h.d)));
  }
}
