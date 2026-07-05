package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.assets.AssetManager;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.GdxRuntimeException;
import com.badlogic.gdx.utils.XmlReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

public final class aa {
  private final AssetManager g;
  
  private final String j;
  
  public final int y;
  
  public final int z;
  
  private final Map l = new HashMap<>();
  
  private static final Pattern g = Pattern.compile("\\d+");
  
  public aa(AssetManager paramAssetManager, String paramString, int paramInt1, int paramInt2) {
    this.g = (Pattern)paramAssetManager;
    this.j = paramString;
    this.y = paramInt1;
    this.z = paramInt2;
  }
  
  public final void l() {
    FileHandle fileHandle = Gdx.files.absolute(this.j);
    XmlReader xmlReader = new XmlReader();
    FileHandle[] arrayOfFileHandle;
    int i = (arrayOfFileHandle = fileHandle.list()).length;
    for (byte b = 0; b < i; b++) {
      FileHandle fileHandle1;
      if ((fileHandle1 = arrayOfFileHandle[b]).isDirectory() && fileHandle1.name().startsWith("pack")) {
        FileHandle[] arrayOfFileHandle1;
        int j = (arrayOfFileHandle1 = fileHandle1.list("xml")).length;
        for (byte b1 = 0; b1 < j; b1++) {
          FileHandle fileHandle2;
          String str = (fileHandle2 = arrayOfFileHandle1[b1]).nameWithoutExtension();
          if (g.matcher(str).matches())
            try {
              String str1;
              if (!(str1 = fileHandle2.readString("UTF-8")).isEmpty() && str1.charAt(0) == ')
                str1 = str1.substring(1); 
              XmlReader.Element element1;
              XmlReader.Element element2;
              if ((element2 = (element1 = xmlReader.parse(str1)).getChildByName("outfits")) != null) {
                int k = element2.getIntAttribute("packid");
                int m = k;
                XmlReader.Element element = element1;
                aa aa1 = this;
                HashMap<Object, Object> hashMap2 = new HashMap<>();
                if ((element = element.getChildByName("images")) != null) {
                  ArrayList<String> arrayList = new ArrayList();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator1.hasNext()) {
                    String str2 = ((XmlReader.Element)arrayIterator1.next()).getAttribute("file");
                    FileHandle fileHandle3;
                    if ((fileHandle3 = a.a(aa1.j, str2, m)) == null)
                      throw new GdxRuntimeException("Texture nencontrada: " + str2 + " (pack " + m + ")"); 
                    str2 = fileHandle3.file().getAbsolutePath();
                    if (!aa1.g.isLoaded(str2, Texture.class))
                      aa1.g.load(str2, Texture.class); 
                    arrayList.add(str2);
                  } 
                  aa1.g.finishLoading();
                  byte b2 = 0;
                  Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator2.hasNext()) {
                    XmlReader.Element element3 = arrayIterator2.next();
                    Texture texture = (Texture)aa1.g.get(arrayList.get(b2++), Texture.class);
                    Array.ArrayIterator<XmlReader.Element> arrayIterator3 = element3.getChildrenByName("t").iterator();
                    while (arrayIterator3.hasNext()) {
                      m = (element = arrayIterator3.next()).getIntAttribute("id");
                      String[] arrayOfString2 = element.getAttribute("s").split(",");
                      String[] arrayOfString3 = element.getAttribute("p").split(",");
                      int i4 = Integer.parseInt(arrayOfString2[0]);
                      int i1 = Integer.parseInt(arrayOfString2[1]);
                      int i5 = Integer.parseInt(arrayOfString3[0]);
                      int i3 = Integer.parseInt(arrayOfString3[1]);
                      int i6 = i1;
                      i5 = i4;
                      i4 = i3;
                      i3 = i5;
                      Texture texture1 = texture;
                      TextureRegion textureRegion2 = new TextureRegion(texture1, i3, i4, i5, i6);
                      float f3 = 1.0F / texture1.getWidth();
                      float f1 = 1.0F / texture1.getHeight();
                      float f4 = (i3 + 0.1F) * f3;
                      float f5 = (i4 + 0.1F) * f1;
                      float f2 = ((i3 + i5) - 0.1F) * f3;
                      f1 = ((i4 + i6) - 0.1F) * f1;
                      textureRegion2.setRegion(f4, f5, f2, f1);
                      TextureRegion textureRegion1 = textureRegion2;
                      String[] arrayOfString1;
                      int i2 = Integer.parseInt((arrayOfString1 = element.getAttribute("o", "0,0").split(","))[0]);
                      int n = Integer.parseInt(arrayOfString1[1]);
                      hashMap2.put(Integer.valueOf(m), new ab(textureRegion1, i2, n));
                    } 
                  } 
                } 
                HashMap<Object, Object> hashMap1 = hashMap2;
                Array.ArrayIterator<XmlReader.Element> arrayIterator = element2.getChildrenByName("x").iterator();
                while (arrayIterator.hasNext()) {
                  m = (element = arrayIterator.next()).getIntAttribute("si");
                  hashMap2 = new HashMap<>();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("ap").iterator();
                  while (arrayIterator1.hasNext()) {
                    XmlReader.Element element3;
                    int i1 = (element3 = arrayIterator1.next()).getIntAttribute("p");
                    int i2 = element3.getIntAttribute("pn");
                    int i3 = element3.getIntAttribute("a");
                    Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element3.getChildrenByName("f").iterator();
                    while (arrayIterator2.hasNext()) {
                      XmlReader.Element element4;
                      int i4 = (element4 = arrayIterator2.next()).getIntAttribute("id");
                      ab ab;
                      if ((ab = (ab)hashMap1.get(Integer.valueOf(i4))) != null) {
                        String str2;
                        String[] arrayOfString;
                        boolean bool = ((arrayOfString = (str2 = element4.getAttribute("tf", "0,0,0,0,0")).split(",")).length > 1 && "1".equals(arrayOfString[1])) ? true : false;
                        int i5 = element4.getIntAttribute("mo", 0);
                        TextureRegion textureRegion = new TextureRegion(ab.o);
                        int i6 = ab.A;
                        int i7 = ab.B;
                        if (bool) {
                          textureRegion.flip(true, false);
                          i6 = this.y - textureRegion.getRegionWidth() - i6;
                        } 
                        ac ac = new ac(textureRegion, i6, i7, i1, str2, i5);
                        ((List<ac>)((Map<Integer, List<ac>>)hashMap2.computeIfAbsent(Integer.valueOf(i3), paramInteger -> new HashMap<>())).computeIfAbsent(Integer.valueOf(i2), paramInteger -> new ArrayList())).add(ac);
                      } 
                    } 
                  } 
                  HashMap<Object, Object> hashMap = new HashMap<>();
                  Iterator<Map.Entry> iterator = hashMap2.entrySet().iterator();
                  while (iterator.hasNext()) {
                    Map.Entry<Integer, ?> entry;
                    int i1 = ((Integer)(entry = iterator.next()).getKey()).intValue();
                    Map<? extends Integer, ?> map;
                    int i2;
                    TextureRegion[][] arrayOfTextureRegion = new TextureRegion[i2 = ((Integer)Collections.<Integer>max((map = (Map<? extends Integer, ?>)entry.getValue()).keySet())).intValue()][];
                    Vector2[][] arrayOfVector2 = new Vector2[i2][];
                    String[][] arrayOfString = new String[i2][];
                    int[][] arrayOfInt1 = new int[i2][];
                    float[] arrayOfFloat = new float[i2];
                    int[][] arrayOfInt2 = new int[i2][];
                    for (byte b2 = 1; b2 <= i2; b2++) {
                      List<ac> list;
                      if ((list = (List)map.get(Integer.valueOf(b2))) == null || list.isEmpty()) {
                        arrayOfTextureRegion[b2 - 1] = new TextureRegion[0];
                        arrayOfVector2[b2 - 1] = new Vector2[0];
                        arrayOfString[b2 - 1] = new String[0];
                        arrayOfInt1[b2 - 1] = new int[0];
                        arrayOfFloat[b2 - 1] = 0.0F;
                      } else {
                        list.sort(Comparator.comparingInt(paramac -> paramac.E));
                        int i3;
                        TextureRegion[] arrayOfTextureRegion1 = new TextureRegion[i3 = list.size()];
                        Vector2[] arrayOfVector21 = new Vector2[i3];
                        String[] arrayOfString1 = new String[i3];
                        int[] arrayOfInt3 = new int[i3];
                        int[] arrayOfInt4 = new int[i3];
                        for (byte b3 = 0; b3 < i3; b3++) {
                          ac ac = list.get(b3);
                          arrayOfTextureRegion1[b3] = ac.p;
                          arrayOfVector21[b3] = new Vector2(ac.C, ac.D);
                          arrayOfString1[b3] = ac.k;
                          arrayOfInt3[b3] = ac.E;
                          arrayOfInt4[b3] = ac.F;
                        } 
                        arrayOfTextureRegion[b2 - 1] = arrayOfTextureRegion1;
                        arrayOfVector2[b2 - 1] = arrayOfVector21;
                        arrayOfString[b2 - 1] = arrayOfString1;
                        arrayOfInt1[b2 - 1] = arrayOfInt3;
                        arrayOfInt2[b2 - 1] = arrayOfInt4;
                        arrayOfFloat[b2 - 1] = 0.1F;
                      } 
                    } 
                    z z = new z(arrayOfTextureRegion, arrayOfVector2, arrayOfString, arrayOfInt1, arrayOfInt2, arrayOfFloat);
                    hashMap.put(Integer.valueOf(i1), z);
                  } 
                  int n = k << 8 | m;
                  this.l.put(Integer.valueOf(n), new y(n, hashMap));
                } 
              } 
            } catch (Exception exception) {
              Gdx.app.error("OutfitLoader", "Falha ao parsear XML: " + exception.getMessage(), exception);
            }  
        } 
      } 
    } 
  }
  
  public final y a(int paramInt) {
    return (y)this.l.get(Integer.valueOf(paramInt));
  }
}
