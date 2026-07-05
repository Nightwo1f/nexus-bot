package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.assets.AssetManager;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.GdxRuntimeException;
import com.badlogic.gdx.utils.XmlReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

public final class v {
  private final AssetManager f;
  
  private final String i;
  
  public final Map j = new HashMap<>();
  
  private static final Pattern f = Pattern.compile("\\d+");
  
  private final int t;
  
  public v(AssetManager paramAssetManager, String paramString, int paramInt) {
    this.f = (Pattern)paramAssetManager;
    this.i = paramString;
    this.t = paramInt;
  }
  
  public final void k() {
    FileHandle fileHandle = Gdx.files.absolute(this.i);
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
          if (f.matcher(str).matches())
            try {
              String str1;
              if (!(str1 = fileHandle2.readString("UTF-8")).isEmpty() && str1.charAt(0) == ')
                str1 = str1.substring(1); 
              XmlReader.Element element1;
              XmlReader.Element element2;
              if ((element2 = (element1 = xmlReader.parse(str1)).getChildByName("creatures")) != null) {
                int k = element2.getIntAttribute("packid");
                int m = k;
                XmlReader.Element element = element1;
                v v1 = this;
                HashMap<Object, Object> hashMap2 = new HashMap<>();
                if ((element = element.getChildByName("images")) != null) {
                  ArrayList<String> arrayList = new ArrayList();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator1.hasNext()) {
                    String str2 = ((XmlReader.Element)arrayIterator1.next()).getAttribute("file");
                    FileHandle fileHandle3;
                    if ((fileHandle3 = a.a(v1.i, str2, m)) == null)
                      throw new GdxRuntimeException("Texture nencontrada: file=\"" + str2 + "\" pack=" + m + " base=" + v1.i); 
                    str2 = fileHandle3.file().getAbsolutePath();
                    if (!v1.f.isLoaded(str2, Texture.class))
                      v1.f.load(str2, Texture.class); 
                    arrayList.add(str2);
                  } 
                  v1.f.finishLoading();
                  byte b2 = 0;
                  Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator2.hasNext()) {
                    XmlReader.Element element3 = arrayIterator2.next();
                    Texture texture = (Texture)v1.f.get(arrayList.get(b2++), Texture.class);
                    Array.ArrayIterator<XmlReader.Element> arrayIterator3 = element3.getChildrenByName("t").iterator();
                    while (arrayIterator3.hasNext()) {
                      m = (element = arrayIterator3.next()).getIntAttribute("id");
                      String[] arrayOfString2;
                      int i3 = Integer.parseInt((arrayOfString2 = element.getAttribute("s").split(","))[0]);
                      int i1 = Integer.parseInt(arrayOfString2[1]);
                      String[] arrayOfString3;
                      int i5 = Integer.parseInt((arrayOfString3 = element.getAttribute("p").split(","))[0]);
                      int i4 = Integer.parseInt(arrayOfString3[1]);
                      int i6 = i1;
                      i5 = i3;
                      i4 = i4;
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
                      hashMap2.put(Integer.valueOf(m), new w(textureRegion1, i2, n));
                    } 
                  } 
                } 
                HashMap<Object, Object> hashMap1 = hashMap2;
                Array.ArrayIterator<XmlReader.Element> arrayIterator = element2.getChildrenByName("x").iterator();
                while (arrayIterator.hasNext()) {
                  m = (element = arrayIterator.next()).getIntAttribute("si");
                  hashMap2 = new HashMap<>();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("a").iterator();
                  while (arrayIterator1.hasNext()) {
                    XmlReader.Element element3;
                    int i1 = (element3 = arrayIterator1.next()).getIntAttribute("id");
                    boolean bool1 = (element3.getIntAttribute("l", 1) == 1) ? true : false;
                    boolean bool2 = (element3.getIntAttribute("s", 0) == 1) ? true : false;
                    XmlReader.Element element4 = element.getChildByName("light");
                    int i2 = 0;
                    Color color = null;
                    if (element4 != null) {
                      i2 = element4.getIntAttribute("s", 0);
                      String[] arrayOfString1;
                      float f1 = Integer.parseInt((arrayOfString1 = element4.getAttribute("c").split(","))[0]) / 255.0F;
                      float f2 = Integer.parseInt(arrayOfString1[1]) / 255.0F;
                      float f3 = Integer.parseInt(arrayOfString1[2]) / 255.0F;
                      float f4 = Integer.parseInt(arrayOfString1[3]) / 255.0F;
                      color = new Color(f1, f2, f3, f4);
                    } 
                    Array array1 = new Array();
                    Array array2 = new Array();
                    Array array3 = new Array();
                    Array array4 = new Array();
                    Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element3.getChildrenByName("f").iterator();
                    while (arrayIterator2.hasNext()) {
                      XmlReader.Element element5;
                      int i3 = (element5 = arrayIterator2.next()).getIntAttribute("id");
                      w w;
                      if ((w = (w)hashMap1.get(Integer.valueOf(i3))) != null) {
                        TextureRegion textureRegion = new TextureRegion(w.n);
                        int i5 = w.u;
                        int i4 = w.v;
                        String str3;
                        String[] arrayOfString1;
                        if (((arrayOfString1 = (str3 = element5.getAttribute("tf", "0,0,0,0,0")).split(",")).length > 1 && "1".equals(arrayOfString1[1]))) {
                          textureRegion.flip(true, false);
                          i5 = this.t - textureRegion.getRegionWidth() - i5;
                        } 
                        array1.add(textureRegion);
                        array2.add(new Vector2(i5, i4));
                        String str2;
                        if ((str2 = element5.getAttribute("p", "150")).contains(",")) {
                          str2.split(",")[0];
                        } else if (str2.contains("-")) {
                          str2.split("-")[0];
                        } 
                        array3.add(Float.valueOf(Integer.parseInt("100") / 1000.0F));
                        array4.add(str3);
                      } 
                    } 
                    TextureRegion[] arrayOfTextureRegion = (TextureRegion[])array1.toArray(TextureRegion.class);
                    float[] arrayOfFloat = new float[array3.size];
                    for (byte b2 = 0; b2 < array3.size; b2++)
                      arrayOfFloat[b2] = ((Float)array3.get(b2)).floatValue(); 
                    Vector2[] arrayOfVector2 = new Vector2[array2.size];
                    for (byte b3 = 0; b3 < array2.size; b3++)
                      arrayOfVector2[b3] = (Vector2)array2.get(b3); 
                    String[] arrayOfString = (String[])array4.toArray(String.class);
                    u u = new u(arrayOfTextureRegion, arrayOfFloat, arrayOfVector2, arrayOfString, bool1, bool2, i2, color);
                    hashMap2.put(Integer.valueOf(i1), u);
                  } 
                  int n = k << 8 | m;
                  this.j.put(Integer.valueOf(n), new t(n, hashMap2));
                } 
              } 
            } catch (Exception exception) {
              Gdx.app.error("MobLoader", "Falha ao parsear XML: " + exception.getMessage());
            }  
        } 
      } 
    } 
  }
  
  public final t a(int paramInt) {
    return (t)this.j.get(Integer.valueOf(paramInt));
  }
}
