package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.Stack;
import com.badlogic.gdx.scenes.scene2d.ui.WidgetGroup;

final class ip extends WidgetGroup {
  ip(Stack paramStack, float paramFloat) {}
  
  public final void layout() {
    this.d.setSize(getWidth() / this.bR, getHeight() / this.bR);
    this.d.setPosition(0.0F, 0.0F);
  }
  
  public final float getPrefWidth() {
    return this.d.getPrefWidth() * this.bR;
  }
  
  public final float getPrefHeight() {
    return this.d.getPrefHeight() * this.bR;
  }
  
  public final Actor hit(float paramFloat1, float paramFloat2, boolean paramBoolean) {
    return (paramFloat1 < 0.0F || paramFloat1 >= getWidth() / this.bR || paramFloat2 < 0.0F || paramFloat2 >= getHeight() / this.bR) ? null : super.hit(paramFloat1, paramFloat2, paramBoolean);
  }
}
