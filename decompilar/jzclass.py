package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Interpolation;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public final class jz {
  private final Runnable p;
  
  public boolean bD = false;
  
  public float cb = 1.0F;
  
  public static jz b;
  
  public final cq m;
  
  private final Runnable q;
  
  private final Consumer e;
  
  public Group l;
  
  public Table F;
  
  public Actor f;
  
  public Label v;
  
  public Table G;
  
  public Table H;
  
  public jz(cq paramcq, Runnable paramRunnable1, Consumer paramConsumer, Runnable paramRunnable2) {
    this.m = paramcq;
    this.q = paramRunnable1;
    this.e = paramConsumer;
    this.p = paramRunnable2;
  }
  
  public final void cl() {
    if (this.l == null)
      return; 
    if (b == this)
      b = null; 
    try {
      if (this.F != null) {
        float f1 = this.F.getY();
        float f2 = -this.F.getWidth();
        this.F.addAction((Action)Actions.sequence((Action)Actions.moveTo(f2, f1, 0.2F, Interpolation.smooth), (Action)Actions.run(() -> {
                  if (this.l != null)
                    this.l.remove(); 
                  this.l = null;
                  this.F = null;
                  this.f = null;
                  if (this.p != null)
                    try {
                      this.p.run();
                      return;
                    } catch (Throwable throwable) {} 
                })));
        return;
      } 
      this.l.remove();
      this.l = null;
      this.F = null;
      this.f = null;
      if (this.p != null)
        try {
          this.p.run();
          return;
        } catch (Throwable throwable) {} 
      return;
    } catch (Throwable throwable) {
      return;
    } 
  }
  
  final void cm() {
    if (this.q != null)
      try {
        this.q.run();
        return;
      } catch (Throwable throwable) {} 
  }
  
  public final void b(List<String> paramList) {
    this.H.clearChildren();
    this.H.defaults().growX().padBottom(this.bD ? 2.0F : 0.0F);
    if (paramList == null)
      paramList = new ArrayList(); 
    for (byte b = 0; b < paramList.size(); b++) {
      int i = b + 1;
      String str = paramList.get(b);
      Table table1 = a(str, () -> {
            if (this.e != null)
              try {
                this.e.accept(Integer.valueOf(paramInt));
                return;
              } catch (Throwable throwable) {} 
          });
      this.H.add((Actor)table1).row();
    } 
    Table table = a(b.a(this.m.S, "id_npc_farewell"), () -> {
          if (this.e != null)
            try {
              this.e.accept(Integer.valueOf(0));
              return;
            } catch (Throwable throwable) {} 
        });
    this.H.add((Actor)table).row();
    this.H.invalidateHierarchy();
  }
  
  public final Label a(String paramString) {
    Label label;
    (label = lj.a((paramString != null) ? paramString : "", Color.WHITE, true, 1)).setFontScale(this.cb);
    return label;
  }
  
  private Table a(String paramString, Runnable paramRunnable) {
    float f1 = this.bD ? 0.0F : 8.0F;
    float f2 = this.m.bP * (this.bD ? this.m.am : 1.0F);
    f2 = this.bD ? f2 : this.m.ae;
    Table table;
    (table = new Table()).setBackground((Drawable)new NinePatchDrawable((NinePatch)b.h));
    table.setTouchable(Touchable.enabled);
    table.pad(0.0F, f1, 0.0F, f1);
    Label label;
    (label = lj.a((paramString != null) ? paramString : "", Color.WHITE, true, 1)).setFontScale(this.cb);
    table.add((Actor)label).expandX().fillX().center().minHeight(f2);
    if (b.m != null) {
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(b.m)))).setScaling(Scaling.fit);
      f1 = this.bD ? (this.cb * 1.5F) : 1.0F;
      f2 = 9.0F * f1;
      f1 = 23.0F * f1;
      float f = this.bD ? 16.0F : 4.0F;
      table.add((Actor)image).size(f2, f1).padRight(f).padLeft(8.0F).right();
    } 
    table.addListener((EventListener)new kf(this, table, paramRunnable));
    table.pack();
    return table;
  }
}
