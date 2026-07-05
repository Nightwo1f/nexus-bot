package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import java.util.Iterator;

final class es extends ChangeListener {
  es(em paramem, NinePatchDrawable paramNinePatchDrawable1, NinePatchDrawable paramNinePatchDrawable2, int paramInt, et paramet, String paramString) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    Iterator<ImageButton> iterator = this.f.q.iterator();
    while (iterator.hasNext()) {
      ImageButton imageButton1;
      ((imageButton1 = iterator.next()).getStyle()).up = (Drawable)this.c;
      (imageButton1.getStyle()).down = (Drawable)this.c;
    } 
    ImageButton imageButton;
    ((imageButton = (ImageButton)paramActor).getStyle()).up = (Drawable)this.d;
    (imageButton.getStyle()).down = (Drawable)this.d;
    this.f.ci = this.cj;
    al.a(3);
    String str2 = (this.a.ae != null) ? this.a.ae : "id_warrior_description";
    String str1 = b.a(this.ad, str2);
    b.a(this.f.b, str1);
  }
}
