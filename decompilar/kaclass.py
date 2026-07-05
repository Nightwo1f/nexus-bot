package a;

import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Stage;

public final class ka extends Action {
  private float bD = this.r.getWidth();
  
  private float bE = this.r.getHeight();
  
  public ka(jz paramjz, Stage paramStage) {}
  
  public final boolean act(float paramFloat) {
    if (this.c.l == null)
      return true; 
    paramFloat = this.r.getWidth();
    float f = this.r.getHeight();
    this.bD = paramFloat;
    this.bE = f;
    Stage stage = this.r;
    jz jz1;
    if ((this.bD != paramFloat || this.bE != f) && (jz1 = this.c).l != null && jz1.F != null && jz1.f != null) {
      float f2 = stage.getWidth();
      float f1 = stage.getHeight();
      jz1.f.setSize(f2, f1);
      if (jz1.bD) {
        f3 = f2 * 0.95F;
        f4 = f1 * 0.9F;
      } else {
        f3 = Math.min(560.0F, f2 * 0.95F);
        f4 = Math.min(510.0F, f1 * 0.95F);
      } 
      float f3 = Math.round(f3);
      float f4 = Math.round(f4);
      jz1.F.setSize(f3, f4);
      jz1.F.clearActions();
      f2 = Math.round((f2 - f3) * 0.5F);
      f1 = Math.round((f1 - f4) * 0.5F);
      jz1.F.setPosition(f2, f1);
      jz1.F.invalidateHierarchy();
    } 
    return false;
  }
}
