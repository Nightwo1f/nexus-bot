package a;

import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public final class il {
  private ByteBuffer a = ByteBuffer.allocate(9000).order(ByteOrder.LITTLE_ENDIAN);
  
  public il() {
    this((byte)0);
  }
  
  private il(byte paramByte) {}
  
  public final byte[] a() {
    byte[] arrayOfByte = new byte[this.a.position()];
    this.a.flip();
    this.a.get(arrayOfByte);
    return arrayOfByte;
  }
  
  public final void aj(int paramInt) {
    this.a.put((byte)paramInt);
  }
  
  public final void ak(int paramInt) {
    this.a.putShort((short)paramInt);
  }
  
  public final void al(int paramInt) {
    this.a.putInt(paramInt);
  }
  
  public final void d(byte[] paramArrayOfbyte) {
    if (paramArrayOfbyte != null && paramArrayOfbyte.length > 0)
      this.a.put(paramArrayOfbyte); 
  }
  
  public final void B(String paramString) {
    if (paramString == null) {
      this.a.put((byte)0);
      return;
    } 
    try {
      byte[] arrayOfByte;
      int i = (arrayOfByte = paramString.getBytes("UTF-8")).length;
      this.a.put((byte)i);
      if (i > 0)
        this.a.put(arrayOfByte); 
      return;
    } catch (UnsupportedEncodingException unsupportedEncodingException) {
      null.printStackTrace();
      this.a.put((byte)0);
      return;
    } 
  }
  
  public final void d(int[] paramArrayOfint) {
    paramArrayOfint.length;
    this.a.put((byte)paramArrayOfint[0]);
    this.a.put((byte)paramArrayOfint[1]);
  }
}
