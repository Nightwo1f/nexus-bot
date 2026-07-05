package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class fq extends ClickListener {
  fq(fj paramfj, az paramaz) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    this.j.aL();
    Gdx.app.postRunnable(() -> this.j.a.p(paramaz.s));
  }
}
