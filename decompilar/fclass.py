package a;

import java.util.Map;

public final class f {
  public final Map c;
  
  private int a;
  
  private int b;
  
  private int c;
  
  private byte[] a;
  
  public f(byte[] paramArrayOfbyte) {
    // Byte code:
    //   0: aload_0
    //   1: invokespecial <init> : ()V
    //   4: aload_0
    //   5: new java/util/HashMap
    //   8: dup
    //   9: invokespecial <init> : ()V
    //   12: putfield c : Ljava/util/Map;
    //   15: aload_0
    //   16: aload_1
    //   17: invokevirtual clone : ()Ljava/lang/Object;
    //   20: checkcast [B
    //   23: putfield a : [B
    //   26: aload_0
    //   27: aload_1
    //   28: astore_2
    //   29: astore_1
    //   30: iconst_0
    //   31: istore_3
    //   32: iload_3
    //   33: aload_2
    //   34: arraylength
    //   35: if_icmpge -> 54
    //   38: aload_2
    //   39: iload_3
    //   40: aload_2
    //   41: iload_3
    //   42: baload
    //   43: bipush #95
    //   45: ixor
    //   46: i2b
    //   47: bastore
    //   48: iinc #3, 1
    //   51: goto -> 32
    //   54: new java/io/ByteArrayInputStream
    //   57: dup
    //   58: aload_2
    //   59: invokespecial <init> : ([B)V
    //   62: astore_3
    //   63: new java/io/DataInputStream
    //   66: dup
    //   67: new java/io/BufferedInputStream
    //   70: dup
    //   71: new java/util/zip/GZIPInputStream
    //   74: dup
    //   75: aload_3
    //   76: invokespecial <init> : (Ljava/io/InputStream;)V
    //   79: invokespecial <init> : (Ljava/io/InputStream;)V
    //   82: invokespecial <init> : (Ljava/io/InputStream;)V
    //   85: astore_2
    //   86: aload_2
    //   87: invokevirtual readUTF : ()Ljava/lang/String;
    //   90: ldc 'JTME_DATA'
    //   92: invokevirtual equals : (Ljava/lang/Object;)Z
    //   95: ifne -> 108
    //   98: new java/io/IOException
    //   101: dup
    //   102: ldc 'Arquivo de mapa invou corrompido (Header incorreto).'
    //   104: invokespecial <init> : (Ljava/lang/String;)V
    //   107: athrow
    //   108: aload_1
    //   109: aload_2
    //   110: invokevirtual readShort : ()S
    //   113: putfield c : I
    //   116: aload_1
    //   117: aload_2
    //   118: invokevirtual readUnsignedShort : ()I
    //   121: putfield a : I
    //   124: aload_1
    //   125: aload_2
    //   126: invokevirtual readUnsignedShort : ()I
    //   129: putfield b : I
    //   132: aload_2
    //   133: invokevirtual available : ()I
    //   136: ifle -> 219
    //   139: aload_2
    //   140: invokevirtual readUnsignedShort : ()I
    //   143: istore #4
    //   145: aload_2
    //   146: invokevirtual readUnsignedShort : ()I
    //   149: istore_3
    //   150: aload_2
    //   151: invokevirtual readByte : ()B
    //   154: istore #5
    //   156: aload_2
    //   157: invokevirtual readByte : ()B
    //   160: dup
    //   161: istore #6
    //   163: newarray short
    //   165: astore #7
    //   167: iconst_0
    //   168: istore #8
    //   170: iload #8
    //   172: iload #6
    //   174: if_icmpge -> 192
    //   177: aload #7
    //   179: iload #8
    //   181: aload_2
    //   182: invokevirtual readShort : ()S
    //   185: sastore
    //   186: iinc #8, 1
    //   189: goto -> 170
    //   192: aload_1
    //   193: getfield c : Ljava/util/Map;
    //   196: iload #4
    //   198: iload_3
    //   199: iload #5
    //   201: invokestatic a : (III)J
    //   204: invokestatic valueOf : (J)Ljava/lang/Long;
    //   207: aload #7
    //   209: invokeinterface put : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   214: pop
    //   215: goto -> 132
    //   218: pop
    //   219: aload_2
    //   220: invokevirtual close : ()V
    //   223: return
    //   224: astore_3
    //   225: aload_2
    //   226: invokevirtual close : ()V
    //   229: goto -> 240
    //   232: astore #4
    //   234: aload_3
    //   235: aload #4
    //   237: invokevirtual addSuppressed : (Ljava/lang/Throwable;)V
    //   240: aload_3
    //   241: athrow
    //   242: astore_3
    //   243: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   246: ldc 'ClientMap'
    //   248: ldc 'Error'
    //   250: aload_3
    //   251: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   256: aload_1
    //   257: getfield c : Ljava/util/Map;
    //   260: invokeinterface clear : ()V
    //   265: return
    // Exception table:
    //   from	to	target	type
    //   30	242	242	java/lang/Exception
    //   86	219	224	java/lang/Throwable
    //   139	215	218	java/io/EOFException
    //   225	229	232	java/lang/Throwable
  }
  
  public final short[] a(int paramInt1, int paramInt2, int paramInt3) {
    // Byte code:
    //   0: aload_0
    //   1: getfield c : Ljava/util/Map;
    //   4: iload_1
    //   5: iload_2
    //   6: iload_3
    //   7: invokestatic a : (III)J
    //   10: invokestatic valueOf : (J)Ljava/lang/Long;
    //   13: invokeinterface get : (Ljava/lang/Object;)Ljava/lang/Object;
    //   18: checkcast [S
    //   21: areturn
  }
  
  public static long a(int paramInt1, int paramInt2, int paramInt3) {
    return (paramInt3 & 0xFFL) << 60L | (paramInt1 & 0x3FFFFFFFL) << 30L | paramInt2 & 0x3FFFFFFFL;
  }
  
  public final void f() {
    // Byte code:
    //   0: aload_0
    //   1: getfield c : Ljava/util/Map;
    //   4: invokeinterface clear : ()V
    //   9: return
  }
}
