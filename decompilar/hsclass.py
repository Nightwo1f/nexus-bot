package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.Preferences;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Interpolation;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Container;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ProgressBar;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Stack;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;

public final class hs extends ScreenAdapter implements bq {
  final cr o;
  
  private final Stage k;
  
  private final SpriteBatch g;
  
  private Container a;
  
  private Actor a;
  
  private Table a;
  
  private boolean ab = false;
  
  private boolean ac = false;
  
  final bf i;
  
  private final String al;
  
  private final int dU;
  
  private ProgressBar a;
  
  private Label p;
  
  private Label q;
  
  private Label r;
  
  private TextButton b;
  
  private TextButton c;
  
  private int dV = 0;
  
  private String am = "";
  
  private String an = "";
  
  private float bF = 0.0F;
  
  private boolean bd = false;
  
  private boolean be = false;
  
  public hs(cr paramcr, bf parambf, String paramString, int paramInt) {
    this.o = paramcr;
    this.i = parambf;
    this.al = paramString;
    this.dU = paramInt;
    this.k = new Stage((Viewport)new ScreenViewport());
    this.g = new SpriteBatch();
    Gdx.input.setInputProcessor((InputProcessor)this.k);
    al();
    hs hs1;
    (hs1 = this).a = (ProgressBar)new Actor();
    hs1.a.setColor(0.0F, 0.0F, 0.0F, 0.55F);
    Viewport viewport = hs1.k.getViewport();
    hs1.a.setBounds(0.0F, 0.0F, viewport.getWorldWidth(), viewport.getWorldHeight());
    hs1.a.setTouchable(Touchable.disabled);
    (hs1.a.getColor()).a = 0.0F;
    hs1.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.15F));
    hs1.k.addActor((Actor)hs1.a);
    hs1.a.toBack();
    this.a = (ProgressBar)a();
    this.a = (ProgressBar)new Container((Actor)this.a);
    this.a.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
    this.a.fill();
    this.k.addActor((Actor)this.a);
    g(true);
    al.a(1);
    this.k.addListener((EventListener)new ht(this, parambf, paramcr));
  }
  
  private void al() {
    float f = this.k.getViewport().getWorldWidth();
    boolean bool = (this.k.getViewport().getWorldHeight() > f) ? true : false;
    this.ac = bool;
  }
  
  private Table a() {
    return this.ac ? c() : b();
  }
  
  private Table b() {
    boolean bool = this.o.f.S;
    Table table2;
    (table2 = new Table()).top().left();
    Table table3 = new Table();
    if (b.f != null)
      table3.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table3.pad(0.0F);
    float f2;
    float f3 = (f2 = (b.f != null) ? Math.max(b.f.getTotalHeight(), 32.0F) : 32.0F) * 1.02F;
    float f4 = (b.c != null) ? (b.c.getWidth() / Math.max(1.0F, b.c.getHeight())) : 0.71875F;
    f4 = f3 * f4;
    Label label = lj.a(b.a(bool, "id_login"), Color.WHITE, false, 1);
    Actor actor1;
    (actor1 = new Actor()).setTouchable(Touchable.disabled);
    Actor actor2;
    (actor2 = new Actor()).setTouchable(Touchable.disabled);
    table3.add(actor1).size(f4, f3).left().padLeft(-4.0F);
    table3.add((Actor)label).expand().fill().center().minWidth(0.0F);
    table3.add(actor2).size(f4, f3).right().padRight(-4.0F);
    table2.add((Actor)table3).growX().height(f2).row();
    (table3 = new Table()).top().left();
    table3.defaults().pad(8.0F).space(0.0F).growX();
    this.q = lj.a(this.am, Color.WHITE, true, 1);
    this.r = lj.a(this.an, Color.WHITE, true, 1);
    this.r.setVisible(false);
    Stack stack2;
    (stack2 = new Stack()).add((Actor)this.q);
    stack2.add((Actor)this.r);
    table3.add((Actor)stack2).expandX().fillX().row();
    NinePatchDrawable ninePatchDrawable1;
    (ninePatchDrawable1 = new NinePatchDrawable(b.y)).setMinHeight(40.0F);
    NinePatchDrawable ninePatchDrawable2;
    (ninePatchDrawable2 = new NinePatchDrawable(b.x)).setMinHeight(34.0F);
    ProgressBar.ProgressBarStyle progressBarStyle;
    (progressBarStyle = new ProgressBar.ProgressBarStyle()).background = (Drawable)ninePatchDrawable1;
    progressBarStyle.knobBefore = (Drawable)ninePatchDrawable2;
    this.a = new ProgressBar(0.0F, 1.0F, 0.01F, false, progressBarStyle);
    this.a.setValue(this.bF);
    this.a.setAnimateDuration(0.2F);
    int i = MathUtils.clamp((int)(this.bF * 100.0F), 0, 100);
    this.p = lj.a("" + i + "%", Color.WHITE, false, 1);
    Stack stack1;
    (stack1 = new Stack()).add((Actor)this.a);
    stack1.add((Actor)this.p);
    table3.add((Actor)stack1).expandX().fillX().height(40.0F).row();
    ScrollPane scrollPane;
    a(scrollPane = new ScrollPane((Actor)table3));
    table2.add((Actor)scrollPane).grow().row();
    float f1 = Math.max(b.h.getTotalHeight() * 0.85F, 38.0F);
    String str2 = b.a(bool, "id_cancel");
    this.b = lj.b(str2);
    lj.c(this.b, str2);
    this.b.addListener((EventListener)new hu(this));
    String str1 = b.a(bool, "id_ok");
    this.c = lj.b(str1);
    lj.c(this.c, str1);
    this.c.addListener((EventListener)new hv(this));
    this.c.setVisible(false);
    Table table1;
    (table1 = new Table()).top().left();
    table1.defaults().pad(0.0F).space(0.0F).growX();
    table1.add((Actor)this.b).height(f1).left();
    table1.add().expandX().height(f1);
    table1.add((Actor)this.c).height(f1).width(160.0F).right();
    table2.add((Actor)table1).growX().row();
    bV();
    return table2;
  }
  
  private Table c() {
    boolean bool = this.o.f.S;
    Table table2;
    (table2 = new Table()).top().left();
    Table table3 = new Table();
    if (b.f != null)
      table3.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table3.pad(0.0F);
    float f1;
    float f2 = (f1 = cq.b()) * 0.8F;
    float f3 = (b.c != null) ? (b.c.getWidth() / Math.max(1.0F, b.c.getHeight())) : 0.71875F;
    f3 = f2 * f3;
    Label label;
    (label = lj.a(b.a(bool, "id_login"), Color.WHITE, false, 1)).setFontScale(2.0F);
    Actor actor1;
    (actor1 = new Actor()).setTouchable(Touchable.disabled);
    Actor actor2;
    (actor2 = new Actor()).setTouchable(Touchable.disabled);
    table3.add(actor1).size(f3, f2).left().padLeft(15.0F);
    table3.add((Actor)label).expand().fill().center().minWidth(0.0F);
    table3.add(actor2).size(f3, f2).right().padRight(15.0F);
    table2.add((Actor)table3).growX().height(f1).row();
    (table3 = new Table()).top().left();
    table3.defaults().pad(15.0F).space(0.0F).growX();
    this.q = lj.a(this.am, Color.WHITE, true, 1);
    this.q.setFontScale(1.5F);
    this.r = lj.a(this.an, Color.WHITE, true, 1);
    this.r.setFontScale(1.5F);
    this.r.setVisible(false);
    Stack stack3;
    (stack3 = new Stack()).add((Actor)this.q);
    stack3.add((Actor)this.r);
    table3.add((Actor)stack3).expandX().fillX().padBottom(30.0F).row();
    NinePatchDrawable ninePatchDrawable1;
    (ninePatchDrawable1 = new NinePatchDrawable(b.y)).setMinHeight(70.0F);
    NinePatchDrawable ninePatchDrawable2;
    (ninePatchDrawable2 = new NinePatchDrawable(b.x)).setMinHeight(64.0F);
    ProgressBar.ProgressBarStyle progressBarStyle;
    (progressBarStyle = new ProgressBar.ProgressBarStyle()).background = (Drawable)ninePatchDrawable1;
    progressBarStyle.knobBefore = (Drawable)ninePatchDrawable2;
    this.a = new ProgressBar(0.0F, 1.0F, 0.01F, false, progressBarStyle);
    this.a.setValue(this.bF);
    this.a.setAnimateDuration(0.2F);
    int i = MathUtils.clamp((int)(this.bF * 100.0F), 0, 100);
    this.p = lj.a("" + i + "%", Color.WHITE, false, 1);
    this.p.setFontScale(1.5F);
    Stack stack2;
    (stack2 = new Stack()).add((Actor)this.a);
    stack2.add((Actor)this.p);
    table3.add((Actor)stack2).expandX().fillX().height(70.0F).row();
    ScrollPane scrollPane;
    a(scrollPane = new ScrollPane((Actor)table3));
    table2.add((Actor)scrollPane).grow().row();
    String str2 = b.a(bool, "id_cancel");
    this.b = lj.b(str2);
    lj.c(this.b, str2);
    this.b.getLabel().setFontScale(1.5F);
    this.b.addListener((EventListener)new hw(this));
    String str1 = b.a(bool, "id_ok");
    this.c = lj.b(str1);
    lj.c(this.c, str1);
    this.c.getLabel().setFontScale(1.5F);
    this.c.addListener((EventListener)new hx(this));
    this.c.setVisible(false);
    Table table1;
    (table1 = new Table()).defaults().growX().height(110.0F).pad(10.0F);
    Stack stack1;
    (stack1 = new Stack()).add((Actor)this.b);
    stack1.add((Actor)this.c);
    table1.add((Actor)stack1).growX();
    table2.add((Actor)table1).growX().padBottom(10.0F).row();
    bV();
    return table2;
  }
  
  final void bU() {
    cj.d(this.dV, this.r.getText().toString());
    this.bd = false;
    bV();
    if (this.i != null)
      this.i.x(); 
  }
  
  private void bV() {
    if (this.bd) {
      this.r.setVisible(true);
      this.c.setVisible(true);
      this.a.setVisible(false);
      if (this.p != null)
        this.p.setVisible(false); 
      this.b.setVisible(false);
      this.q.setVisible(false);
      return;
    } 
    if (this.be) {
      this.q.setVisible(true);
      this.b.setVisible(true);
      this.a.setVisible(false);
      if (this.p != null)
        this.p.setVisible(false); 
      this.r.setVisible(false);
      this.c.setVisible(false);
      return;
    } 
    this.r.setVisible(false);
    this.c.setVisible(false);
    this.a.setVisible(true);
    if (this.p != null)
      this.p.setVisible(true); 
    this.b.setVisible(true);
    this.q.setVisible(true);
  }
  
  private static void a(ScrollPane paramScrollPane) {
    paramScrollPane.setFadeScrollBars(false);
    paramScrollPane.setScrollingDisabled(true, false);
    paramScrollPane.setForceScroll(false, true);
    paramScrollPane.setOverscroll(false, false);
    paramScrollPane.setFlickScroll(true);
    paramScrollPane.setSmoothScrolling(true);
    paramScrollPane.setTouchable(Touchable.enabled);
  }
  
  public final void e(String paramString) {
    String str = paramString;
    hs hs1 = this;
    Gdx.app.postRunnable(() -> {
          this.am = paramString;
          b.a(this.q, paramString);
          if (!this.bd && !this.be)
            this.q.setVisible(true); 
        });
  }
  
  public final void d(float paramFloat) {
    Gdx.app.postRunnable(() -> {
          this.bF = paramFloat;
          if (this.a != null)
            this.a.setValue(paramFloat); 
          if (this.p != null) {
            int i = MathUtils.clamp((int)(paramFloat * 100.0F), 0, 100);
            this.p.setText("" + i + "%");
          } 
          if (!this.bd && !this.be)
            bV(); 
        });
  }
  
  public final void b(int paramInt, String paramString) {
    Gdx.app.postRunnable(() -> {
          this.dV = paramInt;
          if (paramInt > 0) {
            switch (paramInt) {
              case 2:
              
              default:
                if (paramInt > cj.a().getInteger("last_news_id", 0));
                break;
            } 
            if (false) {
              this.an = (paramString != null) ? paramString : "";
              b.a(this.r, this.an);
              this.bd = true;
              this.be = false;
              bV();
              return;
            } 
            cj.d(paramInt, paramString);
            if (this.i != null)
              this.i.x(); 
            return;
          } 
          break;
        });
  }
  
  public final void c(int paramInt, String paramString) {
    Gdx.app.postRunnable(() -> {
          this.am = (paramString != null) ? paramString : "";
          b.a(this.q, this.am);
          this.be = true;
          this.bd = false;
          bV();
          String str = paramString;
          int i = paramInt;
          Preferences preferences;
          (preferences = cj.a()).putInteger("last_error_id", Math.max(0, i));
          if (str != null)
            preferences.putString("last_error_text", str); 
          preferences.flush();
        });
  }
  
  private void g(boolean paramBoolean) {
    Viewport viewport;
    float f2 = (viewport = this.k.getViewport()).getWorldWidth();
    float f1 = viewport.getWorldHeight();
    if (this.ac) {
      f3 = f2 * 0.95F;
      f4 = f1 * 0.9F;
    } else {
      f3 = Math.min(680.0F, f2 * 0.95F);
      f4 = Math.min(510.0F, f1 * 0.95F);
    } 
    float f3 = Math.round(f3);
    float f4 = Math.round(f4);
    if (this.a != null)
      this.a.setBounds(0.0F, 0.0F, f2, f1); 
    if (this.a != null) {
      this.a.clearActions();
      this.a.setSize(f3, f4);
      f3 = Math.round((f2 - f3) * 0.5F);
      f1 = Math.round((f1 - f4) * 0.5F);
      if (paramBoolean && !this.ab) {
        this.a.setPosition(f2, f1);
        this.a.addAction((Action)Actions.moveTo(f3, f1, 0.3F, Interpolation.smooth));
        this.ab = true;
        return;
      } 
      this.a.setPosition(f3, f1);
    } 
  }
  
  final void f(Runnable paramRunnable) {
    if (this.a == null) {
      if (paramRunnable != null)
        paramRunnable.run(); 
      return;
    } 
    if (this.a != null)
      this.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.0F), 0.2F)); 
    float f1 = this.k.getViewport().getWorldWidth();
    float f2 = this.a.getY();
    al.a(2);
    this.a.addAction((Action)Actions.sequence((Action)Actions.moveTo(f1, f2, 0.3F, Interpolation.smooth), (Action)Actions.run(paramRunnable)));
  }
  
  public final void show() {
    super.show();
    Gdx.input.setInputProcessor((InputProcessor)this.k);
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClear(16384);
    this.g.setProjectionMatrix((this.k.getCamera()).combined);
    this.g.begin();
    this.g.draw((Texture)b.b, 0.0F, 0.0F, this.k.getViewport().getWorldWidth(), this.k.getViewport().getWorldHeight());
    this.g.end();
    this.k.act(paramFloat);
    this.k.draw();
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.k.getViewport().update(paramInt1, paramInt2, true);
    boolean bool = this.ac;
    al();
    hs hs1;
    if (bool != this.ac && (hs1 = this).a != null) {
      hs1.a.setActor(null);
      hs1.a = (ProgressBar)hs1.a();
      hs1.a.setActor((Actor)hs1.a);
      hs1.g(false);
    } 
    g(false);
  }
  
  public final void dispose() {
    this.k.dispose();
    this.g.dispose();
  }
}
