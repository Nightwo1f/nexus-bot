package a;

import com.badlogic.gdx.InputAdapter;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.utils.TimeUtils;
import java.util.Comparator;
import java.util.List;

final class fl extends InputAdapter {
  fl(fj paramfj, cq paramcq) {}
  
  public final boolean touchDown(int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
    float f1;
    float f2;
    if (this.e.k())
      return true; 
    if (this.e.ap && this.e.a instanceof dl)
      ((dl)this.e.a).ay(); 
    this.e.a.av();
    this.e.o.set(paramInt1, paramInt2);
    Vector2 vector2;
    if ((vector2 = this.e.i.screenToStageCoordinates(this.e.o)).x < 0.0F || vector2.y < 0.0F || vector2.x >= this.e.i.getWidth() || vector2.y >= this.e.i.getHeight()) {
      if (this.e.b != null)
        this.e.aL(); 
      return true;
    } 
    Actor actor;
    if ((actor = this.e.i.hit(vector2.x, vector2.y, true)) != null && actor != this.e.b)
      return false; 
    if (this.e.b != null) {
      f1 = vector2.x - this.e.b.getX();
      f2 = vector2.y - this.e.b.getY();
      if (this.e.b.hit(f1, f2, true) == null) {
        this.e.aL();
        return true;
      } 
      return false;
    } 
    if (paramInt4 == 1) {
      this.e.p(f1, f2);
      return true;
    } 
    if (paramInt4 == 0) {
      if (this.e.cx != -1)
        return false; 
      this.e.cx = paramInt3;
      this.e.ar = true;
      this.e.as = false;
      this.e.at = false;
      this.e.n = TimeUtils.millis();
      this.e.cu = f1;
      this.e.cv = f2;
      this.e.cw = paramInt4;
      return true;
    } 
    this.e.b.set(f1, f2, 0.0F);
    byte[] arrayOfByte = this.e.b;
    this.e.b.unproject((Vector3)arrayOfByte, this.e.a.getScreenX(), this.e.a.getScreenY(), this.e.a.getScreenWidth(), this.e.a.getScreenHeight());
    int j = (int)Math.floor((((Vector3)arrayOfByte).x / this.i.bP));
    int i = (int)Math.floor((((Vector3)arrayOfByte).y / this.i.bP));
    be be1 = new be(j, i, this.i.aF);
    az az = this.e.a(be1);
    if (paramInt4 == 0 && az != null)
      return this.e.a(az, be1); 
    if (paramInt4 == 0 && !this.i.Y)
      return true; 
    this.e.aX();
    this.e.aM();
    this.e.c = (Comparator)be1;
    this.e.av = this.e.b(be1);
    this.e.e = this.e.d(be1) ? be1 : null;
    this.e.f.add(new fu(be1, this.e.D));
    be be2 = this.e.c();
    List list;
    if ((list = this.e.a.a(be2, be1, true, true, false)) != null)
      this.e.b.addAll(list); 
    if (this.e.b.isEmpty() && this.e.p == 0L && !this.e.aq) {
      this.e.a.D();
      this.e.aA = 0.0F;
    } 
    return true;
  }
  
  public final boolean touchDragged(int paramInt1, int paramInt2, int paramInt3) {
    if (paramInt3 != this.e.cx)
      return false; 
    if (!this.e.ar)
      return false; 
    if (this.e.k())
      return true; 
    float f = Math.max(12.0F, this.i.bP * 0.35F);
    paramInt1 -= this.e.cu;
    paramInt2 -= this.e.cv;
    if (!this.e.as) {
      if (Math.abs(paramInt1) < f && Math.abs(paramInt2) < f)
        return true; 
      this.e.as = true;
      paramInt1 = fj.a(paramInt1, paramInt2);
      this.e.a(paramInt3, paramInt1);
      return true;
    } 
    this.e.b = fj.a(paramInt1, paramInt2);
    return true;
  }
  
  public final boolean touchUp(int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
    if (paramInt3 != this.e.cx)
      return false; 
    this.e.cx = -1;
    if (!this.e.ar)
      return false; 
    if (paramInt4 != this.e.cw)
      return false; 
    if (this.e.at) {
      this.e.ar = false;
      return true;
    } 
    this.e.ar = false;
    if (this.e.as) {
      this.e.as = false;
      this.e.Q(paramInt3);
      return true;
    } 
    if (this.e.k())
      return true; 
    this.e.b.set(paramInt1, paramInt2, 0.0F);
    byte[] arrayOfByte = this.e.b;
    this.e.b.unproject((Vector3)arrayOfByte, this.e.a.getScreenX(), this.e.a.getScreenY(), this.e.a.getScreenWidth(), this.e.a.getScreenHeight());
    paramInt2 = (int)Math.floor((((Vector3)arrayOfByte).x / this.i.bP));
    int i = (int)Math.floor((((Vector3)arrayOfByte).y / this.i.bP));
    be be1 = new be(paramInt2, i, this.i.aF);
    az az;
    if ((az = this.e.a(be1)) != null)
      return this.e.a(az, be1); 
    if (!this.i.Y)
      return true; 
    this.e.aX();
    this.e.aM();
    this.e.c = (Comparator)be1;
    this.e.av = this.e.b(be1);
    this.e.e = this.e.d(be1) ? be1 : null;
    this.e.f.add(new fu(be1, this.e.D));
    boolean bool = (az == null) ? true : false;
    be be2 = this.e.c();
    List list;
    if ((list = this.e.a.a(be2, be1, true, bool, false)) != null)
      this.e.b.addAll(list); 
    if (this.e.b.isEmpty() && this.e.p == 0L && !this.e.aq) {
      this.e.a.D();
      this.e.aA = 0.0F;
    } 
    return true;
  }
}
