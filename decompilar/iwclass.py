package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.Slider;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;

final class iw extends ChangeListener {
  iw(Slider paramSlider, Label paramLabel, jr paramjr) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    float f;
    String str = "" + Math.round((f = this.a.getValue()) * 100.0F) + "%";
    b.a(this.t, str);
    this.t.setText(str);
    if (this.b.c != null)
      this.b.c.accept(Float.valueOf(f)); 
  }
}
