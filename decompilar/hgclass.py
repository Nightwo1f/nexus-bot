package a;

import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class hg extends InputListener {
  hg(gb paramgb) {}
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    if (paramInt2 == 0) {
      this.F.aO = true;
      this.F.aP = true;
      this.F.bz = paramFloat1;
      this.F.bA = paramFloat2;
      return true;
    } 
    if (paramInt2 == 2) {
      this.F.dA = ((cq)this.F.j).aF;
      this.F.dy = ((cq)this.F.j).aD;
      this.F.dz = ((cq)this.F.j).aE;
      this.F.bD();
      return true;
    } 
    return false;
  }
  
  public final void touchDragged(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    if (!this.F.aO)
      return; 
    float f;
    if ((f = this.F.g.getWidth()) <= 1.0F)
      return; 
    paramInt = this.F.dx * 2 + 1;
    f /= paramInt;
    paramFloat1 -= this.F.bz;
    paramFloat2 -= this.F.bA;
    if (this.F.aP && (Math.abs(paramFloat1) > 8.0F || Math.abs(paramFloat2) > 8.0F))
      this.F.aP = false; 
    int i = MathUtils.round(-paramFloat1 / f);
    int j = MathUtils.round(paramFloat2 / f);
    if (i == 0 && j == 0)
      return; 
    this.F.dy += i;
    this.F.dz += j;
    this.F.bz += -i * f;
    this.F.bA += j * f;
    this.F.bD();
  }
  
  public final void touchUp(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    if (paramInt2 != 0)
      return; 
    boolean bool = this.F.aP;
    this.F.aP = false;
    this.F.aO = false;
    if (!bool)
      return; 
    be be = this.F.a(paramFloat1, paramFloat2);
    if (this.F.e(be)) {
      this.F.bB();
      return;
    } 
    this.F.e(be);
    if (this.F.a != null)
      this.F.a.accept(be); 
  }
}
