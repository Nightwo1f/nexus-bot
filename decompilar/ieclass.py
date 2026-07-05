package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.Button;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class ie extends ClickListener {
  ie(hy paramhy, int paramInt) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.f.ci = this.dX;
    al.a(3);
    for (byte b = 0; b < this.f.z.size(); b++)
      ((Button)this.f.z.get(b)).setChecked((b == this.f.ci)); 
    this.f.bZ();
  }
}
