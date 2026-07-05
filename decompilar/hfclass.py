package a;

import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class hf extends ClickListener {
  hf(gb paramgb) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    int i = MathUtils.clamp(25, 5, 60);
    int j = MathUtils.clamp(40, 5, 60);
    int k = MathUtils.clamp(60, 5, 60);
    if (j < i)
      j = i; 
    if (k < j)
      k = j; 
    int m;
    if ((m = this.E.dx) <= i) {
      i = k;
    } else if (m > j) {
      i = j;
    } 
    this.E.ah(i);
  }
}
