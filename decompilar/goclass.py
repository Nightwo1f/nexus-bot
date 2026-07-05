package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class go extends ClickListener {
  go(gb paramgb, int paramInt) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    try {
      al.a(3);
      this.n.m.z(this.dI);
    } catch (Exception exception) {
      Gdx.app.error("GameUI", "Falha ao enviar RequestTake", exception);
    } 
    this.n.br();
  }
}
