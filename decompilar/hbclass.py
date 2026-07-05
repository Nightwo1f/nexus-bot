package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop;

final class hb extends DragAndDrop.Target {
  hb(gb paramgb, Actor paramActor, int paramInt1, int paramInt2) {
    super(paramActor);
  }
  
  public final boolean drag(DragAndDrop.Source paramSource, DragAndDrop.Payload paramPayload, float paramFloat1, float paramFloat2, int paramInt) {
    if (!this.A.q())
      return false; 
    if (paramPayload == null || !(paramPayload.getObject() instanceof hq))
      return false; 
    if (((hq)paramPayload.getObject()).ba)
      return false; 
    boolean bool1 = (this.A.a != null && this.A.a[this.dN]) ? true : false;
    boolean bool2 = (this.A.F != null && this.A.F[this.dN] == 0) ? true : false;
    return (!bool1 && bool2);
  }
  
  public final void drop(DragAndDrop.Source paramSource, DragAndDrop.Payload paramPayload, float paramFloat1, float paramFloat2, int paramInt) {
    hq hq = (hq)paramPayload.getObject();
    try {
      this.A.m.k(hq.dS, this.dO);
      return;
    } catch (Exception exception) {
      Gdx.app.error("Depot/DnD", "RequestStoreDepotItem falhou", exception);
      return;
    } 
  }
}
