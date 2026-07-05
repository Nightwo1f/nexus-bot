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
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;
import java.util.Iterator;

public final class cx extends ScreenAdapter implements ik {
  final cr e;
  
  final Stage c;
  
  private final SpriteBatch b;
  
  private final br f;
  
  private final bf c;
  
  private Container a;
  
  private Actor a;
  
  private Table a;
  
  private boolean ab = false;
  
  private boolean ac = false;
  
  TextField a;
  
  TextField b;
  
  public cx(cr paramcr, br parambr, bf parambf) {
    this.e = paramcr;
    this.b = (TextField)new SpriteBatch();
    this.f = parambr;
    this.c = parambf;
    this.c = (bf)new Stage((Viewport)new ScreenViewport());
    Gdx.input.setInputProcessor((InputProcessor)this.c);
    al();
    cx cx1;
    (cx1 = this).a = (TextField)new Actor();
    cx1.a.setColor(0.0F, 0.0F, 0.0F, 0.55F);
    Viewport viewport = cx1.c.getViewport();
    cx1.a.setBounds(0.0F, 0.0F, viewport.getWorldWidth(), viewport.getWorldHeight());
    cx1.a.setTouchable(Touchable.enabled);
    cx1.a.addListener((EventListener)new dc(cx1));
    (cx1.a.getColor()).a = 0.0F;
    cx1.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.15F));
    cx1.c.addActor((Actor)cx1.a);
    cx1.a.toBack();
    this.a = (TextField)a();
    this.a = (TextField)new Container((Actor)this.a);
    this.a.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
    this.a.fill();
    a((Actor)this.a);
    this.c.addActor((Actor)this.a);
    g(true);
    al.a(1);
    this.c.addListener((EventListener)new cy(this, paramcr));
  }
  
  private void al() {
    float f = this.c.getViewport().getWorldWidth();
    boolean bool = (this.c.getViewport().getWorldHeight() > f) ? true : false;
    this.ac = bool;
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
    boolean bool = this.e.f.S;
    Table table1;
    (table1 = new Table()).top().left();
    a((Actor)table1);
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
    imageButton.addListener((EventListener)new dd(this));
    Label label = lj.a(b.a(bool, "id_add_character_header"), Color.WHITE, false, 1);
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table2.add((Actor)imageButton).size(f4, f3).left().padLeft(-4.0F);
    table2.add((Actor)label).expand().fill().center().minWidth(0.0F);
    table2.add(actor).size(f4, f3).right().padRight(-4.0F);
    table1.add((Actor)table2).growX().height(f2).row();
    (table2 = new Table()).top().left();
    table2.defaults().pad(8.0F).space(0.0F).growX();
    String str2 = b.a(bool, "id_name");
    String str3 = b.a(bool, "id_world");
    BitmapFont bitmapFont;
    (bitmapFont = b.a(str2 + str2)).getData().setScale(1.0F);
    TextureRegionDrawable textureRegionDrawable1 = a(bitmapFont);
    TextureRegionDrawable textureRegionDrawable2 = a();
    TextField.TextFieldStyle textFieldStyle2;
    (textFieldStyle2 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null)).messageFontColor = new Color(1.0F, 1.0F, 1.0F, 0.5F);
    TextField.TextFieldStyle textFieldStyle1;
    (textFieldStyle1 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null)).messageFontColor = textFieldStyle2.messageFontColor;
    this.a = new TextField("", textFieldStyle2);
    this.a.setMessageText(str2);
    this.a.setTextFieldFilter((paramTextField, paramChar) -> (Character.isLetter(paramChar) && paramTextField.getText().length() < 10));
    this.a.setBlinkTime(0.5F);
    Table table3;
    (table3 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table3.add((Actor)this.a).expandX().fillX();
    a(table3, this.a);
    this.a.addListener((EventListener)new de(this, textFieldStyle1, textFieldStyle2, table3));
    this.b = new TextField("", textFieldStyle2);
    this.b.setMessageText(str3);
    this.b.setTextFieldFilter((paramTextField, paramChar) -> (Character.isDigit(paramChar) && paramTextField.getText().length() < 3));
    this.b.setBlinkTime(0.5F);
    Table table4;
    (table4 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table4.add((Actor)this.b).expandX().fillX();
    a(table4, this.b);
    this.b.addListener((EventListener)new df(this, textFieldStyle1, textFieldStyle2, table4));
    table2.add((Actor)table3).row();
    table2.add((Actor)table4).row();
    float f1 = Math.max(b.h.getTotalHeight() * 0.85F, 38.0F);
    TextButton textButton;
    String str1;
    (textButton = a(((str1 = b.a(bool, "id_save")) != null) ? str1 : "Save")).addListener((EventListener)new dg(this));
    (table4 = new Table()).top().left();
    table4.defaults().pad(0.0F).space(0.0F).growX();
    table4.add().expandX().height(f1);
    table4.add((Actor)textButton).height(f1).width(160.0F).right();
    table1.add((Actor)table2).grow().row();
    table1.add((Actor)table4).growX().row();
    an();
    return table1;
  }
  
  private Table c() {
    boolean bool = this.e.f.S;
    Table table1;
    (table1 = new Table()).top().left();
    a((Actor)table1);
    Table table2 = new Table();
    if (b.f != null)
      table2.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table2.pad(0.0F);
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
    imageButton.addListener((EventListener)new dh(this));
    Label label;
    (label = lj.a(b.a(bool, "id_add_character_header"), Color.WHITE, false, 1)).setFontScale(2.0F);
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table2.add((Actor)imageButton).size(f3, f2).left().padLeft(15.0F);
    table2.add((Actor)label).expand().fill().center().minWidth(0.0F);
    table2.add(actor).size(f3, f2).right().padRight(15.0F);
    table1.add((Actor)table2).growX().height(f1).row();
    (table2 = new Table()).top().left();
    table2.defaults().pad(10.0F).space(15.0F).growX();
    String str2 = b.a(bool, "id_name");
    String str3 = b.a(bool, "id_world");
    BitmapFont bitmapFont;
    (bitmapFont = b.a(str2 + str2)).getData().setScale(1.5F);
    TextureRegionDrawable textureRegionDrawable1 = a(bitmapFont);
    TextureRegionDrawable textureRegionDrawable2 = a();
    TextField.TextFieldStyle textFieldStyle2;
    (textFieldStyle2 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null)).messageFontColor = new Color(1.0F, 1.0F, 1.0F, 0.5F);
    TextField.TextFieldStyle textFieldStyle1;
    (textFieldStyle1 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null)).messageFontColor = textFieldStyle2.messageFontColor;
    this.a = new TextField("", textFieldStyle2);
    this.a.setMessageText(str2);
    this.a.setTextFieldFilter((paramTextField, paramChar) -> (Character.isLetter(paramChar) && paramTextField.getText().length() < 10));
    this.a.setBlinkTime(0.5F);
    Table table3;
    (table3 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table3.add((Actor)this.a).expandX().fillX().pad(15.0F);
    a(table3, this.a);
    this.a.addListener((EventListener)new di(this, textFieldStyle1, textFieldStyle2, table3));
    this.b = new TextField("", textFieldStyle2);
    this.b.setMessageText(str3);
    this.b.setTextFieldFilter((paramTextField, paramChar) -> (Character.isDigit(paramChar) && paramTextField.getText().length() < 3));
    this.b.setBlinkTime(0.5F);
    Table table4;
    (table4 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table4.add((Actor)this.b).expandX().fillX().pad(15.0F);
    a(table4, this.b);
    this.b.addListener((EventListener)new dj(this, textFieldStyle1, textFieldStyle2, table4));
    table2.add((Actor)table3).height(90.0F).row();
    table2.add((Actor)table4).height(90.0F).row();
    table1.add((Actor)table2).grow().row();
    String str1;
    TextButton textButton;
    (textButton = a(((str1 = b.a(bool, "id_save")) != null) ? str1 : "Save")).getLabel().setFontScale(1.5F);
    textButton.addListener((EventListener)new dk(this));
    (table2 = new Table()).defaults().growX().height(110.0F);
    table2.add((Actor)textButton).pad(10.0F);
    table1.add((Actor)table2).growX().padBottom(10.0F).row();
    an();
    return table1;
  }
  
  private void a(Table paramTable, TextField paramTextField) {
    paramTable.setTouchable(Touchable.enabled);
    paramTable.setName("INPUT_WRAPPER");
    paramTable.addListener((EventListener)new cz(this, paramTextField));
  }
  
  private void a(Actor paramActor) {
    paramActor.setTouchable(Touchable.enabled);
    paramActor.addListener((EventListener)new da(this));
  }
  
  final void am() {
    int i;
    boolean bool = this.e.f.S;
    String str1;
    if ((str1 = this.a.getText().trim()).isEmpty()) {
      kx.a((Stage)this.c, b.a(bool, "id_name_empty"));
      return;
    } 
    try {
      i = Integer.parseInt(this.b.getText().trim());
    } catch (NumberFormatException numberFormatException) {
      kx.a((Stage)this.c, b.a(bool, "id_invalid_world"));
      return;
    } 
    Iterator<ck> iterator = this.e.f.n.iterator();
    while (iterator.hasNext()) {
      ck ck1;
      if ((ck1 = iterator.next()).L.equalsIgnoreCase(str1) && ck1.bv == i) {
        kx.a((Stage)this.c, b.a(bool, "id_character_already_exist"));
        return;
      } 
    } 
    String str2 = lj.d(str1);
    ck ck = new ck("1.6", str2, "", i, 1, "0", "none", "none", "never");
    this.e.f.a(ck);
    cj.f(this.e.f);
    al.a(3);
    this.e.setScreen((Screen)new eu(this.e, str2, i, this.f, this.c));
  }
  
  private void an() {
    db db = new db(this);
    TextField.TextFieldListener textFieldListener = (paramTextField, paramChar) -> {
        if (paramChar == '\r' || paramChar == '\n') {
          this.c.setKeyboardFocus(null);
          Gdx.input.setOnscreenKeyboardVisible(false);
          am();
        } 
      };
    if (this.a != null) {
      this.a.addListener((EventListener)db);
      this.a.setTextFieldListener(textFieldListener);
    } 
    if (this.b != null) {
      this.b.addListener((EventListener)db);
      this.b.setTextFieldListener(textFieldListener);
    } 
  }
  
  private static TextureRegionDrawable a(BitmapFont paramBitmapFont) {
    float f;
    if ((f = paramBitmapFont.getCapHeight() * paramBitmapFont.getScaleY()) < 10.0F)
      f = 14.0F; 
    Pixmap pixmap;
    (pixmap = new Pixmap(2, (int)f, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap.fill();
    Texture texture = new Texture(pixmap);
    pixmap.dispose();
    return new TextureRegionDrawable(new TextureRegion(texture));
  }
  
  private static TextureRegionDrawable a() {
    Pixmap pixmap;
    (pixmap = new Pixmap(2, 2, Pixmap.Format.RGBA8888)).setColor(0.25F, 0.55F, 1.0F, 0.45F);
    pixmap.fill();
    Texture texture = new Texture(pixmap);
    pixmap.dispose();
    return new TextureRegionDrawable(new TextureRegion(texture));
  }
  
  private void g(boolean paramBoolean) {
    Viewport viewport;
    float f2 = (viewport = this.c.getViewport()).getWorldWidth();
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
  
  final void a(Runnable paramRunnable) {
    if (this.a == null) {
      if (paramRunnable != null)
        paramRunnable.run(); 
      return;
    } 
    if (this.a != null)
      this.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.0F), 0.2F)); 
    float f1 = this.c.getViewport().getWorldWidth();
    float f2 = this.a.getY();
    al.a(2);
    this.a.addAction((Action)Actions.sequence((Action)Actions.moveTo(f1, f2, 0.3F, Interpolation.smooth), (Action)Actions.run(paramRunnable)));
  }
  
  public final void show() {
    super.show();
    Gdx.input.setInputProcessor((InputProcessor)this.c);
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClear(16384);
    this.b.setProjectionMatrix((this.c.getCamera()).combined);
    this.b.begin();
    this.b.draw((Texture)b.b, 0.0F, 0.0F, this.c.getViewport().getWorldWidth(), this.c.getViewport().getWorldHeight());
    this.b.end();
    this.c.act(paramFloat);
    this.c.draw();
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.c.getViewport().update(paramInt1, paramInt2, true);
    boolean bool = this.ac;
    al();
    cx cx1;
    if (bool != this.ac && (cx1 = this).a != null) {
      cx1.a.setActor(null);
      cx1.a = (TextField)cx1.a();
      cx1.a.setActor((Actor)cx1.a);
      cx1.a((Actor)cx1.a);
      cx1.g(false);
    } 
    g(false);
  }
  
  public final void dispose() {
    this.c.dispose();
    this.b.dispose();
  }
  
  public final Stage a() {
    return (Stage)this.c;
  }
}
