package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Skin;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.viewport.ScalingViewport;
import com.badlogic.gdx.utils.viewport.Viewport;

public final class cm extends ScreenAdapter {
  private final cr c;
  
  final String R;
  
  private Stage a;
  
  private Skin a;
  
  private Texture bb;
  
  private Texture bc;
  
  private Texture bd;
  
  private Texture be;
  
  public cm(cr paramcr, String paramString) {
    this.c = paramcr;
    this.R = (paramString != null) ? paramString : "(no crash details)";
  }
  
  public final void show() {
    int i = this.c.f.a;
    int j = this.c.f.b;
    this.a = (Skin)new Stage((Viewport)new ScalingViewport(Scaling.none, i, j));
    Gdx.input.setInputProcessor((InputProcessor)this.a);
    cm cm1;
    (cm1 = this).a = new Skin();
    cm1.bb = a(Color.BLACK);
    cm1.bc = a(new Color(0.95F, 0.95F, 0.95F, 1.0F));
    cm1.bd = a(new Color(0.2F, 0.2F, 0.2F, 1.0F));
    cm1.be = a(new Color(0.12F, 0.12F, 0.12F, 1.0F));
    cm1.a.add("bg", new TextureRegionDrawable(cm1.bb), Drawable.class);
    cm1.a.add("panel", new TextureRegionDrawable(cm1.bc), Drawable.class);
    cm1.a.add("btnUp", new TextureRegionDrawable(cm1.bd), Drawable.class);
    cm1.a.add("btnDown", new TextureRegionDrawable(cm1.be), Drawable.class);
    j = (b.a != null) ? b.a : new BitmapFont();
    cm1.a.add("font", j);
    cm1.a.add("title", new Label.LabelStyle(j, Color.BLACK));
    cm1.a.add("hint", new Label.LabelStyle(j, new Color(0.15F, 0.15F, 0.15F, 1.0F)));
    cm1.a.add("content", new Label.LabelStyle(j, Color.BLACK));
    ScrollPane.ScrollPaneStyle scrollPaneStyle;
    (scrollPaneStyle = new ScrollPane.ScrollPaneStyle()).background = cm1.a.getDrawable("panel");
    cm1.a.add("default", scrollPaneStyle, ScrollPane.ScrollPaneStyle.class);
    TextButton.TextButtonStyle textButtonStyle;
    (textButtonStyle = new TextButton.TextButtonStyle()).up = cm1.a.getDrawable("btnUp");
    textButtonStyle.down = cm1.a.getDrawable("btnDown");
    textButtonStyle.font = j;
    textButtonStyle.fontColor = Color.WHITE;
    cm1.a.add("btn", textButtonStyle);
    Table table1;
    (table1 = new Table()).setFillParent(true);
    table1.setBackground(this.a.getDrawable("bg"));
    table1.pad(24.0F);
    this.a.addActor((Actor)table1);
    Table table2;
    (table2 = new Table()).setBackground(this.a.getDrawable("panel"));
    table2.pad(16.0F);
    Label label1;
    (label1 = new Label("An unexpected error occurred", this.a, "title")).setAlignment(8);
    Label label2;
    (label2 = new Label("Copy the details below and send them to support/dev.", this.a, "hint")).setAlignment(8);
    Label label3;
    (label3 = new Label(this.R, this.a, "content")).setWrap(true);
    label3.setAlignment(10);
    ScrollPane scrollPane;
    (scrollPane = new ScrollPane((Actor)label3, this.a)).setFadeScrollBars(false);
    scrollPane.setScrollingDisabled(true, false);
    scrollPane.setOverscroll(false, false);
    TextButton textButton1 = new TextButton("Copy", this.a, "btn");
    TextButton textButton2 = new TextButton("Close", this.a, "btn");
    textButton1.addListener((EventListener)new cn(this));
    textButton2.addListener((EventListener)new co(this));
    Table table3;
    (table3 = new Table()).add((Actor)textButton1).height(42.0F).width(160.0F).padRight(12.0F);
    table3.add((Actor)textButton2).height(42.0F).width(160.0F);
    float f1 = this.a.getWidth();
    float f2 = this.a.getHeight();
    f1 = Math.min(920.0F, f1 - 80.0F);
    f2 = Math.min(560.0F, f2 - 220.0F);
    table2.add((Actor)label1).growX().left().row();
    table2.add((Actor)label2).growX().left().padTop(6.0F).row();
    table2.add((Actor)scrollPane).width(f1).height(f2).padTop(12.0F).growX().row();
    table2.add((Actor)table3).padTop(12.0F).left();
    table1.add((Actor)table2).center();
    this.a.addListener((EventListener)new cp(this));
  }
  
  private static Texture a(Color paramColor) {
    Pixmap pixmap;
    (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(paramColor);
    pixmap.fill();
    Texture texture = new Texture(pixmap);
    pixmap.dispose();
    return texture;
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClearColor(0.0F, 0.0F, 0.0F, 1.0F);
    Gdx.gl.glClear(16384);
    this.a.act(paramFloat);
    this.a.draw();
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.a.getViewport().update(paramInt1, paramInt2, true);
  }
  
  public final void dispose() {
    try {
      if (this.a != null)
        this.a.dispose(); 
    } catch (Throwable throwable) {}
    try {
      if (this.a != null)
        this.a.dispose(); 
    } catch (Throwable throwable) {}
    try {
      if (this.bb != null)
        this.bb.dispose(); 
    } catch (Throwable throwable) {}
    try {
      if (this.bc != null)
        this.bc.dispose(); 
    } catch (Throwable throwable) {}
    try {
      if (this.bd != null)
        this.bd.dispose(); 
    } catch (Throwable throwable) {}
    try {
      if (this.be != null)
        this.be.dispose(); 
      return;
    } catch (Throwable throwable) {
      return;
    } 
  }
}
