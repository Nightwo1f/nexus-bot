package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.scenes.scene2d.ui.Label;

final class iv extends Label {
  iv(CharSequence paramCharSequence, Label.LabelStyle paramLabelStyle) {
    super(paramCharSequence, paramLabelStyle);
  }
  
  public final void draw(Batch paramBatch, float paramFloat) {
    float f1 = getX();
    float f2 = getY();
    Color color = (getStyle()).fontColor;
    (getStyle()).fontColor = Color.BLACK;
    setPosition(f1 + 1.0F, f2);
    super.draw(paramBatch, paramFloat);
    setPosition(f1 - 1.0F, f2);
    super.draw(paramBatch, paramFloat);
    setPosition(f1, f2 + 1.0F);
    super.draw(paramBatch, paramFloat);
    setPosition(f1, f2 - 1.0F);
    super.draw(paramBatch, paramFloat);
    (getStyle()).fontColor = color;
    setPosition(f1, f2);
    super.draw(paramBatch, paramFloat);
  }
}
