package a;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class ht extends InputListener {
  ht(hs paramhs, bf parambf, cr paramcr) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 111 || paramInt == 4) {
      al.a(3);
      if (this.j != null)
        this.j.y(); 
      this.b.f(() -> paramcr.setScreen((Screen)new hy(paramcr)));
      return true;
    } 
    return false;
  }
}
