package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Matrix4;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public final class ch {
  public final List m = new ArrayList();
  
  public final BitmapFont g;
  
  public final GlyphLayout d;
  
  private int bt = Integer.MIN_VALUE;
  
  private final float R = 1.1F;
  
  private final float S = 1.0F;
  
  private final float T = 1.0F;
  
  private final float U = 1.0F;
  
  private final Color q = new Color(Color.WHITE);
  
  private final Color r = new Color(0.0F, 0.0F, 0.0F, 1.0F);
  
  private final Color s = new Color(0.0F, 0.0F, 0.0F, 1.0F);
  
  private final Matrix4 c = new Matrix4();
  
  private final Matrix4 d = (Matrix4)new GlyphLayout();
  
  public ch(BitmapFont paramBitmapFont) {
    this.d = new Matrix4();
    this.g = paramBitmapFont;
    this.g.getData().setScale(1.0F);
    this.g.setUseIntegerPositions(true);
  }
  
  public final void b(SpriteBatch paramSpriteBatch, cq paramcq, float paramFloat) {
    int i;
    if ((i = paramcq.aF) != this.bt) {
      this.m.clear();
      this.bt = i;
    } 
    this.d.set(paramSpriteBatch.getProjectionMatrix());
    while (this.m.size() > 50)
      this.m.remove(0); 
    Iterator<ci> iterator = this.m.iterator();
    while (iterator.hasNext()) {
      ci ci = iterator.next();
      float f1;
      if ((f1 = paramFloat - ci.V) >= 1.1F) {
        iterator.remove();
        continue;
      } 
      float f3;
      f1 = ((f3 = f1 / 1.1F) < 0.0F) ? 0.0F : ((f3 > 1.0F) ? 1.0F : f3);
      float f2 = paramcq.bP * 1.0F;
      f1 *= f2;
      f2 = ci.Y * 1.1F;
      f2 = ci.W - f2 / 2.0F;
      f1 = ci.X - f1;
      f2 = Math.round(f2);
      f1 = Math.round(f1);
      switch (ci.bu) {
        case 2:
        
        case 3:
        
        default:
          break;
      } 
      Color color1 = Color.WHITE;
      this.q.set(color1.r, color1.g, color1.b, 1.0F);
      this.g.getData().setScale(1.1F);
      this.c.set(this.d);
      this.c.translate(f2, f1, 0.0F);
      this.c.scale(1.0F, -1.0F, 1.0F);
      this.c.translate(-f2, -f1, 0.0F);
      paramSpriteBatch.setProjectionMatrix(this.c);
      boolean bool2 = ci.J;
      Color color2 = this.q;
      float f4 = f1;
      f2 = f2;
      boolean bool1 = ci.J;
      SpriteBatch spriteBatch = paramSpriteBatch;
      ch ch1 = this;
      if (bool2) {
        ch1.s.a = 0.55F;
        ch1.g.setColor(ch1.s);
        ch1.g.draw((Batch)spriteBatch, bool1, f2 + 1.0F, f4 - 1.0F);
        ch1.r.a = 0.9F;
        ch1.g.setColor(ch1.r);
        ch1.g.draw((Batch)spriteBatch, bool1, f2 - 1.0F, f4);
        ch1.g.draw((Batch)spriteBatch, bool1, f2 + 1.0F, f4);
        ch1.g.draw((Batch)spriteBatch, bool1, f2, f4 - 1.0F);
        ch1.g.draw((Batch)spriteBatch, bool1, f2, f4 + 1.0F);
        ch1.g.draw((Batch)spriteBatch, bool1, f2 - 1.0F, f4 - 1.0F);
        ch1.g.draw((Batch)spriteBatch, bool1, f2 + 1.0F, f4 - 1.0F);
        ch1.g.draw((Batch)spriteBatch, bool1, f2 - 1.0F, f4 + 1.0F);
        ch1.g.draw((Batch)spriteBatch, bool1, f2 + 1.0F, f4 + 1.0F);
      } 
      ch1.g.setColor(color2);
      ch1.g.draw((Batch)spriteBatch, bool1, f2, f4);
      paramSpriteBatch.setProjectionMatrix(this.d);
    } 
    this.g.getData().setScale(1.0F);
    this.g.setColor(Color.WHITE);
  }
}
