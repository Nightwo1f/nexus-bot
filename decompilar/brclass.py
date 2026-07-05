package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Interpolation;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import com.badlogic.gdx.utils.Timer;
import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.function.Consumer;

public final class br {
  volatile boolean z = false;
  
  private volatile boolean A = false;
  
  private volatile boolean B = false;
  
  private volatile boolean C = false;
  
  private volatile boolean D = false;
  
  private volatile boolean E = false;
  
  private fj b;
  
  private Timer.Task a;
  
  private Socket a;
  
  private DataOutputStream a;
  
  private DataInputStream a;
  
  private final cq e;
  
  private DataOutputStream b;
  
  private DataInputStream b;
  
  private Socket b;
  
  bq a;
  
  final cr b;
  
  public bj a;
  
  private final Map v = new HashMap<>();
  
  public bd a;
  
  public ce a;
  
  public aw a;
  
  public ay a;
  
  private bf b;
  
  private volatile boolean F = false;
  
  private Thread b;
  
  private volatile long i = 0L;
  
  public volatile boolean G = false;
  
  private im a;
  
  private volatile long j = -1L;
  
  private volatile boolean H = false;
  
  public int bj = 0;
  
  private long k = 0L;
  
  private Timer.Task b = null;
  
  private Timer.Task c;
  
  private cd a;
  
  private jz a;
  
  private bx a = null;
  
  private void F() {
    if (this.b != null) {
      this.b.cancel();
      this.b = null;
    } 
    Gdx.app.postRunnable(() -> ll.cg());
  }
  
  private void G() {
    if (this.c != null) {
      this.c.cancel();
      this.c = null;
    } 
    Gdx.app.postRunnable(() -> ll.cg());
  }
  
  private void H() {
    if (this.z && this.B && this.A && this.C && this.D && this.E) {
      this.z = false;
      if (this.a != null) {
        this.a.cancel();
        this.a = null;
      } 
      Gdx.app.postRunnable(() -> {
            Screen screen;
            if (screen = this.b.getScreen() instanceof fj)
              ((fj)screen).i(true); 
          });
    } 
  }
  
  private void I() {
    if (this.k > 0L) {
      long l = System.currentTimeMillis();
      this.bj = (int)(l - this.k);
      this.k = 0L;
    } 
  }
  
  private void J() {
    this.H = false;
    this.j = -1L;
  }
  
  public br(cq paramcq, cr paramcr, bf parambf) {
    this.a = null;
    this.a = null;
    this.a = null;
    this.e = paramcq;
    this.b = (Timer.Task)paramcr;
    this.b = (Timer.Task)parambf;
  }
  
  private void a(cd paramcd) {
    Gdx.app.postRunnable(() -> {
          float f;
          Screen screen;
          if (!(screen = this.b.getScreen() instanceof fj))
            return; 
          fj fj1;
          be be = (fj1 = (fj)screen).i;
          Runnable runnable1 = ();
          Consumer consumer = ();
          Runnable runnable2 = ();
          if (this.a == null) {
            Runnable runnable4 = runnable2;
            Consumer consumer1 = consumer;
            Runnable runnable3 = runnable1;
            List list5 = paramcd.l;
            List list4 = paramcd.k;
            String str2 = paramcd.H;
            cq cq1 = this.e;
            be be1 = be;
            List list7 = list5;
            List list6 = list4;
            String str4 = str2;
            be be3 = be1;
            jz jz2;
            jz jz4;
            (jz4 = jz2 = new jz(cq1, runnable3, consumer1, runnable4)).cl();
            jz.b = jz4;
            jz4.bD = (Gdx.app.getType() == Application.ApplicationType.Android || be3.getHeight() > be3.getWidth());
            jz4.cb = jz4.bD ? 2.0F : 1.0F;
            jz4.l = new Group();
            jz4.l.setSize(be3.getWidth(), be3.getHeight());
            jz4.l.setTouchable(Touchable.enabled);
            be3.addActor((Actor)jz4.l);
            jz4.l.toFront();
            be be2 = be3;
            Pixmap pixmap1;
            (pixmap1 = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
            pixmap1.fill();
            Texture texture1 = new Texture(pixmap1);
            pixmap1.dispose();
            Image image;
            (image = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(texture1)))).setSize(be2.getWidth(), be2.getHeight());
            image.setColor(0.0F, 0.0F, 0.0F, 0.0F);
            image.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.12F, Interpolation.smooth));
            image.setTouchable(Touchable.enabled);
            image.addListener((EventListener)new kc(jz1));
            jz jz1;
            (jz1 = jz4).f = (Actor)image;
            jz4.l.addActor(jz4.f);
            be be4 = be3;
            List list8 = list7;
            List list3 = list6;
            String str1 = str4;
            float f4 = (jz1 = jz4).bD ? 8.0F : 10.0F;
            float f5 = jz1.bD ? cq.b() : jz1.m.ae;
            float f6 = be4.getWidth();
            float f7 = be4.getHeight();
            if (jz1.bD) {
              f6 *= 0.95F;
              f7 *= 0.9F;
            } else {
              f6 = Math.min(560.0F, f6 * 0.95F);
              f7 = Math.min(510.0F, f7 * 0.95F);
            } 
            f6 = Math.round(f6);
            f7 = Math.round(f7);
            Table table3;
            (table3 = new Table()).top();
            table3.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
            float f8 = jz1.bD ? Math.max(f4, f7 * 0.12F) : f4;
            table3.pad(f4, f4, f8, f4);
            f8 = f5;
            String str3 = str1;
            jz jz3 = jz1;
            Table table4 = new Table();
            if (b.f != null)
              table4.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
            table4.pad(0.0F);
            float f9 = jz3.bD ? (f8 * 0.8F) : (f8 * 1.02F);
            float f10 = (b.f != null) ? (b.f.getWidth() / Math.max(1.0F, b.f.getHeight())) : 0.71875F;
            f10 = f9 * f10;
            float f11 = jz3.bD ? 15.0F : -4.0F;
            Actor actor;
            (actor = new Actor()).setTouchable(Touchable.disabled);
            jz3.v = lj.a((str3 != null) ? str3 : "", Color.WHITE, false, 1);
            jz3.v.setFontScale(jz3.bD ? 2.0F : 1.0F);
            jz jz5 = jz3;
            Pixmap pixmap2;
            (pixmap2 = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
            pixmap2.fill();
            Texture texture2 = new Texture(pixmap2);
            pixmap2.dispose();
            TextureRegion textureRegion1 = (b.f != null) ? new TextureRegion((Texture)b.f) : new TextureRegion(texture2);
            TextureRegion textureRegion2 = (b.g != null) ? new TextureRegion((Texture)b.g) : textureRegion1;
            ImageButton.ImageButtonStyle imageButtonStyle;
            (imageButtonStyle = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)new TextureRegionDrawable(textureRegion1);
            imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(textureRegion2);
            ImageButton imageButton2;
            (imageButton2 = new ImageButton(imageButtonStyle)).getImage().setScaling(Scaling.fit);
            imageButton2.getImageCell().pad(0.0F).expand().fill();
            imageButton2.addListener((EventListener)new ke(jz5));
            ImageButton imageButton1 = imageButton2;
            table4.add(actor).size(f10, f9).left().padLeft(f11);
            table4.add((Actor)jz3.v).expand().fill().center().minWidth(0.0F);
            table4.add((Actor)imageButton1).size(f10, f9).right().padRight(f11);
            table4.pack();
            table4.setHeight(f8);
            table4.invalidateHierarchy();
            table4.validate();
            Table table1 = table4;
            jz1.G = new Table();
            jz1.G.center();
            if (list3 != null)
              for (String str5 : list3) {
                Label label = jz1.a(str5);
                jz1.G.add((Actor)label).center().growX().padBottom(jz1.bD ? 12.0F : 6.0F).row();
              }  
            ScrollPane scrollPane;
            (scrollPane = new ScrollPane((Actor)jz1.G)).setScrollingDisabled(true, false);
            scrollPane.setFadeScrollBars(false);
            scrollPane.setForceScroll(false, true);
            scrollPane.setOverscroll(false, true);
            Table table2 = new Table();
            NinePatchDrawable ninePatchDrawable = (b.l != null) ? new NinePatchDrawable(b.l) : new NinePatchDrawable(b.l);
            table2.setBackground((Drawable)ninePatchDrawable);
            table2.pad(jz1.bD ? 15.0F : 10.0F);
            table2.add((Actor)scrollPane).grow().center();
            jz1.H = new Table();
            jz1.H.top().left();
            jz1.b(list8);
            (scrollPane = new ScrollPane((Actor)jz1.H)).setScrollingDisabled(true, false);
            scrollPane.setFadeScrollBars(false);
            scrollPane.setForceScroll(false, true);
            scrollPane.setOverscroll(false, true);
            table3.add((Actor)table1).growX().height(f5).row();
            table3.add((Actor)table2).grow().padTop(8.0F).row();
            table3.add((Actor)scrollPane).growX().height(new kd(jz1, f5)).padTop(8.0F).row();
            table3.pack();
            table3.setSize(f6, f7);
            jz4.F = table3;
            jz4.F.setTouchable(Touchable.enabled);
            jz4.l.addActor((Actor)jz4.F);
            f = jz4.F.getWidth();
            float f1 = jz4.F.getHeight();
            float f2 = be3.getWidth();
            float f3 = be3.getHeight();
            f = Math.round((f2 - f) * 0.5F);
            f1 = Math.round((f3 - f1) * 0.5F);
            jz4.F.setPosition(Math.round(f2), f1);
            jz4.F.addAction((Action)Actions.moveTo(f, f1, 0.18F, Interpolation.smooth));
            jz4.l.addAction(new ka(jz4, (Stage)be3));
            jz4.l.addListener((EventListener)new kb(jz4));
            this.a = (bx)jz2;
            fj1.aV();
            return;
          } 
          List list2 = f.l;
          List list1 = f.k;
          String str = f.H;
          bx bx1;
          if (((jz)(bx1 = this.a)).v != null) {
            Color color = Color.WHITE;
            String str1 = (str != null) ? str : "";
            Label label = ((jz)bx1).v;
            bx bx2 = bx1;
            if (label != null) {
              if (str1 == null)
                str1 = ""; 
              BitmapFont bitmapFont = b.a(str1);
              label.setStyle(new Label.LabelStyle(bitmapFont, color));
              label.setText(str1);
              label.setWrap(false);
              label.setAlignment(1);
              label.setTouchable(Touchable.disabled);
              label.setFontScale(((jz)bx2).cb);
            } 
          } 
          ((jz)bx1).G.clearChildren();
          if (list1 != null)
            for (String str1 : list1) {
              Label label = bx1.a(str1);
              ((jz)bx1).G.add((Actor)label).center().growX().padBottom(((jz)bx1).bD ? 12.0F : 6.0F).row();
            }  
          ((jz)bx1).G.invalidateHierarchy();
          bx1.b(list2);
        });
  }
  
  public final void K() {
    Gdx.app.postRunnable(() -> {
          Screen screen = this.b.getScreen();
          if (this.a != null) {
            this.a.cl();
            this.a = null;
            this.a = null;
            return;
          } 
          if (screen instanceof fj)
            ((fj)screen).aW(); 
          this.a = null;
        });
  }
  
  public final void a(byte paramByte) {
    this.k = System.currentTimeMillis();
    il il;
    (il = new il()).aj(paramByte);
    b(il.a());
    br br1;
    (br1 = this).G();
    br1.c = new bt(br1);
    Timer.schedule(br1.c, 3.0F);
  }
  
  public final void z(int paramInt) {
    il il;
    (il = new il()).aj(110);
    il.aj(paramInt);
    b(il.a());
  }
  
  public final void A(int paramInt) {
    il il;
    (il = new il()).aj(120);
    il.aj(paramInt);
    b(il.a());
  }
  
  public final void j(int paramInt1, int paramInt2) {
    il il;
    (il = new il()).aj(164);
    il.aj(paramInt1);
    il.aj(paramInt2);
    b(il.a());
  }
  
  public final void k(int paramInt1, int paramInt2) {
    il il;
    (il = new il()).aj(165);
    il.aj(paramInt1);
    il.aj(paramInt2);
    b(il.a());
  }
  
  public final void B(int paramInt) {
    il il;
    (il = new il()).aj(169);
    il.aj(paramInt);
    b(il.a());
  }
  
  public final void l(int paramInt1, int paramInt2) {
    il il;
    (il = new il()).aj(130);
    il.d(new int[] { paramInt1, paramInt2 });
    b(il.a());
  }
  
  public final void m(int paramInt1, int paramInt2) {
    il il;
    (il = new il()).aj(160);
    il.d(new int[] { paramInt1, paramInt2 });
    b(il.a());
    br br1;
    (br1 = this).F();
    br1.b = new bs(br1);
    Timer.schedule(br1.b, 3.0F);
  }
  
  public final void L() {
    il il;
    (il = new il()).aj(161);
    b(il.a());
  }
  
  public final void C(int paramInt) {
    il il;
    (il = new il()).aj(140);
    il.aj(paramInt);
    b(il.a());
  }
  
  public final void D(int paramInt) {
    il il;
    (il = new il()).aj(154);
    il.aj(paramInt);
    b(il.a());
  }
  
  public final void e(String paramString1, String paramString2) {
    il il;
    (il = new il()).aj(151);
    il.B(paramString1);
    il.B(paramString2);
    b(il.a());
  }
  
  private void M() {
    if (this.a != null) {
      this.a.d(1.0F);
      this.a.e(b.a(this.e.S, "id_connection_to_game_server_preloading"));
    } 
    this.A = false;
    this.B = false;
    this.C = false;
    this.D = false;
    this.E = false;
    this.z = true;
    Gdx.app.postRunnable(() -> {
          fj fj1;
          (fj1 = new fj((cr)this.b, this, this.e)).i(false);
          this.b.setScreen((Screen)fj1);
          if (this.a != null)
            this.a.cancel(); 
          this.a = (bx)Timer.schedule(new bu(this), 3.0F);
          (new Thread(())).start();
          H();
        });
  }
  
  public final void b(String paramString, int paramInt) {
    J();
    (new Thread(() -> {
          try {
            this.b = (Timer.Task)new Socket();
            this.b.connect(new InetSocketAddress(paramString, paramInt), 5000);
            this.b = (Timer.Task)new DataOutputStream(this.b.getOutputStream());
            this.b = (Timer.Task)new DataInputStream(new BufferedInputStream(this.b.getInputStream(), 4096));
            this.a = (bx)this.b;
            this.a = (bx)this.b;
            br br1;
            (br1 = this).b = (Timer.Task)new Thread(() -> {
                  try {
                    while (true) {
                      int i;
                      try {
                        i = this.b.readUnsignedByte();
                      } catch (EOFException|java.net.SocketException eOFException) {}
                      int j;
                      int k;
                      if ((k = (j = this.b.readUnsignedByte()) << 8 | i) > 0) {
                        byte[] arrayOfByte1 = new byte[k];
                        this.b.readFully(arrayOfByte1);
                        byte[] arrayOfByte2;
                        (arrayOfByte2 = new byte[2 + k])[0] = (byte)i;
                        arrayOfByte2[1] = (byte)j;
                        System.arraycopy(arrayOfByte1, 0, arrayOfByte2, 2, k);
                        c(arrayOfByte2);
                      } 
                    } 
                  } catch (IOException iOException) {
                    if (!this.F)
                      iOException.printStackTrace(); 
                  } finally {
                    if (!this.F)
                      N(); 
                  } 
                }"GameResponseListener");
            br1.b.setDaemon(true);
            br1.b.start();
            br1 = this;
            il il;
            (il = new il()).aj(3);
            il.aj(36);
            il.B(br1.e.S);
            il.aj(br1.e.bK);
            il.ak(br1.e.bJ);
            if (br1.e.U && b.a != null) {
              il.aj(5);
            } else {
              il.aj(0);
            } 
            il.B(br1.e.T);
            il.ak(12);
            il.aj(br1.e.bV);
            il.aj(br1.e.bW);
            il.aj(0);
            br1.b(il.a());
            if (this.e.S) {
              br1 = this;
              (il = new il()).aj(12);
              il.B(br1.e.U);
              il.al(0);
              il.al(0);
              il.B(br1.e.Y);
              il.B(br1.e.Z);
              il.aj(br1.e.bT);
              il.aj(br1.e.bU);
              br1.b(il.a());
              return;
            } 
            br1 = this;
            (il = new il()).aj(13);
            il.B(br1.e.U);
            il.al(0);
            il.al(0);
            il.B(br1.e.Y);
            il.B(br1.e.Z);
            il.aj(br1.e.bY);
            il.aj(2);
            il.ak(62);
            il.aj(10);
            il.ak(45);
            il.aj(11);
            il.ak(57);
            il.aj(20);
            il.ak(61);
            il.aj(21);
            il.ak(63);
            il.aj(22);
            il.ak(70);
            il.aj(23);
            il.ak(67);
            il.aj(24);
            il.ak(60);
            il.aj(25);
            il.ak(67);
            il.aj(26);
            il.ak(66);
            il.aj(27);
            il.ak(46);
            il.aj(30);
            il.ak(45);
            il.aj(33);
            il.ak(24);
            il.aj(3);
            il.ak(73);
            il.aj(40);
            br1.b(il.a());
            return;
          } catch (IOException iOException) {
            this.a.c(1, b.a(this.e.S, "id_connection_to_game_server_lost"));
            return;
          } 
        }"GameConnectionThread")).start();
  }
  
  public final void b(byte[] paramArrayOfbyte) {
    il il;
    (il = new il()).ak(paramArrayOfbyte.length);
    il.d(paramArrayOfbyte);
    paramArrayOfbyte = il.a();
    this.a.write(paramArrayOfbyte);
    this.a.flush();
  }
  
  private void c(byte[] paramArrayOfbyte) {
    // Byte code:
    //   0: new a/ks
    //   3: dup
    //   4: aload_1
    //   5: invokespecial <init> : ([B)V
    //   8: dup
    //   9: astore_1
    //   10: invokevirtual q : ()I
    //   13: pop
    //   14: aload_1
    //   15: invokevirtual t : ()I
    //   18: ifle -> 6945
    //   21: aload_1
    //   22: invokevirtual p : ()I
    //   25: sipush #255
    //   28: iand
    //   29: dup
    //   30: istore_2
    //   31: tableswitch default -> 6927, 1 -> 839, 2 -> 6927, 3 -> 6927, 4 -> 6927, 5 -> 6927, 6 -> 6927, 7 -> 6927, 8 -> 6927, 9 -> 6927, 10 -> 6927, 11 -> 872, 12 -> 937, 13 -> 1061, 14 -> 6927, 15 -> 6927, 16 -> 6927, 17 -> 6927, 18 -> 6927, 19 -> 6927, 20 -> 1437, 21 -> 6927, 22 -> 6927, 23 -> 6927, 24 -> 6927, 25 -> 6927, 26 -> 6927, 27 -> 6927, 28 -> 6927, 29 -> 6927, 30 -> 6927, 31 -> 6927, 32 -> 6927, 33 -> 6927, 34 -> 6927, 35 -> 6927, 36 -> 6927, 37 -> 6927, 38 -> 6927, 39 -> 6927, 40 -> 1472, 41 -> 1521, 42 -> 836, 43 -> 836, 44 -> 836, 45 -> 836, 46 -> 836, 47 -> 836, 48 -> 836, 49 -> 836, 50 -> 836, 51 -> 1539, 52 -> 1552, 53 -> 836, 54 -> 836, 55 -> 836, 56 -> 836, 57 -> 836, 58 -> 836, 59 -> 836, 60 -> 1584, 61 -> 836, 62 -> 836, 63 -> 836, 64 -> 836, 65 -> 1602, 66 -> 1610, 67 -> 1628, 68 -> 1628, 69 -> 836, 70 -> 1688, 71 -> 1763, 72 -> 1833, 73 -> 1915, 74 -> 2455, 75 -> 2642, 76 -> 2642, 77 -> 836, 78 -> 836, 79 -> 836, 80 -> 836, 81 -> 836, 82 -> 836, 83 -> 836, 84 -> 836, 85 -> 836, 86 -> 836, 87 -> 836, 88 -> 836, 89 -> 836, 90 -> 836, 91 -> 836, 92 -> 836, 93 -> 836, 94 -> 836, 95 -> 836, 96 -> 836, 97 -> 836, 98 -> 836, 99 -> 836, 100 -> 2664, 101 -> 2965, 102 -> 3036, 103 -> 3107, 104 -> 3178, 105 -> 3249, 106 -> 836, 107 -> 836, 108 -> 836, 109 -> 836, 110 -> 3397, 111 -> 3449, 112 -> 3490, 113 -> 836, 114 -> 836, 115 -> 3498, 116 -> 836, 117 -> 3663, 118 -> 3730, 119 -> 3781, 120 -> 3824, 121 -> 3979, 122 -> 3979, 123 -> 3979, 124 -> 3979, 125 -> 4070, 126 -> 4097, 127 -> 4132, 128 -> 4358, 129 -> 4420, 130 -> 4459, 131 -> 4510, 132 -> 4567, 133 -> 4608, 134 -> 4639, 135 -> 836, 136 -> 836, 137 -> 836, 138 -> 836, 139 -> 836, 140 -> 4670, 141 -> 4738, 142 -> 4771, 143 -> 4796, 144 -> 836, 145 -> 836, 146 -> 836, 147 -> 836, 148 -> 836, 149 -> 836, 150 -> 4835, 151 -> 5017, 152 -> 5042, 153 -> 5067, 154 -> 5129, 155 -> 5175, 156 -> 5202, 157 -> 5229, 158 -> 836, 159 -> 836, 160 -> 5259, 161 -> 5457, 162 -> 5577, 163 -> 836, 164 -> 836, 165 -> 836, 166 -> 836, 167 -> 836, 168 -> 836, 169 -> 5627, 170 -> 5658, 171 -> 5691, 172 -> 5802, 173 -> 5914, 174 -> 5724, 175 -> 836, 176 -> 5921, 177 -> 5989, 178 -> 6089, 179 -> 6129, 180 -> 6158, 181 -> 6173, 182 -> 6188, 183 -> 836, 184 -> 6292, 185 -> 836, 186 -> 6640, 187 -> 836, 188 -> 6648, 189 -> 836, 190 -> 6660, 191 -> 6715, 192 -> 6751, 193 -> 6723, 194 -> 6779, 195 -> 6806, 196 -> 6927, 197 -> 6814, 198 -> 6852
    //   836: goto -> 14
    //   839: aload_1
    //   840: invokevirtual q : ()I
    //   843: istore_2
    //   844: aload_0
    //   845: getfield e : La/cq;
    //   848: iload_2
    //   849: putfield bO : I
    //   852: aload_0
    //   853: getfield a : La/aw;
    //   856: ifnull -> 6942
    //   859: aload_0
    //   860: getfield a : La/aw;
    //   863: iload_2
    //   864: invokeinterface l : (I)V
    //   869: goto -> 14
    //   872: aload_1
    //   873: invokevirtual q : ()I
    //   876: pop
    //   877: aload_1
    //   878: invokevirtual g : ()Ljava/lang/String;
    //   881: astore_2
    //   882: aload_0
    //   883: dup
    //   884: astore #4
    //   886: iconst_1
    //   887: putfield H : Z
    //   890: aload #4
    //   892: invokestatic nanoTime : ()J
    //   895: putfield j : J
    //   898: aload_0
    //   899: getfield a : La/bq;
    //   902: ifnull -> 919
    //   905: aload_0
    //   906: getfield a : La/bq;
    //   909: iconst_1
    //   910: aload_2
    //   911: invokeinterface c : (ILjava/lang/String;)V
    //   916: goto -> 14
    //   919: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   922: aload_0
    //   923: aload_2
    //   924: <illegal opcode> run : (La/br;Ljava/lang/String;)Ljava/lang/Runnable;
    //   929: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   934: goto -> 14
    //   937: aload_1
    //   938: invokevirtual p : ()I
    //   941: sipush #255
    //   944: iand
    //   945: dup
    //   946: istore_2
    //   947: ifne -> 977
    //   950: aload_0
    //   951: getfield e : La/cq;
    //   954: getfield S : Z
    //   957: ifeq -> 977
    //   960: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   963: aload_0
    //   964: <illegal opcode> run : (La/br;)Ljava/lang/Runnable;
    //   969: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   974: goto -> 14
    //   977: new java/util/ArrayList
    //   980: dup
    //   981: iload_2
    //   982: invokespecial <init> : (I)V
    //   985: astore_3
    //   986: iconst_0
    //   987: istore #4
    //   989: iload #4
    //   991: iload_2
    //   992: if_icmpge -> 1012
    //   995: aload_3
    //   996: aload_1
    //   997: invokevirtual g : ()Ljava/lang/String;
    //   1000: invokeinterface add : (Ljava/lang/Object;)Z
    //   1005: pop
    //   1006: iinc #4, 1
    //   1009: goto -> 989
    //   1012: aload_0
    //   1013: getfield e : La/cq;
    //   1016: aload_3
    //   1017: astore #7
    //   1019: dup
    //   1020: astore #4
    //   1022: getfield o : Ljava/util/List;
    //   1025: invokeinterface clear : ()V
    //   1030: aload #4
    //   1032: getfield o : Ljava/util/List;
    //   1035: aload #7
    //   1037: invokeinterface addAll : (Ljava/util/Collection;)Z
    //   1042: pop
    //   1043: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   1046: aload_0
    //   1047: aload_3
    //   1048: <illegal opcode> run : (La/br;Ljava/util/List;)Ljava/lang/Runnable;
    //   1053: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   1058: goto -> 14
    //   1061: aload_0
    //   1062: dup
    //   1063: astore #13
    //   1065: getfield a : La/im;
    //   1068: ifnonnull -> 1085
    //   1071: getstatic a/b.a : La/im;
    //   1074: ifnull -> 1085
    //   1077: aload #13
    //   1079: getstatic a/b.a : La/im;
    //   1082: putfield a : La/im;
    //   1085: aload #13
    //   1087: getfield a : La/im;
    //   1090: ifnonnull -> 1103
    //   1093: new java/lang/IllegalStateException
    //   1096: dup
    //   1097: ldc 'Dictionary ainda ncarregado, mas jrecebi pacote de mapa do servidor.'
    //   1099: invokespecial <init> : (Ljava/lang/String;)V
    //   1102: athrow
    //   1103: aload #13
    //   1105: getfield a : La/im;
    //   1108: dup
    //   1109: astore_3
    //   1110: dup
    //   1111: astore_2
    //   1112: getfield b : [S
    //   1115: astore #4
    //   1117: new a/bv
    //   1120: dup
    //   1121: aload_1
    //   1122: invokespecial <init> : (La/ks;)V
    //   1125: astore_2
    //   1126: new java/util/ArrayList
    //   1129: dup
    //   1130: invokespecial <init> : ()V
    //   1133: astore #5
    //   1135: aload_2
    //   1136: aload #4
    //   1138: invokestatic a : (La/bv;[S)I
    //   1141: istore #6
    //   1143: aload_3
    //   1144: iload #6
    //   1146: istore #7
    //   1148: getfield a : [S
    //   1151: iload #7
    //   1153: saload
    //   1154: istore #7
    //   1156: aload_3
    //   1157: iload #6
    //   1159: invokevirtual am : (I)V
    //   1162: iload #7
    //   1164: ifeq -> 1183
    //   1167: aload #5
    //   1169: iload #7
    //   1171: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1174: invokeinterface add : (Ljava/lang/Object;)Z
    //   1179: pop
    //   1180: goto -> 1135
    //   1183: aload_2
    //   1184: invokevirtual ac : ()V
    //   1187: aload_1
    //   1188: invokevirtual p : ()I
    //   1191: sipush #255
    //   1194: iand
    //   1195: istore #6
    //   1197: new java/util/ArrayList
    //   1200: dup
    //   1201: invokespecial <init> : ()V
    //   1204: astore #7
    //   1206: iconst_0
    //   1207: istore_2
    //   1208: iload_2
    //   1209: iload #6
    //   1211: if_icmpge -> 1238
    //   1214: aload #7
    //   1216: aload_1
    //   1217: invokevirtual q : ()I
    //   1220: ldc 65535
    //   1222: iand
    //   1223: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1226: invokeinterface add : (Ljava/lang/Object;)Z
    //   1231: pop
    //   1232: iinc #2, 1
    //   1235: goto -> 1208
    //   1238: aload_1
    //   1239: invokevirtual p : ()I
    //   1242: sipush #255
    //   1245: iand
    //   1246: istore_2
    //   1247: new java/util/ArrayList
    //   1250: dup
    //   1251: invokespecial <init> : ()V
    //   1254: astore_3
    //   1255: iconst_0
    //   1256: istore #4
    //   1258: iload #4
    //   1260: iload_2
    //   1261: if_icmpge -> 1412
    //   1264: aload_1
    //   1265: invokevirtual p : ()I
    //   1268: istore #5
    //   1270: aload_1
    //   1271: invokevirtual q : ()I
    //   1274: istore #6
    //   1276: iconst_0
    //   1277: istore #7
    //   1279: iconst_0
    //   1280: istore #8
    //   1282: iconst_0
    //   1283: istore #9
    //   1285: iconst_0
    //   1286: istore #10
    //   1288: iconst_3
    //   1289: newarray byte
    //   1291: astore #11
    //   1293: iconst_3
    //   1294: newarray byte
    //   1296: astore #12
    //   1298: iconst_3
    //   1299: newarray byte
    //   1301: astore #13
    //   1303: iconst_3
    //   1304: newarray byte
    //   1306: astore #14
    //   1308: iconst_3
    //   1309: newarray byte
    //   1311: astore #15
    //   1313: iload #6
    //   1315: invokestatic i : (I)Z
    //   1318: ifne -> 1370
    //   1321: aload_1
    //   1322: invokevirtual q : ()I
    //   1325: istore #7
    //   1327: aload_1
    //   1328: invokevirtual q : ()I
    //   1331: istore #8
    //   1333: aload_1
    //   1334: invokevirtual q : ()I
    //   1337: istore #9
    //   1339: aload_1
    //   1340: invokevirtual q : ()I
    //   1343: istore #10
    //   1345: aload_1
    //   1346: invokevirtual u : ()I
    //   1349: pop
    //   1350: aload_1
    //   1351: invokevirtual u : ()I
    //   1354: pop
    //   1355: aload_1
    //   1356: invokevirtual u : ()I
    //   1359: pop
    //   1360: aload_1
    //   1361: invokevirtual u : ()I
    //   1364: pop
    //   1365: aload_1
    //   1366: invokevirtual u : ()I
    //   1369: pop
    //   1370: aload_3
    //   1371: new a/bw
    //   1374: dup
    //   1375: iload #5
    //   1377: iload #6
    //   1379: iload #7
    //   1381: iload #8
    //   1383: iload #9
    //   1385: iload #10
    //   1387: aload #11
    //   1389: aload #12
    //   1391: aload #13
    //   1393: aload #14
    //   1395: aload #15
    //   1397: invokespecial <init> : (IIIIII[B[B[B[B[B)V
    //   1400: invokeinterface add : (Ljava/lang/Object;)Z
    //   1405: pop
    //   1406: iinc #4, 1
    //   1409: goto -> 1258
    //   1412: aload_1
    //   1413: invokevirtual t : ()I
    //   1416: ifle -> 1424
    //   1419: aload_1
    //   1420: invokevirtual p : ()I
    //   1423: pop
    //   1424: aload_0
    //   1425: invokevirtual M : ()V
    //   1428: goto -> 14
    //   1431: invokevirtual printStackTrace : ()V
    //   1434: goto -> 14
    //   1437: aload_0
    //   1438: astore #13
    //   1440: new a/il
    //   1443: dup
    //   1444: invokespecial <init> : ()V
    //   1447: dup
    //   1448: astore_2
    //   1449: bipush #30
    //   1451: invokevirtual aj : (I)V
    //   1454: aload #13
    //   1456: aload_2
    //   1457: invokevirtual a : ()[B
    //   1460: invokevirtual b : ([B)V
    //   1463: goto -> 14
    //   1466: invokevirtual printStackTrace : ()V
    //   1469: goto -> 14
    //   1472: aload_1
    //   1473: invokevirtual q : ()I
    //   1476: pop
    //   1477: aload_1
    //   1478: invokevirtual q : ()I
    //   1481: pop
    //   1482: aload_1
    //   1483: invokevirtual p : ()I
    //   1486: pop
    //   1487: iconst_0
    //   1488: istore #6
    //   1490: iload #6
    //   1492: sipush #1024
    //   1495: if_icmpge -> 1518
    //   1498: aload_1
    //   1499: invokevirtual p : ()I
    //   1502: istore #5
    //   1504: iload #6
    //   1506: iload #5
    //   1508: iconst_4
    //   1509: ishr
    //   1510: iconst_1
    //   1511: iadd
    //   1512: iadd
    //   1513: istore #6
    //   1515: goto -> 1490
    //   1518: goto -> 14
    //   1521: aload_1
    //   1522: invokevirtual q : ()I
    //   1525: pop
    //   1526: aload_1
    //   1527: invokevirtual q : ()I
    //   1530: pop
    //   1531: aload_1
    //   1532: invokevirtual p : ()I
    //   1535: pop
    //   1536: goto -> 14
    //   1539: aload_1
    //   1540: invokevirtual q : ()I
    //   1543: pop
    //   1544: aload_1
    //   1545: invokevirtual p : ()I
    //   1548: pop
    //   1549: goto -> 14
    //   1552: aload_1
    //   1553: invokevirtual r : ()I
    //   1556: istore #6
    //   1558: aload_1
    //   1559: invokevirtual p : ()I
    //   1562: pop
    //   1563: aload_0
    //   1564: getfield a : La/aw;
    //   1567: ifnull -> 6942
    //   1570: aload_0
    //   1571: getfield a : La/aw;
    //   1574: iload #6
    //   1576: invokeinterface j : (I)V
    //   1581: goto -> 14
    //   1584: aload_1
    //   1585: invokevirtual g : ()Ljava/lang/String;
    //   1588: pop
    //   1589: aload_1
    //   1590: invokevirtual g : ()Ljava/lang/String;
    //   1593: pop
    //   1594: aload_1
    //   1595: invokevirtual g : ()Ljava/lang/String;
    //   1598: pop
    //   1599: goto -> 14
    //   1602: aload_1
    //   1603: invokevirtual g : ()Ljava/lang/String;
    //   1606: pop
    //   1607: goto -> 14
    //   1610: aload_1
    //   1611: invokevirtual g : ()Ljava/lang/String;
    //   1614: pop
    //   1615: aload_1
    //   1616: invokevirtual g : ()Ljava/lang/String;
    //   1619: pop
    //   1620: aload_1
    //   1621: invokevirtual p : ()I
    //   1624: pop
    //   1625: goto -> 14
    //   1628: aload_1
    //   1629: invokevirtual f : ()Ljava/lang/String;
    //   1632: pop
    //   1633: aload_1
    //   1634: invokevirtual f : ()Ljava/lang/String;
    //   1637: dup
    //   1638: astore #4
    //   1640: invokestatic h : (Ljava/lang/String;)Ljava/lang/String;
    //   1643: dup
    //   1644: astore #5
    //   1646: ifnull -> 1667
    //   1649: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   1652: aload #5
    //   1654: <illegal opcode> run : (Ljava/lang/String;)Ljava/lang/Runnable;
    //   1659: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   1664: goto -> 14
    //   1667: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   1670: ldc 'ServerClient'
    //   1672: aload #4
    //   1674: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;)Ljava/lang/String;
    //   1679: aconst_null
    //   1680: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   1685: goto -> 14
    //   1688: aload_0
    //   1689: new a/bx
    //   1692: dup
    //   1693: invokespecial <init> : ()V
    //   1696: putfield a : La/bx;
    //   1699: aload_1
    //   1700: invokevirtual q : ()I
    //   1703: ldc 65535
    //   1705: iand
    //   1706: istore_3
    //   1707: aload_0
    //   1708: getfield a : La/bx;
    //   1711: iload_3
    //   1712: i2l
    //   1713: putfield l : J
    //   1716: aload_1
    //   1717: invokevirtual q : ()I
    //   1720: pop
    //   1721: aload_1
    //   1722: invokevirtual g : ()Ljava/lang/String;
    //   1725: pop
    //   1726: aload_1
    //   1727: invokevirtual g : ()Ljava/lang/String;
    //   1730: astore #4
    //   1732: aload_0
    //   1733: getfield a : La/bx;
    //   1736: aload #4
    //   1738: putfield w : Ljava/lang/String;
    //   1741: aload_1
    //   1742: invokevirtual p : ()I
    //   1745: pop
    //   1746: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   1749: aload_0
    //   1750: <illegal opcode> run : (La/br;)Ljava/lang/Runnable;
    //   1755: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   1760: goto -> 14
    //   1763: aload_1
    //   1764: invokevirtual g : ()Ljava/lang/String;
    //   1767: astore_3
    //   1768: aload_1
    //   1769: invokevirtual p : ()I
    //   1772: sipush #255
    //   1775: iand
    //   1776: istore #4
    //   1778: aload_0
    //   1779: getfield a : La/bx;
    //   1782: ifnull -> 6942
    //   1785: new a/bz
    //   1788: dup
    //   1789: invokespecial <init> : ()V
    //   1792: dup
    //   1793: astore #5
    //   1795: aload_3
    //   1796: putfield B : Ljava/lang/String;
    //   1799: aload #5
    //   1801: iload #4
    //   1803: iconst_1
    //   1804: if_icmpne -> 1811
    //   1807: iconst_1
    //   1808: goto -> 1812
    //   1811: iconst_0
    //   1812: putfield al : I
    //   1815: aload_0
    //   1816: getfield a : La/bx;
    //   1819: getfield j : Ljava/util/List;
    //   1822: aload #5
    //   1824: invokeinterface add : (Ljava/lang/Object;)Z
    //   1829: pop
    //   1830: goto -> 14
    //   1833: aload_1
    //   1834: invokevirtual g : ()Ljava/lang/String;
    //   1837: astore_3
    //   1838: aload_1
    //   1839: invokevirtual g : ()Ljava/lang/String;
    //   1842: pop
    //   1843: aload_1
    //   1844: invokevirtual q : ()I
    //   1847: istore #4
    //   1849: aload_1
    //   1850: invokevirtual p : ()I
    //   1853: istore #5
    //   1855: aload_0
    //   1856: getfield a : La/bx;
    //   1859: ifnull -> 6942
    //   1862: new a/cb
    //   1865: dup
    //   1866: invokespecial <init> : ()V
    //   1869: dup
    //   1870: astore #6
    //   1872: aload_3
    //   1873: putfield C : Ljava/lang/String;
    //   1876: aload #6
    //   1878: iload #4
    //   1880: putfield bp : I
    //   1883: aload #6
    //   1885: iload #5
    //   1887: putfield al : I
    //   1890: aload #6
    //   1892: iconst_0
    //   1893: putfield bq : I
    //   1896: aload #6
    //   1898: ldc ''
    //   1900: putfield D : Ljava/lang/String;
    //   1903: aload_0
    //   1904: getfield a : La/bx;
    //   1907: aload #6
    //   1909: putfield a : La/cb;
    //   1912: goto -> 14
    //   1915: aload_1
    //   1916: invokevirtual g : ()Ljava/lang/String;
    //   1919: astore_3
    //   1920: aload_1
    //   1921: invokevirtual g : ()Ljava/lang/String;
    //   1924: astore #4
    //   1926: aload_1
    //   1927: invokevirtual g : ()Ljava/lang/String;
    //   1930: astore #5
    //   1932: aload_1
    //   1933: invokevirtual g : ()Ljava/lang/String;
    //   1936: astore #6
    //   1938: aload_0
    //   1939: getfield a : La/bx;
    //   1942: aload_3
    //   1943: putfield x : Ljava/lang/String;
    //   1946: aload_0
    //   1947: getfield a : La/bx;
    //   1950: aload #4
    //   1952: putfield y : Ljava/lang/String;
    //   1955: aload_0
    //   1956: getfield a : La/bx;
    //   1959: aload #5
    //   1961: putfield z : Ljava/lang/String;
    //   1964: aload_0
    //   1965: getfield a : La/bx;
    //   1968: aload #6
    //   1970: putfield A : Ljava/lang/String;
    //   1973: aload_1
    //   1974: invokevirtual q : ()I
    //   1977: pop
    //   1978: aload_1
    //   1979: invokevirtual p : ()I
    //   1982: pop
    //   1983: aload_1
    //   1984: invokevirtual q : ()I
    //   1987: ldc 65535
    //   1989: iand
    //   1990: istore #9
    //   1992: iconst_0
    //   1993: istore #10
    //   1995: iload #10
    //   1997: iload #9
    //   1999: if_icmpge -> 2452
    //   2002: aload_1
    //   2003: invokevirtual r : ()I
    //   2006: istore #11
    //   2008: aconst_null
    //   2009: astore #12
    //   2011: aconst_null
    //   2012: astore #13
    //   2014: aconst_null
    //   2015: astore #14
    //   2017: aload_1
    //   2018: invokevirtual p : ()I
    //   2021: sipush #255
    //   2024: iand
    //   2025: tableswitch default -> 2316, 1 -> 2060, 2 -> 2087, 3 -> 2114, 4 -> 2262, 5 -> 2289
    //   2060: aload_1
    //   2061: invokevirtual q : ()I
    //   2064: ldc 65535
    //   2066: iand
    //   2067: dup
    //   2068: istore_2
    //   2069: ifle -> 2340
    //   2072: iconst_1
    //   2073: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2076: astore #12
    //   2078: iload_2
    //   2079: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2082: astore #13
    //   2084: goto -> 2340
    //   2087: aload_1
    //   2088: invokevirtual q : ()I
    //   2091: ldc 65535
    //   2093: iand
    //   2094: dup
    //   2095: istore_2
    //   2096: ifle -> 2340
    //   2099: iconst_2
    //   2100: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2103: astore #12
    //   2105: iload_2
    //   2106: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2109: astore #13
    //   2111: goto -> 2340
    //   2114: aload_1
    //   2115: invokevirtual p : ()I
    //   2118: sipush #255
    //   2121: iand
    //   2122: istore_2
    //   2123: aload_1
    //   2124: invokevirtual q : ()I
    //   2127: ldc 65535
    //   2129: iand
    //   2130: istore_3
    //   2131: iload_2
    //   2132: iconst_1
    //   2133: iand
    //   2134: ifeq -> 2141
    //   2137: iconst_1
    //   2138: goto -> 2142
    //   2141: iconst_0
    //   2142: ifne -> 2164
    //   2145: iload_3
    //   2146: ifle -> 2164
    //   2149: iconst_3
    //   2150: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2153: astore #12
    //   2155: iload_3
    //   2156: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2159: astore #13
    //   2161: goto -> 2340
    //   2164: aload_1
    //   2165: invokevirtual q : ()I
    //   2168: ldc 65535
    //   2170: iand
    //   2171: istore #5
    //   2173: aload_1
    //   2174: invokevirtual q : ()I
    //   2177: ldc 65535
    //   2179: iand
    //   2180: istore #6
    //   2182: aload_1
    //   2183: invokevirtual q : ()I
    //   2186: ldc 65535
    //   2188: iand
    //   2189: istore #4
    //   2191: aload_1
    //   2192: invokevirtual q : ()I
    //   2195: ldc 65535
    //   2197: iand
    //   2198: istore #7
    //   2200: aload_1
    //   2201: invokevirtual u : ()I
    //   2204: istore #8
    //   2206: aload_1
    //   2207: invokevirtual u : ()I
    //   2210: istore #14
    //   2212: aload_1
    //   2213: invokevirtual u : ()I
    //   2216: istore #15
    //   2218: aload_1
    //   2219: invokevirtual u : ()I
    //   2222: istore #16
    //   2224: aload_1
    //   2225: invokevirtual u : ()I
    //   2228: istore #17
    //   2230: new a/jn
    //   2233: dup
    //   2234: iload_2
    //   2235: iload_3
    //   2236: iload #6
    //   2238: iload #5
    //   2240: iload #4
    //   2242: iload #7
    //   2244: iload #14
    //   2246: iload #8
    //   2248: iload #15
    //   2250: iload #16
    //   2252: iload #17
    //   2254: invokespecial <init> : (IIIIIIIIIII)V
    //   2257: astore #14
    //   2259: goto -> 2340
    //   2262: aload_1
    //   2263: invokevirtual q : ()I
    //   2266: ldc 65535
    //   2268: iand
    //   2269: dup
    //   2270: istore_2
    //   2271: ifle -> 2340
    //   2274: iconst_4
    //   2275: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2278: astore #12
    //   2280: iload_2
    //   2281: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2284: astore #13
    //   2286: goto -> 2340
    //   2289: aload_1
    //   2290: invokevirtual q : ()I
    //   2293: ldc 65535
    //   2295: iand
    //   2296: dup
    //   2297: istore_2
    //   2298: ifle -> 2340
    //   2301: iconst_5
    //   2302: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2305: astore #12
    //   2307: iload_2
    //   2308: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2311: astore #13
    //   2313: goto -> 2340
    //   2316: aload_1
    //   2317: invokevirtual q : ()I
    //   2320: ldc 65535
    //   2322: iand
    //   2323: dup
    //   2324: istore_2
    //   2325: ifle -> 2340
    //   2328: iconst_4
    //   2329: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2332: astore #12
    //   2334: iload_2
    //   2335: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2338: astore #13
    //   2340: aload_1
    //   2341: invokevirtual g : ()Ljava/lang/String;
    //   2344: astore_2
    //   2345: aload_1
    //   2346: invokevirtual g : ()Ljava/lang/String;
    //   2349: astore_3
    //   2350: aload_1
    //   2351: invokevirtual g : ()Ljava/lang/String;
    //   2354: astore #4
    //   2356: aload_1
    //   2357: invokevirtual p : ()I
    //   2360: sipush #255
    //   2363: iand
    //   2364: istore #5
    //   2366: new a/cc
    //   2369: dup
    //   2370: invokespecial <init> : ()V
    //   2373: dup
    //   2374: astore #6
    //   2376: iload #11
    //   2378: putfield d : I
    //   2381: aload #6
    //   2383: aload_2
    //   2384: putfield E : Ljava/lang/String;
    //   2387: aload #6
    //   2389: aload_3
    //   2390: putfield F : Ljava/lang/String;
    //   2393: aload #6
    //   2395: aload #4
    //   2397: putfield G : Ljava/lang/String;
    //   2400: aload #6
    //   2402: iload #5
    //   2404: invokestatic c : (I)I
    //   2407: putfield al : I
    //   2410: aload #6
    //   2412: aload #12
    //   2414: putfield b : Ljava/lang/Integer;
    //   2417: aload #6
    //   2419: aload #13
    //   2421: putfield c : Ljava/lang/Integer;
    //   2424: aload #6
    //   2426: aload #14
    //   2428: putfield a : La/jn;
    //   2431: aload_0
    //   2432: getfield a : La/bx;
    //   2435: getfield h : Ljava/util/List;
    //   2438: aload #6
    //   2440: invokeinterface add : (Ljava/lang/Object;)Z
    //   2445: pop
    //   2446: iinc #10, 1
    //   2449: goto -> 1995
    //   2452: goto -> 14
    //   2455: aload_1
    //   2456: invokevirtual q : ()I
    //   2459: ldc 65535
    //   2461: iand
    //   2462: istore_3
    //   2463: iconst_0
    //   2464: istore #7
    //   2466: iload #7
    //   2468: iload_3
    //   2469: if_icmpge -> 2619
    //   2472: aload_1
    //   2473: invokevirtual r : ()I
    //   2476: istore #8
    //   2478: aload_1
    //   2479: invokevirtual g : ()Ljava/lang/String;
    //   2482: astore #9
    //   2484: aload_1
    //   2485: invokevirtual p : ()I
    //   2488: sipush #255
    //   2491: iand
    //   2492: istore #10
    //   2494: aload_1
    //   2495: invokevirtual p : ()I
    //   2498: sipush #255
    //   2501: iand
    //   2502: bipush #8
    //   2504: if_icmpne -> 2511
    //   2507: iconst_1
    //   2508: goto -> 2512
    //   2511: iconst_0
    //   2512: istore #12
    //   2514: iload #10
    //   2516: bipush #45
    //   2518: if_icmpne -> 2547
    //   2521: aload_0
    //   2522: getfield a : La/bx;
    //   2525: ifnull -> 2613
    //   2528: aload_0
    //   2529: getfield a : La/bx;
    //   2532: iload #8
    //   2534: sipush #255
    //   2537: iand
    //   2538: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   2541: putfield a : Ljava/lang/Integer;
    //   2544: goto -> 2613
    //   2547: iload #10
    //   2549: invokestatic b : (I)Z
    //   2552: ifeq -> 2613
    //   2555: aload_0
    //   2556: getfield a : La/bx;
    //   2559: ifnull -> 2613
    //   2562: new a/by
    //   2565: dup
    //   2566: invokespecial <init> : ()V
    //   2569: dup
    //   2570: astore #13
    //   2572: iload #8
    //   2574: putfield d : I
    //   2577: aload #13
    //   2579: aload #9
    //   2581: putfield B : Ljava/lang/String;
    //   2584: aload #13
    //   2586: iload #12
    //   2588: putfield I : Z
    //   2591: aload #13
    //   2593: iload #10
    //   2595: putfield bo : I
    //   2598: aload_0
    //   2599: getfield a : La/bx;
    //   2602: getfield i : Ljava/util/List;
    //   2605: aload #13
    //   2607: invokeinterface add : (Ljava/lang/Object;)Z
    //   2612: pop
    //   2613: iinc #7, 1
    //   2616: goto -> 2466
    //   2619: aload_0
    //   2620: getfield a : La/bx;
    //   2623: ifnull -> 6942
    //   2626: aload_0
    //   2627: dup
    //   2628: getfield a : La/bx;
    //   2631: invokevirtual a : (La/bx;)V
    //   2634: aload_0
    //   2635: aconst_null
    //   2636: putfield a : La/bx;
    //   2639: goto -> 14
    //   2642: aload_1
    //   2643: invokevirtual p : ()I
    //   2646: pop
    //   2647: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   2650: aload_0
    //   2651: <illegal opcode> run : (La/br;)Ljava/lang/Runnable;
    //   2656: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   2661: goto -> 14
    //   2664: aload_0
    //   2665: invokevirtual G : ()V
    //   2668: aload_0
    //   2669: getfield a : La/bj;
    //   2672: instanceof a/fj
    //   2675: ifeq -> 2688
    //   2678: aload_0
    //   2679: getfield a : La/bj;
    //   2682: checkcast a/fj
    //   2685: invokevirtual aQ : ()V
    //   2688: aload_0
    //   2689: getfield e : La/cq;
    //   2692: invokevirtual g : ()Z
    //   2695: ifeq -> 2753
    //   2698: getstatic a/b.a : La/f;
    //   2701: ifnull -> 2753
    //   2704: aload_1
    //   2705: invokevirtual p : ()I
    //   2708: pop
    //   2709: aload_0
    //   2710: getfield a : La/bj;
    //   2713: instanceof a/fj
    //   2716: ifeq -> 2946
    //   2719: aload_0
    //   2720: getfield a : La/bj;
    //   2723: checkcast a/fj
    //   2726: aload_0
    //   2727: getfield e : La/cq;
    //   2730: invokevirtual j : ()I
    //   2733: aload_0
    //   2734: getfield e : La/cq;
    //   2737: invokevirtual k : ()I
    //   2740: aload_0
    //   2741: getfield e : La/cq;
    //   2744: invokevirtual l : ()I
    //   2747: invokevirtual i : (III)V
    //   2750: goto -> 2946
    //   2753: new a/bv
    //   2756: dup
    //   2757: aload_1
    //   2758: invokespecial <init> : (La/ks;)V
    //   2761: astore_3
    //   2762: aload_0
    //   2763: getfield a : La/im;
    //   2766: invokevirtual a : ()[S
    //   2769: astore #4
    //   2771: aload_0
    //   2772: getfield e : La/cq;
    //   2775: invokevirtual j : ()I
    //   2778: aload_0
    //   2779: invokevirtual d : ()I
    //   2782: isub
    //   2783: istore #5
    //   2785: aload_0
    //   2786: getfield e : La/cq;
    //   2789: invokevirtual k : ()I
    //   2792: aload_0
    //   2793: invokevirtual e : ()I
    //   2796: isub
    //   2797: istore #6
    //   2799: aload_0
    //   2800: getfield e : La/cq;
    //   2803: invokevirtual l : ()I
    //   2806: istore #7
    //   2808: aload_0
    //   2809: getfield v : Ljava/util/Map;
    //   2812: invokeinterface clear : ()V
    //   2817: iconst_0
    //   2818: istore #8
    //   2820: iload #8
    //   2822: aload_0
    //   2823: getfield e : La/cq;
    //   2826: getfield bW : I
    //   2829: if_icmpge -> 2909
    //   2832: iconst_0
    //   2833: istore #9
    //   2835: iload #9
    //   2837: aload_0
    //   2838: getfield e : La/cq;
    //   2841: invokevirtual i : ()I
    //   2844: if_icmpge -> 2903
    //   2847: aload_0
    //   2848: aload_3
    //   2849: aload #4
    //   2851: iload #9
    //   2853: iload #8
    //   2855: iload #7
    //   2857: invokevirtual a : (La/bv;[SIII)La/cg;
    //   2860: astore #10
    //   2862: new a/be
    //   2865: dup
    //   2866: iload #5
    //   2868: iload #9
    //   2870: iadd
    //   2871: iload #6
    //   2873: iload #8
    //   2875: iadd
    //   2876: iload #7
    //   2878: invokespecial <init> : (III)V
    //   2881: astore #11
    //   2883: aload_0
    //   2884: getfield v : Ljava/util/Map;
    //   2887: aload #11
    //   2889: aload #10
    //   2891: invokeinterface put : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   2896: pop
    //   2897: iinc #9, 1
    //   2900: goto -> 2835
    //   2903: iinc #8, 1
    //   2906: goto -> 2820
    //   2909: aload_3
    //   2910: invokevirtual ac : ()V
    //   2913: aload_0
    //   2914: getfield a : La/bj;
    //   2917: ifnull -> 2940
    //   2920: aload_0
    //   2921: getfield a : La/bj;
    //   2924: new java/util/HashMap
    //   2927: dup
    //   2928: aload_0
    //   2929: getfield v : Ljava/util/Map;
    //   2932: invokespecial <init> : (Ljava/util/Map;)V
    //   2935: invokeinterface a : (Ljava/util/Map;)V
    //   2940: goto -> 2946
    //   2943: invokevirtual printStackTrace : ()V
    //   2946: aload_0
    //   2947: getfield z : Z
    //   2950: ifeq -> 6942
    //   2953: aload_0
    //   2954: iconst_1
    //   2955: putfield B : Z
    //   2958: aload_0
    //   2959: invokevirtual H : ()V
    //   2962: goto -> 14
    //   2965: aload_0
    //   2966: invokevirtual I : ()V
    //   2969: aload_0
    //   2970: invokevirtual G : ()V
    //   2973: aload_0
    //   2974: getfield e : La/cq;
    //   2977: aload_0
    //   2978: getfield e : La/cq;
    //   2981: invokevirtual j : ()I
    //   2984: aload_0
    //   2985: getfield e : La/cq;
    //   2988: invokevirtual k : ()I
    //   2991: iconst_1
    //   2992: isub
    //   2993: aload_0
    //   2994: getfield e : La/cq;
    //   2997: invokevirtual l : ()I
    //   3000: invokevirtual g : (III)V
    //   3003: aload_0
    //   3004: getfield e : La/cq;
    //   3007: invokevirtual g : ()Z
    //   3010: ifeq -> 3027
    //   3013: getstatic a/b.a : La/f;
    //   3016: ifnull -> 3027
    //   3019: aload_1
    //   3020: invokevirtual p : ()I
    //   3023: pop
    //   3024: goto -> 14
    //   3027: aload_0
    //   3028: aload_1
    //   3029: iload_2
    //   3030: invokevirtual a : (La/ks;I)V
    //   3033: goto -> 14
    //   3036: aload_0
    //   3037: invokevirtual I : ()V
    //   3040: aload_0
    //   3041: invokevirtual G : ()V
    //   3044: aload_0
    //   3045: getfield e : La/cq;
    //   3048: aload_0
    //   3049: getfield e : La/cq;
    //   3052: invokevirtual j : ()I
    //   3055: iconst_1
    //   3056: iadd
    //   3057: aload_0
    //   3058: getfield e : La/cq;
    //   3061: invokevirtual k : ()I
    //   3064: aload_0
    //   3065: getfield e : La/cq;
    //   3068: invokevirtual l : ()I
    //   3071: invokevirtual g : (III)V
    //   3074: aload_0
    //   3075: getfield e : La/cq;
    //   3078: invokevirtual g : ()Z
    //   3081: ifeq -> 3098
    //   3084: getstatic a/b.a : La/f;
    //   3087: ifnull -> 3098
    //   3090: aload_1
    //   3091: invokevirtual p : ()I
    //   3094: pop
    //   3095: goto -> 14
    //   3098: aload_0
    //   3099: aload_1
    //   3100: iload_2
    //   3101: invokevirtual a : (La/ks;I)V
    //   3104: goto -> 14
    //   3107: aload_0
    //   3108: invokevirtual I : ()V
    //   3111: aload_0
    //   3112: invokevirtual G : ()V
    //   3115: aload_0
    //   3116: getfield e : La/cq;
    //   3119: aload_0
    //   3120: getfield e : La/cq;
    //   3123: invokevirtual j : ()I
    //   3126: aload_0
    //   3127: getfield e : La/cq;
    //   3130: invokevirtual k : ()I
    //   3133: iconst_1
    //   3134: iadd
    //   3135: aload_0
    //   3136: getfield e : La/cq;
    //   3139: invokevirtual l : ()I
    //   3142: invokevirtual g : (III)V
    //   3145: aload_0
    //   3146: getfield e : La/cq;
    //   3149: invokevirtual g : ()Z
    //   3152: ifeq -> 3169
    //   3155: getstatic a/b.a : La/f;
    //   3158: ifnull -> 3169
    //   3161: aload_1
    //   3162: invokevirtual p : ()I
    //   3165: pop
    //   3166: goto -> 14
    //   3169: aload_0
    //   3170: aload_1
    //   3171: iload_2
    //   3172: invokevirtual a : (La/ks;I)V
    //   3175: goto -> 14
    //   3178: aload_0
    //   3179: invokevirtual I : ()V
    //   3182: aload_0
    //   3183: invokevirtual G : ()V
    //   3186: aload_0
    //   3187: getfield e : La/cq;
    //   3190: aload_0
    //   3191: getfield e : La/cq;
    //   3194: invokevirtual j : ()I
    //   3197: iconst_1
    //   3198: isub
    //   3199: aload_0
    //   3200: getfield e : La/cq;
    //   3203: invokevirtual k : ()I
    //   3206: aload_0
    //   3207: getfield e : La/cq;
    //   3210: invokevirtual l : ()I
    //   3213: invokevirtual g : (III)V
    //   3216: aload_0
    //   3217: getfield e : La/cq;
    //   3220: invokevirtual g : ()Z
    //   3223: ifeq -> 3240
    //   3226: getstatic a/b.a : La/f;
    //   3229: ifnull -> 3240
    //   3232: aload_1
    //   3233: invokevirtual p : ()I
    //   3236: pop
    //   3237: goto -> 14
    //   3240: aload_0
    //   3241: aload_1
    //   3242: iload_2
    //   3243: invokevirtual a : (La/ks;I)V
    //   3246: goto -> 14
    //   3249: aload_0
    //   3250: invokevirtual G : ()V
    //   3253: aload_1
    //   3254: invokevirtual q : ()I
    //   3257: istore_3
    //   3258: aload_1
    //   3259: invokevirtual q : ()I
    //   3262: istore #4
    //   3264: aload_1
    //   3265: invokevirtual p : ()I
    //   3268: istore #5
    //   3270: aload_0
    //   3271: getfield e : La/cq;
    //   3274: invokevirtual j : ()I
    //   3277: istore #6
    //   3279: aload_0
    //   3280: getfield e : La/cq;
    //   3283: invokevirtual k : ()I
    //   3286: istore #7
    //   3288: aload_0
    //   3289: getfield e : La/cq;
    //   3292: invokevirtual l : ()I
    //   3295: istore #8
    //   3297: aload_0
    //   3298: getfield e : La/cq;
    //   3301: iload_3
    //   3302: iload #4
    //   3304: iload #5
    //   3306: invokevirtual g : (III)V
    //   3309: aload_0
    //   3310: getfield a : La/bj;
    //   3313: ifnull -> 3341
    //   3316: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   3319: aload_0
    //   3320: iload #6
    //   3322: iload #7
    //   3324: iload #8
    //   3326: iload_3
    //   3327: iload #4
    //   3329: iload #5
    //   3331: <illegal opcode> run : (La/br;IIIIII)Ljava/lang/Runnable;
    //   3336: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   3341: aload_0
    //   3342: astore_2
    //   3343: new a/il
    //   3346: dup
    //   3347: invokespecial <init> : ()V
    //   3350: dup
    //   3351: astore_3
    //   3352: bipush #31
    //   3354: invokevirtual aj : (I)V
    //   3357: aload_2
    //   3358: aload_3
    //   3359: invokevirtual a : ()[B
    //   3362: invokevirtual b : ([B)V
    //   3365: goto -> 3371
    //   3368: invokevirtual printStackTrace : ()V
    //   3371: aload_0
    //   3372: invokestatic nanoTime : ()J
    //   3375: putfield i : J
    //   3378: aload_0
    //   3379: getfield z : Z
    //   3382: ifeq -> 6942
    //   3385: aload_0
    //   3386: iconst_1
    //   3387: putfield A : Z
    //   3390: aload_0
    //   3391: invokevirtual H : ()V
    //   3394: goto -> 14
    //   3397: aload_1
    //   3398: aload_0
    //   3399: getfield e : La/cq;
    //   3402: invokevirtual i : ()I
    //   3405: aload_0
    //   3406: getfield e : La/cq;
    //   3409: getfield R : Z
    //   3412: invokevirtual a : (IZ)I
    //   3415: istore #9
    //   3417: aload_1
    //   3418: invokevirtual q : ()I
    //   3421: ldc 65535
    //   3423: iand
    //   3424: istore #10
    //   3426: aload_0
    //   3427: getfield a : La/bj;
    //   3430: ifnull -> 6942
    //   3433: aload_0
    //   3434: getfield a : La/bj;
    //   3437: iload #9
    //   3439: iload #10
    //   3441: invokeinterface d : (II)V
    //   3446: goto -> 14
    //   3449: aload_1
    //   3450: aload_0
    //   3451: getfield e : La/cq;
    //   3454: invokevirtual i : ()I
    //   3457: aload_0
    //   3458: getfield e : La/cq;
    //   3461: getfield R : Z
    //   3464: invokevirtual a : (IZ)I
    //   3467: istore #9
    //   3469: aload_0
    //   3470: getfield a : La/bj;
    //   3473: ifnull -> 6942
    //   3476: aload_0
    //   3477: getfield a : La/bj;
    //   3480: iload #9
    //   3482: invokeinterface t : (I)V
    //   3487: goto -> 14
    //   3490: aload_1
    //   3491: invokevirtual q : ()I
    //   3494: pop
    //   3495: goto -> 14
    //   3498: aload_1
    //   3499: aload_0
    //   3500: getfield e : La/cq;
    //   3503: invokevirtual i : ()I
    //   3506: aload_0
    //   3507: getfield e : La/cq;
    //   3510: getfield R : Z
    //   3513: invokevirtual a : (IZ)I
    //   3516: istore #10
    //   3518: aload_0
    //   3519: iload #10
    //   3521: invokevirtual a : (I)La/be;
    //   3524: astore #11
    //   3526: new a/bv
    //   3529: dup
    //   3530: aload_1
    //   3531: invokespecial <init> : (La/ks;)V
    //   3534: astore #12
    //   3536: aload_0
    //   3537: getfield a : La/im;
    //   3540: invokevirtual a : ()[S
    //   3543: astore #13
    //   3545: aload_0
    //   3546: aload #12
    //   3548: aload #13
    //   3550: aload #11
    //   3552: invokevirtual a : ()I
    //   3555: aload #11
    //   3557: invokevirtual b : ()I
    //   3560: aload #11
    //   3562: invokevirtual c : ()I
    //   3565: invokevirtual a : (La/bv;[SIII)La/cg;
    //   3568: astore #14
    //   3570: aload #12
    //   3572: invokevirtual ac : ()V
    //   3575: aload #14
    //   3577: getfield a : Lcom/badlogic/gdx/utils/IntArray;
    //   3580: dup
    //   3581: astore #15
    //   3583: getfield size : I
    //   3586: newarray int
    //   3588: astore_2
    //   3589: iconst_0
    //   3590: istore_3
    //   3591: iload_3
    //   3592: aload #15
    //   3594: getfield size : I
    //   3597: if_icmpge -> 3618
    //   3600: aload_2
    //   3601: iload_3
    //   3602: aload #15
    //   3604: iload_3
    //   3605: invokevirtual get : (I)I
    //   3608: ldc 65535
    //   3610: iand
    //   3611: iastore
    //   3612: iinc #3, 1
    //   3615: goto -> 3591
    //   3618: aload_0
    //   3619: getfield a : La/bj;
    //   3622: instanceof a/fj
    //   3625: ifeq -> 3654
    //   3628: aload_0
    //   3629: getfield a : La/bj;
    //   3632: checkcast a/fj
    //   3635: aload #11
    //   3637: invokevirtual a : ()I
    //   3640: aload #11
    //   3642: invokevirtual b : ()I
    //   3645: aload #11
    //   3647: invokevirtual c : ()I
    //   3650: aload_2
    //   3651: invokevirtual a : (III[I)V
    //   3654: goto -> 14
    //   3657: invokevirtual printStackTrace : ()V
    //   3660: goto -> 14
    //   3663: aload_1
    //   3664: invokevirtual p : ()I
    //   3667: sipush #255
    //   3670: iand
    //   3671: istore #12
    //   3673: aload_1
    //   3674: invokevirtual p : ()I
    //   3677: sipush #255
    //   3680: iand
    //   3681: istore #13
    //   3683: aload_1
    //   3684: invokevirtual p : ()I
    //   3687: sipush #255
    //   3690: iand
    //   3691: istore #14
    //   3693: aload_1
    //   3694: invokevirtual p : ()I
    //   3697: sipush #255
    //   3700: iand
    //   3701: istore #15
    //   3703: aload_0
    //   3704: getfield a : La/aw;
    //   3707: ifnull -> 6942
    //   3710: aload_0
    //   3711: getfield a : La/aw;
    //   3714: iload #12
    //   3716: iload #13
    //   3718: iload #14
    //   3720: iload #15
    //   3722: invokeinterface a : (IIII)V
    //   3727: goto -> 14
    //   3730: aload_1
    //   3731: invokevirtual p : ()I
    //   3734: sipush #255
    //   3737: iand
    //   3738: istore_2
    //   3739: aload_1
    //   3740: invokevirtual p : ()I
    //   3743: sipush #255
    //   3746: iand
    //   3747: istore_3
    //   3748: aload_1
    //   3749: invokevirtual p : ()I
    //   3752: sipush #255
    //   3755: iand
    //   3756: istore #4
    //   3758: aload_0
    //   3759: getfield a : La/aw;
    //   3762: ifnull -> 6942
    //   3765: aload_0
    //   3766: getfield a : La/aw;
    //   3769: iload_2
    //   3770: iload_3
    //   3771: iload #4
    //   3773: invokeinterface b : (III)V
    //   3778: goto -> 14
    //   3781: aload_1
    //   3782: invokevirtual p : ()I
    //   3785: sipush #255
    //   3788: iand
    //   3789: istore #5
    //   3791: aload_1
    //   3792: invokevirtual p : ()I
    //   3795: sipush #255
    //   3798: iand
    //   3799: istore #6
    //   3801: aload_0
    //   3802: getfield a : La/aw;
    //   3805: ifnull -> 6942
    //   3808: aload_0
    //   3809: getfield a : La/aw;
    //   3812: iload #5
    //   3814: iload #6
    //   3816: invokeinterface b : (II)V
    //   3821: goto -> 14
    //   3824: aload_1
    //   3825: invokevirtual p : ()I
    //   3828: sipush #255
    //   3831: iand
    //   3832: istore #4
    //   3834: aload_1
    //   3835: invokevirtual p : ()I
    //   3838: sipush #255
    //   3841: iand
    //   3842: istore #7
    //   3844: aload_1
    //   3845: invokevirtual q : ()I
    //   3848: ldc 65535
    //   3850: iand
    //   3851: istore #8
    //   3853: iconst_0
    //   3854: istore #14
    //   3856: iconst_0
    //   3857: istore #15
    //   3859: iconst_0
    //   3860: istore #16
    //   3862: iconst_0
    //   3863: istore #17
    //   3865: iconst_0
    //   3866: istore_2
    //   3867: iconst_0
    //   3868: istore_3
    //   3869: iconst_0
    //   3870: istore #5
    //   3872: iconst_0
    //   3873: istore #6
    //   3875: iconst_0
    //   3876: istore #9
    //   3878: iload #8
    //   3880: invokestatic i : (I)Z
    //   3883: ifne -> 3938
    //   3886: aload_1
    //   3887: invokevirtual q : ()I
    //   3890: istore #15
    //   3892: aload_1
    //   3893: invokevirtual q : ()I
    //   3896: istore #14
    //   3898: aload_1
    //   3899: invokevirtual q : ()I
    //   3902: istore #16
    //   3904: aload_1
    //   3905: invokevirtual q : ()I
    //   3908: istore #17
    //   3910: aload_1
    //   3911: invokevirtual u : ()I
    //   3914: istore_3
    //   3915: aload_1
    //   3916: invokevirtual u : ()I
    //   3919: istore_2
    //   3920: aload_1
    //   3921: invokevirtual u : ()I
    //   3924: istore #5
    //   3926: aload_1
    //   3927: invokevirtual u : ()I
    //   3930: istore #6
    //   3932: aload_1
    //   3933: invokevirtual u : ()I
    //   3936: istore #9
    //   3938: aload_0
    //   3939: getfield a : La/bj;
    //   3942: ifnull -> 3976
    //   3945: aload_0
    //   3946: getfield a : La/bj;
    //   3949: iload #4
    //   3951: iload #7
    //   3953: iload #8
    //   3955: iload #14
    //   3957: iload #15
    //   3959: iload #16
    //   3961: iload #17
    //   3963: iload_2
    //   3964: iload_3
    //   3965: iload #5
    //   3967: iload #6
    //   3969: iload #9
    //   3971: invokeinterface a : (IIIIIIIIIIII)V
    //   3976: goto -> 14
    //   3979: aload_1
    //   3980: invokevirtual p : ()I
    //   3983: sipush #255
    //   3986: iand
    //   3987: istore #4
    //   3989: iload_2
    //   3990: tableswitch default -> 4044, 121 -> 4020, 122 -> 4026, 123 -> 4032, 124 -> 4038
    //   4020: iconst_0
    //   4021: istore #7
    //   4023: goto -> 4047
    //   4026: iconst_1
    //   4027: istore #7
    //   4029: goto -> 4047
    //   4032: iconst_2
    //   4033: istore #7
    //   4035: goto -> 4047
    //   4038: iconst_3
    //   4039: istore #7
    //   4041: goto -> 4047
    //   4044: iconst_0
    //   4045: istore #7
    //   4047: aload_0
    //   4048: getfield a : La/bj;
    //   4051: ifnull -> 6942
    //   4054: aload_0
    //   4055: getfield a : La/bj;
    //   4058: iload #4
    //   4060: iload #7
    //   4062: invokeinterface g : (II)V
    //   4067: goto -> 14
    //   4070: aload_1
    //   4071: invokevirtual p : ()I
    //   4074: istore #4
    //   4076: aload_0
    //   4077: getfield a : La/bj;
    //   4080: ifnull -> 6942
    //   4083: aload_0
    //   4084: getfield a : La/bj;
    //   4087: iload #4
    //   4089: invokeinterface w : (I)V
    //   4094: goto -> 14
    //   4097: aload_1
    //   4098: invokevirtual p : ()I
    //   4101: istore #7
    //   4103: aload_1
    //   4104: invokevirtual p : ()I
    //   4107: istore #8
    //   4109: aload_0
    //   4110: getfield a : La/aw;
    //   4113: ifnull -> 6942
    //   4116: aload_0
    //   4117: getfield a : La/aw;
    //   4120: iload #7
    //   4122: iload #8
    //   4124: invokeinterface a : (II)V
    //   4129: goto -> 14
    //   4132: aload_1
    //   4133: invokevirtual p : ()I
    //   4136: istore #14
    //   4138: aload_1
    //   4139: aload_0
    //   4140: getfield e : La/cq;
    //   4143: invokevirtual i : ()I
    //   4146: aload_0
    //   4147: getfield e : La/cq;
    //   4150: getfield R : Z
    //   4153: invokevirtual a : (IZ)I
    //   4156: istore #15
    //   4158: aload_1
    //   4159: invokevirtual p : ()I
    //   4162: istore #16
    //   4164: aload_1
    //   4165: invokevirtual g : ()Ljava/lang/String;
    //   4168: astore #17
    //   4170: aload_1
    //   4171: invokevirtual p : ()I
    //   4174: istore_2
    //   4175: aload_1
    //   4176: invokevirtual p : ()I
    //   4179: istore_3
    //   4180: aload_1
    //   4181: invokevirtual q : ()I
    //   4184: istore #5
    //   4186: iconst_0
    //   4187: istore #6
    //   4189: iconst_0
    //   4190: istore #9
    //   4192: iconst_0
    //   4193: istore #4
    //   4195: iconst_0
    //   4196: istore #7
    //   4198: iconst_0
    //   4199: istore #8
    //   4201: iconst_0
    //   4202: istore #10
    //   4204: iconst_0
    //   4205: istore #11
    //   4207: iconst_0
    //   4208: istore #12
    //   4210: iconst_0
    //   4211: istore #13
    //   4213: iconst_0
    //   4214: istore #19
    //   4216: iload #5
    //   4218: invokestatic i : (I)Z
    //   4221: ifne -> 4278
    //   4224: aload_1
    //   4225: invokevirtual q : ()I
    //   4228: istore #9
    //   4230: aload_1
    //   4231: invokevirtual q : ()I
    //   4234: istore #6
    //   4236: aload_1
    //   4237: invokevirtual q : ()I
    //   4240: istore #4
    //   4242: aload_1
    //   4243: invokevirtual q : ()I
    //   4246: istore #7
    //   4248: aload_1
    //   4249: invokevirtual u : ()I
    //   4252: istore #10
    //   4254: aload_1
    //   4255: invokevirtual u : ()I
    //   4258: istore #8
    //   4260: aload_1
    //   4261: invokevirtual u : ()I
    //   4264: istore #11
    //   4266: aload_1
    //   4267: invokevirtual u : ()I
    //   4270: istore #12
    //   4272: aload_1
    //   4273: invokevirtual u : ()I
    //   4276: istore #13
    //   4278: aload_1
    //   4279: invokevirtual q : ()I
    //   4282: istore #18
    //   4284: aload_0
    //   4285: getfield e : La/cq;
    //   4288: getfield T : Ljava/lang/String;
    //   4291: ldc 'jtme_client'
    //   4293: invokevirtual equalsIgnoreCase : (Ljava/lang/String;)Z
    //   4296: ifeq -> 4305
    //   4299: aload_1
    //   4300: invokevirtual q : ()I
    //   4303: istore #19
    //   4305: aload_0
    //   4306: getfield a : La/bj;
    //   4309: ifnull -> 6942
    //   4312: aload_0
    //   4313: getfield a : La/bj;
    //   4316: iload #14
    //   4318: iload #15
    //   4320: iload #16
    //   4322: aload #17
    //   4324: iload_2
    //   4325: iload #5
    //   4327: iload_3
    //   4328: iload #6
    //   4330: iload #9
    //   4332: iload #4
    //   4334: iload #7
    //   4336: iload #8
    //   4338: iload #10
    //   4340: iload #11
    //   4342: iload #12
    //   4344: iload #13
    //   4346: iload #18
    //   4348: iload #19
    //   4350: invokeinterface a : (IIILjava/lang/String;IIIIIIIIIIIIII)V
    //   4355: goto -> 14
    //   4358: aload_1
    //   4359: invokevirtual p : ()I
    //   4362: sipush #255
    //   4365: iand
    //   4366: istore_2
    //   4367: aload_1
    //   4368: aload_0
    //   4369: getfield e : La/cq;
    //   4372: invokevirtual i : ()I
    //   4375: aload_0
    //   4376: getfield e : La/cq;
    //   4379: getfield R : Z
    //   4382: invokevirtual a : (IZ)I
    //   4385: istore_3
    //   4386: aload_1
    //   4387: invokevirtual p : ()I
    //   4390: sipush #255
    //   4393: iand
    //   4394: istore #4
    //   4396: aload_0
    //   4397: getfield a : La/bj;
    //   4400: ifnull -> 6942
    //   4403: aload_0
    //   4404: getfield a : La/bj;
    //   4407: iload_2
    //   4408: iload_3
    //   4409: iload #4
    //   4411: i2b
    //   4412: invokeinterface a : (IIB)V
    //   4417: goto -> 14
    //   4420: aload_1
    //   4421: invokevirtual p : ()I
    //   4424: sipush #255
    //   4427: iand
    //   4428: istore_2
    //   4429: aload_1
    //   4430: invokevirtual p : ()I
    //   4433: sipush #255
    //   4436: iand
    //   4437: istore_3
    //   4438: aload_0
    //   4439: getfield a : La/bj;
    //   4442: ifnull -> 6942
    //   4445: aload_0
    //   4446: getfield a : La/bj;
    //   4449: iload_2
    //   4450: iload_3
    //   4451: invokeinterface h : (II)V
    //   4456: goto -> 14
    //   4459: aload_1
    //   4460: aload_0
    //   4461: getfield e : La/cq;
    //   4464: invokevirtual i : ()I
    //   4467: aload_0
    //   4468: getfield e : La/cq;
    //   4471: getfield R : Z
    //   4474: invokevirtual a : (IZ)I
    //   4477: istore #4
    //   4479: aload_1
    //   4480: invokevirtual p : ()I
    //   4483: sipush #255
    //   4486: iand
    //   4487: istore_2
    //   4488: aload_0
    //   4489: getfield a : La/bj;
    //   4492: ifnull -> 4507
    //   4495: aload_0
    //   4496: getfield a : La/bj;
    //   4499: iload #4
    //   4501: iload_2
    //   4502: invokeinterface e : (II)V
    //   4507: goto -> 14
    //   4510: aload_1
    //   4511: aload_0
    //   4512: getfield e : La/cq;
    //   4515: invokevirtual i : ()I
    //   4518: aload_0
    //   4519: getfield e : La/cq;
    //   4522: getfield R : Z
    //   4525: invokevirtual a : (IZ)I
    //   4528: istore #4
    //   4530: aload_1
    //   4531: invokevirtual p : ()I
    //   4534: sipush #255
    //   4537: iand
    //   4538: istore_2
    //   4539: aload_1
    //   4540: invokevirtual g : ()Ljava/lang/String;
    //   4543: astore_3
    //   4544: aload_0
    //   4545: getfield a : La/bj;
    //   4548: ifnull -> 6942
    //   4551: aload_0
    //   4552: getfield a : La/bj;
    //   4555: iload #4
    //   4557: iload_2
    //   4558: aload_3
    //   4559: invokeinterface a : (IILjava/lang/String;)V
    //   4564: goto -> 14
    //   4567: aload_1
    //   4568: invokevirtual p : ()I
    //   4571: sipush #255
    //   4574: iand
    //   4575: istore #4
    //   4577: aload_1
    //   4578: invokevirtual p : ()I
    //   4581: sipush #255
    //   4584: iand
    //   4585: istore_2
    //   4586: aload_0
    //   4587: getfield a : La/bj;
    //   4590: ifnull -> 6942
    //   4593: aload_0
    //   4594: getfield a : La/bj;
    //   4597: iload #4
    //   4599: iload_2
    //   4600: invokeinterface i : (II)V
    //   4605: goto -> 14
    //   4608: aload_1
    //   4609: invokevirtual p : ()I
    //   4612: sipush #255
    //   4615: iand
    //   4616: istore #4
    //   4618: aload_0
    //   4619: getfield a : La/bj;
    //   4622: ifnull -> 6942
    //   4625: aload_0
    //   4626: getfield a : La/bj;
    //   4629: iload #4
    //   4631: invokeinterface u : (I)V
    //   4636: goto -> 14
    //   4639: aload_1
    //   4640: invokevirtual p : ()I
    //   4643: sipush #255
    //   4646: iand
    //   4647: istore #4
    //   4649: aload_0
    //   4650: getfield a : La/bj;
    //   4653: ifnull -> 6942
    //   4656: aload_0
    //   4657: getfield a : La/bj;
    //   4660: iload #4
    //   4662: invokeinterface v : (I)V
    //   4667: goto -> 14
    //   4670: bipush #16
    //   4672: newarray int
    //   4674: astore #4
    //   4676: iconst_0
    //   4677: istore_2
    //   4678: iload_2
    //   4679: bipush #16
    //   4681: if_icmpge -> 4701
    //   4684: aload #4
    //   4686: iload_2
    //   4687: aload_1
    //   4688: invokevirtual q : ()I
    //   4691: ldc 65535
    //   4693: iand
    //   4694: iastore
    //   4695: iinc #2, 1
    //   4698: goto -> 4678
    //   4701: aload_0
    //   4702: getfield a : La/bd;
    //   4705: ifnull -> 4719
    //   4708: aload_0
    //   4709: getfield a : La/bd;
    //   4712: aload #4
    //   4714: invokeinterface a : ([I)V
    //   4719: aload_0
    //   4720: getfield z : Z
    //   4723: ifeq -> 6942
    //   4726: aload_0
    //   4727: iconst_1
    //   4728: putfield E : Z
    //   4731: aload_0
    //   4732: invokevirtual H : ()V
    //   4735: goto -> 14
    //   4738: aload_1
    //   4739: invokevirtual p : ()I
    //   4742: istore #4
    //   4744: aload_1
    //   4745: invokevirtual q : ()I
    //   4748: istore_2
    //   4749: aload_0
    //   4750: getfield a : La/bd;
    //   4753: ifnull -> 6942
    //   4756: aload_0
    //   4757: getfield a : La/bd;
    //   4760: iload #4
    //   4762: iload_2
    //   4763: invokeinterface c : (II)V
    //   4768: goto -> 14
    //   4771: aload_1
    //   4772: invokevirtual p : ()I
    //   4775: istore_3
    //   4776: aload_0
    //   4777: getfield a : La/bd;
    //   4780: ifnull -> 6942
    //   4783: aload_0
    //   4784: getfield a : La/bd;
    //   4787: iload_3
    //   4788: invokeinterface o : (I)V
    //   4793: goto -> 14
    //   4796: aload_1
    //   4797: invokevirtual p : ()I
    //   4800: istore_2
    //   4801: aload_1
    //   4802: invokevirtual r : ()I
    //   4805: istore_3
    //   4806: aload_1
    //   4807: invokevirtual r : ()I
    //   4810: istore #4
    //   4812: aload_0
    //   4813: getfield a : La/aw;
    //   4816: ifnull -> 6942
    //   4819: aload_0
    //   4820: getfield a : La/aw;
    //   4823: iload_2
    //   4824: iload_3
    //   4825: iload #4
    //   4827: invokeinterface a : (III)V
    //   4832: goto -> 14
    //   4835: aload_1
    //   4836: invokevirtual q : ()I
    //   4839: ldc 65535
    //   4841: iand
    //   4842: istore_2
    //   4843: aload_1
    //   4844: invokevirtual q : ()I
    //   4847: ldc 65535
    //   4849: iand
    //   4850: istore_3
    //   4851: aload_1
    //   4852: invokevirtual q : ()I
    //   4855: ldc 65535
    //   4857: iand
    //   4858: istore #4
    //   4860: aload_1
    //   4861: invokevirtual q : ()I
    //   4864: ldc 65535
    //   4866: iand
    //   4867: istore #5
    //   4869: aload_0
    //   4870: getfield e : La/cq;
    //   4873: getfield R : Z
    //   4876: ifeq -> 4903
    //   4879: aload_1
    //   4880: invokevirtual a : ()J
    //   4883: lstore #20
    //   4885: aload_1
    //   4886: invokevirtual a : ()J
    //   4889: lstore #22
    //   4891: aload_1
    //   4892: invokevirtual q : ()I
    //   4895: ldc 65535
    //   4897: iand
    //   4898: istore #6
    //   4900: goto -> 4935
    //   4903: aload_1
    //   4904: invokevirtual r : ()I
    //   4907: i2l
    //   4908: ldc2_w 4294967295
    //   4911: land
    //   4912: lstore #20
    //   4914: aload_1
    //   4915: invokevirtual r : ()I
    //   4918: i2l
    //   4919: ldc2_w 4294967295
    //   4922: land
    //   4923: lstore #22
    //   4925: aload_1
    //   4926: invokevirtual p : ()I
    //   4929: sipush #255
    //   4932: iand
    //   4933: istore #6
    //   4935: aload_1
    //   4936: invokevirtual r : ()I
    //   4939: i2l
    //   4940: ldc2_w 4294967295
    //   4943: land
    //   4944: lstore #24
    //   4946: aload_1
    //   4947: invokevirtual q : ()I
    //   4950: ldc 65535
    //   4952: iand
    //   4953: istore #7
    //   4955: aload_1
    //   4956: invokevirtual q : ()I
    //   4959: ldc 65535
    //   4961: iand
    //   4962: istore #8
    //   4964: aload_0
    //   4965: getfield a : La/aw;
    //   4968: ifnull -> 4998
    //   4971: aload_0
    //   4972: getfield a : La/aw;
    //   4975: iload_2
    //   4976: iload_3
    //   4977: iload #4
    //   4979: iload #5
    //   4981: iload #6
    //   4983: lload #20
    //   4985: lload #22
    //   4987: lload #24
    //   4989: iload #7
    //   4991: iload #8
    //   4993: invokeinterface a : (IIIIIJJJII)V
    //   4998: aload_0
    //   4999: getfield z : Z
    //   5002: ifeq -> 6942
    //   5005: aload_0
    //   5006: iconst_1
    //   5007: putfield C : Z
    //   5010: aload_0
    //   5011: invokevirtual H : ()V
    //   5014: goto -> 14
    //   5017: aload_1
    //   5018: invokevirtual q : ()I
    //   5021: istore_2
    //   5022: aload_0
    //   5023: getfield a : La/aw;
    //   5026: ifnull -> 6942
    //   5029: aload_0
    //   5030: getfield a : La/aw;
    //   5033: iload_2
    //   5034: invokeinterface e : (I)V
    //   5039: goto -> 14
    //   5042: aload_1
    //   5043: invokevirtual q : ()I
    //   5046: istore_2
    //   5047: aload_0
    //   5048: getfield a : La/aw;
    //   5051: ifnull -> 6942
    //   5054: aload_0
    //   5055: getfield a : La/aw;
    //   5058: iload_2
    //   5059: invokeinterface f : (I)V
    //   5064: goto -> 14
    //   5067: aload_0
    //   5068: getfield e : La/cq;
    //   5071: getfield R : Z
    //   5074: ifeq -> 5092
    //   5077: aload_1
    //   5078: invokevirtual a : ()J
    //   5081: lstore #26
    //   5083: aload_1
    //   5084: invokevirtual a : ()J
    //   5087: lstore #28
    //   5089: goto -> 5106
    //   5092: aload_1
    //   5093: invokevirtual r : ()I
    //   5096: i2l
    //   5097: lstore #26
    //   5099: aload_1
    //   5100: invokevirtual r : ()I
    //   5103: i2l
    //   5104: lstore #28
    //   5106: aload_0
    //   5107: getfield a : La/aw;
    //   5110: ifnull -> 6942
    //   5113: aload_0
    //   5114: getfield a : La/aw;
    //   5117: lload #26
    //   5119: lload #28
    //   5121: invokeinterface a : (JJ)V
    //   5126: goto -> 14
    //   5129: aload_0
    //   5130: getfield e : La/cq;
    //   5133: getfield R : Z
    //   5136: ifeq -> 5148
    //   5139: aload_1
    //   5140: invokevirtual q : ()I
    //   5143: istore #26
    //   5145: goto -> 5154
    //   5148: aload_1
    //   5149: invokevirtual p : ()I
    //   5152: istore #26
    //   5154: aload_0
    //   5155: getfield a : La/aw;
    //   5158: ifnull -> 6942
    //   5161: aload_0
    //   5162: getfield a : La/aw;
    //   5165: iload #26
    //   5167: invokeinterface h : (I)V
    //   5172: goto -> 14
    //   5175: aload_1
    //   5176: invokevirtual r : ()I
    //   5179: istore #27
    //   5181: aload_0
    //   5182: getfield a : La/aw;
    //   5185: ifnull -> 6942
    //   5188: aload_0
    //   5189: getfield a : La/aw;
    //   5192: iload #27
    //   5194: invokeinterface i : (I)V
    //   5199: goto -> 14
    //   5202: aload_1
    //   5203: invokevirtual q : ()I
    //   5206: istore #28
    //   5208: aload_0
    //   5209: getfield a : La/aw;
    //   5212: ifnull -> 6942
    //   5215: aload_0
    //   5216: getfield a : La/aw;
    //   5219: iload #28
    //   5221: invokeinterface g : (I)V
    //   5226: goto -> 14
    //   5229: aload_1
    //   5230: invokevirtual q : ()I
    //   5233: ldc 65535
    //   5235: iand
    //   5236: istore #29
    //   5238: aload_0
    //   5239: getfield a : La/aw;
    //   5242: ifnull -> 6942
    //   5245: aload_0
    //   5246: getfield a : La/aw;
    //   5249: iload #29
    //   5251: invokeinterface k : (I)V
    //   5256: goto -> 14
    //   5259: aload_1
    //   5260: invokevirtual p : ()I
    //   5263: sipush #255
    //   5266: iand
    //   5267: istore_2
    //   5268: aload_1
    //   5269: invokevirtual q : ()I
    //   5272: istore_3
    //   5273: iconst_0
    //   5274: istore #4
    //   5276: iconst_0
    //   5277: istore #5
    //   5279: iconst_0
    //   5280: istore #6
    //   5282: iconst_0
    //   5283: istore #7
    //   5285: iconst_0
    //   5286: istore #8
    //   5288: iconst_0
    //   5289: istore #9
    //   5291: iconst_0
    //   5292: istore #10
    //   5294: iconst_0
    //   5295: istore #11
    //   5297: iconst_0
    //   5298: istore #12
    //   5300: iload_3
    //   5301: invokestatic i : (I)Z
    //   5304: ifne -> 5361
    //   5307: aload_1
    //   5308: invokevirtual q : ()I
    //   5311: istore #5
    //   5313: aload_1
    //   5314: invokevirtual q : ()I
    //   5317: istore #4
    //   5319: aload_1
    //   5320: invokevirtual q : ()I
    //   5323: istore #6
    //   5325: aload_1
    //   5326: invokevirtual q : ()I
    //   5329: istore #7
    //   5331: aload_1
    //   5332: invokevirtual u : ()I
    //   5335: istore #9
    //   5337: aload_1
    //   5338: invokevirtual u : ()I
    //   5341: istore #8
    //   5343: aload_1
    //   5344: invokevirtual u : ()I
    //   5347: istore #10
    //   5349: aload_1
    //   5350: invokevirtual u : ()I
    //   5353: istore #11
    //   5355: aload_1
    //   5356: invokevirtual u : ()I
    //   5359: istore #12
    //   5361: aload_0
    //   5362: getfield e : La/cq;
    //   5365: aload_0
    //   5366: getfield e : La/cq;
    //   5369: getfield Y : Ljava/lang/String;
    //   5372: aload_0
    //   5373: getfield e : La/cq;
    //   5376: getfield ca : I
    //   5379: iload_3
    //   5380: iload_2
    //   5381: iload #4
    //   5383: iload #5
    //   5385: iload #6
    //   5387: iload #7
    //   5389: iload #8
    //   5391: iload #9
    //   5393: iload #10
    //   5395: iload #11
    //   5397: iload #12
    //   5399: invokestatic a : (La/cq;Ljava/lang/String;IIIIIIIIIIII)V
    //   5402: aload_0
    //   5403: getfield a : La/bj;
    //   5406: ifnull -> 5438
    //   5409: aload_0
    //   5410: getfield a : La/bj;
    //   5413: iload_2
    //   5414: iload_3
    //   5415: iload #4
    //   5417: iload #5
    //   5419: iload #6
    //   5421: iload #7
    //   5423: iload #8
    //   5425: iload #9
    //   5427: iload #10
    //   5429: iload #11
    //   5431: iload #12
    //   5433: invokeinterface a : (IIIIIIIIIII)V
    //   5438: aload_0
    //   5439: getfield z : Z
    //   5442: ifeq -> 6942
    //   5445: aload_0
    //   5446: iconst_1
    //   5447: putfield D : Z
    //   5450: aload_0
    //   5451: invokevirtual H : ()V
    //   5454: goto -> 14
    //   5457: aload_1
    //   5458: invokevirtual p : ()I
    //   5461: sipush #255
    //   5464: iand
    //   5465: istore_2
    //   5466: aload_1
    //   5467: invokevirtual p : ()I
    //   5470: i2b
    //   5471: istore_3
    //   5472: iconst_0
    //   5473: istore #4
    //   5475: iload_3
    //   5476: iconst_3
    //   5477: if_icmpne -> 5525
    //   5480: aload_1
    //   5481: invokevirtual p : ()I
    //   5484: istore_3
    //   5485: aload_1
    //   5486: invokevirtual p : ()I
    //   5489: pop
    //   5490: aload_1
    //   5491: invokevirtual p : ()I
    //   5494: pop
    //   5495: iload_3
    //   5496: iconst_1
    //   5497: iand
    //   5498: ifeq -> 5522
    //   5501: iconst_0
    //   5502: istore #5
    //   5504: iload #5
    //   5506: bipush #23
    //   5508: if_icmpge -> 5522
    //   5511: aload_1
    //   5512: invokevirtual p : ()I
    //   5515: pop
    //   5516: iinc #5, 1
    //   5519: goto -> 5504
    //   5522: goto -> 5534
    //   5525: aload_1
    //   5526: invokevirtual q : ()I
    //   5529: ldc 65535
    //   5531: iand
    //   5532: istore #4
    //   5534: aload_1
    //   5535: invokevirtual p : ()I
    //   5538: sipush #255
    //   5541: iand
    //   5542: istore_3
    //   5543: aload_1
    //   5544: invokevirtual q : ()I
    //   5547: ldc 65535
    //   5549: iand
    //   5550: istore #5
    //   5552: aload_0
    //   5553: getfield a : La/ce;
    //   5556: ifnull -> 6942
    //   5559: aload_0
    //   5560: getfield a : La/ce;
    //   5563: iload_2
    //   5564: iload #4
    //   5566: iload_3
    //   5567: iload #5
    //   5569: invokeinterface b : (IIII)V
    //   5574: goto -> 14
    //   5577: aload_1
    //   5578: invokevirtual p : ()I
    //   5581: sipush #255
    //   5584: iand
    //   5585: istore_2
    //   5586: aload_1
    //   5587: invokevirtual p : ()I
    //   5590: sipush #255
    //   5593: iand
    //   5594: istore_3
    //   5595: aload_1
    //   5596: invokevirtual q : ()I
    //   5599: ldc 65535
    //   5601: iand
    //   5602: istore #4
    //   5604: aload_0
    //   5605: getfield a : La/ce;
    //   5608: ifnull -> 6942
    //   5611: aload_0
    //   5612: getfield a : La/ce;
    //   5615: iload_2
    //   5616: iload_3
    //   5617: iload #4
    //   5619: invokeinterface e : (III)V
    //   5624: goto -> 14
    //   5627: aload_1
    //   5628: invokevirtual g : ()Ljava/lang/String;
    //   5631: astore_2
    //   5632: aload_1
    //   5633: invokevirtual g : ()Ljava/lang/String;
    //   5636: astore_3
    //   5637: aload_0
    //   5638: getfield a : La/aw;
    //   5641: ifnull -> 6942
    //   5644: aload_0
    //   5645: getfield a : La/aw;
    //   5648: aload_2
    //   5649: aload_3
    //   5650: invokeinterface c : (Ljava/lang/String;Ljava/lang/String;)V
    //   5655: goto -> 14
    //   5658: aload_1
    //   5659: invokevirtual p : ()I
    //   5662: istore #4
    //   5664: aload_1
    //   5665: invokevirtual g : ()Ljava/lang/String;
    //   5668: astore_2
    //   5669: aload_0
    //   5670: getfield a : La/bj;
    //   5673: ifnull -> 5688
    //   5676: aload_0
    //   5677: getfield a : La/bj;
    //   5680: iload #4
    //   5682: aload_2
    //   5683: invokeinterface a : (ILjava/lang/String;)V
    //   5688: goto -> 14
    //   5691: aload_1
    //   5692: invokevirtual g : ()Ljava/lang/String;
    //   5695: astore #4
    //   5697: aload_1
    //   5698: invokevirtual g : ()Ljava/lang/String;
    //   5701: astore_2
    //   5702: aload_0
    //   5703: getfield a : La/aw;
    //   5706: ifnull -> 6942
    //   5709: aload_0
    //   5710: getfield a : La/aw;
    //   5713: aload #4
    //   5715: aload_2
    //   5716: invokeinterface d : (Ljava/lang/String;Ljava/lang/String;)V
    //   5721: goto -> 14
    //   5724: aload_1
    //   5725: invokevirtual g : ()Ljava/lang/String;
    //   5728: astore #30
    //   5730: aload_1
    //   5731: invokevirtual p : ()I
    //   5734: sipush #255
    //   5737: iand
    //   5738: istore #31
    //   5740: new a/cd
    //   5743: dup
    //   5744: invokespecial <init> : ()V
    //   5747: dup
    //   5748: astore_2
    //   5749: aload #30
    //   5751: putfield H : Ljava/lang/String;
    //   5754: iconst_0
    //   5755: istore_3
    //   5756: iload_3
    //   5757: iload #31
    //   5759: if_icmpge -> 5786
    //   5762: aload_1
    //   5763: invokevirtual g : ()Ljava/lang/String;
    //   5766: astore #4
    //   5768: aload_2
    //   5769: getfield k : Ljava/util/List;
    //   5772: aload #4
    //   5774: invokeinterface add : (Ljava/lang/Object;)Z
    //   5779: pop
    //   5780: iinc #3, 1
    //   5783: goto -> 5756
    //   5786: aload_0
    //   5787: aload_2
    //   5788: putfield a : La/cd;
    //   5791: aload_0
    //   5792: dup
    //   5793: getfield a : La/cd;
    //   5796: invokevirtual a : (La/cd;)V
    //   5799: goto -> 14
    //   5802: aload_1
    //   5803: invokevirtual p : ()I
    //   5806: sipush #255
    //   5809: iand
    //   5810: istore #30
    //   5812: new java/util/ArrayList
    //   5815: dup
    //   5816: iload #30
    //   5818: invokespecial <init> : (I)V
    //   5821: astore #31
    //   5823: iconst_0
    //   5824: istore_2
    //   5825: iload_2
    //   5826: iload #30
    //   5828: if_icmpge -> 5849
    //   5831: aload #31
    //   5833: aload_1
    //   5834: invokevirtual g : ()Ljava/lang/String;
    //   5837: invokeinterface add : (Ljava/lang/Object;)Z
    //   5842: pop
    //   5843: iinc #2, 1
    //   5846: goto -> 5825
    //   5849: aload_0
    //   5850: getfield a : La/cd;
    //   5853: ifnonnull -> 5876
    //   5856: aload_0
    //   5857: new a/cd
    //   5860: dup
    //   5861: invokespecial <init> : ()V
    //   5864: putfield a : La/cd;
    //   5867: aload_0
    //   5868: getfield a : La/cd;
    //   5871: ldc ''
    //   5873: putfield H : Ljava/lang/String;
    //   5876: aload_0
    //   5877: getfield a : La/cd;
    //   5880: getfield l : Ljava/util/List;
    //   5883: invokeinterface clear : ()V
    //   5888: aload_0
    //   5889: getfield a : La/cd;
    //   5892: getfield l : Ljava/util/List;
    //   5895: aload #31
    //   5897: invokeinterface addAll : (Ljava/util/Collection;)Z
    //   5902: pop
    //   5903: aload_0
    //   5904: dup
    //   5905: getfield a : La/cd;
    //   5908: invokevirtual a : (La/cd;)V
    //   5911: goto -> 14
    //   5914: aload_0
    //   5915: invokevirtual K : ()V
    //   5918: goto -> 14
    //   5921: invokestatic nanoTime : ()J
    //   5924: lstore #30
    //   5926: aload_0
    //   5927: getfield e : La/cq;
    //   5930: invokevirtual j : ()I
    //   5933: istore_2
    //   5934: aload_0
    //   5935: getfield e : La/cq;
    //   5938: invokevirtual k : ()I
    //   5941: istore_3
    //   5942: aload_0
    //   5943: getfield e : La/cq;
    //   5946: invokevirtual l : ()I
    //   5949: istore #4
    //   5951: new a/be
    //   5954: dup
    //   5955: iload_2
    //   5956: iload_3
    //   5957: iload #4
    //   5959: invokespecial <init> : (III)V
    //   5962: astore #5
    //   5964: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   5967: aload_0
    //   5968: lload #30
    //   5970: aload #5
    //   5972: <illegal opcode> run : (La/br;JLa/be;)Ljava/lang/Runnable;
    //   5977: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   5982: aload_0
    //   5983: invokevirtual K : ()V
    //   5986: goto -> 14
    //   5989: aload_1
    //   5990: invokevirtual g : ()Ljava/lang/String;
    //   5993: astore #30
    //   5995: aload_1
    //   5996: invokevirtual p : ()I
    //   5999: sipush #255
    //   6002: iand
    //   6003: istore #31
    //   6005: aload_1
    //   6006: invokevirtual p : ()I
    //   6009: pop
    //   6010: aload_1
    //   6011: invokevirtual p : ()I
    //   6014: sipush #255
    //   6017: iand
    //   6018: istore_2
    //   6019: aload_1
    //   6020: invokevirtual p : ()I
    //   6023: sipush #255
    //   6026: iand
    //   6027: dup
    //   6028: istore_3
    //   6029: newarray int
    //   6031: astore #4
    //   6033: iconst_0
    //   6034: istore #5
    //   6036: iload #5
    //   6038: iload_3
    //   6039: if_icmpge -> 6060
    //   6042: aload #4
    //   6044: iload #5
    //   6046: aload_1
    //   6047: invokevirtual q : ()I
    //   6050: ldc 65535
    //   6052: iand
    //   6053: iastore
    //   6054: iinc #5, 1
    //   6057: goto -> 6036
    //   6060: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   6063: aload_0
    //   6064: aload #30
    //   6066: iload #31
    //   6068: iload_2
    //   6069: iload_3
    //   6070: aload #4
    //   6072: <illegal opcode> run : (La/br;Ljava/lang/String;III[I)Ljava/lang/Runnable;
    //   6077: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   6082: aload_0
    //   6083: invokevirtual F : ()V
    //   6086: goto -> 14
    //   6089: aload_1
    //   6090: invokevirtual p : ()I
    //   6093: sipush #255
    //   6096: iand
    //   6097: istore #30
    //   6099: aload_1
    //   6100: invokevirtual q : ()I
    //   6103: ldc 65535
    //   6105: iand
    //   6106: istore #31
    //   6108: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   6111: aload_0
    //   6112: iload #30
    //   6114: iload #31
    //   6116: <illegal opcode> run : (La/br;II)Ljava/lang/Runnable;
    //   6121: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   6126: goto -> 14
    //   6129: aload_1
    //   6130: invokevirtual p : ()I
    //   6133: sipush #255
    //   6136: iand
    //   6137: istore #30
    //   6139: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   6142: aload_0
    //   6143: iload #30
    //   6145: <illegal opcode> run : (La/br;I)Ljava/lang/Runnable;
    //   6150: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   6155: goto -> 14
    //   6158: aload_1
    //   6159: invokevirtual g : ()Ljava/lang/String;
    //   6162: astore #30
    //   6164: aload_0
    //   6165: aload #30
    //   6167: invokevirtual g : (Ljava/lang/String;)V
    //   6170: goto -> 14
    //   6173: aload_1
    //   6174: invokevirtual g : ()Ljava/lang/String;
    //   6177: astore #31
    //   6179: aload_0
    //   6180: aload #31
    //   6182: invokevirtual f : (Ljava/lang/String;)V
    //   6185: goto -> 14
    //   6188: iconst_m1
    //   6189: istore_2
    //   6190: aload_1
    //   6191: invokevirtual p : ()I
    //   6194: dup
    //   6195: istore_3
    //   6196: iconst_3
    //   6197: if_icmpne -> 6251
    //   6200: aload_1
    //   6201: invokevirtual p : ()I
    //   6204: sipush #255
    //   6207: iand
    //   6208: istore #4
    //   6210: aload_1
    //   6211: invokevirtual p : ()I
    //   6214: pop
    //   6215: aload_1
    //   6216: invokevirtual p : ()I
    //   6219: pop
    //   6220: iload #4
    //   6222: iconst_1
    //   6223: iand
    //   6224: ifeq -> 6248
    //   6227: iconst_0
    //   6228: istore #4
    //   6230: iload #4
    //   6232: bipush #23
    //   6234: if_icmpge -> 6248
    //   6237: aload_1
    //   6238: invokevirtual p : ()I
    //   6241: pop
    //   6242: iinc #4, 1
    //   6245: goto -> 6230
    //   6248: goto -> 6259
    //   6251: aload_1
    //   6252: invokevirtual q : ()I
    //   6255: ldc 65535
    //   6257: iand
    //   6258: istore_2
    //   6259: aload_1
    //   6260: invokevirtual g : ()Ljava/lang/String;
    //   6263: astore #4
    //   6265: aload_1
    //   6266: invokevirtual g : ()Ljava/lang/String;
    //   6269: astore #5
    //   6271: aload_1
    //   6272: invokevirtual g : ()Ljava/lang/String;
    //   6275: astore #6
    //   6277: aload_0
    //   6278: iload_2
    //   6279: iload_3
    //   6280: aload #4
    //   6282: aload #5
    //   6284: aload #6
    //   6286: invokevirtual a : (IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    //   6289: goto -> 14
    //   6292: aload_1
    //   6293: invokevirtual g : ()Ljava/lang/String;
    //   6296: astore #4
    //   6298: aload_1
    //   6299: invokevirtual p : ()I
    //   6302: sipush #255
    //   6305: iand
    //   6306: istore_2
    //   6307: aload_1
    //   6308: invokevirtual q : ()I
    //   6311: ldc 65535
    //   6313: iand
    //   6314: istore_3
    //   6315: aload_1
    //   6316: invokevirtual q : ()I
    //   6319: ldc 65535
    //   6321: iand
    //   6322: istore #5
    //   6324: aload_1
    //   6325: invokevirtual q : ()I
    //   6328: ldc 65535
    //   6330: iand
    //   6331: istore #6
    //   6333: aload_1
    //   6334: invokevirtual q : ()I
    //   6337: ldc 65535
    //   6339: iand
    //   6340: istore #7
    //   6342: aload_1
    //   6343: invokevirtual q : ()I
    //   6346: ldc 65535
    //   6348: iand
    //   6349: istore #8
    //   6351: aload_1
    //   6352: invokevirtual u : ()I
    //   6355: istore #9
    //   6357: aload_1
    //   6358: invokevirtual u : ()I
    //   6361: istore #10
    //   6363: aload_1
    //   6364: invokevirtual u : ()I
    //   6367: istore #11
    //   6369: aload_1
    //   6370: invokevirtual u : ()I
    //   6373: istore #12
    //   6375: aload_1
    //   6376: invokevirtual u : ()I
    //   6379: istore #13
    //   6381: new java/util/ArrayList
    //   6384: dup
    //   6385: iconst_4
    //   6386: invokespecial <init> : (I)V
    //   6389: astore #14
    //   6391: iconst_0
    //   6392: istore #15
    //   6394: iload #15
    //   6396: iconst_4
    //   6397: if_icmpge -> 6496
    //   6400: aload_1
    //   6401: invokevirtual p : ()I
    //   6404: sipush #255
    //   6407: iand
    //   6408: dup
    //   6409: istore #16
    //   6411: iconst_3
    //   6412: imul
    //   6413: newarray int
    //   6415: astore #17
    //   6417: iconst_0
    //   6418: istore #18
    //   6420: iload #18
    //   6422: iload #16
    //   6424: if_icmpge -> 6480
    //   6427: iload #18
    //   6429: iconst_3
    //   6430: imul
    //   6431: istore #19
    //   6433: aload #17
    //   6435: iload #19
    //   6437: aload_1
    //   6438: invokevirtual q : ()I
    //   6441: ldc 65535
    //   6443: iand
    //   6444: iastore
    //   6445: aload #17
    //   6447: iload #19
    //   6449: iconst_1
    //   6450: iadd
    //   6451: aload_1
    //   6452: invokevirtual p : ()I
    //   6455: sipush #255
    //   6458: iand
    //   6459: iastore
    //   6460: aload #17
    //   6462: iload #19
    //   6464: iconst_2
    //   6465: iadd
    //   6466: aload_1
    //   6467: invokevirtual q : ()I
    //   6470: ldc 65535
    //   6472: iand
    //   6473: iastore
    //   6474: iinc #18, 1
    //   6477: goto -> 6420
    //   6480: aload #14
    //   6482: aload #17
    //   6484: invokeinterface add : (Ljava/lang/Object;)Z
    //   6489: pop
    //   6490: iinc #15, 1
    //   6493: goto -> 6394
    //   6496: new java/util/ArrayList
    //   6499: dup
    //   6500: iconst_5
    //   6501: invokespecial <init> : (I)V
    //   6504: astore #15
    //   6506: iconst_0
    //   6507: istore #16
    //   6509: iload #16
    //   6511: iconst_5
    //   6512: if_icmpge -> 6593
    //   6515: aload_1
    //   6516: invokevirtual p : ()I
    //   6519: sipush #255
    //   6522: iand
    //   6523: dup
    //   6524: istore #17
    //   6526: iconst_2
    //   6527: imul
    //   6528: newarray int
    //   6530: astore #18
    //   6532: iconst_0
    //   6533: istore #19
    //   6535: iload #19
    //   6537: iload #17
    //   6539: if_icmpge -> 6577
    //   6542: iload #19
    //   6544: iconst_2
    //   6545: imul
    //   6546: istore #20
    //   6548: aload #18
    //   6550: iload #20
    //   6552: aload_1
    //   6553: invokevirtual q : ()I
    //   6556: ldc 65535
    //   6558: iand
    //   6559: iastore
    //   6560: aload #18
    //   6562: iload #20
    //   6564: iconst_1
    //   6565: iadd
    //   6566: aload_1
    //   6567: invokevirtual r : ()I
    //   6570: iastore
    //   6571: iinc #19, 1
    //   6574: goto -> 6535
    //   6577: aload #15
    //   6579: aload #18
    //   6581: invokeinterface add : (Ljava/lang/Object;)Z
    //   6586: pop
    //   6587: iinc #16, 1
    //   6590: goto -> 6509
    //   6593: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   6596: aload_0
    //   6597: aload #4
    //   6599: iload_2
    //   6600: iload_3
    //   6601: iload #6
    //   6603: iload #5
    //   6605: iload #7
    //   6607: iload #8
    //   6609: iload #10
    //   6611: iload #9
    //   6613: iload #11
    //   6615: iload #12
    //   6617: iload #13
    //   6619: aload #14
    //   6621: aload #15
    //   6623: <illegal opcode> run : (La/br;Ljava/lang/String;IIIIIIIIIIILjava/util/List;Ljava/util/List;)Ljava/lang/Runnable;
    //   6628: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   6633: aload_0
    //   6634: invokevirtual F : ()V
    //   6637: goto -> 14
    //   6640: aload_1
    //   6641: invokevirtual g : ()Ljava/lang/String;
    //   6644: pop
    //   6645: goto -> 14
    //   6648: aload_1
    //   6649: invokevirtual p : ()I
    //   6652: pop
    //   6653: aload_0
    //   6654: invokevirtual F : ()V
    //   6657: goto -> 14
    //   6660: aload_1
    //   6661: invokevirtual q : ()I
    //   6664: ldc 65535
    //   6666: iand
    //   6667: istore #4
    //   6669: aload_1
    //   6670: invokevirtual q : ()I
    //   6673: ldc 65535
    //   6675: iand
    //   6676: istore_2
    //   6677: aload_1
    //   6678: invokevirtual p : ()I
    //   6681: sipush #255
    //   6684: iand
    //   6685: istore_3
    //   6686: aload_1
    //   6687: invokevirtual g : ()Ljava/lang/String;
    //   6690: astore #5
    //   6692: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   6695: aload_0
    //   6696: iload #4
    //   6698: iload_2
    //   6699: iload_3
    //   6700: aload #5
    //   6702: <illegal opcode> run : (La/br;IIILjava/lang/String;)Ljava/lang/Runnable;
    //   6707: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   6712: goto -> 14
    //   6715: aload_1
    //   6716: invokevirtual p : ()I
    //   6719: pop
    //   6720: goto -> 14
    //   6723: aload_1
    //   6724: invokevirtual p : ()I
    //   6727: sipush #255
    //   6730: iand
    //   6731: istore #4
    //   6733: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   6736: iload #4
    //   6738: <illegal opcode> run : (I)Ljava/lang/Runnable;
    //   6743: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   6748: goto -> 14
    //   6751: aload_1
    //   6752: invokevirtual p : ()I
    //   6755: sipush #255
    //   6758: iand
    //   6759: istore #4
    //   6761: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   6764: iload #4
    //   6766: <illegal opcode> run : (I)Ljava/lang/Runnable;
    //   6771: invokeinterface postRunnable : (Ljava/lang/Runnable;)V
    //   6776: goto -> 14
    //   6779: aload_1
    //   6780: invokevirtual g : ()Ljava/lang/String;
    //   6783: astore #4
    //   6785: aload_0
    //   6786: getfield a : La/bd;
    //   6789: ifnull -> 6942
    //   6792: aload_0
    //   6793: getfield a : La/bd;
    //   6796: aload #4
    //   6798: invokeinterface d : (Ljava/lang/String;)V
    //   6803: goto -> 14
    //   6806: aload_1
    //   6807: invokevirtual g : ()Ljava/lang/String;
    //   6810: pop
    //   6811: goto -> 14
    //   6814: aload_1
    //   6815: invokevirtual p : ()I
    //   6818: sipush #255
    //   6821: iand
    //   6822: istore_2
    //   6823: aload_1
    //   6824: invokevirtual q : ()I
    //   6827: ldc 65535
    //   6829: iand
    //   6830: istore_3
    //   6831: aload_0
    //   6832: getfield a : La/bj;
    //   6835: ifnull -> 6942
    //   6838: aload_0
    //   6839: getfield a : La/bj;
    //   6842: iload_2
    //   6843: iload_3
    //   6844: invokeinterface f : (II)V
    //   6849: goto -> 14
    //   6852: aload_1
    //   6853: aload_0
    //   6854: getfield e : La/cq;
    //   6857: invokevirtual i : ()I
    //   6860: aload_0
    //   6861: getfield e : La/cq;
    //   6864: getfield R : Z
    //   6867: invokevirtual a : (IZ)I
    //   6870: istore #5
    //   6872: aload_1
    //   6873: aload_0
    //   6874: getfield e : La/cq;
    //   6877: invokevirtual i : ()I
    //   6880: aload_0
    //   6881: getfield e : La/cq;
    //   6884: getfield R : Z
    //   6887: invokevirtual a : (IZ)I
    //   6890: istore #6
    //   6892: aload_1
    //   6893: invokevirtual p : ()I
    //   6896: sipush #255
    //   6899: iand
    //   6900: istore #7
    //   6902: aload_0
    //   6903: getfield a : La/bj;
    //   6906: ifnull -> 6942
    //   6909: aload_0
    //   6910: getfield a : La/bj;
    //   6913: iload #5
    //   6915: iload #6
    //   6917: iload #7
    //   6919: invokeinterface c : (III)V
    //   6924: goto -> 14
    //   6927: getstatic java/lang/System.out : Ljava/io/PrintStream;
    //   6930: iload_2
    //   6931: invokestatic toHexString : (I)Ljava/lang/String;
    //   6934: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;)Ljava/lang/String;
    //   6939: invokevirtual println : (Ljava/lang/String;)V
    //   6942: goto -> 14
    //   6945: return
    // Exception table:
    //   from	to	target	type
    //   1061	1428	1431	java/lang/Exception
    //   1437	1463	1466	java/io/IOException
    //   2753	2940	2943	java/lang/Exception
    //   3341	3365	3368	java/io/IOException
    //   3526	3654	3657	java/lang/Exception
  }
  
  private cg a(bv parambv, short[] paramArrayOfshort, int paramInt1, int paramInt2, int paramInt3) {
    cg cg = new cg(paramInt1, paramInt2, paramInt3);
    while (true) {
      paramInt2 = a(parambv, paramArrayOfshort);
      paramInt3 = paramInt2;
      paramInt3 = ((im)this.a).a[paramInt3];
      this.a.am(paramInt2);
      if (paramInt3 != 0) {
        cg.a(paramInt3);
        continue;
      } 
      return cg;
    } 
  }
  
  private void a(ks paramks, int paramInt) {
    try {
      int k;
      int m;
      int i7;
      int i8;
      bv bv = new bv(paramks);
      short[] arrayOfShort = ((im)this.a).b;
      int i = 0;
      int j = 0;
      switch (paramInt) {
        case 101:
          k = this.e.bV;
          m = 1;
          break;
        case 102:
          i = this.e.bV - 1;
          k = 1;
          m = this.e.bW;
          break;
        case 103:
          j = this.e.bW - 1;
          k = this.e.bV;
          m = 1;
          break;
        case 104:
          k = 1;
          m = this.e.bW;
          break;
        default:
          throw new IllegalArgumentException("Diredesconhecida: " + paramInt);
      } 
      int n = this.e.aD - d();
      int i1 = this.e.aE - e();
      int i2 = this.e.aF;
      HashMap<Object, Object> hashMap = new HashMap<>();
      int i3;
      for (i3 = 0; i3 < m; i3++) {
        for (byte b = 0; b < k; b++) {
          int i9 = i + b;
          int i10 = j + i3;
          cg cg = a(bv, arrayOfShort, i9, i10, i2);
          be be = new be(n + i9, i1 + i10, i2);
          this.v.put(be, cg);
          hashMap.put(be, cg);
        } 
      } 
      bv.ac();
      i3 = this.e.aD - d();
      int i4 = this.e.aD + f();
      int i5 = this.e.aE - e();
      int i6 = this.e.aE + g();
      switch (paramInt) {
        case 101:
          i7 = i6 + 1;
          for (i8 = i3; i8 <= i4; i8++)
            this.v.remove(new be(i8, i7, i2)); 
          break;
        case 102:
          i7 = i3 - 1;
          for (i8 = i5; i8 <= i6; i8++)
            this.v.remove(new be(i7, i8, i2)); 
          break;
        case 103:
          i7 = i5 - 1;
          for (i8 = i3; i8 <= i4; i8++)
            this.v.remove(new be(i8, i7, i2)); 
          break;
        case 104:
          i7 = i4 + 1;
          for (i8 = i5; i8 <= i6; i8++)
            this.v.remove(new be(i7, i8, i2)); 
          break;
      } 
      if (this.v.size() > this.e.bV * this.e.bW * 2)
        this.v.keySet().removeIf(parambe -> (parambe.aF != paramInt1 || parambe.aD < paramInt2 || parambe.aD > paramInt3 || parambe.aE < paramInt4 || parambe.aE > paramInt5)); 
      if (this.a != null && !hashMap.isEmpty())
        this.a.a(hashMap); 
      return;
    } catch (Exception exception) {
      null.printStackTrace();
      return;
    } 
  }
  
  private static int a(bv parambv, short[] paramArrayOfshort) {
    int i = 0;
    while (true) {
      int j;
      if ((j = parambv.h()) == -1)
        throw new Exception("Fim inesperado do fluxo"); 
      i = (-i << 1) + j;
      if ((i = paramArrayOfshort[i]) >= 0)
        return i; 
    } 
  }
  
  public final void N() {
    if (this.F)
      return; 
    this.F = true;
    try {
      if (this.b != null && !this.b.isClosed())
        this.b.shutdownInput(); 
    } catch (Exception exception) {}
    try {
      if (this.b != null && !this.b.isClosed())
        this.b.shutdownOutput(); 
    } catch (Exception exception) {}
    try {
      if (this.a != null)
        this.a.close(); 
    } catch (Exception exception) {}
    try {
      if (this.a != null)
        this.a.close(); 
    } catch (Exception exception) {}
    try {
      if (this.a != null)
        this.a.close(); 
    } catch (Exception exception) {}
    try {
      if (this.b != null)
        this.b.close(); 
    } catch (Exception exception) {}
    try {
      if (this.b != null)
        this.b.close(); 
    } catch (Exception exception) {}
    try {
      if (this.b != null)
        this.b.close(); 
    } catch (Exception exception) {}
    if (this.b != null && this.b != Thread.currentThread())
      try {
        this.b.join(200L);
      } catch (InterruptedException interruptedException) {} 
    al.p();
    this.v.clear();
    if (this.a != null)
      this.a.a(new HashMap<>()); 
    if (this.a != null)
      this.a.a(new int[16]); 
    try {
      this.a.cc();
    } catch (Throwable throwable) {}
    br br1;
    long l;
    boolean bool = ((br1 = this).H && (l = System.nanoTime() - br1.j) >= 0L && l <= 2000000000L) ? true : false;
    if (this.a != null && !bool)
      this.a.onDisconnected(); 
    if (kx.g != null) {
      kx.g.remove();
      kx.g = null;
    } 
    if (lb.g != null) {
      lb.g.remove();
      lb.g = null;
    } 
    this.b = null;
    this.a = null;
    this.a = null;
    this.a = null;
    this.b = null;
    this.b = null;
    this.b = null;
    this.F = false;
    K();
    J();
  }
  
  private int d() {
    return this.e.bV / 2;
  }
  
  private int e() {
    return this.e.bW / 2;
  }
  
  private int f() {
    return this.e.bV - 1 - d();
  }
  
  private int g() {
    return this.e.bW - 1 - e();
  }
  
  private be a(int paramInt) {
    int i = this.e.bV;
    int j = paramInt % i;
    paramInt /= i;
    i = d();
    int k = e();
    i = this.e.aD - i + j;
    paramInt = this.e.aE - k + paramInt;
    return new be(i, paramInt, this.e.aF);
  }
  
  private void a(int paramInt1, int paramInt2, String paramString1, String paramString2, String paramString3) {
    Gdx.app.postRunnable(() -> {
          Screen screen;
          if (screen = this.b.getScreen() instanceof fj)
            kt.a((Stage)((fj)screen).i, paramInt1, paramInt2, paramString1, paramString2, paramString3, this.e); 
        });
  }
  
  private void f(String paramString) {
    Gdx.app.postRunnable(() -> {
          Screen screen;
          if (screen = this.b.getScreen() instanceof fj)
            kx.a((Stage)((fj)screen).i, paramString); 
        });
  }
  
  public final void g(String paramString) {
    Gdx.app.postRunnable(() -> {
          Screen screen;
          if (screen = this.b.getScreen() instanceof fj)
            lb.a((Stage)((fj)screen).i, paramString); 
        });
  }
  
  private static int c(int paramInt) {
    switch (paramInt) {
      case 1:
        return 1;
      case 2:
        return 2;
    } 
    return 0;
  }
  
  private static boolean b(int paramInt) {
    return (paramInt >= 48 && paramInt <= 57);
  }
  
  private static boolean a(bx parambx) {
    if (parambx == null || parambx.i == null)
      return false; 
    Iterator<by> iterator = parambx.i.iterator();
    while (iterator.hasNext()) {
      by by;
      if ((by = iterator.next()).bo != 45 && b(by.bo) && !by.I)
        return true; 
    } 
    return false;
  }
  
  private void a(bx parambx) {
    if (parambx == null)
      return; 
    HashSet<Integer> hashSet1 = new HashSet();
    for (cc cc : parambx.h)
      hashSet1.add(Integer.valueOf(cc.d)); 
    HashSet<Integer> hashSet2 = new HashSet();
    Iterator<by> iterator = parambx.i.iterator();
    while (iterator.hasNext()) {
      by by;
      if ((by = iterator.next()).I)
        hashSet2.add(Integer.valueOf(by.d)); 
    } 
    boolean bool2;
    boolean bool3 = ((bool2 = !hashSet2.isEmpty() ? true : false) && hashSet2.containsAll(hashSet1)) ? true : false;
    boolean bool1 = (bool2 && !bool3) ? true : false;
    boolean bool = a(parambx);
    Gdx.app.postRunnable(() -> {
          // Byte code:
          //   0: aload_0
          //   1: getfield b : La/cr;
          //   4: invokevirtual getScreen : ()Lcom/badlogic/gdx/Screen;
          //   7: dup
          //   8: astore #4
          //   10: instanceof a/fj
          //   13: ifne -> 17
          //   16: return
          //   17: aload_0
          //   18: getfield e : La/cq;
          //   21: invokestatic a : (La/cq;)La/jm;
          //   24: aload_1
          //   25: getfield w : Ljava/lang/String;
          //   28: ifnull -> 38
          //   31: aload_1
          //   32: getfield w : Ljava/lang/String;
          //   35: goto -> 40
          //   38: ldc 'Menu'
          //   40: astore #6
          //   42: dup
          //   43: astore #7
          //   45: aload #6
          //   47: putfield w : Ljava/lang/String;
          //   50: aload #7
          //   52: dup
          //   53: astore #11
          //   55: iload_2
          //   56: putfield bo : Z
          //   59: aload #11
          //   61: aload_0
          //   62: aload_1
          //   63: <illegal opcode> run : (La/br;La/bx;)Ljava/lang/Runnable;
          //   68: astore #6
          //   70: dup
          //   71: astore #7
          //   73: aload #6
          //   75: putfield h : Ljava/lang/Runnable;
          //   78: aload #7
          //   80: astore #5
          //   82: aload_1
          //   83: getfield a : La/cb;
          //   86: ifnull -> 253
          //   89: aload_1
          //   90: getfield a : La/cb;
          //   93: getfield bq : I
          //   96: istore #6
          //   98: aload_1
          //   99: getfield a : La/cb;
          //   102: getfield al : I
          //   105: bipush #12
          //   107: if_icmpne -> 114
          //   110: iconst_1
          //   111: goto -> 115
          //   114: iconst_0
          //   115: istore #7
          //   117: aload_1
          //   118: getfield a : La/cb;
          //   121: getfield al : I
          //   124: bipush #9
          //   126: if_icmpne -> 133
          //   129: iconst_1
          //   130: goto -> 134
          //   133: iconst_0
          //   134: istore #8
          //   136: aload #5
          //   138: aload_1
          //   139: getfield a : La/cb;
          //   142: getfield C : Ljava/lang/String;
          //   145: ifnull -> 158
          //   148: aload_1
          //   149: getfield a : La/cb;
          //   152: getfield C : Ljava/lang/String;
          //   155: goto -> 160
          //   158: ldc ''
          //   160: iload #6
          //   162: iconst_0
          //   163: aload_1
          //   164: getfield a : La/cb;
          //   167: getfield bp : I
          //   170: invokestatic max : (II)I
          //   173: iload #7
          //   175: iload #8
          //   177: aload_1
          //   178: getfield a : La/cb;
          //   181: getfield D : Ljava/lang/String;
          //   184: ifnull -> 197
          //   187: aload_1
          //   188: getfield a : La/cb;
          //   191: getfield D : Ljava/lang/String;
          //   194: goto -> 199
          //   197: ldc ''
          //   199: aload_0
          //   200: iload #7
          //   202: aload_1
          //   203: iload #6
          //   205: <illegal opcode> run : (La/br;ZLa/bx;I)Ljava/lang/Runnable;
          //   210: astore #17
          //   212: astore #16
          //   214: istore #15
          //   216: istore #14
          //   218: istore #13
          //   220: istore #8
          //   222: astore #12
          //   224: new a/jq
          //   227: dup
          //   228: aload #12
          //   230: iload #8
          //   232: iload #13
          //   234: iload #14
          //   236: iload #15
          //   238: aload #16
          //   240: aload #17
          //   242: ldc 'Ok'
          //   244: aconst_null
          //   245: aconst_null
          //   246: iconst_1
          //   247: invokespecial <init> : (Ljava/lang/String;IIZZLjava/lang/String;Ljava/lang/Runnable;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Runnable;Z)V
          //   250: putfield a : La/jq;
          //   253: aload_1
          //   254: getfield x : Ljava/lang/String;
          //   257: ifnonnull -> 274
          //   260: aload_1
          //   261: getfield y : Ljava/lang/String;
          //   264: ifnonnull -> 274
          //   267: aload_1
          //   268: getfield z : Ljava/lang/String;
          //   271: ifnull -> 322
          //   274: aload #5
          //   276: aload_1
          //   277: getfield x : Ljava/lang/String;
          //   280: ifnull -> 290
          //   283: aload_1
          //   284: getfield x : Ljava/lang/String;
          //   287: goto -> 292
          //   290: ldc ''
          //   292: aload_1
          //   293: getfield y : Ljava/lang/String;
          //   296: aload_1
          //   297: getfield z : Ljava/lang/String;
          //   300: astore #13
          //   302: astore #8
          //   304: astore #12
          //   306: new a/jx
          //   309: dup
          //   310: aload #12
          //   312: aload #8
          //   314: aload #13
          //   316: invokespecial <init> : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
          //   319: putfield a : La/jx;
          //   322: aload_1
          //   323: getfield A : Ljava/lang/String;
          //   326: ifnull -> 348
          //   329: aload_1
          //   330: getfield A : Ljava/lang/String;
          //   333: invokevirtual isEmpty : ()Z
          //   336: ifne -> 348
          //   339: aload #5
          //   341: aload_1
          //   342: getfield A : Ljava/lang/String;
          //   345: putfield at : Ljava/lang/String;
          //   348: aload_1
          //   349: getfield g : Ljava/util/List;
          //   352: ifnull -> 452
          //   355: aload_1
          //   356: getfield g : Ljava/util/List;
          //   359: invokeinterface isEmpty : ()Z
          //   364: ifne -> 452
          //   367: aload_1
          //   368: getfield g : Ljava/util/List;
          //   371: invokeinterface iterator : ()Ljava/util/Iterator;
          //   376: astore #6
          //   378: aload #6
          //   380: invokeinterface hasNext : ()Z
          //   385: ifeq -> 452
          //   388: aload #6
          //   390: invokeinterface next : ()Ljava/lang/Object;
          //   395: checkcast a/ca
          //   398: astore #7
          //   400: aload #5
          //   402: aload #7
          //   404: getfield B : Ljava/lang/String;
          //   407: ifnull -> 418
          //   410: aload #7
          //   412: getfield B : Ljava/lang/String;
          //   415: goto -> 420
          //   418: ldc ''
          //   420: aload #7
          //   422: getfield al : I
          //   425: istore #8
          //   427: astore #12
          //   429: getfield E : Ljava/util/List;
          //   432: new a/jl
          //   435: dup
          //   436: aload #12
          //   438: iload #8
          //   440: invokespecial <init> : (Ljava/lang/String;I)V
          //   443: invokeinterface add : (Ljava/lang/Object;)Z
          //   448: pop
          //   449: goto -> 378
          //   452: aload_1
          //   453: getfield j : Ljava/util/List;
          //   456: invokeinterface iterator : ()Ljava/util/Iterator;
          //   461: astore #6
          //   463: aload #6
          //   465: invokeinterface hasNext : ()Z
          //   470: ifeq -> 537
          //   473: aload #6
          //   475: invokeinterface next : ()Ljava/lang/Object;
          //   480: checkcast a/bz
          //   483: astore #7
          //   485: aload #5
          //   487: aload #7
          //   489: getfield B : Ljava/lang/String;
          //   492: ifnull -> 503
          //   495: aload #7
          //   497: getfield B : Ljava/lang/String;
          //   500: goto -> 505
          //   503: ldc ''
          //   505: aload #7
          //   507: getfield al : I
          //   510: istore #8
          //   512: astore #12
          //   514: getfield D : Ljava/util/List;
          //   517: new a/jl
          //   520: dup
          //   521: aload #12
          //   523: iload #8
          //   525: invokespecial <init> : (Ljava/lang/String;I)V
          //   528: invokeinterface add : (Ljava/lang/Object;)Z
          //   533: pop
          //   534: goto -> 463
          //   537: aload_1
          //   538: getfield a : Ljava/lang/Integer;
          //   541: ifnull -> 571
          //   544: aload_1
          //   545: getfield a : Ljava/lang/Integer;
          //   548: invokevirtual intValue : ()I
          //   551: sipush #255
          //   554: iand
          //   555: istore #6
          //   557: aload #5
          //   559: aload_0
          //   560: aload_1
          //   561: iload #6
          //   563: <illegal opcode> run : (La/br;La/bx;I)Ljava/lang/Runnable;
          //   568: putfield g : Ljava/lang/Runnable;
          //   571: aload_1
          //   572: getfield h : Ljava/util/List;
          //   575: invokeinterface iterator : ()Ljava/util/Iterator;
          //   580: astore #6
          //   582: aload #6
          //   584: invokeinterface hasNext : ()Z
          //   589: ifeq -> 1327
          //   592: aload #6
          //   594: invokeinterface next : ()Ljava/lang/Object;
          //   599: checkcast a/cc
          //   602: astore #7
          //   604: iconst_0
          //   605: istore #8
          //   607: aload #7
          //   609: getfield a : La/jn;
          //   612: ifnull -> 690
          //   615: aload #7
          //   617: getfield a : La/jn;
          //   620: getfield aN : I
          //   623: invokestatic i : (I)Z
          //   626: istore #9
          //   628: aload #7
          //   630: getfield a : La/jn;
          //   633: getfield ao : I
          //   636: aload #7
          //   638: getfield a : La/jn;
          //   641: getfield ap : I
          //   644: ior
          //   645: aload #7
          //   647: getfield a : La/jn;
          //   650: getfield aq : I
          //   653: ior
          //   654: aload #7
          //   656: getfield a : La/jn;
          //   659: getfield ar : I
          //   662: ior
          //   663: ifeq -> 670
          //   666: iconst_1
          //   667: goto -> 671
          //   670: iconst_0
          //   671: istore #10
          //   673: iload #9
          //   675: ifne -> 687
          //   678: iload #10
          //   680: ifeq -> 687
          //   683: iconst_1
          //   684: goto -> 688
          //   687: iconst_0
          //   688: istore #8
          //   690: aload #7
          //   692: getfield b : Ljava/lang/Integer;
          //   695: ifnull -> 721
          //   698: aload #7
          //   700: getfield c : Ljava/lang/Integer;
          //   703: ifnull -> 721
          //   706: aload #7
          //   708: getfield c : Ljava/lang/Integer;
          //   711: invokevirtual intValue : ()I
          //   714: ifle -> 721
          //   717: iconst_1
          //   718: goto -> 722
          //   721: iconst_0
          //   722: istore #9
          //   724: iload #8
          //   726: ifne -> 734
          //   729: iload #9
          //   731: ifeq -> 738
          //   734: iconst_1
          //   735: goto -> 739
          //   738: iconst_0
          //   739: istore #10
          //   741: aload_1
          //   742: aload #7
          //   744: getfield d : I
          //   747: istore #12
          //   749: dup
          //   750: astore #11
          //   752: ifnull -> 763
          //   755: aload #11
          //   757: getfield i : Ljava/util/List;
          //   760: ifnonnull -> 767
          //   763: iconst_0
          //   764: goto -> 944
          //   767: iload_2
          //   768: ifeq -> 864
          //   771: aload #11
          //   773: dup
          //   774: astore #15
          //   776: ifnull -> 787
          //   779: aload #15
          //   781: getfield i : Ljava/util/List;
          //   784: ifnonnull -> 791
          //   787: iconst_0
          //   788: goto -> 944
          //   791: aload #15
          //   793: getfield i : Ljava/util/List;
          //   796: invokeinterface iterator : ()Ljava/util/Iterator;
          //   801: astore #16
          //   803: aload #16
          //   805: invokeinterface hasNext : ()Z
          //   810: ifeq -> 860
          //   813: aload #16
          //   815: invokeinterface next : ()Ljava/lang/Object;
          //   820: checkcast a/by
          //   823: dup
          //   824: astore #17
          //   826: getfield bo : I
          //   829: bipush #45
          //   831: if_icmpeq -> 803
          //   834: aload #17
          //   836: getfield bo : I
          //   839: invokestatic b : (I)Z
          //   842: ifeq -> 803
          //   845: aload #17
          //   847: getfield I : Z
          //   850: ifeq -> 857
          //   853: iconst_1
          //   854: goto -> 944
          //   857: goto -> 803
          //   860: iconst_0
          //   861: goto -> 944
          //   864: aload #11
          //   866: getfield i : Ljava/util/List;
          //   869: invokeinterface iterator : ()Ljava/util/Iterator;
          //   874: astore #13
          //   876: aload #13
          //   878: invokeinterface hasNext : ()Z
          //   883: ifeq -> 943
          //   886: aload #13
          //   888: invokeinterface next : ()Ljava/lang/Object;
          //   893: checkcast a/by
          //   896: dup
          //   897: astore #14
          //   899: getfield bo : I
          //   902: bipush #45
          //   904: if_icmpeq -> 876
          //   907: aload #14
          //   909: getfield bo : I
          //   912: invokestatic b : (I)Z
          //   915: ifeq -> 876
          //   918: aload #14
          //   920: getfield I : Z
          //   923: ifeq -> 940
          //   926: aload #14
          //   928: getfield d : I
          //   931: iload #12
          //   933: if_icmpne -> 940
          //   936: iconst_1
          //   937: goto -> 944
          //   940: goto -> 876
          //   943: iconst_0
          //   944: istore #11
          //   946: iload_3
          //   947: ifne -> 959
          //   950: iload #11
          //   952: ifne -> 959
          //   955: iconst_1
          //   956: goto -> 960
          //   959: iconst_0
          //   960: ifeq -> 980
          //   963: iload #10
          //   965: ifeq -> 980
          //   968: aload_0
          //   969: aload_1
          //   970: aload #7
          //   972: <illegal opcode> run : (La/br;La/bx;La/cc;)Ljava/lang/Runnable;
          //   977: goto -> 981
          //   980: aconst_null
          //   981: astore #10
          //   983: iload #8
          //   985: ifeq -> 1097
          //   988: aload #5
          //   990: aload #7
          //   992: getfield d : I
          //   995: aload #7
          //   997: getfield al : I
          //   1000: aload #7
          //   1002: getfield E : Ljava/lang/String;
          //   1005: ifnull -> 1016
          //   1008: aload #7
          //   1010: getfield E : Ljava/lang/String;
          //   1013: goto -> 1018
          //   1016: ldc ''
          //   1018: aload #7
          //   1020: getfield F : Ljava/lang/String;
          //   1023: aload #7
          //   1025: getfield G : Ljava/lang/String;
          //   1028: aload #7
          //   1030: getfield a : La/jn;
          //   1033: aload #10
          //   1035: astore #17
          //   1037: astore #16
          //   1039: astore #15
          //   1041: astore #14
          //   1043: astore #13
          //   1045: istore #8
          //   1047: istore #12
          //   1049: astore #11
          //   1051: new a/jr
          //   1054: dup
          //   1055: iload #12
          //   1057: iload #8
          //   1059: aload #13
          //   1061: aload #14
          //   1063: aload #15
          //   1065: aload #17
          //   1067: aload #16
          //   1069: invokespecial <init> : (IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Runnable;La/jn;)V
          //   1072: astore #7
          //   1074: aload #11
          //   1076: aload #7
          //   1078: invokevirtual c : (La/jr;)V
          //   1081: aload #11
          //   1083: getfield B : Ljava/util/List;
          //   1086: aload #7
          //   1088: invokeinterface add : (Ljava/lang/Object;)Z
          //   1093: pop
          //   1094: goto -> 582
          //   1097: iload #9
          //   1099: ifeq -> 1226
          //   1102: aload #5
          //   1104: aload #7
          //   1106: getfield d : I
          //   1109: aload #7
          //   1111: getfield al : I
          //   1114: aload #7
          //   1116: getfield E : Ljava/lang/String;
          //   1119: ifnull -> 1130
          //   1122: aload #7
          //   1124: getfield E : Ljava/lang/String;
          //   1127: goto -> 1132
          //   1130: ldc ''
          //   1132: aload #7
          //   1134: getfield F : Ljava/lang/String;
          //   1137: aload #7
          //   1139: getfield G : Ljava/lang/String;
          //   1142: aload #7
          //   1144: getfield b : Ljava/lang/Integer;
          //   1147: invokevirtual intValue : ()I
          //   1150: aload #7
          //   1152: getfield c : Ljava/lang/Integer;
          //   1155: invokevirtual intValue : ()I
          //   1158: aload #10
          //   1160: astore #7
          //   1162: istore #17
          //   1164: istore #16
          //   1166: astore #15
          //   1168: astore #14
          //   1170: astore #13
          //   1172: istore #8
          //   1174: istore #12
          //   1176: astore #11
          //   1178: new a/jr
          //   1181: dup
          //   1182: iload #12
          //   1184: iload #8
          //   1186: aload #13
          //   1188: aload #14
          //   1190: aload #15
          //   1192: aload #7
          //   1194: iload #16
          //   1196: iload #17
          //   1198: invokespecial <init> : (IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Runnable;II)V
          //   1201: astore #7
          //   1203: aload #11
          //   1205: aload #7
          //   1207: invokevirtual c : (La/jr;)V
          //   1210: aload #11
          //   1212: getfield B : Ljava/util/List;
          //   1215: aload #7
          //   1217: invokeinterface add : (Ljava/lang/Object;)Z
          //   1222: pop
          //   1223: goto -> 582
          //   1226: aload #5
          //   1228: aload #7
          //   1230: getfield d : I
          //   1233: aload #7
          //   1235: getfield al : I
          //   1238: aload #7
          //   1240: getfield E : Ljava/lang/String;
          //   1243: ifnull -> 1254
          //   1246: aload #7
          //   1248: getfield E : Ljava/lang/String;
          //   1251: goto -> 1256
          //   1254: ldc ''
          //   1256: aload #7
          //   1258: getfield F : Ljava/lang/String;
          //   1261: aload #7
          //   1263: getfield G : Ljava/lang/String;
          //   1266: aload #10
          //   1268: astore #16
          //   1270: astore #15
          //   1272: astore #14
          //   1274: astore #13
          //   1276: istore #8
          //   1278: istore #12
          //   1280: astore #11
          //   1282: new a/jr
          //   1285: dup
          //   1286: iload #12
          //   1288: iload #8
          //   1290: aload #13
          //   1292: aload #14
          //   1294: aload #15
          //   1296: aload #16
          //   1298: iconst_1
          //   1299: invokespecial <init> : (IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Runnable;Z)V
          //   1302: astore #17
          //   1304: aload #11
          //   1306: aload #17
          //   1308: invokevirtual c : (La/jr;)V
          //   1311: aload #11
          //   1313: getfield B : Ljava/util/List;
          //   1316: aload #17
          //   1318: invokeinterface add : (Ljava/lang/Object;)Z
          //   1323: pop
          //   1324: goto -> 582
          //   1327: aload_1
          //   1328: getfield i : Ljava/util/List;
          //   1331: invokeinterface iterator : ()Ljava/util/Iterator;
          //   1336: astore #6
          //   1338: aload #6
          //   1340: invokeinterface hasNext : ()Z
          //   1345: ifeq -> 1606
          //   1348: aload #6
          //   1350: invokeinterface next : ()Ljava/lang/Object;
          //   1355: checkcast a/by
          //   1358: dup
          //   1359: astore #7
          //   1361: getfield bo : I
          //   1364: bipush #45
          //   1366: if_icmpeq -> 1338
          //   1369: aload #7
          //   1371: getfield bo : I
          //   1374: invokestatic b : (I)Z
          //   1377: ifeq -> 1338
          //   1380: aconst_null
          //   1381: astore #8
          //   1383: aload #7
          //   1385: getfield bo : I
          //   1388: bipush #48
          //   1390: if_icmplt -> 1414
          //   1393: aload #7
          //   1395: getfield bo : I
          //   1398: bipush #57
          //   1400: if_icmpgt -> 1414
          //   1403: aload #7
          //   1405: getfield bo : I
          //   1408: i2c
          //   1409: invokestatic valueOf : (C)Ljava/lang/String;
          //   1412: astore #8
          //   1414: aload #7
          //   1416: getfield I : Z
          //   1419: ifne -> 1514
          //   1422: aload_0
          //   1423: aload #7
          //   1425: aload_1
          //   1426: <illegal opcode> run : (La/br;La/by;La/bx;)Ljava/lang/Runnable;
          //   1431: astore #9
          //   1433: aload #5
          //   1435: aload #7
          //   1437: getfield d : I
          //   1440: aload #7
          //   1442: getfield B : Ljava/lang/String;
          //   1445: ifnull -> 1456
          //   1448: aload #7
          //   1450: getfield B : Ljava/lang/String;
          //   1453: goto -> 1458
          //   1456: ldc ''
          //   1458: aload #8
          //   1460: aload #9
          //   1462: astore #14
          //   1464: astore #13
          //   1466: astore #8
          //   1468: istore #12
          //   1470: astore #11
          //   1472: new a/jk
          //   1475: dup
          //   1476: iload #12
          //   1478: aload #8
          //   1480: iconst_0
          //   1481: aload #14
          //   1483: iconst_1
          //   1484: aload #13
          //   1486: invokespecial <init> : (ILjava/lang/String;ZLjava/lang/Runnable;ZLjava/lang/String;)V
          //   1489: astore #15
          //   1491: aload #11
          //   1493: aload #15
          //   1495: invokevirtual b : (La/jk;)V
          //   1498: aload #11
          //   1500: getfield C : Ljava/util/List;
          //   1503: aload #15
          //   1505: invokeinterface add : (Ljava/lang/Object;)Z
          //   1510: pop
          //   1511: goto -> 1338
          //   1514: aload_0
          //   1515: aload #7
          //   1517: aload_1
          //   1518: <illegal opcode> run : (La/br;La/by;La/bx;)Ljava/lang/Runnable;
          //   1523: astore #9
          //   1525: aload #5
          //   1527: aload #7
          //   1529: getfield d : I
          //   1532: aload #7
          //   1534: getfield B : Ljava/lang/String;
          //   1537: ifnull -> 1548
          //   1540: aload #7
          //   1542: getfield B : Ljava/lang/String;
          //   1545: goto -> 1550
          //   1548: ldc ''
          //   1550: aload #8
          //   1552: aload #9
          //   1554: astore #14
          //   1556: astore #13
          //   1558: astore #8
          //   1560: istore #12
          //   1562: astore #11
          //   1564: new a/jk
          //   1567: dup
          //   1568: iload #12
          //   1570: aload #8
          //   1572: iconst_1
          //   1573: aload #14
          //   1575: iconst_1
          //   1576: aload #13
          //   1578: invokespecial <init> : (ILjava/lang/String;ZLjava/lang/Runnable;ZLjava/lang/String;)V
          //   1581: astore #15
          //   1583: aload #11
          //   1585: aload #15
          //   1587: invokevirtual b : (La/jk;)V
          //   1590: aload #11
          //   1592: getfield C : Ljava/util/List;
          //   1595: aload #15
          //   1597: invokeinterface add : (Ljava/lang/Object;)Z
          //   1602: pop
          //   1603: goto -> 1338
          //   1606: aload_0
          //   1607: invokevirtual K : ()V
          //   1610: aload #5
          //   1612: invokevirtual a : ()La/ju;
          //   1615: astore #6
          //   1617: aload #4
          //   1619: checkcast a/fj
          //   1622: getfield i : Lcom/badlogic/gdx/scenes/scene2d/Stage;
          //   1625: aload #6
          //   1627: invokestatic a : (Lcom/badlogic/gdx/scenes/scene2d/Stage;La/ju;)V
          //   1630: return
        });
  }
  
  public final void n(int paramInt1, int paramInt2) {
    try {
      il il;
      (il = new il()).aj(70);
      il.ak(paramInt1);
      il.ak(0);
      il.aj(0);
      il.aj(paramInt2);
      il.ak(0);
      il.aj(0);
      b(il.a());
      return;
    } catch (IOException iOException) {
      Gdx.app.error("MenuSend", "sendChooseFooterOption failed", iOException);
      return;
    } 
  }
  
  private void d(int paramInt1, int paramInt2, int paramInt3) {
    try {
      il il;
      (il = new il()).aj(71);
      il.ak(paramInt1);
      il.ak(0);
      il.aj(0);
      paramInt1 = (paramInt2 == 0) ? 1 : (paramInt2 & 0xFF);
      il.aj(paramInt1);
      il.ak(0);
      il.aj(0);
      il.al(paramInt3);
      b(il.a());
      return;
    } catch (IOException iOException) {
      Gdx.app.error("MenuSend", "sendChooseMenuOption failed", iOException);
      return;
    } 
  }
}
