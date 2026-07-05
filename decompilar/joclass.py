package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class jo extends ClickListener {
  private final Runnable i;
  
  private final Table E;
  
  private final int ei;
  
  private final float bV;
  
  private float x;
  
  private float y;
  
  private boolean br;
  
  jo(Runnable paramRunnable, Table paramTable, int paramInt, float paramFloat) {
    this.i = paramRunnable;
    this.E = paramTable;
    this.ei = paramInt;
    this.bV = paramFloat;
  }
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    this.br = false;
    this.x = paramInputEvent.getStageX();
    this.y = paramInputEvent.getStageY();
    in.a(this.E, this.ei, true);
    return super.touchDown(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void touchDragged(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    float f1 = Math.abs(paramInputEvent.getStageX() - this.x);
    float f2 = Math.abs(paramInputEvent.getStageY() - this.y);
    if (!this.br && (f1 > this.bV || f2 > this.bV)) {
      this.br = true;
      in.a(this.E, this.ei, false);
    } 
    super.touchDragged(paramInputEvent, paramFloat1, paramFloat2, paramInt);
  }
  
  public final void touchUp(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    in.a(this.E, this.ei, false);
    super.touchUp(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (!this.br && this.i != null)
      this.i.run(); 
  }
}
