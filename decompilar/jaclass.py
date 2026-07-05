package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class ja extends ClickListener {
  ja(cr paramcr, TextField paramTextField, Stage paramStage, Runnable paramRunnable) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    if (this.t.a != null) {
      if (this.o != null)
        this.o.setKeyboardFocus((Actor)this.m); 
      this.m.getText();
    } 
  }
}
