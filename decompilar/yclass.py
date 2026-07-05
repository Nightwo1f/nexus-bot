package a;

import com.badlogic.gdx.math.Vector2;
import java.util.HashMap;
import java.util.Map;

public final class y {
  private final int w;
  
  public final Map k;
  
  private final Vector2 g = new Vector2();
  
  public y(int paramInt, Map<?, ?> paramMap) {
    this.w = paramInt;
    this.k = new HashMap<>(paramMap);
  }
  
  public final boolean a(int paramInt) {
    return this.k.containsKey(Integer.valueOf(paramInt));
  }
}
