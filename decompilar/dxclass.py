package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class dx extends InputListener {
  dx(dw paramdw, dl paramdl) {}
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    if (this.b.ah)
      this.b.az(); 
    this.b.ai = true;
    this.b.ap = 0.0F;
    this.b.b(paramFloat1, paramFloat2);
    return true;
  }
  
  public final void touchDragged(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    this.b.b(paramFloat1, paramFloat2);
  }
  
  public final void touchUp(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    this.b.ai = false;
    this.b.aq = 0.0F;
    this.b.ar = 0.0F;
    if (this.b.ah)
      return; 
    this.b.az();
  }
}
