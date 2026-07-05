package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;

final class jj extends Image {
  private final jp a;
  
  private final jt a;
  
  private final TextureRegionDrawable l;
  
  private TextureRegion G;
  
  private float D = 0.0F;
  
  private final float bT;
  
  private final float bU;
  
  private final Vector2 q;
  
  jj(jp paramjp, jt paramjt, TextureRegion paramTextureRegion) {
    this.a = (jt)paramjp;
    this.a = paramjt;
    TextureRegion textureRegion = (paramTextureRegion != null) ? paramTextureRegion : new TextureRegion(in.a((Texture)null));
    this.l = new TextureRegionDrawable(textureRegion);
    setDrawable((Drawable)this.l);
    setScaling(Scaling.none);
    setTouchable(Touchable.disabled);
    this.G = textureRegion;
    this.bT = Math.max(1.0F, textureRegion.getRegionWidth());
    this.bU = Math.max(1.0F, textureRegion.getRegionHeight());
    if (paramjt != null) {
      Vector2 vector2 = paramjt.get(0.0F);
      this.q = (vector2 != null) ? new Vector2(vector2) : new Vector2(0.0F, 0.0F);
      return;
    } 
    this.q = new Vector2(0.0F, 0.0F);
  }
  
  public final void act(float paramFloat) {
    super.act(paramFloat);
    if (this.a == null)
      return; 
    this.D += paramFloat;
    TextureRegion textureRegion;
    if ((textureRegion = this.a.get(this.D)) != null && textureRegion != this.G) {
      this.l.setRegion(textureRegion);
      this.G = textureRegion;
    } 
  }
  
  public final void draw(Batch paramBatch, float paramFloat) {
    if (this.a != null) {
      TextureRegion textureRegion = this.a.get(this.D);
      Vector2 vector2 = (this.a != null) ? this.a.get(this.D) : new Vector2(0.0F, 0.0F);
      if (textureRegion != null && vector2 != null) {
        Color color = getColor();
        paramBatch.setColor(color.r, color.g, color.b, color.a * paramFloat);
        paramFloat = getX();
        float f2 = getY();
        float f3 = getWidth();
        float f4 = getHeight();
        float f5 = textureRegion.getRegionWidth();
        float f6 = textureRegion.getRegionHeight();
        f3 = (f3 - this.bT) / 2.0F;
        float f7 = (f4 - this.bU) / 2.0F;
        float f8 = this.q.x;
        float f9 = f4 - this.q.y - this.bU;
        f3 -= f8;
        f7 -= f9;
        f8 = vector2.x;
        float f1 = f4 - vector2.y - f6;
        paramFloat = paramFloat + f8 + f3;
        f1 = f2 + f1 + f7;
        paramBatch.draw(textureRegion, paramFloat, f1, f5, f6);
        return;
      } 
    } 
    super.draw(paramBatch, paramFloat);
  }
}
