package a;

import com.badlogic.gdx.utils.IntArray;
import com.badlogic.gdx.utils.IntSet;

public final class x {
  private final fj a;
  
  private static final IntSet a = new IntSet();
  
  private static final IntSet b = new IntSet();
  
  public x(fj paramfj) {
    this.a = (IntSet)paramfj;
  }
  
  public final boolean a(be parambe, byte paramByte) {
    parambe = a(parambe, paramByte);
    cg cg;
    if ((cg = this.a.a(parambe.aD, parambe.aE, parambe.aF)) == null)
      return false; 
    cf cf = cg.a;
    for (paramByte = 0; paramByte < ((IntArray)cf).size; paramByte++) {
      ah ah;
      if ((ah = b.a.a(cf.get(paramByte))) != null && ah.h)
        return true; 
    } 
    for (paramByte = 0; paramByte < ((IntArray)cf).size; paramByte++) {
      ah ah;
      if ((ah = b.a.a(cf.get(paramByte))) != null && ah.i)
        return true; 
    } 
    for (paramByte = 0; paramByte < ((IntArray)cf).size; paramByte++) {
      ah ah;
      if ((ah = b.a.a(cf.get(paramByte))) != null && ah.g)
        return false; 
    } 
    return true;
  }
  
  public final boolean b(be parambe, byte paramByte) {
    parambe = a(parambe, paramByte);
    cg cg;
    if ((cg = this.a.a(parambe.aD, parambe.aE, parambe.aF)) == null)
      return false; 
    cf cf = cg.a;
    for (paramByte = 0; paramByte < ((IntArray)cf).size; paramByte++) {
      ah ah;
      if ((ah = b.a.a(cf.get(paramByte))) != null && ah.h)
        return true; 
    } 
    return false;
  }
  
  public final boolean c(be parambe, byte paramByte) {
    parambe = a(parambe, paramByte);
    cg cg;
    if ((cg = this.a.a(parambe.aD, parambe.aE, parambe.aF)) == null)
      return false; 
    cf cf = cg.a;
    for (paramByte = 0; paramByte < ((IntArray)cf).size; paramByte++) {
      ah ah;
      if ((ah = b.a.a(cf.get(paramByte))) != null && ah.i)
        return true; 
    } 
    return false;
  }
  
  public final boolean d(be parambe, byte paramByte) {
    parambe = a(parambe, paramByte);
    cg cg;
    if ((cg = this.a.a(parambe.aD, parambe.aE, parambe.aF)) == null)
      return false; 
    cf cf = cg.a;
    for (paramByte = 0; paramByte < ((IntArray)cf).size; paramByte++) {
      if (a.contains(cf.get(paramByte)))
        return true; 
    } 
    return false;
  }
  
  public final boolean e(be parambe, byte paramByte) {
    parambe = a(parambe, paramByte);
    cg cg;
    if ((cg = this.a.a(parambe.aD, parambe.aE, parambe.aF)) == null)
      return false; 
    cf cf = cg.a;
    for (paramByte = 0; paramByte < ((IntArray)cf).size; paramByte++) {
      if (b.contains(cf.get(paramByte)))
        return true; 
    } 
    return false;
  }
  
  private static be a(be parambe, byte paramByte) {
    switch (paramByte) {
      case 100:
        return new be(parambe.aD, parambe.aE - 1, parambe.aF);
      case 101:
        return new be(parambe.aD + 1, parambe.aE, parambe.aF);
      case 102:
        return new be(parambe.aD, parambe.aE + 1, parambe.aF);
      case 103:
        return new be(parambe.aD - 1, parambe.aE, parambe.aF);
    } 
    return parambe;
  }
  
  static {
    a.addAll(new int[] { 
          2586, 2588, 2590, 2592, 2594, 6965, 5583, 6312, 6058, 5570, 
          6148, 6966 });
    b.addAll(new int[] { 2587, 2589, 2591, 2593, 6967 });
  }
}
