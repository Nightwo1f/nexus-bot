package a;

final class bv {
  private final ks a;
  
  private int bk;
  
  private int bl = 8;
  
  public bv(ks paramks) {
    this.a = paramks;
  }
  
  public final int h() {
    if (this.bl == 8) {
      this.bk = this.a.p();
      this.bl = 0;
    } 
    int i = this.bk >> this.bl & 0x1;
    this.bl++;
    return i;
  }
  
  public final void ac() {
    if (this.bl != 8)
      this.bl = 8; 
  }
}
