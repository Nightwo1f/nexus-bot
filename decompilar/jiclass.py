package a;

import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;

final class ji extends Action {
  ji(Label paramLabel, TextField paramTextField) {}
  
  public final boolean act(float paramFloat) {
    this.u.setVisible(this.n.getText().isEmpty());
    return false;
  }
}
