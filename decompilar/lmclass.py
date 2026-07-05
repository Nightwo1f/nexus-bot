package a;

import com.badlogic.gdx.scenes.scene2d.ui.WidgetGroup;

final class lm extends WidgetGroup {
  protected final void sizeChanged() {
    super.sizeChanged();
    ll.g(getWidth(), getHeight());
  }
}
