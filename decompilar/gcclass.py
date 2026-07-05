package a;

import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

final class gc extends InputListener {
  gc(gb paramgb) {}
  
  public final boolean keyDown(InputEvent paramInputEvent, int paramInt) {
    if (this.b.q()) {
      if (paramInt == 29 || paramInt == 21) {
        this.b.bs();
        return true;
      } 
      if (paramInt == 32 || paramInt == 22) {
        this.b.bt();
        return true;
      } 
    } 
    if (paramInt != 111)
      return false; 
    if (this.b.aW && this.b.aX)
      return true; 
    if (this.b.r()) {
      this.b.bz();
      return true;
    } 
    if (this.b.q()) {
      this.b.bu();
      return true;
    } 
    if (this.b.c != null) {
      this.b.br();
      return true;
    } 
    if (this.b.aU) {
      this.b.bf();
      return true;
    } 
    if (!in.t()) {
      this.b.bg();
      return true;
    } 
    return false;
  }
}
