package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class g {
  private final int d;
  
  private final TextureRegion[] e;
  
  public final float[] a;
  
  private final int[] b;
  
  private final int[] c;
  
  private final Vector2 a = new Vector2();
  
  public g(int paramInt, TextureRegion[] paramArrayOfTextureRegion, float[] paramArrayOffloat, int[] paramArrayOfint1, int[] paramArrayOfint2) {
    this.d = paramInt;
    this.e = paramArrayOfTextureRegion;
    this.a = (Vector2)paramArrayOffloat;
    this.b = paramArrayOfint1;
    this.c = paramArrayOfint2;
  }
  
  private boolean b() {
    return (this.e.length > 1);
  }
  
  public final TextureRegion a(float paramFloat) {
    if (!b())
      return this.e[0]; 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.a).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.a.length; i++) {
      if (f2 < this.a[i])
        return this.e[i]; 
      f2 -= this.a[i];
    } 
    return this.e[this.e.length - 1];
  }
  
  public final Vector2 a(float paramFloat) {
    if (!b())
      return this.a.set(this.b[0], this.c[0]); 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.a).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.a.length; i++) {
      if (f2 < this.a[i])
        return this.a.set(this.b[i], this.c[i]); 
      f2 -= this.a[i];
    } 
    return this.a.set(this.b[this.b.length - 1], this.c[this.c.length - 1]);
  }
}
