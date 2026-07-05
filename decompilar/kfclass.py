package a;

import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;

final class kf extends ClickListener {
  kf(jz paramjz, Table paramTable, Runnable paramRunnable) {}
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    if (b.i != null)
      this.I.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.i)); 
    return super.touchDown(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void touchUp(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    if (b.h != null)
      this.I.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.h)); 
    super.touchUp(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (this.r != null)
      this.r.run(); 
  }
}
