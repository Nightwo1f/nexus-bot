package a;

public final class ax {
  private final cq a;
  
  private final cr a;
  
  private bf a;
  
  private br a;
  
  public ax(cq paramcq, cr paramcr) {
    this.a = (br)paramcq;
    this.a = (br)paramcr;
  }
  
  public final synchronized bf a() {
    if (this.a == null)
      this.a = (br)new bf((cq)this.a); 
    return (bf)this.a;
  }
  
  public final synchronized br a() {
    if (this.a == null)
      this.a = new br((cq)this.a, (cr)this.a, a()); 
    return this.a;
  }
}
