package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.assets.AssetLoaderParameters;
import com.badlogic.gdx.assets.AssetManager;
import com.badlogic.gdx.assets.loaders.TextureLoader;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.GdxRuntimeException;
import com.badlogic.gdx.utils.XmlReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class ae {
  private final AssetManager h;
  
  private final String l;
  
  private final Map m = new HashMap<>();
  
  private final Map n = new HashMap<>();
  
  private static final Pattern h = Pattern.compile("\\d+");
  
  private static final Pattern i = Pattern.compile("^(?:\\.?\\./)?pack(\\d+)/(.+)$");
  
  public ae(AssetManager paramAssetManager, String paramString) {
    this.h = (Pattern)paramAssetManager;
    this.l = paramString.replace('\\', '/');
  }
  
  public final void m() {
    FileHandle fileHandle = Gdx.files.absolute(this.l);
    ArrayList<FileHandle> arrayList = new ArrayList();
    FileHandle[] arrayOfFileHandle;
    int i = (arrayOfFileHandle = fileHandle.list()).length;
    for (byte b = 0; b < i; b++) {
      FileHandle fileHandle1;
      if ((fileHandle1 = arrayOfFileHandle[b]).isDirectory() && fileHandle1.name().startsWith("pack"))
        arrayList.add(fileHandle1); 
    } 
    arrayList.sort(Comparator.comparingInt(ae::a));
    XmlReader xmlReader = new XmlReader();
    Iterator<FileHandle> iterator = arrayList.iterator();
    while (iterator.hasNext()) {
      FileHandle fileHandle1;
      int k = a(fileHandle1 = iterator.next());
      FileHandle[] arrayOfFileHandle1;
      Arrays.sort(arrayOfFileHandle1 = fileHandle1.list("xml"), (paramFileHandle1, paramFileHandle2) -> {
            String str1 = paramFileHandle1.nameWithoutExtension();
            String str2 = paramFileHandle2.nameWithoutExtension();
            int i = h.matcher(str1).matches() ? Integer.parseInt(str1) : Integer.MAX_VALUE;
            int j = h.matcher(str2).matches() ? Integer.parseInt(str2) : Integer.MAX_VALUE;
            return Integer.compare(i, j);
          });
      int j = arrayOfFileHandle1.length;
      for (byte b1 = 0; b1 < j; b1++) {
        FileHandle fileHandle2;
        String str = (fileHandle2 = arrayOfFileHandle1[b1]).nameWithoutExtension();
        if (h.matcher(str).matches())
          try {
            if (!(str = fileHandle2.readString("UTF-8")).isEmpty() && str.charAt(0) == ')
              str = str.substring(1); 
            XmlReader.Element element1;
            XmlReader.Element element2;
            if ((element2 = (element1 = xmlReader.parse(str)).getChildByName("suboutfits")) != null) {
              int m = element2.getIntAttribute("packid", k);
              int i1 = m;
              int n = k;
              XmlReader.Element element = element1;
              ae ae1 = this;
              HashMap<Object, Object> hashMap2 = new HashMap<>();
              if ((element = element.getChildByName("images")) != null) {
                ArrayList<af> arrayList1 = new ArrayList();
                Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("texture").iterator();
                while (arrayIterator1.hasNext()) {
                  String str1;
                  int i4 = a(str1 = ((XmlReader.Element)arrayIterator1.next()).getAttribute("file").replace('\\', '/'));
                  int i5 = n;
                  String str2 = str1;
                  Matcher matcher;
                  if ((matcher = i.matcher(str1)).matches()) {
                    i5 = Integer.parseInt(matcher.group(1));
                    str2 = matcher.group(2);
                  } 
                  FileHandle fileHandle3;
                  if ((fileHandle3 = ae1.b(i5, str2)) == null && !matcher.matches() && i1 != i5)
                    fileHandle3 = ae1.b(i1, str2); 
                  if (fileHandle3 == null)
                    throw new GdxRuntimeException("Texture nencontrada: tentou pack " + i5 + ((i1 != i5) ? (" e pack " + i1) : "") + " para \"" + str2 + "\" base=" + ae1.l); 
                  String str3 = fileHandle3.file().getAbsolutePath().replace('\\', '/');
                  int i6 = a(fileHandle3.name());
                  int i3 = i6;
                  int i2;
                  if ((i2 = i4) <= 0)
                    i2 = 1; 
                  if (i3 <= 0)
                    i3 = 1; 
                  float f = i3 / i2;
                  if (!ae1.h.isLoaded(str3, Texture.class)) {
                    TextureLoader.TextureParameter textureParameter;
                    (textureParameter = new TextureLoader.TextureParameter()).minFilter = Texture.TextureFilter.Nearest;
                    textureParameter.magFilter = Texture.TextureFilter.Nearest;
                    textureParameter.genMipMaps = false;
                    ae1.h.load(str3, Texture.class, (AssetLoaderParameters)textureParameter);
                  } 
                  af af;
                  (af = new af(ae1)).e = str3;
                  af.a = f;
                  arrayList1.add(af);
                } 
                ae1.h.finishLoading();
                byte b2 = 0;
                Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element.getChildrenByName("texture").iterator();
                while (arrayIterator2.hasNext()) {
                  XmlReader.Element element3 = arrayIterator2.next();
                  af af = arrayList1.get(b2++);
                  Texture texture;
                  (texture = (Texture)ae1.h.get(af.e, Texture.class)).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
                  texture.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
                  float f = af.a;
                  Array.ArrayIterator<XmlReader.Element> arrayIterator3 = element3.getChildrenByName("t").iterator();
                  while (arrayIterator3.hasNext()) {
                    XmlReader.Element element4;
                    int i5 = (element4 = arrayIterator3.next()).getIntAttribute("id");
                    String[] arrayOfString3 = element4.getAttribute("s").split(",");
                    String[] arrayOfString2 = element4.getAttribute("p").split(",");
                    int i6 = Integer.parseInt(arrayOfString3[0]);
                    int i2 = Integer.parseInt(arrayOfString3[1]);
                    n = Integer.parseInt(arrayOfString2[0]);
                    i1 = Integer.parseInt(arrayOfString2[1]);
                    n = Math.round(n * f);
                    i1 = Math.round(i1 * f);
                    int i4 = Math.round(i6 * f);
                    i2 = Math.round(i2 * f);
                    TextureRegion textureRegion = new TextureRegion(texture, n, i1, i4, i2);
                    String[] arrayOfString1;
                    i1 = Integer.parseInt((arrayOfString1 = element4.getAttribute("o", "0,0").split(","))[0]);
                    int i3 = Integer.parseInt(arrayOfString1[1]);
                    i1 = Math.round(i1 * f);
                    i3 = Math.round(i3 * f);
                    hashMap2.put(Integer.valueOf(i5), new ag(textureRegion, i1, i3));
                  } 
                } 
              } 
              HashMap<Object, Object> hashMap1 = hashMap2;
              Array.ArrayIterator<XmlReader.Element> arrayIterator = element2.getChildrenByName("x").iterator();
              while (arrayIterator.hasNext()) {
                n = (element = arrayIterator.next()).getIntAttribute("si");
                XmlReader.Element element3 = element.getChildByName("light");
                int i2 = 0;
                Color color = null;
                if (element3 != null) {
                  i2 = element3.getIntAttribute("s", 0);
                  String[] arrayOfString = element3.getAttribute("c").split(",");
                  color = new Color(Integer.parseInt(arrayOfString[0]) / 255.0F, Integer.parseInt(arrayOfString[1]) / 255.0F, Integer.parseInt(arrayOfString[2]) / 255.0F, Integer.parseInt(arrayOfString[3]) / 255.0F);
                } 
                Array array1 = new Array();
                Array array2 = new Array();
                Array array3 = new Array();
                Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("a").iterator();
                while (arrayIterator1.hasNext()) {
                  Array.ArrayIterator<XmlReader.Element> arrayIterator2 = ((XmlReader.Element)arrayIterator1.next()).getChildrenByName("f").iterator();
                  while (arrayIterator2.hasNext()) {
                    XmlReader.Element element4;
                    int i3 = (element4 = arrayIterator2.next()).getIntAttribute("id");
                    ag ag;
                    if ((ag = (ag)hashMap1.get(Integer.valueOf(i3))) != null) {
                      array1.add(ag.q);
                      array2.add(new Vector2(ag.I, ag.J));
                      String str1 = (str1 = element4.getAttribute("p", "150")).contains(",") ? str1.split(",")[0] : (str1.contains("-") ? str1.split("-")[0] : str1);
                      array3.add(Float.valueOf(Integer.parseInt(str1) / 1000.0F));
                    } 
                  } 
                } 
                if (array1.size != 0) {
                  TextureRegion[] arrayOfTextureRegion = (TextureRegion[])array1.toArray(TextureRegion.class);
                  float[] arrayOfFloat = new float[array3.size];
                  for (byte b2 = 0; b2 < array3.size; b2++)
                    arrayOfFloat[b2] = ((Float)array3.get(b2)).floatValue(); 
                  int[] arrayOfInt1 = new int[array2.size];
                  int[] arrayOfInt2 = new int[array2.size];
                  for (byte b3 = 0; b3 < array2.size; b3++) {
                    arrayOfInt1[b3] = (int)((Vector2)array2.get(b3)).x;
                    arrayOfInt2[b3] = (int)((Vector2)array2.get(b3)).y;
                  } 
                  Integer integer;
                  if ((integer = (Integer)this.n.get(Integer.valueOf(n))) == null || k >= integer.intValue()) {
                    this.m.put(Integer.valueOf(n), new ad(n, arrayOfTextureRegion, arrayOfFloat, arrayOfInt1, arrayOfInt2, i2, color));
                    this.n.put(Integer.valueOf(n), Integer.valueOf(k));
                  } 
                } 
              } 
            } 
          } catch (Exception exception) {
            Gdx.app.error("SubOutfitLoader", "Erro ao parsear " + fileHandle2.path(), exception);
          }  
      } 
    } 
  }
  
  private FileHandle b(int paramInt, String paramString) {
    String str1 = this.l + "/pack" + this.l + "/";
    paramString = paramString.replace('\\', '/');
    FileHandle fileHandle;
    if ((fileHandle = Gdx.files.absolute(str1 + str1)).exists())
      return fileHandle; 
    int i = a(paramString);
    int[] arrayOfInt1 = { 4, 2, 1 };
    String str2 = ".png";
    int j = paramString.lastIndexOf('.');
    int k = paramString.lastIndexOf('.', j - 1);
    paramString = (j > 0 && k >= 0) ? paramString.substring(0, k) : (((j = paramString.lastIndexOf('.')) > 0) ? paramString.substring(0, j) : paramString);
    int[] arrayOfInt2;
    (arrayOfInt2 = arrayOfInt1).length;
    for (byte b = 0; b < 3; b++) {
      FileHandle fileHandle1;
      if ((k = arrayOfInt2[b]) != i && (fileHandle1 = Gdx.files.absolute(str1 + str1 + "." + paramString + k)).exists())
        return fileHandle1; 
    } 
    return null;
  }
  
  public final ad a(int paramInt) {
    return (ad)this.m.get(Integer.valueOf(paramInt));
  }
  
  private static int a(FileHandle paramFileHandle) {
    try {
      return Integer.parseInt(paramFileHandle.name().replace("pack", ""));
    } catch (Exception exception) {
      return 0;
    } 
  }
  
  private static int a(String paramString) {
    int i;
    int j;
    if ((i = paramString.lastIndexOf('.')) > 1 && (j = paramString.lastIndexOf('.', i - 1)) >= 0) {
      String str = paramString.substring(j + 1, i);
      if ("1".equals(str) || "2".equals(str) || "4".equals(str))
        return Integer.parseInt(str); 
    } 
    return paramString.endsWith(".1.png") ? 1 : (paramString.endsWith(".2.png") ? 2 : (paramString.endsWith(".4.png") ? 4 : 1));
  }
}
