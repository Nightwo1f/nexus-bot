package a;

import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Stage;

public final class kh extends Action {
  private float bD = this.s.getWidth();
  
  private float bE = this.s.getHeight();
  
  public kh(kg paramkg, Stage paramStage) {}
  
  public final boolean act(float paramFloat) {
    if (this.c.l == null)
      return true; 
    paramFloat = this.s.getWidth();
    float f = this.s.getHeight();
    this.bD = paramFloat;
    this.bE = f;
    Stage stage = this.s;
    kg kg1;
    if ((this.bD != paramFloat || this.bE != f) && (kg1 = this.c).l != null && kg1.F != null && kg1.f != null) {
      float f2 = stage.getWidth();
      float f1 = stage.getHeight();
      kg1.cd = f2;
      kg1.ce = f1;
      kg1.f.setSize(f2, f1);
      if (kg1.aL) {
        f3 = f2 * 0.95F;
        f4 = f1 * 0.9F;
      } else {
        f3 = Math.min(560.0F, f2 * 0.95F);
        f4 = Math.min(510.0F, f1 * 0.95F);
      } 
      float f3 = Math.round(f3);
      float f4 = Math.round(f4);
      kg1.F.setSize(f3, f4);
      kg1.F.clearActions();
      kg1.F.setPosition(Math.round((f2 - f3) * 0.5F), Math.round((f1 - f4) * 0.5F));
      kg1.F.invalidateHierarchy();
    } 
    return false;
  }
}
