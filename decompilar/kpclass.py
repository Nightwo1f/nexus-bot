package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class kp extends ClickListener {
  private boolean bF = false;
  
  private float cg;
  
  private float ch;
  
  kp(kg paramkg, Runnable paramRunnable) {}
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    this.bF = false;
    this.cg = paramInputEvent.getStageX();
    this.ch = paramInputEvent.getStageY();
    return super.touchDown(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void touchDragged(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    if (!this.bF) {
      paramFloat1 = Math.abs(paramInputEvent.getStageX() - this.cg);
      float f = Math.abs(paramInputEvent.getStageY() - this.ch);
      this.bF = (paramFloat1 > 10.0F || f > 10.0F);
    } 
  }
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (!this.bF && this.t != null)
      this.t.run(); 
  }
}
