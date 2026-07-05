package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;
import java.util.HashMap;
import java.util.Map;

public final class t {
  private final int r;
  
  public final Map i;
  
  private final Vector2 e = new Vector2();
  
  public t(int paramInt, Map<?, ?> paramMap) {
    this.r = paramInt;
    this.i = new HashMap<>(paramMap);
  }
  
  public final TextureRegion a(int paramInt, float paramFloat) {
    u u;
    if ((u = (u)this.i.get(Integer.valueOf(paramInt))) != null && u.i.length != 0) {
      if (u.i.length == 1)
        return u.i[0]; 
      paramFloat = u.a(paramFloat);
      for (byte b = 0; b < u.e.length; b++) {
        if (paramFloat < u.e[b])
          return u.i[b]; 
        paramFloat -= u.e[b];
      } 
      return u.i[u.i.length - 1];
    } 
    return null;
  }
  
  public final Vector2 a(int paramInt, float paramFloat) {
    u u;
    if ((u = (u)this.i.get(Integer.valueOf(paramInt))) != null) {
      if (u.a == null || u.a.length == 0)
        return u.f.set(0.0F, 0.0F); 
      if (u.a.length == 1)
        return u.a[0]; 
      paramFloat = u.a(paramFloat);
      for (byte b = 0; b < u.e.length; b++) {
        if (paramFloat < u.e[b])
          return u.a[b]; 
        paramFloat -= u.e[b];
      } 
      return u.a[u.a.length - 1];
    } 
    return this.e.set(0.0F, 0.0F);
  }
}
