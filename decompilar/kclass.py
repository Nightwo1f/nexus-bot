package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class k {
  private final int g;
  
  private final TextureRegion[] f;
  
  private final float[] b;
  
  private final int[] d;
  
  private final int[] e;
  
  public final int h;
  
  public final Color a;
  
  private final Vector2 b = new Vector2();
  
  public k(int paramInt1, TextureRegion[] paramArrayOfTextureRegion, float[] paramArrayOffloat, int[] paramArrayOfint1, int[] paramArrayOfint2, int paramInt2, Color paramColor) {
    this.g = paramInt1;
    this.f = paramArrayOfTextureRegion;
    this.b = (Vector2)paramArrayOffloat;
    this.d = paramArrayOfint1;
    this.e = paramArrayOfint2;
    this.h = paramInt2;
    this.a = paramColor;
  }
  
  public final boolean c() {
    return (this.f.length > 1);
  }
  
  public final TextureRegion b(float paramFloat) {
    if (!c())
      return this.f[0]; 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.b).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.b.length; i++) {
      if (f2 < this.b[i])
        return this.f[i]; 
      f2 -= this.b[i];
    } 
    return this.f[this.f.length - 1];
  }
  
  public final Vector2 b(float paramFloat) {
    if (!c())
      return this.b.set(this.d[0], this.e[0]); 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.b).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.b.length; i++) {
      if (f2 < this.b[i])
        return this.b.set(this.d[i], this.e[i]); 
      f2 -= this.b[i];
    } 
    return this.b.set(this.d[this.d.length - 1], this.e[this.e.length - 1]);
  }
  
  public final float a() {
    float f = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.b).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f += vector21;
    } 
    return f;
  }
}
