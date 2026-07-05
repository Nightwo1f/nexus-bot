package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

final class bn {
  final TextureRegion C;
  
  final Vector2 l;
  
  final int aS;
  
  final int aT;
  
  final int aU;
  
  bn(bl parambl, TextureRegion paramTextureRegion, Vector2 paramVector2, int paramInt1, int paramInt2, int paramInt3) {
    this.C = paramTextureRegion;
    this.l = paramVector2;
    this.aS = paramInt1;
    this.aT = paramInt2;
    this.aU = paramInt3;
  }
  
  public final int a(int[] paramArrayOfint) {
    for (byte b = 0; b < paramArrayOfint.length; b++) {
      if (paramArrayOfint[b] == this.aS)
        return b; 
    } 
    return paramArrayOfint.length + 1;
  }
}
