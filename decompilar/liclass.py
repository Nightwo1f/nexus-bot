package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.Group;
import java.util.ArrayList;
import java.util.HashMap;

public final class li {
  private final Group n;
  
  private final HashMap c = new HashMap<>();
  
  private final ArrayList b = new ArrayList();
  
  public li(Group paramGroup) {
    this.n = paramGroup;
  }
  
  public final void b(String paramString, float paramFloat1, float paramFloat2, Color paramColor, TextureRegion paramTextureRegion) {
    if (paramString == null || paramString.isEmpty())
      return; 
    if (paramFloat2 <= 0.0F || paramFloat1 <= 0.0F) {
      D(paramString);
      return;
    } 
    lh lh2;
    if ((lh2 = (lh)this.c.get(paramString)) == null) {
      lh2 = new lh(paramString, () -> D(paramString));
      this.c.put(paramString, lh2);
      this.b.add(paramString);
      this.n.addActor(lh2);
    } 
    paramFloat2 = paramFloat1;
    paramFloat1 = paramFloat2;
    lh lh1;
    (lh1 = lh2).cm = Math.max(0.001F, paramFloat1);
    lh1.cn = Math.min(Math.max(0.001F, paramFloat2), lh1.cm);
    if (paramColor != null)
      lh1.u.set(paramColor); 
    lh1.I = paramTextureRegion;
    lh1.bJ = false;
  }
  
  private void D(String paramString) {
    lh lh = (lh)this.c.remove(paramString);
    this.b.remove(paramString);
    if (lh != null)
      lh.remove(); 
  }
  
  public final void a(float paramFloat1, float paramFloat2, float paramFloat3) {
    if (this.b.isEmpty()) {
      this.n.setVisible(false);
      this.n.setSize(0.0F, 0.0F);
      return;
    } 
    this.n.setVisible(true);
    boolean bool = false;
    for (String str : this.b) {
      if (((lh)this.c.get(str)).u()) {
        bool = true;
        break;
      } 
    } 
    float f1 = Math.max(8.0F, paramFloat3);
    float f2 = bool ? Math.max(10.0F, 20.0F) : 10.0F;
    paramFloat3 = f1 + (bool ? 21.0F : 0.0F);
    int i;
    float f3 = (i = this.b.size()) * f2 + (i - 1) * 1.0F;
    paramFloat2 = paramFloat2 - 50.0F - f3;
    this.n.setPosition(Math.round(paramFloat1), Math.round(paramFloat2));
    this.n.setSize(paramFloat3, f3);
    for (byte b = 0; b < i; b++) {
      String str = this.b.get(b);
      lh lh;
      if ((lh = (lh)this.c.get(str)) != null) {
        lh.m(bool);
        lh.setSize(paramFloat3, f2);
        f3 = (i - 1 - b) * (f2 + 1.0F);
        lh.setPosition(0.0F, f3);
      } 
    } 
  }
}
