package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gs extends ClickListener {
  gs(gb paramgb) {}
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    gs gs1;
    if ((gs1 = this).r.e != null) {
      gs1.r.e.clearActions();
      (gs1.r.e.getColor()).a = 0.85F;
      gs1.r.e.setVisible(true);
      gs1.r.e.setZIndex(Math.max(0, gs1.r.p.getZIndex() - 1));
      gs1.r.p.toFront();
      if (gs1.r.a != null)
        gs1.r.a.toFront(); 
    } 
    return super.touchDown(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void touchUp(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    gs gs1;
    if ((gs1 = this).r.e != null) {
      gs1.r.e.clearActions();
      gs1.r.e.setVisible(false);
      (gs1.r.e.getColor()).a = 1.0F;
    } 
    super.touchUp(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void touchDragged(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    if (this.r.e == null)
      return; 
    boolean bool = (paramFloat1 >= 0.0F && paramFloat1 <= this.r.p.getWidth() && paramFloat2 >= 0.0F && paramFloat2 <= this.r.p.getHeight()) ? true : false;
    this.r.e.setVisible(bool);
  }
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    al.a(3);
    this.r.m.n(0, 14);
  }
}
