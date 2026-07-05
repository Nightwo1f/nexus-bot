package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class ah {
  private final int K;
  
  private final TextureRegion[] k;
  
  private final float[] h;
  
  private final float[] i;
  
  private final float c;
  
  private final boolean e;
  
  private final boolean f;
  
  private final int[] l;
  
  private final int[] m;
  
  final boolean g;
  
  public final int L;
  
  public final boolean h;
  
  final boolean i;
  
  public final boolean j;
  
  public final int M;
  
  public final Color f;
  
  private final Vector2 j = new Vector2();
  
  public ah(int paramInt1, TextureRegion[] paramArrayOfTextureRegion, float[] paramArrayOffloat1, float[] paramArrayOffloat2, int[] paramArrayOfint1, int[] paramArrayOfint2, boolean paramBoolean1, int paramInt2, boolean paramBoolean2, boolean paramBoolean3, boolean paramBoolean4, int paramInt3, Color paramColor, boolean paramBoolean5) {
    this.K = paramInt1;
    this.k = paramArrayOfTextureRegion;
    this.h = paramArrayOffloat1;
    this.i = paramArrayOffloat2;
    this.l = paramArrayOfint1;
    this.m = paramArrayOfint2;
    this.g = paramBoolean1;
    this.L = paramInt2;
    this.h = paramBoolean2;
    this.i = paramBoolean3;
    this.j = paramBoolean4;
    this.M = paramInt3;
    this.f = paramColor;
    this.f = paramBoolean5;
    paramInt1 = 0;
    float f = 0.0F;
    if (paramArrayOfTextureRegion.length > 1)
      for (byte b = 0; b < paramArrayOffloat1.length; b++) {
        if (paramArrayOffloat1[b] != paramArrayOffloat2[b])
          paramInt1 = 1; 
        f += (paramArrayOffloat1[b] + paramArrayOffloat2[b]) / 2.0F;
      }  
    this.e = paramInt1;
    this.c = Math.max(0.001F, f);
  }
  
  public final boolean e() {
    return (this.k.length > 1);
  }
  
  private int a(float paramFloat1, float paramFloat2, float paramFloat3) {
    if (!e())
      return 0; 
    if (this.f == null) {
      float f1 = (Math.abs(Float.floatToIntBits(paramFloat2) * 73 ^ Float.floatToIntBits(paramFloat3) * 271) % 10000) / 1000.0F;
      paramFloat1 += f1;
    } 
    if (!this.e) {
      float f1 = paramFloat1 % this.c;
      for (byte b1 = 0; b1 < this.h.length; b1++) {
        if (f1 < this.h[b1])
          return b1; 
        f1 -= this.h[b1];
      } 
      return this.h.length - 1;
    } 
    int j = (int)(paramFloat1 / this.c);
    float f = paramFloat1 % this.c;
    paramFloat1 = 0.0F;
    int i = (this.f != null) ? this.K : (Float.floatToIntBits(paramFloat2) * 73 ^ Float.floatToIntBits(paramFloat3) * 271);
    for (byte b = 0; b < this.h.length; b++) {
      byte b1 = b;
      int k = j;
      float f1 = (Math.abs((((i * 31 ^ k) * 31 ^ b1 ^ ((i * 31 ^ k) * 31 ^ b1) >> 16) * -2048144789 ^ ((i * 31 ^ k) * 31 ^ b1 ^ ((i * 31 ^ k) * 31 ^ b1) >> 16) * -2048144789 >> 13) * -1028477387 ^ (((i * 31 ^ k) * 31 ^ b1 ^ ((i * 31 ^ k) * 31 ^ b1) >> 16) * -2048144789 ^ ((i * 31 ^ k) * 31 ^ b1 ^ ((i * 31 ^ k) * 31 ^ b1) >> 16) * -2048144789 >> 13) * -1028477387 >> 16) % 1000) / 1000.0F;
      f1 = this.h[b] + (this.i[b] - this.h[b]) * f1;
      paramFloat1 += f1;
      if (f < paramFloat1)
        return b; 
    } 
    return this.h.length - 1;
  }
  
  public final TextureRegion a(float paramFloat1, float paramFloat2, float paramFloat3) {
    return this.k[a(paramFloat1, paramFloat2, paramFloat3)];
  }
  
  public final Vector2 a(float paramFloat1, float paramFloat2, float paramFloat3) {
    int i = a(paramFloat1, paramFloat2, paramFloat3);
    return this.j.set(this.l[i], this.m[i]);
  }
  
  public final TextureRegion a() {
    return a(0.0F, 0.0F, 0.0F);
  }
}
