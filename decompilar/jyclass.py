package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.g2d.freetype.FreeTypeFontGenerator;
import com.badlogic.gdx.math.Vector2;

public final class jy {
  private static final jy a = new jy();
  
  public boolean az = false;
  
  public static jy a() {
    return a;
  }
  
  public final void a(SpriteBatch paramSpriteBatch, Vector2 paramVector2, float paramFloat1, float paramFloat2, float paramFloat3, cq paramcq) {
    if (b.b == null)
      return; 
    float f3 = paramFloat1 * 1.0F;
    float f4 = paramFloat1 * 1.8F;
    float f2 = paramcq.ad;
    float f5 = paramVector2.x - paramFloat1 * f2;
    paramFloat1 = paramVector2.x + paramFloat1 * f2 - f3;
    float f1 = paramVector2.y - f4 / 2.0F;
    paramSpriteBatch.setColor(0.0F, 0.0F, 0.0F, 0.45F);
    FreeTypeFontGenerator freeTypeFontGenerator = b.b;
    paramSpriteBatch.draw((TextureRegion)freeTypeFontGenerator, f5, f1, f3, f4);
    paramSpriteBatch.draw(freeTypeFontGenerator.getTexture(), paramFloat1, f1, f3, f4, freeTypeFontGenerator.getU2(), freeTypeFontGenerator.getV(), freeTypeFontGenerator.getU(), freeTypeFontGenerator.getV2());
    Color color2 = (paramFloat2 > 0.5F) ? Color.GREEN : ((paramFloat2 > 0.25F) ? Color.YELLOW : Color.RED);
    paramSpriteBatch.setColor(color2);
    a(paramSpriteBatch, (TextureRegion)freeTypeFontGenerator, f5, f1, f3, f4, paramFloat2, false);
    Color color1 = this.az ? Color.GRAY : Color.ROYAL;
    paramSpriteBatch.setColor(color1);
    a(paramSpriteBatch, (TextureRegion)freeTypeFontGenerator, paramFloat1, f1, f3, f4, paramFloat3, true);
    paramSpriteBatch.setColor(Color.WHITE);
  }
  
  private static void a(SpriteBatch paramSpriteBatch, TextureRegion paramTextureRegion, float paramFloat1, float paramFloat2, float paramFloat3, float paramFloat4, float paramFloat5, boolean paramBoolean) {
    if (paramFloat5 <= 0.0F)
      return; 
    if (paramFloat5 > 1.0F)
      paramFloat5 = 1.0F; 
    float f2 = paramFloat4 * paramFloat5;
    paramFloat2 += paramFloat4 - f2;
    paramFloat4 = paramTextureRegion.getV2() - paramTextureRegion.getV();
    paramFloat4 = paramTextureRegion.getV2() - paramFloat4 * paramFloat5;
    paramFloat5 = paramBoolean ? paramTextureRegion.getU2() : paramTextureRegion.getU();
    float f1 = paramBoolean ? paramTextureRegion.getU() : paramTextureRegion.getU2();
    paramSpriteBatch.draw(paramTextureRegion.getTexture(), paramFloat1, paramFloat2, paramFloat3, f2, paramFloat5, paramFloat4, f1, paramTextureRegion.getV2());
  }
}
