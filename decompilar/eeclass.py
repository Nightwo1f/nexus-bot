package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class ee extends ChangeListener {
  ee(dy paramdy) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.f.b(() -> this.f.g.setScreen((Screen)new em((cr)this.f.g, this.f.h, (bf)this.f.d)));
  }
}
