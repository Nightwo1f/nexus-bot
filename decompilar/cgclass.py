package a;

import com.badlogic.gdx.utils.IntArray;

public final class cg {
  public int aD;
  
  public int aE;
  
  public int aF;
  
  public final IntArray a;
  
  private int br;
  
  private cf a;
  
  private String B;
  
  private String I;
  
  public int bs = 0;
  
  public final IntArray b;
  
  public cg(int paramInt1, int paramInt2, int paramInt3) {
    this.aD = paramInt1;
    this.aE = paramInt2;
    this.aF = paramInt3;
    this.a = (cf)new IntArray(false, 10);
    this.b = new IntArray(false, 10);
  }
  
  public final void H(int paramInt) {
    if (!this.b.contains(paramInt))
      this.b.add(paramInt); 
  }
  
  public final void I(int paramInt) {
    this.b.removeValue(paramInt);
  }
  
  public final void J(int paramInt) {
    this.a.add(paramInt);
  }
  
  public final void a(short paramShort) {
    this.a.add(paramShort);
  }
  
  public final void f(int paramInt1, int paramInt2, int paramInt3) {
    this.aD = paramInt1;
    this.aE = paramInt2;
    this.aF = paramInt3;
  }
  
  public final void ad() {
    this.a.clear();
    this.br = 0;
    this.a = null;
    this.B = null;
    this.I = null;
    this.bs = 0;
    this.b.clear();
  }
}
