package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class km extends ClickListener {
  km(kg paramkg, Runnable paramRunnable) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (this.s != null)
      this.s.run(); 
  }
}
