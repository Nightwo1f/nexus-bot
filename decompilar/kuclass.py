package a;

import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Table;

final class ku extends Action {
  private float bD = this.t.getViewport().getWorldWidth();
  
  private float bE = this.t.getViewport().getWorldHeight();
  
  ku(Stage paramStage, Table paramTable, boolean paramBoolean) {}
  
  public final boolean act(float paramFloat) {
    if (kt.m != null && kt.m.getStage() != null) {
      kt.m.toFront();
      kt.m.setZIndex((kt.m.getStage().getRoot().getChildren()).size - 1);
    } 
    if (this.M.getParent() != null) {
      this.M.toFront();
      this.M.setZIndex((this.M.getParent().getChildren()).size - 1);
      paramFloat = this.t.getViewport().getWorldWidth();
      float f = this.t.getViewport().getWorldHeight();
      if (this.bD != paramFloat || this.bE != f) {
        this.bD = paramFloat;
        this.bE = f;
        float f1 = (fj.au > 0.0F) ? fj.au : (paramFloat / 2.0F);
        float f2 = this.M.getWidth();
        float f3 = this.M.getHeight();
        if (this.bG) {
          f1 -= f2 / 2.0F;
          f1 = Math.max(10.0F, Math.min(f1, paramFloat - f2 - 10.0F));
          if ((paramFloat = f * 0.5F - f3 / 2.0F) < 10.0F)
            paramFloat = 10.0F; 
          this.M.setPosition(Math.round(f1), Math.round(paramFloat));
        } else {
          f1 -= f2 / 2.0F;
          paramFloat = (f - f3) / 2.0F - 90.0F;
          this.M.setPosition(Math.round(f1), Math.round(paramFloat));
        } 
      } 
    } 
    return false;
  }
}
