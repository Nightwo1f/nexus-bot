package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gw extends ClickListener {
  gw(gb paramgb, int paramInt) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (this.v.a[this.dJ])
      return; 
    if (this.v.F[this.dJ] == 0)
      return; 
    if (paramInputEvent.getButton() != 0)
      return; 
    int i;
    if ((i = this.v.m()) == 0) {
      this.v.m.g(b.a(((cq)this.v.j).S, "id_no_free_backpack_position_found"));
      return;
    } 
    try {
      this.v.m.j(this.dJ + 1, i);
      return;
    } catch (Exception exception) {
      Gdx.app.error("Depot", "RequestTakeDepotItem", exception);
      return;
    } 
  }
}
