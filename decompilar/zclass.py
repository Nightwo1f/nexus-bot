package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class z {
  private final TextureRegion[][] a;
  
  private final Vector2[][] a;
  
  private final String[][] a;
  
  private final int[][] a;
  
  private final int[][] b;
  
  private final float[] f;
  
  private final boolean c;
  
  private final boolean d;
  
  public float b;
  
  private final int x;
  
  private final Color d;
  
  private final Vector2 h = new Vector2();
  
  public z(TextureRegion[][] paramArrayOfTextureRegion, Vector2[][] paramArrayOfVector2, String[][] paramArrayOfString, int[][] paramArrayOfint1, int[][] paramArrayOfint2, float[] paramArrayOffloat) {
    this.a = (int[][])paramArrayOfTextureRegion;
    this.a = (int[][])paramArrayOfVector2;
    this.a = (int[][])paramArrayOfString;
    this.a = paramArrayOfint1;
    this.b = paramArrayOfint2;
    this.f = paramArrayOffloat;
    this.c = true;
    this.d = false;
    this.x = 0;
    this.d = null;
    this.b = 0.0F;
    float[] arrayOfFloat;
    int i = (arrayOfFloat = paramArrayOffloat).length;
    for (byte b = 0; b < i; b++) {
      float f = arrayOfFloat[b];
      this.b += f;
    } 
  }
  
  private float a(float paramFloat) {
    return this.c ? ((this.b > 0.0F) ? (paramFloat % this.b) : 0.0F) : Math.min(paramFloat, this.b);
  }
  
  private int a(float paramFloat) {
    for (byte b = 0; b < this.f.length; b++) {
      if (paramFloat < this.f[b])
        return b; 
      paramFloat -= this.f[b];
    } 
    return this.f.length - 1;
  }
  
  public final TextureRegion[] a(float paramFloat) {
    if (this.a == null || this.a.length == 0)
      return new TextureRegion[0]; 
    if (this.a.length == 1)
      return (TextureRegion[])this.a[0]; 
    paramFloat = a(paramFloat);
    int i = a(paramFloat);
    return (TextureRegion[])this.a[i];
  }
  
  public final int[] a(float paramFloat) {
    if (this.b == null || this.b.length == 0)
      return new int[0]; 
    if (this.b.length == 1)
      return this.b[0]; 
    paramFloat = a(paramFloat);
    int i = a(paramFloat);
    return this.b[i];
  }
  
  public final Vector2[] a(float paramFloat) {
    if (this.a == null || this.a.length == 0)
      return new Vector2[0]; 
    if (this.a.length == 1)
      return (Vector2[])this.a[0]; 
    paramFloat = a(paramFloat);
    int i = a(paramFloat);
    return (Vector2[])this.a[i];
  }
  
  public final int[] b(float paramFloat) {
    if (this.a == null || this.a.length == 0)
      return new int[0]; 
    if (this.a.length == 1)
      return this.a[0]; 
    paramFloat = a(paramFloat);
    int i = a(paramFloat);
    return this.a[i];
  }
  
  public final int b(float paramFloat) {
    paramFloat = a(paramFloat);
    return a(paramFloat);
  }
}
