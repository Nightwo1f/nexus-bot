package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;

public final class lg {
  public final ImageButton[] d;
  
  public final Drawable[] e;
  
  public final Drawable[] f;
  
  private final Actor[] b = new Actor[2];
  
  public final int[] H = new int[2];
  
  public lg(ImageButton[] paramArrayOfImageButton, Drawable[] paramArrayOfDrawable1, Drawable[] paramArrayOfDrawable2) {
    this.d = paramArrayOfImageButton;
    this.e = paramArrayOfDrawable1;
    this.f = paramArrayOfDrawable2;
  }
  
  public final void aq(int paramInt) {
    if ((paramInt -= 101) < 0 || paramInt >= this.d.length)
      return; 
    if (this.b[paramInt] != null) {
      this.b[paramInt].remove();
      this.b[paramInt] = null;
    } 
    this.d[paramInt].setDisabled(false);
  }
  
  public final void s(int paramInt1, int paramInt2, int paramInt3) {
    Color color;
    aq(paramInt1);
    if ((paramInt1 -= 101) < 0 || paramInt1 >= this.d.length)
      return; 
    float f1 = 0.0F;
    float f2 = 0.0F;
    switch (paramInt2) {
      case 1:
        color = Color.RED;
        f1 = paramInt3;
        this.d[paramInt1].setDisabled(true);
        break;
      case 4:
        color = Color.GREEN;
        f1 = paramInt3;
        this.d[paramInt1].setDisabled(true);
        break;
      case 5:
        color = Color.GREEN;
        f2 = MathUtils.clamp(paramInt3 / 100.0F, 0.0F, 1.0F);
        this.d[paramInt1].setDisabled(false);
        break;
      default:
        return;
    } 
    ImageButton imageButton = this.d[paramInt1];
    float f3 = Math.min(6.0F, imageButton.getHeight() * 0.08F);
    lf lf;
    (lf = new lf(paramInt2, color, f1, f2, () -> {
          this.d[paramInt].setDisabled(false);
          this.b[paramInt] = null;
        })).setTouchable(Touchable.disabled);
    lf.setSize(imageButton.getWidth() - 4.0F, f3);
    lf.setPosition(2.0F, 2.0F);
    imageButton.addActor(lf);
    lf.toFront();
    this.b[paramInt1] = lf;
  }
}
