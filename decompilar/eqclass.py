package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class eq extends ChangeListener {
  eq(em paramem) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.d.c(() -> this.d.i.setScreen((Screen)new hy(this.d.i)));
  }
}
