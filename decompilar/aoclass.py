package a;

import java.util.Random;

final class ao {
  final float q;
  
  final float r;
  
  ao(float paramFloat1, float paramFloat2) {
    this.q = paramFloat1;
    this.r = paramFloat2;
  }
  
  final float a(Random paramRandom) {
    return (this.q == this.r) ? this.q : (this.q + paramRandom.nextFloat() * (this.r - this.q));
  }
}
