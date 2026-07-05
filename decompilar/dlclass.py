package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Button;
import com.badlogic.gdx.scenes.scene2d.ui.Cell;
import com.badlogic.gdx.scenes.scene2d.ui.Container;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.Scaling;
import java.util.Iterator;
import java.util.Map;

public final class dl extends gb {
  private Image a;
  
  private fj c;
  
  private static ScrollPane.ScrollPaneStyle a;
  
  private boolean ad = false;
  
  private ImageButton a;
  
  private ImageButton b;
  
  private ImageButton c;
  
  private ImageButton d;
  
  int cd = 0;
  
  private boolean ae = false;
  
  dw a;
  
  public Byte a;
  
  private ImageButton e;
  
  boolean af = false;
  
  private boolean ag = false;
  
  float[] l = new float[7];
  
  float[] m = new float[7];
  
  private Group[] a;
  
  private DragAndDrop a = null;
  
  private Table f;
  
  private ImageButton f;
  
  public dl(fj paramfj, Stage paramStage, cr paramcr, br parambr, cq paramcq, Map paramMap, bo parambo) {
    super(paramfj, paramStage, paramcr, parambr, paramcq, paramMap, parambo);
    this.a = (DragAndDrop)new Group[7];
    this.c = (ImageButton)paramfj;
    if (b.c != null) {
      this.a = (DragAndDrop)new Image((Drawable)b.c);
      this.a.setTouchable(Touchable.enabled);
      paramStage.addActor((Actor)this.a);
      this.a.toBack();
    } 
    dl dl1;
    if (!(dl1 = this).ad) {
      dl1.ad = true;
      if (dl1.i != null && dl1.b != null) {
        dl1.i.setTouchable(Touchable.disabled);
        dl1.b.setTouchable(Touchable.enabled);
        dl1.b.addListener((EventListener)new do(dl1));
      } 
      dq dq = new dq(dl1);
      if (dl1.q != null)
        dl1.q.addListener((EventListener)dq); 
      if (dl1.t != null)
        dl1.t.addListener((EventListener)dq); 
      if (dl1.r != null)
        dl1.r.addListener((EventListener)dq); 
      if (dl1.s != null)
        dl1.s.addListener((EventListener)dq); 
      if (dl1.d != null) {
        ScrollPane.ScrollPaneStyle scrollPaneStyle;
        (scrollPaneStyle = new ScrollPane.ScrollPaneStyle()).vScroll = (Drawable)new NinePatchDrawable((NinePatch)b.b);
        scrollPaneStyle.vScrollKnob = (Drawable)new NinePatchDrawable((NinePatch)b.c);
        if (scrollPaneStyle.vScroll instanceof BaseDrawable)
          ((BaseDrawable)scrollPaneStyle.vScroll).setMinWidth(8.0F); 
        if (scrollPaneStyle.vScrollKnob instanceof BaseDrawable) {
          ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinWidth(8.0F);
          ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinHeight(18.0F);
        } 
        dl1.d.setStyle(scrollPaneStyle);
        dl1.d.setFlickScroll(true);
        dl1.d.setFadeScrollBars(false);
        dl1.d.setScrollingDisabled(true, false);
        dl1.d.setCancelTouchFocus(false);
      } 
    } 
    aq();
    a((Label)this.i, 20.0F);
    a((Label)this.j, 20.0F);
    a((Label)this.k, 25.0F);
    a((Label)this.d, 25.0F);
    ImageButton.ImageButtonStyle imageButtonStyle;
    (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)b.d;
    imageButtonStyle.down = (Drawable)b.e;
    imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.e));
    imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.e));
    this.e = new ImageButton(imageButtonStyle);
    this.e.addListener((EventListener)new dm(this, paramcq, parambr, paramStage));
    paramStage.addActor((Actor)this.e);
    this.a = new DragAndDrop();
    String[] arrayOfString = { "Quest/Map", "Buttons", "AnalogStick", "Inventory", "Equipment", "Skill 1", "Skill 2" };
    Pixmap pixmap;
    (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(0.0F, 0.8F, 0.0F, 0.45F);
    pixmap.fill();
    TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(new TextureRegion(new Texture(pixmap)));
    pixmap.dispose();
    for (byte b = 0; b < 7; b++) {
      byte b1 = b;
      Group group = new Group();
      Image image;
      (image = new Image((Drawable)textureRegionDrawable)).setFillParent(true);
      group.addActor((Actor)image);
      Label label;
      (label = lj.a(arrayOfString[b], Color.WHITE, true, 1)).setFillParent(true);
      group.addActor((Actor)label);
      group.setVisible(false);
      paramStage.addActor((Actor)group);
      this.a[b] = (DragAndDrop)group;
      this.a.addSource(new dn(this, (Actor)group, group, b1, paramStage));
    } 
  }
  
  private static void a(Label paramLabel, float paramFloat) {
    if (paramLabel == null)
      return; 
    if (paramLabel.getStyle() != null && (paramLabel.getStyle()).font != null && (paramLabel.getStyle()).font.getLineHeight() > 0.0F) {
      if ((paramFloat /= (paramLabel.getStyle()).font.getLineHeight()) <= 0.01F)
        paramFloat = 1.0F; 
      paramLabel.setFontScale(paramFloat);
    } 
  }
  
  private boolean h() {
    return (this.i != null && this.i.isVisible());
  }
  
  final void h(boolean paramBoolean) {
    if (this.q == null || this.c == null)
      return; 
    this.c.setTouchable(Touchable.enabled);
    this.c.setFlickScroll(true);
    this.c.setScrollingDisabled(true, false);
    this.c.setFadeScrollBars(false);
    float f = this.c.getWidth();
    f = Math.max(0.0F, f - 16.0F - 6.0F);
    boolean bool = (this.c.getScrollPercentY() >= 0.97F) ? true : false;
    this.q.clear();
    this.q.setTouchable(Touchable.disabled);
    this.q.top().left().pad(4.0F);
    this.q.defaults().expandX().fillX().left();
    dl dl1 = this;
    switch (dv.y[dl1.a.ordinal()]) {
      case 1:
      
      case 2:
      
      case 3:
      
      default:
        break;
    } 
    TextField.TextFieldStyle<String> textFieldStyle = dl1.s;
    for (byte b = 0; b < textFieldStyle.size(); b++) {
      String str;
      if ((str = textFieldStyle.get(b)) == null)
        str = ""; 
      Label label;
      (((label = lj.a(str, Color.WHITE, true, 8)).getStyle()).font.getData()).markupEnabled = true;
      label.setText(str);
      label.setFontScale(1.5F);
      label.setWrap(true);
      label.setAlignment(8);
      label.setTouchable(Touchable.disabled);
      label.setWidth(f);
      this.q.add((Actor)label).width(f).expandX().fillX().left().row();
    } 
    this.q.invalidateHierarchy();
    this.q.pack();
    this.c.layout();
    if (paramBoolean || bool) {
      this.c.setScrollY(this.c.getMaxY());
      this.c.updateVisualScroll();
    } 
  }
  
  private void i(float paramFloat) {
    if (this.q == null)
      return; 
    paramFloat = Math.max(0.0F, paramFloat - 16.0F - 6.0F);
    Array.ArrayIterator<Actor> arrayIterator = this.q.getChildren().iterator();
    while (arrayIterator.hasNext()) {
      Label label;
      (label = (Label)actor).setFontScale(1.5F);
      label.setWrap(true);
      label.setAlignment(8);
      label.setWidth(paramFloat);
      label.setTouchable(Touchable.disabled);
      Cell cell;
      Actor actor;
      if (actor = arrayIterator.next() instanceof Label && (cell = this.q.getCell((Actor)label)) != null)
        cell.width(paramFloat).expandX().fillX().left(); 
    } 
    this.q.invalidateHierarchy();
  }
  
  private void ap() {
    if (this.c == null)
      return; 
    if (a == null) {
      ScrollPane.ScrollPaneStyle scrollPaneStyle;
      (scrollPaneStyle = new ScrollPane.ScrollPaneStyle()).background = null;
      scrollPaneStyle.vScroll = null;
      scrollPaneStyle.vScrollKnob = null;
      a = (DragAndDrop)scrollPaneStyle;
    } 
    this.c.setStyle((ScrollPane.ScrollPaneStyle)a);
    this.c.setFadeScrollBars(false);
    this.c.setScrollingDisabled(true, false);
    this.c.setFlickScroll(true);
    this.c.setTouchable(Touchable.enabled);
    this.c.setScrollBarPositions(false, true);
    this.c.setForceScroll(false, true);
  }
  
  private void aq() {
    if (this.ae)
      return; 
    if (this.i == null)
      return; 
    this.ae = true;
    this.i.addAction((Action)Actions.forever((Action)Actions.sequence((Action)Actions.delay(0.033F), (Action)Actions.run(this::ar))));
  }
  
  private void ar() {
    if (!h())
      return; 
    if (this.d == null || this.b == null)
      return; 
    if (!this.b.isVisible())
      return; 
    if (!this.d.isVisible())
      return; 
    as();
    float f1;
    if ((f1 = this.b.getHeight() * this.b.getScaleY()) <= 1.0F)
      return; 
    float f2 = ((this.j != null) ? (((cq)this.j).bP * ((cq)this.j).am) : 48.0F) * 2.5F;
    f2 = Math.max(this.d.getWidth(), f2);
    float f3 = this.b.getX() + this.b.getWidth() * this.b.getScaleX() - f2;
    float f4 = this.b.getY() + f1 + 2.0F;
    if ((Math.abs(this.d.getWidth() - f2) > 1.0F || Math.abs(this.d.getX() - f3) > 1.0F || Math.abs(this.d.getY() - f4) > 1.0F)) {
      this.d.setBounds(f3, f4, f2, f1);
      this.d.toFront();
    } 
  }
  
  private void as() {
    if (this.d == null)
      return; 
    this.d.setTransform(false);
    this.d.setScale(1.0F);
    Actor actor;
    if (actor = this.d.getActor() instanceof Label) {
      Label label;
      (label = (Label)actor).setFontScale(1.5F);
      label.setWrap(false);
      label.setAlignment(9);
    } 
    this.d.invalidateHierarchy();
    this.d.pack();
  }
  
  public final void at() {
    super.at();
    h(true);
    aq();
  }
  
  public final void au() {
    super.au();
    h(false);
    aq();
  }
  
  public final void av() {
    super.av();
    h(false);
  }
  
  public final void p(String paramString) {
    super.p(paramString);
    aq();
    h(true);
  }
  
  public final void q(String paramString) {
    paramString = a(paramString, hp.b);
    this.s.add(paramString);
    if (this.s.size() > 25)
      this.s.remove(0); 
    if (this.a == hp.b && h())
      h(false); 
  }
  
  public final void r(String paramString) {
    paramString = a(paramString, hp.c);
    this.t.add(paramString);
    if (this.t.size() > 25)
      this.t.remove(0); 
    if (this.a == hp.c && h())
      h(false); 
  }
  
  public final void s(String paramString) {
    paramString = a(paramString, hp.d);
    this.u.add(paramString);
    if (this.u.size() > 25)
      this.u.remove(0); 
    if (this.a == hp.d && h())
      h(false); 
  }
  
  public final void t(String paramString) {
    paramString = a(paramString, hp.e);
    this.v.add(paramString);
    if (this.v.size() > 25)
      this.v.remove(0); 
    if (this.a == hp.e && h())
      h(false); 
  }
  
  public final void b(int paramInt, float paramFloat) {
    super.b(paramInt, paramFloat);
    if (paramFloat <= 0.0F && this.e != null) {
      this.e.clearActions();
      this.e.setVisible(false);
    } 
  }
  
  public final void a(long paramLong) {
    super.a(paramLong);
    if (this.j != null) {
      this.j.getHeight();
      j(this.j.getWidth());
    } 
  }
  
  public final void b(long paramLong) {
    super.b(paramLong);
    if (this.j != null) {
      this.j.getHeight();
      j(this.j.getWidth());
    } 
  }
  
  public final void a(String paramString, float paramFloat1, float paramFloat2, Color paramColor, TextureRegion paramTextureRegion) {
    super.a(paramString, paramFloat1, paramFloat2, paramColor, paramTextureRegion);
    dl dl1;
    if ((dl1 = this).j != null)
      dl1.a(dl1.j.getWidth(), dl1.j.getHeight()); 
  }
  
  protected final void a(float paramFloat1, float paramFloat2) {
    if (this.l == null || this.l.length < 7)
      this.l = new float[7]; 
    if (this.m == null || this.m.length < 7)
      this.m = new float[7]; 
    if (this.a == null || this.a.length < 7)
      this.a = (DragAndDrop)new Group[7]; 
    if (this.j != null)
      this.j.h(paramFloat1); 
    float f1 = ((cq)this.j).bP;
    float f2 = ((cq)this.j).am;
    float f3 = f1 * f2;
    float f4 = 3.0F * f3 + 4.0F;
    if (!this.ag) {
      if (((cq)this.j).K) {
        float[] arrayOfFloat1 = ((cq)this.j).j;
        float[] arrayOfFloat2 = ((cq)this.j).k;
        for (byte b = 0; b < 7; b++) {
          this.l[b] = arrayOfFloat1[b];
          this.m[b] = arrayOfFloat2[b];
        } 
      } else {
        float f21 = 2.0F * f3 + 2.0F;
        float f22;
        float f23 = (f22 = paramFloat1 - 4.0F - f4) - 10.0F - f21;
        float f24 = 4.0F + f4 + 20.0F;
        float f25 = f4 * 0.9F;
        float f26 = (f4 - f25) / 2.0F;
        float f27 = f24 + f4 + 2.0F;
        float f28 = paramFloat1 - 4.0F - f21;
        this.l[0] = 4.0F;
        this.m[0] = f24 + f26;
        this.l[1] = f23;
        this.m[1] = f24;
        this.l[2] = 4.0F;
        this.m[2] = 4.0F;
        this.l[3] = f22;
        this.m[3] = f24;
        this.l[4] = f22;
        this.m[4] = 4.0F;
        this.l[5] = f28;
        this.m[5] = f27;
        this.l[6] = f28 + f3 + 2.0F;
        this.m[6] = f27;
      } 
      this.ag = true;
    } 
    float f5 = this.l[0];
    float f6 = this.m[0];
    float f7 = this.l[1];
    float f8 = this.m[1];
    float f9 = this.l[2];
    float f10 = this.m[2];
    float f11 = this.l[3];
    float f12 = this.m[3];
    float f13 = this.l[4];
    float f14 = this.m[4];
    NinePatchDrawable ninePatchDrawable1 = (b.m != null) ? new NinePatchDrawable((NinePatch)b.m) : null;
    NinePatchDrawable ninePatchDrawable2 = (b.n != null) ? new NinePatchDrawable((NinePatch)b.n) : null;
    if (this.o != null)
      this.o.setVisible(false); 
    float f15 = f4 + 20.0F + f4;
    f15 = 4.0F + f15 + 4.0F;
    if (this.a != null) {
      this.a.setVisible(true);
      this.a.setSize(paramFloat1, f15);
      this.a.setPosition(0.0F, 0.0F);
      this.a.toBack();
    } 
    int[][] arrayOfInt = { { 1, 2 }, { 0, 2 }, { 2, 1 }, { 0, 0 }, { 2, 2 }, { 0, 1 }, { 2, 0 } };
    for (byte b3 = 0; b3 < 7 && b3 < this.a.length; b3++) {
      int j = arrayOfInt[b3][0];
      int k = arrayOfInt[b3][1];
      DragAndDrop dragAndDrop;
      if ((dragAndDrop = this.a[b3]) != null) {
        dragAndDrop.setSize(f1, f1);
        dragAndDrop.setTransform(true);
        dragAndDrop.setScale(f2);
        dragAndDrop.setOrigin(12);
        dragAndDrop.setPosition(f13 + j * (f3 + 2.0F), f14 + k * (f3 + 2.0F));
        dragAndDrop.setVisible(true);
        dragAndDrop.toFront();
        dragAndDrop.setTouchable(Touchable.childrenOnly);
        Array.ArrayIterator<Actor> arrayIterator = dragAndDrop.getChildren().iterator();
        while (arrayIterator.hasNext()) {
          Actor actor;
          if (actor = arrayIterator.next() instanceof ImageButton) {
            ((ImageButton)actor).setFillParent(true);
            if (((ImageButton)actor).getImage() != null)
              ((ImageButton)actor).getImage().setScaling(Scaling.fit); 
            continue;
          } 
          if (actor instanceof Image) {
            ((Image)actor).setFillParent(true);
            ((Image)actor).setScaling(Scaling.none);
          } 
        } 
      } 
    } 
    if (this.d != null) {
      this.d.setSize(f1, f1);
      this.d.setOrigin(12);
      this.d.setScale(f2);
      float f21 = f13 + 1.0F * (f3 + 2.0F);
      float f22 = f14 + 1.0F * (f3 + 2.0F);
      this.d.setPosition(f21, f22);
      this.d.setScaling(Scaling.none);
      this.d.setTouchable(Touchable.disabled);
      this.d.toFront();
    } 
    if (this.h != null) {
      float f = f13 + 1.0F * (f3 + 2.0F);
      a((ImageButton)this.h, f1, f2, f, f14);
    } 
    if (this.a == null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.av));
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.au));
      this.a = (DragAndDrop)new ImageButton(imageButtonStyle);
      this.a.addListener((EventListener)new dr(this));
      this.j.addActor((Actor)this.a);
    } 
    if (this.b == null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      this.b = new ImageButton(imageButtonStyle);
      this.j.addActor((Actor)this.b);
    } 
    if (this.c == null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.at));
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.as));
      this.c = new ImageButton(imageButtonStyle);
      this.c.addListener((EventListener)new ds(this));
      this.j.addActor((Actor)this.c);
    } 
    if (this.d == null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ar));
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aq));
      this.d = new ImageButton(imageButtonStyle);
      this.d.addListener((EventListener)new dt(this));
      this.j.addActor((Actor)this.d);
    } 
    a((ImageButton)this.a, f1, f2, f7, f8 + 2.0F * (f3 + 2.0F));
    float f16 = f7 + 1.0F * (f3 + 2.0F);
    float f17 = f8 + 2.0F * (f3 + 2.0F);
    a(this.b, f1, f2, f16, f17);
    if (this.p != null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = this.p.getStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      this.p.setStyle((Button.ButtonStyle)imageButtonStyle);
      a(this.p, f1, f2, f16, f17);
      if (this.e != null) {
        this.e.remove();
        this.e = null;
      } 
      if (this.a != null) {
        this.a.setOrigin(12);
        this.a.setScale(f2);
        this.a.setSize(f1, f1);
        this.a.setPosition(f16, f17);
      } 
    } 
    if (this.n != null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = this.n.getStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      this.n.setStyle((Button.ButtonStyle)imageButtonStyle);
      a((ImageButton)this.n, f1, f2, f16, f8 + 1.0F * (f3 + 2.0F));
    } 
    a(this.c, f1, f2, f7, f8 + 1.0F * (f3 + 2.0F));
    if (this.m != null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = this.m.getStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      this.m.setStyle((Button.ButtonStyle)imageButtonStyle);
      a((ImageButton)this.m, f1, f2, f7, f8);
    } 
    a(this.d, f1, f2, f16, f8);
    for (byte b4 = 0; b4 < 3; b4++) {
      for (byte b = 0; b < 3; b++) {
        int j;
        if ((j = b4 * 3 + b) < 9 && this.a[j] != null) {
          float f = f11 + b * (f3 + 2.0F);
          f7 = f12 + (2 - b4) * (f3 + 2.0F);
          a((ImageButton)this.a[j], f1, f2, f, f7);
        } 
      } 
    } 
    float f18;
    float f19 = (f18 = f4 * 0.9F) / f2;
    if (this.a != null) {
      this.a.setVisible((this.cd == 0));
      if (this.cd == 0) {
        this.a.setSize(Math.round(f19), Math.round(f19));
        this.a.setOrigin(12);
        this.a.setTransform(true);
        this.a.setScale(f2);
        this.a.setPosition(Math.round(f5), Math.round(f6));
        this.a.setTouchable(Touchable.childrenOnly);
        this.a.toFront();
        if (this.j != null) {
          this.j.setFillParent(true);
          if (this.j.getImageCell() != null)
            this.j.getImageCell().expand().fill(); 
        } 
        if (this.b != null)
          this.b.setFillParent(true); 
      } 
    } 
    if (this.c != null) {
      this.c.setVisible((this.cd == 1));
      if (this.cd == 1) {
        this.c.setSize(Math.round(f19), Math.round(f19));
        this.c.setOrigin(12);
        this.c.setTransform(true);
        this.c.setScale(f2);
        this.c.setPosition(Math.round(f5), Math.round(f6));
        this.c.toFront();
        if (this.p != null) {
          f17 = this.c.getPadLeft();
          float f = this.c.getPadRight();
          f7 = this.c.getPadTop();
          f8 = this.c.getPadBottom();
          f11 = f19 - f17 - f;
          f12 = f19 - f7 - f8;
          this.p.setSize(f11, f12);
          this.p.setPosition(f17, f8);
        } 
        if (this.q != null) {
          this.q.setVisible(true);
          f17 = this.aL ? 8.0F : 3.0F;
          this.q.setSize(f17, f17);
          float f = this.c.getPadLeft();
          f7 = this.c.getPadBottom();
          f8 = f19 - f - this.c.getPadRight();
          f11 = f19 - this.c.getPadTop() - f7;
          f12 = f5 + f * f2 + (f8 * f2 - f17) * 0.5F;
          f13 = f6 + f7 * f2 + (f11 * f2 - f17) * 0.5F;
          this.q.setPosition(Math.round(f12), Math.round(f13));
          this.q.toFront();
        } 
      } else if (this.q != null) {
        this.q.setVisible(false);
      } 
    } else if (this.q != null) {
      this.q.setVisible(false);
    } 
    if (this.f == null) {
      this.f = (ImageButton)new Table();
      this.j.addActor((Actor)this.f);
      if (this.l != null)
        this.l.remove(); 
      if (this.i != null)
        this.i.remove(); 
      if (this.m != null)
        this.m.remove(); 
      if (this.j != null)
        this.j.remove(); 
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.i));
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.j));
      this.f = new ImageButton(imageButtonStyle);
      this.f.addListener((EventListener)new du(this));
      this.j.addActor((Actor)this.f);
    } 
    if (this.f != null && this.f != null) {
      boolean bool = (this.cd == 2) ? true : false;
      this.f.setVisible(bool);
      this.f.setVisible(bool);
      if (bool) {
        float f = 2.0F / f2;
        f7 = f19 - f1 - f;
        f11 = f1 / 2.0F;
        this.f.clear();
        Table table1;
        (table1 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.F));
        if (this.l != null)
          table1.add((Actor)this.l).size(f11 * 0.8F, f11 * 0.8F).padRight(4.0F); 
        if (this.i != null) {
          this.i.setFontScale(1.15F);
          table1.add((Actor)this.i).expandX().right().padRight(4.0F);
        } 
        Table table2;
        (table2 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.F));
        if (this.m != null)
          table2.add((Actor)this.m).size(f11 * 0.8F, f11 * 0.8F).padRight(4.0F); 
        if (this.j != null) {
          this.j.setFontScale(1.15F);
          table2.add((Actor)this.j).expandX().right().padRight(4.0F);
        } 
        this.f.add((Actor)table1).width(f7).height(f11).row();
        this.f.add((Actor)table2).width(f7).height(f11);
        this.f.setSize(Math.round(f7), Math.round(f1));
        this.f.setOrigin(12);
        this.f.setTransform(true);
        this.f.setScale(f2);
        this.f.setPosition(Math.round(f5), Math.round(f6 + f18 - f3));
        this.f.toFront();
        f5 = f5 + f7 * f2 + 2.0F;
        f6 = f6 + f18 - f3;
        a(this.f, f1, f2, f5, f6);
      } 
    } 
    if (this.a == null) {
      this.a = (DragAndDrop)new dw(this);
      this.j.addActor((Actor)this.a);
    } 
    this.a.setBounds(f9, f10, f4, f4);
    float f20 = 4.0F + f4 + 20.0F + f4 + 2.0F;
    if (this.o != null) {
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = this.o.getStyle()).up = (Drawable)ninePatchDrawable1;
      imageButtonStyle.down = (Drawable)ninePatchDrawable2;
      this.o.setStyle((Button.ButtonStyle)imageButtonStyle);
      a((ImageButton)this.o, f1, f2, 4.0F, f20);
    } 
    if (this.e != null)
      if (this.af) {
        f7 = 4.0F + f3 + 2.0F;
        a(this.e, f1, f2, f7, f20);
      } else {
        this.e.setVisible(false);
      }  
    if (this.q != null) {
      (this.q.getStyle()).up = (Drawable)ninePatchDrawable1;
      (this.q.getStyle()).down = (Drawable)ninePatchDrawable2;
      (this.q.getStyle()).checked = (Drawable)ninePatchDrawable2;
    } 
    if (this.t != null) {
      (this.t.getStyle()).up = (Drawable)ninePatchDrawable1;
      (this.t.getStyle()).down = (Drawable)ninePatchDrawable2;
      (this.t.getStyle()).checked = (Drawable)ninePatchDrawable2;
    } 
    if (this.r != null) {
      (this.r.getStyle()).up = (Drawable)ninePatchDrawable1;
      (this.r.getStyle()).down = (Drawable)ninePatchDrawable2;
      (this.r.getStyle()).checked = (Drawable)ninePatchDrawable2;
    } 
    if (this.s != null) {
      (this.s.getStyle()).up = (Drawable)ninePatchDrawable1;
      (this.s.getStyle()).down = (Drawable)ninePatchDrawable2;
      (this.s.getStyle()).checked = (Drawable)ninePatchDrawable2;
    } 
    if (this.b[0] != null)
      a(this.b[0], f1, f2, this.l[5], this.m[5]); 
    if (this.b[1] != null)
      a(this.b[1], f1, f2, this.l[6], this.m[6]); 
    if (this.i != null && this.i.isVisible()) {
      aq();
      f7 = f1;
      f13 = 8.0F * f2;
      f5 = f3 + f13;
      f1 = paramFloat1 - 8.0F;
      f9 = f3 * 0.95F;
      f10 = f4 + 2.0F + f9;
      f13 = f20 + f3 + 2.0F;
      this.i.setPosition(Math.round(4.0F), Math.round(f13));
      this.i.setSize(Math.round(f1), Math.round(f10));
      if (this.w != null) {
        this.w.setPosition(0.0F, 0.0F);
        this.w.setSize(Math.round(f1), Math.round(f4));
      } 
      if (this.d != null) {
        this.d.setTransform(true);
        this.d.setScale(f2);
        this.d.setOrigin(12);
        this.d.setScrollBarPositions(false, true);
        Actor actor;
        if (actor = this.d.getWidget() instanceof Table) {
          Table table;
          Array.ArrayIterator<Cell> arrayIterator = (table = (Table)actor).getCells().iterator();
          while (arrayIterator.hasNext()) {
            Cell cell;
            (cell = arrayIterator.next()).size(f7, f7);
            if (cell.getActor() instanceof ImageButton) {
              ImageButton imageButton1;
              (imageButton1 = (ImageButton)cell.getActor()).getImageCell().expand().fill();
              if (imageButton1.getImage() != null)
                imageButton1.getImage().setScaling(Scaling.fit); 
            } 
          } 
          table.invalidate();
          table.pack();
        } 
        f10 = f7 + 8.0F;
        f14 = (f4 - 4.0F) / f2;
        this.d.setBounds(0.0F, 2.0F, f10, f14);
        this.d.setVisible(true);
        this.d.toFront();
        this.d.layout();
      } 
      if (this.q != null && this.q.getParent() == this.i)
        this.q.setVisible(false); 
      if (this.t != null && this.t.getParent() == this.i)
        this.t.setVisible(false); 
      if (this.r != null && this.r.getParent() == this.i)
        this.r.setVisible(false); 
      if (this.s != null && this.s.getParent() == this.i)
        this.s.setVisible(false); 
      f12 = f4 + 2.0F;
      f10 = f5 + 2.0F;
      f14 = f1 - f10 - 2.0F;
      if (this.b != null) {
        this.b.setTransform(true);
        this.b.setScale(2.0F);
        this.b.setOrigin(12);
        float f21 = Math.round(f14 / 2.0F);
        f1 = Math.round(f9 / 2.0F);
        this.b.setSize(f21, f1);
        this.b.setPosition(Math.round(f10), Math.round(f12));
        if (this.i != null)
          this.i.setBounds(0.0F, 0.0F, f21, f1); 
        if (this.e != null)
          this.e.setSize(f21, f1); 
      } 
      if (this.d != null && this.d.isVisible()) {
        as();
        this.d.pack();
        float f21 = f3 * 2.5F;
        f1 = Math.max(this.d.getWidth(), f21);
        f5 = f12 + f9 + 2.0F;
        this.d.setBounds(f10 + f14 - f1, f5, f1, f9);
        this.d.toFront();
      } 
      float f = f4 - 4.0F;
      if (this.c != null) {
        this.c.setBounds(f10, 2.0F, f14, f);
        this.c.layout();
        ap();
        if (this.q != null) {
          this.q.setWidth(f14);
          this.q.top().left();
        } 
        i(f14);
      } 
      this.i.toFront();
    } 
    if (h())
      h(false); 
    f7 = (this.f != null && this.f.getHeight() > 0.0F) ? this.f.getHeight() : 62.0F;
    f8 = f3 * 0.3F / f7;
    f11 = f2 + f8;
    f5 = ((this.f != null) ? this.f.getHeight() : 0.0F) * f11;
    f6 = paramFloat2 - 4.0F - 35.0F - f5;
    if (this.f != null) {
      f8 = f6;
      this.f.setOrigin(12);
      this.f.setScale(f11);
      this.f.setPosition(Math.round(4.0F), Math.round(f8));
      this.f.toFront();
      this.g.setSize(105.0F, 14.0F);
      a((Actor)this.g, f8, 40.0F, f11);
      a((Actor)this.h, f8, 40.0F, f11);
      a((Actor)this.i, f8, 21.0F, f11);
      a((Actor)this.j, f8, 10.0F, f11);
      if ((f9 = (this.e.getStyle() != null && (this.e.getStyle()).font != null) ? (this.e.getStyle()).font.getLineHeight() : 16.0F) <= 0.0F)
        f9 = 16.0F; 
      if ((f10 = 24.0F * f11 / f9) <= 0.01F || Float.isNaN(f10) || Float.isInfinite(f10))
        f10 = 1.0F; 
      this.e.setSize(105.0F * f11, 14.0F * f11);
      this.e.setAlignment(1);
      a((Actor)this.e, f8, 40.0F, f11);
      this.e.setFontScale(f10);
      this.f.setSize(105.0F * f11, 14.0F * f11);
      this.f.setAlignment(1);
      a((Actor)this.f, f8, 21.0F, f11);
      this.f.setFontScale(f10);
      if (this.g != null)
        this.g.setVisible(false); 
      if (this.h != null) {
        f12 = this.f.getWidth() * f11;
        f13 = 111.0F * f11;
        f12 = Math.max(0.0F, f12 - f13);
        this.h.setSize(f12, 14.0F * f11);
        this.h.setAlignment(1);
        this.h.setFontScale(f10);
        f10 = 4.0F + f13;
        f14 = f8 + 40.0F * f11;
        this.h.setPosition(f10, f14);
        this.h.toFront();
      } 
      f12 = f6;
      this.d.setTransform(true);
      this.d.setScale(f11);
      this.d.setOrigin(12);
      if (this.d != null && this.d.isVisible() && (f13 = this.d.getHeight() * f11) > 0.0F) {
        f12 -= f13 + 5.0F * f11;
        this.d.setPosition(4.0F, f12);
        this.d.toFront();
      } 
      if (this.w != null) {
        f13 = f11;
        f10 = 27.0F * f13;
        boolean bool = false;
        Iterator<Container> iterator = this.w.iterator();
        while (iterator.hasNext()) {
          if (((Container)iterator.next()).isVisible()) {
            bool = true;
            break;
          } 
        } 
        if (bool) {
          f12 -= f10 + 5.0F * f11;
          float f = 4.0F;
          Iterator<Container> iterator1 = this.w.iterator();
          while (iterator1.hasNext()) {
            Container container;
            if ((container = iterator1.next()).isVisible()) {
              container.setTransform(true);
              container.setScale(f13);
              container.setOrigin(12);
              container.setSize(27.0F, 27.0F);
              container.setPosition(f, f12);
              container.toFront();
              f += f10 + 4.0F * f11;
            } 
          } 
        } 
      } 
    } 
    if (this.e != null) {
      if (this.n != null && this.o != null && this.k != null) {
        f1 = this.n.getWidth();
        f8 = this.n.getHeight();
        this.e.setSize(f1, f8);
        this.n.setPosition(0.0F, 0.0F);
        this.o.setPosition(30.0F, 11.0F);
        this.o.setHeight(14.0F);
        this.k.setSize(105.0F, 24.0F);
        this.k.setPosition(30.0F, 32.0F);
        this.k.setAlignment(1);
      } 
      this.e.setTransform(true);
      this.e.setScale(f11);
      this.e.setOrigin(12);
      f1 = this.e.getWidth() * f11;
      f8 = this.e.getHeight() * f11;
      f9 = paramFloat1 - 4.0F - f1;
      this.e.setPosition(Math.round(f9), Math.round(paramFloat2 - 4.0F - 35.0F - f8));
      this.e.toFront();
    } 
    e(paramFloat1, paramFloat2);
    f(paramFloat1, paramFloat2);
    if (this.a != null)
      this.a.toBack(); 
    if (this.aL) {
      DragAndDrop dragAndDrop;
      int j = (dragAndDrop = this.a).length;
      byte b;
      for (b = 0; b < j; b++) {
        DragAndDrop dragAndDrop1;
        if ((dragAndDrop1 = dragAndDrop[b]) != null)
          dragAndDrop1.toFront(); 
      } 
      j = (dragAndDrop = this.a).length;
      for (b = 0; b < j; b++) {
        DragAndDrop dragAndDrop1;
        if ((dragAndDrop1 = dragAndDrop[b]) != null)
          dragAndDrop1.toFront(); 
      } 
      if (this.h != null)
        this.h.toFront(); 
      if (this.a != null)
        this.a.toFront(); 
      if (this.b != null)
        this.b.toFront(); 
      if (this.p != null)
        this.p.toFront(); 
      if (this.a != null)
        this.a.toFront(); 
      if (this.c != null)
        this.c.toFront(); 
      if (this.d != null)
        this.d.toFront(); 
      if (this.a != null)
        this.a.toFront(); 
    } 
    if (this.o != null)
      this.o.toFront(); 
    if (this.m != null)
      this.m.toFront(); 
    if (this.n != null)
      this.n.toFront(); 
    ImageButton imageButton;
    int i = (imageButton = this.b).length;
    byte b2;
    for (b2 = 0; b2 < i; b2++) {
      ImageButton imageButton1;
      if ((imageButton1 = imageButton[b2]) != null)
        imageButton1.toFront(); 
    } 
    if (this.i != null && this.i.isVisible())
      this.i.toFront(); 
    if (this.cd == 0 && this.a != null && this.a.isVisible())
      this.a.toFront(); 
    if (this.cd == 1 && this.c != null && this.c.isVisible()) {
      this.c.toFront();
      if (this.q != null)
        this.q.toFront(); 
    } 
    if (this.cd == 2 && this.f != null && this.f.isVisible()) {
      this.f.toFront();
      if (this.f != null)
        this.f.toFront(); 
    } 
    if (q() && this.j != null) {
      if (this.c != null) {
        this.c.setVisible(true);
        this.c.setBounds(0.0F, 0.0F, paramFloat1, paramFloat2);
        this.c.toFront();
      } 
      this.j.toFront();
      if (this.aL) {
        DragAndDrop dragAndDrop;
        i = (dragAndDrop = this.a).length;
        for (b2 = 0; b2 < i; b2++) {
          DragAndDrop dragAndDrop1;
          if ((dragAndDrop1 = dragAndDrop[b2]) != null) {
            dragAndDrop1.toFront();
            dragAndDrop1.setTouchable(Touchable.enabled);
          } 
        } 
        i = (dragAndDrop = this.a).length;
        for (b2 = 0; b2 < i; b2++) {
          DragAndDrop dragAndDrop1;
          if ((dragAndDrop1 = dragAndDrop[b2]) != null) {
            dragAndDrop1.toFront();
            dragAndDrop1.setTouchable(Touchable.childrenOnly);
          } 
        } 
        if (this.h != null) {
          this.h.toFront();
          this.h.setTouchable(Touchable.enabled);
        } 
      } 
      if (this.o != null)
        this.o.setTouchable(Touchable.disabled); 
      if (this.m != null)
        this.m.setTouchable(Touchable.disabled); 
      if (this.n != null)
        this.n.setTouchable(Touchable.disabled); 
    } else {
      if (this.c != null)
        this.c.setVisible(false); 
      if (this.o != null)
        this.o.setTouchable(Touchable.enabled); 
      if (this.m != null)
        this.m.setTouchable(Touchable.enabled); 
      if (this.n != null)
        this.n.setTouchable(Touchable.enabled); 
      if (this.h != null)
        this.h.setTouchable(Touchable.enabled); 
    } 
    if (r() && this.f != null)
      this.f.toFront(); 
    if (this.c != null)
      this.c.toFront(); 
    for (byte b1 = 0; b1 < 7; b1++) {
      if (this.a[b1] != null) {
        float f21 = f4;
        float f22 = f4;
        if (b1 == 0) {
          f22 = f21 = f18;
        } else if (b1 == 1) {
          f21 = 2.0F * f3 + 2.0F;
        } else if (b1 == 5 || b1 == 6) {
          f21 = f3;
          f22 = f3;
        } 
        this.a[b1].setBounds(this.l[b1], this.m[b1], f21, f22);
        this.a[b1].setVisible(this.af);
        if (this.af)
          this.a[b1].toFront(); 
      } 
    } 
  }
  
  public final void aw() {
    this.af = true;
    this.m.g(b.a(((cq)this.j).S, "id_msg_edit_mode_active"));
    a(this.j.getWidth(), this.j.getHeight());
  }
  
  public final void ax() {
    this.ag = false;
    this.af = false;
    ((cq)this.j).K = false;
    cj.f((cq)this.j);
    this.m.g(b.a(((cq)this.j).S, "id_msg_layout_restored"));
    a(this.j.getWidth(), this.j.getHeight());
  }
  
  private void j(float paramFloat) {
    if (this.o == null || !this.o.isVisible())
      return; 
    float f1 = ((cq)this.j).bP;
    float f2 = ((cq)this.j).am;
    f1 *= f2;
    f1 = 3.0F * f1 + 4.0F;
    paramFloat = paramFloat - 4.0F - f1;
    this.o.pack();
    float f3;
    f2 = Math.max(((f3 = this.o.getWidth()) > 0.0F) ? (f1 / f3) : f2, 1.0F);
    this.o.setTransform(true);
    this.o.setScale(f2);
    this.o.setOrigin(12);
    f1 = 4.0F + f1 + 2.0F;
    this.o.setPosition(Math.round(paramFloat), Math.round(f1));
    this.o.toFront();
    if (this.f != null && this.o.getZIndex() <= this.f.getZIndex())
      this.o.setZIndex(this.f.getZIndex() + 1); 
    if (q() && this.j != null) {
      if (this.c != null)
        this.c.toFront(); 
      this.j.toFront();
      if (this.h != null)
        this.h.toFront(); 
    } 
    if (r() && this.f != null)
      this.f.toFront(); 
    if (this.c != null)
      this.c.toFront(); 
  }
  
  private static void a(ImageButton paramImageButton, float paramFloat1, float paramFloat2, float paramFloat3, float paramFloat4) {
    paramImageButton.setSize(Math.round(paramFloat1), Math.round(paramFloat1));
    paramImageButton.setPosition(Math.round(paramFloat3), Math.round(paramFloat4));
    paramImageButton.setTransform(true);
    paramImageButton.setScale(paramFloat2);
    paramImageButton.setOrigin(12);
    paramImageButton.setVisible(true);
    paramImageButton.toFront();
    paramImageButton.setTouchable(Touchable.enabled);
    if (paramImageButton.getImageCell() != null)
      paramImageButton.getImageCell().size(Math.round(paramFloat1), Math.round(paramFloat1)).align(1); 
    if (paramImageButton.getImage() != null) {
      paramImageButton.getImage().setScaling(Scaling.none);
      paramImageButton.getImage().setTouchable(Touchable.disabled);
    } 
  }
  
  private static void a(Actor paramActor, float paramFloat1, float paramFloat2, float paramFloat3) {
    if (paramActor != null) {
      paramActor.setPosition(Math.round(4.0F + 6.0F * paramFloat3), Math.round(paramFloat1 + paramFloat2 * paramFloat3));
      paramActor.setOrigin(12);
      if (paramActor instanceof Image)
        ((Image)paramActor).setScaling(Scaling.stretch); 
      if (paramActor instanceof Label) {
        paramFloat1 = (paramFloat3 <= 0.01F) ? 1.0F : paramFloat3;
        ((Label)paramActor).setFontScale(paramFloat1);
      } else {
        paramActor.setScale(paramFloat3);
      } 
      paramActor.toFront();
    } 
  }
  
  public final void resize(int paramInt1, int paramInt2) {
    super.resize(paramInt1, paramInt2);
    j(paramInt1);
  }
  
  public final void ay() {
    if (this.a != null)
      this.a.az(); 
  }
}
