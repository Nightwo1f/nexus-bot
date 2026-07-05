package a;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public final class al {
  private static final ar a = new ar();
  
  private static final am a = new am();
  
  private static boolean k;
  
  private static boolean l = true;
  
  private static long a = 1500L;
  
  private static final Set b;
  
  private static final Map p = new HashMap<>();
  
  public static void b(String paramString) {
    // Byte code:
    //   0: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   3: aload_0
    //   4: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   9: invokevirtual exists : ()Z
    //   12: ifne -> 31
    //   15: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   18: ldc 'Audio'
    //   20: aload_0
    //   21: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;)Ljava/lang/String;
    //   26: invokeinterface log : (Ljava/lang/String;Ljava/lang/String;)V
    //   31: getstatic a/al.a : La/ar;
    //   34: aload_0
    //   35: ldc 'soundfx.xml'
    //   37: invokevirtual b : (Ljava/lang/String;Ljava/lang/String;)V
    //   40: getstatic a/al.a : La/am;
    //   43: aload_0
    //   44: ldc 'music.xml'
    //   46: invokevirtual a : (Ljava/lang/String;Ljava/lang/String;)V
    //   49: iconst_1
    //   50: putstatic a/al.k : Z
    //   53: getstatic a/al.p : Ljava/util/Map;
    //   56: invokeinterface clear : ()V
    //   61: return
  }
  
  public static void d() {
    // Byte code:
    //   0: getstatic a/al.a : La/ar;
    //   3: dup
    //   4: astore_0
    //   5: invokevirtual r : ()V
    //   8: aload_0
    //   9: getfield s : Ljava/util/Map;
    //   12: invokeinterface values : ()Ljava/util/Collection;
    //   17: invokeinterface iterator : ()Ljava/util/Iterator;
    //   22: astore_1
    //   23: aload_1
    //   24: invokeinterface hasNext : ()Z
    //   29: ifeq -> 55
    //   32: aload_1
    //   33: invokeinterface next : ()Ljava/lang/Object;
    //   38: checkcast com/badlogic/gdx/audio/Sound
    //   41: astore_2
    //   42: aload_2
    //   43: invokeinterface dispose : ()V
    //   48: goto -> 23
    //   51: pop
    //   52: goto -> 23
    //   55: aload_0
    //   56: getfield s : Ljava/util/Map;
    //   59: invokeinterface clear : ()V
    //   64: aload_0
    //   65: getfield r : Ljava/util/Map;
    //   68: invokeinterface clear : ()V
    //   73: getstatic a/al.a : La/am;
    //   76: dup
    //   77: astore_0
    //   78: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   81: invokestatic a : (Lcom/badlogic/gdx/audio/Music;)V
    //   84: aload_0
    //   85: getfield b : Lcom/badlogic/gdx/audio/Music;
    //   88: invokestatic a : (Lcom/badlogic/gdx/audio/Music;)V
    //   91: aload_0
    //   92: aconst_null
    //   93: putfield a : Lcom/badlogic/gdx/audio/Music;
    //   96: aload_0
    //   97: aconst_null
    //   98: putfield b : Lcom/badlogic/gdx/audio/Music;
    //   101: aload_0
    //   102: getstatic a/aq.V : I
    //   105: putfield T : I
    //   108: aload_0
    //   109: getfield q : Ljava/util/Map;
    //   112: invokeinterface clear : ()V
    //   117: aload_0
    //   118: dup
    //   119: fconst_0
    //   120: dup_x1
    //   121: putfield m : F
    //   124: putfield l : F
    //   127: aload_0
    //   128: dup
    //   129: fconst_0
    //   130: dup_x1
    //   131: putfield p : F
    //   134: putfield o : F
    //   137: iconst_0
    //   138: putstatic a/al.k : Z
    //   141: getstatic a/al.p : Ljava/util/Map;
    //   144: invokeinterface clear : ()V
    //   149: return
    // Exception table:
    //   from	to	target	type
    //   42	48	51	java/lang/Exception
  }
  
  public static void a(float paramFloat) {
    a.j = ar.c(paramFloat);
  }
  
  public static void b(float paramFloat) {
    // Byte code:
    //   0: getstatic a/al.a : La/am;
    //   3: fload_0
    //   4: fstore_1
    //   5: dup
    //   6: astore_0
    //   7: fload_1
    //   8: invokestatic c : (F)F
    //   11: putfield j : F
    //   14: aload_0
    //   15: invokevirtual q : ()V
    //   18: return
  }
  
  public static void a(int paramInt) {
    // Byte code:
    //   0: getstatic a/al.k : Z
    //   3: ifne -> 7
    //   6: return
    //   7: getstatic a/al.b : Ljava/util/Set;
    //   10: iload_0
    //   11: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   14: invokeinterface contains : (Ljava/lang/Object;)Z
    //   19: ifeq -> 31
    //   22: getstatic a/al.a : La/ar;
    //   25: iload_0
    //   26: invokevirtual a : (I)J
    //   29: pop2
    //   30: return
    //   31: getstatic a/al.l : Z
    //   34: ifeq -> 100
    //   37: getstatic a/al.a : J
    //   40: lconst_0
    //   41: lcmp
    //   42: ifle -> 100
    //   45: invokestatic millis : ()J
    //   48: lstore_1
    //   49: getstatic a/al.p : Ljava/util/Map;
    //   52: iload_0
    //   53: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   56: invokeinterface get : (Ljava/lang/Object;)Ljava/lang/Object;
    //   61: checkcast java/lang/Long
    //   64: dup
    //   65: astore_3
    //   66: ifnull -> 83
    //   69: lload_1
    //   70: aload_3
    //   71: invokevirtual longValue : ()J
    //   74: lsub
    //   75: getstatic a/al.a : J
    //   78: lcmp
    //   79: ifge -> 83
    //   82: return
    //   83: getstatic a/al.p : Ljava/util/Map;
    //   86: iload_0
    //   87: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   90: lload_1
    //   91: invokestatic valueOf : (J)Ljava/lang/Long;
    //   94: invokeinterface put : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   99: pop
    //   100: getstatic a/al.a : La/ar;
    //   103: iload_0
    //   104: invokevirtual a : (I)J
    //   107: pop2
    //   108: return
  }
  
  public static void o() {
    // Byte code:
    //   0: getstatic a/al.k : Z
    //   3: ifne -> 7
    //   6: return
    //   7: getstatic a/al.a : La/ar;
    //   10: invokevirtual r : ()V
    //   13: return
  }
  
  public static void b(int paramInt) {
    // Byte code:
    //   0: getstatic a/al.k : Z
    //   3: ifne -> 7
    //   6: return
    //   7: getstatic a/al.a : La/am;
    //   10: iload_0
    //   11: invokevirtual c : (I)V
    //   14: return
  }
  
  public static void p() {
    if (!k)
      return; 
    long l;
    am.a((l = a).a);
    am.a(l.b);
    l.a = null;
    l.b = null;
    l.T = aq.V;
    l.l = l.m = 0.0F;
    l.o = l.p = 0.0F;
  }
  
  public static void c(float paramFloat) {
    // Byte code:
    //   0: getstatic a/al.k : Z
    //   3: ifne -> 7
    //   6: return
    //   7: getstatic a/al.a : La/am;
    //   10: fload_0
    //   11: fstore_1
    //   12: astore_0
    //   13: fload_1
    //   14: fconst_0
    //   15: fcmpg
    //   16: ifle -> 403
    //   19: getstatic a/an.n : [I
    //   22: aload_0
    //   23: getfield T : I
    //   26: iconst_1
    //   27: isub
    //   28: iaload
    //   29: tableswitch default -> 403, 1 -> 60, 2 -> 149, 3 -> 150, 4 -> 318
    //   60: aload_0
    //   61: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   64: ifnonnull -> 75
    //   67: aload_0
    //   68: getstatic a/aq.V : I
    //   71: putfield T : I
    //   74: return
    //   75: aload_0
    //   76: dup
    //   77: getfield l : F
    //   80: fload_1
    //   81: fsub
    //   82: putfield l : F
    //   85: aload_0
    //   86: getfield l : F
    //   89: fconst_0
    //   90: fcmpg
    //   91: ifgt -> 120
    //   94: aload_0
    //   95: fconst_0
    //   96: putfield l : F
    //   99: aload_0
    //   100: getstatic a/aq.X : I
    //   103: putfield T : I
    //   106: aload_0
    //   107: dup
    //   108: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   111: aload_0
    //   112: getfield k : F
    //   115: fconst_1
    //   116: invokevirtual a : (Lcom/badlogic/gdx/audio/Music;FF)V
    //   119: return
    //   120: fconst_1
    //   121: aload_0
    //   122: getfield l : F
    //   125: aload_0
    //   126: getfield m : F
    //   129: invokestatic b : (F)F
    //   132: fdiv
    //   133: fsub
    //   134: fstore_1
    //   135: aload_0
    //   136: dup
    //   137: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   140: aload_0
    //   141: getfield k : F
    //   144: fload_1
    //   145: invokevirtual a : (Lcom/badlogic/gdx/audio/Music;FF)V
    //   148: return
    //   149: return
    //   150: aload_0
    //   151: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   154: ifnull -> 164
    //   157: aload_0
    //   158: getfield b : Lcom/badlogic/gdx/audio/Music;
    //   161: ifnonnull -> 201
    //   164: aload_0
    //   165: getfield b : Lcom/badlogic/gdx/audio/Music;
    //   168: invokestatic a : (Lcom/badlogic/gdx/audio/Music;)V
    //   171: aload_0
    //   172: aconst_null
    //   173: putfield b : Lcom/badlogic/gdx/audio/Music;
    //   176: aload_0
    //   177: dup
    //   178: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   181: ifnonnull -> 190
    //   184: getstatic a/aq.V : I
    //   187: goto -> 193
    //   190: getstatic a/aq.X : I
    //   193: putfield T : I
    //   196: aload_0
    //   197: invokevirtual q : ()V
    //   200: return
    //   201: aload_0
    //   202: dup
    //   203: getfield o : F
    //   206: fload_1
    //   207: fsub
    //   208: putfield o : F
    //   211: aload_0
    //   212: getfield o : F
    //   215: fconst_0
    //   216: fcmpg
    //   217: ifgt -> 274
    //   220: aload_0
    //   221: fconst_0
    //   222: putfield o : F
    //   225: aload_0
    //   226: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   229: invokestatic a : (Lcom/badlogic/gdx/audio/Music;)V
    //   232: aload_0
    //   233: dup
    //   234: getfield b : Lcom/badlogic/gdx/audio/Music;
    //   237: putfield a : Lcom/badlogic/gdx/audio/Music;
    //   240: aload_0
    //   241: dup
    //   242: getfield n : F
    //   245: putfield k : F
    //   248: aload_0
    //   249: aconst_null
    //   250: putfield b : Lcom/badlogic/gdx/audio/Music;
    //   253: aload_0
    //   254: getstatic a/aq.X : I
    //   257: putfield T : I
    //   260: aload_0
    //   261: dup
    //   262: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   265: aload_0
    //   266: getfield k : F
    //   269: fconst_1
    //   270: invokevirtual a : (Lcom/badlogic/gdx/audio/Music;FF)V
    //   273: return
    //   274: fconst_1
    //   275: aload_0
    //   276: getfield o : F
    //   279: aload_0
    //   280: getfield p : F
    //   283: invokestatic b : (F)F
    //   286: fdiv
    //   287: fsub
    //   288: fstore_1
    //   289: aload_0
    //   290: dup
    //   291: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   294: aload_0
    //   295: getfield k : F
    //   298: fconst_1
    //   299: fload_1
    //   300: fsub
    //   301: invokevirtual a : (Lcom/badlogic/gdx/audio/Music;FF)V
    //   304: aload_0
    //   305: dup
    //   306: getfield b : Lcom/badlogic/gdx/audio/Music;
    //   309: aload_0
    //   310: getfield n : F
    //   313: fload_1
    //   314: invokevirtual a : (Lcom/badlogic/gdx/audio/Music;FF)V
    //   317: return
    //   318: aload_0
    //   319: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   322: ifnonnull -> 333
    //   325: aload_0
    //   326: getstatic a/aq.V : I
    //   329: putfield T : I
    //   332: return
    //   333: aload_0
    //   334: dup
    //   335: getfield l : F
    //   338: fload_1
    //   339: fsub
    //   340: putfield l : F
    //   343: aload_0
    //   344: getfield l : F
    //   347: fconst_0
    //   348: fcmpg
    //   349: ifgt -> 377
    //   352: aload_0
    //   353: fconst_0
    //   354: putfield l : F
    //   357: aload_0
    //   358: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   361: invokestatic a : (Lcom/badlogic/gdx/audio/Music;)V
    //   364: aload_0
    //   365: aconst_null
    //   366: putfield a : Lcom/badlogic/gdx/audio/Music;
    //   369: aload_0
    //   370: getstatic a/aq.V : I
    //   373: putfield T : I
    //   376: return
    //   377: aload_0
    //   378: getfield l : F
    //   381: aload_0
    //   382: getfield m : F
    //   385: invokestatic b : (F)F
    //   388: fdiv
    //   389: fstore_1
    //   390: aload_0
    //   391: dup
    //   392: getfield a : Lcom/badlogic/gdx/audio/Music;
    //   395: aload_0
    //   396: getfield k : F
    //   399: fload_1
    //   400: invokevirtual a : (Lcom/badlogic/gdx/audio/Music;FF)V
    //   403: return
  }
  
  static {
    (b = new HashSet<>()).add(Integer.valueOf(1));
    b.add(Integer.valueOf(2));
    b.add(Integer.valueOf(3));
    b.add(Integer.valueOf(4));
  }
}
