package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.Value;

public final class kd extends Value {
  public kd(jz paramjz, float paramFloat) {}
  
  public final float get(Actor paramActor) {
    return (paramActor.getParent() == null) ? 100.0F : ((paramActor.getParent().getHeight() - this.cc) * 0.3F);
  }
}
