package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop;

final class gx extends DragAndDrop.Target {
  gx(gb paramgb, Actor paramActor, int paramInt) {
    super(paramActor);
  }
  
  public final boolean drag(DragAndDrop.Source paramSource, DragAndDrop.Payload paramPayload, float paramFloat1, float paramFloat2, int paramInt) {
    if (!this.w.q())
      return false; 
    boolean bool1 = (this.w.C[this.dK - 1] == null) ? true : false;
    if (paramPayload == null)
      return false; 
    Object object = paramPayload.getObject();
    Integer integer = null;
    if (object instanceof Integer) {
      integer = (Integer)object;
    } else if (object instanceof hq) {
      if (!((hq)(object = object)).ba)
        return false; 
      integer = Integer.valueOf(((hq)object).dS);
    } 
    boolean bool2 = (integer != null && integer.intValue() > 0 && integer.intValue() <= this.w.c.length && !this.w.a[integer.intValue() - 1] && this.w.F[integer.intValue() - 1] != 0) ? true : false;
    return (bool1 && bool2);
  }
  
  public final void drop(DragAndDrop.Source paramSource, DragAndDrop.Payload paramPayload, float paramFloat1, float paramFloat2, int paramInt) {
    int i;
    if (paramPayload == null)
      return; 
    Object object;
    if (object = paramPayload.getObject() instanceof Integer) {
      i = ((Integer)object).intValue();
    } else if (i instanceof hq) {
      i = ((hq)i).dS;
    } else {
      return;
    } 
    try {
      this.w.m.j(i, this.dK);
      return;
    } catch (Exception exception) {
      Gdx.app.error("Depot/DnD", "RequestTakeDepotItem falhou", exception);
      return;
    } 
  }
}
