package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class eo extends ChangeListener {
  eo(em paramem) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.b.c(() -> this.b.i.setScreen((Screen)new hy(this.b.i)));
  }
}
