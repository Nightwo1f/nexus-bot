package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Interpolation;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Button;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Stack;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import java.io.IOException;

public final class kg {
  final br o;
  
  public float cd = 0.0F;
  
  public float ce = 0.0F;
  
  public boolean aL = false;
  
  public float br = 1.0F;
  
  public float cf = 1.0F;
  
  public static kg b;
  
  private boolean bE = false;
  
  public Group l;
  
  public Table F;
  
  public Actor f;
  
  public kg(br parambr) {
    this.o = parambr;
  }
  
  public final void cp() {
    cr();
  }
  
  final void cq() {
    if (this.bE)
      return; 
    this.bE = true;
    try {
      this.o.G = true;
      this.o.L();
      return;
    } catch (Exception exception) {
      Gdx.app.error("OutfitShop0", "Falha ao enviar RequestLeaveShop", exception);
      return;
    } finally {
      cr();
    } 
  }
  
  public final void cr() {
    if (this.l == null)
      return; 
    if (b == this)
      b = null; 
    try {
      if (this.F != null) {
        this.F.addAction((Action)Actions.sequence((Action)Actions.moveTo(-this.F.getWidth(), this.F.getY(), 0.2F, Interpolation.smooth), (Action)Actions.run(() -> {
                  if (this.l != null)
                    this.l.remove(); 
                  this.l = null;
                  this.F = null;
                  this.f = null;
                })));
        return;
      } 
      this.l.remove();
      this.l = null;
      this.F = null;
      this.f = null;
      return;
    } catch (Throwable throwable) {
      return;
    } 
  }
  
  public final Table a(String paramString, kr paramkr) {
    paramkr.aL = paramString;
    float f1 = lj.a(paramkr.n) * this.cf;
    float f2 = this.aL ? 8.0F : 10.0F;
    float f3 = this.aL ? cq.b() : paramkr.n.ae;
    float f4 = (this.cd > 0.0F) ? this.cd : ((this.l != null) ? this.l.getWidth() : Gdx.graphics.getWidth());
    float f5 = (this.ce > 0.0F) ? this.ce : ((this.l != null) ? this.l.getHeight() : Gdx.graphics.getHeight());
    if (this.aL) {
      f4 *= 0.95F;
      f5 *= 0.9F;
    } else {
      f4 = Math.min(560.0F, f4 * 0.95F);
      f5 = Math.min(510.0F, f5 * 0.95F);
    } 
    f4 = Math.round(f4);
    f5 = Math.round(f5);
    paramkr.ci = f4;
    Table table3;
    (table3 = new Table()).top();
    if (b.d != null) {
      table3.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
    } else {
      Pixmap pixmap;
      (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.DARK_GRAY);
      pixmap.fill();
      table3.setBackground((Drawable)new TextureRegionDrawable(new TextureRegion(new Texture(pixmap))));
    } 
    float f6 = this.aL ? Math.max(f2, f5 * 0.12F) : f2;
    table3.pad(f2, f2, f6, f2);
    table3.setSize(f4, f5);
    Table table2 = new Table();
    if (b.f != null)
      table2.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table2.pad(0.0F);
    f4 = this.aL ? (f3 * 0.8F) : (f3 * 1.02F);
    f5 = 0.71875F;
    if (b.f != null)
      f5 = b.f.getWidth() / Math.max(1.0F, b.f.getHeight()); 
    f5 = f4 * f5;
    f6 = this.aL ? 15.0F : -4.0F;
    TextureRegion textureRegion1 = a((Texture)b.c);
    TextureRegion textureRegion2 = a((Texture)b.d);
    ImageButton.ImageButtonStyle imageButtonStyle1;
    (imageButtonStyle1 = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)new TextureRegionDrawable(textureRegion1);
    imageButtonStyle1.imageDown = (Drawable)new TextureRegionDrawable(textureRegion2);
    paramkr.A = new ImageButton(imageButtonStyle1);
    paramkr.A.getImage().setScaling(Scaling.fit);
    paramkr.A.getImageCell().pad(0.0F).expand().fill();
    paramkr.A.setVisible(false);
    paramkr.A.addListener((EventListener)new kk(this, paramkr));
    Actor actor;
    (actor = new Actor()).setTouchable(Touchable.disabled);
    Stack stack2;
    (stack2 = new Stack()).add(actor);
    stack2.add((Actor)paramkr.A);
    paramkr.v = new Label((paramString != null) ? paramString : "", new Label.LabelStyle(b.a(paramString), Color.WHITE));
    paramkr.v.setAlignment(1);
    if (this.aL)
      paramkr.v.setFontScale(this.br * 1.1F); 
    kg kg2 = this;
    Drawable drawable1 = c();
    TextureRegion textureRegion3;
    if ((textureRegion3 = (b.f != null) ? new TextureRegion((Texture)b.f) : new TextureRegion(c())).getTexture() != null)
      textureRegion3.getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear); 
    TextureRegionDrawable textureRegionDrawable3 = new TextureRegionDrawable(textureRegion3);
    if ((textureRegion3 = (b.g != null) ? new TextureRegion((Texture)b.g) : textureRegion3).getTexture() != null)
      textureRegion3.getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear); 
    TextureRegionDrawable textureRegionDrawable2 = new TextureRegionDrawable(textureRegion3);
    ImageButton.ImageButtonStyle imageButtonStyle3;
    (imageButtonStyle3 = new ImageButton.ImageButtonStyle()).up = drawable1;
    imageButtonStyle3.down = drawable1;
    imageButtonStyle3.imageUp = (Drawable)textureRegionDrawable3;
    imageButtonStyle3.imageDown = (Drawable)textureRegionDrawable2;
    ImageButton imageButton3;
    (imageButton3 = new ImageButton(imageButtonStyle3)).getImage().setScaling(Scaling.fit);
    imageButton3.getImageCell().pad(0.0F).expand().fill();
    imageButton3.addListener((EventListener)new ko(kg2));
    ImageButton imageButton1 = imageButton3;
    table2.add((Actor)stack2).size(f5, f4).left().padLeft(f6);
    table2.add((Actor)paramkr.v).expand().fill().center().minWidth(0.0F);
    table2.add((Actor)imageButton1).size(f5, f4).right().padRight(f6);
    Table table1 = new Table();
    if (b.a != null)
      table1.setBackground((Drawable)b.a); 
    f4 = this.aL ? 24.0F : 8.0F;
    f5 = this.aL ? 8.0F : 6.0F;
    table1.pad(f5, f4, f5, f4);
    kr kr1;
    (kr1 = paramkr).F = new Image();
    kr1.F.setScaling(Scaling.fit);
    kr1.F.setAlign(1);
    Image image = kr1.F;
    Runnable runnable = () -> {
        try {
          this.o.L();
        } catch (IOException iOException) {
          null.printStackTrace();
        } 
        this.o.n(0, 111);
      };
    float f7 = f1;
    kg kg1 = this;
    ImageButton.ImageButtonStyle imageButtonStyle2 = new ImageButton.ImageButtonStyle();
    Drawable drawable2 = c();
    imageButtonStyle2.up = drawable2;
    imageButtonStyle2.down = drawable2;
    TextureRegion textureRegion4;
    if ((textureRegion4 = (b.ap != null) ? new TextureRegion(b.ap) : new TextureRegion(c())).getTexture() != null)
      textureRegion4.getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear); 
    TextureRegionDrawable textureRegionDrawable1 = new TextureRegionDrawable(textureRegion4);
    if ((textureRegion4 = (b.ao != null) ? new TextureRegion(b.ao) : textureRegion4).getTexture() != null)
      textureRegion4.getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear); 
    TextureRegionDrawable textureRegionDrawable4 = new TextureRegionDrawable(textureRegion4);
    imageButtonStyle2.imageUp = (Drawable)textureRegionDrawable1;
    imageButtonStyle2.imageDown = (Drawable)textureRegionDrawable4;
    ImageButton imageButton4;
    (imageButton4 = new ImageButton(imageButtonStyle2)).getImage().setScaling(Scaling.fit);
    float f9 = kg1.aL ? 1.0F : 0.92F;
    imageButton4.getImageCell().size(f7 * f9, f7 * f9).center();
    imageButton4.setSize(f7, f7);
    imageButton4.addListener((EventListener)new km(kg1, runnable));
    ImageButton imageButton2 = imageButton4;
    Table table6;
    (table6 = new Table()).add((Actor)image).size(f1, f1).padRight(15.0F);
    table6.add((Actor)imageButton2).size(f1, f1);
    table1.add((Actor)table6).left().expandX();
    Stack stack1 = new Stack();
    paramkr.K = (new Table()).top();
    paramkr.K.defaults().growX().space(this.aL ? 2.0F : 0.0F);
    paramkr.K.add((Actor)a(paramkr, a(paramkr, "id_hair", "Hair"), 0, b.aH)).row();
    paramkr.K.add((Actor)a(paramkr, a(paramkr, "id_head", "Head"), 1, b.aG)).row();
    paramkr.K.add((Actor)a(paramkr, a(paramkr, "id_body", "Body"), 2, b.aE)).row();
    paramkr.K.add((Actor)a(paramkr, a(paramkr, "id_extras", "Misc"), 3, b.aF)).row();
    ScrollPane scrollPane1;
    (scrollPane1 = new ScrollPane((Actor)paramkr.K)).setScrollingDisabled(true, false);
    scrollPane1.setFadeScrollBars(false);
    scrollPane1.setForceScroll(false, true);
    paramkr.J = (new Table()).top().left();
    ScrollPane scrollPane2;
    (scrollPane2 = new ScrollPane((Actor)paramkr.J)).setScrollingDisabled(true, false);
    scrollPane2.setFadeScrollBars(false);
    scrollPane2.setForceScroll(false, true);
    scrollPane2.setOverscroll(false, true);
    paramkr.L = (new Table()).top().left();
    paramkr.L.add((Actor)scrollPane2).expand().fill();
    paramkr.L.setVisible(false);
    stack1.add((Actor)scrollPane1);
    stack1.add((Actor)paramkr.L);
    Table table4;
    (table4 = new Table()).bottom();
    Table table5 = new Table();
    if (b.b != null) {
      table5.setBackground((Drawable)b.b);
    } else if (b.a != null) {
      table5.setBackground((Drawable)b.a);
    } 
    Button.ButtonStyle buttonStyle;
    (buttonStyle = new Button.ButtonStyle()).up = (Drawable)new NinePatchDrawable((NinePatch)b.h);
    if (b.i != null) {
      buttonStyle.down = (Drawable)new NinePatchDrawable((NinePatch)b.i);
    } else {
      buttonStyle.down = buttonStyle.up;
    } 
    Button button = new Button(buttonStyle);
    f7 = this.aL ? 0.0F : 4.0F;
    button.pad(0.0F, f7, 0.0F, f7);
    f7 = this.aL ? f1 : paramkr.n.ae;
    Label label;
    (label = lj.a(a(paramkr, "id_save", "Salvar"), Color.WHITE, false, 1)).setFontScale(this.br);
    button.add((Actor)label).expandX().fillX().center().minHeight(f7);
    button.addListener((EventListener)new kl(this, paramkr));
    float f8 = this.aL ? cq.c() : paramkr.n.ae;
    table4.add((Actor)table5).growX().height(f8).row();
    table4.add((Actor)button).growX().height(f7).row();
    table3.add((Actor)table2).growX().height(f3).row();
    f1 += f5 * 2.0F;
    table3.add((Actor)table1).growX().height(f1).row();
    table3.add((Actor)stack1).grow().row();
    table3.add((Actor)table4).growX().bottom().row();
    b(paramkr);
    return table3;
  }
  
  static void a(kr paramkr) {
    paramkr.v.setText(paramkr.aL);
    paramkr.A.setVisible(false);
    paramkr.K.setVisible(true);
    paramkr.L.setVisible(false);
  }
  
  final void a(kr paramkr, int paramInt, String paramString) {
    paramkr.eC = paramInt;
    paramkr.v.setText(paramString);
    paramkr.A.setVisible(true);
    paramkr.K.setVisible(false);
    paramkr.L.setVisible(true);
    a(paramkr, paramInt);
  }
  
  private Table a(kr paramkr, String paramString, int paramInt, Texture paramTexture) {
    Button.ButtonStyle buttonStyle;
    (buttonStyle = new Button.ButtonStyle()).up = (Drawable)new NinePatchDrawable((NinePatch)b.h);
    if (b.i != null) {
      buttonStyle.down = (Drawable)new NinePatchDrawable((NinePatch)b.i);
    } else {
      buttonStyle.down = buttonStyle.up;
    } 
    Button button = new Button(buttonStyle);
    float f1 = this.aL ? 0.0F : 8.0F;
    button.pad(0.0F, f1, 0.0F, f1);
    float f2 = f1 = lj.a(paramkr.n) * this.cf;
    if (paramTexture != null) {
      paramTexture.setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
      Button button1 = new Button(b());
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(paramTexture)))).setScaling(Scaling.fit);
      float f5 = this.aL ? 8.0F : 2.0F;
      button1.add((Actor)image).expand().fill().pad(f5).center();
      button1.setTouchable(Touchable.disabled);
      float f4 = this.aL ? 24.0F : 0.0F;
      button.add((Actor)button1).size(f1, f1).padRight(10.0F).padLeft(f4).left();
    } 
    Label label;
    (label = lj.a(paramString, Color.WHITE, false, 8)).setFontScale(this.br);
    float f3 = this.aL ? 24.0F : 8.0F;
    button.add((Actor)label).expandX().fillX().left().minHeight(f2).padLeft((paramTexture != null) ? 0.0F : f3);
    if (b.m != null) {
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(b.m)))).setScaling(Scaling.fit);
      f3 = this.aL ? (this.br * 1.5F) : 1.0F;
      float f = 9.0F * f3;
      f1 = 23.0F * f3;
      f2 = this.aL ? 16.0F : 4.0F;
      button.add((Actor)image).size(f, f1).padRight(f2).padLeft(8.0F).right();
    } 
    button.addListener((EventListener)new kn(this, paramkr, paramInt, paramString));
    return (Table)button;
  }
  
  private static String a(kr paramkr, String paramString1, String paramString2) {
    try {
      String str;
      if ((str = b.a((paramkr != null && paramkr.n != null) ? paramkr.n.S : null, paramString1)) != null && !str.isEmpty())
        return str; 
    } catch (Throwable throwable) {}
    return paramString2;
  }
  
  private void a(kr paramkr, int paramInt) {
    paramkr.J.clearChildren();
    paramkr.J.top().left();
    int[] arrayOfInt;
    if ((arrayOfInt = (int[])((paramkr.J != null && paramkr.J.size() > paramInt) ? paramkr.J.get(paramInt) : null)) == null || arrayOfInt.length == 0) {
      Label label;
      (label = lj.a("Sem itens.", Color.WHITE, false, 8)).setFontScale(this.br);
      paramkr.J.add((Actor)label).top().left();
      return;
    } 
    int i = arrayOfInt.length / 3;
    a(paramkr, i, paramInt2 -> {
          paramInt2 *= 3;
          int j = paramArrayOfint[paramInt2];
          int i = paramArrayOfint[paramInt2 + 2];
          jn jn = a(paramkr.a());
          switch (paramInt1) {
            case 0:
              jn.ao = i;
              break;
            case 1:
              jn.ap = i;
              break;
            case 2:
              jn.aq = i;
              break;
            case 3:
              jn.ar = i;
              break;
          } 
          Image image = a(paramkr, jn);
          return a(paramkr, (Actor)image, ());
        });
    paramkr.J.invalidateHierarchy();
  }
  
  private void a(kr paramkr, int paramInt, boolean paramBoolean) {
    paramkr.J.clearChildren();
    paramkr.J.top().left();
    int[] arrayOfInt;
    if ((arrayOfInt = (int[])((paramkr.K != null && paramkr.K.size() > paramInt) ? paramkr.K.get(paramInt) : null)) == null || arrayOfInt.length == 0) {
      Label label;
      (label = lj.a("Sem cores.", Color.WHITE, false, 8)).setFontScale(this.br);
      paramkr.J.add((Actor)label).top().left();
      return;
    } 
    int i = arrayOfInt.length / 2;
    a(paramkr, i, paramInt2 -> {
          paramInt2 *= 2;
          int j = paramArrayOfint[paramInt2];
          int i = e(paramArrayOfint[paramInt2 + 1]);
          int k = i;
          jn jn = a(paramkr.a());
          switch (paramInt1) {
            case 0:
              jn.as = k;
              break;
            case 1:
              jn.at = k;
              break;
            case 2:
              jn.au = k;
              break;
            case 3:
              jn.av = k;
              break;
            case 4:
              jn.aw = k;
              break;
          } 
          Image image = a(paramkr, jn);
          return a(paramkr, (Actor)image, ());
        });
    paramkr.J.invalidateHierarchy();
  }
  
  private void a(kr paramkr, int paramInt, kq paramkq) {
    float f1;
    float f2 = (f1 = lj.a(paramkr.n)) * this.cf;
    f1 = lj.f(f1);
    float f3 = this.aL ? 24.0F : 20.0F;
    int i;
    if ((i = (int)((paramkr.ci - f3 - 20.0F + f1) / (f2 + f1))) <= 0)
      i = 1; 
    Table table;
    (table = new Table()).top().left();
    table.defaults().space(f1).size(f2, f2).top().left();
    for (byte b = 0; b < paramInt; b++) {
      Actor actor = paramkq.make(b);
      table.add(actor);
      if ((b + 1) % i == 0)
        table.row(); 
    } 
    paramkr.J.add((Actor)table).top().left().expandX();
  }
  
  private static Drawable b() {
    return (Drawable)((b.d != null) ? b.d : new NinePatchDrawable((NinePatch)b.h));
  }
  
  private Actor a(kr paramkr, Actor paramActor, Runnable paramRunnable) {
    float f = lj.a(paramkr.n) * this.cf;
    Button.ButtonStyle buttonStyle;
    (buttonStyle = new Button.ButtonStyle()).up = b();
    buttonStyle.over = buttonStyle.up;
    buttonStyle.down = (b.e != null) ? (Drawable)b.e : b();
    buttonStyle.checked = buttonStyle.down;
    Button button;
    (button = new Button(buttonStyle)).defaults().center();
    button.add(paramActor).expand().fill().center();
    button.pack();
    button.setSize(f, f);
    button.addListener((EventListener)new kp(this, paramRunnable));
    return (Actor)button;
  }
  
  private static void b(kr paramkr) {
    Image image;
    if ((image = a(paramkr, paramkr.a())) != null) {
      paramkr.F.setDrawable(image.getDrawable());
      paramkr.F.invalidateHierarchy();
    } 
  }
  
  private static Image a(kr paramkr, jn paramjn) {
    try {
      if (lj.i(paramjn.aN))
        return null; 
      if (!(((paramjn.ao | paramjn.ap | paramjn.aq | paramjn.ar) != 0) ? 1 : 0))
        return null; 
      int i = f(paramjn.as);
      int j = f(paramjn.at);
      int k = f(paramjn.au);
      int m = f(paramjn.av);
      int n = f(paramjn.aw);
      bl bl;
      (bl = new bl(paramkr.n)).b(paramjn.am, paramjn.aN, paramjn.ao, paramjn.ap, paramjn.aq, paramjn.ar, i, j, k, m, n);
      Texture texture = bl.b();
      texture.setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
      TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(new TextureRegion(texture));
      in.a(texture);
      Image image;
      (image = new Image((Drawable)textureRegionDrawable)).setScaling(Scaling.fit);
      return image;
    } catch (Throwable throwable) {
      Gdx.app.error("OutfitShop0", "OutfitShop0 preview fail", throwable);
      return null;
    } 
  }
  
  private static Drawable c() {
    Pixmap pixmap;
    (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(0.0F, 0.0F, 0.0F, 0.0F);
    pixmap.fill();
    Texture texture = new Texture(pixmap);
    pixmap.dispose();
    return (Drawable)new TextureRegionDrawable(new TextureRegion(texture));
  }
  
  public static int e(int paramInt) {
    int i = paramInt >>> 8 & 0xFF;
    int j = paramInt >>> 16 & 0xFF;
    int k = paramInt >>> 24 & 0xFF;
    if ((i = i << 16 | j << 8 | k) == 0 && (paramInt & 0xFFFFFF) != 0)
      i = paramInt & 0xFFFFFF; 
    if (i == 0)
      i = 16777215; 
    return i;
  }
  
  private static int f(int paramInt) {
    return ((paramInt &= 0xFFFFFF) == 0) ? 16777215 : paramInt;
  }
  
  private static jn a(jn paramjn) {
    return new jn(paramjn.am, paramjn.aN, paramjn.ao, paramjn.ap, paramjn.aq, paramjn.ar, paramjn.as, paramjn.at, paramjn.au, paramjn.av, paramjn.aw);
  }
  
  private static TextureRegion a(Texture paramTexture) {
    return (paramTexture != null) ? new TextureRegion(paramTexture) : new TextureRegion(c());
  }
  
  private static Texture c() {
    Pixmap pixmap;
    (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap.fill();
    Texture texture = new Texture(pixmap);
    pixmap.dispose();
    return texture;
  }
}
