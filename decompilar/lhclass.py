package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.Touchable;

public final class lh extends Actor {
  private final String aP;
  
  private final Runnable v;
  
  float cm = 1.0F;
  
  float cn = 1.0F;
  
  final Color u = new Color(1.0F, 1.0F, 1.0F, 1.0F);
  
  boolean bJ = false;
  
  TextureRegion I = null;
  
  private boolean bK = false;
  
  private float co = 0.0F;
  
  private float cp = 0.0F;
  
  public lh(String paramString, Runnable paramRunnable) {
    this.aP = paramString;
    this.v = paramRunnable;
    setTouchable(Touchable.disabled);
  }
  
  public final boolean u() {
    return (this.I != null);
  }
  
  public final void m(boolean paramBoolean) {
    this.bK = paramBoolean;
    this.co = 20.0F;
    this.cp = 1.0F;
  }
  
  public final void act(float paramFloat) {
    super.act(paramFloat);
    if (this.bJ)
      return; 
    this.cn -= paramFloat;
    if (this.cn <= 0.0F) {
      this.bJ = true;
      if (this.v != null)
        this.v.run(); 
    } 
  }
  
  public final void draw(Batch paramBatch, float paramFloat) {
    float f1 = getX();
    float f2 = getY();
    float f3 = getWidth();
    float f4 = getHeight();
    float f5 = Math.max(0.0F, Math.min(1.0F, this.cn / this.cm));
    float f6 = this.bK ? (this.co + this.cp) : 0.0F;
    if (this.I != null) {
      float f = f2 + (f4 - this.co) / 2.0F;
      paramBatch.setColor(1.0F, 1.0F, 1.0F, paramFloat);
      paramBatch.draw(this.I, f1, f, this.co, this.co);
    } 
    float f7 = f1 + f6;
    f1 = Math.max(1.0F, f3 - f6);
    f2 += (f4 - 10.0F) / 2.0F;
    paramBatch.setColor(Color.WHITE);
    b.a.draw(paramBatch, f7 - 1.0F, f2 - 1.0F, f1 + 2.0F, 12.0F);
    paramBatch.setColor(this.u.r, this.u.g, this.u.b, paramFloat);
    paramBatch.draw((TextureRegion)b.a, f7, f2, f1 * f5, 10.0F);
    paramBatch.setColor(Color.WHITE);
  }
}
