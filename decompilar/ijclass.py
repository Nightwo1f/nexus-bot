package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.TimeUtils;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;

public final class ij extends ScreenAdapter {
  private final cr s;
  
  private final Stage m;
  
  private final Texture bj;
  
  private final Image E;
  
  private int eb = 0;
  
  private long v;
  
  private final long w = 2500L;
  
  private boolean bf = false;
  
  private boolean bg = false;
  
  private boolean bh = false;
  
  public ij(cr paramcr) {
    this.s = paramcr;
    this.m = new Stage((Viewport)new ScreenViewport());
    this.bj = new Texture(Gdx.files.internal("pack1/backdrop_menu_start.png"));
    this.bj.setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    this.E = new Image(this.bj);
    this.E.setFillParent(true);
    this.E.setScaling(Scaling.fill);
    this.m.addActor((Actor)this.E);
    this.v = TimeUtils.millis();
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClearColor(0.0F, 0.0F, 0.0F, 1.0F);
    Gdx.gl.glClear(16384);
    this.m.act(paramFloat);
    this.m.draw();
    this.eb++;
    if (this.eb == 5 && !this.bf) {
      b.a();
      if (b.a())
        b.a(e.values(), this.s.f); 
      this.bf = true;
    } 
    if (this.bf && !this.bg && b.a().update())
      this.bg = true; 
    if (this.bg && !this.bh && TimeUtils.millis() - this.v >= 2500L) {
      this.bh = true;
      b.a(this.s.f);
      this.E.addAction((Action)Actions.sequence((Action)Actions.fadeOut(1.0F), (Action)Actions.run(() -> {
                this.s.setScreen((Screen)new hy(this.s));
                dispose();
              })));
    } 
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.m.getViewport().update(paramInt1, paramInt2, true);
  }
  
  public final void dispose() {
    this.m.dispose();
    this.bj.dispose();
  }
}
