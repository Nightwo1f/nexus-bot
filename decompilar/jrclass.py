package a;

import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import java.util.function.Consumer;
import java.util.function.Supplier;

public final class jr implements js {
  final int el;
  
  final int em;
  
  final String aA;
  
  final String aB;
  
  final String aC;
  
  final Runnable l;
  
  final boolean bv;
  
  final TextureRegion H;
  
  final Integer d;
  
  final Integer e;
  
  final jn b;
  
  String ar;
  
  final boolean bw;
  
  final Consumer b;
  
  final float bW;
  
  final float bX;
  
  final float bY;
  
  final Supplier a;
  
  final Consumer c;
  
  final Runnable m;
  
  String[] c;
  
  int en;
  
  Consumer d;
  
  Table D;
  
  Runnable f;
  
  public final Table g() {
    return this.D;
  }
  
  public final int o() {
    return this.em;
  }
  
  public final Runnable a() {
    return this.f;
  }
  
  public jr(int paramInt1, int paramInt2, String paramString, Runnable paramRunnable, boolean paramBoolean) {
    this.el = paramInt1;
    this.em = paramInt2;
    this.aA = paramString;
    this.aB = null;
    this.aC = null;
    this.l = paramRunnable;
    this.bv = paramBoolean;
    this.H = null;
    this.d = null;
    this.e = null;
    this.b = null;
    this.bw = false;
    this.b = null;
    this.bW = 0.0F;
    this.bX = 0.0F;
    this.bY = 0.0F;
    this.a = null;
    this.c = null;
    this.m = null;
  }
  
  jr(int paramInt1, String paramString, Runnable paramRunnable, int paramInt2, boolean paramBoolean) {
    this.el = paramInt1;
    this.em = 0;
    this.aA = paramString;
    this.aB = null;
    this.aC = null;
    this.l = paramRunnable;
    this.bv = paramBoolean;
    this.H = null;
    this.d = (Consumer)Integer.valueOf(4);
    this.e = Integer.valueOf(paramInt2);
    this.b = null;
    this.bw = false;
    this.b = null;
    this.bW = 0.0F;
    this.bX = 0.0F;
    this.bY = 0.0F;
    this.a = null;
    this.c = null;
    this.m = null;
  }
  
  public jr(int paramInt1, int paramInt2, String paramString1, String paramString2, String paramString3, Runnable paramRunnable, boolean paramBoolean) {
    this.el = paramInt1;
    this.em = paramInt2;
    this.aA = paramString1;
    this.aB = paramString2;
    this.aC = paramString3;
    this.l = paramRunnable;
    this.bv = paramBoolean;
    this.H = null;
    this.d = null;
    this.e = null;
    this.b = null;
    this.bw = false;
    this.b = null;
    this.bW = 0.0F;
    this.bX = 0.0F;
    this.bY = 0.0F;
    this.a = null;
    this.c = null;
    this.m = null;
  }
  
  public jr(int paramInt1, int paramInt2, String paramString1, String paramString2, String paramString3, Runnable paramRunnable, int paramInt3, int paramInt4) {
    this.el = paramInt1;
    this.em = paramInt2;
    this.aA = paramString1;
    this.aB = paramString2;
    this.aC = paramString3;
    this.l = paramRunnable;
    this.bv = true;
    this.H = null;
    this.d = (Consumer)Integer.valueOf(paramInt3);
    this.e = Integer.valueOf(paramInt4);
    this.b = null;
    this.bw = false;
    this.b = null;
    this.bW = 0.0F;
    this.bX = 0.0F;
    this.bY = 0.0F;
    this.a = null;
    this.c = null;
    this.m = null;
  }
  
  public jr(int paramInt1, int paramInt2, String paramString1, String paramString2, String paramString3, Runnable paramRunnable, jn paramjn) {
    this.el = paramInt1;
    this.em = paramInt2;
    this.aA = paramString1;
    this.aB = paramString2;
    this.aC = paramString3;
    this.l = paramRunnable;
    this.bv = true;
    this.H = null;
    this.d = null;
    this.e = null;
    this.b = (Consumer)paramjn;
    this.bw = false;
    this.b = null;
    this.bW = 0.0F;
    this.bX = 0.0F;
    this.bY = 0.0F;
    this.a = null;
    this.c = null;
    this.m = null;
  }
  
  jr(int paramInt, String paramString, boolean paramBoolean, Consumer paramConsumer) {
    this.el = paramInt;
    this.em = 3;
    this.aA = paramString;
    this.aB = null;
    this.aC = null;
    this.l = null;
    this.bv = false;
    this.H = null;
    this.d = null;
    this.e = null;
    this.b = null;
    this.bw = paramBoolean;
    this.b = paramConsumer;
    this.bW = 0.0F;
    this.bX = 0.0F;
    this.bY = 0.0F;
    this.a = null;
    this.c = null;
    this.m = null;
  }
  
  jr(int paramInt1, String paramString, String[] paramArrayOfString, int paramInt2, Consumer paramConsumer) {
    this.el = paramInt1;
    this.em = 5;
    this.aA = paramString;
    this.aB = null;
    this.aC = null;
    this.l = null;
    this.bv = false;
    this.H = null;
    this.d = null;
    this.e = null;
    this.b = null;
    this.bw = false;
    this.b = null;
    this.bW = 0.0F;
    this.bX = 0.0F;
    this.bY = 0.0F;
    this.a = null;
    this.c = null;
    this.m = null;
    this.c = paramArrayOfString;
    this.en = Math.max(0, Math.min(paramInt2, paramArrayOfString.length - 1));
    this.d = paramConsumer;
  }
}
