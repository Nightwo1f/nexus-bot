package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.audio.Sound;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.XmlReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

final class ar {
  final Map r = new HashMap<>();
  
  final Map s = new HashMap<>();
  
  private final Map t = new HashMap<>();
  
  private final Random b = new Random();
  
  float j = 1.0F;
  
  final void b(String paramString1, String paramString2) {
    this.r.clear();
    FileHandle fileHandle;
    if (!(fileHandle = Gdx.files.absolute(paramString1 + paramString1)).exists())
      return; 
    try {
      Array.ArrayIterator<XmlReader.Element> arrayIterator = (new XmlReader()).parse(fileHandle).getChildrenByName("setting").iterator();
      while (arrayIterator.hasNext()) {
        XmlReader.Element element;
        String str;
        if ((str = (element = arrayIterator.next()).getAttribute("id", null)) != null) {
          int i = Integer.parseInt(str);
          au au = new au(i);
          for (byte b = 0; b < element.getChildCount(); b++) {
            XmlReader.Element element1 = element.getChild(b);
            if ("client".equals(element1.getName())) {
              Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element1.getChildrenByName("channel").iterator();
              while (arrayIterator1.hasNext()) {
                XmlReader.Element element2 = arrayIterator1.next();
                XmlReader.Element element3 = element2;
                String str1 = paramString1;
                au au1 = au;
                ar ar1 = this;
                Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element3.getChildrenByName("sound").iterator();
                while (arrayIterator2.hasNext()) {
                  XmlReader.Element element5 = arrayIterator2.next();
                  av av;
                  if ((av = ar1.a(str1, element5)) != null)
                    au1.a(av); 
                } 
                XmlReader.Element element4;
                if ((element4 = element3.getChildByName("randomize")) != null) {
                  Array.ArrayIterator<XmlReader.Element> arrayIterator3 = element4.getChildrenByName("sound").iterator();
                  while (arrayIterator3.hasNext()) {
                    XmlReader.Element element5 = arrayIterator3.next();
                    av av;
                    if ((av = ar1.a(str1, element5)) != null)
                      au1.a(av); 
                  } 
                } 
              } 
            } 
          } 
          if (!au.a.isEmpty())
            this.r.put(Integer.valueOf(i), au); 
        } 
      } 
      return;
    } catch (Exception exception) {
      Gdx.app.error("SfxManager", "Falha parseando " + fileHandle.path(), exception);
      return;
    } 
  }
  
  private av a(String paramString, XmlReader.Element paramElement) {
    String str;
    if ((str = paramElement.getAttribute("file", null)) == null || str.isEmpty())
      return null; 
    as as = a(paramElement.getAttribute("volume", "100"));
    boolean bool = "infinite".equalsIgnoreCase(paramElement.getAttribute("repetitions", ""));
    int i = paramElement.getIntAttribute("probability", 100);
    Sound sound;
    return ((sound = a(paramString, str)) == null) ? null : new av(sound, as, bool, i);
  }
  
  private Sound a(String paramString1, String paramString2) {
    Sound sound2;
    if ((sound2 = (Sound)this.s.get(paramString2)) != null)
      return sound2; 
    FileHandle fileHandle;
    if ((fileHandle = b(paramString1, paramString2)) == null) {
      Gdx.app.error("SfxManager", "Arquivo de som nencontrado para: " + paramString2);
      return null;
    } 
    Sound sound1 = Gdx.audio.newSound(fileHandle);
    this.s.put(paramString2, sound1);
    return sound1;
  }
  
  private static FileHandle b(String paramString1, String paramString2) {
    FileHandle fileHandle1;
    FileHandle fileHandle2;
    return (fileHandle2 = Gdx.files.absolute(paramString1 + paramString1 + ".wav")).exists() ? fileHandle2 : ((fileHandle2 = Gdx.files.absolute(paramString1 + paramString1 + ".ogg")).exists() ? fileHandle2 : ((fileHandle1 = Gdx.files.absolute(paramString1 + paramString1 + ".mp3")).exists() ? fileHandle1 : null));
  }
  
  final long a(int paramInt) {
    au au;
    if ((au = (au)this.r.get(Integer.valueOf(paramInt))) == null)
      return -1L; 
    av av;
    if ((av = au.a(this.b)) == null)
      return -1L; 
    float f = c(this.j * av.a.b(this.b));
    if (av.n) {
      d(paramInt);
      long l = av.b.loop(f);
      this.t.put(Integer.valueOf(paramInt), new at(av.b, l));
      return l;
    } 
    return av.b.play(f);
  }
  
  private void d(int paramInt) {
    at at;
    if ((at = (at)this.t.remove(Integer.valueOf(paramInt))) != null)
      at.a.stop(at.b); 
  }
  
  final void r() {
    for (Integer integer : new ArrayList(this.t.keySet()))
      d(integer.intValue()); 
  }
  
  static float c(float paramFloat) {
    return (paramFloat < 0.0F) ? 0.0F : Math.min(paramFloat, 1.0F);
  }
  
  private static as a(String paramString) {
    if (paramString == null || paramString.trim().isEmpty()) {
      100.0F / 100.0F;
      return new as(1.0F, 1.0F);
    } 
    int i = (paramString = paramString.trim()).indexOf('-');
    try {
      float f1;
      if (i > 0) {
        float f4 = Float.parseFloat(paramString.substring(0, i).trim()) / 100.0F;
        f1 = Float.parseFloat(paramString.substring(i + 1).trim()) / 100.0F;
        float f3 = Math.min(f4, f1);
        f1 = Math.max(f4, f1);
        return new as(c(f3), c(f1));
      } 
      float f2 = c(Float.parseFloat(f1) / 100.0F);
      return new as(f2, f2);
    } catch (Exception exception) {
      100.0F / 100.0F;
      return new as(1.0F, 1.0F);
    } 
  }
}
