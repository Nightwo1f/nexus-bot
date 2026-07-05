package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class kl extends ClickListener {
  kl(kg paramkg, kr paramkr) {}
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    try {
      int i4 = this.c.eB;
      int i3 = this.c.eA;
      int i2 = this.c.ez;
      int i1 = this.c.ey;
      int n = this.c.ex;
      int m = this.c.ew;
      int k = this.c.ev;
      int j = this.c.eu;
      int i = this.c.et;
      br br = this.g.o;
      il il;
      (il = new il()).aj(170);
      il.ak(j);
      il.ak(i);
      il.ak(k);
      il.ak(m);
      il.ak(i1);
      il.ak(n);
      il.ak(i2);
      il.ak(i3);
      il.ak(i4);
      br.b(il.a());
      this.g.o.G = true;
      this.g.o.L();
      return;
    } catch (Exception exception) {
      Gdx.app.error("OutfitShop0", "Falha ao enviar RequestSetOutfit", exception);
      return;
    } 
  }
}
