package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;

final class ir extends InputListener {
  ir(TextField paramTextField, boolean paramBoolean, ju paramju) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    boolean bool;
    if ((bool = (Gdx.input.isKeyPressed(129) || Gdx.input.isKeyPressed(130)) ? true : false) && paramInt == 29) {
      this.l.selectAll();
      return true;
    } 
    if (!this.bl && (paramInt == 66 || paramInt == 160)) {
      if (in.n != null) {
        in.n.setKeyboardFocus(null);
        Gdx.input.setOnscreenKeyboardVisible(false);
      } 
      if (this.b.b.j != null)
        this.b.b.j.run(); 
      in.g(null);
      return true;
    } 
    if (this.bl && bool && (paramInt == 66 || paramInt == 160)) {
      if (in.n != null) {
        in.n.setKeyboardFocus(null);
        Gdx.input.setOnscreenKeyboardVisible(false);
      } 
      if (this.b.b.j != null)
        this.b.b.j.run(); 
      in.g(null);
      return true;
    } 
    return false;
  }
}
