package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;
import com.badlogic.gdx.scenes.scene2d.Stage;
import java.util.Iterator;

final class jg extends InputListener {
  jg(ju paramju, Stage paramStage) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    String str;
    if (in.bj)
      return false; 
    if (this.e.b != null && in.j != null && this.q.getKeyboardFocus() == in.j)
      return false; 
    if (in.b != null)
      return false; 
    paramInputEvent = null;
    if (paramInt >= 7 && paramInt <= 16) {
      str = String.valueOf(paramInt - 7);
    } else if (paramInt >= 144 && paramInt <= 153) {
      str = String.valueOf(paramInt - 144);
    } 
    if (str != null) {
      boolean bool = (in.x != null && in.x.isVisible()) ? true : false;
      Iterator<jk> iterator = this.e.F.iterator();
      while (iterator.hasNext()) {
        jk jk;
        if ((jk = iterator.next()).aq != null && jk.aq.equals(str)) {
          boolean bool1 = false;
          if (jk.bn) {
            if (bool && (this.e.bz || jk.ef == in.ec))
              bool1 = true; 
          } else if (!bool) {
            bool1 = true;
          } 
          if (bool1) {
            in.b = jk;
            in.ed = paramInt;
            in.ce();
            return true;
          } 
        } 
      } 
    } 
    if (paramInt == 51 || paramInt == 19) {
      if (!in.s())
        return false; 
      in.an(-1);
      in.ee = paramInt;
      in.bK = 0.0F;
      in.bi = false;
      return true;
    } 
    if (paramInt == 47 || paramInt == 20) {
      if (!in.s())
        return false; 
      in.an(1);
      in.ee = paramInt;
      in.bK = 0.0F;
      in.bi = false;
      return true;
    } 
    if (paramInt == 66 || paramInt == 160 || paramInt == 62) {
      if (in.a != null && in.a().contains(in.a)) {
        in.b = in.a;
        in.ed = paramInt;
        in.ce();
        return true;
      } 
      if (this.e.b != null && this.e.b.j != null && (paramInt == 66 || paramInt == 160)) {
        al.a(3);
        this.e.b.j.run();
        in.g(null);
        return true;
      } 
    } 
    return false;
  }
  
  public final boolean keyUp(InputEvent paramInputEvent, int paramInt) {
    if (in.bj)
      return false; 
    if (paramInt == in.ee)
      in.ee = -1; 
    if (in.b != null && paramInt == in.ed) {
      js js = in.b;
      in.b = null;
      in.ed = -1;
      in.ce();
      if (js.a() != null)
        js.a().run(); 
      return true;
    } 
    return false;
  }
}
