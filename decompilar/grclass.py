package a;

import com.badlogic.gdx.scenes.scene2d.Action;

final class gr extends Action {
  private float bD = -1.0F;
  
  private float bE = -1.0F;
  
  gr(gb paramgb) {}
  
  public final boolean act(float paramFloat) {
    if (this.q.j == null || this.q.j.getViewport() == null)
      return false; 
    paramFloat = this.q.j.getViewport().getWorldWidth();
    float f = this.q.j.getViewport().getWorldHeight();
    if (this.bD != paramFloat || this.bE != f) {
      this.bD = paramFloat;
      this.bE = f;
      this.q.d(paramFloat, f);
    } 
    return false;
  }
}
