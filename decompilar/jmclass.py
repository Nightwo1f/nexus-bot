package a;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.function.Consumer;

public final class jm {
  private final cq k;
  
  public String w = "Menu";
  
  public jx a;
  
  public boolean bo = false;
  
  public final List B = new ArrayList();
  
  public final List C = new ArrayList();
  
  public String at;
  
  private Float a;
  
  private Float b;
  
  private boolean bp = true;
  
  public Runnable g;
  
  public final List D = new ArrayList();
  
  public jq a;
  
  public String au = null;
  
  public final List E = new ArrayList();
  
  public String av;
  
  public int eh = 0;
  
  public boolean bq = true;
  
  public Runnable h;
  
  jm(cq paramcq) {
    this.k = paramcq;
  }
  
  public final jm a(String paramString) {
    this.av = paramString;
    this.eh = 0;
    return this;
  }
  
  public final void c(jr paramjr) {
    if (this.au != null) {
      paramjr.ar = this.au;
      this.au = null;
    } 
  }
  
  public final jm a(String paramString1, String paramString2, Runnable paramRunnable1, Runnable paramRunnable2) {
    this.a = new jq("", 0, 0, false, false, "", paramRunnable1, paramString1, paramString2, paramRunnable2, false);
    return this;
  }
  
  public final jm a(int paramInt1, String paramString, String[] paramArrayOfString, int paramInt2, Consumer paramConsumer) {
    jr jr = new jr(paramInt1, paramString, paramArrayOfString, paramInt2, paramConsumer);
    c(jr);
    this.B.add(jr);
    return this;
  }
  
  public final jm a(int paramInt1, String paramString, int paramInt2, Runnable paramRunnable) {
    jr jr = new jr(paramInt1, paramString, paramRunnable, paramInt2, true);
    c(jr);
    this.B.add(jr);
    return this;
  }
  
  public final jm a(int paramInt1, int paramInt2, String paramString, Runnable paramRunnable) {
    jr jr = new jr(paramInt1, paramInt2, paramString, paramRunnable, false);
    c(jr);
    this.B.add(jr);
    return this;
  }
  
  public final jm b(int paramInt1, String paramString, int paramInt2, Runnable paramRunnable) {
    jr jr = new jr(paramInt1, paramString, paramRunnable, paramInt2, false);
    c(jr);
    this.B.add(jr);
    return this;
  }
  
  public final jm a(int paramInt, String paramString, boolean paramBoolean, Consumer paramConsumer) {
    jr jr = new jr(paramInt, paramString, paramBoolean, paramConsumer);
    c(jr);
    this.B.add(jr);
    return this;
  }
  
  public final void b(jk paramjk) {
    if (this.au != null) {
      paramjk.ar = this.au;
      this.au = null;
    } 
  }
  
  public final ju a() {
    jx jx1;
    float f1 = this.k.bP;
    float f2 = (this.a != null) ? this.a.floatValue() : 0.0F;
    f1 = (this.b != null) ? this.b.floatValue() : f1;
    boolean bool1 = false;
    boolean bool2 = false;
    Iterator<jr> iterator = this.B.iterator();
    while (iterator.hasNext()) {
      jr jr;
      if ((jr = iterator.next()).aB != null && !jr.aB.isEmpty())
        bool1 = true; 
      if (jr.aC != null && !jr.aC.isEmpty())
        bool2 = true; 
      if (!bool1 || !bool2);
    } 
    jq jq2;
    boolean bool3 = ((this.a != null && ((((jx)(jq2 = this.a)).aI != null && !((jx)jq2).aI.isEmpty()))) || bool1) ? true : false;
    boolean bool4 = ((this.a != null && ((((jx)(jq2 = this.a)).aJ != null && !((jx)jq2).aJ.isEmpty()))) || bool2) ? true : false;
    bool1 = (this.B.stream().anyMatch(paramjr -> (paramjr.ar != null)) || this.C.stream().anyMatch(paramjk -> (paramjk.ar != null))) ? true : false;
    jq jq1;
    if ((jq1 = this.a) == null && (bool3 || bool4))
      jx1 = new jx("", "", ""); 
    return new ju(this.k, this.w, jx1, bool3, bool4, this.at, this.C, this.B, f2, f1, this.bp, this.g, this.bo, this.a, this.E, this.D, this.av, this.eh, this.bq, this.h, bool1);
  }
}
