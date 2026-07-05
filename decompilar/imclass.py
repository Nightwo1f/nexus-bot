package a;

import java.io.ByteArrayInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public final class im {
  private final byte[] d;
  
  public short[] a = null;
  
  public short[] b = null;
  
  public im(byte[] paramArrayOfbyte) {
    this.d = Arrays.copyOf(paramArrayOfbyte, paramArrayOfbyte.length);
    e(paramArrayOfbyte);
  }
  
  private void e(byte[] paramArrayOfbyte) {
    try {
      DataInputStream dataInputStream = new DataInputStream(new ByteArrayInputStream(paramArrayOfbyte));
      try {
        short s;
        if ((s = (short)(dataInputStream.readByte() & 0xFF | (dataInputStream.readByte() & 0xFF) << 8)) >= 1200) {
          this.a = new short[s];
          int i;
          for (i = 0; i < s; i++)
            this.a[i] = (short)((dataInputStream.readByte() & 0xFF) << 8 | dataInputStream.readByte() & 0xFF); 
          i = s * 2;
          this.b = new short[i];
          for (s = 0; s < i - 2; s += 2) {
            short s1 = (short)(dataInputStream.readByte() & 0xFF | (dataInputStream.readByte() & 0xFF) << 8);
            short s2 = (short)(dataInputStream.readByte() & 0xFF | (dataInputStream.readByte() & 0xFF) << 8);
            this.b[s] = s1;
            this.b[s + 1] = s2;
          } 
        } else {
          dataInputStream.close();
          return;
        } 
        dataInputStream.close();
        return;
      } catch (Throwable throwable) {
        try {
          dataInputStream.close();
        } catch (Throwable throwable1) {
          throwable.addSuppressed(throwable1);
        } 
        throw throwable;
      } 
    } catch (IOException iOException) {
      this.a = null;
      this.b = null;
      throw iOException;
    } 
  }
  
  public final short[] a() {
    return this.b;
  }
  
  public final void am(int paramInt) {
    if (paramInt > 0) {
      this.a[paramInt] = (short)(this.a[paramInt] ^ this.a[paramInt - 1]);
      this.a[paramInt - 1] = (short)(this.a[paramInt - 1] ^ this.a[paramInt]);
      this.a[paramInt] = (short)(this.a[paramInt] ^ this.a[paramInt - 1]);
    } 
  }
  
  public final synchronized void cc() {
    try {
      e(this.d);
      return;
    } catch (IOException iOException) {
      this.a = null;
      this.b = null;
      return;
    } 
  }
}
