package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class ew extends InputListener {
  ew(eu parameu) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (((Gdx.input.isKeyPressed(129) || Gdx.input.isKeyPressed(130))) && paramInt == 29) {
      this.b.g.selectAll();
      return true;
    } 
    return false;
  }
}
