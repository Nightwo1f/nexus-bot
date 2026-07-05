package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
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
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Iterator;

public final class eu extends ScreenAdapter {
  final cr k;
  
  final Stage h;
  
  private final SpriteBatch e;
  
  private final br k;
  
  final bf g;
  
  private Container a;
  
  private Actor a;
  
  private Table a;
  
  private boolean ab = false;
  
  private boolean ak = false;
  
  private boolean ac = false;
  
  private final String af;
  
  private final int cm;
  
  TextField g;
  
  private TextButton a;
  
  private boolean al = false;
  
  public eu(cr paramcr, String paramString, int paramInt, br parambr, bf parambf) {
    this.k = (br)paramcr;
    this.af = paramString;
    this.cm = paramInt;
    this.k = parambr;
    this.g = (TextField)parambf;
    this.h = new Stage((Viewport)new ScreenViewport());
    this.e = new SpriteBatch();
    Gdx.input.setInputProcessor((InputProcessor)this.h);
    al();
    eu eu1;
    (eu1 = this).a = (TextButton)new Actor();
    eu1.a.setColor(0.0F, 0.0F, 0.0F, 0.55F);
    Viewport viewport = eu1.h.getViewport();
    eu1.a.setBounds(0.0F, 0.0F, viewport.getWorldWidth(), viewport.getWorldHeight());
    eu1.a.setTouchable(Touchable.enabled);
    eu1.a.addListener((EventListener)new fa(eu1));
    (eu1.a.getColor()).a = 0.0F;
    eu1.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.15F));
    eu1.h.addActor((Actor)eu1.a);
    eu1.a.toBack();
    this.a = (TextButton)a();
    this.a = (TextButton)new Container((Actor)this.a);
    this.a.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
    this.a.fill();
    a((Actor)this.a);
    this.h.addActor((Actor)this.a);
    g(true);
    al.a(1);
    this.h.addListener((EventListener)new ev(this, parambf, paramcr));
    Gdx.app.postRunnable(() -> {
          if (this.g != null) {
            this.h.setKeyboardFocus((Actor)this.g);
            this.g.setCursorPosition(this.g.getText().length());
            Gdx.input.setOnscreenKeyboardVisible(true);
          } 
        });
  }
  
  private void al() {
    float f1 = this.h.getViewport().getWorldWidth();
    float f2 = this.h.getViewport().getWorldHeight();
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
    boolean bool = ((cr)this.k).f.S;
    Table table1;
    (table1 = new Table()).top().left();
    a((Actor)table1);
    Table table3 = new Table();
    if (b.f != null)
      table3.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table3.pad(0.0F);
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
    imageButton.addListener((EventListener)new fb(this));
    Label label2 = lj.a(b.a(bool, "id_password"), Color.WHITE, false, 1);
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table3.add((Actor)imageButton).size(f4, f3).left().padLeft(-4.0F);
    table3.add((Actor)label2).expand().fill().center().minWidth(0.0F);
    table3.add(actor).size(f4, f3).right().padRight(-4.0F);
    table1.add((Actor)table3).growX().height(f2).row();
    (table3 = new Table()).top().left();
    table3.defaults().pad(8.0F).space(0.0F).growX();
    Label label1 = lj.a(this.af + " " + this.af + " " + b.a(bool, "id_world"), Color.WHITE, false, 1);
    table3.add((Actor)label1).expandX().center().padBottom(6.0F).row();
    a(table3, bool, 1.0F, false);
    float f1 = Math.max(b.h.getTotalHeight() * 0.85F, 38.0F);
    aD();
    String str2 = this.al ? b.a(bool, "id_setting_always") : b.a(bool, "id_setting_never");
    this.a = a(str2);
    this.a.addListener((EventListener)new fc(this, bool));
    table3.add((Actor)this.a).height(f1).row();
    aE();
    ScrollPane scrollPane;
    a(scrollPane = new ScrollPane((Actor)table3));
    table1.add((Actor)scrollPane).grow().row();
    Table table2;
    (table2 = new Table()).top().left();
    table2.defaults().pad(0.0F).space(0.0F).growX();
    TextButton textButton;
    String str1;
    (textButton = a(((str1 = b.a(bool, "id_ok")) != null) ? str1 : "OK")).addListener((EventListener)new fd(this));
    table2.add().expandX().height(f1);
    table2.add((Actor)textButton).height(f1).width(160.0F).right();
    table1.add((Actor)table2).growX().row();
    return table1;
  }
  
  private Table c() {
    boolean bool = ((cr)this.k).f.S;
    Table table1;
    (table1 = new Table()).top().left();
    a((Actor)table1);
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
    imageButton.addListener((EventListener)new fe(this));
    Label label2;
    (label2 = lj.a(b.a(bool, "id_password"), Color.WHITE, false, 1)).setFontScale(2.0F);
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table3.add((Actor)imageButton).size(f3, f2).left().padLeft(15.0F);
    table3.add((Actor)label2).expand().fill().center().minWidth(0.0F);
    table3.add(actor).size(f3, f2).right().padRight(15.0F);
    table1.add((Actor)table3).growX().height(f1).row();
    (table3 = new Table()).top().left();
    table3.defaults().pad(10.0F).space(15.0F).growX();
    Label label1;
    (label1 = lj.a(this.af + " " + this.af + " " + b.a(bool, "id_world"), Color.WHITE, false, 1)).setFontScale(1.5F);
    table3.add((Actor)label1).expandX().center().padBottom(15.0F).row();
    a(table3, bool, 1.5F, true);
    aD();
    String str2 = this.al ? b.a(bool, "id_setting_always") : b.a(bool, "id_setting_never");
    this.a = a(str2);
    this.a.getLabel().setFontScale(1.5F);
    this.a.addListener((EventListener)new ff(this, bool));
    table3.add((Actor)this.a).height(110.0F).row();
    aE();
    ScrollPane scrollPane;
    a(scrollPane = new ScrollPane((Actor)table3));
    table1.add((Actor)scrollPane).grow().row();
    Table table2;
    (table2 = new Table()).defaults().growX().height(110.0F).padBottom(10.0F);
    TextButton textButton;
    String str1;
    (textButton = a(((str1 = b.a(bool, "id_ok")) != null) ? str1 : "OK")).getLabel().setFontScale(1.5F);
    textButton.addListener((EventListener)new fg(this));
    table2.add((Actor)textButton).row();
    table1.add((Actor)table2).growX().padBottom(10.0F).row();
    return table1;
  }
  
  private void a(Table paramTable, String paramString, float paramFloat, boolean paramBoolean) {
    BitmapFont bitmapFont;
    (bitmapFont = b.a(paramString = b.a(paramString, "id_enter_password"))).getData().setScale(paramFloat);
    paramFloat = Math.max(14.0F, bitmapFont.getCapHeight() * paramFloat);
    Pixmap pixmap1;
    (pixmap1 = new Pixmap(2, (int)paramFloat, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap1.fill();
    Texture texture1 = new Texture(pixmap1);
    pixmap1.dispose();
    TextureRegionDrawable textureRegionDrawable2 = new TextureRegionDrawable(new TextureRegion(texture1));
    Pixmap pixmap2;
    (pixmap2 = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(1.0F, 1.0F, 1.0F, 0.35F);
    pixmap2.fill();
    Texture texture2 = new Texture(pixmap2);
    pixmap2.dispose();
    TextureRegionDrawable textureRegionDrawable4 = new TextureRegionDrawable(new TextureRegion(texture2));
    TextField.TextFieldStyle textFieldStyle2;
    (textFieldStyle2 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable2, (Drawable)textureRegionDrawable4, null)).messageFontColor = new Color(1.0F, 1.0F, 1.0F, 0.5F);
    TextField.TextFieldStyle textFieldStyle1;
    (textFieldStyle1 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable2, (Drawable)textureRegionDrawable4, null)).messageFontColor = textFieldStyle2.messageFontColor;
    this.g = new TextField("", textFieldStyle2);
    this.g.setMessageText(paramString);
    this.g.setTextFieldFilter((paramTextField, paramChar) -> (paramTextField.getText().length() < 10));
    this.g.setBlinkTime(0.5F);
    this.g.setPasswordCharacter('*');
    this.g.setPasswordMode(true);
    TextureRegionDrawable textureRegionDrawable1 = new TextureRegionDrawable(new TextureRegion(b.aS));
    TextureRegionDrawable textureRegionDrawable3 = new TextureRegionDrawable(new TextureRegion(b.aT));
    textureRegionDrawable4 = new TextureRegionDrawable(new TextureRegion(b.aU));
    TextureRegionDrawable textureRegionDrawable5 = new TextureRegionDrawable(new TextureRegion(b.aV));
    ImageButton imageButton = new ImageButton((Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable3);
    float f3 = (b.g != null) ? (b.g.getTotalHeight() * 0.45F) : 32.0F;
    f3 = paramBoolean ? 60.0F : Math.max(28.0F, f3);
    if (paramBoolean)
      imageButton.getImageCell().expand().fill(); 
    imageButton.setSize(f3, f3);
    imageButton.addListener((EventListener)new fh(this, imageButton, textureRegionDrawable1, textureRegionDrawable4, textureRegionDrawable3, textureRegionDrawable5));
    Table table;
    (table = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table.defaults().pad(8.0F).center();
    float f2 = paramBoolean ? 15.0F : 0.0F;
    table.add((Actor)this.g).expandX().fillX().left().pad(f2);
    table.add((Actor)imageButton).size(f3, f3).right().padRight(f2);
    a(table, this.g);
    this.g.addListener((EventListener)new fi(this, textFieldStyle1, textFieldStyle2, table));
    this.g.addListener((EventListener)new ew(this));
    float f1 = paramBoolean ? 90.0F : 0.0F;
    if (paramBoolean) {
      paramTable.add((Actor)table).height(f1).row();
      return;
    } 
    paramTable.add((Actor)table).row();
  }
  
  private void a(Table paramTable, TextField paramTextField) {
    paramTable.setTouchable(Touchable.enabled);
    paramTable.setName("INPUT_WRAPPER");
    paramTable.addListener((EventListener)new ex(this, paramTextField));
  }
  
  private void a(Actor paramActor) {
    paramActor.setTouchable(Touchable.enabled);
    paramActor.addListener((EventListener)new ey(this));
  }
  
  private void aD() {
    Iterator<ck> iterator = ((cr)this.k).f.n.iterator();
    while (iterator.hasNext()) {
      ck ck;
      if ((ck = iterator.next()).L.equals(this.af) && ck.bv == this.cm) {
        this.al = "always".equalsIgnoreCase(ck.Q);
        if (this.al && ck.M != null && !ck.M.isEmpty()) {
          this.g.setText(lj.g(ck.M));
          return;
        } 
        break;
      } 
    } 
  }
  
  final void u(String paramString) {
    al.a(3);
    this.al = !this.al;
    paramString = this.al ? b.a(paramString, "id_setting_always") : b.a(paramString, "id_setting_never");
    lj.c(this.a, paramString);
    if (this.ac)
      this.a.getLabel().setFontScale(1.5F); 
  }
  
  private void aE() {
    this.g.addListener((EventListener)new ez(this));
    this.g.setTextFieldListener((paramTextField, paramChar) -> {
          if (paramChar == '\r' || paramChar == '\n') {
            this.h.setKeyboardFocus(null);
            Gdx.input.setOnscreenKeyboardVisible(false);
            aF();
          } 
        });
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
  
  final void aF() {
    if (this.ak)
      return; 
    al.a(3);
    boolean bool = ((cr)this.k).f.S;
    String str2;
    if ((str2 = this.g.getText().trim()).isEmpty()) {
      kx.a(this.h, b.a(bool, "id_password_empty"));
      return;
    } 
    this.ak = true;
    String str1 = lj.e(str2);
    str2 = lj.f(str2);
    for (byte b = 0; b < ((cr)this.k).f.n.size(); b++) {
      ck ck;
      if ((ck = ((cr)this.k).f.n.get(b)).L.equals(this.af) && ck.bv == this.cm) {
        ((cr)this.k).f.n.set(b, new ck(ck.K, ck.L, str2, ck.bv, ck.bw, ck.N, ck.O, ck.P, this.al ? "always" : "never"));
        break;
      } 
    } 
    cj.f(((cr)this.k).f);
    cq cq;
    (cq = ((cr)this.k).f).Y = this.af;
    cq.Z = str1;
    cq.ca = this.cm;
    hs hs = new hs((cr)this.k, (bf)this.g, this.af, this.cm);
    ((cr)this.k).a = (cs)hs;
    ((bf)this.g).a = (FileOutputStream)hs;
    this.k.setScreen((Screen)hs);
    (new Thread(() -> {
          try {
            this.g.a(paramcq.V, paramcq.bM);
            Gdx.app.postRunnable(());
            return;
          } catch (IOException iOException) {
            Gdx.app.postRunnable(());
            return;
          } 
        })).start();
  }
  
  private void g(boolean paramBoolean) {
    Viewport viewport;
    float f2 = (viewport = this.h.getViewport()).getWorldWidth();
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
  
  final void d(Runnable paramRunnable) {
    if (this.a == null) {
      if (paramRunnable != null)
        paramRunnable.run(); 
      return;
    } 
    if (this.a != null)
      this.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.0F), 0.2F)); 
    float f1 = this.h.getViewport().getWorldWidth();
    float f2 = this.a.getY();
    al.a(2);
    this.a.addAction((Action)Actions.sequence((Action)Actions.moveTo(f1, f2, 0.3F, Interpolation.smooth), (Action)Actions.run(paramRunnable)));
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClearColor(0.0F, 0.0F, 0.0F, 1.0F);
    Gdx.gl.glClear(16384);
    this.e.setProjectionMatrix((this.h.getCamera()).combined);
    this.e.begin();
    this.e.draw((Texture)b.b, 0.0F, 0.0F, this.h.getViewport().getWorldWidth(), this.h.getViewport().getWorldHeight());
    this.e.end();
    this.h.act(paramFloat);
    this.h.draw();
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.h.getViewport().update(paramInt1, paramInt2, true);
    boolean bool = this.ac;
    al();
    eu eu1;
    if (bool != this.ac && (eu1 = this).a != null) {
      eu1.a.setActor(null);
      eu1.a = (TextButton)eu1.a();
      eu1.a.setActor((Actor)eu1.a);
      eu1.a((Actor)eu1.a);
      eu1.g(false);
    } 
    g(false);
  }
  
  public final void dispose() {
    this.h.dispose();
    this.e.dispose();
  }
}
