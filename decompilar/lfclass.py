package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.Actor;

public final class lf extends Actor {
  private final int eH;
  
  private final float cj;
  
  private final Color t;
  
  private float ck = 0.0F;
  
  private float cl = 0.0F;
  
  private final Runnable u;
  
  public lf(int paramInt, Color paramColor, float paramFloat1, float paramFloat2, Runnable paramRunnable) {
    this.eH = paramInt;
    this.t = paramColor;
    this.cj = paramFloat1;
    this.cl = paramFloat2;
    this.u = paramRunnable;
  }
  
  public final void act(float paramFloat) {
    super.act(paramFloat);
    if (this.eH == 5)
      return; 
    this.ck += paramFloat;
    if (this.ck >= this.cj) {
      if (this.u != null)
        this.u.run(); 
      remove();
    } 
  }
  
  public final void draw(Batch paramBatch, float paramFloat) {
    float f1 = getX();
    float f2 = getY();
    float f3 = getWidth();
    float f4 = getHeight();
    paramBatch.setColor(Color.WHITE);
    b.a.draw(paramBatch, f1 - 1.0F, f2 - 1.0F, f3 + 2.0F, f4 + 2.0F);
    float f5 = 0.0F;
    if (this.eH == 1) {
      f5 = Math.min(this.ck / this.cj, 1.0F);
      f5 = f3 * f5;
    } else if (this.eH == 4) {
      f5 = Math.min(this.ck / this.cj, 1.0F);
      f5 = f3 * (1.0F - f5);
    } else if (this.eH == 5) {
      f5 = f3 * this.cl;
    } 
    paramBatch.setColor(this.t.r, this.t.g, this.t.b, paramFloat);
    paramBatch.draw((TextureRegion)b.a, f1, f2, f5, f4);
    paramBatch.setColor(Color.WHITE);
  }
}
