package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class jh extends ClickListener {
  jh(Runnable paramRunnable) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    al.a(3);
    if (this.d != null)
      this.d.run(); 
  }
}
