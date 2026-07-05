package a;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.charset.StandardCharsets;

public final class ks {
  public final ByteBuffer b;
  
  private int eD;
  
  public ks(byte[] paramArrayOfbyte) {
    this.b = ByteBuffer.wrap(paramArrayOfbyte, 0, paramArrayOfbyte.length - 0);
    this.b.order(ByteOrder.LITTLE_ENDIAN);
    this.eD = 8;
  }
  
  public final int p() {
    return this.b.get() & 0xFF;
  }
  
  public final int q() {
    return this.b.getShort() & 0xFFFF;
  }
  
  public final int r() {
    return this.b.getInt();
  }
  
  public final long a() {
    return this.b.getLong();
  }
  
  private int s() {
    int i = p();
    int j = p();
    return i | j << 8;
  }
  
  public final String f() {
    int i;
    if ((i = p()) == 0)
      return ""; 
    if (i == 255 && (i = s()) == 0)
      return ""; 
    if (this.b.remaining() < i)
      throw new IllegalStateException("String underflow: len=" + i + " remaining=" + this.b.remaining() + " pos=" + this.b.position() + " limit=" + this.b.limit()); 
    byte[] arrayOfByte = new byte[i];
    this.b.get(arrayOfByte);
    return new String(arrayOfByte, StandardCharsets.ISO_8859_1);
  }
  
  public final String g() {
    int i;
    if ((i = p()) == 0)
      return ""; 
    if (i == 255 && (i = s()) == 0)
      return ""; 
    if (this.b.remaining() < i)
      throw new IllegalStateException("String Unicode underflow: len=" + i + " remaining=" + this.b.remaining() + " pos=" + this.b.position()); 
    byte[] arrayOfByte = new byte[i];
    this.b.get(arrayOfByte);
    String str = new String(arrayOfByte, StandardCharsets.UTF_8);
    int j = 0;
    for (byte b2 = 0; b2 < str.length(); b2++) {
      if (str.charAt(b2) == ')
        j++; 
    } 
    if (j > 0)
      return new String(arrayOfByte, StandardCharsets.ISO_8859_1); 
    StringBuilder stringBuilder = new StringBuilder(str.length() + 8);
    for (byte b1 = 0; b1 < str.length(); b1++) {
      if ((j = str.charAt(b1)) >= '&& j <= 57599) {
        j = 128 + j - 57344;
        stringBuilder.append(').append(').append((char)j);
      } else {
        stringBuilder.append(j);
      } 
    } 
    return stringBuilder.toString();
  }
  
  public final int t() {
    return this.b.remaining();
  }
  
  public final int u() {
    int i = p() & 0xFF;
    int j = p() & 0xFF;
    int k = p() & 0xFF;
    return i << 16 | j << 8 | k;
  }
  
  public final int a(int paramInt, boolean paramBoolean) {
    if (paramBoolean) {
      int i = p();
      return p() * paramInt + i;
    } 
    return p() & 0xFF;
  }
}
