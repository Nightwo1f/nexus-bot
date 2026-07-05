package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gh extends ClickListener {
  gh(gb paramgb) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (!this.g.i.isVisible()) {
      this.g.at();
      return;
    } 
    this.g.bm();
  }
}
