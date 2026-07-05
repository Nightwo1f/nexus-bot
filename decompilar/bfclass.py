package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.files.FileHandle;
import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Properties;

public final class bf {
  private Socket a;
  
  private DataOutputStream a;
  
  private DataInputStream a;
  
  private Thread a;
  
  private final cq b;
  
  public br b;
  
  public bq a;
  
  private boolean w = false;
  
  private final Deque a;
  
  private final File a;
  
  private final File b;
  
  private final Properties a;
  
  private FileOutputStream a = (FileOutputStream)new ArrayDeque();
  
  private int aG;
  
  private int aH;
  
  private long c;
  
  private long d;
  
  private long e;
  
  private int aI;
  
  private int aJ;
  
  private long f;
  
  private File c;
  
  private File d;
  
  private File e;
  
  private long a(File paramFile) {
    long l = 0L;
    File[] arrayOfFile;
    if ((arrayOfFile = paramFile.listFiles()) == null)
      return 0L; 
    int i = arrayOfFile.length;
    for (byte b = 0; b < i; b++) {
      File file;
      if ((file = arrayOfFile[b]).isDirectory()) {
        l += a(file);
      } else if (!file.getName().startsWith(".")) {
        l += file.length();
      } 
    } 
    return l;
  }
  
  private void a(File paramFile) {
    if (paramFile == null || !paramFile.exists())
      return; 
    File[] arrayOfFile;
    if ((arrayOfFile = paramFile.listFiles()) != null) {
      int i = arrayOfFile.length;
      for (byte b = 0; b < i; b++) {
        File file;
        if ((file = arrayOfFile[b]).isDirectory())
          a(file); 
        file.delete();
      } 
    } 
    paramFile.delete();
  }
  
  private static File a(File paramFile) {
    return new File(paramFile, ".complete");
  }
  
  private void v() {
    if (this.a == null)
      return; 
    try {
      this.a.flush();
      this.a.close();
      return;
    } catch (IOException iOException) {
      return;
    } finally {
      this.a = null;
    } 
  }
  
  private void w() {
    try {
      FileOutputStream fileOutputStream = new FileOutputStream(this.b);
      try {
        this.a.store(fileOutputStream, "Packs JTME");
        fileOutputStream.close();
        return;
      } catch (Throwable throwable) {
        try {
          fileOutputStream.close();
        } catch (Throwable throwable1) {
          throwable.addSuppressed(throwable1);
        } 
        throw throwable;
      } 
    } catch (IOException iOException) {
      null.printStackTrace();
      return;
    } 
  }
  
  private boolean a(int paramInt1, int paramInt2, long paramLong) {
    File file;
    if (!(file = new File((File)this.a, "pack" + paramInt1)).exists() || !file.isDirectory())
      return false; 
    if (b(file) != paramLong)
      return false; 
    String str = "pack" + paramInt1;
    if (!this.a.containsKey(str))
      return false; 
    try {
      return (Integer.parseInt(this.a.getProperty(str)) == paramInt2);
    } catch (NumberFormatException numberFormatException) {
      return false;
    } 
  }
  
  private long b(File paramFile) {
    long l = 0L;
    File[] arrayOfFile;
    if ((arrayOfFile = paramFile.listFiles()) != null) {
      int i = arrayOfFile.length;
      for (byte b = 0; b < i; b++) {
        File file;
        if ((file = arrayOfFile[b]).isFile()) {
          l += file.length();
        } else {
          l += b(file);
        } 
      } 
    } 
    return l;
  }
  
  public bf(cq paramcq) {
    this.a = (FileOutputStream)new Properties();
    this.aG = 0;
    this.aH = 0;
    this.c = 0L;
    this.d = 0L;
    this.e = 0L;
    this.aI = -1;
    this.aJ = -1;
    this.f = 0L;
    this.c = null;
    this.d = null;
    this.e = null;
    this.b = (File)paramcq;
    FileHandle fileHandle;
    (fileHandle = Gdx.files.local("JTME")).mkdirs();
    this.a = (FileOutputStream)fileHandle.file();
    this.b = new File((File)this.a, "packs.properties");
    bf bf1;
    if (!(bf1 = this).a.exists())
      bf1.a.mkdirs(); 
    if (bf1.b.exists())
      try {
        FileInputStream fileInputStream = new FileInputStream(bf1.b);
        try {
          bf1.a.load(fileInputStream);
          fileInputStream.close();
          return;
        } catch (Throwable throwable) {
          try {
            fileInputStream.close();
          } catch (Throwable throwable1) {
            throwable.addSuppressed(throwable1);
          } 
          throw throwable;
        } 
      } catch (IOException iOException) {
        null.printStackTrace();
      }  
  }
  
  public final void a(String paramString, int paramInt) {
    this.a = (FileOutputStream)new Socket();
    this.a.connect(new InetSocketAddress(paramString, paramInt), 5000);
    this.a = (FileOutputStream)new DataOutputStream(this.a.getOutputStream());
    this.a = (FileOutputStream)new DataInputStream(new BufferedInputStream(this.a.getInputStream(), 5000));
    bf bf1;
    (bf1 = this).a = (FileOutputStream)new Thread(() -> {
          try {
            while (!Thread.currentThread().isInterrupted()) {
              String str1;
              int n;
              int i1;
              String str2;
              File file1;
              ks ks2;
              int i2;
              int i4;
              String str3;
              int i3;
              long l1;
              String str4;
              int i5;
              File file2;
              byte[] arrayOfByte3;
              int i6;
              long l2;
              File file3;
              String str5;
              long l3;
              File file4;
              byte[] arrayOfByte4;
              int i = this.a.readUnsignedByte();
              int j;
              int k = (j = this.a.readUnsignedByte()) << 8 | i;
              int m = this.a.readUnsignedByte();
              byte[] arrayOfByte2 = new byte[k - 1];
              this.a.readFully(arrayOfByte2);
              byte[] arrayOfByte1;
              (arrayOfByte1 = new byte[2 + k])[0] = (byte)i;
              arrayOfByte1[1] = (byte)j;
              arrayOfByte1[2] = (byte)m;
              System.arraycopy(arrayOfByte2, 0, arrayOfByte1, 3, arrayOfByte2.length);
              ks ks1 = new ks(arrayOfByte1);
              j = m;
              bf bf1 = this;
              ks1.q();
              switch (j) {
                case 51:
                  ks1.p();
                  ks1.q();
                  ks1.b.getInt();
                  ks1.f();
                  continue;
                case 50:
                  ks1.p();
                  j = ks1.p();
                  m = 0;
                  while (true)
                    m++; 
                  m = ks1.p();
                  n = 0;
                  while (true)
                    n++; 
                  n = ks1.p();
                  for (i1 = 0; i1 < n; i1++) {
                    ks1.q();
                    ks1.b.getInt();
                    ks1.f();
                  } 
                  i1 = ks1.p();
                  for (i4 = 0; i4 < i1; i4++) {
                    int i7 = ks1.q();
                    int i8 = ks1.b.getInt();
                    String str = ks1.f();
                    bf1.a.setProperty("sound" + str, String.valueOf(i7));
                    if ("ogg".equalsIgnoreCase(str)) {
                      long l = i8;
                      String str6 = "pack5";
                      bf bf2 = bf1;
                      File file;
                      if (!((!(file = new File((File)bf2.a, str6)).exists() || !file.isDirectory()) ? 0 : ((bf2.b(file) == l) ? 1 : 0)))
                        bf1.a.add(new bh(bi.d, 0, 0, i8)); 
                    } 
                  } 
                  if (((cq)bf1.b).U) {
                    i4 = ks1.p();
                    for (byte b = 0; b < i4; b++) {
                      int i7 = ks1.q();
                      int i8 = ks1.b.getInt();
                      int i9 = ks1.p();
                      if (!bf1.a(i9, i7, i8)) {
                        bf1.a.add(new bh(bi.e, i9, 0, i8));
                      } else {
                        bf1.a.setProperty("pack" + i9, String.valueOf(i7));
                      } 
                    } 
                  } 
                  bf1.w();
                  bf1.aG = bf1.a.size();
                  bf1.aH = 0;
                  bf1.c = 0L;
                  for (bh bh : bf1.a)
                    bf1.c += bh.g; 
                  bf1.d = 0L;
                  bf1.e = 0L;
                  bf1.z();
                  continue;
                case 20:
                  ks1.p();
                  j = ks1.q();
                  str1 = ks1.f();
                  ks1.f();
                  if (bf1.a != null)
                    bf1.a.b(j, str1); 
                  bf1.w = true;
                  continue;
                case 11:
                  ks1.p();
                  n = ks1.q();
                  str2 = ks1.f();
                  if (bf1.a != null) {
                    bf1.y();
                    bf1.a.c(n, str2);
                  } 
                  continue;
                case 100:
                  ks1.p();
                  if (((cq)bf1.b).bJ > 228)
                    ks1.p(); 
                  i4 = ks1.q();
                  str4 = ks1.f();
                  i6 = ks1.q();
                  ((cq)bf1.b).cb = i4;
                  ((cq)bf1.b).W = str4;
                  ((cq)bf1.b).bN = i6;
                  if (bf1.b != null && !((cq)bf1.b).S) {
                    ((br)bf1.b).a = (bx)bf1.a;
                    bf1.b.b(str4, i6);
                  } 
                  continue;
                case 40:
                  ks1.p();
                  i4 = ks1.p();
                  i5 = ks1.q();
                  l2 = ks1.b.getInt();
                  ks1.p();
                  str5 = ks1.f();
                  bf1.aI = i4;
                  bf1.aJ = i5;
                  bf1.f = l2;
                  file4 = new File((File)bf1.a, "pack" + i4);
                  if (i4 == 4)
                    file4 = new File(file4, str5); 
                  if (!file4.exists())
                    file4.mkdirs(); 
                  bf1.d = file4;
                  file1 = file4;
                  bf1.e = new File(file1.getAbsolutePath() + ".tmp");
                  bf1.a(bf1.e);
                  bf1.e.mkdirs();
                  bf1.c = bf1.e;
                  bf1.e = 0L;
                  continue;
                case 41:
                  ks1.p();
                  str3 = ks1.f();
                  bf1.v();
                  if ((file3 = (file2 = new File(bf1.c, str3)).getParentFile()) != null && !file3.exists())
                    file3.mkdirs(); 
                  try {
                    bf1.a = new FileOutputStream(file2, false);
                  } catch (FileNotFoundException fileNotFoundException) {
                    null.printStackTrace();
                  } 
                  continue;
                case 42:
                  ks1.p();
                  i3 = ks1.q();
                  i2 = i3;
                  ks2 = ks1;
                  arrayOfByte4 = new byte[i2];
                  ks2.b.get(arrayOfByte4);
                  arrayOfByte3 = arrayOfByte4;
                  if (bf1.a == null) {
                    bf1.y();
                    continue;
                  } 
                  try {
                    bf1.a.write(arrayOfByte3);
                    bf1.e += i3;
                    long l = bf1.d + bf1.e;
                    float f1 = (bf1.c > 0L) ? ((float)l / (float)bf1.c) : 1.0F;
                    float f2;
                    if ((f2 = 0.2F + f1 * 0.8F) > 1.0F)
                      f2 = 1.0F; 
                    if (bf1.a != null)
                      bf1.a.d(f2); 
                  } catch (IOException iOException) {
                    null.printStackTrace();
                    if (bf1.a != null)
                      bf1.a.c(1, "Erro ao escrever dados do dicion); 
                  } 
                  continue;
                case 43:
                  ks1.p();
                  bf1.v();
                  l1 = bf1.f;
                  file3 = bf1.e;
                  l3 = (bf1.e != null) ? bf1.a(bf1.e) : -1L;
                  if ((j = (l1 > 0L && file3 == l1 && l3 == l1) ? 1 : 0) != 0) {
                    bf1.a(bf1.d);
                    if (bf1.e.renameTo(bf1.d)) {
                      File file = bf1.d;
                      try {
                        a(file).createNewFile();
                      } catch (IOException iOException) {}
                      bf1.a.setProperty("pack" + bf1.aI, String.valueOf(bf1.aJ));
                      bf1.w();
                    } 
                  } else {
                    bf1.a(bf1.e);
                  } 
                  if (j != 0)
                    bf1.d += file3; 
                  bf1.e = 0L;
                  bf1.z();
                  continue;
              } 
              continue;
              System.out.println("Unk Packet LOGIN ID: 0x" + Integer.toHexString(SYNTHETIC_LOCAL_VARIABLE_2));
            } 
            return;
          } catch (IOException iOException) {
            y();
            return;
          } 
        }"LoginClient-Response");
    bf1.a.setDaemon(true);
    bf1.a.start();
  }
  
  public final void a(int paramInt1, String paramString1, String paramString2, int paramInt2) {
    if (this.a != null) {
      this.a.d(0.1F);
      this.a.e(b.a(((cq)this.b).S, "id_connect_to_login_server"));
    } 
    il il;
    (il = new il()).aj(3);
    il.aj(36);
    il.B(paramString1);
    il.aj(paramInt2);
    il.ak(paramInt1);
    il.aj(0);
    il.B(paramString2);
    a(il.a());
  }
  
  public final void p(int paramInt) {
    if (this.a != null) {
      this.a.d(0.2F);
      this.a.e(b.a(((cq)this.b).S, "id_connection_to_game_server_established"));
    } 
    il il;
    (il = new il()).aj(19);
    il.aj(paramInt);
    il.aj(1);
    a(il.a());
  }
  
  private void q(int paramInt) {
    il il;
    (il = new il()).aj(18);
    il.aj(paramInt);
    a(il.a());
  }
  
  private void r(int paramInt) {
    if (this.a != null) {
      this.a.d(0.5F);
      this.a.e(b.a(((cq)this.b).S, "id_motd_received"));
    } 
    il il;
    (il = new il()).aj(17);
    il.ak(paramInt);
    a(il.a());
  }
  
  public final void s(int paramInt) {
    if (this.a != null) {
      this.a.d(0.7F);
      this.a.e(b.a(((cq)this.b).S, "id_connect_to_game_server"));
    } 
    il il;
    (il = new il()).aj(16);
    il.ak(paramInt);
    a(il.a());
  }
  
  private void a(byte[] paramArrayOfbyte) {
    il il;
    (il = new il()).ak(paramArrayOfbyte.length);
    il.d(paramArrayOfbyte);
    paramArrayOfbyte = il.a();
    this.a.write(paramArrayOfbyte);
    this.a.flush();
  }
  
  public final void x() {
    if (!this.w)
      return; 
    this.w = false;
    try {
      s(((cq)this.b).ca);
      return;
    } catch (IOException iOException) {
      y();
      return;
    } 
  }
  
  public final void y() {
    v();
    a(this.e);
    if (this.a != null)
      this.a.interrupt(); 
    try {
      if (this.a != null)
        this.a.close(); 
    } catch (IOException iOException) {}
    try {
      if (this.a != null)
        this.a.close(); 
    } catch (IOException iOException) {}
    try {
      if (this.a != null)
        this.a.close(); 
    } catch (IOException iOException) {}
    if (this.a != null)
      this.a.c(1, b.a(((cq)this.b).S, "id_connection_to_login_server_failed")); 
  }
  
  private void z() {
    if (this.a.isEmpty()) {
      if (this.aG > 0) {
        Gdx.app.postRunnable(() -> {
              b.e();
              b.a(new e[] { e.b, (e)e.a, e.c, e.e, e.f }, (cq)this.b);
              try {
                q(((cq)this.b).ca);
                r(((cq)this.b).ca);
                return;
              } catch (IOException iOException) {
                y();
                return;
              } 
            });
        return;
      } 
      try {
        q(((cq)this.b).ca);
        r(((cq)this.b).ca);
        return;
      } catch (IOException iOException) {
        y();
        return;
      } 
    } 
    this.aH++;
    String str = String.format(b.a(((cq)this.b).S, "id_downloading_game_data_counter_d_of_maxcounter_d"), new Object[] { Integer.valueOf(this.aH), Integer.valueOf(this.aG) });
    if (this.a != null)
      this.a.e(str); 
    bh bh = this.a.poll();
    try {
      bf bf1;
      int j;
      String str1;
      int i;
      int k;
      il il1;
      il il2;
      switch (bg.s[bh.a.ordinal()]) {
        case 1:
          k = bh.aL;
          j = bh.aK;
          bf1 = this;
          (il2 = new il()).aj(12);
          il2.aj(j);
          il2.aj(k);
          il2.aj(1);
          bf1.a(il2.a());
          return;
        case 2:
          j = ((cq)this.b).bZ;
          bf1 = this;
          (il1 = new il()).aj(13);
          il1.aj(j);
          bf1.a(il1.a());
          return;
        case 3:
          str1 = "ogg";
          bf1 = this;
          (il1 = new il()).aj(20);
          il1.B(str1);
          bf1.a(il1.a());
          return;
        case 4:
          i = ((bh)bf1).aK;
          bf1 = this;
          (il1 = new il()).aj(11);
          il1.aj(i);
          bf1.a(il1.a());
          break;
      } 
      return;
    } catch (IOException iOException) {
      y();
      return;
    } 
  }
}
