package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Interpolation;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Container;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public final class em extends ScreenAdapter implements ik {
  final cr i;
  
  final Stage g;
  
  private final SpriteBatch d;
  
  private final br j;
  
  private final bf f;
  
  private Container a;
  
  private Actor a;
  
  private Table a;
  
  private boolean ab = false;
  
  private boolean ac = false;
  
  private final List p = new ArrayList();
  
  final List q = new ArrayList();
  
  int ci = -1;
  
  Label b;
  
  public em(cr paramcr, br parambr, bf parambf) {
    this.i = paramcr;
    this.j = parambr;
    this.f = parambf;
    this.d = new SpriteBatch();
    this.g = new Stage((Viewport)new ScreenViewport());
    Gdx.input.setInputProcessor((InputProcessor)this.g);
    al();
    em em1;
    (em1 = this).p.clear();
    em1.p.add(new et(1, 1, (TextureRegion)b.d, "id_warrior_description"));
    em1.p.add(new et(1, 2, (TextureRegion)b.e, "id_warrior_description"));
    em1.p.add(new et(2, 1, (TextureRegion)b.f, "id_wizard_description"));
    em1.p.add(new et(2, 2, b.g, "id_wizard_description"));
    (em1 = this).a = (Table)new Actor();
    em1.a.setColor(0.0F, 0.0F, 0.0F, 0.55F);
    Viewport viewport = em1.g.getViewport();
    em1.a.setBounds(0.0F, 0.0F, viewport.getWorldWidth(), viewport.getWorldHeight());
    em1.a.setTouchable(Touchable.disabled);
    (em1.a.getColor()).a = 0.0F;
    em1.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.15F));
    em1.g.addActor((Actor)em1.a);
    em1.a.toBack();
    this.a = a();
    this.a = (Table)new Container((Actor)this.a);
    this.a.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
    this.a.fill();
    this.a.pad(b.d.getTopHeight(), b.d.getLeftWidth(), b.d.getBottomHeight(), b.d.getRightWidth());
    this.g.addActor((Actor)this.a);
    g(true);
    al.a(1);
    this.g.addListener((EventListener)new en(this, paramcr));
  }
  
  private void al() {
    float f1 = this.g.getViewport().getWorldWidth();
    float f2 = this.g.getViewport().getWorldHeight();
    this.ac = (f2 > f1);
  }
  
  private static TextButton a(String paramString) {
    TextButton.TextButtonStyle textButtonStyle;
    (textButtonStyle = new TextButton.TextButtonStyle()).font = b.a((paramString != null) ? paramString : "");
    if (b.m != null) {
      textButtonStyle.up = (Drawable)new NinePatchDrawable((NinePatch)b.m);
      textButtonStyle.over = textButtonStyle.up;
    } 
    if (b.n != null) {
      textButtonStyle.down = (Drawable)new NinePatchDrawable((NinePatch)b.n);
    } else if (b.m != null) {
      textButtonStyle.down = (Drawable)new NinePatchDrawable((NinePatch)b.m);
    } 
    TextButton textButton;
    (textButton = new TextButton((paramString != null) ? paramString : "", textButtonStyle)).getLabel().setAlignment(1);
    textButton.getLabel().setWrap(false);
    return textButton;
  }
  
  private Table a() {
    return this.ac ? c() : b();
  }
  
  private Table b() {
    boolean bool = this.i.f.S;
    Table table1;
    (table1 = new Table()).top().left();
    Table table2 = new Table();
    if (b.f != null)
      table2.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table2.pad(0.0F);
    float f2;
    float f3 = (f2 = (b.f != null) ? Math.max(b.f.getTotalHeight(), 32.0F) : 32.0F) * 1.02F;
    float f4 = (b.c != null) ? (b.c.getWidth() / Math.max(1.0F, b.c.getHeight())) : 0.71875F;
    f4 = f3 * f4;
    ImageButton.ImageButtonStyle imageButtonStyle;
    (imageButtonStyle = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.c));
    if (b.d != null) {
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.d));
    } else {
      imageButtonStyle.imageDown = imageButtonStyle.imageUp;
    } 
    ImageButton imageButton;
    (imageButton = new ImageButton(imageButtonStyle)).getImage().setScaling(Scaling.fit);
    imageButton.getImageCell().pad(0.0F).expand().fill();
    imageButton.addListener((EventListener)new eo(this));
    Label label = lj.a(b.a(bool, "id_new_game_vocation"), Color.WHITE, false, 1);
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table2.add((Actor)imageButton).size(f4, f3).left().padLeft(-4.0F);
    table2.add((Actor)label).expand().fill().center().minWidth(0.0F);
    table2.add(actor).size(f4, f3).right().padRight(-4.0F);
    table1.add((Actor)table2).growX().height(f2).row();
    (table2 = new Table()).top().left();
    table2.defaults().pad(8.0F).space(0.0F).growX();
    ScrollPane scrollPane2 = a(bool, 3.2F);
    f3 = b.B.getTotalWidth() * 3.2F + 16.0F;
    table2.add((Actor)scrollPane2).growX().height(f3).row();
    String str2 = b.a(bool, ((et)this.p.get(0)).ae);
    this.b = lj.a(str2, Color.WHITE, true, 8);
    Table table3;
    (table3 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.v));
    table3.add((Actor)this.b).growX().pad(10.0F).minHeight(72.0F);
    table2.add((Actor)table3).growX().row();
    ScrollPane scrollPane1;
    a(scrollPane1 = new ScrollPane((Actor)table2));
    table1.add((Actor)scrollPane1).grow().row();
    float f1 = Math.max(b.h.getTotalHeight() * 0.85F, 38.0F);
    String str1;
    TextButton textButton;
    (textButton = a(((str1 = b.a(bool, "id_ok")) != null) ? str1 : "OK")).addListener((EventListener)new ep(this));
    (table3 = new Table()).top().left();
    table3.defaults().pad(0.0F).space(0.0F).growX();
    table3.add().expandX().height(f1);
    table3.add((Actor)textButton).height(f1).width(160.0F).right();
    table1.add((Actor)table3).growX().row();
    return table1;
  }
  
  private Table c() {
    boolean bool = this.i.f.S;
    Table table1;
    (table1 = new Table()).top().left();
    Table table3 = new Table();
    if (b.f != null)
      table3.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table3.pad(0.0F);
    float f1;
    float f2 = (f1 = cq.b()) * 0.8F;
    float f3 = (b.c != null) ? (b.c.getWidth() / Math.max(1.0F, b.c.getHeight())) : 0.71875F;
    f3 = f2 * f3;
    ImageButton.ImageButtonStyle imageButtonStyle;
    (imageButtonStyle = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.c));
    if (b.d != null) {
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.d));
    } else {
      imageButtonStyle.imageDown = imageButtonStyle.imageUp;
    } 
    ImageButton imageButton;
    (imageButton = new ImageButton(imageButtonStyle)).getImage().setScaling(Scaling.fit);
    imageButton.getImageCell().pad(0.0F).expand().fill();
    imageButton.addListener((EventListener)new eq(this));
    Label label;
    (label = lj.a(b.a(bool, "id_new_game_vocation"), Color.WHITE, false, 1)).setFontScale(2.0F);
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table3.add((Actor)imageButton).size(f3, f2).left().padLeft(15.0F);
    table3.add((Actor)label).expand().fill().center().minWidth(0.0F);
    table3.add(actor).size(f3, f2).right().padRight(15.0F);
    table1.add((Actor)table3).growX().height(f1).row();
    (table3 = new Table()).top().left();
    table3.defaults().pad(10.0F).space(15.0F).growX();
    ScrollPane scrollPane2 = a(bool, 4.8F);
    f2 = b.B.getTotalWidth() * 4.8F + 20.0F;
    table3.add((Actor)scrollPane2).growX().height(f2).row();
    String str2 = b.a(bool, ((et)this.p.get(0)).ae);
    this.b = lj.a(str2, Color.WHITE, true, 8);
    this.b.setFontScale(1.5F);
    Table table4;
    (table4 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.v));
    table4.add((Actor)this.b).growX().pad(15.0F).minHeight(100.0F);
    table3.add((Actor)table4).growX().row();
    ScrollPane scrollPane1;
    a(scrollPane1 = new ScrollPane((Actor)table3));
    table1.add((Actor)scrollPane1).grow().row();
    TextButton textButton;
    String str1;
    (textButton = a(((str1 = b.a(bool, "id_ok")) != null) ? str1 : "OK")).getLabel().setFontScale(1.5F);
    textButton.addListener((EventListener)new er(this));
    Table table2;
    (table2 = new Table()).defaults().growX().height(110.0F);
    table2.add((Actor)textButton).pad(10.0F);
    table1.add((Actor)table2).growX().padBottom(10.0F).row();
    return table1;
  }
  
  private ScrollPane a(String paramString, float paramFloat) {
    this.q.clear();
    float f = (paramFloat = b.B.getTotalWidth() * paramFloat) * 0.1F;
    NinePatchDrawable ninePatchDrawable1 = new NinePatchDrawable(b.B);
    NinePatchDrawable ninePatchDrawable2 = new NinePatchDrawable(b.C);
    Table table2;
    (table2 = new Table()).top().left();
    table2.defaults().size(paramFloat, paramFloat).pad(f);
    for (byte b = 0; b < this.p.size(); b++) {
      byte b1 = b;
      et et = this.p.get(b);
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable1;
      imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(et.D);
      imageButtonStyle.imageDown = imageButtonStyle.imageUp;
      ImageButton imageButton;
      (imageButton = new ImageButton(imageButtonStyle)).getImage().setScaling(Scaling.fit);
      imageButton.getImageCell().pad(paramFloat * 0.1F);
      this.q.add(imageButton);
      imageButton.addListener((EventListener)new es(this, ninePatchDrawable1, ninePatchDrawable2, b1, et, paramString));
      table2.add((Actor)imageButton);
    } 
    if (!this.q.isEmpty()) {
      (((ImageButton)this.q.get(0)).getStyle()).up = (Drawable)ninePatchDrawable2;
      (((ImageButton)this.q.get(0)).getStyle()).down = (Drawable)ninePatchDrawable2;
      this.ci = 0;
    } 
    Table table1;
    (table1 = new Table()).top().left();
    table1.add().expandX().fillX();
    table1.add((Actor)table2);
    table1.add().expandX().fillX();
    ScrollPane scrollPane;
    (scrollPane = new ScrollPane((Actor)table1)).setFadeScrollBars(false);
    scrollPane.setScrollingDisabled(false, true);
    scrollPane.setForceScroll(true, false);
    scrollPane.setOverscroll(false, false);
    scrollPane.setFlickScroll(true);
    scrollPane.setSmoothScrolling(true);
    scrollPane.setTouchable(Touchable.enabled);
    return scrollPane;
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
  
  final void aC() {
    if (this.ci < 0 || this.ci >= this.p.size()) {
      kx.a(this.g, b.a(this.i.f.S, "id_select_vocation_first"));
      return;
    } 
    et et = this.p.get(this.ci);
    al.a(3);
    int j = et.ck;
    int i = et.cl;
    cq cq;
    (cq = this.i.f).S = true;
    cq.bT = j;
    cq.bU = i;
    try {
      this.f.a(cq.V, cq.bM);
      this.f.a(cq.bJ, cq.S, cq.T, cq.bK);
      this.f.s(cq.cb);
    } catch (IOException iOException) {
      this.f.y();
      return;
    } 
    Gdx.app.postRunnable(() -> this.i.setScreen((Screen)new dy(this.i, paramcq.bT, paramcq.bU, this.j, this.f)));
  }
  
  private void g(boolean paramBoolean) {
    Viewport viewport;
    float f2 = (viewport = this.g.getViewport()).getWorldWidth();
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
  
  final void c(Runnable paramRunnable) {
    if (this.a == null) {
      if (paramRunnable != null)
        paramRunnable.run(); 
      return;
    } 
    if (this.a != null)
      this.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.0F), 0.2F)); 
    float f1 = this.g.getViewport().getWorldWidth();
    float f2 = this.a.getY();
    al.a(2);
    this.a.addAction((Action)Actions.sequence((Action)Actions.moveTo(f1, f2, 0.3F, Interpolation.smooth), (Action)Actions.run(paramRunnable)));
  }
  
  public final void show() {
    super.show();
    Gdx.input.setInputProcessor((InputProcessor)this.g);
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClear(16384);
    this.d.setProjectionMatrix((this.g.getCamera()).combined);
    this.d.begin();
    this.d.draw((Texture)b.b, 0.0F, 0.0F, this.g.getViewport().getWorldWidth(), this.g.getViewport().getWorldHeight());
    this.d.end();
    this.g.act(paramFloat);
    this.g.draw();
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.g.getViewport().update(paramInt1, paramInt2, true);
    boolean bool = this.ac;
    al();
    em em1;
    if (bool != this.ac && (em1 = this).a != null) {
      em1.a.setActor(null);
      em1.a = em1.a();
      em1.a.setActor((Actor)em1.a);
      em1.g(false);
    } 
    g(false);
  }
  
  public final void dispose() {
    this.g.dispose();
    this.d.dispose();
  }
  
  public final Stage a() {
    return this.g;
  }
}
