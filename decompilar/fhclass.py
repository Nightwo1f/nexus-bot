package a;

import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;

final class fh extends ChangeListener {
  boolean am = true;
  
  fh(eu parameu, ImageButton paramImageButton, TextureRegionDrawable paramTextureRegionDrawable1, TextureRegionDrawable paramTextureRegionDrawable2, TextureRegionDrawable paramTextureRegionDrawable3, TextureRegionDrawable paramTextureRegionDrawable4) {}
  
  public final void changed(ChangeListener.ChangeEvent paramChangeEvent, Actor paramActor) {
    al.a(3);
    this.am = !this.am;
    this.m.g.setPasswordMode(this.am);
    (this.g.getStyle()).imageUp = this.am ? (Drawable)this.a : (Drawable)this.b;
    (this.g.getStyle()).imageDown = this.am ? (Drawable)this.c : (Drawable)this.d;
  }
}
