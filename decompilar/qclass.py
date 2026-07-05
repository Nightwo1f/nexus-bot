package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class q {
  private final int o;
  
  private final TextureRegion[] h;
  
  public final float[] d;
  
  private final int[] h;
  
  private final int[] i;
  
  private final Vector2 d = new Vector2();
  
  public q(int paramInt, TextureRegion[] paramArrayOfTextureRegion, float[] paramArrayOffloat, int[] paramArrayOfint1, int[] paramArrayOfint2) {
    this.o = paramInt;
    this.h = (int[])paramArrayOfTextureRegion;
    this.d = (Vector2)paramArrayOffloat;
    this.h = paramArrayOfint1;
    this.i = paramArrayOfint2;
  }
  
  private boolean b() {
    return (this.h.length > 1);
  }
  
  public final TextureRegion d(float paramFloat) {
    if (!b())
      return this.h[0]; 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.d).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.d.length; i++) {
      if (f2 < this.d[i])
        return this.h[i]; 
      f2 -= this.d[i];
    } 
    return this.h[this.h.length - 1];
  }
  
  public final Vector2 d(float paramFloat) {
    if (!b())
      return this.d.set(this.h[0], this.i[0]); 
    float f1 = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.d).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f1 += vector21;
    } 
    float f2 = paramFloat % f1;
    for (i = 0; i < this.d.length; i++) {
      if (f2 < this.d[i])
        return this.d.set(this.h[i], this.i[i]); 
      f2 -= this.d[i];
    } 
    return this.d.set(this.h[this.h.length - 1], this.i[this.i.length - 1]);
  }
}
