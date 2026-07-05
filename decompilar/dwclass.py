package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.g2d.freetype.FreeTypeFontGenerator;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop;

public final class dw extends Actor {
  private int cf = 0;
  
  float ap = 0.0F;
  
  boolean ah = false;
  
  private Byte b = null;
  
  public float aq = 0.0F;
  
  public float ar = 0.0F;
  
  public boolean ai = false;
  
  public dw(dl paramdl) {
    setTouchable(Touchable.enabled);
    addListener((EventListener)new dx(this, paramdl));
  }
  
  final void b(float paramFloat1, float paramFloat2) {
    Byte byte_;
    byte b;
    float f1 = getWidth() / 2.0F;
    float f2 = getHeight() / 2.0F;
    paramFloat1 -= f1;
    paramFloat2 -= f2;
    f1 = (float)Math.sqrt((paramFloat1 * paramFloat1 + paramFloat2 * paramFloat2));
    f2 = getWidth() / 2.0F;
    if (f1 > f2) {
      this.aq = paramFloat1 / f1 * f2;
      this.ar = paramFloat2 / f1 * f2;
    } else {
      this.aq = paramFloat1;
      this.ar = paramFloat2;
    } 
    if (f1 < getWidth() * 0.2F) {
      if (!this.ah) {
        this.i.a = null;
        this.cf = 0;
        this.ap = 0.0F;
        this.b = null;
      } 
      return;
    } 
    if ((paramFloat1 = MathUtils.atan2(paramFloat2, paramFloat1) * 57.295776F) < 0.0F)
      paramFloat1 += 360.0F; 
    if (paramFloat1 >= 45.0F && paramFloat1 < 135.0F) {
      b = 3;
      byte_ = Byte.valueOf((byte)100);
    } else if (byte_ >= 135.0F && byte_ < 225.0F) {
      b = 2;
      byte_ = Byte.valueOf((byte)103);
    } else if (byte_ >= 225.0F && byte_ < 315.0F) {
      b = 1;
      byte_ = Byte.valueOf((byte)102);
    } else {
      b = 4;
      byte_ = Byte.valueOf((byte)101);
    } 
    if (byte_ != this.b) {
      this.ah = false;
      this.ap = 0.0F;
      this.b = byte_;
    } 
    this.cf = b;
    this.i.a = (DragAndDrop)byte_;
  }
  
  public final void act(float paramFloat) {
    super.act(paramFloat);
    if (this.ai && !this.ah && this.i.a != null) {
      this.ap += paramFloat;
      if (this.ap >= 3.0F)
        this.ah = true; 
    } 
  }
  
  public final void az() {
    this.ah = false;
    this.cf = 0;
    this.i.a = null;
    this.ap = 0.0F;
    this.b = null;
    if (!this.ai) {
      this.aq = 0.0F;
      this.ar = 0.0F;
    } 
  }
  
  public final void draw(Batch paramBatch, float paramFloat) {
    if (b.a != null && b.a.length == 5) {
      FreeTypeFontGenerator freeTypeFontGenerator = b.a[this.cf];
      Color color = getColor();
      paramBatch.setColor(color.r, color.g, color.b, color.a * paramFloat);
      paramBatch.draw((TextureRegion)freeTypeFontGenerator, getX(), getY(), getWidth(), getHeight());
      paramBatch.setColor(Color.WHITE);
    } 
  }
}
