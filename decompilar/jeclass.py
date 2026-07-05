package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.Value;

final class je extends Value {
  je(Table paramTable, float paramFloat) {}
  
  public final float get(Actor paramActor) {
    return this.C.isVisible() ? this.bS : 0.0F;
  }
}
