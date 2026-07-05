package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import java.util.Objects;

final class hz extends InputListener {
  hz(hy paramhy, cr paramcr) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    Runnable runnable;
    if (paramInt == 111 || paramInt == 4) {
      Objects.requireNonNull(Gdx.app);
      runnable = Gdx.app::exit;
      hy hy1;
      if ((hy1 = this.a).r == null) {
        if (runnable != null)
          runnable.run(); 
      } else {
        if (hy1.a != null)
          hy1.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.0F), 0.2F)); 
        float f1 = hy1.l.getViewport().getWorldWidth();
        float f2 = hy1.r.getY();
        al.a(2);
        hy1.r.addAction((Action)Actions.sequence((Action)Actions.moveTo(f1, f2, 0.3F), (Action)Actions.run(runnable)));
      } 
      return true;
    } 
    if ((runnable == 66 || runnable == ') && this.a.d != null && !this.a.d.isDisabled() && this.a.ci >= 0 && this.a.ci < this.a.y.size()) {
      al.a(3);
      ck ck = this.a.y.get(this.a.ci);
      this.r.setScreen((Screen)new eu(this.r, ck.L, ck.bv, this.a.n, this.a.k));
      return true;
    } 
    return false;
  }
}
