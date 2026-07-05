package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class n {
  private final int k;
  
  private final TextureRegion[] g;
  
  private final float[] c;
  
  private final int[] f;
  
  private final int[] g;
  
  public final int l;
  
  public final Color b;
  
  private final Vector2 c = new Vector2();
  
  public n(int paramInt1, TextureRegion[] paramArrayOfTextureRegion, float[] paramArrayOffloat, int[] paramArrayOfint1, int[] paramArrayOfint2, int paramInt2, Color paramColor) {
    this.k = paramInt1;
    this.g = (int[])paramArrayOfTextureRegion;
    this.c = (Vector2)paramArrayOffloat;
    this.f = paramArrayOfint1;
    this.g = paramArrayOfint2;
    this.l = paramInt2;
    this.b = paramColor;
  }
  
  public final boolean d() {
    return (this.g.length > 1);
  }
  
  public final TextureRegion c(float paramFloat) {
    if (!d())
      return this.g[0]; 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.c).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.c.length; i++) {
      if (f2 < this.c[i])
        return this.g[i]; 
      f2 -= this.c[i];
    } 
    return this.g[this.g.length - 1];
  }
  
  public final Vector2 c(float paramFloat) {
    if (!d())
      return this.c.set(this.f[0], this.g[0]); 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.c).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.c.length; i++) {
      if (f2 < this.c[i])
        return this.c.set(this.f[i], this.g[i]); 
      f2 -= this.c[i];
    } 
    return this.c.set(this.f[this.f.length - 1], this.g[this.g.length - 1]);
  }
}
