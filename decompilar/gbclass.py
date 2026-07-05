package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Button;
import com.badlogic.gdx.scenes.scene2d.ui.ButtonGroup;
import com.badlogic.gdx.scenes.scene2d.ui.Cell;
import com.badlogic.gdx.scenes.scene2d.ui.Container;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Stack;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.IntArray;
import com.badlogic.gdx.utils.LongMap;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.TimeUtils;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.function.Consumer;
import java.util.function.Supplier;

public class gb {
  private fj c;
  
  protected final int dg = 105;
  
  protected final int dh = 14;
  
  protected final int di = 105;
  
  protected final int dj = 14;
  
  protected final int dk = 105;
  
  protected final int dl = 6;
  
  public final cr n;
  
  protected final cq j;
  
  protected final Stage j;
  
  protected final br m;
  
  protected Image b;
  
  protected final bo b;
  
  protected final Map z;
  
  protected boolean aL;
  
  protected float br;
  
  protected final float bs = 0.0F;
  
  protected final float bt = 2.0F;
  
  protected final float bu = 2.0F;
  
  protected final float bv = 10.0F;
  
  protected lg a;
  
  protected final ImageButton[] a;
  
  protected final ImageButton[] b;
  
  protected final Stack[] a;
  
  protected final Image[] a;
  
  protected ImageButton h;
  
  protected final Drawable[] a;
  
  protected final Drawable[] b;
  
  protected final int[] C;
  
  protected final int[] D;
  
  protected final Drawable[] c;
  
  protected final Drawable[] d;
  
  protected final Texture bf;
  
  protected final Actor[] a;
  
  private int dm;
  
  private Table n;
  
  private ScrollPane a;
  
  private ScrollPane.ScrollPaneStyle b;
  
  protected Group c;
  
  public int dn;
  
  protected ImageButton i;
  
  protected Drawable g;
  
  protected Drawable h;
  
  protected Image c;
  
  protected Stack a;
  
  protected ImageButton j;
  
  protected Label d;
  
  protected ScrollPane b;
  
  protected Container b;
  
  protected Image d;
  
  protected Image e;
  
  protected Image f;
  
  protected ho a;
  
  protected Image g;
  
  protected Image h;
  
  protected Image i;
  
  protected Image j;
  
  protected Label e;
  
  protected Label f;
  
  protected Label g;
  
  protected Label h;
  
  protected final float bw = 0.1F;
  
  public int do;
  
  public int cG;
  
  protected int dp;
  
  protected int cH;
  
  protected boolean aM;
  
  protected Group d;
  
  protected li a;
  
  protected Table o;
  
  protected Table p;
  
  protected Image k;
  
  protected Image l;
  
  protected Image m;
  
  protected Label i;
  
  protected Label j;
  
  protected Group e;
  
  protected Image n;
  
  protected Image o;
  
  protected Label k;
  
  protected final float bx;
  
  protected final float by;
  
  protected Pixmap a;
  
  protected Texture bg;
  
  protected Image p;
  
  protected Color[] a;
  
  protected Image q;
  
  protected int dq;
  
  protected int dr;
  
  protected final LongMap b;
  
  private int ds;
  
  private int dt;
  
  private int du;
  
  private long u;
  
  private boolean aN;
  
  protected int dv;
  
  protected int dw;
  
  protected Container c;
  
  protected Group f;
  
  protected Actor b;
  
  protected Image r;
  
  protected Image s;
  
  protected Label l;
  
  protected ImageButton k;
  
  protected ImageButton l;
  
  protected Group g;
  
  protected Image t;
  
  protected Image u;
  
  protected Group h;
  
  protected Pixmap b;
  
  protected Texture bh;
  
  protected TextureRegionDrawable e;
  
  protected int dx;
  
  protected int dy;
  
  protected int dz;
  
  protected int dA;
  
  protected boolean aO;
  
  protected float bz;
  
  protected float bA;
  
  protected boolean aP;
  
  protected int dB;
  
  protected Image v;
  
  protected static final int[] E = new int[] { 25, 40, 60 };
  
  protected be j;
  
  protected be p;
  
  protected Consumer a;
  
  protected ImageButton m;
  
  protected ImageButton n;
  
  protected ImageButton o;
  
  protected ImageButton p;
  
  protected float bB;
  
  protected float bC;
  
  protected Group i;
  
  protected Image w;
  
  protected ImageButton q;
  
  protected ImageButton r;
  
  protected ImageButton s;
  
  protected ImageButton t;
  
  protected ScrollPane c;
  
  protected Table q;
  
  protected ScrollPane d;
  
  protected hp a;
  
  protected List s;
  
  protected List t;
  
  protected List u;
  
  protected List v;
  
  protected TextField i;
  
  protected TextField.TextFieldStyle s;
  
  protected TextField.TextFieldStyle t;
  
  protected boolean aQ;
  
  protected String aj;
  
  protected Label m;
  
  protected Container d;
  
  protected Stack b;
  
  protected Label n;
  
  protected Container e;
  
  protected boolean aR;
  
  public Container f;
  
  public Image x;
  
  public Container g;
  
  public Image y;
  
  public Container h;
  
  public Image z;
  
  public Container i;
  
  public Image A;
  
  public Container j;
  
  public Image B;
  
  public final List w;
  
  protected Actor c;
  
  protected DragAndDrop b;
  
  protected boolean aS;
  
  protected boolean aT;
  
  protected boolean aU;
  
  protected Runnable a;
  
  private boolean aV;
  
  protected boolean aW;
  
  protected boolean aX;
  
  protected Group j;
  
  private Image C;
  
  private Label o;
  
  private ImageButton u;
  
  private ImageButton v;
  
  private ImageButton w;
  
  private NinePatchDrawable e;
  
  private NinePatchDrawable f;
  
  private Image D;
  
  ImageButton[] c;
  
  private Image[] b;
  
  int[] F;
  
  boolean[] a;
  
  private boolean aY;
  
  boolean aZ;
  
  private String ak;
  
  private int dC;
  
  int dD;
  
  private int dE;
  
  private TextureRegionDrawable f;
  
  Drawable i;
  
  private Drawable j;
  
  private TextureRegionDrawable g;
  
  private TextureRegionDrawable h;
  
  private TextureRegionDrawable i;
  
  private TextureRegionDrawable j;
  
  private TextureRegionDrawable k;
  
  public final void a(Consumer paramConsumer) {
    this.a = (boolean[])paramConsumer;
  }
  
  public final void e(be parambe) {
    this.p = (ImageButton)parambe;
  }
  
  private void o(int paramInt1, int paramInt2, int paramInt3) {
    if (this.p == null)
      return; 
    if (((be)this.p).aF != paramInt3)
      return; 
    paramInt3 = this.dq / 2 - ((this.dq % 2 == 0) ? 1 : 0);
    int i = this.dr / 2 - ((this.dr % 2 == 0) ? 1 : 0);
    paramInt1 -= paramInt3;
    paramInt2 -= i;
    paramInt1 = ((be)this.p).aD - paramInt1;
    paramInt2 = ((be)this.p).aE - paramInt2;
    if (paramInt1 < 0 || paramInt1 >= this.dq || paramInt2 < 0 || paramInt2 >= this.dr)
      return; 
    paramInt3 = this.a.getWidth() / this.dq;
    this.a.setColor(Color.WHITE);
    int[][] arrayOfInt;
    (arrayOfInt = new int[][] { { 0, 0 }, { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }).length;
    for (byte b = 0; b < 5; b++) {
      int[] arrayOfInt1 = arrayOfInt[b];
      int k = paramInt1 + arrayOfInt1[0];
      int j = paramInt2 + arrayOfInt1[1];
      if (k >= 0 && k < this.dq && j >= 0 && j < this.dr)
        this.a.fillRectangle(k * paramInt3, j * paramInt3, paramInt3, paramInt3); 
    } 
    this.bg.draw((Pixmap)this.a, 0, 0);
  }
  
  private void a(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5) {
    if (this.p == null)
      return; 
    if (((be)this.p).aF != this.dA)
      return; 
    this.b.setColor(Color.WHITE);
    int[][] arrayOfInt;
    (arrayOfInt = new int[][] { { 0, 0 }, { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }).length;
    for (byte b = 0; b < 5; b++) {
      int[] arrayOfInt1 = arrayOfInt[b];
      int j = ((be)this.p).aD + arrayOfInt1[0];
      int i = ((be)this.p).aE + arrayOfInt1[1];
      j -= paramInt1;
      i -= paramInt2;
      if (j >= 0 && j < paramInt3 && i >= 0 && i < paramInt4) {
        i = paramInt4 - 1 - i;
        this.b.fillRectangle(j * paramInt5, i * paramInt5, paramInt5, paramInt5);
      } 
    } 
  }
  
  final be a(float paramFloat1, float paramFloat2) {
    float f = this.g.getWidth();
    int m = this.dx * 2 + 1;
    f /= m;
    int i = MathUtils.clamp((int)(paramFloat1 / f), 0, m - 1);
    int j = MathUtils.clamp((int)(paramFloat2 / f), 0, m - 1);
    int k = this.dy - this.dx;
    int n = this.dz - this.dx;
    i = k + i;
    j = n + m - 1 - j;
    return new be(i, j, this.dA);
  }
  
  private static long b(int paramInt1, int paramInt2, int paramInt3) {
    return (paramInt3 & 0xFF) << 60L | (paramInt1 & 0x3FFFFFFF) << 30L | (paramInt2 & 0x3FFFFFFF);
  }
  
  public final void j(boolean paramBoolean) {
    this.aU = paramBoolean;
  }
  
  public final boolean m() {
    return this.aU;
  }
  
  public final void e(Runnable paramRunnable) {
    this.a = (boolean[])paramRunnable;
  }
  
  final void bf() {
    if (this.a != null)
      this.a.run(); 
    this.aU = false;
  }
  
  public gb(fj paramfj, Stage paramStage, cr paramcr, br parambr, cq paramcq, Map paramMap, bo parambo) {
    TextureRegion textureRegion;
    this.dg = 105;
    this.dh = 14;
    this.di = 105;
    this.dj = 14;
    this.dk = 105;
    this.dl = 6;
    this.aL = false;
    this.br = 1.0F;
    this.bs = 0.0F;
    this.bt = 2.0F;
    this.bu = 2.0F;
    this.bv = 10.0F;
    this.a = (boolean[])new ImageButton[9];
    this.b = (Image[])new ImageButton[2];
    this.a = (boolean[])new Stack[7];
    this.a = (boolean[])new Image[7];
    this.a = (boolean[])new Drawable[9];
    this.b = (Image[])new Drawable[9];
    this.C = (Image)new int[16];
    this.D = (Image)new int[2];
    this.c = (ImageButton[])new Drawable[2];
    this.d = (Container)new Drawable[2];
    this.a = (boolean[])new Actor[2];
    this.dm = 7;
    this.dn = 0;
    this.bw = 0.1F;
    this.do = 0;
    this.cG = 1;
    this.dp = 0;
    this.cH = 1;
    this.aM = false;
    this.bx = b.v.getWidth();
    this.by = b.v.getHeight();
    this.a = (boolean[])new Color[10];
    this.b = (Image[])new LongMap();
    this.ds = Integer.MIN_VALUE;
    this.dt = Integer.MIN_VALUE;
    this.du = Integer.MIN_VALUE;
    this.u = 0L;
    this.aN = false;
    this.dv = 4;
    this.dw = 20;
    this.dx = 35;
    this.aO = false;
    this.aP = false;
    this.dB = 30;
    this.j = null;
    this.p = null;
    this.a = null;
    this.a = (boolean[])hp.b;
    this.s = (TextField.TextFieldStyle)new ArrayList();
    this.t = (TextField.TextFieldStyle)new ArrayList();
    this.u = (ImageButton)new ArrayList();
    this.v = (ImageButton)new ArrayList();
    this.aQ = false;
    this.aj = null;
    this.aR = false;
    this.w = (ImageButton)new ArrayList();
    this.aS = false;
    this.aT = false;
    this.aU = false;
    this.aV = false;
    this.aW = false;
    this.aX = false;
    this.aY = false;
    this.aZ = false;
    this.ak = "";
    this.dC = 0;
    this.dD = 0;
    this.dE = 0;
    this.n = (Label)paramcr;
    this.c = (ImageButton[])paramfj;
    this.j = (TextureRegionDrawable)paramStage;
    this.j = (TextureRegionDrawable)paramcq;
    this.m = (Label)parambr;
    this.z = (Image)paramMap;
    this.b = (Image[])parambo;
    Pixmap pixmap1;
    (pixmap1 = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap1.fill();
    this.bf = new Texture(pixmap1);
    pixmap1.dispose();
    this.b = (Image[])new Image((Drawable)b.c);
    paramStage.addActor((Actor)this.b);
    gb gb1 = this;
    BitmapFont bitmapFont2 = b.d;
    BitmapFont bitmapFont5 = b.e;
    Supplier<ImageButton> supplier1 = () -> {
        ImageButton.ImageButtonStyle imageButtonStyle;
        (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = paramDrawable1;
        imageButtonStyle.down = paramDrawable2;
        return new ImageButton(imageButtonStyle);
      };
    byte b1;
    for (b1 = 0; b1 < 9; b1++) {
      byte b;
      int i1 = (b = b1) + 1;
      gb1.a[b] = (ImageButton)supplier1.get();
      boolean bool;
      (bool = gb1.a[b]).getImage().setScaling(Scaling.none);
      bool.getImageCell().expand().center();
      bool.addListener((EventListener)new hr(gb1, i1, false, bool));
      gb1.j.addActor(gb1.a[b]);
      gb1.a[b] = (gb1.a[b].getStyle()).imageUp;
      gb1.b[b] = (Image)(gb1.a[b].getStyle()).imageDown;
    } 
    for (b1 = 0; b1 < 2; b1++) {
      byte b = b1;
      int i1 = 101 + b1;
      gb1.b[b1] = (Image)supplier1.get();
      Image image;
      ImageButton.ImageButtonStyle imageButtonStyle = (image = gb1.b[b1]).getStyle();
      if (i1 == 101) {
        imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.Q));
        imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.P));
      } else {
        imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.S));
        imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.R));
      } 
      image.setStyle((Button.ButtonStyle)imageButtonStyle);
      gb1.c[b] = (ImageButton)imageButtonStyle.imageUp;
      gb1.d[b] = (Container)imageButtonStyle.imageDown;
      image.addListener((EventListener)new hr(gb1, i1, true, (Actor)image));
      gb1.j.addActor((Actor)image);
    } 
    gb1.a = (boolean[])new lg((ImageButton[])gb1.b, (Drawable[])gb1.c, (Drawable[])gb1.d);
    Texture texture2;
    if ((texture2 = b.al) == null) {
      Pixmap pixmap;
      (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(0.0F, 0.0F, 0.0F, 0.0F);
      pixmap.fill();
      texture2 = new Texture(pixmap);
      pixmap.dispose();
    } 
    gb1.d = (Container)new Image((Drawable)new TextureRegionDrawable(new TextureRegion(texture2)));
    gb1.j.addActor((Actor)gb1.d);
    int[] arrayOfInt = { 10, 11, 12, 13, 14, 15, 16 };
    for (byte b2 = 0; b2 < 7; b2++) {
      byte b = b2;
      int i1 = arrayOfInt[b2];
      ImageButton imageButton1;
      ImageButton.ImageButtonStyle imageButtonStyle = (imageButton1 = supplier1.get()).getStyle();
      switch (i1) {
        case 10:
          imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.Y));
          imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.X));
          break;
        case 11:
          imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aa));
          imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.Z));
          break;
        case 12:
          imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.W));
          imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.V));
          break;
        case 13:
          imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ac));
          imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ab));
          break;
        case 14:
          imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.U));
          imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.T));
          break;
        case 15:
          imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ag));
          imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.af));
          break;
        case 16:
          imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ae));
          imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ad));
          break;
      } 
      imageButton1.setStyle((Button.ButtonStyle)imageButtonStyle);
      imageButton1.addListener((EventListener)new hr(gb1, i1, false, (Actor)imageButton1));
      Image image;
      (image = new Image(null)).setTouchable(Touchable.disabled);
      gb1.a[b] = image;
      Stack stack;
      (stack = new Stack()).add((Actor)imageButton1);
      stack.add((Actor)image);
      gb1.a[b] = stack;
      gb1.j.addActor((Actor)stack);
    } 
    gb1.h = (TextureRegionDrawable)supplier1.get();
    ImageButton.ImageButtonStyle imageButtonStyle9;
    (imageButtonStyle9 = gb1.h.getStyle()).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ai));
    imageButtonStyle9.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ah));
    gb1.h.setStyle((Button.ButtonStyle)imageButtonStyle9);
    gb1.h.addListener((EventListener)new gj(gb1));
    gb1.j.addActor((Actor)gb1.h);
    gb1 = this;
    ImageButton.ImageButtonStyle imageButtonStyle2 = new ImageButton.ImageButtonStyle();
    NinePatchDrawable ninePatchDrawable5 = new NinePatchDrawable((NinePatch)b.e);
    imageButtonStyle2.up = (Drawable)ninePatchDrawable5;
    imageButtonStyle2.down = (Drawable)ninePatchDrawable5;
    gb1.j = (TextureRegionDrawable)new ImageButton(imageButtonStyle2);
    gb1.d = (Container)lj.a("", Color.BLACK, true, 1);
    gb1.d.setWrap(true);
    ScrollPane.ScrollPaneStyle scrollPaneStyle;
    (scrollPaneStyle = new ScrollPane.ScrollPaneStyle()).vScroll = (Drawable)new NinePatchDrawable((NinePatch)b.b);
    scrollPaneStyle.vScrollKnob = (Drawable)new NinePatchDrawable((NinePatch)b.c);
    float f2 = gb1.aL ? 20.0F : 10.0F;
    if (scrollPaneStyle.vScroll instanceof BaseDrawable)
      ((BaseDrawable)scrollPaneStyle.vScroll).setMinWidth(f2); 
    if (scrollPaneStyle.vScrollKnob instanceof BaseDrawable)
      ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinWidth(f2); 
    gb1.b = (Image[])new ScrollPane((Actor)gb1.d, scrollPaneStyle);
    gb1.b.setScrollingDisabled(true, false);
    gb1.b.setFadeScrollBars(false);
    gb1.b.setOverscroll(false, false);
    gb1.b = (Image[])new Container((Actor)gb1.b);
    gb1.b.pad(4.0F);
    gb1.b.fill();
    gb1.b.addListener((EventListener)new gk(gb1));
    gb1.a = (boolean[])new Stack();
    gb1.a.add((Actor)gb1.j);
    gb1.a.add((Actor)gb1.b);
    gb1.j.addActor((Actor)gb1.a);
    (gb1 = this).e = (NinePatchDrawable)new Image((Drawable)b.e);
    gb1.e.setVisible(false);
    gb1.e.setTouchable(Touchable.disabled);
    gb1.j.addActor((Actor)gb1.e);
    gb1.d = (Container)new Group();
    gb1.d.setTouchable(Touchable.disabled);
    gb1.j.addActor((Actor)gb1.d);
    gb1.a = (boolean[])new li((Group)gb1.d);
    k k;
    if ((k = (k)((b.a != null) ? b.a.a(528) : null)) != null) {
      k.c();
      textureRegion = k.b(0.0F);
    } else {
      Texture texture;
      if ((texture = b.al) == null) {
        Pixmap pixmap;
        (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(0.0F, 0.0F, 0.0F, 0.0F);
        pixmap.fill();
        texture = new Texture(pixmap);
        pixmap.dispose();
        b.al = texture;
      } 
      textureRegion = new TextureRegion(texture);
    } 
    gb1.bB = textureRegion.getRegionWidth();
    gb1.bC = textureRegion.getRegionHeight();
    TextureRegionDrawable textureRegionDrawable3 = new TextureRegionDrawable(textureRegion);
    ImageButton.ImageButtonStyle imageButtonStyle6;
    (imageButtonStyle6 = new ImageButton.ImageButtonStyle()).up = null;
    imageButtonStyle6.down = null;
    imageButtonStyle6.imageUp = (Drawable)textureRegionDrawable3;
    imageButtonStyle6.imageDown = (Drawable)textureRegionDrawable3;
    gb1.p = new ImageButton(imageButtonStyle6);
    gb1.p.setSize(((cq)gb1.j).bP, ((cq)gb1.j).bP);
    gb1.p.getImageCell().align(1);
    gb1.p.getImage().setScaling(Scaling.none);
    gb1.j.addActor((Actor)gb1.p);
    gb1.a = (boolean[])new ho();
    gb1.a.setVisible(false);
    gb1.a.setTouchable(Touchable.disabled);
    gb1.j.addActor((Actor)gb1.a);
    gb1.p.addListener((EventListener)new gs(gb1));
    gb1.f = (TextureRegionDrawable)new Image((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.q)));
    gb1.j.addActor((Actor)gb1.f);
    gb1.g = (TextureRegionDrawable)new Image((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.s)));
    gb1.j.addActor((Actor)gb1.g);
    gb1.g.setVisible(false);
    gb1.h = (TextureRegionDrawable)new Image((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.t)));
    gb1.j.addActor((Actor)gb1.h);
    gb1.i = (TextureRegionDrawable)new Image((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.u)));
    gb1.j.addActor((Actor)gb1.i);
    Label.LabelStyle labelStyle3 = new Label.LabelStyle(b.a((String)null), Color.WHITE);
    gb1.e = (NinePatchDrawable)new Label("0/0", labelStyle3);
    gb1.e.setAlignment(1);
    gb1.j.addActor((Actor)gb1.e);
    Label.LabelStyle labelStyle4 = new Label.LabelStyle(b.a((String)null), Color.WHITE);
    gb1.f = (TextureRegionDrawable)new Label("0/0", labelStyle4);
    gb1.f.setAlignment(1);
    gb1.j.addActor((Actor)gb1.f);
    gb1.j = (TextureRegionDrawable)new Image((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.w)));
    gb1.j.addActor((Actor)gb1.j);
    Label.LabelStyle labelStyle1 = new Label.LabelStyle(b.a((String)null), Color.WHITE);
    gb1.g = (TextureRegionDrawable)new Label("0/0", labelStyle1);
    gb1.g.setAlignment(1);
    gb1.j.addActor((Actor)gb1.g);
    Label.LabelStyle labelStyle2 = new Label.LabelStyle(b.a((String)null), Color.WHITE);
    gb1.h = (TextureRegionDrawable)new Label("1", labelStyle2);
    gb1.h.setAlignment(8);
    gb1.j.addActor((Actor)gb1.h);
    (gb1 = this).e = (NinePatchDrawable)new Group();
    gb1.n = (Label)new Image((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.r)));
    gb1.e.addActor((Actor)gb1.n);
    gb1.o = (Label)new Image((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.v)));
    gb1.e.addActor((Actor)gb1.o);
    gb1.k = (TextureRegionDrawable)lj.a("", Color.WHITE, false, 1);
    gb1.e.addActor((Actor)gb1.k);
    gb1.e.setVisible(false);
    gb1.j.addActor((Actor)gb1.e);
    gb1 = this;
    BitmapFont bitmapFont1 = b.c[13];
    BitmapFont bitmapFont4 = b.c[17];
    gb1.l = (ImageButton)new Image((Drawable)new TextureRegionDrawable((TextureRegion)bitmapFont1));
    gb1.i = (TextureRegionDrawable)lj.a("0", Color.WHITE, false, 16);
    gb1.m = (Label)new Image((Drawable)new TextureRegionDrawable((TextureRegion)bitmapFont4));
    gb1.j = (TextureRegionDrawable)lj.a("0", Color.WHITE, false, 16);
    NinePatchDrawable ninePatchDrawable6 = new NinePatchDrawable(b.F);
    NinePatchDrawable ninePatchDrawable7 = new NinePatchDrawable(b.G);
    gb1.l.setScaling(Scaling.fit);
    gb1.m.setScaling(Scaling.fit);
    Table table2;
    (table2 = new Table()).setBackground((Drawable)ninePatchDrawable6);
    table2.pad(2.0F, 6.0F, 2.0F, 6.0F);
    table2.add((Actor)gb1.l).size(16.0F, 16.0F).padRight(6.0F);
    table2.add((Actor)gb1.i).expandX().right();
    gb1.k = (TextureRegionDrawable)new Image();
    gb1.k.setScaling(Scaling.fit);
    gb1.k.setVisible(false);
    gb1.p = (ImageButton)new Table();
    gb1.p.setBackground((Drawable)ninePatchDrawable7);
    gb1.p.pad(3.0F);
    gb1.p.add((Actor)gb1.k).size(18.0F, 18.0F);
    Table table3;
    (table3 = new Table()).setBackground((Drawable)ninePatchDrawable6);
    table3.pad(2.0F, 6.0F, 2.0F, 6.0F);
    table3.add((Actor)gb1.m).size(16.0F, 16.0F).padRight(6.0F);
    table3.add((Actor)gb1.j).expandX().right();
    ImageButton.ImageButtonStyle imageButtonStyle3;
    (imageButtonStyle3 = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.i));
    imageButtonStyle3.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion((Texture)b.j));
    ImageButton imageButton;
    (imageButton = new ImageButton(imageButtonStyle3)).addListener((EventListener)new gq(gb1));
    gb1.o = (Label)new Table();
    gb1.o.setTouchable(Touchable.childrenOnly);
    gb1.o.center();
    gb1.o.add((Actor)table2).size(80.0F, 22.0F).padRight(4.0F);
    gb1.o.add((Actor)gb1.p).size(28.0F, 28.0F).padRight(4.0F);
    gb1.o.add((Actor)table3).size(80.0F, 22.0F).padRight(4.0F);
    gb1.o.add((Actor)imageButton).size(26.0F, 26.0F);
    gb1.o.pack();
    gb1.j.addActor((Actor)gb1.o);
    gb1.o.addAction((Action)Actions.forever(new gr(gb1)));
    gb1.d(gb1.j.getWidth(), gb1.j.getHeight());
    gb1 = this;
    String[] arrayOfString = { 
        "#000000", "#989898", "#00cb00", "#fecb98", "#986532", "#fefe00", "#656565", "#006500", "#3200cb", "#653200", 
        "#fe3200", "#fefefe" };
    gb1.a = (boolean[])new Color[arrayOfString.length];
    int i;
    for (i = 0; i < arrayOfString.length; i++) {
      String str = arrayOfString[i].startsWith("#") ? arrayOfString[i].substring(1) : arrayOfString[i];
      gb1.a[i] = Color.valueOf(str);
    } 
    i = gb1.dw * 2 + 1;
    int j = gb1.dw * 2 + 1;
    gb1.dq = i;
    gb1.dr = j;
    int m = gb1.dq * 2;
    int n = gb1.dr * 2;
    gb1.a = (boolean[])new Pixmap(m, n, Pixmap.Format.RGBA8888);
    gb1.a.setColor(gb1.a[0]);
    gb1.a.fill();
    gb1.bg = new Texture((Pixmap)gb1.a);
    gb1.p = (ImageButton)new Image((Drawable)new TextureRegionDrawable(new TextureRegion(gb1.bg)));
    gb1.p.setScaling(Scaling.fill);
    NinePatchDrawable ninePatchDrawable3 = new NinePatchDrawable(b.F);
    gb1.c = (ImageButton[])new Container((Actor)gb1.p);
    gb1.c.setBackground((Drawable)ninePatchDrawable3);
    gb1.c.pad(4.0F);
    gb1.c.fill();
    gb1.j.addActor((Actor)gb1.c);
    Pixmap pixmap3;
    (pixmap3 = new Pixmap(3, 3, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap3.fill();
    Texture texture3 = new Texture(pixmap3);
    pixmap3.dispose();
    gb1.q = (Table)new Image((Drawable)new TextureRegionDrawable(new TextureRegion(texture3)));
    gb1.j.addActor((Actor)gb1.q);
    gb1.c.setTouchable(Touchable.enabled);
    gb1.p.setTouchable(Touchable.enabled);
    gi gi = new gi(gb1);
    gb1.c.addListener((EventListener)gi);
    gb1.p.addListener((EventListener)gi);
    FileHandle fileHandle;
    byte[] arrayOfByte;
    if ((gb1 = this).a != null && gb1.a != null && (fileHandle = Gdx.files.local("JTME/map/minimap.dat")).exists() && (arrayOfByte = fileHandle.readBytes()).length >= 4) {
      ByteBuffer byteBuffer;
      int i1 = (byteBuffer = ByteBuffer.wrap(arrayOfByte).order(ByteOrder.LITTLE_ENDIAN)).getInt();
      gb1.b.clear();
      for (m = 0; m < i1 && byteBuffer.remaining() >= 10; m++) {
        n = byteBuffer.getInt();
        int i2 = byteBuffer.getInt();
        int i3 = byteBuffer.get() & 0xFF;
        int i4 = byteBuffer.get() & 0xFF;
        long l = b(n, i2, i3);
        gb1.b.put(l, Integer.valueOf(i4));
      } 
      gb1.ds = Integer.MIN_VALUE;
      gb1.bp();
    } 
    bA();
    float f1 = ((cq)(gb1 = this).j).bP;
    BitmapFont bitmapFont3 = b.d;
    BitmapFont bitmapFont7 = b.e;
    ImageButton.ImageButtonStyle imageButtonStyle5;
    (imageButtonStyle5 = new ImageButton.ImageButtonStyle()).up = (Drawable)bitmapFont3;
    imageButtonStyle5.down = (Drawable)bitmapFont7;
    imageButtonStyle5.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.an));
    imageButtonStyle5.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.am));
    gb1.m = (Label)new ImageButton(imageButtonStyle5);
    gb1.m.setSize(f1, f1);
    gb1.m.addListener((EventListener)new gf(gb1));
    gb1.j.addActor((Actor)gb1.m);
    ImageButton.ImageButtonStyle imageButtonStyle7;
    (imageButtonStyle7 = new ImageButton.ImageButtonStyle()).up = (Drawable)bitmapFont3;
    imageButtonStyle7.down = (Drawable)bitmapFont7;
    imageButtonStyle7.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ap));
    imageButtonStyle7.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ao));
    gb1.n = (Label)new ImageButton(imageButtonStyle7);
    gb1.n.setSize(f1, f1);
    gb1.n.addListener((EventListener)new gg(gb1));
    gb1.j.addActor((Actor)gb1.n);
    ImageButton.ImageButtonStyle imageButtonStyle8;
    (imageButtonStyle8 = new ImageButton.ImageButtonStyle()).up = (Drawable)bitmapFont3;
    imageButtonStyle8.down = (Drawable)bitmapFont7;
    imageButtonStyle8.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aj));
    imageButtonStyle8.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.ak));
    gb1.o = (Label)new ImageButton(imageButtonStyle8);
    gb1.o.setSize(f1, f1);
    gb1.o.addListener((EventListener)new gh(gb1));
    gb1.j.addActor((Actor)gb1.o);
    (gb1 = this).i = (TextureRegionDrawable)new Group();
    gb1.i.setTouchable(Touchable.enabled);
    NinePatchDrawable ninePatchDrawable2 = new NinePatchDrawable(b.D);
    gb1.w = (ImageButton)new Image((Drawable)ninePatchDrawable2);
    gb1.i.addActor((Actor)gb1.w);
    gb1.m = new Label("", new Label.LabelStyle(b.a((String)null), Color.WHITE));
    gb1.m.setAlignment(8);
    gb1.m.setTouchable(Touchable.disabled);
    NinePatchDrawable ninePatchDrawable4 = new NinePatchDrawable(b.F);
    gb1.d = new Container((Actor)gb1.m);
    gb1.d.setBackground((Drawable)ninePatchDrawable4);
    gb1.d.pad(4.0F, 8.0F, 4.0F, 8.0F);
    gb1.d.setTouchable(Touchable.enabled);
    gb1.bn();
    gb1.d.addListener((EventListener)new gy(gb1));
    gb1.i.addActor((Actor)gb1.d);
    ImageButton.ImageButtonStyle imageButtonStyle4;
    (imageButtonStyle4 = new ImageButton.ImageButtonStyle()).up = (Drawable)b.d;
    imageButtonStyle4.down = (Drawable)b.e;
    imageButtonStyle4.checked = (Drawable)b.e;
    (imageButtonStyle5 = new ImageButton.ImageButtonStyle(imageButtonStyle4)).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aL));
    imageButtonStyle5.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aK));
    imageButtonStyle5.imageChecked = imageButtonStyle5.imageDown;
    gb1.t = (TextField.TextFieldStyle)new ImageButton(imageButtonStyle5);
    (imageButtonStyle7 = new ImageButton.ImageButtonStyle(imageButtonStyle4)).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aJ));
    imageButtonStyle7.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aI));
    imageButtonStyle7.imageChecked = imageButtonStyle7.imageDown;
    gb1.q = (Table)new ImageButton(imageButtonStyle7);
    (imageButtonStyle8 = new ImageButton.ImageButtonStyle(imageButtonStyle4)).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aP));
    imageButtonStyle8.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aO));
    imageButtonStyle8.imageChecked = imageButtonStyle8.imageDown;
    gb1.r = new ImageButton(imageButtonStyle8);
    ImageButton.ImageButtonStyle imageButtonStyle1;
    (imageButtonStyle1 = new ImageButton.ImageButtonStyle(imageButtonStyle4)).imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aN));
    imageButtonStyle1.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aM));
    imageButtonStyle1.imageChecked = imageButtonStyle1.imageDown;
    gb1.s = (TextField.TextFieldStyle)new ImageButton(imageButtonStyle1);
    ButtonGroup buttonGroup;
    (buttonGroup = new ButtonGroup((Button[])new ImageButton[] { (ImageButton)gb1.t, (ImageButton)gb1.q, gb1.r, (ImageButton)gb1.s })).setMinCheckCount(1);
    buttonGroup.setMaxCheckCount(1);
    buttonGroup.setUncheckLast(true);
    gb1.q.setChecked(true);
    gb1.t.addListener((EventListener)new hi(gb1));
    gb1.q.addListener((EventListener)new hj(gb1));
    gb1.r.addListener((EventListener)new hk(gb1));
    gb1.s.addListener((EventListener)new hl(gb1));
    Table table1;
    (table1 = new Table()).defaults().space(0.0F).pad(0.0F);
    table1.add((Actor)gb1.q).row();
    table1.add((Actor)gb1.t).row();
    table1.add((Actor)gb1.r).row();
    table1.add((Actor)gb1.s).row();
    gb1.d = (Container)new ScrollPane((Actor)table1);
    gb1.d.setFadeScrollBars(false);
    gb1.d.setScrollingDisabled(true, false);
    gb1.d.setOverscroll(false, false);
    gb1.d.setScrollBarPositions(false, false);
    gb1.i.addActor((Actor)gb1.d);
    gb1.q = new Table();
    gb1.q.top().left().pad(4.0F);
    gb1.c = (ImageButton[])new ScrollPane((Actor)gb1.q);
    gb1.c.setFadeScrollBars(false);
    gb1.c.setScrollingDisabled(true, false);
    gb1.c.setFlickScroll(false);
    gb1.c.setTouchable(Touchable.disabled);
    gb1.i.addActor((Actor)gb1.c);
    Pixmap pixmap4;
    (pixmap4 = new Pixmap(1, (int)b.a.getCapHeight(), Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap4.fill();
    Texture texture4 = new Texture(pixmap4);
    pixmap4.dispose();
    TextureRegionDrawable textureRegionDrawable2 = new TextureRegionDrawable(new TextureRegion(texture4));
    Pixmap pixmap2;
    (pixmap2 = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(1.0F, 1.0F, 1.0F, 0.35F);
    pixmap2.fill();
    Texture texture1 = new Texture(pixmap2);
    pixmap2.dispose();
    TextureRegionDrawable textureRegionDrawable1 = new TextureRegionDrawable(new TextureRegion(texture1));
    BitmapFont bitmapFont6 = b.a(");
    gb1.s = new TextField.TextFieldStyle();
    gb1.s.font = bitmapFont6;
    gb1.s.fontColor = Color.WHITE;
    gb1.s.cursor = (Drawable)textureRegionDrawable2;
    gb1.s.selection = (Drawable)textureRegionDrawable1;
    gb1.s.background = (Drawable)new NinePatchDrawable(b.z);
    gb1.s.messageFontColor = new Color(1.0F, 1.0F, 1.0F, 0.5F);
    gb1.s.messageFont = bitmapFont6;
    gb1.t = new TextField.TextFieldStyle();
    gb1.t.font = bitmapFont6;
    gb1.t.fontColor = Color.WHITE;
    gb1.t.cursor = (Drawable)textureRegionDrawable2;
    gb1.t.selection = (Drawable)textureRegionDrawable1;
    gb1.t.background = (Drawable)new NinePatchDrawable(b.A);
    gb1.t.messageFontColor = gb1.s.messageFontColor;
    gb1.t.messageFont = bitmapFont6;
    gb1.i = (TextureRegionDrawable)new TextField("", gb1.s);
    gb1.i.setMaxLength(40);
    gb1.i.setFocusTraversal(false);
    gb1.i.setDisabled(true);
    gb1.i.setOnlyFontChars(false);
    gb1.n = lj.a("", new Color(1.0F, 1.0F, 1.0F, 0.5F), false, 8);
    gb1.n.setAlignment(8);
    gb1.n.setTouchable(Touchable.disabled);
    gb1.e = (NinePatchDrawable)new Container((Actor)gb1.n);
    gb1.e.setTouchable(Touchable.disabled);
    gb1.e.align(8);
    gb1.e.padLeft(8.0F);
    gb1.e.padBottom(1.0F);
    gb1.b = (Image[])new Stack();
    gb1.b.setTouchable(Touchable.childrenOnly);
    gb1.b.setVisible(false);
    gb1.b.addActor((Actor)gb1.i);
    gb1.b.addActor((Actor)gb1.e);
    gb1.bi();
    gb1.bk();
    gb1.i.addActor((Actor)gb1.b);
    gb1.i.addListener((EventListener)new hm(gb1));
    gb1.i.addListener((EventListener)new hn(gb1));
    gb1.i.addListener((EventListener)new gd(gb1));
    gb1.i.addListener((EventListener)new ge(gb1));
    gb1.i.setVisible(false);
    gb1.j.addActor((Actor)gb1.i);
    (gb1 = this).q = new Table();
    gb1.q.top().left().pad(4.0F);
    gb1.c = (ImageButton[])new ScrollPane((Actor)gb1.q);
    gb1.c.setFadeScrollBars(false);
    gb1.c.setScrollingDisabled(true, false);
    gb1.c.setFlickScroll(true);
    gb1.c.setTouchable(Touchable.enabled);
    gb1.i.addActor((Actor)gb1.c);
    gb1 = this;
    NinePatchDrawable ninePatchDrawable1 = new NinePatchDrawable(b.F);
    Supplier<Container> supplier = () -> {
        Image image = new Image();
        Container container;
        (container = new Container((Actor)image)).setBackground((Drawable)paramNinePatchDrawable);
        container.setSize(27.0F, 27.0F);
        container.pad(2.0F);
        this.j.addActor((Actor)container);
        this.w.add(container);
        return container;
      };
    gb1.x = new Image();
    gb1.f = (TextureRegionDrawable)supplier.get();
    gb1.y = new Image();
    gb1.g = (TextureRegionDrawable)supplier.get();
    gb1.z = new Image();
    gb1.h = (TextureRegionDrawable)supplier.get();
    gb1.A = new Image();
    gb1.i = (TextureRegionDrawable)supplier.get();
    gb1.B = new Image();
    gb1.j = (TextureRegionDrawable)supplier.get();
    a(paramStage.getWidth(), paramStage.getHeight());
    paramStage.addListener((EventListener)new gc(this));
    this.c = (ImageButton[])new Actor();
    this.c.setTouchable(Touchable.enabled);
    this.c.setBounds(0.0F, 0.0F, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
    this.c.addListener((EventListener)new gn(this));
    this.c.setVisible(false);
    paramStage.addActor((Actor)this.c);
    this.c.toFront();
    this.b = (Image[])new DragAndDrop();
    this.b.setDragTime(120);
  }
  
  protected final void bg() {
    String str = b.a(((cq)this.j).S, "id_sure_header");
    jm jm1;
    (jm1 = in.a((cq)this.j)).w = str;
    jm jm2;
    (jm2 = jm1.a(b.a(((cq)this.j).S, "id_sure_save_and_logout_text"))).bq = false;
    ju ju = jm2.a(b.a(((cq)this.j).S, "id_yes"), b.a(((cq)this.j).S, "id_no"), this::bh, (Runnable)null).a();
    in.a((Stage)this.j, ju);
  }
  
  private void bh() {
    if (this.aV)
      return; 
    this.aV = true;
    in.cf();
    try {
      if (this.m != null) {
        Label label = this.m;
        al.p();
        al.o();
        il il;
        (il = new il()).aj(20);
        label.b(il.a());
      } 
    } catch (IOException iOException) {
      Gdx.app.error("Net", "Falha ao enviar logout", iOException);
    } 
    try {
      if (this.m != null)
        this.m.N(); 
    } catch (Exception exception) {}
    Gdx.app.postRunnable(() -> this.n.setScreen((Screen)new hy((cr)this.n)));
    Gdx.app.postRunnable(() -> this.n.setScreen((Screen)new hy((cr)this.n)));
  }
  
  public final void Z(int paramInt) {
    d(0, paramInt, 8, 12);
    d(2, paramInt, 256, 6);
    boolean bool = ((paramInt & 0x40) != 0) ? true : false;
    int i = ((paramInt & 0x80) != 0) ? 1 : 0;
    if (bool && i) {
      a(3, true, 5);
    } else if (bool) {
      a(3, true, 3);
    } else if (i) {
      a(3, true, 4);
    } else {
      a(3, false, -1);
    } 
    if (this.w.size() > 1)
      ((Container)this.w.get(1)).setVisible(false); 
    if (this.w.size() > 4)
      ((Container)this.w.get(4)).setVisible(false); 
    bool = ((paramInt & 0x10) != 0) ? true : false;
    if (this.a != null) {
      this.a.setVisible(bool);
      if (bool)
        this.a.toFront(); 
    } 
    i = paramInt;
    gb gb1;
    if ((gb1 = this).k != null) {
      byte b = -1;
      if ((i & 0x200) != 0) {
        b = 7;
      } else if ((i & 0x2) != 0) {
        b = 2;
      } else if ((i & 0x4) != 0) {
        b = 1;
      } else if ((i & 0x1) != 0) {
        b = 0;
      } 
      if (b != -1 && b < b.d.length) {
        BitmapFont bitmapFont = b.d[b];
        gb1.k.setDrawable((Drawable)new TextureRegionDrawable((TextureRegion)bitmapFont));
        gb1.k.setVisible(true);
      } else {
        gb1.k.setDrawable(null);
        gb1.k.setVisible(false);
      } 
    } 
    if (this.j != null)
      ((cq)this.j).O = ((paramInt & 0x2) != 0); 
    if (this.j != null)
      ((cq)this.j).P = ((paramInt & 0x1) != 0); 
    if ((gb1 = this).f != null) {
      float f2 = gb1.f.getY() - 27.0F - 2.0F;
      float f1 = gb1.f.getX() + 6.0F;
      Iterator<Container> iterator = gb1.w.iterator();
      while (iterator.hasNext()) {
        Container container;
        if ((container = iterator.next()) != null && container.isVisible()) {
          container.setPosition(f1, f2);
          f1 += 29.0F;
        } 
      } 
    } 
  }
  
  private void d(int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
    paramInt2 = ((paramInt2 & paramInt3) != 0) ? 1 : 0;
    a(paramInt1, paramInt2, paramInt4);
  }
  
  private void a(int paramInt1, boolean paramBoolean, int paramInt2) {
    if (paramInt1 >= this.w.size())
      return; 
    Container container;
    Image image = (Image)(container = this.w.get(paramInt1)).getActor();
    if (paramBoolean && paramInt2 >= 0 && paramInt2 < b.d.length) {
      BitmapFont bitmapFont = b.d[paramInt2];
      image.setDrawable((Drawable)new TextureRegionDrawable((TextureRegion)bitmapFont));
      image.setSize(23.0F, 23.0F);
    } 
    container.setVisible(paramBoolean);
  }
  
  public void q(String paramString) {
    paramString = a(paramString, hp.b);
    this.s.add(paramString);
    if (this.s.size() > 25) {
      this.s.remove(0);
      if (this.a == hp.b) {
        bl();
        return;
      } 
    } else if (this.a == hp.b) {
      x(paramString);
    } 
  }
  
  public void r(String paramString) {
    paramString = a(paramString, hp.c);
    this.t.add(paramString);
    if (this.t.size() > 25) {
      this.t.remove(0);
      if (this.a == hp.c) {
        bl();
        return;
      } 
    } else if (this.a == hp.c) {
      x(paramString);
    } 
  }
  
  public void s(String paramString) {
    paramString = a(paramString, hp.d);
    this.u.add(paramString);
    if (this.u.size() > 25) {
      this.u.remove(0);
      if (this.a == hp.d) {
        bl();
        return;
      } 
    } else if (this.a == hp.d) {
      x(paramString);
    } 
  }
  
  public void t(String paramString) {
    paramString = a(paramString, hp.e);
    this.v.add(paramString);
    if (this.v.size() > 25) {
      this.v.remove(0);
      if (this.a == hp.e) {
        bl();
        return;
      } 
    } else if (this.a == hp.e) {
      x(paramString);
    } 
  }
  
  private void x(String paramString) {
    if (this.q == null)
      return; 
    Label label;
    (((label = lj.a(paramString, Color.WHITE, true, 8)).getStyle()).font.getData()).markupEnabled = true;
    label.setText(paramString);
    label.setWrap(true);
    label.setAlignment(8);
    this.q.add((Actor)label).width(this.c.getWidth() - 25.0F).expandX().fillX().left().padBottom(2.0F).row();
    this.q.layout();
    if (this.c.getScrollPercentY() >= 0.95F) {
      this.c.layout();
      this.c.setScrollPercentY(1.0F);
    } 
  }
  
  public final void y(String paramString) {
    if ((paramString = paramString.trim().replaceAll("\\[(#[0-9a-fA-F]{6}|[a-zA-Z]+)\\]", "")).isEmpty())
      return; 
    if ((this.a == hp.c && this.aQ)) {
      if (paramString.length() > 15)
        paramString = paramString.substring(0, 15); 
      this.aj = paramString;
      this.aQ = false;
      b.a(this.m, b.a(((cq)this.j).S, "id_chat_with") + ": " + b.a(((cq)this.j).S, "id_chat_with"));
      bn();
      a(this.j.getWidth(), this.j.getHeight());
      this.i.setText("");
      bi();
      bk();
      this.j.setKeyboardFocus((Actor)this.i);
      return;
    } 
    if (this.a == hp.c && (this.aj == null || this.aj.trim().isEmpty())) {
      this.aQ = true;
      this.i.setText("");
      bi();
      bk();
      bn();
      this.j.setKeyboardFocus((Actor)this.i);
      return;
    } 
    switch (hh.G[this.a.ordinal()]) {
      case 1:
        t("" + ((cq)this.j).Y + ": " + ((cq)this.j).Y);
        try {
          this.m.e("World", paramString);
        } catch (Exception exception) {}
        break;
      case 2:
        q("" + ((cq)this.j).Y + ": " + ((cq)this.j).Y);
        try {
          String str = paramString;
          Label label = this.m;
          il il;
          (il = new il()).aj(150);
          il.B(str);
          label.b(il.a());
          this.b.a(((cq)this.j).Y, paramString, 0);
        } catch (Exception exception) {}
        break;
      case 3:
        r("" + ((cq)this.j).Y + ": " + ((cq)this.j).Y);
        try {
          this.m.e(this.aj, paramString);
        } catch (Exception exception) {}
        break;
      case 4:
        s("" + ((cq)this.j).Y + ": " + ((cq)this.j).Y);
        try {
          this.m.e("*g", paramString);
        } catch (Exception exception) {}
        break;
    } 
    this.i.setText("");
    bi();
    bk();
    this.j.setKeyboardFocus((Actor)this.i);
  }
  
  static boolean a(Actor paramActor1, Actor paramActor2) {
    if (paramActor1 == null || paramActor2 == null)
      return false; 
    while (paramActor1 != null) {
      if (paramActor1 == paramActor2)
        return true; 
      Group group = paramActor1.getParent();
    } 
    return false;
  }
  
  final void bi() {
    if (this.n == null)
      return; 
    String str = (this.a == hp.c && this.aQ) ? b.a(((cq)this.j).S, "id_enter_name") : b.a(((cq)this.j).S, "id_enter_message");
    b.a(this.n, str);
    if (this.i != null) {
      this.i.setMessageText(str);
      this.i.invalidate();
    } 
    bj();
  }
  
  public final boolean n() {
    return (this.i != null && this.i.isVisible());
  }
  
  final void bj() {
    if (this.i == null || this.s == null || this.t == null)
      return; 
    String str1;
    if ((str1 = this.i.getText()) == null)
      str1 = ""; 
    String str2;
    if ((str2 = (String)((this.n != null) ? this.n.getText().toString() : "")) == null)
      str2 = ""; 
    BitmapFont bitmapFont = b.a(!str1.isEmpty() ? str1 : str2);
    boolean bool = false;
    if (this.s.font != bitmapFont || this.s.messageFont != bitmapFont) {
      TextField.TextFieldStyle textFieldStyle;
      (textFieldStyle = new TextField.TextFieldStyle(this.s)).font = bitmapFont;
      textFieldStyle.messageFont = bitmapFont;
      this.s = textFieldStyle;
      boolean bool1 = true;
    } 
    if (this.t.font != bitmapFont || this.t.messageFont != bitmapFont) {
      TextField.TextFieldStyle textFieldStyle;
      (textFieldStyle = new TextField.TextFieldStyle(this.t)).font = bitmapFont;
      textFieldStyle.messageFont = bitmapFont;
      this.t = textFieldStyle;
      bool = true;
    } 
    if (bool) {
      this.i.setStyle(this.i.hasKeyboardFocus() ? this.t : this.s);
      this.i.invalidate();
    } 
  }
  
  final void bk() {
    if (this.n == null || this.i == null)
      return; 
    this.n.setVisible(this.i.getText().isEmpty());
  }
  
  public void p(String paramString) {
    if (!this.i.isVisible())
      this.i.setVisible(true); 
    this.a = (boolean[])hp.c;
    this.r.setChecked(true);
    this.aj = paramString;
    this.m.setText(b.a(((cq)this.j).S, "id_chat_with") + ": " + b.a(((cq)this.j).S, "id_chat_with"));
    bl();
    this.aQ = false;
    this.i.setText("");
    this.b.setVisible(true);
    this.i.setVisible(true);
    this.i.setDisabled(false);
    bi();
    bk();
    bn();
    this.j.setKeyboardFocus((Actor)this.i);
    this.aR = true;
  }
  
  final void bl() {
    TextField.TextFieldStyle textFieldStyle2;
    ImageButton imageButton;
    TextField.TextFieldStyle textFieldStyle1;
    this.q.clear();
    switch (hh.G[this.a.ordinal()]) {
      case 3:
        textFieldStyle2 = this.t;
        break;
      case 4:
        imageButton = this.u;
        break;
      case 1:
        imageButton = this.v;
        break;
      default:
        textFieldStyle1 = this.s;
        break;
    } 
    for (String str : textFieldStyle1)
      x(str); 
    this.q.pack();
    this.c.layout();
    this.c.setScrollPercentY(1.0F);
    this.c.updateVisualScroll();
  }
  
  public void at() {
    this.i.setVisible(true);
    bl();
    if (this.aR) {
      this.b.setVisible(true);
      this.i.setVisible(true);
      this.i.setDisabled(false);
      this.j.setKeyboardFocus((Actor)this.i);
    } else {
      this.b.setVisible(false);
      this.i.setVisible(true);
      this.i.setDisabled(true);
      this.j.setKeyboardFocus(null);
    } 
    bi();
    bk();
    bn();
    a(this.j.getWidth(), this.j.getHeight());
  }
  
  public final void bm() {
    if (!this.i.isVisible())
      return; 
    this.aR = this.b.isVisible();
    this.i.setVisible(false);
    this.b.setVisible(false);
    this.i.setVisible(true);
    this.i.setDisabled(true);
    this.j.setKeyboardFocus(null);
    bi();
    bk();
    bn();
  }
  
  public void au() {
    this.b.setVisible(true);
    this.i.setVisible(true);
    this.i.setDisabled(false);
    bi();
    bk();
    bn();
    this.j.setKeyboardFocus((Actor)this.i);
    this.aR = true;
    a(this.j.getWidth(), this.j.getHeight());
  }
  
  public void av() {
    this.j.setKeyboardFocus(null);
    this.b.setVisible(false);
    this.i.setVisible(true);
    this.i.setDisabled(true);
    this.aR = false;
    bi();
    bk();
    bn();
  }
  
  final void bn() {
    boolean bool = (this.b != null && this.b.isVisible() && this.a == hp.c && this.aj != null && !this.aQ) ? true : false;
    if (this.d != null)
      this.d.setVisible(bool); 
  }
  
  final void bo() {
    String str = b.a(((cq)this.j).S, "id_showmenu_tooltip");
    jm jm;
    (jm = in.a((cq)this.j)).w = str;
    jm.bq = true;
    ju ju = jm.a(1, b.a(((cq)this.j).S, "id_premium"), 617, () -> this.m.n(0, 13)).a(2, b.a(((cq)this.j).S, "id_characterinfo"), 528, () -> this.m.n(0, 14)).a(3, b.a(((cq)this.j).S, "id_support"), 616, () -> this.m.n(0, 15)).b(4, b.a(((cq)this.j).S, "id_options"), 606, () -> {
          gb gb1;
          boolean bool;
          String str1 = (b.a(bool = ((cq)(gb1 = this).j).S, "id_options") != null) ? b.a(bool, "id_options") : "Options";
          String str3 = (b.a(bool, "id_help_options_default") != null) ? b.a(bool, "id_help_options_default") : "Select an option to view its details.";
          String str7 = str1;
          jm jm2;
          (jm2 = in.a((cq)gb1.j)).w = str7;
          jm2.bq = true;
          str7 = str3;
          (jm2 = jm2).at = str7;
          jm jm1 = jm2;
          str3 = (b.a(bool, "id_cat_controls") != null) ? b.a(bool, "id_cat_controls") : "CONTROLES";
          jm1.a(10, 1, " " + str3.toUpperCase(), (Runnable)null);
          str3 = (b.a(bool, "id_controls_keybinds") != null) ? b.a(bool, "id_controls_keybinds") : "Controls";
          str7 = b.a(bool, "id_help_controls");
          (jm2 = jm1).au = str7;
          jm2.a(11, 0, str3, () -> Gdx.app.postRunnable(()));
          str3 = (b.a(bool, "id_cat_video") != null) ? b.a(bool, "id_cat_video") : "VE GR;
          jm1.a(20, 1, " " + str3.toUpperCase(), (Runnable)null);
          str3 = (b.a(bool, "id_show_fps") != null) ? b.a(bool, "id_show_fps") : "Show FPS";
          String str5 = (b.a(bool, "id_help_fps") != null) ? b.a(bool, "id_help_fps") : "Displays your current Frames Per Second and Ping on the screen.";
          str7 = str5;
          (jm2 = jm1).au = str7;
          jm2.a(21, str3, ((cq)gb1.j).Q, paramBoolean -> {
                this.j.f(paramBoolean.booleanValue());
                cj.f((cq)this.j);
              });
          String[] arrayOfString2 = { "V-Sync", "30 FPS", "60 FPS", "120 FPS", "Ilimitado" };
          str5 = (b.a(bool, "id_fps_limit") != null) ? b.a(bool, "id_fps_limit") : "FPS Limit";
          String str6 = (b.a(bool, "id_help_fps_limit") != null) ? b.a(bool, "id_help_fps_limit") : "Controla o limite de quadros. Valores menores economizam bateria.";
          str7 = str6;
          (jm2 = jm1).au = str7;
          jm2.a(22, str5, arrayOfString2, ((cq)gb1.j).bI, paramInteger -> {
                this.j.K(paramInteger.intValue());
                this.j.ag();
                cj.f((cq)this.j);
              });
          String str2 = (b.a(bool, "id_enable_lights") != null) ? b.a(bool, "id_enable_lights") : "Enable Lights";
          str5 = (b.a(bool, "id_help_enable_lights") != null) ? b.a(bool, "id_help_enable_lights") : "Ativa ou desativa a iluminadinDesligue para melhorar o desempenho.";
          str7 = str5;
          (jm2 = jm1).au = str7;
          jm2.a(23, str2, ((cq)gb1.j).L, paramBoolean -> {
                this.j.e(paramBoolean.booleanValue());
                cj.f((cq)this.j);
              });
          str2 = (b.a(bool, "id_cat_interface") != null) ? b.a(bool, "id_cat_interface") : "INTERFACE E HUD";
          jm1.a(30, 1, " " + str2.toUpperCase(), (Runnable)null);
          str2 = (b.a(bool, "id_click_to_walk") != null) ? b.a(bool, "id_click_to_walk") : "Click to Walk";
          str5 = (b.a(bool, "id_help_click_to_walk") != null) ? b.a(bool, "id_help_click_to_walk") : "Enables or disables moving by tapping on the screen.";
          str7 = str5;
          (jm2 = jm1).au = str7;
          jm2.a(31, str2, ((cq)gb1.j).Y, paramBoolean -> {
                this.j.d(paramBoolean.booleanValue());
                cj.f((cq)this.j);
              });
          str2 = (b.a(bool, "id_analog_indicator") != null) ? b.a(bool, "id_analog_indicator") : "Movement Indicator";
          str5 = (b.a(bool, "id_help_analog_indicator") != null) ? b.a(bool, "id_help_analog_indicator") : "Exibe um indicador visual abaixo do personagem ao se movimentar.";
          str7 = str5;
          (jm2 = jm1).au = str7;
          jm2.a(32, str2, ((cq)gb1.j).M, paramBoolean -> {
                this.j.c(paramBoolean.booleanValue());
                cj.f((cq)this.j);
              });
          str2 = (b.a(bool, "id_show_creature_levels") != null) ? b.a(bool, "id_show_creature_levels") : "Show Creature Levels";
          str7 = b.a(bool, "id_help_creature_levels");
          (jm2 = jm1).au = str7;
          jm2.a(33, str2, ((cq)gb1.j).X, paramBoolean -> {
                ((cq)this.j).X = paramBoolean.booleanValue();
                cj.f((cq)this.j);
              });
          str2 = (b.a(bool, "id_circular_bars") != null) ? b.a(bool, "id_circular_bars") : "Circular HP/MP Bar";
          str7 = b.a(bool, "id_help_circular_bars");
          (jm2 = jm1).au = str7;
          jm2.a(34, str2, ((cq)gb1.j).V, paramBoolean -> {
                ((cq)this.j).V = paramBoolean.booleanValue();
                cj.f((cq)this.j);
              });
          String[] arrayOfString1 = new String[21];
          for (byte b = 0; b <= 20; b++)
            arrayOfString1[b] = "" + b * 5 + "%"; 
          String str4 = (b.a(bool, "id_bar_distance") != null) ? b.a(bool, "id_bar_distance") : "Bar Distance";
          str6 = (b.a(bool, "id_help_bar_distance") != null) ? b.a(bool, "id_help_bar_distance") : "Ajusta a distdas barras de HP e MP em relaao personagem.";
          int j = MathUtils.clamp(Math.round((((cq)gb1.j).ad - 0.5F) / 0.1F), 0, 20);
          str7 = str6;
          (jm2 = jm1).au = str7;
          jm2.a(35, str4, arrayOfString1, j, paramInteger -> {
                float f = 0.5F + paramInteger.intValue() * 0.1F;
                this.j.e(f);
                cj.f((cq)this.j);
              });
          if ((Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS)) {
            str4 = (b.a(bool, "id_edit_layout") != null) ? b.a(bool, "id_edit_layout") : "Edit UI Layout";
            str6 = (b.a(bool, "id_help_edit_layout") != null) ? b.a(bool, "id_help_edit_layout") : "Mova e organize os painda interface livremente.";
            str7 = str6;
            (jm2 = jm1).au = str7;
            jm2.a(36, str4, 606, () -> {
                  in.cf();
                  if (this instanceof dl)
                    ((dl)this).aw(); 
                });
            str4 = (b.a(bool, "id_restore_layout") != null) ? b.a(bool, "id_restore_layout") : "Restore Default Layout";
            str6 = (b.a(bool, "id_help_restore_layout") != null) ? b.a(bool, "id_help_restore_layout") : "Restaura todos os painpara as posioriginais.";
            str7 = str6;
            (jm2 = jm1).au = str7;
            jm2.a(37, str4, 616, () -> {
                  in.cf();
                  if (this instanceof dl)
                    ((dl)this).ax(); 
                });
          } 
          str4 = (b.a(bool, "id_cat_audio") != null) ? b.a(bool, "id_cat_audio") : ";
          jm1.a(40, 1, " " + str4.toUpperCase(), (Runnable)null);
          str6 = (b.a(bool, "id_sound_effect_volume") != null) ? b.a(bool, "id_sound_effect_volume") : "SFX Volume";
          int i = Math.round(((cq)gb1.j).ag * 20.0F);
          str7 = b.a(bool, "id_help_sfx_volume");
          (jm2 = jm1).au = str7;
          jm2.a(41, str6, arrayOfString1, i, paramInteger -> {
                float f = paramInteger.intValue() * 0.05F;
                this.j.f(f);
                al.a(f);
                cj.f((cq)this.j);
              });
          str6 = (b.a(bool, "id_ambient_volume") != null) ? b.a(bool, "id_ambient_volume") : "Music Volume";
          i = Math.round(((cq)gb1.j).ah * 20.0F);
          str7 = b.a(bool, "id_help_music_volume");
          (jm2 = jm1).au = str7;
          jm2.a(42, str6, arrayOfString1, i, paramInteger -> {
                float f = paramInteger.intValue() * 0.05F;
                this.j.g(f);
                al.b(f);
                cj.f((cq)this.j);
              });
          in.a((Stage)gb1.j, jm1.a());
        }).b(5, b.a(((cq)this.j).S, "id_logout"), 618, () -> bg()).a();
    in.a((Stage)this.j, ju);
  }
  
  public final void bp() {
    if (!((cq)this.j).N)
      return; 
    int i = ((cq)this.j).aD;
    int j = ((cq)this.j).aE;
    int k = ((cq)this.j).aF;
    int m = 0;
    int n = -this.dv;
    int i1 = this.dv;
    int i2;
    for (i2 = n; i2 <= i1; i2++) {
      for (int i5 = n; i5 <= i1; i5++) {
        int i6 = i + i2;
        int i7 = j + i5;
        long l = b(i6, i7, k);
        cg cg;
        if (!this.b.containsKey(l) && (cg = this.c.a(i6, i7, k)) != null) {
          m = a(cg);
          this.b.put(l, Integer.valueOf(m));
          m = 1;
        } 
      } 
    } 
    if (m != 0)
      bq(); 
    if (m == 0 && i == this.ds && j == this.dt && k == this.du)
      return; 
    this.ds = i;
    this.dt = j;
    this.du = k;
    this.a.setColor(this.a[0]);
    this.a.fill();
    i2 = this.a.getWidth() / this.dq;
    int i3;
    for (int i4 = -(i3 = this.dw); i4 <= i3; i4++) {
      for (int i5 = -i3; i5 <= i3; i5++) {
        long l = b(i + i4, j + i5, k);
        if (this.b.containsKey(l)) {
          int i7;
          boolean bool = ((i7 = ((Integer)this.b.get(l, Integer.valueOf(0))).intValue()) >= 0 && i7 < this.a.length) ? this.a[i7] : this.a[0];
          this.a.setColor(bool);
          int i6 = (i4 + i3) * i2;
          n = (i5 + i3) * i2;
          this.a.fillRectangle(i6, n, i2, i2);
        } 
      } 
    } 
    r(i, j, k);
    o(i, j, k);
    this.bg.draw((Pixmap)this.a, 0, 0);
    if (r())
      bD(); 
  }
  
  private static int a(cg paramcg) {
    cf cf;
    for (int i = ((IntArray)(cf = paramcg.a)).size - 1; i >= 0; i--) {
      ah ah;
      if ((ah = b.a.a(cf.get(i))) != null && ah.L != -1)
        return ah.L; 
    } 
    return 0;
  }
  
  private void bq() {
    long l;
    if ((l = TimeUtils.millis()) - this.u < 10000L || this.aN)
      return; 
    this.u = l;
    this.aN = true;
    int i = ((LongMap)this.b).size;
    ByteBuffer byteBuffer;
    (byteBuffer = ByteBuffer.allocate(4 + i * 10).order(ByteOrder.LITTLE_ENDIAN)).putInt(i);
    byte b = 0;
    for (LongMap.Entry entry : this.b.entries()) {
      if (b < i) {
        long l1 = entry.key;
        int j = ((Integer)entry.value).intValue();
        int k = (int)(l1 >>> 60L & 0xFL);
        int m = (int)(l1 >>> 30L & 0x3FFFFFFFL);
        int n = (int)(l1 & 0x3FFFFFFFL);
        byteBuffer.putInt(m);
        byteBuffer.putInt(n);
        byteBuffer.put((byte)k);
        byteBuffer.put((byte)j);
        b++;
      } 
    } 
    (new Thread(() -> {
          try {
            FileHandle fileHandle;
            (fileHandle = Gdx.files.local("JTME/map/minimap.dat")).parent().mkdirs();
            fileHandle.writeBytes(paramByteBuffer.array(), false);
            return;
          } catch (Exception exception) {
            Gdx.app.error("Minimap", "Error async save", exception);
            return;
          } finally {
            this.aN = false;
          } 
        })).start();
  }
  
  public final void k(boolean paramBoolean) {
    this.aW = paramBoolean;
    br();
    this.i.setVisible(false);
    if (this.j != null)
      this.j.setVisible(false); 
    if (this.c != null) {
      paramBoolean = (paramBoolean && (this.j == null || !this.j.isVisible()));
      this.c.setVisible(paramBoolean);
      this.c.toFront();
      this.c.setSize(this.j.getWidth(), this.j.getHeight());
      this.c.setPosition(0.0F, 0.0F);
    } 
    this.j.setKeyboardFocus(null);
  }
  
  public final boolean o() {
    return this.aW;
  }
  
  public final void l(boolean paramBoolean) {
    this.aX = paramBoolean;
  }
  
  public final void z(String paramString) {
    if (paramString == null)
      paramString = ""; 
    BitmapFont bitmapFont = b.a(paramString);
    if (this.d != null) {
      Label.LabelStyle labelStyle;
      if ((labelStyle = this.d.getStyle()) == null || labelStyle.font != bitmapFont) {
        (labelStyle = (labelStyle != null) ? new Label.LabelStyle(labelStyle) : new Label.LabelStyle(bitmapFont, Color.BLACK)).font = bitmapFont;
        if (labelStyle.fontColor == null) {
          labelStyle.fontColor = new Color(Color.BLACK);
        } else {
          labelStyle.fontColor.set(Color.BLACK);
        } 
        this.d.setStyle(labelStyle);
      } 
      this.d.setText(paramString);
      this.d.invalidateHierarchy();
    } 
    if (this.b != null) {
      this.b.invalidateHierarchy();
      this.b.layout();
      this.b.setScrollPercentY(0.0F);
    } 
  }
  
  protected void a(float paramFloat1, float paramFloat2) {
    int i = (Gdx.app.getType() == Application.ApplicationType.Android) ? 1 : 0;
    boolean bool = (paramFloat2 > paramFloat1) ? true : false;
    this.aL = (i || bool);
    this.br = this.aL ? 1.3F : 1.0F;
    this.dm = 7;
    i = ((cq)this.j).bP;
    this.p.setSize(i, i);
    this.p.setOrigin(12);
    this.p.setScale(1.0F);
    if (this.p.getImage() != null)
      this.p.getImage().setScaling(Scaling.none); 
    this.p.setPosition(10.0F, paramFloat2 - 10.0F - i * 1.0F);
    if (this.a != null) {
      this.a.setSize(i, i);
      this.a.setOrigin(12);
      this.a.setScale(1.0F);
      this.a.setPosition(this.p.getX(), this.p.getY());
      this.a.toFront();
    } 
    this.f.setOrigin(12);
    this.f.setScale(1.0F);
    this.f.setPosition(this.p.getX() + i * 1.0F + 5.0F, paramFloat2 - 10.0F - this.f.getHeight() * 1.0F);
    if (this.e != null) {
      float f14 = this.p.getX() - (i - this.p.getWidth()) / 2.0F;
      float f15 = this.p.getY() - (i - this.p.getHeight()) / 2.0F - 2.0F;
      this.e.setSize(i, i);
      this.e.setOrigin(12);
      this.e.setScale(1.0F);
      this.e.setPosition(Math.round(f14), Math.round(f15));
      this.e.setZIndex(Math.max(0, this.p.getZIndex() - 1));
    } 
    if (this.a != null && this.p != null) {
      this.a.a(this.p.getX(), this.p.getY(), ((cq)this.j).bP);
      try {
        this.d.setZIndex(this.p.getZIndex() + 2);
      } catch (Exception exception) {}
    } 
    float f2 = this.f.getX();
    float f3 = this.f.getY();
    this.g.setSize(105.0F, 14.0F);
    this.g.setOrigin(12);
    this.g.setScale(1.0F);
    this.g.setPosition(f2 + 6.0F, f3 + 40.0F);
    this.h.setOrigin(12);
    this.h.setScale(1.0F);
    this.h.setPosition(f2 + 6.0F, f3 + 40.0F);
    this.h.setHeight(14.0F);
    this.e.setSize(105.0F, 14.0F);
    this.e.setPosition(f2 + 6.0F, f3 + 40.0F);
    this.e.setAlignment(1);
    this.i.setOrigin(12);
    this.i.setScale(1.0F);
    this.i.setPosition(f2 + 6.0F, f3 + 21.0F);
    this.i.setHeight(14.0F);
    this.f.setSize(105.0F, 14.0F);
    this.f.setPosition(f2 + 6.0F, f3 + 21.0F);
    this.f.setAlignment(1);
    this.j.setOrigin(12);
    this.j.setScale(1.0F);
    this.j.setPosition(f2 + 6.0F, f3 + 10.0F);
    this.j.setHeight(6.0F);
    this.g.setVisible(false);
    f2 += 111.0F;
    float f6 = (this.f.getWidth() - 6.0F - 105.0F) * 1.0F;
    f3 += 40.0F;
    this.h.setSize(f6, 14.0F);
    this.h.setPosition(f2, f3);
    this.h.setAlignment(1);
    f2 = ((f2 = (this.e.getStyle() != null && (this.e.getStyle()).font != null) ? (this.e.getStyle()).font.getLineHeight() : 16.0F) > 0.0F) ? (24.0F / f2) : 1.0F;
    this.e.setFontScale(f2);
    this.f.setFontScale(f2);
    if (this.h != null)
      this.h.setFontScale(f2); 
    if (this.g != null)
      this.g.setFontScale(f2); 
    d(paramFloat1, paramFloat2);
    f2 = (3 * i) + 0.0F + 4.0F;
    this.b.setSize(f2, paramFloat2);
    this.b.setPosition(Math.round(paramFloat1 - f2), 0.0F);
    f3 = this.b.getX();
    f6 = this.b.getY();
    float f8 = f3 + 2.0F;
    f6 += 2.0F;
    int[][] arrayOfInt = { { 1, 2 }, { 0, 2 }, { 2, 1 }, { 0, 0 }, { 2, 2 }, { 0, 1 }, { 2, 0 } };
    for (byte b2 = 0; b2 < arrayOfInt.length; b2++) {
      int j = arrayOfInt[b2][0];
      int k = arrayOfInt[b2][1];
      boolean bool1;
      (bool1 = this.a[b2]).setSize(i, i);
      bool1.setPosition(f8 + j * (i + 0.0F), f6 + k * (i + 0.0F));
    } 
    this.h.setSize(i, i);
    this.h.setPosition(f8 + i + 0.0F, f6);
    float f10 = f6 + 2.0F * (i + 0.0F) + i + 2.0F;
    float f11 = f3 + 2.0F + ((3 * i) + 0.0F - (2 * i) + 0.0F) / 2.0F;
    for (byte b3 = 0; b3 < 2; b3++) {
      this.b[b3].setSize(i, i);
      this.b[b3].setPosition(f11 + b3 * (i + 0.0F), f10);
    } 
    this.d.setSize(i, i);
    this.d.setPosition(f8 + i + 0.0F, f6 + i + 0.0F);
    float f12 = f10 + i + 2.0F;
    float f13 = f3 + 2.0F;
    for (byte b1 = 0; b1 < 3; b1++) {
      for (byte b = 0; b < 3; b++) {
        int j = b1 * 3 + b;
        this.a[j].setSize(i, i);
        this.a[j].setPosition(f13 + b * (i + 0.0F), f12 + (2 - b1) * (i + 0.0F));
      } 
    } 
    float f9 = (f8 = (2 * i) + 2.0F) - this.c.getPadTop() - this.c.getPadBottom();
    this.p.setSize(f9, f9);
    float f5 = f9 + this.c.getPadLeft() + this.c.getPadRight();
    this.c.setSize(f5, f8);
    this.c.setPosition(f3 + f2 - 2.0F - f5, paramFloat2 - 2.0F - f8);
    f2 = this.aL ? 8.0F : 3.0F;
    this.q.setSize(f2, f2);
    f2 = this.c.getX() + this.c.getPadLeft() + (f9 - this.q.getWidth()) * 0.5F;
    f5 = this.c.getY() + this.c.getPadBottom() + (f9 - this.q.getHeight()) * 0.5F;
    this.q.setPosition(f2, f5);
    f2 = this.c.getX() - 2.0F - i;
    f5 = this.c.getY() + f8;
    this.m.setPosition(f2, f5 - i);
    this.n.setPosition(f2, f5 - (2 * i) - 2.0F);
    this.e.setSize(this.n.getWidth(), this.n.getHeight());
    f2 = f3 - 2.0F - this.n.getWidth();
    f5 = paramFloat2 - 10.0F - this.n.getHeight();
    this.e.setPosition(f2, f5);
    this.n.setPosition(0.0F, 0.0F);
    this.o.setPosition(30.0F, 11.0F);
    this.o.setHeight(14.0F);
    this.k.setSize(105.0F, 24.0F);
    this.k.setPosition(30.0F, 30.0F);
    this.k.setAlignment(1);
    f2 = ((f2 = (this.k.getStyle() != null && (this.k.getStyle()).font != null) ? (this.k.getStyle()).font.getLineHeight() : 16.0F) > 0.0F) ? (24.0F / f2) : 1.0F;
    this.k.setFontScale(f2);
    f2 = (3 * i) + 0.0F;
    f5 = (3 * i) + 0.0F;
    f2 = f12 + f2;
    if ((f8 = this.c.getY() - 2.0F - f2) >= i / 2.0F) {
      f3 += 2.0F;
      this.a.setVisible(true);
      if (this.b != null && this.b.getStyle() != null) {
        f9 = this.aL ? 15.0F : 20.0F;
        Drawable drawable1 = (this.b.getStyle()).vScroll;
        Drawable drawable2 = (this.b.getStyle()).vScrollKnob;
        if (drawable1 instanceof BaseDrawable)
          ((BaseDrawable)drawable1).setMinWidth(f9); 
        if (drawable2 instanceof BaseDrawable)
          ((BaseDrawable)drawable2).setMinWidth(f9); 
        this.b.invalidate();
      } 
      this.a.setBounds(Math.round(f3), Math.round(f2), Math.round(f5), Math.round(f8));
      this.j.setSize(Math.round(f5), Math.round(f8));
      this.b.setSize(Math.round(f5), Math.round(f8));
      this.b.layout();
    } else {
      this.a.setVisible(false);
    } 
    this.o.setPosition(10.0F, 10.0F);
    this.o.setPosition(10.0F, 10.0F);
    f9 = this.o.getX() + i + 2.0F;
    f11 = this.b.getX() - f9 - 10.0F;
    f2 = (3 * i) + 8.0F;
    f3 = this.o.getY() - 2.0F;
    this.i.setBounds(Math.round(f9), Math.round(f3), Math.round(f11), Math.round(f2));
    this.w.setSize(Math.round(f11), Math.round(f2));
    this.w.setPosition(0.0F, 0.0F);
    f3 = this.aL ? 20.0F : 10.0F;
    f3 = i + f3;
    f5 = (3 * i);
    ScrollPane.ScrollPaneStyle scrollPaneStyle;
    (scrollPaneStyle = new ScrollPane.ScrollPaneStyle()).vScroll = (Drawable)new NinePatchDrawable((NinePatch)b.b);
    scrollPaneStyle.vScrollKnob = (Drawable)new NinePatchDrawable((NinePatch)b.c);
    f9 = this.aL ? 35.0F : 16.0F;
    if (scrollPaneStyle.vScroll instanceof BaseDrawable)
      ((BaseDrawable)scrollPaneStyle.vScroll).setMinWidth(f9); 
    if (scrollPaneStyle.vScrollKnob instanceof BaseDrawable) {
      ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinWidth(f9);
      ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinHeight(f9 + 10.0F);
    } 
    if (this.c != null)
      this.c.setStyle(scrollPaneStyle); 
    (scrollPaneStyle = new ScrollPane.ScrollPaneStyle()).vScroll = (Drawable)new NinePatchDrawable((NinePatch)b.b);
    scrollPaneStyle.vScrollKnob = (Drawable)new NinePatchDrawable((NinePatch)b.c);
    f9 = this.aL ? 20.0F : 8.0F;
    if (scrollPaneStyle.vScroll instanceof BaseDrawable)
      ((BaseDrawable)scrollPaneStyle.vScroll).setMinWidth(f9); 
    if (scrollPaneStyle.vScrollKnob instanceof BaseDrawable) {
      ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinWidth(f9);
      ((BaseDrawable)scrollPaneStyle.vScrollKnob).setMinHeight(f9 + 10.0F);
    } 
    if (this.d != null)
      this.d.setStyle(scrollPaneStyle); 
    this.d.setBounds(2.0F, 2.0F, f3, f5);
    Actor actor;
    if (this.d != null && actor = this.d.getWidget() instanceof Table) {
      Table table;
      Array.ArrayIterator<Cell> arrayIterator = (table = (Table)actor).getCells().iterator();
      while (arrayIterator.hasNext())
        ((Cell)arrayIterator.next()).size(i, i); 
      table.invalidate();
    } 
    float f4 = 2.0F + f3 + 2.0F;
    float f7 = f11 - f4 - 2.0F;
    f9 = f2 - 4.0F;
    this.c.setBounds(f4, 2.0F, f7, f9);
    f2 = i * 0.7F;
    this.b.setSize(f7, f2);
    this.b.setPosition(f4, 2.0F + f9 + 2.0F);
    this.i.setBounds(0.0F, 0.0F, f7, f2);
    this.e.setSize(f7, f2);
    this.d.pack();
    f3 = this.d.getWidth();
    f4 = this.d.getHeight();
    float f1 = i * 2.0F;
    f1 = Math.max(f3, f1);
    f2 = Math.max(f4, f2);
    f3 = this.b.getX() + this.b.getWidth() - f1;
    f4 = this.b.getY() + this.b.getHeight() + 2.0F;
    this.d.setSize(f1, f2);
    this.d.setPosition(f3, f4);
    this.d.setZIndex(this.b.getZIndex() + 1);
    f1 = this.f.getY() - 27.0F - 2.0F;
    f2 = this.f.getX() + 6.0F;
    Iterator<Container> iterator = this.w.iterator();
    while (iterator.hasNext()) {
      Container container;
      if ((container = iterator.next()).isVisible()) {
        container.setPosition(f2, f1);
        f2 += 29.0F;
      } 
    } 
    e(paramFloat1, paramFloat2);
    f(paramFloat1, paramFloat2);
  }
  
  public final void p(int paramInt1, int paramInt2, int paramInt3) {
    // Byte code:
    //   0: iload_1
    //   1: bipush #101
    //   3: isub
    //   4: dup
    //   5: istore #4
    //   7: iflt -> 28
    //   10: iload #4
    //   12: aload_0
    //   13: getfield D : [I
    //   16: arraylength
    //   17: if_icmpge -> 28
    //   20: aload_0
    //   21: getfield D : [I
    //   24: iload #4
    //   26: iload_2
    //   27: iastore
    //   28: aload_0
    //   29: getfield a : La/lg;
    //   32: iload_1
    //   33: iload_2
    //   34: iload_3
    //   35: istore #4
    //   37: istore_3
    //   38: istore_2
    //   39: astore_1
    //   40: iload_3
    //   41: ifne -> 127
    //   44: iload_2
    //   45: bipush #101
    //   47: isub
    //   48: dup
    //   49: istore_3
    //   50: iflt -> 62
    //   53: iload_3
    //   54: aload_1
    //   55: getfield d : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   58: arraylength
    //   59: if_icmplt -> 63
    //   62: return
    //   63: aload_1
    //   64: getfield H : [I
    //   67: iload_3
    //   68: iconst_0
    //   69: iastore
    //   70: aload_1
    //   71: getfield d : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   74: iload_3
    //   75: aaload
    //   76: dup
    //   77: astore #4
    //   79: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   82: dup
    //   83: astore #5
    //   85: aload_1
    //   86: getfield e : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   89: iload_3
    //   90: aaload
    //   91: putfield imageUp : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   94: aload #5
    //   96: aload_1
    //   97: getfield f : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   100: iload_3
    //   101: aaload
    //   102: putfield imageDown : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   105: aload #4
    //   107: aload #5
    //   109: invokevirtual setStyle : (Lcom/badlogic/gdx/scenes/scene2d/ui/Button$ButtonStyle;)V
    //   112: aload #4
    //   114: invokevirtual getImage : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   117: aconst_null
    //   118: invokevirtual setDrawable : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   121: aload_1
    //   122: iload_2
    //   123: invokevirtual aq : (I)V
    //   126: return
    //   127: iload_2
    //   128: bipush #101
    //   130: isub
    //   131: dup
    //   132: istore_2
    //   133: iflt -> 145
    //   136: iload_2
    //   137: aload_1
    //   138: getfield d : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   141: arraylength
    //   142: if_icmplt -> 146
    //   145: return
    //   146: aload_1
    //   147: getfield H : [I
    //   150: iload_2
    //   151: iload_3
    //   152: iastore
    //   153: aload_1
    //   154: getfield d : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   157: iload_2
    //   158: aaload
    //   159: dup
    //   160: astore #5
    //   162: invokevirtual getImage : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   165: getstatic com/badlogic/gdx/utils/Scaling.none : Lcom/badlogic/gdx/utils/Scaling;
    //   168: invokevirtual setScaling : (Lcom/badlogic/gdx/utils/Scaling;)V
    //   171: aload #5
    //   173: invokevirtual getImageCell : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Cell;
    //   176: invokevirtual expand : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Cell;
    //   179: invokevirtual center : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Cell;
    //   182: pop
    //   183: aload #5
    //   185: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   188: astore #6
    //   190: getstatic a/b.a : La/l;
    //   193: ifnull -> 206
    //   196: getstatic a/b.a : La/l;
    //   199: iload_3
    //   200: invokevirtual a : (I)La/k;
    //   203: goto -> 207
    //   206: aconst_null
    //   207: dup
    //   208: astore_3
    //   209: ifnull -> 240
    //   212: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   215: dup
    //   216: aload_3
    //   217: fconst_0
    //   218: invokevirtual b : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   221: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   224: astore_1
    //   225: aload #6
    //   227: aload_1
    //   228: putfield imageUp : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   231: aload #6
    //   233: aload_1
    //   234: putfield imageDown : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   237: goto -> 262
    //   240: aload #6
    //   242: aload_1
    //   243: getfield e : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   246: iload_2
    //   247: aaload
    //   248: putfield imageUp : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   251: aload #6
    //   253: aload_1
    //   254: getfield f : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   257: iload_2
    //   258: aaload
    //   259: putfield imageDown : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   262: aload #5
    //   264: aload #6
    //   266: invokevirtual setStyle : (Lcom/badlogic/gdx/scenes/scene2d/ui/Button$ButtonStyle;)V
    //   269: aload #5
    //   271: invokevirtual getImage : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   274: aload #5
    //   276: invokevirtual getWidth : ()F
    //   279: aload #5
    //   281: invokevirtual getHeight : ()F
    //   284: invokevirtual setSize : (FF)V
    //   287: aload #5
    //   289: invokevirtual getImage : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   292: fconst_0
    //   293: fconst_0
    //   294: invokevirtual setPosition : (FF)V
    //   297: iload #4
    //   299: ifle -> 309
    //   302: aload #5
    //   304: iconst_1
    //   305: invokevirtual setDisabled : (Z)V
    //   308: return
    //   309: aload #5
    //   311: iconst_0
    //   312: invokevirtual setDisabled : (Z)V
    //   315: return
  }
  
  public final void q(int paramInt1, int paramInt2, int paramInt3) {
    this.a.s(paramInt1, paramInt2, paramInt3);
  }
  
  public final void c(int[] paramArrayOfint) {
    if (paramArrayOfint == null || paramArrayOfint.length != 16)
      return; 
    System.arraycopy(paramArrayOfint, 0, this.C, 0, 16);
    for (byte b1 = 0; b1 < 9; b1++) {
      int i = paramArrayOfint[b1];
      boolean bool;
      ImageButton.ImageButtonStyle imageButtonStyle = (bool = this.a[b1]).getStyle();
      if (i != 0) {
        n n;
        if ((n = (n)((b.a != null) ? b.a.a(i) : null)) != null) {
          n.d();
          TextureRegion textureRegion = n.c(0.0F);
          TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(textureRegion);
          imageButtonStyle.imageUp = (Drawable)textureRegionDrawable;
          imageButtonStyle.imageDown = (Drawable)textureRegionDrawable;
        } else {
          imageButtonStyle.imageUp = this.a[b1];
          imageButtonStyle.imageDown = (Drawable)this.b[b1];
        } 
      } else {
        imageButtonStyle.imageUp = this.a[b1];
        imageButtonStyle.imageDown = (Drawable)this.b[b1];
      } 
      bool.setStyle((Button.ButtonStyle)imageButtonStyle);
    } 
    float f = ((cq)this.j).bP;
    for (byte b2 = 0; b2 < 7; b2++) {
      int i = 9 + b2;
      int j = paramArrayOfint[i];
      boolean bool = this.a[b2];
      if (j != 0) {
        n n;
        if ((n = (n)((b.a != null) ? b.a.a(j) : null)) != null) {
          n.d();
          TextureRegion textureRegion = n.c(0.0F);
          TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(textureRegion);
          bool.setDrawable((Drawable)textureRegionDrawable);
          float f1 = textureRegion.getRegionWidth();
          float f2 = textureRegion.getRegionHeight();
          bool.setSize(f1, f2);
          bool.setScaling(Scaling.none);
          f1 = (f - f1) / 2.0F;
          f2 = (f - f2) / 2.0F;
          bool.setPosition(f1, f2);
        } else {
          bool.setDrawable(null);
        } 
      } else {
        bool.setDrawable(null);
      } 
    } 
  }
  
  public final void d(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, int paramInt6, int paramInt7, int paramInt8, int paramInt9, int paramInt10, int paramInt11) {
    b.a((cq)this.j, paramInt1, paramInt2, paramInt3, paramInt4, paramInt5, paramInt6, paramInt7, paramInt8, paramInt9, paramInt10, paramInt11);
    Texture texture;
    if ((texture = b.al) != null)
      this.d.setDrawable((Drawable)new TextureRegionDrawable(new TextureRegion(texture))); 
  }
  
  final void b(int paramInt, float paramFloat1, float paramFloat2) {
    // Byte code:
    //   0: aload_0
    //   1: invokevirtual q : ()Z
    //   4: ifeq -> 8
    //   7: return
    //   8: aload_0
    //   9: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   12: ifnull -> 19
    //   15: aload_0
    //   16: invokevirtual br : ()V
    //   19: iload_1
    //   20: bipush #101
    //   22: if_icmplt -> 35
    //   25: iload_1
    //   26: bipush #102
    //   28: if_icmpgt -> 35
    //   31: iconst_1
    //   32: goto -> 36
    //   35: iconst_0
    //   36: dup
    //   37: istore #4
    //   39: ifeq -> 49
    //   42: iload_1
    //   43: bipush #101
    //   45: isub
    //   46: goto -> 52
    //   49: iload_1
    //   50: iconst_1
    //   51: isub
    //   52: dup
    //   53: istore #5
    //   55: iflt -> 84
    //   58: iload #4
    //   60: ifeq -> 74
    //   63: iload #5
    //   65: aload_0
    //   66: getfield D : [I
    //   69: arraylength
    //   70: if_icmplt -> 85
    //   73: return
    //   74: iload #5
    //   76: aload_0
    //   77: getfield C : [I
    //   80: arraylength
    //   81: if_icmplt -> 85
    //   84: return
    //   85: iload #4
    //   87: ifeq -> 108
    //   90: aload_0
    //   91: getfield D : [I
    //   94: iload #5
    //   96: iaload
    //   97: ifne -> 104
    //   100: iconst_1
    //   101: goto -> 123
    //   104: iconst_0
    //   105: goto -> 123
    //   108: aload_0
    //   109: getfield C : [I
    //   112: iload #5
    //   114: iaload
    //   115: ifne -> 122
    //   118: iconst_1
    //   119: goto -> 123
    //   122: iconst_0
    //   123: ifeq -> 142
    //   126: aload_0
    //   127: invokevirtual p : ()Z
    //   130: ifne -> 134
    //   133: return
    //   134: aload_0
    //   135: iload_1
    //   136: fload_2
    //   137: fload_3
    //   138: invokevirtual c : (IFF)V
    //   141: return
    //   142: aload_0
    //   143: new com/badlogic/gdx/scenes/scene2d/Group
    //   146: dup
    //   147: invokespecial <init> : ()V
    //   150: putfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   153: aload_0
    //   154: iload_1
    //   155: putfield dn : I
    //   158: aload_0
    //   159: getfield j : Lcom/badlogic/gdx/scenes/scene2d/Stage;
    //   162: aload_0
    //   163: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   166: invokevirtual addActor : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   169: aload_0
    //   170: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   173: invokevirtual toFront : ()V
    //   176: aload_0
    //   177: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   180: getstatic com/badlogic/gdx/scenes/scene2d/Touchable.enabled : Lcom/badlogic/gdx/scenes/scene2d/Touchable;
    //   183: invokevirtual setTouchable : (Lcom/badlogic/gdx/scenes/scene2d/Touchable;)V
    //   186: aload_0
    //   187: iload_1
    //   188: istore #7
    //   190: dup
    //   191: astore #6
    //   193: getfield i : Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   196: ifnull -> 249
    //   199: aload #6
    //   201: getfield i : Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   204: dup
    //   205: astore #8
    //   207: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   210: aload #6
    //   212: getfield g : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   215: putfield up : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   218: aload #8
    //   220: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   223: aload #6
    //   225: getfield h : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   228: putfield down : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   231: aload #6
    //   233: aconst_null
    //   234: putfield i : Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   237: aload #6
    //   239: aconst_null
    //   240: putfield g : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   243: aload #6
    //   245: aconst_null
    //   246: putfield h : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   249: aload #6
    //   251: iload #7
    //   253: istore #8
    //   255: astore #7
    //   257: iload #8
    //   259: ifle -> 282
    //   262: iload #8
    //   264: bipush #9
    //   266: if_icmpgt -> 282
    //   269: aload #7
    //   271: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   274: iload #8
    //   276: iconst_1
    //   277: isub
    //   278: aaload
    //   279: goto -> 430
    //   282: iload #8
    //   284: bipush #10
    //   286: if_icmplt -> 378
    //   289: iload #8
    //   291: bipush #16
    //   293: if_icmpgt -> 378
    //   296: iload #8
    //   298: bipush #10
    //   300: isub
    //   301: dup
    //   302: istore #8
    //   304: iflt -> 374
    //   307: iload #8
    //   309: aload #7
    //   311: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/ui/Stack;
    //   314: arraylength
    //   315: if_icmpge -> 374
    //   318: aload #7
    //   320: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/ui/Stack;
    //   323: iload #8
    //   325: aaload
    //   326: invokevirtual getChildren : ()Lcom/badlogic/gdx/utils/SnapshotArray;
    //   329: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   332: astore #7
    //   334: aload #7
    //   336: invokeinterface hasNext : ()Z
    //   341: ifeq -> 374
    //   344: aload #7
    //   346: invokeinterface next : ()Ljava/lang/Object;
    //   351: checkcast com/badlogic/gdx/scenes/scene2d/Actor
    //   354: dup
    //   355: astore #8
    //   357: instanceof com/badlogic/gdx/scenes/scene2d/ui/ImageButton
    //   360: ifeq -> 371
    //   363: aload #8
    //   365: checkcast com/badlogic/gdx/scenes/scene2d/ui/ImageButton
    //   368: goto -> 430
    //   371: goto -> 334
    //   374: aconst_null
    //   375: goto -> 430
    //   378: iload #8
    //   380: bipush #101
    //   382: if_icmplt -> 429
    //   385: iload #8
    //   387: bipush #102
    //   389: if_icmpgt -> 429
    //   392: iload #8
    //   394: bipush #101
    //   396: isub
    //   397: dup
    //   398: istore #8
    //   400: iflt -> 425
    //   403: iload #8
    //   405: aload #7
    //   407: getfield b : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   410: arraylength
    //   411: if_icmpge -> 425
    //   414: aload #7
    //   416: getfield b : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   419: iload #8
    //   421: aaload
    //   422: goto -> 430
    //   425: aconst_null
    //   426: goto -> 430
    //   429: aconst_null
    //   430: dup
    //   431: astore #8
    //   433: ifnull -> 491
    //   436: aload #6
    //   438: aload #8
    //   440: putfield i : Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   443: aload #6
    //   445: aload #8
    //   447: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   450: getfield up : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   453: putfield g : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   456: aload #6
    //   458: aload #8
    //   460: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   463: getfield down : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   466: putfield h : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   469: aload #8
    //   471: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   474: getstatic a/b.e : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   477: putfield up : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   480: aload #8
    //   482: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   485: getstatic a/b.e : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   488: putfield down : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   491: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   494: invokeinterface getType : ()Lcom/badlogic/gdx/Application$ApplicationType;
    //   499: getstatic com/badlogic/gdx/Application$ApplicationType.Android : Lcom/badlogic/gdx/Application$ApplicationType;
    //   502: if_acmpne -> 509
    //   505: iconst_1
    //   506: goto -> 510
    //   509: iconst_0
    //   510: dup
    //   511: istore #6
    //   513: ifeq -> 526
    //   516: aload_0
    //   517: getfield j : La/cq;
    //   520: getfield am : F
    //   523: goto -> 527
    //   526: fconst_1
    //   527: fstore #7
    //   529: aload_0
    //   530: getfield j : La/cq;
    //   533: getfield bP : I
    //   536: i2f
    //   537: dup
    //   538: fstore #8
    //   540: fload #7
    //   542: fmul
    //   543: fstore #9
    //   545: aload_0
    //   546: getfield j : Lcom/badlogic/gdx/scenes/scene2d/Stage;
    //   549: invokevirtual getWidth : ()F
    //   552: fstore #10
    //   554: aload_0
    //   555: getfield j : Lcom/badlogic/gdx/scenes/scene2d/Stage;
    //   558: invokevirtual getHeight : ()F
    //   561: fstore #11
    //   563: getstatic a/b.aD : Lcom/badlogic/gdx/graphics/Texture;
    //   566: dup
    //   567: astore #12
    //   569: invokevirtual getWidth : ()I
    //   572: i2f
    //   573: fload #7
    //   575: fmul
    //   576: fstore #13
    //   578: aload #12
    //   580: invokevirtual getHeight : ()I
    //   583: i2f
    //   584: fload #7
    //   586: fmul
    //   587: fstore #14
    //   589: aload_0
    //   590: new com/badlogic/gdx/scenes/scene2d/ui/Image
    //   593: dup
    //   594: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   597: dup
    //   598: new com/badlogic/gdx/graphics/g2d/TextureRegion
    //   601: dup
    //   602: aload #12
    //   604: invokespecial <init> : (Lcom/badlogic/gdx/graphics/Texture;)V
    //   607: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   610: invokespecial <init> : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   613: putfield c : Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   616: aload_0
    //   617: getfield c : Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   620: fload #13
    //   622: fload #14
    //   624: invokevirtual setSize : (FF)V
    //   627: aload_0
    //   628: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   631: aload_0
    //   632: getfield c : Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   635: invokevirtual addActor : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   638: aload_0
    //   639: invokevirtual p : ()Z
    //   642: istore #12
    //   644: iload #4
    //   646: ifne -> 654
    //   649: iload #12
    //   651: ifne -> 658
    //   654: iconst_1
    //   655: goto -> 659
    //   658: iconst_0
    //   659: istore #12
    //   661: new java/util/ArrayList
    //   664: dup
    //   665: invokespecial <init> : ()V
    //   668: astore #15
    //   670: iload #12
    //   672: ifeq -> 685
    //   675: aload #15
    //   677: iconst_0
    //   678: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   681: invokevirtual add : (Ljava/lang/Object;)Z
    //   684: pop
    //   685: aload #15
    //   687: iconst_1
    //   688: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   691: invokevirtual add : (Ljava/lang/Object;)Z
    //   694: pop
    //   695: aload #15
    //   697: iconst_2
    //   698: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   701: invokevirtual add : (Ljava/lang/Object;)Z
    //   704: pop
    //   705: iconst_1
    //   706: aload #15
    //   708: invokevirtual size : ()I
    //   711: iadd
    //   712: i2f
    //   713: fload #9
    //   715: fmul
    //   716: fstore #12
    //   718: fload #9
    //   720: fstore #16
    //   722: fload_2
    //   723: fload #9
    //   725: fconst_2
    //   726: fdiv
    //   727: fadd
    //   728: fstore_2
    //   729: fload_3
    //   730: fload #9
    //   732: fadd
    //   733: fload #14
    //   735: fadd
    //   736: fconst_2
    //   737: fadd
    //   738: dup
    //   739: fstore #17
    //   741: fload #16
    //   743: fadd
    //   744: fload #11
    //   746: fcmpg
    //   747: ifgt -> 754
    //   750: iconst_1
    //   751: goto -> 755
    //   754: iconst_0
    //   755: dup
    //   756: istore #11
    //   758: ifeq -> 766
    //   761: fload #17
    //   763: goto -> 779
    //   766: fconst_2
    //   767: fload_3
    //   768: fload #14
    //   770: fsub
    //   771: fconst_2
    //   772: fsub
    //   773: fload #16
    //   775: fsub
    //   776: invokestatic max : (FF)F
    //   779: fstore_3
    //   780: fload_2
    //   781: fload #12
    //   783: fconst_2
    //   784: fdiv
    //   785: fsub
    //   786: fconst_0
    //   787: fload #10
    //   789: fload #12
    //   791: fsub
    //   792: invokestatic clamp : (FFF)F
    //   795: fstore #10
    //   797: aload_0
    //   798: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   801: fload #10
    //   803: invokestatic round : (F)I
    //   806: i2f
    //   807: fload_3
    //   808: invokestatic round : (F)I
    //   811: i2f
    //   812: invokevirtual setPosition : (FF)V
    //   815: fload #10
    //   817: fload #13
    //   819: fconst_2
    //   820: fdiv
    //   821: fadd
    //   822: fstore_3
    //   823: fload #10
    //   825: fload #12
    //   827: fadd
    //   828: fload #13
    //   830: fconst_2
    //   831: fdiv
    //   832: fsub
    //   833: fstore #12
    //   835: fload_2
    //   836: fload_3
    //   837: fload #12
    //   839: invokestatic clamp : (FFF)F
    //   842: fstore_2
    //   843: aload_0
    //   844: getfield c : Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   847: fload_2
    //   848: fload #10
    //   850: fsub
    //   851: fload #13
    //   853: fconst_2
    //   854: fdiv
    //   855: fsub
    //   856: iload #11
    //   858: ifeq -> 869
    //   861: fload #14
    //   863: fneg
    //   864: fconst_2
    //   865: fsub
    //   866: goto -> 873
    //   869: fload #16
    //   871: fconst_2
    //   872: fadd
    //   873: invokevirtual setPosition : (FF)V
    //   876: fload #9
    //   878: fload #8
    //   880: iload #6
    //   882: fload #7
    //   884: <illegal opcode> apply : (FFZF)Ljava/util/function/BiFunction;
    //   889: astore_2
    //   890: aconst_null
    //   891: astore_3
    //   892: iload #4
    //   894: ifeq -> 943
    //   897: getstatic a/b.a : La/l;
    //   900: ifnull -> 919
    //   903: getstatic a/b.a : La/l;
    //   906: aload_0
    //   907: getfield D : [I
    //   910: iload #5
    //   912: iaload
    //   913: invokevirtual a : (I)La/k;
    //   916: goto -> 920
    //   919: aconst_null
    //   920: dup
    //   921: astore #4
    //   923: ifnull -> 940
    //   926: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   929: dup
    //   930: aload #4
    //   932: fconst_0
    //   933: invokevirtual b : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   936: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   939: astore_3
    //   940: goto -> 986
    //   943: getstatic a/b.a : La/o;
    //   946: ifnull -> 965
    //   949: getstatic a/b.a : La/o;
    //   952: aload_0
    //   953: getfield C : [I
    //   956: iload #5
    //   958: iaload
    //   959: invokevirtual a : (I)La/n;
    //   962: goto -> 966
    //   965: aconst_null
    //   966: dup
    //   967: astore #4
    //   969: ifnull -> 986
    //   972: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   975: dup
    //   976: aload #4
    //   978: fconst_0
    //   979: invokevirtual c : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   982: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   985: astore_3
    //   986: new a/gl
    //   989: dup
    //   990: aload_0
    //   991: iload_1
    //   992: invokespecial <init> : (La/gb;I)V
    //   995: astore #4
    //   997: aload_2
    //   998: aload_3
    //   999: aload #4
    //   1001: invokeinterface apply : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   1006: checkcast com/badlogic/gdx/scenes/scene2d/Actor
    //   1009: dup
    //   1010: astore_3
    //   1011: fconst_0
    //   1012: fconst_0
    //   1013: invokevirtual setPosition : (FF)V
    //   1016: aload_0
    //   1017: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   1020: aload_3
    //   1021: invokevirtual addActor : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   1024: fconst_0
    //   1025: fload #9
    //   1027: fadd
    //   1028: fstore_3
    //   1029: aload #15
    //   1031: invokevirtual iterator : ()Ljava/util/Iterator;
    //   1034: astore #4
    //   1036: aload #4
    //   1038: invokeinterface hasNext : ()Z
    //   1043: ifeq -> 1157
    //   1046: aload #4
    //   1048: invokeinterface next : ()Ljava/lang/Object;
    //   1053: checkcast java/lang/Integer
    //   1056: invokevirtual intValue : ()I
    //   1059: dup
    //   1060: istore #5
    //   1062: ifne -> 1071
    //   1065: getstatic a/b.az : Lcom/badlogic/gdx/graphics/Texture;
    //   1068: goto -> 1086
    //   1071: iload #5
    //   1073: iconst_1
    //   1074: if_icmpne -> 1083
    //   1077: getstatic a/b.aA : Lcom/badlogic/gdx/graphics/Texture;
    //   1080: goto -> 1086
    //   1083: getstatic a/b.aB : Lcom/badlogic/gdx/graphics/Texture;
    //   1086: astore #6
    //   1088: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   1091: dup
    //   1092: new com/badlogic/gdx/graphics/g2d/TextureRegion
    //   1095: dup
    //   1096: aload #6
    //   1098: invokespecial <init> : (Lcom/badlogic/gdx/graphics/Texture;)V
    //   1101: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   1104: astore #6
    //   1106: new a/gm
    //   1109: dup
    //   1110: aload_0
    //   1111: iload #5
    //   1113: iload_1
    //   1114: invokespecial <init> : (La/gb;II)V
    //   1117: astore #5
    //   1119: aload_2
    //   1120: aload #6
    //   1122: aload #5
    //   1124: invokeinterface apply : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   1129: checkcast com/badlogic/gdx/scenes/scene2d/Actor
    //   1132: dup
    //   1133: astore #5
    //   1135: fload_3
    //   1136: fconst_0
    //   1137: invokevirtual setPosition : (FF)V
    //   1140: aload_0
    //   1141: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   1144: aload #5
    //   1146: invokevirtual addActor : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   1149: fload_3
    //   1150: fload #9
    //   1152: fadd
    //   1153: fstore_3
    //   1154: goto -> 1036
    //   1157: aload_0
    //   1158: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   1161: invokevirtual getColor : ()Lcom/badlogic/gdx/graphics/Color;
    //   1164: fconst_0
    //   1165: putfield a : F
    //   1168: aload_0
    //   1169: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   1172: ldc 0.2
    //   1174: invokestatic fadeIn : (F)Lcom/badlogic/gdx/scenes/scene2d/actions/AlphaAction;
    //   1177: invokevirtual addAction : (Lcom/badlogic/gdx/scenes/scene2d/Action;)V
    //   1180: return
  }
  
  final void c(int paramInt, float paramFloat1, float paramFloat2) {
    if (this.c != null)
      br(); 
    this.c = (ImageButton[])new Group();
    this.dn = paramInt;
    boolean bool;
    float f1 = (bool = (Gdx.app.getType() == Application.ApplicationType.Android) ? true : false) ? ((cq)this.j).am : 1.0F;
    float f2 = ((cq)this.j).bP * f1;
    Texture texture;
    float f4 = (texture = b.aD).getWidth() * f1;
    f1 = texture.getHeight() * f1;
    this.c = (ImageButton[])new Image((Drawable)new TextureRegionDrawable(new TextureRegion(texture)));
    this.c.setSize(f4, f1);
    float f3 = 1.0F * f2;
    float f5 = f2;
    float f6 = this.j.getWidth();
    float f7 = this.j.getHeight();
    float f8 = paramFloat1;
    float f9 = paramFloat2 + f2 + f1 + 2.0F;
    if (f8 + f3 > f6)
      f8 = f6 - f3; 
    if (f8 < 0.0F)
      f8 = 0.0F; 
    if ((f6 = f9) + f5 > f7 && (f6 = paramFloat2 - f1 - f5 - 2.0F) < 0.0F)
      f6 = 2.0F; 
    this.c.setPosition(Math.round(f8), Math.round(f6));
    paramFloat2 = paramFloat1 + f2 / 2.0F;
    paramFloat1 = f8 + f4 / 2.0F;
    f3 = f8 + f3 - f4 / 2.0F;
    paramFloat1 = MathUtils.clamp(paramFloat2, paramFloat1, f3) - f8 - f4 / 2.0F;
    if (Math.abs(f9 - f6) < 1.0F) {
      paramFloat2 = -f1 - 2.0F;
    } else {
      paramFloat2 = f5 + 2.0F;
    } 
    this.c.setPosition(paramFloat1, paramFloat2);
    this.c.addActor((Actor)this.c);
    NinePatchDrawable ninePatchDrawable = new NinePatchDrawable(b.w);
    ImageButton.ImageButtonStyle imageButtonStyle;
    (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)ninePatchDrawable;
    imageButtonStyle.down = (Drawable)ninePatchDrawable;
    imageButtonStyle.imageUp = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aC));
    imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(new TextureRegion(b.aC));
    ImageButton imageButton;
    (imageButton = new ImageButton(imageButtonStyle)).setSize(f2, f2);
    if (bool) {
      imageButton.getImageCell().size(f2, f2);
      imageButton.getImage().setScaling(Scaling.fit);
    } 
    imageButton.addListener((EventListener)new go(this, paramInt));
    imageButton.setPosition(0.0F, 0.0F);
    this.c.addActor((Actor)imageButton);
    (this.c.getColor()).a = 0.0F;
    this.j.addActor((Actor)this.c);
    this.c.toFront();
    this.c.addAction((Action)Actions.fadeIn(0.2F));
    this.c.setTouchable(Touchable.enabled);
  }
  
  final void br() {
    if (this.c == null)
      return; 
    ImageButton[] arrayOfImageButton = this.c;
    this.c = null;
    this.dn = 0;
    arrayOfImageButton.addAction((Action)Actions.sequence((Action)Actions.fadeOut(0.2F), (Action)Actions.run(new gp(this, (Group)arrayOfImageButton))));
    if (this.i != null) {
      TextureRegionDrawable textureRegionDrawable;
      ((textureRegionDrawable = this.i).getStyle()).up = (Drawable)this.g;
      (textureRegionDrawable.getStyle()).down = (Drawable)this.h;
      this.i = null;
      this.g = null;
      this.h = null;
    } 
    if (this.c != null)
      this.c = null; 
  }
  
  public final void aa(int paramInt) {
    // Byte code:
    //   0: iload_1
    //   1: ifle -> 10
    //   4: iload_1
    //   5: bipush #16
    //   7: if_icmple -> 11
    //   10: return
    //   11: iload_1
    //   12: bipush #9
    //   14: if_icmpgt -> 66
    //   17: iload_1
    //   18: iconst_1
    //   19: isub
    //   20: istore_2
    //   21: aload_0
    //   22: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   25: iload_2
    //   26: aaload
    //   27: dup
    //   28: astore_1
    //   29: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   32: dup
    //   33: astore_3
    //   34: aload_0
    //   35: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   38: iload_2
    //   39: aaload
    //   40: putfield imageUp : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   43: aload_3
    //   44: aload_0
    //   45: getfield b : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   48: iload_2
    //   49: aaload
    //   50: putfield imageDown : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   53: aload_1
    //   54: aload_3
    //   55: invokevirtual setStyle : (Lcom/badlogic/gdx/scenes/scene2d/ui/Button$ButtonStyle;)V
    //   58: aload_0
    //   59: getfield C : [I
    //   62: iload_2
    //   63: iconst_0
    //   64: iastore
    //   65: return
    //   66: iload_1
    //   67: bipush #10
    //   69: isub
    //   70: dup
    //   71: istore_2
    //   72: iflt -> 81
    //   75: iload_2
    //   76: bipush #6
    //   78: if_icmple -> 82
    //   81: return
    //   82: aload_0
    //   83: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   86: iload_2
    //   87: aaload
    //   88: aconst_null
    //   89: invokevirtual setDrawable : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   92: aload_0
    //   93: getfield C : [I
    //   96: iload_1
    //   97: iconst_1
    //   98: isub
    //   99: iconst_0
    //   100: iastore
    //   101: return
  }
  
  public final void r(int paramInt1, int paramInt2) {
    // Byte code:
    //   0: iload_1
    //   1: ifle -> 10
    //   4: iload_1
    //   5: bipush #16
    //   7: if_icmple -> 11
    //   10: return
    //   11: iload_2
    //   12: ifgt -> 21
    //   15: aload_0
    //   16: iload_1
    //   17: invokevirtual aa : (I)V
    //   20: return
    //   21: iload_1
    //   22: bipush #9
    //   24: if_icmpgt -> 147
    //   27: iload_1
    //   28: iconst_1
    //   29: isub
    //   30: istore_3
    //   31: aload_0
    //   32: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton;
    //   35: iload_3
    //   36: aaload
    //   37: dup
    //   38: astore #4
    //   40: invokevirtual getStyle : ()Lcom/badlogic/gdx/scenes/scene2d/ui/ImageButton$ImageButtonStyle;
    //   43: astore #5
    //   45: getstatic a/b.a : La/o;
    //   48: ifnull -> 61
    //   51: getstatic a/b.a : La/o;
    //   54: iload_2
    //   55: invokevirtual a : (I)La/n;
    //   58: goto -> 62
    //   61: aconst_null
    //   62: dup
    //   63: astore #6
    //   65: ifnull -> 110
    //   68: aload #6
    //   70: invokevirtual d : ()Z
    //   73: pop
    //   74: aload #6
    //   76: fconst_0
    //   77: invokevirtual c : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   80: astore #7
    //   82: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   85: dup
    //   86: aload #7
    //   88: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   91: astore #7
    //   93: aload #5
    //   95: aload #7
    //   97: putfield imageUp : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   100: aload #5
    //   102: aload #7
    //   104: putfield imageDown : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   107: goto -> 132
    //   110: aload #5
    //   112: aload_0
    //   113: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   116: iload_3
    //   117: aaload
    //   118: putfield imageUp : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   121: aload #5
    //   123: aload_0
    //   124: getfield b : [Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   127: iload_3
    //   128: aaload
    //   129: putfield imageDown : Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;
    //   132: aload #4
    //   134: aload #5
    //   136: invokevirtual setStyle : (Lcom/badlogic/gdx/scenes/scene2d/ui/Button$ButtonStyle;)V
    //   139: aload_0
    //   140: getfield C : [I
    //   143: iload_3
    //   144: iload_2
    //   145: iastore
    //   146: return
    //   147: iload_1
    //   148: bipush #10
    //   150: isub
    //   151: dup
    //   152: istore_3
    //   153: iflt -> 162
    //   156: iload_3
    //   157: bipush #6
    //   159: if_icmple -> 163
    //   162: return
    //   163: aload_0
    //   164: getfield a : [Lcom/badlogic/gdx/scenes/scene2d/ui/Image;
    //   167: iload_3
    //   168: aaload
    //   169: astore #4
    //   171: getstatic a/b.a : La/o;
    //   174: ifnull -> 187
    //   177: getstatic a/b.a : La/o;
    //   180: iload_2
    //   181: invokevirtual a : (I)La/n;
    //   184: goto -> 188
    //   187: aconst_null
    //   188: dup
    //   189: astore #5
    //   191: ifnull -> 300
    //   194: aload #5
    //   196: invokevirtual d : ()Z
    //   199: pop
    //   200: aload #5
    //   202: fconst_0
    //   203: invokevirtual c : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   206: astore #6
    //   208: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   211: dup
    //   212: aload #6
    //   214: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   217: astore #7
    //   219: aload #4
    //   221: aload #7
    //   223: invokevirtual setDrawable : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   226: aload #6
    //   228: invokevirtual getRegionWidth : ()I
    //   231: i2f
    //   232: fstore #7
    //   234: aload #6
    //   236: invokevirtual getRegionHeight : ()I
    //   239: i2f
    //   240: fstore_3
    //   241: aload #4
    //   243: fload #7
    //   245: fload_3
    //   246: invokevirtual setSize : (FF)V
    //   249: aload #4
    //   251: getstatic com/badlogic/gdx/utils/Scaling.none : Lcom/badlogic/gdx/utils/Scaling;
    //   254: invokevirtual setScaling : (Lcom/badlogic/gdx/utils/Scaling;)V
    //   257: aload_0
    //   258: getfield j : La/cq;
    //   261: getfield bP : I
    //   264: i2f
    //   265: dup
    //   266: fstore #5
    //   268: fload #7
    //   270: fsub
    //   271: fconst_2
    //   272: fdiv
    //   273: fstore #6
    //   275: fload #5
    //   277: fload_3
    //   278: fsub
    //   279: fconst_2
    //   280: fdiv
    //   281: fstore_3
    //   282: aload #4
    //   284: fload #6
    //   286: fload_3
    //   287: invokevirtual setPosition : (FF)V
    //   290: aload_0
    //   291: getfield C : [I
    //   294: iload_1
    //   295: iconst_1
    //   296: isub
    //   297: iload_2
    //   298: iastore
    //   299: return
    //   300: aload #4
    //   302: aconst_null
    //   303: invokevirtual setDrawable : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   306: aload_0
    //   307: getfield C : [I
    //   310: iload_1
    //   311: iconst_1
    //   312: isub
    //   313: iconst_0
    //   314: iastore
    //   315: return
  }
  
  public final void ab(int paramInt) {
    if (q() || this.aW)
      return; 
    if (this.c != null) {
      br();
      return;
    } 
    int i;
    if ((i = paramInt - 1) < 0 || i >= 9)
      return; 
    if (this.C[i] == null) {
      if (p())
        try {
          this.m.z(paramInt);
          return;
        } catch (Exception exception) {
          return;
        }  
    } else {
      try {
        this.m.A(paramInt);
        return;
      } catch (Exception exception) {}
    } 
  }
  
  final boolean p() {
    int i = ((cq)this.j).aD;
    int j = ((cq)this.j).aE;
    int k = ((cq)this.j).aF;
    cg cg;
    return ((cg = this.c.a(i, j, k)) != null && cg.bs > 0);
  }
  
  public void a(long paramLong) {
    this.i.setText(lj.a(paramLong));
    d(this.j.getWidth(), this.j.getHeight());
  }
  
  public void b(long paramLong) {
    this.j.setText(lj.a(paramLong));
    d(this.j.getWidth(), this.j.getHeight());
  }
  
  public void resize(int paramInt1, int paramInt2) {
    a(paramInt1, paramInt2);
    d(paramInt1, paramInt2);
  }
  
  final void d(float paramFloat1, float paramFloat2) {
    if (this.o == null)
      return; 
    this.o.pack();
    if (this.f != null) {
      paramFloat2 = this.f.getY() + this.f.getHeight() - this.o.getHeight() - 2.0F;
    } else {
      paramFloat2 = paramFloat2 - this.o.getHeight() - 10.0F;
    } 
    float f = ((fj.au > 0.0F) ? fj.au : (paramFloat1 / 2.0F)) - this.o.getWidth() / 2.0F;
    f = Math.max(10.0F, Math.min(f, paramFloat1 - 10.0F - this.o.getWidth()));
    this.o.setPosition(Math.round(f), Math.round(paramFloat2));
    if (this.f != null && this.o.getParent() == this.f.getParent())
      this.o.setZIndex(this.f.getZIndex() + 1); 
  }
  
  public void b(int paramInt, float paramFloat) {
    az az;
    if ((az = (az)this.z.get(Integer.valueOf(paramInt))) == null)
      return; 
    this.k.setText(az.s);
    int i = MathUtils.round(105.0F * MathUtils.clamp(paramFloat, 0.0F, 1.0F));
    TextureRegion textureRegion = new TextureRegion((Texture)b.v, 0, 0, i, 14);
    this.o.setDrawable((Drawable)new TextureRegionDrawable(textureRegion));
    this.o.setSize(i, 14.0F);
    this.e.clearActions();
    this.e.setVisible(true);
    this.e.addAction((Action)Actions.sequence((Action)Actions.delay(5.0F), (Action)Actions.run(() -> this.e.setVisible(false))));
  }
  
  public final void ac(int paramInt) {
    int i = lj.h(paramInt);
    lj.a(paramInt, (cq)this.j);
    if (i <= 0)
      return; 
    k k;
    if ((k = (k)((b.a != null) ? b.a.a(i) : null)) == null)
      return; 
    k.c();
    TextureRegion textureRegion = k.b(0.0F);
    TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(textureRegion);
    ImageButton.ImageButtonStyle imageButtonStyle;
    (imageButtonStyle = this.p.getStyle()).imageUp = (Drawable)textureRegionDrawable;
    imageButtonStyle.imageDown = (Drawable)textureRegionDrawable;
    this.p.setStyle((Button.ButtonStyle)imageButtonStyle);
    this.bB = textureRegion.getRegionWidth();
    this.bC = textureRegion.getRegionHeight();
    this.p.setSize(((cq)this.j).bP, ((cq)this.j).bP);
    a(this.j.getWidth(), this.j.getHeight());
  }
  
  public final void c(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, long paramLong1, long paramLong2, long paramLong3, int paramInt6, int paramInt7) {
    this.do = paramInt1;
    this.cG = paramInt2;
    this.dp = paramInt3;
    this.cH = paramInt4;
    float f2 = MathUtils.clamp(paramInt1 / paramInt2, 0.0F, 1.0F);
    int j = Math.round(b.t.getWidth() * f2);
    TextureRegion textureRegion2 = new TextureRegion((Texture)b.t, 0, 0, j, b.t.getHeight());
    this.h.setDrawable((Drawable)new TextureRegionDrawable(textureRegion2));
    this.h.setSize(j, b.t.getHeight());
    float f1 = MathUtils.clamp(paramInt3 / paramInt4, 0.0F, 1.0F);
    int i = Math.round(((paramInt6 > 0) ? b.s.getWidth() : b.u.getWidth()) * f1);
    paramInt3 = b.u.getHeight();
    NinePatch ninePatch = (paramInt6 > 0) ? b.s : b.u;
    TextureRegion textureRegion1 = new TextureRegion((Texture)ninePatch, 0, 0, i, paramInt3);
    this.i.setDrawable((Drawable)new TextureRegionDrawable(textureRegion1));
    this.i.setSize(i, paramInt3);
    this.e.setText("" + paramInt1 + "/" + paramInt1);
    this.f.setText("" + this.dp + "/" + this.dp);
    ad(paramInt5);
    c(paramLong1, paramLong2);
    a(paramLong3);
    Z(paramInt7);
  }
  
  public final void ad(int paramInt) {
    this.h.setText(Integer.toString(paramInt));
  }
  
  public final void ae(int paramInt) {
    float f = MathUtils.clamp(paramInt / this.cG, 0.0F, 1.0F);
    int i = Math.round(105.0F * f);
    this.h.clearActions();
    this.h.addAction((Action)Actions.sizeTo(i, 14.0F, 0.1F));
    this.do = paramInt;
    this.e.setText("" + paramInt + "/" + paramInt);
  }
  
  public final void af(int paramInt) {
    this.dp = paramInt;
    float f = MathUtils.clamp(paramInt / this.cH, 0.0F, 1.0F);
    int i = Math.round(105.0F * f);
    this.i.clearActions();
    this.i.setSize(i, 14.0F);
    this.f.setText("" + this.dp + "/" + this.dp);
  }
  
  public final void ag(int paramInt) {
    this.aM = (paramInt > 0);
    NinePatch ninePatch = this.aM ? b.s : b.u;
    this.i.setDrawable((Drawable)new TextureRegionDrawable(new TextureRegion((Texture)ninePatch)));
    float f = MathUtils.clamp(this.dp / this.cH, 0.0F, 1.0F);
    int i = Math.round(105.0F * f);
    this.i.setSize(i, 14.0F);
  }
  
  private static int a(long paramLong) {
    int i = 1;
    for (int j = Math.max(1, 9999); i < j; j = k - 1) {
      int k;
      long l = lk.b(k = i + j + 1 >>> 1);
      if (paramLong >= l) {
        i = k;
        continue;
      } 
    } 
    return i;
  }
  
  public final void c(long paramLong1, long paramLong2) {
    int j;
    long l1 = lk.b(j = a(paramLong1));
    long l2;
    if ((l2 = paramLong2) <= l1)
      l2 = lk.b(j + 1); 
    long l3 = Math.max(0L, paramLong1 - l1);
    long l4;
    float f1 = ((l4 = l2 - l1) <= 0L) ? 1.0F : MathUtils.clamp((float)l3 / (float)l4, 0.0F, 1.0F);
    int i = Math.round(105.0F * f1);
    float f2 = this.j.getWidth();
    this.j.clearActions();
    if (i > f2) {
      this.j.addAction((Action)Actions.sizeTo(i, 6.0F, 0.1F));
      return;
    } 
    if (i < f2) {
      this.j.setSize(i, 6.0F);
      return;
    } 
    this.j.setHeight(6.0F);
  }
  
  private static TextureRegionDrawable a(float paramFloat1, float paramFloat2, float paramFloat3, float paramFloat4) {
    Pixmap pixmap;
    (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(paramFloat1, paramFloat2, paramFloat3, paramFloat4);
    pixmap.fill();
    TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(new TextureRegion(new Texture(pixmap)));
    pixmap.dispose();
    return textureRegionDrawable;
  }
  
  private TextureRegionDrawable a(Texture paramTexture) {
    if (paramTexture != null)
      return new TextureRegionDrawable(new TextureRegion(paramTexture)); 
    if (this.f == null)
      this.f = a(0.0F, 0.0F, 0.0F, 0.0F); 
    return this.f;
  }
  
  private static ImageButton a(Drawable paramDrawable1, Drawable paramDrawable2, Drawable paramDrawable3) {
    ImageButton.ImageButtonStyle imageButtonStyle;
    (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = paramDrawable1;
    imageButtonStyle.down = paramDrawable2;
    imageButtonStyle.imageUp = paramDrawable3;
    imageButtonStyle.imageDown = paramDrawable3;
    return new ImageButton(imageButtonStyle);
  }
  
  public final boolean q() {
    return (this.aZ && this.j != null && this.j.isVisible());
  }
  
  final void bs() {
    if (!q())
      return; 
    if (this.v != null && this.dC > 0) {
      this.v.clearActions();
      (this.v.getStyle()).up = (Drawable)this.j;
      (this.v.getStyle()).imageUp = (Drawable)this.i;
      this.v.addAction((Action)Actions.sequence((Action)Actions.delay(0.15F), (Action)Actions.run(() -> {
                (this.v.getStyle()).up = (Drawable)this.i;
                (this.v.getStyle()).imageUp = (Drawable)this.h;
              })));
    } 
    if (this.aY) {
      System.out.println("[DEPOT] Prev ignorado: aguardando p);
      return;
    } 
    if (this.dC <= 0) {
      System.out.println("[DEPOT] Jestna primeira p);
      return;
    } 
    int i = this.dC - 1;
    this.aY = true;
    try {
      al.a(3);
      this.m.B(i);
      return;
    } catch (Exception exception) {
      this.aY = false;
      Gdx.app.error("Depot", "RequestSwitchDepotPage (prev)", exception);
      return;
    } 
  }
  
  final void bt() {
    if (!q())
      return; 
    if (this.w != null) {
      this.w.clearActions();
      (this.w.getStyle()).up = (Drawable)this.j;
      (this.w.getStyle()).imageUp = (Drawable)this.k;
      this.w.addAction((Action)Actions.sequence((Action)Actions.delay(0.15F), (Action)Actions.run(() -> {
                (this.w.getStyle()).up = (Drawable)this.i;
                (this.w.getStyle()).imageUp = (Drawable)this.j;
              })));
    } 
    if (this.aY) {
      System.out.println("[DEPOT] Next ignorado: aguardando p);
      return;
    } 
    int i = this.dC + 1;
    this.aY = true;
    try {
      al.a(3);
      this.m.B(i);
      return;
    } catch (Exception exception) {
      this.aY = false;
      Gdx.app.error("Depot", "RequestSwitchDepotPage (next)", exception);
      return;
    } 
  }
  
  final void bu() {
    if (this.j != null)
      this.j.setVisible(false); 
    this.aZ = false;
    if (this.c != null) {
      this.c.setVisible(false);
      this.c.setBounds(0.0F, 0.0F, this.j.getWidth(), this.j.getHeight());
    } 
    a(Touchable.enabled);
    if (this.j != null && this.j.getScrollFocus() == this.a)
      this.j.setScrollFocus(null); 
    ((br)this.m).G = true;
    try {
      al.a(3);
      if (this.m != null)
        this.m.L(); 
      return;
    } catch (Exception exception) {
      Gdx.app.error("Depot", "RequestLeaveShop", exception);
      return;
    } 
  }
  
  final int m() {
    for (byte b = 1; b <= 9; b++) {
      if (this.C[b - 1] == null)
        return b; 
    } 
    return 0;
  }
  
  private void bv() {
    for (byte b = 0; b < this.c.length; b++) {
      ImageButton imageButton;
      if ((imageButton = this.c[b]) != null) {
        int i = this.F[b];
        ImageButton.ImageButtonStyle imageButtonStyle = imageButton.getStyle();
        if (i != 0) {
          n n;
          if ((n = (n)((b.a != null) ? b.a.a(i) : null)) != null) {
            TextureRegion textureRegion = n.c(0.0F);
            TextureRegionDrawable textureRegionDrawable = new TextureRegionDrawable(textureRegion);
            imageButtonStyle.imageUp = (Drawable)textureRegionDrawable;
            imageButtonStyle.imageDown = (Drawable)textureRegionDrawable;
          } else {
            imageButtonStyle.imageUp = null;
            imageButtonStyle.imageDown = null;
          } 
        } else {
          imageButtonStyle.imageUp = null;
          imageButtonStyle.imageDown = null;
        } 
        imageButton.setStyle((Button.ButtonStyle)imageButtonStyle);
      } 
    } 
  }
  
  public final void b(String paramString, int paramInt1, int paramInt2, int paramInt3, int[] paramArrayOfint) {
    if (this.aW && !this.aX && !this.aZ)
      return; 
    boolean bool = (Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS) ? true : false;
    int i = (Gdx.graphics.getHeight() > Gdx.graphics.getWidth()) ? 1 : 0;
    this.aL = (bool || i);
    this.aX = false;
    gb gb1;
    if ((gb1 = this).j == null) {
      if (gb1.f == null)
        gb1.f = a(0.0F, 0.0F, 0.0F, 0.0F); 
      TextureRegionDrawable textureRegionDrawable1 = a(0.18F, 0.18F, 0.18F, 0.95F);
      BitmapFont bitmapFont;
      gb1.i = ((bitmapFont = b.d) != null) ? (TextureRegionDrawable)bitmapFont : textureRegionDrawable1;
      textureRegionDrawable1 = gb1.i;
      gb1.j = ((bitmapFont = b.e) != null) ? (TextureRegionDrawable)bitmapFont : textureRegionDrawable1;
      gb1.g = gb1.a((Texture)b.k);
      TextureRegion textureRegion1 = new TextureRegion((Texture)b.c);
      TextureRegion textureRegion2 = new TextureRegion((Texture)b.d);
      gb1.h = new TextureRegionDrawable(textureRegion1);
      gb1.i = new TextureRegionDrawable(textureRegion2);
      TextureRegion textureRegion3 = new TextureRegion((Texture)b.c);
      TextureRegion textureRegion4 = new TextureRegion((Texture)b.d);
      textureRegion3.flip(true, false);
      textureRegion4.flip(true, false);
      gb1.j = new TextureRegionDrawable(textureRegion3);
      gb1.k = new TextureRegionDrawable(textureRegion4);
      gb1.j = (TextureRegionDrawable)new Group();
      gb1.j.setVisible(false);
      gb1.j.setTouchable(Touchable.enabled);
      gb1.j.addActor((Actor)gb1.j);
      gb1.e = new NinePatchDrawable((NinePatch)b.d);
      gb1.f = (TextureRegionDrawable)new NinePatchDrawable((NinePatch)b.f);
      gb1.C = new Image((Drawable)gb1.e);
      gb1.j.addActor((Actor)gb1.C);
      gb1.D = new Image((Drawable)gb1.f);
      gb1.j.addActor((Actor)gb1.D);
      ImageButton.ImageButtonStyle imageButtonStyle1;
      (imageButtonStyle1 = new ImageButton.ImageButtonStyle()).up = (Drawable)gb1.i;
      imageButtonStyle1.down = (Drawable)gb1.j;
      imageButtonStyle1.imageUp = (Drawable)gb1.h;
      imageButtonStyle1.imageDown = (Drawable)gb1.i;
      gb1.v = new ImageButton(imageButtonStyle1);
      gb1.v.getImage().setScaling(Scaling.fit);
      gb1.v.getImageCell().pad(0.0F).expand().fill();
      gb1.v.addListener((EventListener)new gt(gb1));
      gb1.j.addActor((Actor)gb1.v);
      gb1.o = new Label("", new Label.LabelStyle(b.a((String)null), Color.WHITE));
      gb1.o.setAlignment(1);
      gb1.o.setEllipsis(true);
      gb1.j.addActor((Actor)gb1.o);
      ImageButton.ImageButtonStyle imageButtonStyle2;
      (imageButtonStyle2 = new ImageButton.ImageButtonStyle()).up = (Drawable)gb1.i;
      imageButtonStyle2.down = (Drawable)gb1.j;
      imageButtonStyle2.imageUp = (Drawable)gb1.j;
      imageButtonStyle2.imageDown = (Drawable)gb1.k;
      gb1.w = new ImageButton(imageButtonStyle2);
      gb1.w.getImage().setScaling(Scaling.fit);
      gb1.w.getImageCell().pad(0.0F).expand().fill();
      gb1.w.addListener((EventListener)new gu(gb1));
      gb1.j.addActor((Actor)gb1.w);
      TextureRegionDrawable textureRegionDrawable2 = gb1.a((Texture)b.f);
      TextureRegionDrawable textureRegionDrawable3 = gb1.a((Texture)b.g);
      ImageButton.ImageButtonStyle imageButtonStyle3;
      (imageButtonStyle3 = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)textureRegionDrawable2;
      imageButtonStyle3.imageDown = (Drawable)textureRegionDrawable3;
      gb1.u = new ImageButton(imageButtonStyle3);
      gb1.u.getImage().setScaling(Scaling.fit);
      gb1.u.getImageCell().pad(0.0F).expand().fill();
      gb1.u.addListener((EventListener)new gv(gb1));
      gb1.j.addActor((Actor)gb1.u);
      gb1.n = (Label)new Table();
      gb1.n.top().left();
      gb1.n.defaults().pad(0.0F).space(0.0F);
      gb gb2;
      if ((gb2 = gb1).b == null) {
        gb2.b = (Image[])new ScrollPane.ScrollPaneStyle();
        ((ScrollPane.ScrollPaneStyle)gb2.b).vScroll = (Drawable)new NinePatchDrawable((NinePatch)b.b);
        ((ScrollPane.ScrollPaneStyle)gb2.b).vScrollKnob = (Drawable)new NinePatchDrawable((NinePatch)b.c);
        float f = gb2.aL ? 45.0F : 20.0F;
        if (((ScrollPane.ScrollPaneStyle)gb2.b).vScroll instanceof BaseDrawable)
          ((BaseDrawable)((ScrollPane.ScrollPaneStyle)gb2.b).vScroll).setMinWidth(f); 
        if (((ScrollPane.ScrollPaneStyle)gb2.b).vScrollKnob instanceof BaseDrawable)
          ((BaseDrawable)((ScrollPane.ScrollPaneStyle)gb2.b).vScrollKnob).setMinWidth(f); 
      } 
      gb1.a = (boolean[])new ScrollPane((Actor)gb1.n, (ScrollPane.ScrollPaneStyle)gb1.b);
      gb1.a.setTouchable(Touchable.enabled);
      gb1.a.setScrollingDisabled(true, false);
      gb1.a.setFadeScrollBars(false);
      gb1.a.setScrollbarsOnTop(false);
      gb1.a.setForceScroll(false, false);
      gb1.a.setFlickScroll(true);
      gb1.a.setFlickScrollTapSquareSize(20.0F);
      gb1.a.setCancelTouchFocus(true);
      gb1.a.setOverscroll(false, false);
      gb1.j.addActor((Actor)gb1.a);
      gb1.c = new ImageButton[0];
      gb1.F = new int[0];
      gb1.b = new Image[0];
      gb1.a = new boolean[0];
    } 
    this.aY = false;
    this.ak = (paramString != null) ? paramString : "";
    this.dC = paramInt1;
    this.dD = Math.max(0, paramInt2);
    this.dE = Math.max(0, paramInt3);
    if (this.F == null || this.F.length != this.dE || this.dm != 7) {
      this.dm = 7;
      i = this.dE;
      (gb1 = this).n.clearChildren();
      gb1.n.align(10);
      gb1.c = new ImageButton[i];
      gb1.F = new int[i];
      gb1.b = new Image[i];
      gb1.a = new boolean[i];
      int j = gb1.dm;
      int k = (int)Math.ceil((i / j));
      float f1 = ((cq)gb1.j).bP;
      float f2 = gb1.aL ? ((cq)gb1.j).am : 1.0F;
      float f3 = f1 * f2;
      byte b1 = 0;
      for (byte b2 = 0; b2 < k; b2++) {
        for (byte b = 0; b < j && b1 < i; b++) {
          ImageButton.ImageButtonStyle imageButtonStyle;
          (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)gb1.i;
          imageButtonStyle.down = (Drawable)gb1.j;
          ImageButton imageButton;
          (imageButton = new ImageButton(imageButtonStyle)).getImage().setScaling(Scaling.none);
          imageButton.getImageCell().expand().center();
          byte b3 = b1;
          Image image;
          (image = new Image()).setTouchable(Touchable.disabled);
          image.setVisible(false);
          image.setScaling(Scaling.stretch);
          gb1.b[b3] = image;
          Stack stack;
          (stack = new Stack()).add((Actor)imageButton);
          stack.add((Actor)image);
          if (f2 != 1.0F) {
            stack.setTransform(true);
            stack.setScale(f2);
            stack.setOrigin(12);
          } 
          Container container;
          (container = new Container((Actor)stack)).align(12);
          container.width(f1).height(f1);
          imageButton.addListener((EventListener)new gw(gb1, b3));
          gb1.c[b1] = imageButton;
          gb1.n.add((Actor)container).size(f3, f3);
          b1++;
        } 
        gb1.n.row();
      } 
      Actor actor;
      (actor = new Actor()).setVisible(false);
      gb1.n.add(actor).colspan(j).height(f3).width(1.0F).row();
      gb1.a.setScrollX(0.0F);
      gb1.a.updateVisualScroll();
      gb1.n.invalidateHierarchy();
      gb1.n.layout();
      gb1.bx();
    } 
    if (paramArrayOfint != null && paramArrayOfint.length == this.dE)
      System.arraycopy(paramArrayOfint, 0, this.F, 0, this.dE); 
    bv();
    bx();
    if ((gb1 = this).a != null) {
      i = gb1.a.length;
      int j = Math.max(0, Math.min(gb1.dD, i));
      for (byte b = 0; b < i; b++) {
        boolean bool1 = (b >= j) ? true : false;
        boolean bool2 = bool1;
        byte b1 = b;
        gb gb2;
        if ((gb2 = gb1).a != null && b1 >= 0 && b1 < gb2.a.length) {
          gb2.a[b1] = bool2;
          ImageButton imageButton = gb2.c[b1];
          Image image;
          if ((image = gb2.b[b1]) != null)
            if (bool2) {
              image.setDrawable((gb2.g != null) ? (Drawable)gb2.g : (Drawable)a(0.0F, 0.0F, 0.0F, 0.45F));
              image.setVisible(true);
              image.setColor(1.0F, 1.0F, 1.0F, 1.0F);
              image.toFront();
            } else {
              image.setVisible(false);
              image.setDrawable(null);
            }  
          if (imageButton != null)
            imageButton.setDisabled(bool2); 
        } 
      } 
    } 
    if (this.dC >= 100) {
      paramString = this.ak;
    } else {
      paramString = this.ak + " (" + this.ak + ")";
    } 
    b.a(this.o, paramString);
    this.o.setFontScale(this.aL ? 2.0F : 1.0F);
    bm();
    bz();
    br();
    this.aZ = true;
    if (this.c != null) {
      this.c.setVisible(true);
      float f = (this.b != null) ? this.b.getX() : this.j.getWidth();
      this.c.setBounds(0.0F, 0.0F, f, this.j.getHeight());
      this.c.toFront();
    } 
    a(Touchable.disabled);
    this.j.setVisible(true);
    this.j.toFront();
    a(this.j.getWidth(), this.j.getHeight());
    if (this.j != null)
      this.j.setScrollFocus((Actor)this.a); 
  }
  
  private void a(Touchable paramTouchable) {
    if (this.m != null)
      this.m.setTouchable(paramTouchable); 
    if (this.n != null)
      this.n.setTouchable(paramTouchable); 
    if (this.o != null)
      this.o.setTouchable(paramTouchable); 
    if (this.c != null)
      this.c.setTouchable(paramTouchable); 
    if (this.p != null)
      this.p.setTouchable(paramTouchable); 
    if (this.j != null)
      this.j.setTouchable(paramTouchable); 
    if (this.b != null)
      this.b.setTouchable(paramTouchable); 
  }
  
  public final void bw() {
    if (this.j != null)
      this.j.setVisible(false); 
    this.aZ = false;
    if (this.j != null && this.j.getScrollFocus() == this.a)
      this.j.setScrollFocus(null); 
  }
  
  public final void s(int paramInt1, int paramInt2) {
    if (this.F == null || this.F.length == 0)
      return; 
    if (--paramInt1 < 0 || paramInt1 >= this.F.length)
      return; 
    this.F[paramInt1] = paramInt2;
    bv();
  }
  
  protected final void e(float paramFloat1, float paramFloat2) {
    boolean bool1 = (Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS) ? true : false;
    boolean bool2 = (paramFloat2 > paramFloat1) ? true : false;
    this.aL = (bool1 || bool2);
    if (this.j == null || !this.j.isVisible())
      return; 
    float f1 = ((cq)this.j).bP;
    float f2 = this.aL ? ((cq)this.j).am : 1.0F;
    f1 *= f2;
    f2 = this.aL ? cq.b() : lj.b((cq)this.j);
    float f3 = f1;
    float f4 = this.aL ? 30.0F : 8.0F;
    float f5 = this.aL ? (f2 * 0.8F) : (f2 * 1.02F);
    float f6 = 0.71875F;
    if (b.f != null)
      f6 = b.f.getWidth() / Math.max(1.0F, b.f.getHeight()); 
    f6 = f5 * f6;
    int i = (int)Math.floor((paramFloat2 * (this.aL ? 0.65F : 0.6F) / f1));
    i = Math.max(this.aL ? 3 : 6, Math.min(10, i));
    float f8 = this.dm * f1;
    float f9 = this.aL ? 45.0F : 20.0F;
    this.o.pack();
    float f10 = this.o.getWidth();
    float f7 = i * f1;
    float f11 = f8 + f9 + 2.0F * f4;
    float f12 = f10 + 2.0F * (f6 + 8.0F);
    if (f11 < f12)
      f11 = f12; 
    f7 = f2 + 6.0F + f7 + 6.0F + f3 + 2.0F * f4;
    if (this.aL) {
      f12 = ((cq)this.j).bP * ((cq)this.j).am;
      float f15 = (3.0F * f12 + 4.0F) * 2.0F + 28.0F;
      float f16 = (paramFloat2 - f15) * 0.95F;
      f11 = f8 + f9 + 2.0F * f4;
      f7 = Math.min(f7, f16);
      paramFloat1 = (paramFloat1 - f11) * 0.5F;
      paramFloat2 = f15 + (paramFloat2 - f15 - f7) * 0.5F;
    } else {
      paramFloat1 = (paramFloat1 - f11) * 0.5F;
      paramFloat2 = (paramFloat2 - f7) * 0.5F;
    } 
    paramFloat1 = Math.round(paramFloat1);
    paramFloat2 = Math.round(paramFloat2);
    f11 = Math.round(f11);
    f7 = Math.round(f7);
    this.j.setBounds(paramFloat1, paramFloat2, f11, f7);
    this.C.setBounds(0.0F, 0.0F, f11, f7);
    f12 = f4;
    paramFloat2 = f4;
    float f13 = f11 - 2.0F * f4;
    float f14 = f7 - f4 - f2;
    this.D.setBounds(f12, f14, f13, f2);
    this.u.setSize(f6, f5);
    f7 = this.aL ? 15.0F : (-f4 / 2.0F);
    paramFloat1 = f14 + (f2 - f5) / 2.0F;
    this.u.setPosition(f11 - f4 - f6 - f7, paramFloat1);
    paramFloat1 = f13 - (f6 + Math.abs(f7) + 6.0F) * 2.0F;
    paramFloat1 = Math.max(40.0F, Math.min(f10, paramFloat1));
    this.o.setSize(paramFloat1, f2);
    this.o.setPosition(f12 + (f13 - paramFloat1) * 0.5F, f14);
    paramFloat1 = paramFloat2;
    paramFloat2 = f1 * 1.5F;
    f1 *= 1.5F;
    f2 = f3 * 0.8F;
    f4 = (f3 - f2) / 2.0F;
    this.v.setSize(paramFloat2, f2);
    this.v.setPosition(f12, paramFloat1 + f4);
    this.v.setTouchable((this.dC <= 0) ? Touchable.disabled : Touchable.enabled);
    (this.v.getColor()).a = (this.dC <= 0) ? 0.35F : 1.0F;
    this.w.setSize(f1, f2);
    this.w.setPosition(f12 + f13 - f1, paramFloat1 + f4);
    paramFloat2 = f12;
    f1 = f8 + f9;
    if (f13 > f1)
      paramFloat2 = f12 + (f13 - f1) * 0.5F; 
    paramFloat1 = paramFloat1 + f3 + 6.0F;
    f2 = f14 - paramFloat1 - 6.0F;
    this.a.setBounds(paramFloat2, paramFloat1, f1, f2);
    this.a.setScrollingDisabled(true, false);
    this.a.invalidate();
    this.a.layout();
    this.n.invalidateHierarchy();
    this.n.layout();
    this.D.toFront();
    this.o.toFront();
    this.u.toFront();
  }
  
  private void bx() {
    if (this.b == null || this.c == null || this.c.length == 0)
      return; 
    if (!this.aT) {
      this.b.clear();
      return;
    } 
    this.b.clear();
    for (byte b1 = 0; b1 < 9; b1++) {
      byte b = b1;
      int i = b1 + 1;
      this.b.addTarget(new gx(this, this.a[b], i));
    } 
    int[] arrayOfInt = { 10, 11, 12, 13, 14, 15, 16 };
    byte b2;
    for (b2 = 0; b2 < arrayOfInt.length; b2++) {
      int i;
      int j = (i = arrayOfInt[b2]) - 10;
      boolean bool = this.a[j];
      this.b.addSource(new gz(this, bool, i));
    } 
    for (b2 = 0; b2 < 9; b2++) {
      byte b = b2;
      int i = b2 + 1;
      this.b.addSource(new ha(this, this.a[b], i));
    } 
    for (b2 = 0; b2 < this.c.length; b2++) {
      byte b = b2;
      int i = b2 + 1;
      this.b.addTarget(new hb(this, (Actor)this.c[b], b, i));
      this.b.addSource(new hc(this, (Actor)this.c[b], b, i));
    } 
  }
  
  protected final boolean r() {
    return (this.f != null && this.f.isVisible());
  }
  
  public final void by() {
    if (r()) {
      bz();
      return;
    } 
    gb gb1;
    (gb1 = this).bA();
    gb1.b.setVisible(true);
    gb1.f.setVisible(true);
    gb1.b.toFront();
    gb1.f.toFront();
    gb1.dA = ((cq)gb1.j).aF;
    gb1.dy = ((cq)gb1.j).aD;
    gb1.dz = ((cq)gb1.j).aE;
    gb1.bD();
    gb1.a(gb1.j.getWidth(), gb1.j.getHeight());
  }
  
  final void bz() {
    if (this.f != null)
      this.f.setVisible(false); 
    if (this.b != null)
      this.b.setVisible(false); 
  }
  
  private void bA() {
    if (this.f != null)
      return; 
    if (this.f == null)
      this.f = a(0.0F, 0.0F, 0.0F, 0.0F); 
    if (this.i == null) {
      TextureRegionDrawable textureRegionDrawable = a(0.18F, 0.18F, 0.18F, 0.95F);
      BitmapFont bitmapFont;
      this.i = ((bitmapFont = b.d) != null) ? (TextureRegionDrawable)bitmapFont : textureRegionDrawable;
      textureRegionDrawable = this.i;
      this.j = ((bitmapFont = b.e) != null) ? (TextureRegionDrawable)bitmapFont : textureRegionDrawable;
    } 
    if (this.e == null)
      this.e = new NinePatchDrawable((NinePatch)b.d); 
    if (this.f == null)
      this.f = (TextureRegionDrawable)new NinePatchDrawable((NinePatch)b.f); 
    this.b = (Image[])new Actor();
    this.b.setTouchable(Touchable.enabled);
    this.b.addListener((EventListener)new hd(this));
    this.b.setVisible(false);
    this.j.addActor((Actor)this.b);
    this.f = (TextureRegionDrawable)new Group();
    this.f.setVisible(false);
    this.f.setTouchable(Touchable.enabled);
    this.j.addActor((Actor)this.f);
    this.r = (ImageButton)new Image((Drawable)this.e);
    this.f.addActor((Actor)this.r);
    this.s = (TextField.TextFieldStyle)new Image((Drawable)this.f);
    this.f.addActor((Actor)this.s);
    this.l = (ImageButton)new Label(b.a(((cq)this.j).S, "id_minimap"), new Label.LabelStyle(b.a((String)null), Color.WHITE));
    this.l.setAlignment(1);
    this.l.setEllipsis(true);
    this.f.addActor((Actor)this.l);
    int i = MathUtils.clamp(40, 5, 60);
    if (this.dx < 5 || this.dx > 60)
      this.dx = i; 
    this.g = (TextureRegionDrawable)new Group();
    this.f.addActor((Actor)this.g);
    bC();
    if (this.e == null) {
      TextureRegion textureRegion1;
      (textureRegion1 = new TextureRegion(this.bh)).flip(false, true);
      this.e = (NinePatchDrawable)new TextureRegionDrawable(textureRegion1);
    } 
    this.t = (TextField.TextFieldStyle)new Image((Drawable)this.e);
    this.t.setScaling(Scaling.fill);
    this.g.addActor((Actor)this.t);
    this.h = (TextureRegionDrawable)new Group();
    this.h.setTouchable(Touchable.enabled);
    this.g.addActor((Actor)this.h);
    TextureRegionDrawable textureRegionDrawable2 = a((Texture)b.f);
    TextureRegionDrawable textureRegionDrawable3 = a((Texture)b.g);
    ImageButton.ImageButtonStyle imageButtonStyle;
    (imageButtonStyle = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)textureRegionDrawable2;
    imageButtonStyle.imageDown = (Drawable)textureRegionDrawable3;
    this.k = (TextureRegionDrawable)new ImageButton(imageButtonStyle);
    this.k.getImage().setScaling(Scaling.fit);
    this.k.getImageCell().pad(0.0F).expand().fill();
    this.k.addListener((EventListener)new he(this));
    this.f.addActor((Actor)this.k);
    TextureRegion textureRegion;
    Texture texture1;
    if ((textureRegion = (TextureRegion)(((texture1 = b.aA) != null) ? new TextureRegion(texture1) : null)) != null && textureRegion.getRegionWidth() > 2 && textureRegion.getRegionHeight() > 2)
      textureRegion.setRegion(textureRegion.getRegionX() + 1, textureRegion.getRegionY() + 1, textureRegion.getRegionWidth() - 2, textureRegion.getRegionHeight() - 2); 
    TextureRegionDrawable textureRegionDrawable1 = (textureRegion != null) ? new TextureRegionDrawable(textureRegion) : null;
    this.l = a((Drawable)this.i, (Drawable)this.j, (Drawable)textureRegionDrawable1);
    this.l.addListener((EventListener)new hf(this));
    this.h.addActor((Actor)this.l);
    Pixmap pixmap;
    (pixmap = new Pixmap(7, 7, Pixmap.Format.RGBA8888)).setColor(0.0F, 0.0F, 0.0F, 1.0F);
    pixmap.fill();
    pixmap.setColor(1.0F, 1.0F, 1.0F, 1.0F);
    pixmap.fillRectangle(1, 1, 5, 5);
    Texture texture2;
    (texture2 = new Texture(pixmap)).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    pixmap.dispose();
    this.u = (ImageButton)new Image((Drawable)new TextureRegionDrawable(new TextureRegion(texture2)));
    this.g.addActor((Actor)this.u);
    if (this.v == null) {
      this.v = (ImageButton)new Image(a());
      this.v.setVisible(false);
      this.v.setTouchable(Touchable.disabled);
      this.g.addActor((Actor)this.v);
      this.v.toBack();
      this.t.toBack();
    } 
    this.t.setTouchable(Touchable.enabled);
    this.t.addListener((EventListener)new hg(this));
    bD();
  }
  
  final boolean e(be parambe) {
    if (this.dB <= 0)
      return false; 
    if (parambe.aF != ((cq)this.j).aF)
      return true; 
    int j = Math.abs(parambe.aD - ((cq)this.j).aD);
    int i = Math.abs(parambe.aE - ((cq)this.j).aE);
    return (j + i > this.dB);
  }
  
  final void bB() {
    if (this.v == null)
      return; 
    this.dA = ((cq)this.j).aF;
    this.dy = ((cq)this.j).aD;
    this.dz = ((cq)this.j).aE;
    bD();
    this.v.clearActions();
    this.v.setVisible(true);
    (this.v.getColor()).a = 0.0F;
    this.v.addAction((Action)Actions.sequence((Action)Actions.fadeIn(0.08F), (Action)Actions.delay(0.28F), (Action)Actions.fadeOut(0.28F), (Action)Actions.visible(false)));
  }
  
  private static Drawable a() {
    Pixmap pixmap;
    (pixmap = new Pixmap(128, 128, Pixmap.Format.RGBA8888)).setColor(1.0F, 1.0F, 1.0F, 0.0F);
    pixmap.fill();
    128 / 2;
    128 / 2;
    pixmap.setColor(1.0F, 1.0F, 1.0F, 0.12F);
    128 / 2;
    pixmap.fillCircle(64, 64, 62);
    pixmap.setColor(1.0F, 1.0F, 1.0F, 0.35F);
    128 / 2;
    pixmap.drawCircle(64, 64, 62);
    Texture texture;
    (texture = new Texture(pixmap)).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    pixmap.dispose();
    return (Drawable)new TextureRegionDrawable(new TextureRegion(texture));
  }
  
  protected final void f(float paramFloat1, float paramFloat2) {
    if (this.b == null || this.f == null)
      return; 
    this.b.setBounds(0.0F, 0.0F, paramFloat1, paramFloat2);
    if (!this.f.isVisible())
      return; 
    boolean bool1 = (Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS) ? true : false;
    boolean bool2 = (paramFloat2 > paramFloat1) ? true : false;
    this.aL = (bool1 || bool2);
    float f1 = this.aL ? ((((cq)this.j).am > 1.0F) ? ((cq)this.j).am : 1.5F) : 1.0F;
    float f2 = this.aL ? 0.95F : 0.75F;
    float f3 = 8.0F * f1;
    float f4 = this.aL ? cq.b() : lj.b((cq)this.j);
    float f5 = paramFloat1 * f2;
    f2 = paramFloat2 * f2;
    f2 = Math.min(f5 - f3 * 2.0F, f2 - f4 - f3 * 3.0F);
    f5 = (f2 = Math.max(200.0F * f1, f2)) + f3 * 2.0F;
    float f6 = f2 + f4 + f3 * 3.0F;
    paramFloat1 = MathUtils.round((paramFloat1 - f5) * 0.5F);
    paramFloat2 = MathUtils.round((paramFloat2 - f6) * 0.5F);
    this.f.setPosition(paramFloat1, paramFloat2);
    this.f.setSize(f5, f6);
    this.r.setBounds(0.0F, 0.0F, f5, f6);
    paramFloat1 = f6 - f3 - f4;
    paramFloat2 = f5 - f3 * 2.0F;
    this.s.setBounds(f3, paramFloat1, paramFloat2, f4);
    f6 = this.aL ? (f4 * 0.8F) : (f4 * 1.02F);
    float f7 = 0.71875F;
    if (b.f != null)
      f7 = b.f.getWidth() / Math.max(1.0F, b.f.getHeight()); 
    f7 = f6 * f7;
    this.k.setSize(f7, f6);
    float f8 = this.aL ? 15.0F : (-f3 / 2.0F);
    f6 = paramFloat1 + (f4 - f6) / 2.0F;
    this.k.setPosition(f5 - f3 - f7 - f8, f6);
    this.l.setFontScale(f1);
    this.l.pack();
    f5 = this.l.getWidth();
    f6 = paramFloat2 - (f7 + Math.abs(f8) + 6.0F) * 2.0F;
    f5 = Math.max(40.0F, Math.min(f5, f6));
    this.l.setSize(f5, f4);
    this.l.setAlignment(1);
    this.l.setPosition(MathUtils.round(this.s.getX() + (paramFloat2 - f5) * 0.5F), MathUtils.round(paramFloat1));
    paramFloat1 = f3;
    paramFloat2 = f3;
    this.g.setPosition(paramFloat1, paramFloat2);
    this.g.setSize(f2, f2);
    this.t.setBounds(0.0F, 0.0F, f2, f2);
    paramFloat1 = ((cq)this.j).bP;
    paramFloat1 = Math.max(30.0F, paramFloat1 * 0.95F) * f1;
    paramFloat2 = 6.0F * f1;
    if (this.l != null) {
      this.l.setSize(paramFloat1, paramFloat1);
      f1 = f2 - paramFloat2 - paramFloat1;
      paramFloat1 = f2 - paramFloat2 - paramFloat1;
      this.l.setPosition(MathUtils.round(f1), MathUtils.round(paramFloat1));
    } 
    if (this.u != null) {
      f1 = this.dx * 2.0F + 1.0F;
      paramFloat1 = f2 / f1;
      paramFloat2 = this.aL ? 12.0F : 7.0F;
      f1 = this.aL ? 24.0F : 12.0F;
      paramFloat1 = MathUtils.clamp(paramFloat1 * 0.6F, paramFloat2, f1);
      this.u.setSize(paramFloat1, paramFloat1);
    } 
    this.r.toBack();
    this.g.toFront();
    this.s.toFront();
    this.l.toFront();
    this.k.toFront();
    if (this.l != null)
      this.l.toFront(); 
    if (this.u != null)
      this.u.toFront(); 
  }
  
  private void bC() {
    int i = this.dx * 2 + 1;
    int j = this.dx * 2 + 1;
    i *= 2;
    j *= 2;
    if (this.b != null && this.b.getWidth() == i && this.b.getHeight() == j)
      return; 
    if (this.bh != null)
      this.bh.dispose(); 
    if (this.b != null)
      this.b.dispose(); 
    this.b = (Image[])new Pixmap(i, j, Pixmap.Format.RGBA8888);
    this.b.setColor(this.a[0]);
    this.b.fill();
    this.bh = new Texture((Pixmap)this.b);
    this.bh.setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    if (this.e != null) {
      TextureRegion textureRegion;
      (textureRegion = new TextureRegion(this.bh)).flip(false, true);
      this.e.setRegion(textureRegion);
    } 
  }
  
  final void ah(int paramInt) {
    if ((paramInt = MathUtils.clamp(paramInt, 5, 60)) == this.dx)
      return; 
    this.dx = paramInt;
    paramInt = this.dx;
    for (byte b = 0; b < E.length; b++)
      Math.abs(paramInt - E[b]); 
    bC();
    bD();
  }
  
  final void bD() {
    if (this.b == null || this.bh == null)
      return; 
    if (!((cq)this.j).N) {
      this.b.setColor(this.a[0]);
      this.b.fill();
      this.bh.draw((Pixmap)this.b, 0, 0);
      return;
    } 
    int i;
    if ((i = ((cq)this.j).aF) != this.dA) {
      this.dA = i;
      this.dy = ((cq)this.j).aD;
      this.dz = ((cq)this.j).aE;
    } 
    this.b.setColor(this.a[0]);
    this.b.fill();
    i = this.dx * 2 + 1;
    int j = this.dx * 2 + 1;
    int k = i / 2 - ((i % 2 == 0) ? 1 : 0);
    int m = j / 2 - ((j % 2 == 0) ? 1 : 0);
    k = this.dy - k;
    m = this.dz - m;
    int n = this.b.getWidth() / i;
    for (byte b = 0; b < i; b++) {
      for (byte b1 = 0; b1 < j; b1++) {
        int i1 = k + b;
        int i2 = m + b1;
        long l = b(i1, i2, this.dA);
        if (this.b.containsKey(l)) {
          boolean bool = ((i1 = ((Integer)this.b.get(l, Integer.valueOf(0))).intValue()) > 0 && i1 < this.a.length) ? this.a[i1] : this.a[0];
          this.b.setColor(bool);
          i1 = j - 1 - b1;
          this.b.fillRectangle(b * n, i1 * n, n, n);
        } 
      } 
    } 
    a(k, m, i, j, n);
    b(k, m, i, j, n);
    this.bh.draw((Pixmap)this.b, 0, 0);
    float f;
    if (this.u != null && this.g != null && (f = this.g.getWidth()) > 1.0F) {
      int i1 = ((cq)this.j).aD - k;
      int i2 = ((cq)this.j).aE - m;
      if (i1 < 0 || i1 >= i || i2 < 0 || i2 >= j) {
        this.u.setVisible(false);
      } else {
        this.u.setVisible(true);
        int i3 = j - 1 - i2;
        float f3 = f / i;
        float f4 = this.u.getWidth();
        float f1 = i1 * f3 + f3 * 0.5F - f4 * 0.5F;
        float f2 = i3 * f3 + f3 * 0.5F - f4 * 0.5F;
        this.u.setPosition((float)Math.floor(f1), (float)Math.floor(f2));
        this.u.toFront();
      } 
    } 
    e(k, m, i, j);
  }
  
  private void e(int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
    if (this.v == null || this.g == null)
      return; 
    float f4;
    if ((f4 = this.g.getWidth()) <= 1.0F)
      return; 
    f4 /= paramInt3;
    paramInt1 = ((cq)this.j).aD - paramInt1;
    paramInt2 = ((cq)this.j).aE - paramInt2;
    if (paramInt1 < 0 || paramInt1 >= paramInt3 || paramInt2 < 0 || paramInt2 >= paramInt4) {
      this.v.setVisible(false);
      return;
    } 
    paramInt2 = paramInt4 - 1 - paramInt2;
    float f1 = paramInt1 * f4 + f4 * 0.5F;
    float f2 = paramInt2 * f4 + f4 * 0.5F;
    float f3 = this.dB * f4;
    this.v.setSize(f3 * 2.0F, f3 * 2.0F);
    this.v.setPosition(MathUtils.floor(f1 - f3), MathUtils.floor(f2 - f3));
    this.v.toBack();
    this.t.toBack();
    if (this.u != null)
      this.u.toFront(); 
  }
  
  public final void f(be parambe) {
    this.j = (TextureRegionDrawable)parambe;
  }
  
  private void r(int paramInt1, int paramInt2, int paramInt3) {
    if (this.j == null)
      return; 
    if (((be)this.j).aF != paramInt3)
      return; 
    paramInt3 = this.dq / 2 - ((this.dq % 2 == 0) ? 1 : 0);
    int i = this.dr / 2 - ((this.dr % 2 == 0) ? 1 : 0);
    paramInt1 -= paramInt3;
    paramInt2 -= i;
    paramInt1 = ((be)this.j).aD - paramInt1;
    paramInt2 = ((be)this.j).aE - paramInt2;
    if (paramInt1 < 0 || paramInt1 >= this.dq || paramInt2 < 0 || paramInt2 >= this.dr)
      return; 
    paramInt3 = this.a.getWidth() / this.dq;
    this.a.setColor(Color.RED);
    int[][] arrayOfInt;
    (arrayOfInt = new int[][] { { 0, 0 }, { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }).length;
    for (byte b = 0; b < 5; b++) {
      int[] arrayOfInt1 = arrayOfInt[b];
      int k = paramInt1 + arrayOfInt1[0];
      int j = paramInt2 + arrayOfInt1[1];
      if (k >= 0 && k < this.dq && j >= 0 && j < this.dr)
        this.a.fillRectangle(k * paramInt3, j * paramInt3, paramInt3, paramInt3); 
    } 
  }
  
  private void b(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5) {
    if (this.j == null)
      return; 
    if (((be)this.j).aF != this.dA)
      return; 
    this.b.setColor(Color.RED);
    int[][] arrayOfInt;
    (arrayOfInt = new int[][] { { 0, 0 }, { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }).length;
    for (byte b = 0; b < 5; b++) {
      int[] arrayOfInt1 = arrayOfInt[b];
      int j = ((be)this.j).aD + arrayOfInt1[0];
      int i = ((be)this.j).aE + arrayOfInt1[1];
      j -= paramInt1;
      i -= paramInt2;
      if (j >= 0 && j < paramInt3 && i >= 0 && i < paramInt4) {
        i = paramInt4 - 1 - i;
        this.b.fillRectangle(j * paramInt5, i * paramInt5, paramInt5, paramInt5);
      } 
    } 
  }
  
  public final void a(String paramString, float paramFloat1, float paramFloat2, Color paramColor) {
    this.a.b(paramString, paramFloat1, paramFloat2, paramColor, null);
    this.a.a(this.p.getX(), this.p.getY(), ((cq)this.j).bP);
  }
  
  public void a(String paramString, float paramFloat1, float paramFloat2, Color paramColor, TextureRegion paramTextureRegion) {
    this.a.b(paramString, paramFloat1, paramFloat2, paramColor, paramTextureRegion);
    this.a.a(this.p.getX(), this.p.getY(), ((cq)this.j).bP);
  }
  
  protected final String a(String paramString, hp paramhp) {
    // Byte code:
    //   0: aload_1
    //   1: ldc ': '
    //   3: invokevirtual indexOf : (Ljava/lang/String;)I
    //   6: dup
    //   7: istore_3
    //   8: iconst_m1
    //   9: if_icmpne -> 14
    //   12: aload_1
    //   13: areturn
    //   14: aload_1
    //   15: iconst_0
    //   16: iload_3
    //   17: invokevirtual substring : (II)Ljava/lang/String;
    //   20: astore #4
    //   22: aload_1
    //   23: iload_3
    //   24: invokevirtual substring : (I)Ljava/lang/String;
    //   27: ldc '['
    //   29: ldc '[['
    //   31: invokevirtual replace : (Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    //   34: astore_1
    //   35: iconst_1
    //   36: istore_3
    //   37: aload_0
    //   38: getfield j : La/cq;
    //   41: ifnull -> 64
    //   44: aload #4
    //   46: aload_0
    //   47: getfield j : La/cq;
    //   50: getfield Y : Ljava/lang/String;
    //   53: invokevirtual equalsIgnoreCase : (Ljava/lang/String;)Z
    //   56: ifeq -> 64
    //   59: iconst_1
    //   60: istore_3
    //   61: goto -> 133
    //   64: aload_0
    //   65: getfield z : Ljava/util/Map;
    //   68: ifnull -> 133
    //   71: aload_0
    //   72: getfield z : Ljava/util/Map;
    //   75: invokeinterface values : ()Ljava/util/Collection;
    //   80: invokeinterface iterator : ()Ljava/util/Iterator;
    //   85: astore #5
    //   87: aload #5
    //   89: invokeinterface hasNext : ()Z
    //   94: ifeq -> 133
    //   97: aload #5
    //   99: invokeinterface next : ()Ljava/lang/Object;
    //   104: checkcast a/az
    //   107: dup
    //   108: astore #6
    //   110: getfield s : Ljava/lang/String;
    //   113: aload #4
    //   115: invokevirtual equalsIgnoreCase : (Ljava/lang/String;)Z
    //   118: ifeq -> 130
    //   121: aload #6
    //   123: getfield al : I
    //   126: istore_3
    //   127: goto -> 133
    //   130: goto -> 87
    //   133: aload #4
    //   135: ldc 'GM-'
    //   137: invokevirtual startsWith : (Ljava/lang/String;)Z
    //   140: ifeq -> 150
    //   143: ldc '[#FF0000]'
    //   145: astore #5
    //   147: goto -> 237
    //   150: aload #4
    //   152: ldc 'PM-'
    //   154: invokevirtual startsWith : (Ljava/lang/String;)Z
    //   157: ifeq -> 167
    //   160: ldc '[#4169E1]'
    //   162: astore #5
    //   164: goto -> 237
    //   167: iload_3
    //   168: iconst_3
    //   169: if_icmpne -> 179
    //   172: ldc '[#FFFF00]'
    //   174: astore #5
    //   176: goto -> 237
    //   179: iload_3
    //   180: iconst_4
    //   181: if_icmpne -> 191
    //   184: ldc '[#FF0000]'
    //   186: astore #5
    //   188: goto -> 237
    //   191: aload_2
    //   192: getstatic a/hp.b : La/hp;
    //   195: if_acmpne -> 205
    //   198: ldc '[#FFD700]'
    //   200: astore #5
    //   202: goto -> 237
    //   205: aload_2
    //   206: getstatic a/hp.c : La/hp;
    //   209: if_acmpne -> 219
    //   212: ldc '[#AAAAAA]'
    //   214: astore #5
    //   216: goto -> 237
    //   219: aload_2
    //   220: getstatic a/hp.d : La/hp;
    //   223: if_acmpne -> 233
    //   226: ldc '[#00FFFF]'
    //   228: astore #5
    //   230: goto -> 237
    //   233: ldc '[#00FF00]'
    //   235: astore #5
    //   237: aload #5
    //   239: aload #4
    //   241: aload_1
    //   242: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   247: areturn
  }
  
  public void aw() {}
  
  public void ax() {}
}
