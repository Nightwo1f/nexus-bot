package META-INF.versions.10.org.lwjgl.system;

import org.lwjgl.system.APIUtil;

public final class MathUtil {
  static {
    APIUtil.apiLog("Java 10 multiplyHigh enabled");
  }
  
  public static boolean mathIsPoT(int value) {
    return (Integer.bitCount(value) == 1);
  }
  
  public static int mathRoundPoT(int value) {
    return 1 << 32 - Integer.numberOfLeadingZeros(value - 1);
  }
  
  public static boolean mathHasZeroByte(int value) {
    return ((value - 16843009 & (value ^ 0xFFFFFFFF) & 0x80808080) != 0);
  }
  
  public static boolean mathHasZeroByte(long value) {
    return ((value - 72340172838076673L & (value ^ 0xFFFFFFFFFFFFFFFFL) & 0x8080808080808080L) != 0L);
  }
  
  public static boolean mathHasZeroShort(int value) {
    return ((value - 65537 & (value ^ 0xFFFFFFFF) & 0x80008000) != 0);
  }
  
  public static boolean mathHasZeroShort(long value) {
    return ((value - 281479271743489L & (value ^ 0xFFFFFFFFFFFFFFFFL) & 0x8000800080008000L) != 0L);
  }
  
  public static long mathMultiplyHighU64(long x, long y) {
    long result = Math.multiplyHigh(x, y);
    if (x < 0L)
      result += y; 
    if (y < 0L)
      result += x; 
    return result;
  }
  
  public static long mathMultiplyHighS64(long x, long y) {
    return Math.multiplyHigh(x, y);
  }
  
  public static long mathDivideUnsigned(long dividend, long divisor) {
    if (0L <= divisor)
      return (0L <= dividend) ? (
        dividend / divisor) : 
        udivdi3(dividend, divisor); 
    return (Long.compareUnsigned(dividend, divisor) < 0) ? 0L : 1L;
  }
  
  public static long mathRemainderUnsigned(long dividend, long divisor) {
    if (0L < dividend && 0L < divisor)
      return dividend % divisor; 
    return (Long.compareUnsigned(dividend, divisor) < 0) ? 
      dividend : (
      dividend - divisor * udivdi3(dividend, divisor));
  }
  
  private static long udivdi3(long u, long v) {
    if (v >>> 32L == 0L) {
      if (u >>> 32L < v) {
        long l = (u >>> 1L) / v << Long.numberOfLeadingZeros(v) >>> 31L;
        if (u - l * v >= v)
          l++; 
        return l;
      } 
      long u1 = u >>> 32L;
      long q1 = u1 / v;
      long l1 = (u1 - q1 * v << 32L | u & 0xFFFFFFFFL) / v;
      return q1 << 32L | l1;
    } 
    int n = Long.numberOfLeadingZeros(v);
    long q0 = (u >>> 1L) / (v << n >>> 32L) << n >>> 31L;
    if (q0 != 0L)
      q0--; 
    if (Long.compareUnsigned(u - q0 * v, v) >= 0)
      q0++; 
    return q0;
  }
}
