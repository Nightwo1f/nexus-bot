package a;

import com.badlogic.gdx.math.Vector2;

final class fw {
  final g a;
  
  final float bd;
  
  fw(g paramg, float paramFloat) {
    this.a = paramg;
    this.bd = paramFloat;
  }
  
  final float d() {
    float f = 0.0F;
    Vector2 vector2;
    int i = (vector2 = this.a.a).length;
    for (byte b = 0; b < i; b++) {
      Vector2 vector21 = vector2[b];
      f += vector21;
    } 
    return f;
  }
}
