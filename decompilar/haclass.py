package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;

final class ha extends DragAndDrop.Source {
  ha(gb paramgb, Actor paramActor, int paramInt) {
    super(paramActor);
  }
  
  public final DragAndDrop.Payload dragStart(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    if (!this.z.q())
      return null; 
    Image image2;
    if ((image2 = this.z.C[this.dM - 1]) == null)
      return null; 
    DragAndDrop.Payload payload;
    (payload = new DragAndDrop.Payload()).setObject(new hq(false, this.dM));
    float f2 = ((cq)this.z.j).bP;
    n n;
    TextureRegion textureRegion;
    float f3 = ((textureRegion = (TextureRegion)(((n = (n)((b.a != null) ? b.a.a(image2) : null)) != null) ? n.c(0.0F) : null)) != null) ? textureRegion.getRegionWidth() : f2;
    float f4 = (textureRegion != null) ? textureRegion.getRegionHeight() : f2;
    Image image1;
    (image1 = new Image((textureRegion != null) ? (Drawable)new TextureRegionDrawable(textureRegion) : (Drawable)this.z.i)).setScaling(Scaling.none);
    image1.setSize(f3, f4);
    payload.setDragActor((Actor)image1);
    float f1 = (f2 - f3) * 0.5F;
    f2 = (f2 - f4) * 0.5F;
    f1 = paramFloat1 - f1;
    paramFloat1 = paramFloat2 - f2;
    this.z.b.setDragActorPosition(-f1, -paramFloat1);
    this.z.aS = true;
    return payload;
  }
  
  public final void dragStop(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt, DragAndDrop.Payload paramPayload, DragAndDrop.Target paramTarget) {
    this.z.aS = false;
  }
}
