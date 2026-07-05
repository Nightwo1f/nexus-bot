package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class gl extends ClickListener {
  gl(gb paramgb, int paramInt) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    try {
      this.k.m.A(this.dF);
    } catch (Exception exception) {
      Gdx.app.error("GameUI", "Preview click", exception);
    } 
    this.k.br();
  }
}
