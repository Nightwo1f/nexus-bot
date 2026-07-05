package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.scenes.scene2d.Actor;

public final class ho extends Actor {
  private int dR = 532;
  
  private float D = 0.0F;
  
  public final void act(float paramFloat) {
    super.act(paramFloat);
    if (isVisible())
      this.D += paramFloat; 
  }
  
  public final void draw(Batch paramBatch, float paramFloat) {
    if (b.a == null)
      return; 
    k k;
    if ((k = b.a.a(this.dR)) == null)
      return; 
    TextureRegion textureRegion;
    if ((textureRegion = k.b(this.D)) != null) {
      Color color = getColor();
      paramBatch.setColor(color.r, color.g, color.b, color.a * paramFloat);
      paramFloat = textureRegion.getRegionWidth();
      float f2 = textureRegion.getRegionHeight();
      Vector2 vector2 = k.b(this.D);
      float f3 = getScaleX();
      float f4 = getScaleY();
      float f5 = getX() + vector2.x * f3;
      float f1 = getY() + (getHeight() - vector2.y - f2) * f4;
      paramFloat *= f3;
      f2 *= f4;
      paramBatch.draw(textureRegion, f5, f1, paramFloat, f2);
      paramBatch.setColor(Color.WHITE);
    } 
  }
}
