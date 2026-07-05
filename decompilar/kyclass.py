package a;

import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Table;

final class ky extends Action {
  private float bD = this.u.getViewport().getWorldWidth();
  
  private float bE = this.u.getViewport().getWorldHeight();
  
  ky(Stage paramStage, Table paramTable, boolean paramBoolean) {}
  
  public final boolean act(float paramFloat) {
    if (kx.m != null && kx.m.getStage() != null) {
      kx.m.toFront();
      kx.m.setZIndex((kx.m.getStage().getRoot().getChildren()).size - 1);
    } 
    if (this.N.getParent() != null) {
      this.N.toFront();
      this.N.setZIndex((this.N.getParent().getChildren()).size - 1);
      paramFloat = this.u.getViewport().getWorldWidth();
      float f = this.u.getViewport().getWorldHeight();
      if (this.bD != paramFloat || this.bE != f) {
        this.bD = paramFloat;
        this.bE = f;
        float f1 = (fj.au > 0.0F) ? fj.au : (paramFloat / 2.0F);
        float f2 = this.N.getWidth();
        float f3 = this.N.getHeight();
        if (this.bH) {
          f1 -= f2 / 2.0F;
          f1 = Math.max(10.0F, Math.min(f1, paramFloat - f2 - 10.0F));
          this.N.setPosition(Math.round(f1), Math.round((f - f3) / 2.0F));
        } else {
          f1 -= f2 / 2.0F;
          paramFloat = (f - f3) * 0.4F;
          this.N.setPosition(Math.round(f1), Math.round(paramFloat));
        } 
      } 
    } 
    return false;
  }
}
