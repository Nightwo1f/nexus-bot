package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Vector2;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public final class bo {
  private int aV = -1;
  
  private boolean x = true;
  
  private GlyphLayout b = null;
  
  private String q;
  
  private String r;
  
  private int ad = -1;
  
  private int ae = -1;
  
  private TextureRegion B = null;
  
  private final Color m = new Color(1.0F, 1.0F, 1.0F, 1.0F);
  
  private final Color n = new Color(1.0F, 1.0F, 1.0F, 1.0F);
  
  private final Color o = new Color(1.0F, 1.0F, 1.0F, 1.0F);
  
  private final Color p = new Color(1.0F, 1.0F, 1.0F, 1.0F);
  
  private static final int[] u = new int[] { 4, 3, 0, 6, 8, 9, 2, 5 };
  
  private static final int[] v = new int[] { 5, 3, 0, 6, 8, 9, 2, 4 };
  
  private static final int[] w = new int[] { 3, 0, 6, 8, 9, 2, 4, 5 };
  
  private boolean v;
  
  private k a = null;
  
  private static final List e = new ArrayList(128);
  
  private final List f = new ArrayList(16);
  
  private static final Comparator b = new bp();
  
  public final cq d;
  
  public int aW;
  
  public int aX;
  
  public int aY;
  
  public int aZ;
  
  public int ba;
  
  public int bb;
  
  public int bc;
  
  public int bd;
  
  public int be;
  
  public int bf;
  
  public int bg;
  
  public float L;
  
  public float M;
  
  private int aj;
  
  public int ak;
  
  public boolean y;
  
  public boolean r = "";
  
  public float E;
  
  public float F;
  
  public float D;
  
  private boolean q = null;
  
  public float N;
  
  public float O;
  
  private String u;
  
  private float G;
  
  private int bh;
  
  private float P;
  
  private float Q;
  
  private String v = Character.MIN_VALUE;
  
  private int az;
  
  public int bi;
  
  private float H;
  
  private static bb a(TextureRegion paramTextureRegion, Vector2 paramVector2, int paramInt1, int paramInt2, int paramInt3, int[] paramArrayOfint) {
    bb bb;
    if (e.isEmpty()) {
      bb = new bb();
    } else {
      bb = e.remove(e.size() - 1);
    } 
    bb.a(paramTextureRegion, paramVector2, paramInt1, paramInt2, paramInt3, paramArrayOfint);
    return bb;
  }
  
  public final void b(boolean paramBoolean) {
    this.v = paramBoolean;
    if (paramBoolean && this.a == null)
      this.a = b.a.a(593); 
  }
  
  public bo(cq paramcq) {
    this.q = true;
    this.N = 2.0F;
    this.O = 0.0F;
    this.u = null;
    this.G = 0.0F;
    this.bh = 0;
    this.v = null;
    this.az = -1;
    this.bi = 600;
    this.H = 1.0F;
    this.d = paramcq;
    this.aW = 0;
    this.aX = 0;
    this.aY = 0;
    this.aZ = 0;
    this.ba = 0;
    this.bb = 0;
    this.bc = 0;
    this.bd = 0;
    this.be = 0;
    this.bf = 0;
    this.bg = 0;
    this.aj = 3;
    this.ak = 3;
    this.r = false;
    this.E = 0.0F;
    this.F = 0.0F;
    this.D = 0.0F;
    t();
    s();
  }
  
  private void s() {
    this.r = "player_" + this.aW + "_" + this.aY + "_" + this.aZ + "_" + this.ba + "_" + this.bb + "_" + this.bc + "_" + this.bd + "_" + this.be + "_" + this.bf + "_" + this.bg;
    this.ad = -1;
  }
  
  private void t() {
    this.m.set((this.bd >> 16 & 0xFF) / 255.0F, (this.bd >> 8 & 0xFF) / 255.0F, (this.bd & 0xFF) / 255.0F, 1.0F);
    this.n.set((this.bc >> 16 & 0xFF) / 255.0F, (this.bc >> 8 & 0xFF) / 255.0F, (this.bc & 0xFF) / 255.0F, 1.0F);
    this.o.set((this.be >> 16 & 0xFF) / 255.0F, (this.be >> 8 & 0xFF) / 255.0F, (this.be & 0xFF) / 255.0F, 1.0F);
    this.p.set((this.bf >> 16 & 0xFF) / 255.0F, (this.bf >> 8 & 0xFF) / 255.0F, (this.bf & 0xFF) / 255.0F, 1.0F);
  }
  
  public final void c(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, int paramInt6, int paramInt7, int paramInt8, int paramInt9, int paramInt10, int paramInt11) {
    this.aX = paramInt1;
    this.aW = paramInt2;
    this.aY = paramInt3;
    this.aZ = paramInt4;
    this.ba = paramInt5;
    this.bb = paramInt6;
    this.bc = paramInt7;
    this.bd = paramInt8;
    this.be = paramInt9;
    this.bf = paramInt10;
    this.bg = paramInt11;
    this.x = true;
    t();
    s();
  }
  
  public final void x(int paramInt) {
    if (this.r || this.y)
      return; 
    switch (paramInt) {
      case 0:
        this.aj = 2;
        break;
      case 1:
        this.aj = 5;
        break;
      case 2:
        this.aj = 3;
        break;
      case 3:
        this.aj = 4;
        break;
      default:
        this.aj = 1;
        break;
    } 
    if (!this.r) {
      this.ak = this.aj;
      this.D = 0.0F;
    } 
  }
  
  public final void y(int paramInt) {
    this.y = true;
    switch (paramInt) {
      case 0:
        this.aj = 2;
        break;
      case 1:
        this.aj = 5;
        break;
      case 2:
        this.aj = 3;
        break;
      case 3:
        this.aj = 4;
        break;
      default:
        this.aj = 3;
        break;
    } 
    switch (paramInt) {
      case 0:
      
      case 1:
      
      case 2:
      
      case 3:
      
      default:
        break;
    } 
    paramInt = 7;
    boolean bool = (this.az == paramInt) ? true : false;
    this.az = paramInt;
    this.ak = paramInt;
    if (!bool)
      this.D = 0.0F; 
    E();
  }
  
  public final void D() {
    this.y = false;
    this.ak = this.aj;
    this.az = -1;
    this.D = 0.0F;
    this.H = 1.0F;
  }
  
  private static int b(int paramInt) {
    switch (paramInt) {
      case 2:
        return 6;
      case 5:
        return 9;
      case 3:
        return 7;
      case 4:
        return 8;
    } 
    return 7;
  }
  
  private float a(int paramInt) {
    y y;
    return lj.i(this.aW) ? (((t = b.a.a(this.aW)) != null && t.i.containsKey(Integer.valueOf(paramInt))) ? ((u)t.i.get(Integer.valueOf(paramInt))).b : 0.4F) : ((this.ba != 0 && b.a != null && (y = b.a.a(this.ba)) != null && y.k.containsKey(Integer.valueOf(paramInt))) ? ((z)y.k.get(Integer.valueOf(paramInt))).b : ((this.aZ != 0 && b.a != null && (y = b.a.a(this.aZ)) != null && y.k.containsKey(Integer.valueOf(paramInt))) ? ((z)y.k.get(Integer.valueOf(paramInt))).b : ((this.aY != 0 && b.a != null && (y = b.a.a(this.aY)) != null && y.k.containsKey(Integer.valueOf(paramInt))) ? ((z)y.k.get(Integer.valueOf(paramInt))).b : 0.4F)));
  }
  
  public final void E() {
    float f1 = this.bi / 1000.0F;
    int i = (this.az != -1) ? this.az : b(this.aj);
    float f2 = a(i);
    if (f1 <= 0.0F || f2 <= 0.0F) {
      this.H = 1.0F;
      return;
    } 
    f1 /= Math.max(1, 1);
    this.H = f2 / f1;
    this.H = MathUtils.clamp(this.H, 0.25F, 5.0F);
  }
  
  public final void a(SpriteBatch paramSpriteBatch, OrthographicCamera paramOrthographicCamera, float paramFloat) {
    bo bo1;
    (bo1 = this).D += paramFloat * bo1.H;
    if (bo1.u != null) {
      bo1.G += paramFloat;
      if (bo1.G >= 8.0F) {
        bo1.u = null;
        bo1.G = 0.0F;
      } 
    } 
    if (bo1.r) {
      bo1.F += paramFloat;
      if (bo1.F >= bo1.E) {
        bo1.r = false;
        if (bo1.y) {
          switch (bo1.aj) {
            case 2:
              bo1.ak = 6;
              break;
            case 5:
              bo1.ak = 9;
              break;
            case 3:
              bo1.ak = 7;
              break;
            case 4:
              bo1.ak = 8;
              break;
            default:
              bo1.ak = bo1.aj;
              break;
          } 
        } else {
          bo1.ak = bo1.aj;
        } 
        bo1.D = 0.0F;
      } 
    } 
    boolean bool1 = (this.ak == 10 || this.ak == 13 || this.ak == 11 || this.ak == 12) ? true : false;
    float f2 = (this.r && bool1) ? this.F : this.D;
    float f3 = this.N * this.d.bP;
    float f4 = this.O * this.d.bP;
    f3 = paramOrthographicCamera.position.x - f3;
    float f1 = paramOrthographicCamera.position.y - f4;
    this.L = f3;
    this.M = f1;
    this.P = f3;
    this.Q = f1;
    if (lj.i(this.aW)) {
      t t;
      if ((t = b.a.a(this.aW)) == null)
        return; 
      TextureRegion textureRegion = t.a(this.ak, f2);
      Vector2 vector2 = t.a(this.ak, f2);
      if (textureRegion == null)
        return; 
      float f5 = f3 + vector2.x;
      float f6 = f1 + vector2.y;
      paramSpriteBatch.draw(textureRegion, MathUtils.round(f5), MathUtils.round(f6 + textureRegion.getRegionHeight()), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
      u u;
      if ((u = (u)t.i.get(Integer.valueOf(this.ak))) != null && u.s > 0)
        a(u.s, u.c, f3, f1, f2); 
      int m;
      ad ad1;
      if ((m = lj.g(this.aX)) != -1 && (ad1 = b.a.a(m)) != null) {
        textureRegion = ad1.e(f2);
        Vector2 vector21 = ad1.e(f2);
        if (textureRegion != null) {
          float f8 = f3 + vector21.x;
          float f7 = f1 + vector21.y;
          paramSpriteBatch.draw(textureRegion, MathUtils.round(f8), MathUtils.round(f7 + textureRegion.getRegionHeight()), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
          if (ad1.H > 0)
            a(ad1.H, ad1.e, f3, f1, f2); 
        } 
      } 
      a(paramSpriteBatch, f3, f1, f2);
      return;
    } 
    int i = 0;
    y y1 = null;
    y y2 = null;
    y y3 = null;
    if (b.a != null) {
      y1 = (this.ba != 0) ? b.a.a(this.ba) : null;
      y2 = (this.aZ != 0) ? b.a.a(this.aZ) : null;
      y3 = (this.aY != 0) ? b.a.a(this.aY) : null;
    } 
    if (y1 != null && y1.a(this.ak)) {
      i = ((z)y1.k.get(Integer.valueOf(this.ak))).b(f2);
    } else if (y2 != null && y2.a(this.ak)) {
      i = ((z)y2.k.get(Integer.valueOf(this.ak))).b(f2);
    } 
    boolean bool2 = false;
    if (this.ak != this.ad || i != this.ae || this.B == null) {
      String str;
      TextureRegion textureRegion;
      if ((textureRegion = bk.a(str = "" + this.r + "_" + this.r + "_" + this.ak)) != null) {
        this.B = textureRegion;
        this.ad = this.ak;
        this.ae = i;
      } else {
        List list = this.f;
        e.addAll(list);
        list.clear();
        int m;
        int[] arrayOfInt = (int[])(((m = this.ak) == 5 || m == 9 || m == 13) ? u : ((m == 4 || m == 8 || m == 12 || m == 2 || m == 6) ? v : w));
        if (y1 != null && y1.a(this.ak)) {
          z z;
          TextureRegion[] arrayOfTextureRegion = (z = (z)y1.k.get(Integer.valueOf(this.ak))).a(f2);
          Vector2[] arrayOfVector2 = z.a(f2);
          int[] arrayOfInt2 = z.b(f2);
          int[] arrayOfInt1 = z.a(f2);
          if (arrayOfTextureRegion != null)
            for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
              if (arrayOfTextureRegion[b] != null)
                this.f.add(a(arrayOfTextureRegion[b], arrayOfVector2[b], arrayOfInt2[b], arrayOfInt1[b], 0, arrayOfInt)); 
            }  
        } 
        if (y2 != null && y2.a(this.ak)) {
          z z;
          TextureRegion[] arrayOfTextureRegion = (z = (z)y2.k.get(Integer.valueOf(this.ak))).a(f2);
          Vector2[] arrayOfVector2 = z.a(f2);
          int[] arrayOfInt2 = z.b(f2);
          int[] arrayOfInt1 = z.a(f2);
          if (arrayOfTextureRegion != null)
            for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
              if (arrayOfTextureRegion[b] != null)
                this.f.add(a(arrayOfTextureRegion[b], arrayOfVector2[b], arrayOfInt2[b], arrayOfInt1[b], 1, arrayOfInt)); 
            }  
        } 
        if (y3 != null && y3.a(this.ak)) {
          z z;
          TextureRegion[] arrayOfTextureRegion = (z = (z)y3.k.get(Integer.valueOf(this.ak))).a(f2);
          Vector2[] arrayOfVector2 = z.a(f2);
          int[] arrayOfInt2 = z.b(f2);
          int[] arrayOfInt1 = z.a(f2);
          if (arrayOfTextureRegion != null)
            for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
              if (arrayOfTextureRegion[b] != null)
                this.f.add(a(arrayOfTextureRegion[b], arrayOfVector2[b], arrayOfInt2[b], arrayOfInt1[b], 2, arrayOfInt)); 
            }  
        } 
        this.f.sort(b);
        if (bk.f()) {
          boolean bool;
          if (bool = paramSpriteBatch.isDrawing())
            paramSpriteBatch.end(); 
          TextureRegion textureRegion1 = bk.a(str, this.f, this.m, this.n, this.o, this.p);
          if (bool)
            paramSpriteBatch.begin(); 
          this.B = textureRegion1;
          this.ad = this.ak;
          this.ae = i;
        } else {
          bool2 = true;
          for (byte b = 0; b < this.f.size(); b++) {
            bb bb;
            switch ((bb = this.f.get(b)).F) {
              case 1:
                paramSpriteBatch.setColor(this.m);
                break;
              case 2:
                paramSpriteBatch.setColor(this.n);
                break;
              case 3:
                paramSpriteBatch.setColor(this.o);
                break;
              case 4:
                paramSpriteBatch.setColor(this.p);
                break;
              default:
                paramSpriteBatch.setColor(Color.WHITE);
                break;
            } 
            paramSpriteBatch.draw(bb.j, f3 + bb.k.x, f1 + bb.k.y + bb.j.getRegionHeight(), bb.j.getRegionWidth(), -bb.j.getRegionHeight());
          } 
          paramSpriteBatch.setColor(Color.WHITE);
        } 
      } 
    } 
    if (!bool2 && this.B != null) {
      paramSpriteBatch.setColor(Color.WHITE);
      paramSpriteBatch.draw(this.B, f3 - 64.0F, f1 - 64.0F + 128.0F, 128.0F, -128.0F);
    } 
    int j;
    ad ad;
    if ((j = lj.g(this.aX)) != -1 && (ad = b.a.a(j)) != null) {
      TextureRegion textureRegion = ad.e(f2);
      Vector2 vector2 = ad.e(f2);
      if (textureRegion != null) {
        float f5 = f3 + vector2.x;
        float f6 = f1 + vector2.y;
        paramSpriteBatch.draw(textureRegion, MathUtils.round(f5), MathUtils.round(f6 + textureRegion.getRegionHeight()), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
        if (ad.H > 0)
          a(ad.H, ad.e, f3, f1, f2); 
      } 
    } 
    a(paramSpriteBatch, f3, f1, f2);
  }
  
  private static void a(int paramInt, Color paramColor, float paramFloat1, float paramFloat2, float paramFloat3) {
    q q;
    if ((q = (q)((b.a != null) ? b.a.a(paramInt) : null)) != null) {
      bc bc;
      (bc = new bc()).a = q;
      bc.l = paramColor;
      Vector2 vector2 = q.d(paramFloat3);
      bc.v = paramFloat1 + vector2.x;
      bc.w = paramFloat2 + vector2.y;
      az.b.add(bc);
    } 
  }
  
  private void a(SpriteBatch paramSpriteBatch, float paramFloat1, float paramFloat2, float paramFloat3) {
    if (this.v == null)
      return; 
    k k1;
    if ((k1 = (k)((this.a != null) ? this.a : b.a.a(593))) == null)
      return; 
    TextureRegion textureRegion;
    if ((textureRegion = k1.b(paramFloat3)) == null)
      return; 
    Vector2 vector2 = k1.b(paramFloat3);
    float f2 = this.d.bP;
    f2 = paramFloat1 + f2 - textureRegion.getRegionWidth();
    float f1 = paramFloat2 + vector2.y;
    paramSpriteBatch.draw(textureRegion, MathUtils.round(f2), MathUtils.round(f1 + textureRegion.getRegionHeight()), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
    if (k1.h > 0)
      a(k1.h, k1.a, paramFloat1, paramFloat2, paramFloat3); 
  }
  
  public final void c(SpriteBatch paramSpriteBatch, cq paramcq) {
    if (this.u != null) {
      Color color;
      String str1 = this.u;
      cq cq1 = paramcq;
      SpriteBatch spriteBatch = paramSpriteBatch;
      bo bo1 = this;
      if (str1 == null || str1.isEmpty())
        return; 
      String str2;
      BitmapFont bitmapFont = b.a((str2 = (str2 = (bo1.v != null) ? bo1.v : "").isEmpty() ? "" : (str2 + ":")).isEmpty() ? str1 : (str2 + " " + str2));
      switch (bo1.bh) {
        case 1:
          color = Color.WHITE;
          break;
        case 2:
          color = Color.CYAN;
          break;
        case 3:
          color = Color.valueOf("bee2ff");
          break;
        default:
          color = Color.YELLOW;
          break;
      } 
      float f2;
      float f3 = (f2 = cq1.bP) * 5.0F;
      float f4 = (bitmapFont.getData()).lineHeight;
      bitmapFont.getData().setLineHeight(f4 * 1.0F);
      if (bo1.b == null || !str1.equals(bo1.q)) {
        bo1.b = (Comparator)new GlyphLayout(bitmapFont, str1, color, f3, 1, true);
        bo1.q = str1;
      } 
      bitmapFont.getData().setLineHeight(f4);
      float f5 = bo1.Q + f2;
      float f6 = f2 * 1.2F;
      f5 -= f6;
      f2 = Math.round(bo1.P + f2 / 2.0F - f3 / 2.0F);
      f6 = (bitmapFont.getData()).scaleX;
      float f7 = (bitmapFont.getData()).scaleY;
      bitmapFont.getData().setScale(f6, -f7);
      float f8 = f5 - ((GlyphLayout)bo1.b).height;
      float f1 = f5 - ((GlyphLayout)bo1.b).height - f4;
      bitmapFont.setColor(Color.BLACK);
      bitmapFont.draw((Batch)spriteBatch, str1, f2 - 1.0F, f8, f3, 1, true);
      bitmapFont.draw((Batch)spriteBatch, str1, f2 + 1.0F, f8, f3, 1, true);
      bitmapFont.draw((Batch)spriteBatch, str1, f2, f8 - 1.0F, f3, 1, true);
      bitmapFont.draw((Batch)spriteBatch, str1, f2, f8 + 1.0F, f3, 1, true);
      bitmapFont.setColor(color);
      bitmapFont.draw((Batch)spriteBatch, str1, f2, f8, f3, 1, true);
      if (!str2.isEmpty()) {
        bitmapFont.setColor(Color.BLACK);
        bitmapFont.draw((Batch)spriteBatch, str2, f2 - 1.0F, f1, f3, 1, false);
        bitmapFont.draw((Batch)spriteBatch, str2, f2 + 1.0F, f1, f3, 1, false);
        bitmapFont.draw((Batch)spriteBatch, str2, f2, f1 - 1.0F, f3, 1, false);
        bitmapFont.draw((Batch)spriteBatch, str2, f2, f1 + 1.0F, f3, 1, false);
        bitmapFont.setColor(color);
        bitmapFont.draw((Batch)spriteBatch, str2, f2, f1, f3, 1, false);
      } 
      bitmapFont.getData().setScale(f6, f7);
      bitmapFont.setColor(Color.WHITE);
    } 
  }
  
  public final void a(String paramString1, String paramString2, int paramInt) {
    this.v = paramString1;
    this.u = paramString2;
    this.bh = paramInt;
    this.G = 0.0F;
  }
}
