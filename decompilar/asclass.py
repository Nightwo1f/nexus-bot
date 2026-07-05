package a;

import java.util.Random;

final class as {
  final float t;
  
  final float u;
  
  as(float paramFloat1, float paramFloat2) {
    this.t = paramFloat1;
    this.u = paramFloat2;
  }
  
  final float b(Random paramRandom) {
    return (this.t == this.u) ? this.t : (this.t + paramRandom.nextFloat() * (this.u - this.t));
  }
}
