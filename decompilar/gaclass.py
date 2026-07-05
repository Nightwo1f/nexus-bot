package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Vector2;

final class ga {
  final float bg;
  
  final float bh;
  
  final TextureRegion F;
  
  final float bi;
  
  final float bj;
  
  final float bk;
  
  final float bl;
  
  final float bm;
  
  final float bn;
  
  final float bo;
  
  final float bp;
  
  final float bq;
  
  ga(g paramg, float paramFloat1, be parambe1, be parambe2, float paramFloat2) {
    this.bg = paramFloat1;
    paramFloat1 = (parambe2.aD - parambe1.aD);
    float f3 = (parambe2.aE - parambe1.aE);
    float f4 = (float)Math.sqrt((paramFloat1 * paramFloat1 + f3 * f3));
    this.bh = Math.max(0.15F, f4 * 0.08F);
    this.F = paramg.a(0.0F);
    Vector2 vector2 = paramg.a(0.0F);
    this.bo = this.F.getRegionWidth();
    this.bp = -this.F.getRegionHeight();
    this.bm = this.bo / 2.0F;
    this.bn = this.bp / 2.0F;
    this.bi = parambe1.aD * paramFloat2 + vector2.x;
    this.bj = parambe1.aE * paramFloat2 + vector2.y + this.F.getRegionHeight();
    float f2 = parambe2.aD * paramFloat2 + vector2.x;
    float f1 = parambe2.aE * paramFloat2 + vector2.y + this.F.getRegionHeight();
    this.bk = f2 - this.bi;
    this.bl = f1 - this.bj;
    f1 = MathUtils.atan2(f3, paramFloat1) * 57.295776F;
    this.bq = f1 + 45.0F;
  }
  
  final float e(float paramFloat) {
    return MathUtils.clamp((paramFloat - this.bg) / this.bh, 0.0F, 1.0F);
  }
}
