package a;

import java.util.ArrayList;
import java.util.Random;

final class au {
  final int aa;
  
  final ArrayList a = new ArrayList();
  
  int ab;
  
  au(int paramInt) {
    this.aa = paramInt;
  }
  
  final void a(av paramav) {
    this.a.add(paramav);
    this.ab += paramav.ac;
  }
  
  final av a(Random paramRandom) {
    if (this.a.isEmpty())
      return null; 
    if (this.a.size() == 1)
      return this.a.get(0); 
    int j;
    if ((j = this.ab) <= 0)
      return this.a.get(paramRandom.nextInt(this.a.size())); 
    int i = paramRandom.nextInt(j) + 1;
    j = 0;
    for (av av : this.a) {
      j += av.ac;
      if (i <= j)
        return av; 
    } 
    return this.a.get(this.a.size() - 1);
  }
}
