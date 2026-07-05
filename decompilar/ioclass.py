package a;

import com.badlogic.gdx.scenes.scene2d.ui.HorizontalGroup;

final class io extends HorizontalGroup {
  public final float getPrefHeight() {
    float f;
    if (getWrap() && (f = getWidth()) <= 1.0F) {
      float f1 = (in.bQ > 0.0F) ? in.bQ : 800.0F;
      setWidth(f1);
      invalidate();
      f1 = super.getPrefHeight();
      setWidth(f);
      invalidate();
      return f1;
    } 
    return super.getPrefHeight();
  }
}
