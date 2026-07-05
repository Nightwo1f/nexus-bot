package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;
import com.badlogic.gdx.scenes.scene2d.Stage;

final class cw extends InputListener {
  cw(Stage paramStage, cr paramcr, ct paramct) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (paramInt == 111) {
      cv.a(this.b);
      cv.b(this.d, this.b);
      return true;
    } 
    cu.a(this.s, paramInt);
    cj.f(this.d.f);
    cv.a(this.b);
    cv.b(this.d, this.b);
    return true;
  }
}
