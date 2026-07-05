package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class gd extends InputListener {
  gd(gb paramgb) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 66) {
      this.c.y(this.c.i.getText());
      return true;
    } 
    if (((Gdx.input.isKeyPressed(129) || Gdx.input.isKeyPressed(130))) && paramInt == 29) {
      this.c.i.selectAll();
      return true;
    } 
    return false;
  }
}
