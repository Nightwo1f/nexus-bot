package a;

import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Stage;

final class jf extends Action {
  private float bD = this.p.getWidth();
  
  private float bE = this.p.getHeight();
  
  jf(Stage paramStage) {}
  
  public final boolean act(float paramFloat) {
    if (in.n == null)
      return true; 
    if (in.ee != -1 && !in.bj)
      if (!in.s()) {
        in.ee = -1;
      } else {
        in.bK += paramFloat;
        paramFloat = in.bi ? 0.08F : 0.35F;
        if (in.bK >= paramFloat) {
          in.bK = 0.0F;
          in.bi = true;
          if (in.ee == 51 || in.ee == 19) {
            in.an(-1);
          } else if (in.ee == 47 || in.ee == 20) {
            in.an(1);
          } 
        } 
      }  
    paramFloat = in.n.getWidth();
    float f = in.n.getHeight();
    if (this.bD != paramFloat || this.bE != f) {
      this.bD = paramFloat;
      this.bE = f;
      in.cd();
    } 
    return false;
  }
}
