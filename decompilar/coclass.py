package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class co extends ClickListener {
  co(cm paramcm) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    try {
      Gdx.app.exit();
      return;
    } catch (Throwable throwable) {
      return;
    } 
  }
}
