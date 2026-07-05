package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.audio.Music;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.XmlReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Random;
import java.util.Set;

final class am {
  private final Set c = new HashSet();
  
  final Map q = new HashMap<>();
  
  private final Random a;
  
  float j = 1.0F;
  
  String n;
  
  Music a = (Music)new Random();
  
  float k = 1.0F;
  
  float l = 0.0F;
  
  float m = 0.0F;
  
  Music b;
  
  float n = 1.0F;
  
  float o = 0.0F;
  
  float p = 0.0F;
  
  int T = aq.V;
  
  final void a(String paramString1, String paramString2) {
    this.n = paramString1;
    this.q.clear();
    FileHandle fileHandle;
    if (!(fileHandle = Gdx.files.absolute(paramString1 + paramString1)).exists())
      return; 
    try {
      if (!(paramString2 = fileHandle.readString("UTF-8")).isEmpty() && paramString2.charAt(0) == ')
        paramString2 = paramString2.substring(1); 
      Array.ArrayIterator<XmlReader.Element> arrayIterator = (new XmlReader()).parse(paramString2).getChildrenByName("setting").iterator();
      while (arrayIterator.hasNext()) {
        int i = Integer.parseInt(str1);
        XmlReader.Element element;
        String str1;
        String str2;
        if ((str1 = (element = arrayIterator.next()).getAttribute("id", null)) != null && (element = a(element)) != null && (str2 = element.getAttribute("file", null)) != null && !str2.isEmpty()) {
          ao ao = a(element.getAttribute("volume", "100"));
          float f = element.getFloatAttribute("fadeInDuration", 0.0F);
          boolean bool = "infinite".equalsIgnoreCase(element.getAttribute("repetitions", ""));
          this.q.put(Integer.valueOf(i), new ap(i, str2, ao, f, bool));
        } 
      } 
      return;
    } catch (Exception exception) {
      Gdx.app.error("MusicManager", "Falha parseando " + fileHandle.path(), exception);
      return;
    } 
  }
  
  final void c(int paramInt) {
    ap ap;
    if ((ap = (ap)this.q.get(Integer.valueOf(paramInt))) == null) {
      if ((am1 = this).a == null) {
        am1.T = aq.V;
        return;
      } 
      if (am1.b != null) {
        a(am1.b);
        am1.b = null;
      } 
      am1.T = aq.Z;
      am1.m = Math.max(0.05F, 0.45F);
      am1.l = am1.m;
      return;
    } 
    String str = ap.o;
    float f = this.n;
    FileHandle fileHandle1;
    FileHandle fileHandle2;
    FileHandle fileHandle3;
    if ((fileHandle1 = (FileHandle)((fileHandle2 = Gdx.files.absolute("" + f + f + ".ogg")).exists() ? fileHandle2 : ((fileHandle3 = Gdx.files.absolute("" + f + f + ".mp3")).exists() ? fileHandle3 : ((fileHandle1 = Gdx.files.absolute("" + f + f + ".wav")).exists() ? fileHandle1 : null)))) == null) {
      Gdx.app.error("MusicManager", "Arquivo de mnencontrado: " + ap.o);
      return;
    } 
    f = ((f = ap.s) > 0.0F) ? f : 0.45F;
    if (this.a == null) {
      float f1 = f;
      ap = ap;
      fileHandle1 = fileHandle1;
      am1 = this;
      try {
        Music music;
        if ((music = am1.a(fileHandle1, ap.o)) == null) {
          am1.T = aq.V;
          return;
        } 
        am1.a = music;
        am1.a.setLooping(ap.m);
        am1.k = c(ap.a.a((Random)am1.a));
        am1.T = aq.W;
        am1.m = Math.max(0.01F, f1);
        am1.l = am1.m;
        am1.a.setVolume(0.0F);
        am1.a.play();
        return;
      } catch (Throwable throwable) {
        Gdx.app.error("MusicManager", "Falha tocando musica: " + fileHandle1.path() + " size=" + fileHandle1.length(), throwable);
        a(am1.a);
        am1.a = null;
        am1.T = aq.V;
        return;
      } 
    } 
    am am2 = am1;
    ap = ap;
    fileHandle1 = fileHandle1;
    am am1;
    if ((am1 = this).b != null) {
      a(am1.b);
      am1.b = null;
    } 
    try {
      Music music;
      if ((music = am1.a(fileHandle1, ap.o)) == null) {
        am1.T = aq.X;
        am1.q();
        return;
      } 
      am1.b = music;
      am1.b.setLooping(ap.m);
      am1.n = c(ap.a.a((Random)am1.a));
      am1.p = Math.max(0.05F, am2);
      am1.o = am1.p;
      am1.T = aq.Y;
      am1.a(am1.a, am1.k, 1.0F);
      am1.b.setVolume(0.0F);
      am1.b.play();
      return;
    } catch (Throwable throwable) {
      Gdx.app.error("MusicManager", "Falha iniciando crossfade: " + fileHandle1.path() + " size=" + fileHandle1.length(), throwable);
      a(am1.b);
      am1.b = null;
      am1.T = aq.X;
      am1.q();
      return;
    } 
  }
  
  private Music a(FileHandle paramFileHandle, String paramString) {
    Music music2;
    if ((music2 = a(paramFileHandle)) != null)
      return music2; 
    FileHandle fileHandle2 = Gdx.files.absolute("" + this.n + this.n + ".ogg");
    FileHandle fileHandle1 = Gdx.files.absolute("" + this.n + this.n + ".mp3");
    FileHandle fileHandle3 = Gdx.files.absolute("" + this.n + this.n + ".wav");
    Music music1;
    if (fileHandle1.exists() && (paramFileHandle == null || !fileHandle1.path().equals(paramFileHandle.path())) && (music1 = a(fileHandle1)) != null)
      return music1; 
    if (fileHandle3.exists() && (paramFileHandle == null || !fileHandle3.path().equals(paramFileHandle.path())) && (music1 = a(fileHandle3)) != null)
      return music1; 
    if (fileHandle2.exists() && (paramFileHandle == null || !fileHandle2.path().equals(paramFileHandle.path())) && (music1 = a(fileHandle2)) != null)
      return music1; 
    String str = "" + this.n + this.n + ".[ogg|mp3|wav]";
    this.c.add(str);
    return null;
  }
  
  private Music a(FileHandle paramFileHandle) {
    // Byte code:
    //   0: aload_1
    //   1: ifnull -> 11
    //   4: aload_1
    //   5: invokevirtual exists : ()Z
    //   8: ifne -> 13
    //   11: aconst_null
    //   12: areturn
    //   13: getstatic com/badlogic/gdx/Gdx.audio : Lcom/badlogic/gdx/Audio;
    //   16: aload_1
    //   17: invokeinterface newMusic : (Lcom/badlogic/gdx/files/FileHandle;)Lcom/badlogic/gdx/audio/Music;
    //   22: areturn
    //   23: astore_2
    //   24: aload_1
    //   25: invokevirtual extension : ()Ljava/lang/String;
    //   28: ldc 'ogg'
    //   30: invokevirtual equalsIgnoreCase : (Ljava/lang/String;)Z
    //   33: ifeq -> 98
    //   36: aload_2
    //   37: astore_3
    //   38: aload_3
    //   39: ifnull -> 90
    //   42: aload_3
    //   43: invokevirtual getMessage : ()Ljava/lang/String;
    //   46: dup
    //   47: astore #4
    //   49: ifnull -> 82
    //   52: aload #4
    //   54: invokevirtual toLowerCase : ()Ljava/lang/String;
    //   57: dup
    //   58: astore #4
    //   60: ldc 'does not contain vorbis'
    //   62: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   65: ifne -> 78
    //   68: aload #4
    //   70: ldc 'vorbis audio data'
    //   72: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   75: ifeq -> 82
    //   78: iconst_1
    //   79: goto -> 91
    //   82: aload_3
    //   83: invokevirtual getCause : ()Ljava/lang/Throwable;
    //   86: astore_3
    //   87: goto -> 38
    //   90: iconst_0
    //   91: ifeq -> 98
    //   94: iconst_1
    //   95: goto -> 99
    //   98: iconst_0
    //   99: istore_3
    //   100: aload_0
    //   101: getfield c : Ljava/util/Set;
    //   104: aload_1
    //   105: invokevirtual path : ()Ljava/lang/String;
    //   108: invokeinterface add : (Ljava/lang/Object;)Z
    //   113: ifeq -> 166
    //   116: iload_3
    //   117: ifeq -> 142
    //   120: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   123: ldc 'MusicManager'
    //   125: aload_1
    //   126: invokevirtual path : ()Ljava/lang/String;
    //   129: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;)Ljava/lang/String;
    //   134: invokeinterface log : (Ljava/lang/String;Ljava/lang/String;)V
    //   139: goto -> 166
    //   142: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   145: ldc 'MusicManager'
    //   147: aload_1
    //   148: invokevirtual path : ()Ljava/lang/String;
    //   151: aload_1
    //   152: invokevirtual length : ()J
    //   155: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;J)Ljava/lang/String;
    //   160: aload_2
    //   161: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   166: aconst_null
    //   167: areturn
    //   168: astore_2
    //   169: aload_0
    //   170: getfield c : Ljava/util/Set;
    //   173: aload_1
    //   174: invokevirtual path : ()Ljava/lang/String;
    //   177: invokeinterface add : (Ljava/lang/Object;)Z
    //   182: ifeq -> 209
    //   185: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   188: ldc 'MusicManager'
    //   190: aload_1
    //   191: invokevirtual path : ()Ljava/lang/String;
    //   194: aload_1
    //   195: invokevirtual length : ()J
    //   198: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;J)Ljava/lang/String;
    //   203: aload_2
    //   204: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   209: aconst_null
    //   210: areturn
    // Exception table:
    //   from	to	target	type
    //   13	22	23	com/badlogic/gdx/utils/GdxRuntimeException
    //   13	22	168	java/lang/Throwable
  }
  
  final void q() {
    if (this.T == aq.Y && this.a != null && this.b != null) {
      float f = 1.0F - this.o / b(this.p);
      a(this.a, this.k, 1.0F - f);
      a(this.b, this.n, f);
      return;
    } 
    if (this.a != null) {
      if (this.T == aq.W) {
        float f = 1.0F - this.l / b(this.m);
        a(this.a, this.k, f);
        return;
      } 
      if (this.T == aq.Z) {
        float f = this.l / b(this.m);
        a(this.a, this.k, f);
        return;
      } 
      a(this.a, this.k, 1.0F);
    } 
  }
  
  final void a(Music paramMusic, float paramFloat1, float paramFloat2) {
    if (paramMusic == null)
      return; 
    paramFloat1 = c(paramFloat1) * c(this.j) * c(paramFloat2);
    paramMusic.setVolume(paramFloat1);
  }
  
  static float b(float paramFloat) {
    return (paramFloat <= 1.0E-4F) ? 1.0E-4F : paramFloat;
  }
  
  static void a(Music paramMusic) {
    if (paramMusic == null)
      return; 
    try {
      paramMusic.stop();
    } catch (Exception exception) {}
    try {
      paramMusic.dispose();
      return;
    } catch (Exception exception) {
      return;
    } 
  }
  
  private XmlReader.Element a(XmlReader.Element paramElement) {
    if ("sound".equals(paramElement.getName()))
      return paramElement; 
    for (byte b = 0; b < paramElement.getChildCount(); b++) {
      XmlReader.Element element = paramElement.getChild(b);
      if ((element = a(element)) != null)
        return element; 
    } 
    return null;
  }
  
  static float c(float paramFloat) {
    return (paramFloat < 0.0F) ? 0.0F : Math.min(paramFloat, 1.0F);
  }
  
  private static ao a(String paramString) {
    if (paramString == null || paramString.trim().isEmpty()) {
      100.0F / 100.0F;
      return new ao(1.0F, 1.0F);
    } 
    int i = (paramString = paramString.trim()).indexOf('-');
    try {
      float f1;
      if (i > 0) {
        float f4 = Float.parseFloat(paramString.substring(0, i).trim()) / 100.0F;
        f1 = Float.parseFloat(paramString.substring(i + 1).trim()) / 100.0F;
        float f3 = Math.min(f4, f1);
        f1 = Math.max(f4, f1);
        return new ao(c(f3), c(f1));
      } 
      float f2 = c(Float.parseFloat(f1) / 100.0F);
      return new ao(f2, f2);
    } catch (Exception exception) {
      100.0F / 100.0F;
      return new ao(1.0F, 1.0F);
    } 
  }
}
