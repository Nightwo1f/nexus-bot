package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class cn extends ClickListener {
  cn(cm paramcm) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    try {
      Gdx.app.getClipboard().setContents(this.a.R);
      return;
    } catch (Throwable throwable) {
      return;
    } 
  }
}
