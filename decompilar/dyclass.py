package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
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
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.ui.Value;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;
import java.io.IOException;

public final class dy extends ScreenAdapter implements ik {
  final cr g;
  
  public final Stage f;
  
  private final SpriteBatch c;
  
  private Container a;
  
  private Actor a;
  
  private Table a;
  
  private boolean ab = false;
  
  private boolean ac = false;
  
  private final int cg;
  
  private final int ch;
  
  final br h;
  
  final bf d;
  
  public TextField a;
  
  TextField d;
  
  TextField e;
  
  TextField b;
  
  private Label a;
  
  private Table g;
  
  private float as = 40.0F;
  
  private float at = 3.0F;
  
  private boolean aj = false;
  
  public dy(cr paramcr, int paramInt1, int paramInt2, br parambr, bf parambf) {
    this.g = (Table)paramcr;
    this.cg = paramInt1;
    this.ch = paramInt2;
    this.h = parambr;
    this.d = (TextField)parambf;
    this.c = new SpriteBatch();
    this.f = new Stage((Viewport)new ScreenViewport());
    Gdx.input.setInputProcessor((InputProcessor)this.f);
    al();
    dy dy1;
    (dy1 = this).a = (Label)new Actor();
    dy1.a.setColor(0.0F, 0.0F, 0.0F, 0.55F);
    Viewport viewport = dy1.f.getViewport();
    dy1.a.setBounds(0.0F, 0.0F, viewport.getWorldWidth(), viewport.getWorldHeight());
    dy1.a.setTouchable(Touchable.enabled);
    dy1.a.addListener((EventListener)new ed(dy1));
    (dy1.a.getColor()).a = 0.0F;
    dy1.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.15F));
    dy1.f.addActor((Actor)dy1.a);
    dy1.a.toBack();
    this.a = (Label)a();
    this.a = (Label)new Container((Actor)this.a);
    this.a.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
    this.a.fill();
    a((Actor)this.a);
    this.f.addActor((Actor)this.a);
    g(true);
    al.a(1);
    this.f.addListener((EventListener)new dz(this, paramcr, parambr, parambf));
  }
  
  private boolean i() {
    return (this.f.getViewport().getWorldWidth() < 620.0F);
  }
  
  private void al() {
    float f1 = this.f.getViewport().getWorldWidth();
    float f2 = this.f.getViewport().getWorldHeight();
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
    boolean bool = ((cr)this.g).f.S;
    this.aj = i();
    this.as = this.aj ? 32.0F : 40.0F;
    this.at = this.aj ? 4.0F : 3.0F;
    Table table1;
    (table1 = new Table()).top().left();
    a((Actor)table1);
    Table table2 = new Table();
    if (b.f != null)
      table2.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table2.pad(0.0F);
    float f2;
    float f4 = (f2 = ((b.f != null) ? Math.max(b.f.getTotalHeight(), 32.0F) : 32.0F) * (this.aj ? 0.92F : 1.0F)) * 1.02F;
    float f5 = (b.c != null) ? (b.c.getWidth() / Math.max(1.0F, b.c.getHeight())) : 0.71875F;
    f5 = f4 * f5;
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
    imageButton.addListener((EventListener)new ee(this));
    Label label = lj.a(b.a(bool, "id_new_game"), Color.WHITE, false, 1);
    if (this.aj)
      label.setFontScale(0.92F); 
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table2.add((Actor)imageButton).size(f5, f4).left().padLeft(-4.0F);
    table2.add((Actor)label).expand().fill().center().minWidth(0.0F);
    table2.add(actor).size(f5, f4).right().padRight(-4.0F);
    table1.add((Actor)table2).growX().height(f2).row();
    (table2 = new Table()).top().left();
    table2.defaults().pad(this.aj ? 6.0F : 8.0F).space(0.0F).growX();
    Table table3;
    (table3 = new Table()).top().left();
    table3.defaults().pad(this.aj ? 4.0F : 6.0F).space(0.0F);
    Table table5;
    (table5 = a(bool, 1.0F, false)).pack();
    f5 = table5.getPrefHeight();
    table3.add((Actor)table5).expand().fill().left();
    float f3 = Math.max(26.0F, this.as + this.at * 2.0F);
    float f6 = (this.aj ? 4.0F : 6.0F) + (this.aj ? 4.0F : 6.0F) + (this.aj ? 4.0F : 6.0F);
    f5 = this.aj ? Math.max(44.0F, this.as * 1.2F) : Math.max(60.0F, f5 - f3 - f6);
    Table table4 = a(bool, f3, f5);
    f5 = this.aj ? 0.34F : 0.38F;
    table3.add((Actor)table4).width(Value.percentWidth(f5, (Actor)table3)).top().right();
    table2.add((Actor)table3).expand().fill().row();
    ScrollPane scrollPane;
    a(scrollPane = new ScrollPane((Actor)table2));
    table1.add((Actor)scrollPane).grow().row();
    float f1 = Math.max(b.h.getTotalHeight() * (this.aj ? 0.75F : 0.85F), this.aj ? 34.0F : 38.0F);
    String str;
    TextButton textButton = a(((str = b.a(bool, "id_start_game")) != null) ? str : "Start");
    if (this.aj)
      textButton.getLabel().setFontScale(0.95F); 
    textButton.addListener((EventListener)new ef(this));
    (table3 = new Table()).top().left();
    table3.defaults().pad(0.0F).space(0.0F).growX();
    table3.add().expandX().height(f1);
    table3.add((Actor)textButton).height(f1).width(this.aj ? 176.0F : 200.0F).right();
    table1.add((Actor)table3).growX().row();
    an();
    return table1;
  }
  
  private Table c() {
    boolean bool = ((cr)this.g).f.S;
    this.as = 90.0F;
    this.at = 10.0F;
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
    imageButton.addListener((EventListener)new eg(this));
    Label label2;
    (label2 = lj.a(b.a(bool, "id_new_game"), Color.WHITE, false, 1)).setFontScale(2.0F);
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    table3.add((Actor)imageButton).size(f3, f2).left().padLeft(15.0F);
    table3.add((Actor)label2).expand().fill().center().minWidth(0.0F);
    table3.add(actor).size(f3, f2).right().padRight(15.0F);
    table1.add((Actor)table3).growX().height(f1).row();
    (table3 = new Table()).top().left();
    table3.defaults().pad(10.0F).space(0.0F).growX();
    Table table5 = d();
    table3.add((Actor)table5).center().padBottom(5.0F).row();
    Label label1;
    (label1 = lj.a(b.a(bool, a(this.cg, this.ch)), Color.WHITE, true, 1)).setFontScale(1.4F);
    Table table6;
    (table6 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.v));
    table6.add((Actor)label1).growX().pad(15.0F);
    table3.add((Actor)table6).growX().padBottom(20.0F).row();
    Table table4 = a(bool, 1.5F, true);
    table3.add((Actor)table4).growX().row();
    ScrollPane scrollPane;
    a(scrollPane = new ScrollPane((Actor)table3));
    table1.add((Actor)scrollPane).grow().row();
    String str;
    TextButton textButton;
    (textButton = a(((str = b.a(bool, "id_start_game")) != null) ? str : "Start")).getLabel().setFontScale(1.5F);
    textButton.addListener((EventListener)new eh(this));
    Table table2;
    (table2 = new Table()).defaults().growX().height(110.0F);
    table2.add((Actor)textButton).pad(10.0F);
    table1.add((Actor)table2).growX().padBottom(10.0F).row();
    an();
    return table1;
  }
  
  private Table d() {
    TextureRegion textureRegion = b();
    Image image;
    (image = new Image((Drawable)new TextureRegionDrawable(textureRegion))).setScaling(Scaling.fit);
    Table table;
    (table = new Table()).setBackground((Drawable)new NinePatchDrawable(b.B));
    Container container;
    (container = new Container((Actor)image)).fill();
    container.prefSize(120.0F, 120.0F);
    table.add((Actor)container).size(120.0F, 120.0F).center();
    return table;
  }
  
  private TextureRegion b() {
    return (TextureRegion)((this.cg == 1) ? ((this.ch == 1) ? b.d : b.e) : ((this.cg == 2) ? ((this.ch == 1) ? b.f : b.g) : ((this.cg == 3) ? ((this.ch == 1) ? b.f : b.g) : new TextureRegion(b.H))));
  }
  
  private Table a(String paramString, float paramFloat1, float paramFloat2) {
    TextureRegion textureRegion = b();
    Image image;
    (image = new Image((Drawable)new TextureRegionDrawable(textureRegion))).setScaling(Scaling.fit);
    Table table2;
    (table2 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.B));
    table2.defaults().pad(0.0F).space(0.0F);
    Container container;
    (container = new Container((Actor)image)).fill();
    container.minSize(paramFloat1, paramFloat1).prefSize(paramFloat1, paramFloat1).maxSize(paramFloat1, paramFloat1);
    table2.add((Actor)container).size(paramFloat1, paramFloat1).center().row();
    paramString = b.a(paramString, a(this.cg, this.ch));
    this.a = lj.a(paramString, Color.WHITE, true, 1);
    this.a.setEllipsis(false);
    if (this.aj)
      this.a.setFontScale(0.95F); 
    this.g = new Table();
    this.g.setBackground((Drawable)new NinePatchDrawable(b.v));
    this.g.defaults().pad(this.aj ? 8.0F : 10.0F).space(0.0F).growX();
    this.g.add((Actor)this.a).growX().row();
    float f = paramFloat2;
    this.g.addAction((Action)Actions.run(() -> k(paramFloat)));
    Table table1;
    (table1 = new Table()).top().left();
    table1.defaults().pad(this.aj ? 4.0F : 6.0F).space(0.0F).growX();
    table1.add((Actor)table2).left().row();
    table1.add((Actor)this.g).growX().row();
    return table1;
  }
  
  private void k(float paramFloat) {
    if (this.a == null || this.g == null)
      return; 
    float f1 = Math.max(10.0F, this.g.getWidth() - (this.aj ? 16.0F : 20.0F));
    if (this.aj) {
      this.a.setWrap(false);
      this.a.setEllipsis(true);
      this.a.setFontScale(0.92F);
      this.a.setWidth(f1);
      this.a.invalidateHierarchy();
      this.a.layout();
      this.g.setHeight(paramFloat);
      return;
    } 
    this.a.setWrap(true);
    this.a.setEllipsis(false);
    float f2 = 1.0F;
    this.a.setFontScale(1.0F);
    this.a.setWidth(f1);
    this.a.invalidateHierarchy();
    this.a.layout();
    float f3;
    for (f3 = this.a.getPrefHeight(); f3 > paramFloat && f2 > 0.85F; f3 = this.a.getPrefHeight()) {
      f2 -= 0.05F;
      this.a.setFontScale(f2);
      this.a.setWidth(f1);
      this.a.invalidateHierarchy();
      this.a.layout();
    } 
    if (f3 > paramFloat) {
      this.a.setWrap(false);
      this.a.setEllipsis(true);
      this.a.setFontScale(Math.max(0.85F, f2));
      this.a.setWidth(f1);
      this.a.invalidateHierarchy();
      this.a.layout();
      this.g.setHeight(paramFloat);
      return;
    } 
    this.g.invalidateHierarchy();
  }
  
  private static String a(int paramInt1, int paramInt2) {
    switch (paramInt1) {
      case 1:
        return (paramInt2 == 1) ? "id_warrior_male" : "id_warrior_female";
      case 2:
        return (paramInt2 == 1) ? "id_wizard_male" : "id_wizard_female";
      case 3:
        return (paramInt2 == 1) ? "id_hunter_male" : "id_hunter_female";
    } 
    return "id_warrior_male";
  }
  
  private Table a(String paramString, float paramFloat, boolean paramBoolean) {
    String str1 = b.a(paramString, "id_name");
    String str2 = b.a(paramString, "id_password");
    String str3 = b.a(paramString, "id_repeat_password");
    String str4 = b.a(paramString, "id_world");
    BitmapFont bitmapFont;
    (bitmapFont = b.a(str1 + str1 + str2 + str3)).getData().setScale(paramFloat);
    float f = Math.max(2.0F, bitmapFont.getCapHeight() * paramFloat);
    Pixmap pixmap1;
    (pixmap1 = new Pixmap(2, (int)f, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap1.fill();
    Texture texture2 = new Texture(pixmap1);
    pixmap1.dispose();
    TextureRegionDrawable textureRegionDrawable1 = new TextureRegionDrawable(new TextureRegion(texture2));
    Pixmap pixmap2;
    (pixmap2 = new Pixmap(2, 2, Pixmap.Format.RGBA8888)).setColor(1.0F, 1.0F, 1.0F, 0.28F);
    pixmap2.fill();
    Texture texture1 = new Texture(pixmap2);
    pixmap2.dispose();
    TextureRegionDrawable textureRegionDrawable2 = new TextureRegionDrawable(new TextureRegion(texture1));
    TextField.TextFieldStyle textFieldStyle1;
    (textFieldStyle1 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null)).messageFontColor = new Color(1.0F, 1.0F, 1.0F, 0.5F);
    TextField.TextFieldStyle textFieldStyle2;
    (textFieldStyle2 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null)).messageFontColor = textFieldStyle1.messageFontColor;
    f = paramBoolean ? 15.0F : 5.0F;
    this.a = (Label)new TextField("", textFieldStyle1);
    this.a.setMessageText(str1);
    this.a.setBlinkTime(0.5F);
    String str5;
    if ((str5 = ((cr)this.g).f.d()) != null && !str5.isEmpty())
      this.a.setText(str5); 
    this.a.setTextFieldFilter((paramTextField, paramChar) -> (Character.isLetter(paramChar) && paramTextField.getText().length() < 10));
    Table table3;
    (table3 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table3.add((Actor)this.a).growX().pad(f);
    a(table3, (TextField)this.a);
    this.a.addListener((EventListener)new ei(this, textFieldStyle2, textFieldStyle1, table3));
    this.d = new TextField("", textFieldStyle1);
    this.d.setPasswordMode(true);
    this.d.setPasswordCharacter('*');
    this.d.setMessageText(str2);
    this.d.setBlinkTime(0.5F);
    this.d.setTextFieldFilter((paramTextField, paramChar) -> (paramTextField.getText().length() < 10));
    Table table2;
    (table2 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table2.add((Actor)this.d).growX().pad(f);
    a(table2, this.d);
    this.d.addListener((EventListener)new ej(this, textFieldStyle2, textFieldStyle1, table2));
    this.e = new TextField("", textFieldStyle1);
    this.e.setPasswordMode(true);
    this.e.setPasswordCharacter('*');
    this.e.setMessageText(str3);
    this.e.setBlinkTime(0.5F);
    this.e.setTextFieldFilter((paramTextField, paramChar) -> (paramTextField.getText().length() < 10));
    Table table4;
    (table4 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table4.add((Actor)this.e).growX().pad(f);
    a(table4, this.e);
    this.e.addListener((EventListener)new ek(this, textFieldStyle2, textFieldStyle1, table4));
    this.b = new TextField("", textFieldStyle1);
    this.b.setMessageText(str4);
    this.b.setBlinkTime(0.5F);
    this.b.setText("200");
    this.b.setTextFieldFilter((paramTextField, paramChar) -> (Character.isDigit(paramChar) && paramTextField.getText().length() < 3));
    Table table5;
    (table5 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
    table5.add((Actor)this.b).growX().pad(f);
    a(table5, this.b);
    this.b.addListener((EventListener)new el(this, textFieldStyle2, textFieldStyle1, table5));
    Table table1;
    (table1 = new Table()).top().left();
    table1.defaults().growX().height(this.as).pad(this.at);
    table1.add((Actor)table3).row();
    table1.add((Actor)table2).row();
    table1.add((Actor)table4).row();
    table1.add((Actor)table5).row();
    return table1;
  }
  
  private void a(Table paramTable, TextField paramTextField) {
    paramTable.setTouchable(Touchable.enabled);
    paramTable.setName("INPUT_WRAPPER");
    paramTable.addListener((EventListener)new ea(this, paramTextField));
  }
  
  private void a(Actor paramActor) {
    paramActor.setTouchable(Touchable.enabled);
    paramActor.addListener((EventListener)new eb(this));
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
  
  final void aA() {
    int j;
    al.a(3);
    boolean bool = ((cr)this.g).f.S;
    String str2 = this.a.getText().trim();
    String str3 = this.d.getText();
    String str4 = this.e.getText().trim();
    if (str2.isEmpty()) {
      kx.a(this.f, b.a(bool, "id_name_empty"));
      return;
    } 
    if (str2.length() < 3) {
      kx.a(this.f, b.a(bool, "id_name_not_available"));
      return;
    } 
    if (str3.length() <= 5) {
      kx.a(this.f, "Password must be at least 6 characters long.");
      return;
    } 
    if (!str3.equals(str4)) {
      kx.a(this.f, b.a(bool, "id_password_not_equal"));
      return;
    } 
    try {
      j = Integer.parseInt(this.b.getText().trim());
    } catch (Exception exception) {
      kx.a(this.f, b.a(bool, "id_invalid_world"));
      return;
    } 
    String str1 = lj.e(str4);
    str2 = lj.d(str2);
    cq cq;
    (cq = ((cr)this.g).f).Y = str2;
    cq.Z = str1;
    int i = j;
    if (i != cq.cb)
      try {
        this.d.s(i);
        return;
      } catch (IOException iOException) {
        null.printStackTrace();
        return;
      }  
    this.h.b(cq.W, cq.bN);
  }
  
  private void an() {
    ec ec = new ec(this);
    TextField.TextFieldListener textFieldListener = (paramTextField, paramChar) -> {
        if (paramChar == '\r' || paramChar == '\n') {
          this.f.setKeyboardFocus(null);
          Gdx.input.setOnscreenKeyboardVisible(false);
          aA();
        } 
      };
    if (this.a != null) {
      this.a.addListener((EventListener)ec);
      this.a.setTextFieldListener(textFieldListener);
    } 
    if (this.d != null) {
      this.d.addListener((EventListener)ec);
      this.d.setTextFieldListener(textFieldListener);
    } 
    if (this.e != null) {
      this.e.addListener((EventListener)ec);
      this.e.setTextFieldListener(textFieldListener);
    } 
    if (this.b != null) {
      this.b.addListener((EventListener)ec);
      this.b.setTextFieldListener(textFieldListener);
    } 
  }
  
  private void g(boolean paramBoolean) {
    Viewport viewport;
    float f2 = (viewport = this.f.getViewport()).getWorldWidth();
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
  
  final void b(Runnable paramRunnable) {
    if (this.a == null) {
      if (paramRunnable != null)
        paramRunnable.run(); 
      return;
    } 
    if (this.a != null)
      this.a.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.0F), 0.2F)); 
    float f1 = this.f.getViewport().getWorldWidth();
    float f2 = this.a.getY();
    al.a(2);
    this.a.addAction((Action)Actions.sequence((Action)Actions.moveTo(f1, f2, 0.3F, Interpolation.smooth), (Action)Actions.run(paramRunnable)));
  }
  
  public final void show() {
    super.show();
    Gdx.input.setInputProcessor((InputProcessor)this.f);
  }
  
  public final void render(float paramFloat) {
    Gdx.gl.glClear(16384);
    this.c.setProjectionMatrix((this.f.getCamera()).combined);
    this.c.begin();
    this.c.draw((Texture)b.b, 0.0F, 0.0F, this.f.getViewport().getWorldWidth(), this.f.getViewport().getWorldHeight());
    this.c.end();
    this.f.act(paramFloat);
    this.f.draw();
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    this.f.getViewport().update(paramInt1, paramInt2, true);
    boolean bool = this.ac;
    al();
    dy dy1;
    if (bool != this.ac && (dy1 = this).a != null) {
      dy1.a.setActor(null);
      dy1.a = (Label)dy1.a();
      dy1.a.setActor((Actor)dy1.a);
      dy1.a((Actor)dy1.a);
      dy1.g(false);
    } 
    g(false);
    if (!this.ac) {
      this.aj = i();
      if (this.g != null)
        this.g.addAction((Action)Actions.run(() -> k(this.aj ? Math.max(44.0F, this.as * 1.2F) : this.g.getHeight()))); 
    } 
  }
  
  public final void dispose() {
    this.f.dispose();
    this.c.dispose();
  }
  
  public final Stage a() {
    return this.f;
  }
}
