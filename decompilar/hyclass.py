package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.Net;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.Event;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Button;
import com.badlogic.gdx.scenes.scene2d.ui.Container;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.ui.Value;
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public final class hy extends ScreenAdapter {
  final cr q;
  
  final Stage l;
  
  private final SpriteBatch h;
  
  final bf k;
  
  final br n;
  
  private final Texture bi;
  
  Table r;
  
  Actor a;
  
  private Table a;
  
  private boolean ab = false;
  
  private final List x;
  
  private boolean ac = false;
  
  final float bG = Math.max(b.h.getTotalHeight(), 44.0F) + 16.0F;
  
  private final float bH = 110.0F;
  
  final List y;
  
  int ci = -1;
  
  final List z = new ArrayList();
  
  private ImageButton x = (ImageButton)new ArrayList();
  
  private ImageButton y = (ImageButton)new ArrayList();
  
  TextButton d;
  
  private TextButton e;
  
  private TextButton f;
  
  Table s;
  
  private ScrollPane e;
  
  private Label s;
  
  private void bW() {
    Iterator<Texture> iterator = this.x.iterator();
    while (iterator.hasNext()) {
      Texture texture;
      if ((texture = iterator.next()) != null)
        texture.dispose(); 
    } 
    this.x.clear();
  }
  
  public hy(cr paramcr) {
    this.q = paramcr;
    this.l = new Stage((Viewport)new ScreenViewport());
    this.h = new SpriteBatch();
    this.k = paramcr.a.a();
    this.n = paramcr.a.a();
    this.k.b = (File)this.n;
    Gdx.input.setInputProcessor((InputProcessor)this.l);
    this.y.addAll(paramcr.f.n);
    this.bi = new Texture(Gdx.files.internal("pack1/backdrop_menuscreen_125.png"));
    this.bi.setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    al();
    hy hy2 = this;
    ImageButton.ImageButtonStyle imageButtonStyle = new ImageButton.ImageButtonStyle();
    if (b.B != null)
      imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable((Texture)b.B); 
    if (b.C != null)
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable((Texture)b.C); 
    hy2.x = new ImageButton(imageButtonStyle);
    hy2.x.addListener(paramEvent -> {
          if (cv.a(paramEvent)) {
            al.a(3);
            cv.a(this.q, this.l);
            return true;
          } 
          return false;
        });
    Texture texture = b.a(hy2.q.f.S);
    hy2.y = new ImageButton((Drawable)new TextureRegionDrawable(new TextureRegion(texture)));
    hy2.y.addListener(paramEvent -> {
          if (!cv.a(paramEvent))
            return false; 
          String str = b.b(this.q.f.S);
          this.q.f.o(str);
          Texture texture = b.a(str);
          TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(new TextureRegion(texture));
          ImageButton.ImageButtonStyle imageButtonStyle;
          (imageButtonStyle = this.y.getStyle()).imageUp = (Drawable)textureRegionDrawable;
          imageButtonStyle.imageDown = (Drawable)textureRegionDrawable;
          al.a(3);
          bY();
          return true;
        });
    hy2.l.addActor((Actor)hy2.x);
    hy2.l.addActor((Actor)hy2.y);
    hy2.bX();
    this.a = a();
    (hy2 = this).a = (Table)new Actor();
    hy2.a.setColor(0.0F, 0.0F, 0.0F, 0.55F);
    Viewport viewport = hy2.l.getViewport();
    hy2.a.setBounds(0.0F, 0.0F, viewport.getWorldWidth(), viewport.getWorldHeight());
    hy2.a.setTouchable(Touchable.disabled);
    (hy2.a.getColor()).a = 0.0F;
    hy2.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.15F));
    hy2.l.addActor((Actor)hy2.a);
    hy2.a.toBack();
    this.r = new Table();
    NinePatchDrawable ninePatchDrawable = new NinePatchDrawable((NinePatch)b.d);
    this.r.setBackground((Drawable)ninePatchDrawable);
    this.r.pad(b.d.getTopHeight(), b.d.getLeftWidth(), b.d.getBottomHeight(), b.d.getRightWidth());
    this.r.add((Actor)this.a).grow();
    this.l.addActor((Actor)this.r);
    g(true);
    hy hy1 = this;
    boolean bool = System.getProperty("os.name").toLowerCase().contains("win");
    if (hy1.q.f.Z && Gdx.app.getType() == Application.ApplicationType.Desktop && bool) {
      Net.HttpRequest httpRequest;
      (httpRequest = new Net.HttpRequest("GET")).setUrl(hy1.q.f.aa);
      Gdx.net.sendHttpRequest(httpRequest, new if(hy1));
    } 
    int i;
    String str = "Version " + (i = paramcr.f.bJ) / 100 + "." + String.format("%02d", new Object[] { Integer.valueOf(i % 100) });
    this.s = lj.a(str, new Color(1.0F, 1.0F, 1.0F, 0.7F), false, 8);
    this.l.addActor((Actor)this.s);
    al.a(1);
    this.l.addListener((EventListener)new hz(this, paramcr));
  }
  
  private void al() {
    float f = this.l.getViewport().getWorldWidth();
    boolean bool = (this.l.getViewport().getWorldHeight() > f) ? true : false;
    this.ac = bool;
  }
  
  static TextButton a(String paramString) {
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
  
  private ScrollPane.ScrollPaneStyle a() {
    ScrollPane.ScrollPaneStyle scrollPaneStyle = new ScrollPane.ScrollPaneStyle();
    if (b.b != null)
      scrollPaneStyle.vScroll = (Drawable)new NinePatchDrawable((NinePatch)b.b); 
    if (b.c != null)
      scrollPaneStyle.vScrollKnob = (Drawable)new NinePatchDrawable((NinePatch)b.c); 
    float f = this.ac ? 25.0F : 20.0F;
    if (scrollPaneStyle.vScroll instanceof BaseDrawable)
      ((BaseDrawable)scrollPaneStyle.vScroll).setMinWidth(f); 
    if (scrollPaneStyle.vScrollKnob instanceof BaseDrawable) {
      ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinWidth(f);
      ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinHeight(f + 10.0F);
    } 
    return scrollPaneStyle;
  }
  
  private void bX() {
    Viewport viewport;
    float f2 = (viewport = this.l.getViewport()).getWorldWidth();
    float f1 = viewport.getWorldHeight();
    float f3 = this.q.f.bP;
    this.x.setSize(f3, f3);
    this.y.setSize(f3, f3);
    this.x.getImageCell().expand().fill();
    this.x.getImage().setScaling(Scaling.fill);
    this.y.getImageCell().expand().fill();
    this.y.getImage().setScaling(Scaling.fill);
    this.x.setPosition(Math.round(f2 - f3 - 20.0F), Math.round(f1 - f3 - 20.0F));
    this.y.setPosition(Math.round(this.x.getX() - 15.0F - f3), Math.round(this.x.getY()));
  }
  
  private Table a() {
    return this.ac ? c() : b();
  }
  
  private Table b() {
    boolean bool = this.q.f.S;
    Table table2;
    (table2 = new Table()).top().left();
    Table table3;
    (table3 = new Table()).top().left();
    table3.defaults().pad(0.0F).space(8.0F);
    float f = (b.f != null) ? Math.max(b.f.getTotalHeight(), 32.0F) : 32.0F;
    Table table4 = new Table();
    if (b.f != null)
      table4.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    String str2;
    if ((str2 = b.a(bool, "id_characters")) == null)
      str2 = "Characters"; 
    Label label2 = lj.a(str2, Color.WHITE, false, 1);
    table4.add((Actor)label2).expandX().fillX().center();
    Table table5 = new Table();
    if (b.f != null)
      table5.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    String str1;
    if ((str1 = b.a(bool, "id_news")) == null)
      str1 = "Server News"; 
    Label label1 = lj.a(str1, Color.WHITE, false, 1);
    table5.add((Actor)label1).expandX().fillX().center();
    table3.add((Actor)table4).width(Value.percentWidth(0.55F, (Actor)table3)).minWidth(0.0F).height(f);
    table3.add((Actor)table5).width(Value.percentWidth(0.45F, (Actor)table3)).minWidth(0.0F).height(f);
    table2.add((Actor)table3).growX().row();
    Table table1;
    (table1 = new Table()).top().left();
    table1.defaults().pad(0.0F).space(8.0F).growY().minWidth(0.0F);
    this.s = (Label)new Table();
    this.s.top().left();
    this.s.defaults().pad(0.0F).space(0.0F).growX();
    this.z.clear();
    this.e = a();
    this.s.add((Actor)this.e).grow().minWidth(0.0F).row();
    table3 = a(false);
    Math.max(b.h.getTotalHeight() * 0.85F, 38.0F);
    this.s.add((Actor)table3).growX().minWidth(0.0F).row();
    table3 = e();
    table1.add((Actor)this.s).width(Value.percentWidth(0.55F, (Actor)table1)).minWidth(0.0F).growY();
    table1.add((Actor)table3).width(Value.percentWidth(0.45F, (Actor)table1)).minWidth(0.0F).growY();
    table2.add((Actor)table1).grow().row();
    bZ();
    return table2;
  }
  
  private Table c() {
    boolean bool1 = this.q.f.S;
    Table table2;
    (table2 = new Table()).top().left();
    Table table3 = new Table();
    if (b.f != null)
      table3.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    boolean bool2 = cq.Z;
    String str;
    if ((str = b.a(bool1, "id_characters")) == null)
      str = "Characters"; 
    Label label;
    (label = lj.a(str, Color.WHITE, false, 1)).setFontScale(2.0F);
    table3.add((Actor)label).expandX().fillX().center();
    table2.add((Actor)table3).growX().height(bool2).padBottom(5.0F).row();
    this.s = (Label)new Table();
    this.z.clear();
    this.e = a();
    table2.add((Actor)this.e).grow().padBottom(15.0F).row();
    Table table1 = a(true);
    table2.add((Actor)table1).fillX().padBottom(15.0F).row();
    table1 = e();
    table2.add((Actor)table1).fillX().height(Value.percentHeight(0.25F, (Actor)table2)).row();
    bZ();
    return table2;
  }
  
  private ScrollPane a() {
    ScrollPane scrollPane;
    (scrollPane = new ScrollPane((Actor)f(), a())).setFadeScrollBars(false);
    scrollPane.setScrollingDisabled(true, false);
    scrollPane.setForceScroll(false, true);
    scrollPane.setOverscroll(false, true);
    scrollPane.setFlickScroll(true);
    scrollPane.setSmoothScrolling(true);
    scrollPane.setTouchable(Touchable.enabled);
    return scrollPane;
  }
  
  private Table a(boolean paramBoolean) {
    boolean bool = this.q.f.S;
    Table table;
    (table = new Table()).top();
    table.defaults().pad(0.0F).space(5.0F).growX();
    float f2 = paramBoolean ? 110.0F : Math.max(b.h.getTotalHeight() * 0.85F, 38.0F);
    float f1 = paramBoolean ? 1.5F : 1.0F;
    String str2;
    if ((str2 = b.a(bool, "id_start_game")) == null || str2.isEmpty())
      str2 = b.a(bool, "id_play"); 
    this.d = a(str2);
    this.d.setColor(0.65F, 1.0F, 0.65F, 1.0F);
    this.d.getLabel().setEllipsis(true);
    this.d.getLabel().setFontScale(f1);
    this.d.addListener((EventListener)new ia(this));
    if ((str2 = b.a(bool, "id_create_character")) == null || str2.isEmpty())
      str2 = "Create Character"; 
    this.e = (ScrollPane)a(str2);
    this.e.getLabel().setEllipsis(true);
    this.e.getLabel().setFontScale(f1);
    this.e.addListener((EventListener)new ib(this));
    String str1;
    if ((str1 = b.a(bool, "id_add_character_name")) == null || str1.isEmpty())
      str1 = "Add Character"; 
    this.f = a(str1);
    this.f.getLabel().setEllipsis(true);
    this.f.getLabel().setFontScale(f1);
    this.f.addListener((EventListener)new ic(this));
    table.add((Actor)this.d).height(f2).row();
    table.add((Actor)this.e).height(f2).row();
    table.add((Actor)this.f).height(f2).row();
    return table;
  }
  
  private Table e() {
    Table table1 = new Table();
    if (b.m != null) {
      NinePatchDrawable ninePatchDrawable1 = new NinePatchDrawable((NinePatch)b.m);
      table1.setBackground((Drawable)ninePatchDrawable1);
      table1.pad(b.m.getTopHeight(), b.m.getLeftWidth(), b.m.getBottomHeight(), b.m.getRightWidth());
    } 
    table1.top().left();
    table1.defaults().pad(0.0F).space(0.0F).growX();
    Table table2;
    (table2 = new Table()).top().left();
    table2.defaults().pad(0.0F).space(0.0F).growX();
    Table table3 = new Table();
    NinePatchDrawable ninePatchDrawable = new NinePatchDrawable((NinePatch)b.h);
    table3.setBackground((Drawable)ninePatchDrawable);
    table3.pad(b.h.getTopHeight(), b.h.getLeftWidth(), b.h.getBottomHeight(), b.h.getRightWidth());
    Image image;
    (image = new Image((Texture)b.a)).setScaling(Scaling.fill);
    image.setAlign(1);
    Container container;
    (container = new Container((Actor)image)).setClip(true);
    float f = cq.b();
    table3.add((Actor)container).growX().height(f).padBottom(5.0F).row();
    String str;
    if ((str = cj.a()) == null || str.trim().isEmpty())
      str = "Welcome To JTME"; 
    Label label = lj.a(str, Color.WHITE, true, 10);
    if (this.ac)
      label.setFontScale(1.5F); 
    table3.add((Actor)label).expand().fill().left().top();
    table2.add((Actor)table3).growX().pad(8.0F).row();
    ScrollPane scrollPane;
    (scrollPane = new ScrollPane((Actor)table2, a())).setFadeScrollBars(false);
    scrollPane.setScrollingDisabled(true, false);
    scrollPane.setForceScroll(false, true);
    scrollPane.setOverscroll(false, true);
    scrollPane.setFlickScroll(true);
    scrollPane.setSmoothScrolling(true);
    scrollPane.setTouchable(Touchable.enabled);
    table1.add((Actor)scrollPane).expand().fill().minWidth(0.0F).row();
    return table1;
  }
  
  private Table f() {
    Table table;
    (table = new Table()).top();
    table.defaults().growX().pad(0.0F).space(0.0F);
    this.z.clear();
    float f = this.ac ? 110.0F : this.bG;
    if (this.y.isEmpty()) {
      hy hy1 = this;
      Table table1;
      (table1 = new Table()).setBackground((Drawable)new NinePatchDrawable((NinePatch)b.h));
      table1.pad(10.0F);
      Label label = lj.a(b.a(hy1.q.f.S, "id_new_game"), Color.WHITE, true, 1);
      if (hy1.ac)
        label.setFontScale(1.3F); 
      table1.add((Actor)label).growX().center();
      table.add((Actor)table1).growX().height(f).row();
      return table;
    } 
    for (byte b = 0; b < this.y.size(); b++) {
      String str2;
      float f1 = f;
      byte b1 = b;
      ck ck = this.y.get(b);
      hy hy1 = this;
      boolean bool1 = (b1 == hy1.ci) ? true : false;
      Button.ButtonStyle buttonStyle;
      (buttonStyle = new Button.ButtonStyle()).up = (Drawable)new NinePatchDrawable((NinePatch)b.h);
      buttonStyle.down = buttonStyle.up;
      buttonStyle.checked = (Drawable)new NinePatchDrawable(b.j);
      Button button;
      (button = new Button(buttonStyle)).pad(8.0F);
      button.setChecked(bool1);
      f1 = Math.max(32.0F, f1 - button.getPadTop() - button.getPadBottom());
      boolean bool2 = false;
      if (ck.bx > 0 || ck.bB > 0 || ck.bz > 0) {
        bl bl;
        (bl = new bl(hy1.q.f)).b(ck.by, ck.bx, ck.bz, ck.bA, ck.bB, ck.bC, ck.bD, ck.bE, ck.bF, ck.bG, ck.bH);
        Texture texture;
        (texture = bl.b()).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
        hy1.x.add(texture);
        TextureRegion textureRegion = new TextureRegion(texture);
        bool2 = true;
      } else {
        String str = ck.P;
        str2 = ((str2 = ck.O) == null) ? "none" : str2.toLowerCase();
        str = (str == null) ? "none" : str.toLowerCase();
        str2 = str2.equals("warrior") ? (str.equals("female") ? (String)b.e : (String)b.d) : (str2.equals("wizard") ? (str.equals("female") ? (String)b.g : (String)b.f) : (str2.equals("archer") ? (String)new TextureRegion(b.H) : (String)new TextureRegion(b.H)));
      } 
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable((TextureRegion)str2))).setScaling(Scaling.none);
      float f3 = str2.getRegionWidth();
      float f2 = str2.getRegionHeight();
      image.setSize(f3, f2);
      Group group;
      (group = new Group()).setTransform(true);
      group.setSize(f1, f1);
      image.setPosition((f1 - f3) / 2.0F, (f1 - f2) / 2.0F);
      group.addActor((Actor)image);
      f2 = Math.min(f1 / f3, f1 / f2);
      f2 = bool2 ? (f2 * 1.3F) : f2;
      group.setOrigin(1);
      group.setScale(f2);
      Table table1;
      (table1 = new Table()).add((Actor)group).size(f1, f1).center();
      button.add((Actor)table1).size(f1, f1).padRight(10.0F).left();
      String str1 = b.a(hy1.q.f.S, "id_world_worldnr").replace("%u", Integer.toString(ck.bv));
      Label label1;
      (label1 = lj.a(ck.L, Color.WHITE, false, 8)).setEllipsis(true);
      Label label2;
      (label2 = lj.a(str1, new Color(1.0F, 1.0F, 1.0F, 0.85F), false, 8)).setEllipsis(true);
      if (hy1.ac) {
        label1.setFontScale(1.5F);
        label2.setFontScale(1.3F);
      } 
      Table table2;
      (table2 = new Table()).add((Actor)label1).left().growX().minWidth(0.0F).row();
      table2.add((Actor)label2).left().growX().minWidth(0.0F);
      button.add((Actor)table2).expandX().fillX().minWidth(0.0F).left();
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.z));
      imageButtonStyle.down = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.A));
      ImageButton imageButton;
      (imageButton = new ImageButton(imageButtonStyle)).addListener((EventListener)new id(hy1, b1));
      f1 = Math.min(f1, hy1.ac ? 90.0F : 40.0F);
      button.add((Actor)imageButton).size(f1, f1).right().padLeft(4.0F);
      button.addListener((EventListener)new ie(hy1, b1));
      hy1.z.add(button);
      table.add((Actor)button).growX().minWidth(0.0F).height(f).row();
    } 
    return table;
  }
  
  private void g(boolean paramBoolean) {
    Viewport viewport;
    float f2 = (viewport = this.l.getViewport()).getWorldWidth();
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
    if (this.r != null) {
      this.r.clearActions();
      this.r.setSize(f3, f4);
      f3 = Math.round((f2 - f3) * 0.5F);
      f1 = Math.round((f1 - f4) * 0.5F);
      if (paramBoolean && !this.ab) {
        this.r.setPosition(f2, f1);
        this.r.addAction((Action)Actions.moveTo(f3, f1, 0.3F));
        this.ab = true;
      } else {
        this.r.setPosition(f3, f1);
      } 
      this.r.invalidateHierarchy();
      this.r.validate();
    } 
    bX();
    if (this.s != null)
      this.s.setPosition(10.0F, 10.0F); 
  }
  
  final void bY() {
    if (this.r == null)
      return; 
    bW();
    this.a.remove();
    this.a = a();
    this.r.clearChildren();
    this.r.add((Actor)this.a).grow();
    bZ();
    g(false);
  }
  
  final void a(TextButton paramTextButton) {
    boolean bool = this.q.f.S;
    (new Thread(() -> {
          try {
            URLConnection uRLConnection;
            int i = (uRLConnection = (new URL(this.q.f.ab)).openConnection()).getContentLength();
            InputStream inputStream = uRLConnection.getInputStream();
            FileHandle fileHandle1 = Gdx.files.local("update_temp.zip");
            FileOutputStream fileOutputStream = new FileOutputStream(fileHandle1.file());
            byte[] arrayOfByte = new byte[4096];
            long l = 0L;
            int k = -1;
            String str1;
            if ((str1 = b.a(paramString, "id_update_downloading")) == null)
              str1 = "Downloading..."; 
            int j;
            while ((j = inputStream.read(arrayOfByte)) > 0) {
              fileOutputStream.write(arrayOfByte, 0, j);
              l += j;
              if (i > 0 && (j = (int)(l * 100L / i)) != k) {
                k = j;
                String str = str1 + " " + str1 + "%";
                Gdx.app.postRunnable(());
              } 
            } 
            fileOutputStream.close();
            inputStream.close();
            Gdx.app.postRunnable(());
            Gdx.files.local("update_extracted").mkdirs();
            ZipInputStream zipInputStream = new ZipInputStream(fileHandle1.read());
            try {
              for (ZipEntry zipEntry = zipInputStream.getNextEntry(); zipEntry != null; zipEntry = zipInputStream.getNextEntry()) {
                FileHandle fileHandle = Gdx.files.local("update_extracted/" + zipEntry.getName());
                if (zipEntry.isDirectory()) {
                  fileHandle.mkdirs();
                } else {
                  fileHandle.parent().mkdirs();
                  FileOutputStream fileOutputStream1 = new FileOutputStream(fileHandle.file());
                  try {
                    byte[] arrayOfByte1 = new byte[4096];
                    int m;
                    while ((m = zipInputStream.read(arrayOfByte1)) > 0)
                      fileOutputStream1.write(arrayOfByte1, 0, m); 
                    fileOutputStream1.close();
                  } catch (Throwable throwable) {
                    try {
                      fileOutputStream1.close();
                    } catch (Throwable throwable1) {
                      throwable.addSuppressed(throwable1);
                    } 
                    throw throwable;
                  } 
                } 
              } 
              zipInputStream.closeEntry();
              zipInputStream.close();
            } catch (Throwable throwable) {
              try {
                zipInputStream.close();
              } catch (Throwable throwable1) {
                throwable.addSuppressed(throwable1);
              } 
              throw throwable;
            } 
            Gdx.app.postRunnable(());
            FileHandle fileHandle2 = Gdx.files.local("update.bat");
            String str2 = "@echo off\ntimeout /t 3 /nobreak >nul\nxcopy /s /y \"update_extracted\\*\" \".\\\"\nrmdir /s /q \"update_extracted\"\ndel update_temp.zip\ndel run_update.vbs\nstart JTME.exe\ndel \"%~f0\"";
            fileHandle2.writeString(str2, false);
            Gdx.files.local("run_update.vbs").writeString("CreateObject(\"Wscript.Shell\").Run \"\"\"update.bat\"\"\", 0, False", false);
            Runtime.getRuntime().exec("wscript run_update.vbs");
            Gdx.app.exit();
            return;
          } catch (Exception exception) {
            Gdx.app.postRunnable(());
            return;
          } 
        })).start();
  }
  
  final void bZ() {
    boolean bool = (this.ci >= 0 && this.ci < this.y.size()) ? true : false;
    if (this.d != null) {
      this.d.setDisabled(!bool);
      (this.d.getColor()).a = bool ? 1.0F : 0.55F;
    } 
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClearColor(0.0F, 0.0F, 0.0F, 1.0F);
    Gdx.gl.glClear(16384);
    this.h.setProjectionMatrix((this.l.getCamera()).combined);
    this.h.begin();
    this.h.draw(this.bi, 0.0F, 0.0F, this.l.getViewport().getWorldWidth(), this.l.getViewport().getWorldHeight());
    this.h.end();
    this.l.act(paramFloat);
    this.l.draw();
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.l.getViewport().update(paramInt1, paramInt2, true);
    boolean bool = this.ac;
    al();
    if (bool != this.ac)
      bY(); 
    g(false);
  }
  
  public final void dispose() {
    bW();
    this.l.dispose();
    this.h.dispose();
    this.bi.dispose();
  }
}
