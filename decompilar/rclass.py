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
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

public final class r {
  private final AssetManager e;
  
  private final String h;
  
  private final Map h = new HashMap<>();
  
  private static final Pattern e = Pattern.compile("\\d+");
  
  public r(AssetManager paramAssetManager, String paramString) {
    this.e = (Pattern)paramAssetManager;
    this.h = (Map)paramString;
  }
  
  public final void j() {
    FileHandle fileHandle = Gdx.files.absolute((String)this.h);
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
          if (e.matcher(str).matches())
            try {
              if (!(str = fileHandle2.readString("UTF-8")).isEmpty() && str.charAt(0) == ')
                str = str.substring(1); 
              XmlReader.Element element1;
              XmlReader.Element element2;
              if ((element2 = (element1 = xmlReader.parse(str)).getChildByName("lightsources")) != null) {
                int k = element2.getIntAttribute("packid");
                int m = k;
                XmlReader.Element element = element1;
                r r1 = this;
                HashMap<Object, Object> hashMap2 = new HashMap<>();
                if ((element = element.getChildByName("images")) != null) {
                  ArrayList<String> arrayList = new ArrayList();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator1.hasNext()) {
                    String str1 = ((XmlReader.Element)arrayIterator1.next()).getAttribute("file");
                    FileHandle fileHandle3;
                    if ((fileHandle3 = a.a((String)r1.h, str1, m)) == null)
                      throw new GdxRuntimeException("Texture nencontrada: file=\"" + str1 + "\" pack=" + m + " base=" + r1.h); 
                    str1 = fileHandle3.file().getAbsolutePath();
                    if (!r1.e.isLoaded(str1, Texture.class))
                      r1.e.load(str1, Texture.class); 
                    arrayList.add(str1);
                  } 
                  r1.e.finishLoading();
                  byte b2 = 0;
                  Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator2.hasNext()) {
                    XmlReader.Element element3 = arrayIterator2.next();
                    Texture texture = (Texture)r1.e.get(arrayList.get(b2++), Texture.class);
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
                      hashMap2.put(Integer.valueOf(m), new s(textureRegion1, i2, n));
                    } 
                  } 
                } 
                HashMap<Object, Object> hashMap1 = hashMap2;
                Array.ArrayIterator<XmlReader.Element> arrayIterator = element2.getChildrenByName("x").iterator();
                while (arrayIterator.hasNext()) {
                  m = (element = arrayIterator.next()).getIntAttribute("si");
                  Array array1 = element.getChildByName("a").getChildrenByName("f");
                  Array array2 = new Array();
                  Array array3 = new Array();
                  Array array4 = new Array();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = array1.iterator();
                  while (arrayIterator1.hasNext()) {
                    XmlReader.Element element3;
                    int n = (element3 = arrayIterator1.next()).getIntAttribute("id");
                    s s = (s)hashMap1.get(Integer.valueOf(n));
                    array2.add(s.m);
                    array3.add(new Vector2(s.p, s.q));
                    String str2;
                    String str1 = (str2 = element3.getAttribute("p", "150")).contains(",") ? str2.split(",")[0] : (str2.contains("-") ? str2.split("-")[0] : str2);
                    array4.add(Float.valueOf(Integer.parseInt(str1) / 1000.0F));
                  } 
                  TextureRegion[] arrayOfTextureRegion = (TextureRegion[])array2.toArray(TextureRegion.class);
                  float[] arrayOfFloat = new float[array4.size];
                  for (byte b2 = 0; b2 < array4.size; b2++)
                    arrayOfFloat[b2] = ((Float)array4.get(b2)).floatValue(); 
                  int[] arrayOfInt1 = new int[array3.size];
                  int[] arrayOfInt2 = new int[array3.size];
                  for (byte b3 = 0; b3 < array3.size; b3++) {
                    arrayOfInt1[b3] = (int)((Vector2)array3.get(b3)).x;
                    arrayOfInt2[b3] = (int)((Vector2)array3.get(b3)).y;
                  } 
                  q q = new q(m, arrayOfTextureRegion, arrayOfFloat, arrayOfInt1, arrayOfInt2);
                  this.h.put(Integer.valueOf(m), q);
                } 
              } 
            } catch (Exception exception) {
              Gdx.app.error("LightLoader", "Erro ao parsear " + fileHandle2.path(), exception);
            }  
        } 
      } 
    } 
  }
  
  public final q a(int paramInt) {
    return (q)this.h.get(Integer.valueOf(paramInt));
  }
}
