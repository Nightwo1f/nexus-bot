package a;

import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;

public final class ak implements Drawable {
  public final Texture ba;
  
  private final int P;
  
  private final int Q;
  
  private final int R;
  
  private final int S;
  
  private final TextureRegion s;
  
  private final TextureRegion t;
  
  private final TextureRegion u;
  
  private final TextureRegion v;
  
  private final TextureRegion w;
  
  private final TextureRegion x;
  
  private final TextureRegion y;
  
  private final TextureRegion z;
  
  private final TextureRegion A;
  
  private float d;
  
  private float e;
  
  private float f;
  
  private float g;
  
  private float h;
  
  private float i;
  
  public ak(Texture paramTexture, int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
    this.ba = paramTexture;
    this.P = paramInt1;
    this.Q = paramInt2;
    this.R = paramInt3;
    this.S = paramInt4;
    paramTexture.setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat);
    int i = paramTexture.getWidth();
    int j = paramTexture.getHeight();
    this.s = new TextureRegion(paramTexture, 0, j - paramInt4, paramInt1, paramInt4);
    this.t = new TextureRegion(paramTexture, i - paramInt2, j - paramInt4, paramInt2, paramInt4);
    this.u = new TextureRegion(paramTexture, 0, 0, paramInt1, paramInt3);
    this.v = new TextureRegion(paramTexture, i - paramInt2, 0, paramInt2, paramInt3);
    this.w = new TextureRegion(paramTexture, paramInt1, j - paramInt4, i - paramInt1 - paramInt2, paramInt4);
    this.x = new TextureRegion(paramTexture, paramInt1, 0, i - paramInt1 - paramInt2, paramInt3);
    this.y = new TextureRegion(paramTexture, 0, paramInt3, paramInt1, j - paramInt3 - paramInt4);
    this.z = new TextureRegion(paramTexture, i - paramInt2, paramInt3, paramInt2, j - paramInt3 - paramInt4);
    this.A = new TextureRegion(paramTexture, paramInt1, paramInt3, i - paramInt1 - paramInt2, j - paramInt3 - paramInt4);
    this.d = paramInt1;
    this.e = paramInt2;
    this.f = paramInt3;
    this.g = paramInt4;
    this.h = (paramInt1 + paramInt2);
    this.i = (paramInt3 + paramInt4);
  }
  
  public final float getLeftWidth() {
    return this.d;
  }
  
  public final void setLeftWidth(float paramFloat) {
    this.d = paramFloat;
  }
  
  public final float getRightWidth() {
    return this.e;
  }
  
  public final void setRightWidth(float paramFloat) {
    this.e = paramFloat;
  }
  
  public final float getTopHeight() {
    return this.f;
  }
  
  public final void setTopHeight(float paramFloat) {
    this.f = paramFloat;
  }
  
  public final float getBottomHeight() {
    return this.g;
  }
  
  public final void setBottomHeight(float paramFloat) {
    this.g = paramFloat;
  }
  
  public final float getMinWidth() {
    return this.h;
  }
  
  public final void setMinWidth(float paramFloat) {
    this.h = paramFloat;
  }
  
  public final float getMinHeight() {
    return this.i;
  }
  
  public final void setMinHeight(float paramFloat) {
    this.i = paramFloat;
  }
  
  public final void draw(Batch paramBatch, float paramFloat1, float paramFloat2, float paramFloat3, float paramFloat4) {
    paramBatch.draw(this.s, paramFloat1, paramFloat2, this.P, this.S);
    paramBatch.draw(this.t, paramFloat1 + paramFloat3 - this.Q, paramFloat2, this.Q, this.S);
    paramBatch.draw(this.u, paramFloat1, paramFloat2 + paramFloat4 - this.R, this.P, this.R);
    paramBatch.draw(this.v, paramFloat1 + paramFloat3 - this.Q, paramFloat2 + paramFloat4 - this.R, this.Q, this.R);
    float f = paramFloat3 - this.P - this.Q;
    paramBatch.draw(this.w, paramFloat1 + this.P, paramFloat2, f, this.S);
    paramBatch.draw(this.x, paramFloat1 + this.P, paramFloat2 + paramFloat4 - this.R, f, this.R);
    paramFloat4 = paramFloat4 - this.R - this.S;
    paramBatch.draw(this.y, paramFloat1, paramFloat2 + this.S, this.P, paramFloat4);
    paramBatch.draw(this.z, paramFloat1 + paramFloat3 - this.Q, paramFloat2 + this.S, this.Q, paramFloat4);
    int i = this.A.getRegionWidth();
    int m = this.A.getRegionHeight();
    int n = (int)(f / i);
    int k = (int)(f % i);
    int i1 = (int)(paramFloat4 / m);
    int j = (int)(paramFloat4 % m);
    paramFloat1 += this.P;
    paramFloat2 += this.S;
    for (byte b = 0; b < i1; b++) {
      float f1 = paramFloat2 + (b * m);
      for (byte b1 = 0; b1 < n; b1++) {
        float f2 = paramFloat1 + (b1 * i);
        paramBatch.draw(this.A, f2, f1, i, m);
      } 
      if (k > 0) {
        float f2 = paramFloat1 + (n * i);
        paramBatch.draw(this.A, f2, f1, k, m);
      } 
    } 
    if (j > 0) {
      float f1 = paramFloat2 + (i1 * m);
      for (byte b1 = 0; b1 < n; b1++) {
        float f2 = paramFloat1 + (b1 * i);
        paramBatch.draw(this.A, f2, f1, i, j);
      } 
      if (k > 0) {
        float f2 = paramFloat1 + (n * i);
        paramBatch.draw(this.A, f2, f1, k, j);
      } 
    } 
  }
}
