package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class ad {
  private final int G;
  
  private final TextureRegion[] j;
  
  public final float[] g;
  
  private final int[] j;
  
  private final int[] k;
  
  public final int H;
  
  public final Color e;
  
  private final Vector2 i = new Vector2();
  
  public ad(int paramInt1, TextureRegion[] paramArrayOfTextureRegion, float[] paramArrayOffloat, int[] paramArrayOfint1, int[] paramArrayOfint2, int paramInt2, Color paramColor) {
    this.G = paramInt1;
    this.j = (int[])paramArrayOfTextureRegion;
    this.g = paramArrayOffloat;
    this.j = paramArrayOfint1;
    this.k = paramArrayOfint2;
    this.H = paramInt2;
    this.e = paramColor;
  }
  
  private boolean b() {
    return (this.j.length > 1);
  }
  
  public final TextureRegion e(float paramFloat) {
    if (!b())
      return this.j[0]; 
    float f1 = 0.0F;
    float[] arrayOfFloat;
    int i = (arrayOfFloat = this.g).length;
    for (byte b = 0; b < i; b++) {
      float f = arrayOfFloat[b];
      f1 += f;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.g.length; i++) {
      if (f2 < this.g[i])
        return this.j[i]; 
      f2 -= this.g[i];
    } 
    return this.j[this.j.length - 1];
  }
  
  public final Vector2 e(float paramFloat) {
    if (!b())
      return this.i.set(this.j[0], this.k[0]); 
    float f1 = 0.0F;
    float[] arrayOfFloat;
    int i = (arrayOfFloat = this.g).length;
    for (byte b = 0; b < i; b++) {
      float f = arrayOfFloat[b];
      f1 += f;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.g.length; i++) {
      if (f2 < this.g[i])
        return this.i.set(this.j[i], this.k[i]); 
      f2 -= this.g[i];
    } 
    return this.i.set(this.j[this.j.length - 1], this.k[this.k.length - 1]);
  }
}
