package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public final class bb {
  public TextureRegion j;
  
  public Vector2 k;
  
  public int F;
  
  public int aB;
  
  public int aC;
  
  final void a(TextureRegion paramTextureRegion, Vector2 paramVector2, int paramInt1, int paramInt2, int paramInt3, int[] paramArrayOfint) {
    this.j = paramTextureRegion;
    this.k = paramVector2;
    this.F = paramInt2;
    this.aB = paramInt3;
    this.aC = a(paramInt1, paramArrayOfint);
  }
  
  private static int a(int paramInt, int[] paramArrayOfint) {
    for (byte b = 0; b < paramArrayOfint.length; b++) {
      if (paramArrayOfint[b] == paramInt)
        return b; 
    } 
    return paramArrayOfint.length + 1;
  }
}
