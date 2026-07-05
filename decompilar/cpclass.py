package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class cp extends ClickListener {
  cp(cm paramcm) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (((Gdx.input.isKeyPressed(129) || Gdx.input.isKeyPressed(130))) && paramInt == 31) {
      try {
        Gdx.app.getClipboard().setContents(this.c.R);
      } catch (Throwable throwable) {}
      return true;
    } 
    if (paramInt == 111) {
      try {
        Gdx.app.exit();
      } catch (Throwable throwable) {}
      return true;
    } 
    return false;
  }
}
