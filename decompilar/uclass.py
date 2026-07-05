package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class u {
  final TextureRegion[] i;
  
  final float[] e;
  
  final Vector2[] a;
  
  private final String[] b;
  
  private final boolean a;
  
  private final boolean b;
  
  public float b;
  
  public final int s;
  
  public final Color c;
  
  final Vector2 f = new Vector2();
  
  public u(TextureRegion[] paramArrayOfTextureRegion, float[] paramArrayOffloat, Vector2[] paramArrayOfVector2, String[] paramArrayOfString, boolean paramBoolean1, boolean paramBoolean2, int paramInt, Color paramColor) {
    this.i = paramArrayOfTextureRegion;
    this.e = paramArrayOffloat;
    this.a = paramArrayOfVector2;
    this.b = paramArrayOfString;
    this.a = paramBoolean1;
    this.b = paramBoolean2;
    this.s = paramInt;
    this.c = paramColor;
    this.b = 0.0F;
    float[] arrayOfFloat;
    int i = (arrayOfFloat = paramArrayOffloat).length;
    for (byte b = 0; b < i; b++) {
      float f = arrayOfFloat[b];
      this.b += f;
    } 
  }
  
  final float a(float paramFloat) {
    return this.a ? (paramFloat % this.b) : Math.min(paramFloat, this.b);
  }
}
