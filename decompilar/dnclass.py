package a;

import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop;

final class dn extends DragAndDrop.Source {
  float an;
  
  float ao;
  
  dn(dl paramdl, Actor paramActor, Group paramGroup, int paramInt, Stage paramStage) {
    super(paramActor);
  }
  
  public final DragAndDrop.Payload dragStart(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    if (!this.b.af)
      return null; 
    this.a.toFront();
    this.an = paramFloat1;
    this.ao = paramFloat2;
    DragAndDrop.Payload payload;
    (payload = new DragAndDrop.Payload()).setObject(Integer.valueOf(this.ce));
    Actor actor;
    (actor = new Actor()).setSize(0.0F, 0.0F);
    payload.setDragActor(actor);
    return payload;
  }
  
  public final void drag(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    paramFloat1 = paramInputEvent.getStageX() - this.an;
    float f = paramInputEvent.getStageY() - this.ao;
    paramFloat1 = MathUtils.clamp(paramFloat1, 0.0F, this.e.getWidth() - this.a.getWidth());
    f = MathUtils.clamp(f, 0.0F, this.e.getHeight() - this.a.getHeight());
    this.a.setPosition(paramFloat1, f);
  }
  
  public final void dragStop(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt, DragAndDrop.Payload paramPayload, DragAndDrop.Target paramTarget) {
    if (this.b.af) {
      this.b.l[this.ce] = this.a.getX();
      this.b.m[this.ce] = this.a.getY();
      this.b.a(this.e.getWidth(), this.e.getHeight());
    } 
  }
}
