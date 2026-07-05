package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.glutils.FrameBuffer;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.scenes.scene2d.Actor;
import java.util.ArrayList;
import java.util.Iterator;

public final class bl extends Actor {
  private int aN;
  
  private int am;
  
  public int aO;
  
  public int aP;
  
  public int aQ;
  
  public int aR;
  
  public int as;
  
  public int at;
  
  public int au;
  
  public int av;
  
  public int aw;
  
  private final cq c;
  
  public bl(cq paramcq) {
    this.c = paramcq;
    this.aN = 0;
    this.am = 0;
    this.aO = 0;
    this.aP = 0;
    this.aQ = 0;
    this.aR = 0;
    this.as = 0;
    this.at = 0;
    this.au = 0;
    this.av = 0;
    this.aw = 0;
    float f = paramcq.bP;
    setSize(f, f);
  }
  
  public final void b(int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, int paramInt6, int paramInt7, int paramInt8, int paramInt9, int paramInt10, int paramInt11) {
    this.am = paramInt1;
    this.aN = paramInt2;
    this.aO = paramInt3;
    this.aP = paramInt4;
    this.aQ = paramInt5;
    this.aR = paramInt6;
    this.as = paramInt7;
    this.at = paramInt8;
    this.au = paramInt9;
    this.av = paramInt10;
    this.aw = paramInt11;
  }
  
  public final void draw(Batch paramBatch, float paramFloat) {
    float f2;
    if (!(paramBatch instanceof SpriteBatch))
      return; 
    SpriteBatch spriteBatch = (SpriteBatch)paramBatch;
    paramFloat = getX();
    float f1 = getY();
    Vector2 vector2 = new Vector2(0.0F, 0.0F);
    if (lj.i(this.aN)) {
      t t;
      if ((t = (t)((b.a != null) ? b.a.a(this.aN) : null)) == null)
        return; 
      TextureRegion textureRegion = t.a(3, 0.0F);
      Vector2 vector21;
      if ((vector21 = t.a(3, 0.0F)) == null)
        vector21 = vector2; 
      if (textureRegion == null)
        return; 
      float f3 = paramFloat + vector21.x;
      float f4 = f1 + vector21.y;
      spriteBatch.draw(textureRegion, MathUtils.round(f3), MathUtils.round(f4 + textureRegion.getRegionHeight()), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
      u u;
      if ((u = (u)t.i.get(Integer.valueOf(3))) != null && u.s > 0) {
        q q;
        if ((q = (q)((b.a != null) ? b.a.a(u.s) : null)) != null) {
          TextureRegion textureRegion1 = q.d(0.0F);
          Vector2 vector22;
          if ((vector22 = q.d(0.0F)) == null)
            vector22 = vector2; 
          float f5 = this.c.bP;
          float f6 = paramFloat + vector22.x - f5 / 2.0F;
          float f7 = f1 + vector22.y - f5 / 2.0F;
          if (textureRegion1 != null) {
            spriteBatch.flush();
            Gdx.gl.glEnable(3042);
            spriteBatch.setBlendFunction(770, 1);
            spriteBatch.setColor(u.c);
            spriteBatch.draw(textureRegion1, MathUtils.round(f6), MathUtils.round(f7), textureRegion1.getRegionWidth(), textureRegion1.getRegionHeight());
            spriteBatch.setColor(Color.WHITE);
            Gdx.gl.glDisable(3042);
          } 
        } 
      } 
      int j;
      if (this.am != 0 && this.am != 1 && (j = lj.g(this.am)) != -1) {
        ad ad;
        if ((ad = (ad)((b.a != null) ? b.a.a(j) : null)) != null) {
          TextureRegion textureRegion1 = ad.e(0.0F);
          Vector2 vector22;
          if ((vector22 = ad.e(0.0F)) == null)
            vector22 = vector2; 
          if (textureRegion1 != null) {
            float f5 = paramFloat + vector22.x;
            float f6 = f1 + vector22.y;
            spriteBatch.draw(textureRegion1, MathUtils.round(f5), MathUtils.round(f6 + textureRegion1.getRegionHeight()), textureRegion1.getRegionWidth(), -textureRegion1.getRegionHeight());
            if (ad.H > 0) {
              q q;
              if ((q = (q)((b.a != null) ? b.a.a(ad.H) : null)) != null) {
                TextureRegion textureRegion2 = q.d(0.0F);
                Vector2 vector23;
                if ((vector23 = q.d(0.0F)) == null)
                  vector23 = vector2; 
                if (textureRegion2 != null) {
                  f2 = this.c.bP;
                  paramFloat = paramFloat + vector23.x - f2 / 2.0F;
                  f1 = f1 + vector23.y - f2 / 2.0F;
                  spriteBatch.flush();
                  Gdx.gl.glEnable(3042);
                  spriteBatch.setBlendFunction(770, 1);
                  spriteBatch.setColor(ad.e);
                  spriteBatch.draw(textureRegion2, MathUtils.round(paramFloat), MathUtils.round(f1));
                  spriteBatch.setColor(Color.WHITE);
                  Gdx.gl.glDisable(3042);
                } 
              } 
            } 
          } 
        } 
      } 
      return;
    } 
    (new int[8])[0] = 4;
    (new int[8])[1] = 3;
    (new int[8])[2] = 0;
    (new int[8])[3] = 6;
    (new int[8])[4] = 8;
    (new int[8])[5] = 9;
    (new int[8])[6] = 2;
    (new int[8])[7] = 5;
    (new int[8])[0] = 5;
    (new int[8])[1] = 3;
    (new int[8])[2] = 0;
    (new int[8])[3] = 6;
    (new int[8])[4] = 8;
    (new int[8])[5] = 9;
    (new int[8])[6] = 2;
    (new int[8])[7] = 4;
    (new int[8])[0] = 3;
    (new int[8])[1] = 0;
    (new int[8])[2] = 6;
    (new int[8])[3] = 8;
    (new int[8])[4] = 9;
    (new int[8])[5] = 2;
    (new int[8])[6] = 4;
    (new int[8])[7] = 5;
    String str;
    int[] arrayOfInt = ((str = "3").equals("5") || str.equals("9") || str.equals("13")) ? new int[8] : ((str.equals("4") || str.equals("8") || str.equals("12") || str.equals("2") || str.equals("6")) ? new int[8] : new int[8]);
    ArrayList<bn> arrayList = new ArrayList();
    y y;
    z z;
    if (this.aQ != 0 && b.a != null && (y = b.a.a(this.aQ)) != null && (z = (z)y.k.get(Integer.valueOf(3))) != null) {
      TextureRegion[] arrayOfTextureRegion = z.a(0.0F);
      Vector2[] arrayOfVector2 = z.a(0.0F);
      int[] arrayOfInt2 = z.b(0.0F);
      int[] arrayOfInt1 = z.a(0.0F);
      if (arrayOfTextureRegion != null)
        for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
          TextureRegion textureRegion;
          if ((textureRegion = arrayOfTextureRegion[b]) != null) {
            Vector2 vector21 = (Vector2)((arrayOfVector2 != null && b < arrayOfVector2.length && arrayOfVector2[b] != null) ? arrayOfVector2[b] : f2);
            boolean bool1 = (arrayOfInt2 != null && b < arrayOfInt2.length) ? arrayOfInt2[b] : false;
            boolean bool2 = (arrayOfInt1 != null && b < arrayOfInt1.length) ? arrayOfInt1[b] : false;
            arrayList.add(new bn(this, textureRegion, vector21, bool1, bool2, 0));
          } 
        }  
    } 
    if (this.aP != 0 && b.a != null && (y = b.a.a(this.aP)) != null && (z = (z)y.k.get(Integer.valueOf(3))) != null) {
      TextureRegion[] arrayOfTextureRegion = z.a(0.0F);
      Vector2[] arrayOfVector2 = z.a(0.0F);
      int[] arrayOfInt2 = z.b(0.0F);
      int[] arrayOfInt1 = z.a(0.0F);
      if (arrayOfTextureRegion != null)
        for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
          TextureRegion textureRegion;
          if ((textureRegion = arrayOfTextureRegion[b]) != null) {
            Vector2 vector21 = (Vector2)((arrayOfVector2 != null && b < arrayOfVector2.length && arrayOfVector2[b] != null) ? arrayOfVector2[b] : f2);
            boolean bool1 = (arrayOfInt2 != null && b < arrayOfInt2.length) ? arrayOfInt2[b] : false;
            boolean bool2 = (arrayOfInt1 != null && b < arrayOfInt1.length) ? arrayOfInt1[b] : false;
            arrayList.add(new bn(this, textureRegion, vector21, bool1, bool2, 1));
          } 
        }  
    } 
    if (this.aO != 0 && b.a != null && (y = b.a.a(this.aO)) != null && (z = (z)y.k.get(Integer.valueOf(3))) != null) {
      TextureRegion[] arrayOfTextureRegion = z.a(0.0F);
      Vector2[] arrayOfVector2 = z.a(0.0F);
      int[] arrayOfInt2 = z.b(0.0F);
      int[] arrayOfInt1 = z.a(0.0F);
      if (arrayOfTextureRegion != null)
        for (byte b = 0; b < arrayOfTextureRegion.length; b++) {
          TextureRegion textureRegion;
          if ((textureRegion = arrayOfTextureRegion[b]) != null) {
            Vector2 vector21 = (Vector2)((arrayOfVector2 != null && b < arrayOfVector2.length && arrayOfVector2[b] != null) ? arrayOfVector2[b] : f2);
            boolean bool1 = (arrayOfInt2 != null && b < arrayOfInt2.length) ? arrayOfInt2[b] : false;
            boolean bool2 = (arrayOfInt1 != null && b < arrayOfInt1.length) ? arrayOfInt1[b] : false;
            arrayList.add(new bn(this, textureRegion, vector21, bool1, bool2, 2));
          } 
        }  
    } 
    arrayList.sort(new bm(this, arrayOfInt));
    Iterator<bn> iterator = arrayList.iterator();
    while (iterator.hasNext()) {
      float f5;
      bn bn;
      switch ((bn = iterator.next()).aT) {
        case 1:
          f3 = (this.at >> 16 & 0xFF) / 255.0F;
          f4 = (this.at >> 8 & 0xFF) / 255.0F;
          f5 = (this.at & 0xFF) / 255.0F;
          spriteBatch.setColor(f3, f4, f5, 1.0F);
          break;
        case 2:
          f3 = (this.as >> 16 & 0xFF) / 255.0F;
          f4 = (this.as >> 8 & 0xFF) / 255.0F;
          f5 = (this.as & 0xFF) / 255.0F;
          spriteBatch.setColor(f3, f4, f5, 1.0F);
          break;
        case 3:
          f3 = (this.au >> 16 & 0xFF) / 255.0F;
          f4 = (this.au >> 8 & 0xFF) / 255.0F;
          f5 = (this.au & 0xFF) / 255.0F;
          spriteBatch.setColor(f3, f4, f5, 1.0F);
          break;
        case 4:
          f3 = (this.av >> 16 & 0xFF) / 255.0F;
          f4 = (this.av >> 8 & 0xFF) / 255.0F;
          f5 = (this.av & 0xFF) / 255.0F;
          spriteBatch.setColor(f3, f4, f5, 1.0F);
          break;
        default:
          spriteBatch.setColor(Color.WHITE);
          break;
      } 
      float f3 = paramFloat + bn.l.x;
      float f4 = f1 + bn.l.y;
      spriteBatch.draw(bn.C, MathUtils.round(f3), MathUtils.round(f4 + bn.C.getRegionHeight()), bn.C.getRegionWidth(), -bn.C.getRegionHeight());
    } 
    spriteBatch.setColor(Color.WHITE);
    int i;
    if (this.am != 0 && this.am != 1 && (i = lj.g(this.am)) != -1) {
      ad ad;
      if ((ad = (ad)((b.a != null) ? b.a.a(i) : null)) != null) {
        float f;
        TextureRegion textureRegion = ad.e(0.0F);
        Vector2 vector21;
        if ((vector21 = ad.e(0.0F)) == null)
          f = f2; 
        if (textureRegion != null) {
          float f4 = paramFloat + f.x;
          float f3 = f1 + f.y;
          spriteBatch.draw(textureRegion, MathUtils.round(f4), MathUtils.round(f3 + textureRegion.getRegionHeight()), textureRegion.getRegionWidth(), -textureRegion.getRegionHeight());
          if (ad.H > 0) {
            q q;
            if ((q = (q)((b.a != null) ? b.a.a(ad.H) : null)) != null) {
              float f5;
              TextureRegion textureRegion1 = q.d(0.0F);
              Vector2 vector22;
              if ((vector22 = q.d(0.0F)) == null)
                f5 = f2; 
              if (textureRegion1 != null) {
                float f6 = paramFloat + f5.x - this.c.bP / 2.0F;
                float f7 = f1 + f5.y - this.c.bP / 2.0F;
                spriteBatch.flush();
                Gdx.gl.glEnable(3042);
                spriteBatch.setBlendFunction(770, 1);
                spriteBatch.setColor(ad.e);
                spriteBatch.draw(textureRegion1, MathUtils.round(f6), MathUtils.round(f7));
                spriteBatch.setColor(Color.WHITE);
                Gdx.gl.glDisable(3042);
              } 
            } 
          } 
        } 
      } 
    } 
  }
  
  public final Texture b() {
    int i = this.c.bP;
    int j = this.c.bP;
    FrameBuffer frameBuffer;
    (frameBuffer = new FrameBuffer(Pixmap.Format.RGBA8888, i, j, false)).begin();
    Gdx.gl.glClearColor(0.0F, 0.0F, 0.0F, 0.0F);
    Gdx.gl.glClear(16384);
    OrthographicCamera orthographicCamera;
    (orthographicCamera = new OrthographicCamera(i, j)).setToOrtho(false, i, j);
    orthographicCamera.update();
    SpriteBatch spriteBatch;
    (spriteBatch = new SpriteBatch()).setProjectionMatrix(orthographicCamera.combined);
    spriteBatch.begin();
    setPosition(i / 2.0F - getWidth() / 2.0F, j / 2.0F - getHeight() / 2.0F);
    draw((Batch)spriteBatch, 1.0F);
    spriteBatch.end();
    Pixmap pixmap = Pixmap.createFromFrameBuffer(0, 0, i, j);
    Texture texture = new Texture(pixmap);
    pixmap.dispose();
    frameBuffer.end();
    spriteBatch.dispose();
    frameBuffer.dispose();
    return texture;
  }
}
