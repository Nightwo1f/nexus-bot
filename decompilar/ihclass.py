package a;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;

public final class ih {
  private final fj l;
  
  private final x b;
  
  private static final byte[] c = new byte[] { 100, 101, 102, 103 };
  
  public ih(fj paramfj, x paramx) {
    this.l = paramfj;
    this.b = paramx;
  }
  
  public final List a(be parambe1, be parambe2, boolean paramBoolean) {
    return a(parambe1, parambe2, paramBoolean, true, true);
  }
  
  public final List a(be parambe1, be parambe2) {
    return a(parambe1, parambe2, true, true, true);
  }
  
  public final List b(be parambe1, be parambe2) {
    return a(parambe1, parambe2, true, true, true);
  }
  
  public final List a(be parambe1, be parambe2, boolean paramBoolean1, boolean paramBoolean2, boolean paramBoolean3) {
    if (parambe1 == null || parambe2 == null || parambe1.equals(parambe2))
      return null; 
    PriorityQueue<ii> priorityQueue = new PriorityQueue();
    HashMap<Object, Object> hashMap = new HashMap<>();
    ii ii1 = new ii(parambe1, null, (byte)0, 0, a(parambe1, parambe2) * 10);
    priorityQueue.add(ii1);
    hashMap.put(parambe1, Integer.valueOf(0));
    byte b = 0;
    ii ii2 = ii1;
    int i = ii1.dZ;
    while (!priorityQueue.isEmpty() && ++b <= ') {
      ii ii;
      if ((ii = priorityQueue.poll()).q.equals(parambe2)) {
        ii2 = ii;
        break;
      } 
      if (ii.dZ < i) {
        i = ii.dZ;
        ii2 = ii;
      } 
      byte[] arrayOfByte;
      int j = (arrayOfByte = c).length;
      for (byte b1 = 0; b1 < j; b1++) {
        byte b2 = arrayOfByte[b1];
        be be1;
        if ((be1 = b(ii.q, b2)) != null && this.l.a(be1.aD, be1.aE, be1.aF) != null && this.b.a(ii.q, b2) && (!paramBoolean1 || !this.l.d(be1) || be1.equals(parambe2)) && (!paramBoolean2 || !this.l.a(be1)) && (!this.l.f(ii.q, b2) || be1.equals(parambe2))) {
          int k = 0;
          if (ii.a != null && ii.d != b2)
            k = 2; 
          if ((k = ii.dY + 10 + k) < ((Integer)hashMap.getOrDefault(be1, (V)Integer.valueOf(2147483647))).intValue()) {
            hashMap.put(be1, Integer.valueOf(k));
            int m = a(be1, parambe2) * 10;
            priorityQueue.add(new ii(be1, ii, b2, k, m));
          } 
        } 
      } 
    } 
    if (ii2 == ii1)
      return null; 
    if (!paramBoolean3) {
      int j = Math.abs(ii2.q.aD - parambe2.aD);
      int k = Math.abs(ii2.q.aE - parambe2.aE);
      if (Math.abs(ii2.q.aF - parambe2.aF) != 0 || j > 1 || k > 1)
        return null; 
    } 
    LinkedList<Byte> linkedList = new LinkedList();
    for (ii ii3 = ii2; ii3.a != null; ii3 = ii3.a)
      linkedList.addFirst(Byte.valueOf(ii3.d)); 
    return new ArrayList<>(linkedList);
  }
  
  public static int a(be parambe1, be parambe2) {
    return (parambe1 == null || parambe2 == null) ? Integer.MAX_VALUE : (Math.abs(parambe1.aD - parambe2.aD) + Math.abs(parambe1.aE - parambe2.aE));
  }
  
  private static be b(be parambe, byte paramByte) {
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
}
