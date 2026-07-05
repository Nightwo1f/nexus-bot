package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Matrix4;
import com.badlogic.gdx.math.Vector2;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;

public final class az {
  public static boolean o = false;
  
  private GlyphLayout a;
  
  private String p;
  
  private GlyphLayout b;
  
  private String q;
  
  private String r;
  
  private int ad = -1;
  
  private int ae = -1;
  
  private TextureRegion B;
  
  public int af = 0;
  
  public final int ag;
  
  public be a;
  
  public float v;
  
  public float w;
  
  public float x;
  
  public float y;
  
  public float z;
  
  public float A;
  
  public float B = null;
  
  public float C;
  
  public boolean p = null;
  
  public int ah;
  
  public int ai;
  
  public int aj;
  
  public int ak;
  
  public float D;
  
  public final int al;
  
  private final int am;
  
  public int an;
  
  private int ao;
  
  private int ap;
  
  private int aq;
  
  private int ar;
  
  private int as;
  
  private int at;
  
  private int au;
  
  private int av;
  
  private int aw;
  
  private int ax = 0;
  
  private ad a;
  
  public String s;
  
  private String t;
  
  public boolean q = null;
  
  public boolean r = "";
  
  public float E;
  
  public float F;
  
  public String u;
  
  public float G;
  
  public int ay;
  
  private float H;
  
  public int az;
  
  private static ShapeRenderer a = null;
  
  public boolean s;
  
  public boolean t;
  
  public float I;
  
  public float J;
  
  public boolean u;
  
  public float K;
  
  public int aA;
  
  private boolean v;
  
  private k a;
  
  private static final List a = new ArrayList(16);
  
  private static final Matrix4 a = new Matrix4();
  
  private static final Matrix4 b = new Matrix4();
  
  private static final GlyphLayout c = new GlyphLayout();
  
  private static final int[] p = new int[] { 4, 3, 0, 6, 8, 9, 2, 5 };
  
  private static final int[] q = new int[] { 5, 3, 0, 6, 8, 9, 2, 4 };
  
  private static final int[] r = new int[] { 3, 0, 6, 8, 9, 2, 4, 5 };
  
  private final Color g;
  
  private final Color h;
  
  private final Color i;
  
  private final Color j;
  
  private final Color k;
  
  public y a = null;
  
  public y b = null;
  
  public y c;
  
  public y d;
  
  public static final List b = new ArrayList();
  
  public static final List c = new ArrayList();
  
  private static final Comparator a = new ba();
  
  private static final List d = new ArrayList(128);
  
  private static bc a() {
    return c.isEmpty() ? new bc() : c.remove(c.size() - 1);
  }
  
  public final void a(boolean paramBoolean) {
    this.v = paramBoolean;
    if (paramBoolean && this.a == null)
      this.a = (Comparator)b.a.a(593); 
  }
  
  public az(int paramInt1, int paramInt2, String paramString, int paramInt3, int paramInt4, be parambe, float paramFloat, int paramInt5, int paramInt6, int paramInt7, int paramInt8, int paramInt9, int paramInt10, int paramInt11, int paramInt12, int paramInt13, int paramInt14, int paramInt15, int paramInt16) {
    this.a = null;
    this.t = null;
    this.q = true;
    this.r = false;
    this.E = 0.4F;
    this.F = 0.0F;
    this.u = null;
    this.G = 0.0F;
    this.H = 1.0F;
    this.az = -1;
    this.s = false;
    this.t = false;
    this.I = 1.0F;
    this.J = 1.0F;
    this.u = false;
    this.K = 0.0F;
    this.aA = -1;
    this.v = false;
    this.a = null;
    this.g = new Color(1.0F, 1.0F, 1.0F, 1.0F);
    this.h = new Color(1.0F, 1.0F, 1.0F, 1.0F);
    this.i = new Color(1.0F, 1.0F, 1.0F, 1.0F);
    this.j = new Color(1.0F, 1.0F, 1.0F, 1.0F);
    this.k = new Color(1.0F, 1.0F, 1.0F, 1.0F);
    this.ag = paramInt1;
    this.an = paramInt2;
    this.s = paramString;
    this.al = paramInt3;
    this.am = paramInt5;
    this.ao = paramInt6;
    this.ap = paramInt7;
    this.aq = paramInt8;
    this.ar = paramInt9;
    this.as = paramInt10;
    this.at = paramInt11;
    this.au = paramInt12;
    this.av = paramInt13;
    this.aw = paramInt14;
    this.ax = paramInt15;
    if (paramInt16 > 0) {
      this.ay = paramInt16;
    } else {
      this.ay = 700;
    } 
    this.a = (Comparator)parambe;
    this.aj = a(paramInt4);
    this.ak = this.aj;
    this.D = 0.0F;
    this.v = parambe.aD * paramFloat;
    this.w = parambe.aE * paramFloat;
    this.p = false;
    if (paramInt5 != 0 && paramInt5 != 1)
      n(paramInt5); 
    t();
    u();
    s();
  }
  
  private void s() {
    this.r = (int[])("" + this.an + "_" + this.an + "_" + this.ao + "_" + this.ap + "_" + this.aq + "_" + this.ar + "_" + this.as + "_" + this.at + "_" + this.au + "_" + this.av);
    this.ad = -1;
  }
  
  private void t() {
    this.g.set((this.at >> 16 & 0xFF) / 255.0F, (this.at >> 8 & 0xFF) / 255.0F, (this.at & 0xFF) / 255.0F, 1.0F);
    this.h.set((this.as >> 16 & 0xFF) / 255.0F, (this.as >> 8 & 0xFF) / 255.0F, (this.as & 0xFF) / 255.0F, 1.0F);
    this.i.set((this.au >> 16 & 0xFF) / 255.0F, (this.au >> 8 & 0xFF) / 255.0F, (this.au & 0xFF) / 255.0F, 1.0F);
    this.j.set((this.av >> 16 & 0xFF) / 255.0F, (this.av >> 8 & 0xFF) / 255.0F, (this.av & 0xFF) / 255.0F, 1.0F);
    this.k.set((this.aw >> 16 & 0xFF) / 255.0F, (this.aw >> 8 & 0xFF) / 255.0F, (this.aw & 0xFF) / 255.0F, 1.0F);
  }
  
  private void u() {
    if (b.a != null) {
      this.a = (this.aq != 0) ? (Comparator)b.a.a(this.aq) : null;
      this.b = (this.ap != 0) ? (List)b.a.a(this.ap) : null;
      this.c = (this.ao != 0) ? (List)b.a.a(this.ao) : null;
      this.d = (this.ar != 0) ? (List)b.a.a(this.ar) : null;
    } 
  }
  
  public final void a(int paramInt, float paramFloat) {
    int i = paramInt;
    u u;
    t t;
    az az1;
    float f = lj.i((az1 = this).an) ? (((t = b.a.a(az1.an)) != null && (u = (u)t.i.get(Integer.valueOf(i))) != null) ? u.b : 0.4F) : ((((az)u).a != null && ((y)((az)u).a).k.containsKey(Integer.valueOf(i))) ? ((z)((y)((az)u).a).k.get(Integer.valueOf(i))).b : ((((az)u).b != null && ((y)((az)u).b).k.containsKey(Integer.valueOf(i))) ? ((z)((y)((az)u).b).k.get(Integer.valueOf(i))).b : ((((az)u).c != null && ((y)((az)u).c).k.containsKey(Integer.valueOf(i))) ? ((z)((y)((az)u).c).k.get(Integer.valueOf(i))).b : 0.4F)));
    if (paramFloat <= 0.0F || f <= 0.0F) {
      this.H = 1.0F;
      return;
    } 
    this.H = 1.0F * f / paramFloat;
  }
  
  public static int a(int paramInt) {
    switch (paramInt) {
      case 0:
        return 2;
      case 1:
        return 5;
      case 2:
        return 3;
      case 3:
        return 4;
    } 
    return 1;
  }
  
  public final void a(SpriteBatch paramSpriteBatch, cq paramcq, float paramFloat) {
    if (this.q == null)
      return; 
    az az1;
    (az1 = this).D += paramFloat * az1.H;
    if (az1.u != null) {
      az1.G += paramFloat;
      if (az1.G >= 8.0F) {
        az1.u = null;
        az1.G = 0.0F;
      } 
    } 
    if (az1.r != null) {
      az1.F += paramFloat;
      if (az1.F >= az1.E) {
        az1.r = false;
        az1.ak = az1.aj;
        az1.D = 0.0F;
      } 
    } 
    if (az1.p != null) {
      az1.B = Math.min(az1.B + paramFloat, az1.C);
      float f = az1.B / az1.C;
      az1.v = MathUtils.lerp(az1.x, az1.z, f);
      az1.w = MathUtils.lerp(az1.y, az1.A, f);
      if (az1.B >= az1.C) {
        az1.v = az1.z;
        az1.w = az1.A;
        az1.a = (Comparator)new be(((be)az1.a).aD + az1.ah, ((be)az1.a).aE + az1.ai, ((be)az1.a).aF);
        az1.p = false;
        az1.ak = az1.aj;
        az1.D = 0.0F;
      } 
    } 
    if (this.af != 0) {
      NinePatch ninePatch = null;
      if (this.af == 1) {
        ninePatch = b.D;
      } else if (this.af == 2) {
        ninePatch = b.F;
      } else if (this.af == 3) {
        ninePatch = b.E;
      } 
      if (ninePatch != null) {
        float f1 = paramcq.bP;
        int i = (int)(this.D / 0.15F) % 3 * 64;
        float f2 = this.v + (f1 - 64.0F) / 2.0F;
        float f3 = this.w + f1 - 44.0F / 1.5F;
        paramSpriteBatch.setColor(Color.WHITE);
        paramSpriteBatch.draw((Texture)ninePatch, f2, f3 + 44.0F, 64.0F, -44.0F, i, 0, 64, 44, false, false);
      } 
    } 
    if (lj.i(this.an)) {
      t t1;
      if ((t1 = a()) == null)
        return; 
      TextureRegion textureRegion = t1.a(this.ak, this.D);
      Vector2 vector2 = t1.a(this.ak, this.D);
      if (textureRegion == null || vector2 == null)
        return; 
      float f1 = this.v + vector2.x;
      float f2 = this.w + vector2.y;
      paramSpriteBatch.draw(textureRegion, f1, f2 + textureRegion.getRegionHeight(), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
    } else {
      int i = 0;
      if (this.a != null && this.a.a(this.ak)) {
        i = ((z)((y)this.a).k.get(Integer.valueOf(this.ak))).b(this.D);
      } else if (this.b != null && this.b.a(this.ak)) {
        i = ((z)((y)this.b).k.get(Integer.valueOf(this.ak))).b(this.D);
      } 
      boolean bool = false;
      if (this.ak != this.ad || i != this.ae || this.B == null) {
        String str;
        TextureRegion textureRegion;
        if ((textureRegion = bk.a(str = "" + this.r + "_" + this.r + "_" + this.ak)) != null) {
          this.B = textureRegion;
          this.ad = this.ak;
          this.ae = i;
        } else {
          Comparator comparator1 = a;
          d.addAll((Collection)comparator1);
          comparator1.clear();
          int j;
          int[] arrayOfInt = ((j = this.ak) == 5 || j == 9 || j == 13) ? p : ((j == 4 || j == 8 || j == 12 || j == 2 || j == 6) ? q : r);
          z z;
          if (this.a != null && this.a.a(this.ak) && (z = (z)((y)this.a).k.get(Integer.valueOf(this.ak))) != null) {
            TextureRegion[] arrayOfTextureRegion = z.a(this.D);
            Vector2[] arrayOfVector2 = z.a(this.D);
            int[] arrayOfInt2 = z.b(this.D);
            int[] arrayOfInt1 = z.a(this.D);
            if (arrayOfTextureRegion != null)
              for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
                if (arrayOfTextureRegion[b] != null)
                  a.add(a(arrayOfTextureRegion[b], arrayOfVector2[b], arrayOfInt2[b], arrayOfInt1[b], 0, arrayOfInt)); 
              }  
          } 
          if (this.b != null && this.b.a(this.ak) && (z = (z)((y)this.b).k.get(Integer.valueOf(this.ak))) != null) {
            TextureRegion[] arrayOfTextureRegion = z.a(this.D);
            Vector2[] arrayOfVector2 = z.a(this.D);
            int[] arrayOfInt2 = z.b(this.D);
            int[] arrayOfInt1 = z.a(this.D);
            if (arrayOfTextureRegion != null)
              for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
                if (arrayOfTextureRegion[b] != null)
                  a.add(a(arrayOfTextureRegion[b], arrayOfVector2[b], arrayOfInt2[b], arrayOfInt1[b], 1, arrayOfInt)); 
              }  
          } 
          if (this.c != null && this.c.a(this.ak) && (z = (z)((y)this.c).k.get(Integer.valueOf(this.ak))) != null) {
            TextureRegion[] arrayOfTextureRegion = z.a(this.D);
            Vector2[] arrayOfVector2 = z.a(this.D);
            int[] arrayOfInt2 = z.b(this.D);
            int[] arrayOfInt1 = z.a(this.D);
            if (arrayOfTextureRegion != null)
              for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
                if (arrayOfTextureRegion[b] != null)
                  a.add(a(arrayOfTextureRegion[b], arrayOfVector2[b], arrayOfInt2[b], arrayOfInt1[b], 2, arrayOfInt)); 
              }  
          } 
          a.sort(a);
          if (bk.f()) {
            boolean bool1;
            if (bool1 = paramSpriteBatch.isDrawing())
              paramSpriteBatch.end(); 
            TextureRegion textureRegion1 = bk.a(str, (List)a, this.g, this.h, this.i, this.j);
            if (bool1)
              paramSpriteBatch.begin(); 
            this.B = textureRegion1;
            this.ad = this.ak;
            this.ae = i;
          } else {
            bool = true;
            for (byte b = 0; b < a.size(); b++) {
              bb bb;
              switch ((bb = a.get(b)).F) {
                case 1:
                  paramSpriteBatch.setColor(this.g);
                  break;
                case 2:
                  paramSpriteBatch.setColor(this.h);
                  break;
                case 3:
                  paramSpriteBatch.setColor(this.i);
                  break;
                case 4:
                  paramSpriteBatch.setColor(this.j);
                  break;
                default:
                  paramSpriteBatch.setColor(Color.WHITE);
                  break;
              } 
              paramSpriteBatch.draw(bb.j, this.v + bb.k.x, this.w + bb.k.y + bb.j.getRegionHeight(), bb.j.getRegionWidth(), -bb.j.getRegionHeight());
            } 
            paramSpriteBatch.setColor(Color.WHITE);
          } 
        } 
      } 
      if (!bool && this.B != null) {
        paramSpriteBatch.setColor(Color.WHITE);
        paramSpriteBatch.draw(this.B, this.v - 64.0F, this.w - 64.0F + 128.0F, 128.0F, -128.0F);
      } 
    } 
    paramSpriteBatch.setColor(Color.WHITE);
    Comparator comparator;
    if ((comparator = this.a) != null) {
      TextureRegion textureRegion = comparator.e(this.D);
      Vector2 vector2 = comparator.e(this.D);
      if (textureRegion != null && vector2 != null) {
        float f1 = this.v + vector2.x;
        float f2 = this.w + vector2.y;
        paramSpriteBatch.draw(textureRegion, f1, f2 + textureRegion.getRegionHeight(), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
      } 
    } 
    cq cq1 = paramcq;
    SpriteBatch spriteBatch = paramSpriteBatch;
    if ((az1 = this).v) {
      TextureRegion textureRegion;
      if ((paramSpriteBatch = (SpriteBatch)((az1.a != null) ? az1.a : ((b.a != null) ? b.a.a(593) : null))) != null && (textureRegion = paramSpriteBatch.b(az1.D)) != null) {
        Vector2 vector2 = paramSpriteBatch.b(az1.D);
        float f1 = cq1.bP;
        f1 = az1.v + f1 - textureRegion.getRegionWidth();
        float f2 = az1.w + vector2.y;
        spriteBatch.draw(textureRegion, MathUtils.round(f1), MathUtils.round(f2 + textureRegion.getRegionHeight()), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
        if (((k)paramSpriteBatch).h > 0)
          az1.a(((k)paramSpriteBatch).h, ((k)paramSpriteBatch).a); 
      } 
    } 
    t t;
    u u;
    if ((t = a()) != null && (u = (u)t.i.get(Integer.valueOf(this.ak))) != null && u.s > 0)
      a(u.s, u.c); 
    if (this.a != null && ((ad)this.a).H > 0)
      a(((ad)this.a).H, ((ad)this.a).e); 
  }
  
  private void a(int paramInt, Color paramColor) {
    q q;
    if ((q = (q)((b.a != null) ? b.a.a(paramInt) : null)) != null) {
      bc bc;
      (bc = a()).a = q;
      bc.l = paramColor;
      Vector2 vector2 = q.d(this.D);
      bc.v = this.v + vector2.x + 0.0F;
      bc.w = this.w + vector2.y + 0.0F;
      b.add(bc);
    } 
  }
  
  public final boolean a(cq paramcq, Vector2 paramVector2, int[] paramArrayOfint) {
    byte b;
    if (!this.u)
      return false; 
    if (this.aA < 0)
      return false; 
    if (this.aA >= 77) {
      b = 11;
    } else if (this.aA >= 60) {
      b = 10;
    } else if (this.aA >= 25) {
      b = 9;
    } else {
      b = 8;
    } 
    float f2;
    float f3 = MathUtils.round((f2 = paramcq.bP) * 0.7F);
    float f4 = MathUtils.round(this.v);
    float f5 = MathUtils.round(this.w);
    f4 = MathUtils.round(f4 + (f2 - f3) * 0.5F);
    f2 = MathUtils.round(MathUtils.round(f5 - MathUtils.round(f2 * 0.07F) - 1.0F) - MathUtils.round(f2 * 0.07F) + 1.0F);
    f3 = MathUtils.round(f4 + f3 + 1.0F);
    float f1 = MathUtils.round(paramcq.bP * 0.2F);
    f1 = MathUtils.round(f2 + f1);
    paramVector2.set(f3, f1);
    paramArrayOfint[0] = b;
    return true;
  }
  
  public final void a(SpriteBatch paramSpriteBatch, cq paramcq) {
    BitmapFont bitmapFont;
    if (this.q == null || this.al == 2)
      return; 
    SpriteBatch spriteBatch = paramSpriteBatch;
    az az1;
    float f2 = MathUtils.round((az1 = this).v);
    float f3 = MathUtils.round(az1.w);
    float f1;
    float f4 = MathUtils.round((f1 = paramcq.bP) * 0.7F);
    float f5 = MathUtils.round(f1 * 0.07F);
    f1 = MathUtils.round(f2 + (f1 - f4) * 0.5F);
    f2 = MathUtils.round(f3 - f5 - 1.0F);
    if (az1.u) {
      f3 = MathUtils.round(f2 - f5 + 1.0F);
      spriteBatch.setColor(Color.WHITE);
      b.a.draw((Batch)spriteBatch, f1 - 1.0F, f3 - 1.0F, f4 + 2.0F, f5 + 2.0F);
      spriteBatch.setColor(Color.GREEN);
      spriteBatch.draw((TextureRegion)b.a, f1, f3, f4 * az1.I, f5);
      spriteBatch.setColor(Color.WHITE);
      b.a.draw((Batch)spriteBatch, f1 - 1.0F, f2 - 1.0F, f4 + 2.0F, f5 + 2.0F);
      spriteBatch.setColor(Color.YELLOW);
      spriteBatch.draw((TextureRegion)b.a, f1, f2, f4 * az1.K, f5);
      spriteBatch.setColor(Color.WHITE);
      if (az1.aA >= 0) {
        byte b;
        if (az1.aA >= 77) {
          b = 11;
        } else if (b.aA >= 60) {
          b = 10;
        } else if (b.aA >= 25) {
          b = 9;
        } else {
          b = 8;
        } 
        if ((bitmapFont = b.d[b]) != null) {
          float f6 = bitmapFont.getRegionWidth();
          float f7 = bitmapFont.getRegionHeight();
          f2 = f2 + f5 - f3;
          f2 = f3 + f2 / 2.0F;
          f1 = f1 + f4 + 4.0F;
          f2 -= f7 / 2.0F;
          spriteBatch.draw((TextureRegion)bitmapFont, MathUtils.round(f1), MathUtils.round(f2 + f7), f6, -f7);
        } 
      } 
      return;
    } 
    if (((az)bitmapFont).s || ((az)bitmapFont).t) {
      f2 = MathUtils.round(f2);
      if (((az)bitmapFont).t) {
        spriteBatch.setColor(Color.WHITE);
        b.a.draw((Batch)spriteBatch, f1 - 1.0F, f2 - 1.0F, f4 + 2.0F, f5 + 2.0F);
        spriteBatch.setColor(Color.BLUE);
        spriteBatch.draw((TextureRegion)b.a, f1, f2, f4 * ((az)bitmapFont).J, f5);
        f3 = MathUtils.round(f2 - f5 + 1.0F);
        spriteBatch.setColor(Color.WHITE);
        b.a.draw((Batch)spriteBatch, f1 - 1.0F, f3 - 1.0F, f4 + 2.0F, f5 + 2.0F);
        spriteBatch.setColor(Color.GREEN);
        spriteBatch.draw((TextureRegion)b.a, f1, f3, f4 * ((az)bitmapFont).I, f5);
      } else {
        Color color;
        switch (((az)bitmapFont).al) {
          case 3:
            color = Color.YELLOW;
            break;
          case 4:
            color = Color.RED;
            break;
          default:
            color = Color.GREEN;
            break;
        } 
        spriteBatch.setColor(Color.WHITE);
        b.a.draw((Batch)spriteBatch, f1 - 1.0F, f2 - 1.0F, f4 + 2.0F, f5 + 2.0F);
        spriteBatch.setColor(color);
        spriteBatch.draw((TextureRegion)b.a, f1, f2, f4 * ((az)bitmapFont).I, f5);
      } 
      spriteBatch.setColor(Color.WHITE);
    } 
  }
  
  public final void b(SpriteBatch paramSpriteBatch, cq paramcq) {
    // Byte code:
    //   0: getstatic a/az.o : Z
    //   3: ifne -> 22
    //   6: aload_0
    //   7: getfield q : Z
    //   10: ifeq -> 21
    //   13: aload_0
    //   14: getfield al : I
    //   17: iconst_2
    //   18: if_icmpne -> 22
    //   21: return
    //   22: aload_0
    //   23: getfield u : Ljava/lang/String;
    //   26: ifnull -> 541
    //   29: aload_0
    //   30: aload_1
    //   31: aload_2
    //   32: aload_0
    //   33: getfield u : Ljava/lang/String;
    //   36: astore #4
    //   38: astore_3
    //   39: astore_2
    //   40: astore_1
    //   41: aload #4
    //   43: ifnull -> 54
    //   46: aload #4
    //   48: invokevirtual isEmpty : ()Z
    //   51: ifeq -> 55
    //   54: return
    //   55: aload_1
    //   56: getfield s : Ljava/lang/String;
    //   59: ifnull -> 69
    //   62: aload_1
    //   63: getfield s : Ljava/lang/String;
    //   66: goto -> 71
    //   69: ldc ''
    //   71: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;)Ljava/lang/String;
    //   76: dup
    //   77: astore #5
    //   79: aload #4
    //   81: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   86: invokestatic a : (Ljava/lang/String;)Lcom/badlogic/gdx/graphics/g2d/BitmapFont;
    //   89: astore #7
    //   91: aload_3
    //   92: getfield bP : I
    //   95: i2f
    //   96: dup
    //   97: fstore_3
    //   98: ldc 5.0
    //   100: fmul
    //   101: fstore #6
    //   103: aload #7
    //   105: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   108: getfield lineHeight : F
    //   111: fstore #8
    //   113: aload #7
    //   115: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   118: fload #8
    //   120: fconst_1
    //   121: fmul
    //   122: invokevirtual setLineHeight : (F)V
    //   125: aload_1
    //   126: getfield b : Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   129: ifnull -> 144
    //   132: aload #4
    //   134: aload_1
    //   135: getfield q : Ljava/lang/String;
    //   138: invokevirtual equals : (Ljava/lang/Object;)Z
    //   141: ifne -> 172
    //   144: aload_1
    //   145: new com/badlogic/gdx/graphics/g2d/GlyphLayout
    //   148: dup
    //   149: aload #7
    //   151: aload #4
    //   153: getstatic com/badlogic/gdx/graphics/Color.YELLOW : Lcom/badlogic/gdx/graphics/Color;
    //   156: fload #6
    //   158: iconst_1
    //   159: iconst_1
    //   160: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/BitmapFont;Ljava/lang/CharSequence;Lcom/badlogic/gdx/graphics/Color;FIZ)V
    //   163: putfield b : Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   166: aload_1
    //   167: aload #4
    //   169: putfield q : Ljava/lang/String;
    //   172: aload #7
    //   174: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   177: fload #8
    //   179: invokevirtual setLineHeight : (F)V
    //   182: aload_1
    //   183: getfield w : F
    //   186: fstore #9
    //   188: aload_1
    //   189: getfield s : Z
    //   192: ifne -> 209
    //   195: aload_1
    //   196: getfield t : Z
    //   199: ifne -> 209
    //   202: aload_1
    //   203: getfield u : Z
    //   206: ifeq -> 216
    //   209: fload_3
    //   210: ldc 0.35
    //   212: fmul
    //   213: goto -> 220
    //   216: fload_3
    //   217: ldc 0.3
    //   219: fmul
    //   220: fstore #10
    //   222: fload #9
    //   224: fload #10
    //   226: fsub
    //   227: fstore #11
    //   229: aload_1
    //   230: getfield v : F
    //   233: fload_3
    //   234: fconst_2
    //   235: fdiv
    //   236: fadd
    //   237: fload #6
    //   239: fconst_2
    //   240: fdiv
    //   241: fsub
    //   242: invokestatic round : (F)I
    //   245: i2f
    //   246: fstore #10
    //   248: aload #7
    //   250: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   253: getfield scaleX : F
    //   256: fstore #9
    //   258: aload #7
    //   260: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   263: getfield scaleY : F
    //   266: fstore #12
    //   268: aload #7
    //   270: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   273: fload #9
    //   275: fload #12
    //   277: fneg
    //   278: invokevirtual setScale : (FF)V
    //   281: fload #11
    //   283: aload_1
    //   284: getfield b : Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   287: getfield height : F
    //   290: fsub
    //   291: fstore #13
    //   293: fload #11
    //   295: aload_1
    //   296: getfield b : Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   299: getfield height : F
    //   302: fsub
    //   303: fload #8
    //   305: fsub
    //   306: fstore_1
    //   307: aload #7
    //   309: getstatic com/badlogic/gdx/graphics/Color.BLACK : Lcom/badlogic/gdx/graphics/Color;
    //   312: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   315: aload #7
    //   317: aload_2
    //   318: aload #4
    //   320: fload #10
    //   322: fconst_1
    //   323: fsub
    //   324: fload #13
    //   326: fload #6
    //   328: iconst_1
    //   329: iconst_1
    //   330: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   333: pop
    //   334: aload #7
    //   336: aload_2
    //   337: aload #4
    //   339: fload #10
    //   341: fconst_1
    //   342: fadd
    //   343: fload #13
    //   345: fload #6
    //   347: iconst_1
    //   348: iconst_1
    //   349: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   352: pop
    //   353: aload #7
    //   355: aload_2
    //   356: aload #4
    //   358: fload #10
    //   360: fload #13
    //   362: fconst_1
    //   363: fsub
    //   364: fload #6
    //   366: iconst_1
    //   367: iconst_1
    //   368: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   371: pop
    //   372: aload #7
    //   374: aload_2
    //   375: aload #4
    //   377: fload #10
    //   379: fload #13
    //   381: fconst_1
    //   382: fadd
    //   383: fload #6
    //   385: iconst_1
    //   386: iconst_1
    //   387: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   390: pop
    //   391: aload #7
    //   393: getstatic com/badlogic/gdx/graphics/Color.YELLOW : Lcom/badlogic/gdx/graphics/Color;
    //   396: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   399: aload #7
    //   401: aload_2
    //   402: aload #4
    //   404: fload #10
    //   406: fload #13
    //   408: fload #6
    //   410: iconst_1
    //   411: iconst_1
    //   412: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   415: pop
    //   416: aload #7
    //   418: getstatic com/badlogic/gdx/graphics/Color.BLACK : Lcom/badlogic/gdx/graphics/Color;
    //   421: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   424: aload #7
    //   426: aload_2
    //   427: aload #5
    //   429: fload #10
    //   431: fconst_1
    //   432: fsub
    //   433: fload_1
    //   434: fload #6
    //   436: iconst_1
    //   437: iconst_0
    //   438: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   441: pop
    //   442: aload #7
    //   444: aload_2
    //   445: aload #5
    //   447: fload #10
    //   449: fconst_1
    //   450: fadd
    //   451: fload_1
    //   452: fload #6
    //   454: iconst_1
    //   455: iconst_0
    //   456: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   459: pop
    //   460: aload #7
    //   462: aload_2
    //   463: aload #5
    //   465: fload #10
    //   467: fload_1
    //   468: fconst_1
    //   469: fsub
    //   470: fload #6
    //   472: iconst_1
    //   473: iconst_0
    //   474: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   477: pop
    //   478: aload #7
    //   480: aload_2
    //   481: aload #5
    //   483: fload #10
    //   485: fload_1
    //   486: fconst_1
    //   487: fadd
    //   488: fload #6
    //   490: iconst_1
    //   491: iconst_0
    //   492: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   495: pop
    //   496: aload #7
    //   498: getstatic com/badlogic/gdx/graphics/Color.YELLOW : Lcom/badlogic/gdx/graphics/Color;
    //   501: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   504: aload #7
    //   506: aload_2
    //   507: aload #5
    //   509: fload #10
    //   511: fload_1
    //   512: fload #6
    //   514: iconst_1
    //   515: iconst_0
    //   516: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FFFIZ)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   519: pop
    //   520: aload #7
    //   522: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   525: fload #9
    //   527: fload #12
    //   529: invokevirtual setScale : (FF)V
    //   532: aload #7
    //   534: getstatic com/badlogic/gdx/graphics/Color.WHITE : Lcom/badlogic/gdx/graphics/Color;
    //   537: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   540: return
    //   541: aload_0
    //   542: aload_1
    //   543: aload_2
    //   544: astore_3
    //   545: astore_2
    //   546: astore_1
    //   547: getstatic a/az.o : Z
    //   550: ifne -> 561
    //   553: aload_1
    //   554: getfield al : I
    //   557: iconst_2
    //   558: if_icmpeq -> 1102
    //   561: aload_1
    //   562: aload_3
    //   563: astore #12
    //   565: astore #9
    //   567: aload #12
    //   569: ifnull -> 608
    //   572: aload #12
    //   574: getfield X : Z
    //   577: ifeq -> 608
    //   580: aload #9
    //   582: getfield ax : I
    //   585: ifle -> 608
    //   588: aload #9
    //   590: getfield s : Ljava/lang/String;
    //   593: aload #9
    //   595: getfield ax : I
    //   598: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;I)Ljava/lang/String;
    //   603: astore #13
    //   605: goto -> 615
    //   608: aload #9
    //   610: getfield s : Ljava/lang/String;
    //   613: astore #13
    //   615: getstatic a/az.o : Z
    //   618: ifeq -> 635
    //   621: aload #13
    //   623: aload #9
    //   625: getfield ag : I
    //   628: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;I)Ljava/lang/String;
    //   633: astore #13
    //   635: aload #9
    //   637: getfield t : Ljava/lang/String;
    //   640: ifnull -> 664
    //   643: aload #9
    //   645: getfield t : Ljava/lang/String;
    //   648: aload #13
    //   650: invokevirtual equals : (Ljava/lang/Object;)Z
    //   653: ifeq -> 664
    //   656: aload #9
    //   658: getfield t : Ljava/lang/String;
    //   661: goto -> 676
    //   664: aload #9
    //   666: aload #13
    //   668: putfield t : Ljava/lang/String;
    //   671: aload #9
    //   673: getfield t : Ljava/lang/String;
    //   676: dup
    //   677: astore #4
    //   679: invokestatic a : (Ljava/lang/String;)Lcom/badlogic/gdx/graphics/g2d/BitmapFont;
    //   682: astore #5
    //   684: aload_1
    //   685: getfield a : Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   688: ifnull -> 703
    //   691: aload #4
    //   693: aload_1
    //   694: getfield p : Ljava/lang/String;
    //   697: invokevirtual equals : (Ljava/lang/Object;)Z
    //   700: ifne -> 724
    //   703: aload_1
    //   704: new com/badlogic/gdx/graphics/g2d/GlyphLayout
    //   707: dup
    //   708: aload #5
    //   710: aload #4
    //   712: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/BitmapFont;Ljava/lang/CharSequence;)V
    //   715: putfield a : Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   718: aload_1
    //   719: aload #4
    //   721: putfield p : Ljava/lang/String;
    //   724: aload_1
    //   725: getfield a : Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   728: getfield width : F
    //   731: fstore #6
    //   733: aload_3
    //   734: getfield bP : I
    //   737: i2f
    //   738: fstore #7
    //   740: aload_1
    //   741: getfield v : F
    //   744: fload #7
    //   746: fload #6
    //   748: fsub
    //   749: fconst_2
    //   750: fdiv
    //   751: fadd
    //   752: fstore_3
    //   753: aload_1
    //   754: getfield al : I
    //   757: tableswitch default -> 836, 1 -> 796, 2 -> 836, 3 -> 804, 4 -> 812, 5 -> 820, 6 -> 828
    //   796: getstatic com/badlogic/gdx/graphics/Color.GREEN : Lcom/badlogic/gdx/graphics/Color;
    //   799: astore #6
    //   801: goto -> 841
    //   804: getstatic com/badlogic/gdx/graphics/Color.YELLOW : Lcom/badlogic/gdx/graphics/Color;
    //   807: astore #6
    //   809: goto -> 841
    //   812: getstatic com/badlogic/gdx/graphics/Color.RED : Lcom/badlogic/gdx/graphics/Color;
    //   815: astore #6
    //   817: goto -> 841
    //   820: getstatic com/badlogic/gdx/graphics/Color.GREEN : Lcom/badlogic/gdx/graphics/Color;
    //   823: astore #6
    //   825: goto -> 841
    //   828: getstatic com/badlogic/gdx/graphics/Color.GREEN : Lcom/badlogic/gdx/graphics/Color;
    //   831: astore #6
    //   833: goto -> 841
    //   836: getstatic com/badlogic/gdx/graphics/Color.WHITE : Lcom/badlogic/gdx/graphics/Color;
    //   839: astore #6
    //   841: aload_1
    //   842: getfield al : I
    //   845: iconst_1
    //   846: if_icmpne -> 901
    //   849: aload_1
    //   850: getfield s : Ljava/lang/String;
    //   853: ifnull -> 901
    //   856: aload_1
    //   857: getfield s : Ljava/lang/String;
    //   860: iconst_1
    //   861: iconst_0
    //   862: ldc 'GM-'
    //   864: iconst_0
    //   865: iconst_3
    //   866: invokevirtual regionMatches : (ZILjava/lang/String;II)Z
    //   869: ifeq -> 880
    //   872: getstatic com/badlogic/gdx/graphics/Color.RED : Lcom/badlogic/gdx/graphics/Color;
    //   875: astore #6
    //   877: goto -> 901
    //   880: aload_1
    //   881: getfield s : Ljava/lang/String;
    //   884: iconst_1
    //   885: iconst_0
    //   886: ldc 'PM-'
    //   888: iconst_0
    //   889: iconst_3
    //   890: invokevirtual regionMatches : (ZILjava/lang/String;II)Z
    //   893: ifeq -> 901
    //   896: getstatic com/badlogic/gdx/graphics/Color.BLUE : Lcom/badlogic/gdx/graphics/Color;
    //   899: astore #6
    //   901: aload_1
    //   902: getfield s : Z
    //   905: ifne -> 922
    //   908: aload_1
    //   909: getfield t : Z
    //   912: ifne -> 922
    //   915: aload_1
    //   916: getfield u : Z
    //   919: ifeq -> 932
    //   922: aload_1
    //   923: getfield w : F
    //   926: ldc 30.0
    //   928: fsub
    //   929: goto -> 939
    //   932: aload_1
    //   933: getfield w : F
    //   936: ldc 20.0
    //   938: fsub
    //   939: fstore #8
    //   941: fload #7
    //   943: ldc 0.04
    //   945: fmul
    //   946: fstore_1
    //   947: fload_3
    //   948: invokestatic round : (F)I
    //   951: i2f
    //   952: fstore #9
    //   954: fload #8
    //   956: fload_1
    //   957: fsub
    //   958: invokestatic round : (F)I
    //   961: i2f
    //   962: fstore #10
    //   964: aload #5
    //   966: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   969: getfield scaleX : F
    //   972: fstore #11
    //   974: aload #5
    //   976: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   979: getfield scaleY : F
    //   982: fstore_3
    //   983: aload #5
    //   985: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   988: fload #11
    //   990: fload_3
    //   991: fneg
    //   992: invokevirtual setScale : (FF)V
    //   995: aload #5
    //   997: getstatic com/badlogic/gdx/graphics/Color.BLACK : Lcom/badlogic/gdx/graphics/Color;
    //   1000: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   1003: aload #5
    //   1005: aload_2
    //   1006: aload #4
    //   1008: fload #9
    //   1010: fconst_1
    //   1011: fsub
    //   1012: fload #10
    //   1014: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FF)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   1017: pop
    //   1018: aload #5
    //   1020: aload_2
    //   1021: aload #4
    //   1023: fload #9
    //   1025: fconst_1
    //   1026: fadd
    //   1027: fload #10
    //   1029: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FF)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   1032: pop
    //   1033: aload #5
    //   1035: aload_2
    //   1036: aload #4
    //   1038: fload #9
    //   1040: fload #10
    //   1042: fconst_1
    //   1043: fsub
    //   1044: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FF)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   1047: pop
    //   1048: aload #5
    //   1050: aload_2
    //   1051: aload #4
    //   1053: fload #9
    //   1055: fload #10
    //   1057: fconst_1
    //   1058: fadd
    //   1059: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FF)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   1062: pop
    //   1063: aload #5
    //   1065: aload #6
    //   1067: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   1070: aload #5
    //   1072: aload_2
    //   1073: aload #4
    //   1075: fload #9
    //   1077: fload #10
    //   1079: invokevirtual draw : (Lcom/badlogic/gdx/graphics/g2d/Batch;Ljava/lang/CharSequence;FF)Lcom/badlogic/gdx/graphics/g2d/GlyphLayout;
    //   1082: pop
    //   1083: aload #5
    //   1085: invokevirtual getData : ()Lcom/badlogic/gdx/graphics/g2d/BitmapFont$BitmapFontData;
    //   1088: fload #11
    //   1090: fload_3
    //   1091: invokevirtual setScale : (FF)V
    //   1094: aload #5
    //   1096: getstatic com/badlogic/gdx/graphics/Color.WHITE : Lcom/badlogic/gdx/graphics/Color;
    //   1099: invokevirtual setColor : (Lcom/badlogic/gdx/graphics/Color;)V
    //   1102: return
  }
  
  public final void m(int paramInt) {
    if (this.p != null)
      return; 
    this.aj = a(paramInt);
    this.ak = this.aj;
    this.D = 0.0F;
  }
  
  public final void n(int paramInt) {
    switch (paramInt) {
      case 0:
      case 1:
        this.a = null;
        return;
      case 2:
      case 3:
        paramInt = 1;
        break;
      case 4:
      case 5:
        paramInt = 2;
        break;
      case 6:
      case 7:
        paramInt = 3;
        break;
      case 8:
      case 9:
        paramInt = 4;
        break;
      case 10:
      case 11:
        paramInt = 5;
        break;
      case 12:
      case 13:
        paramInt = 6;
        break;
      case 14:
      case 15:
        paramInt = 7;
        break;
      default:
        this.a = null;
        return;
    } 
    this.a = (Comparator)b.a.a(paramInt);
  }
  
  private t a() {
    return b.a.a(this.an);
  }
  
  public final void a(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, int paramInt6, int paramInt7, int paramInt8, int paramInt9, int paramInt10) {
    this.an = paramInt1;
    this.ao = paramInt2;
    this.ap = paramInt3;
    this.aq = paramInt4;
    this.ar = paramInt5;
    this.as = paramInt6;
    this.at = paramInt7;
    this.au = paramInt8;
    this.av = paramInt9;
    this.aw = paramInt10;
    t();
    u();
    s();
  }
  
  private static bb a(TextureRegion paramTextureRegion, Vector2 paramVector2, int paramInt1, int paramInt2, int paramInt3, int[] paramArrayOfint) {
    bb bb;
    if (d.isEmpty()) {
      bb = new bb();
    } else {
      bb = d.remove(d.size() - 1);
    } 
    bb.a(paramTextureRegion, paramVector2, paramInt1, paramInt2, paramInt3, paramArrayOfint);
    return bb;
  }
}
