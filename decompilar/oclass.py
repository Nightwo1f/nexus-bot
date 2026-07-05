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

public final class o {
  private final AssetManager d;
  
  private final String g;
  
  private final Map g = new HashMap<>();
  
  private static final Pattern d = Pattern.compile("\\d+");
  
  public o(AssetManager paramAssetManager, String paramString) {
    this.d = (Pattern)paramAssetManager;
    this.g = (Map)paramString;
  }
  
  public final void i() {
    FileHandle fileHandle = Gdx.files.absolute((String)this.g);
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
          if (d.matcher(str).matches())
            try {
              if (!(str = fileHandle2.readString("UTF-8")).isEmpty() && str.charAt(0) == ')
                str = str.substring(1); 
              XmlReader.Element element1;
              XmlReader.Element element2;
              if ((element2 = (element1 = xmlReader.parse(str)).getChildByName("items")) != null) {
                int k = element2.getIntAttribute("packid");
                int m = k;
                XmlReader.Element element = element1;
                o o1 = this;
                HashMap<Object, Object> hashMap2 = new HashMap<>();
                if ((element = element.getChildByName("images")) != null) {
                  ArrayList<String> arrayList = new ArrayList();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator1.hasNext()) {
                    String str1 = ((XmlReader.Element)arrayIterator1.next()).getAttribute("file");
                    FileHandle fileHandle3;
                    if ((fileHandle3 = a.a((String)o1.g, str1, m)) == null)
                      throw new GdxRuntimeException("Texture nencontrada: file=\"" + str1 + "\" pack=" + m + " base=" + o1.g); 
                    String str2 = fileHandle3.file().getAbsolutePath();
                    if (!o1.d.isLoaded(str2, Texture.class))
                      o1.d.load(str2, Texture.class); 
                    arrayList.add(str2);
                  } 
                  o1.d.finishLoading();
                  byte b2 = 0;
                  Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element.getChildrenByName("texture").iterator();
                  while (arrayIterator2.hasNext()) {
                    XmlReader.Element element3 = arrayIterator2.next();
                    String str1 = arrayList.get(b2++);
                    Texture texture;
                    (texture = (Texture)o1.d.get(str1, Texture.class)).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
                    texture.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
                    int n = texture.getWidth();
                    m = texture.getHeight();
                    Array.ArrayIterator<XmlReader.Element> arrayIterator3 = element3.getChildrenByName("t").iterator();
                    while (arrayIterator3.hasNext()) {
                      XmlReader.Element element4;
                      int i2 = (element4 = arrayIterator3.next()).getIntAttribute("id");
                      String[] arrayOfString2;
                      int i5 = Integer.parseInt((arrayOfString2 = element4.getAttribute("s").split(","))[0]);
                      int i3 = Integer.parseInt(arrayOfString2[1]);
                      String[] arrayOfString3;
                      int i7 = Integer.parseInt((arrayOfString3 = element4.getAttribute("p").split(","))[0]);
                      int i6 = Integer.parseInt(arrayOfString3[1]);
                      TextureRegion textureRegion = new TextureRegion(texture, i7, i6, i5, i3);
                      float f1 = 0.25F / n;
                      float f2 = 0.25F / m;
                      textureRegion.setU(textureRegion.getU() + f1);
                      textureRegion.setV(textureRegion.getV() + f2);
                      textureRegion.setU2(textureRegion.getU2() - f1);
                      textureRegion.setV2(textureRegion.getV2() - f2);
                      String[] arrayOfString1;
                      int i4 = Integer.parseInt((arrayOfString1 = element4.getAttribute("o", "0,0").split(","))[0]);
                      int i1 = Integer.parseInt(arrayOfString1[1]);
                      hashMap2.put(Integer.valueOf(i2), new p(textureRegion, i4, i1));
                    } 
                  } 
                } 
                HashMap<Object, Object> hashMap1 = hashMap2;
                Array.ArrayIterator<XmlReader.Element> arrayIterator = element2.getChildrenByName("x").iterator();
                while (arrayIterator.hasNext()) {
                  Array array2;
                  m = (element = arrayIterator.next()).getIntAttribute("si");
                  XmlReader.Element element3;
                  if ((element3 = element.getChildByName("a")) != null) {
                    array2 = element3.getChildrenByName("f");
                  } else {
                    array2 = element.getChildrenByName("f");
                  } 
                  if (array2 == null || array2.size == 0) {
                    Gdx.app.error("ItemLoader", "AVISO: Arquivo: " + fileHandle2.name() + " | SI (Local ID): " + m);
                    continue;
                  } 
                  element = element.getChildByName("light");
                  int i1 = 0;
                  Color color = null;
                  if (element != null) {
                    i1 = element.getIntAttribute("s", 0);
                    String[] arrayOfString;
                    float f1 = Integer.parseInt((arrayOfString = element.getAttribute("c").split(","))[0]) / 255.0F;
                    float f2 = Integer.parseInt(arrayOfString[1]) / 255.0F;
                    float f3 = Integer.parseInt(arrayOfString[2]) / 255.0F;
                    float f4 = Integer.parseInt(arrayOfString[3]) / 255.0F;
                    color = new Color(f1, f2, f3, f4);
                  } 
                  Array array1 = new Array();
                  Array array3 = new Array();
                  Array array4 = new Array();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = array2.iterator();
                  while (arrayIterator1.hasNext()) {
                    XmlReader.Element element4;
                    int i3 = (element4 = arrayIterator1.next()).getIntAttribute("id");
                    p p = (p)hashMap1.get(Integer.valueOf(i3));
                    array1.add(p.l);
                    array3.add(new Vector2(p.m, p.n));
                    String str2;
                    String str1 = (str2 = element4.getAttribute("p", "150")).contains(",") ? str2.split(",")[0] : (str2.contains("-") ? str2.split("-")[0] : str2);
                    array4.add(Float.valueOf(Integer.parseInt(str1) / 1000.0F));
                  } 
                  TextureRegion[] arrayOfTextureRegion = (TextureRegion[])array1.toArray(TextureRegion.class);
                  float[] arrayOfFloat = new float[array4.size];
                  for (byte b2 = 0; b2 < array4.size; b2++)
                    arrayOfFloat[b2] = ((Float)array4.get(b2)).floatValue(); 
                  int[] arrayOfInt2 = new int[array3.size];
                  int[] arrayOfInt1 = new int[array3.size];
                  int i2;
                  for (i2 = 0; i2 < array3.size; i2++) {
                    arrayOfInt2[i2] = (int)((Vector2)array3.get(i2)).x;
                    arrayOfInt1[i2] = (int)((Vector2)array3.get(i2)).y;
                  } 
                  i2 = k << 8 | m;
                  n n = new n(i2, arrayOfTextureRegion, arrayOfFloat, arrayOfInt2, arrayOfInt1, i1, color);
                  this.g.put(Integer.valueOf(i2), n);
                } 
              } 
            } catch (Exception exception) {
              Gdx.app.error("ItemLoader", "Erro ao parsear " + fileHandle2.path(), exception);
            }  
        } 
      } 
    } 
  }
  
  public final n a(int paramInt) {
    return (n)this.g.get(Integer.valueOf(paramInt));
  }
}
