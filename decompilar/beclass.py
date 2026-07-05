package a;

import java.util.Objects;

public final class be {
  public int aD;
  
  public int aE;
  
  public int aF;
  
  public be(int paramInt1, int paramInt2, int paramInt3) {
    this.aD = paramInt1;
    this.aE = paramInt2;
    this.aF = paramInt3;
  }
  
  public final int a() {
    return this.aD;
  }
  
  public final int b() {
    return this.aE;
  }
  
  public final int c() {
    return this.aF;
  }
  
  public final boolean equals(Object paramObject) {
    if (this == paramObject)
      return true; 
    if (paramObject == null || getClass() != paramObject.getClass())
      return false; 
    paramObject = paramObject;
    return (this.aD == ((be)paramObject).aD && this.aE == ((be)paramObject).aE && this.aF == ((be)paramObject).aF);
  }
  
  public final int hashCode() {
    return Objects.hash(new Object[] { Integer.valueOf(this.aD), Integer.valueOf(this.aE), Integer.valueOf(this.aF) });
  }
}
