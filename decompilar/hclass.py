package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.assets.AssetLoaderParameters;
import com.badlogic.gdx.assets.AssetManager;
import com.badlogic.gdx.assets.loaders.TextureLoader;
import com.badlogic.gdx.files.FileHandle;
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

public final class h {
  private final AssetManager b;
  
  private final String d;
  
  private final Map d = new HashMap<>();
  
  private final Map e = new HashMap<>();
  
  private static final Pattern a = Pattern.compile("\\d+");
  
  private static final Pattern b = Pattern.compile("^(?:\\.?\\./)?pack(\\d+)/(.+)$");
  
  public h(AssetManager paramAssetManager, String paramString) {
    this.b = (Pattern)paramAssetManager;
    this.d = (Map)paramString.replace('\\', '/');
  }
  
  public final void g() {
    FileHandle fileHandle = Gdx.files.absolute((String)this.d);
    XmlReader xmlReader = new XmlReader();
    ArrayList<FileHandle> arrayList = new ArrayList();
    FileHandle[] arrayOfFileHandle;
    int i = (arrayOfFileHandle = fileHandle.list()).length;
    int j;
    for (j = 0; j < i; j++) {
      FileHandle fileHandle1;
      if ((fileHandle1 = arrayOfFileHandle[j]).isDirectory() && fileHandle1.name().startsWith("pack"))
        arrayList.add(fileHandle1); 
    } 
    arrayList.sort(Comparator.comparingInt(h::a));
    Iterator<FileHandle> iterator = arrayList.iterator();
    while (iterator.hasNext()) {
      FileHandle fileHandle1;
      j = a(fileHandle1 = iterator.next());
      FileHandle[] arrayOfFileHandle2;
      Arrays.sort(arrayOfFileHandle2 = fileHandle1.list("xml"), (paramFileHandle1, paramFileHandle2) -> {
            String str1 = paramFileHandle1.nameWithoutExtension();
            String str2 = paramFileHandle2.nameWithoutExtension();
            int i = a.matcher(str1).matches() ? Integer.parseInt(str1) : Integer.MAX_VALUE;
            int j = a.matcher(str2).matches() ? Integer.parseInt(str2) : Integer.MAX_VALUE;
            return Integer.compare(i, j);
          });
      FileHandle[] arrayOfFileHandle1;
      int k = (arrayOfFileHandle1 = arrayOfFileHandle2).length;
      for (byte b = 0; b < k; b++) {
        FileHandle fileHandle2;
        String str = (fileHandle2 = arrayOfFileHandle1[b]).nameWithoutExtension();
        if (a.matcher(str).matches())
          try {
            if (!(str = fileHandle2.readString("UTF-8")).isEmpty() && str.charAt(0) == ')
              str = str.substring(1); 
            XmlReader.Element element1;
            XmlReader.Element element2;
            if ((element2 = (element1 = xmlReader.parse(str)).getChildByName("effects")) != null) {
              int m = element2.getIntAttribute("packid", j);
              int i1 = m;
              int n = j;
              XmlReader.Element element = element1;
              h h1 = this;
              HashMap<Object, Object> hashMap2 = new HashMap<>();
              if ((element = element.getChildByName("images")) != null) {
                ArrayList<i> arrayList1 = new ArrayList();
                Array.ArrayIterator<XmlReader.Element> arrayIterator1 = element.getChildrenByName("texture").iterator();
                while (arrayIterator1.hasNext()) {
                  String str1;
                  int i2 = a(str1 = ((XmlReader.Element)arrayIterator1.next()).getAttribute("file").replace('\\', '/'));
                  int i3 = n;
                  String str2 = str1;
                  Matcher matcher;
                  if ((matcher = b.matcher(str1)).matches()) {
                    i3 = Integer.parseInt(matcher.group(1));
                    str2 = matcher.group(2);
                  } 
                  FileHandle fileHandle3;
                  if ((fileHandle3 = h1.b(i3, str2)) == null && !matcher.matches() && i1 != i3)
                    fileHandle3 = h1.b(i1, str2); 
                  if (fileHandle3 == null)
                    throw new GdxRuntimeException("Texture nencontrada: pack=" + i3 + ((i1 != i3) ? (", fallback=" + i1) : "") + " file=\"" + str2 + "\" base=" + h1.d); 
                  String str3 = fileHandle3.file().getAbsolutePath().replace('\\', '/');
                  int i4 = a(fileHandle3.name());
                  if (i2 <= 0)
                    i2 = 1; 
                  if (i4 <= 0)
                    i4 = 1; 
                  float f = i4 / i2;
                  if (!h1.b.isLoaded(str3, Texture.class)) {
                    TextureLoader.TextureParameter textureParameter;
                    (textureParameter = new TextureLoader.TextureParameter()).minFilter = Texture.TextureFilter.Nearest;
                    textureParameter.magFilter = Texture.TextureFilter.Nearest;
                    textureParameter.genMipMaps = false;
                    h1.b.load(str3, Texture.class, (AssetLoaderParameters)textureParameter);
                  } 
                  i i5;
                  (i5 = new i(h1)).e = str3;
                  i5.a = f;
                  arrayList1.add(i5);
                } 
                h1.b.finishLoading();
                byte b1 = 0;
                Array.ArrayIterator<XmlReader.Element> arrayIterator2 = element.getChildrenByName("texture").iterator();
                while (arrayIterator2.hasNext()) {
                  XmlReader.Element element3 = arrayIterator2.next();
                  i i2 = arrayList1.get(b1++);
                  Texture texture;
                  (texture = (Texture)h1.b.get(i2.e, Texture.class)).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
                  texture.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
                  float f = i2.a;
                  Array.ArrayIterator<XmlReader.Element> arrayIterator3 = element3.getChildrenByName("t").iterator();
                  while (arrayIterator3.hasNext()) {
                    XmlReader.Element element4;
                    int i5 = (element4 = arrayIterator3.next()).getIntAttribute("id");
                    String[] arrayOfString3 = element4.getAttribute("s").split(",");
                    String[] arrayOfString2 = element4.getAttribute("p").split(",");
                    int i7 = Integer.parseInt(arrayOfString3[0]);
                    int i3 = Integer.parseInt(arrayOfString3[1]);
                    n = Integer.parseInt(arrayOfString2[0]);
                    i1 = Integer.parseInt(arrayOfString2[1]);
                    Math.round(n * f);
                    Math.round(i1 * f);
                    Math.round(i7 * f);
                    Math.round(i3 * f);
                    i1 = i3;
                    n = i7;
                    i3 = i1;
                    int i6 = n;
                    Texture texture1 = texture;
                    TextureRegion textureRegion2 = new TextureRegion(texture1, i6, i3, n, i1);
                    float f4 = 1.0F / texture1.getWidth();
                    float f3 = 1.0F / texture1.getHeight();
                    float f5 = (i6 + 0.1F) * f4;
                    float f6 = (i3 + 0.1F) * f3;
                    float f2 = ((i6 + n) - 0.1F) * f4;
                    float f1 = ((i3 + i1) - 0.1F) * f3;
                    textureRegion2.setRegion(f5, f6, f2, f1);
                    TextureRegion textureRegion1 = textureRegion2;
                    String[] arrayOfString1;
                    i1 = Integer.parseInt((arrayOfString1 = element4.getAttribute("o", "0,0").split(","))[0]);
                    int i4 = Integer.parseInt(arrayOfString1[1]);
                    i1 = Math.round(i1 * f);
                    i4 = Math.round(i4 * f);
                    hashMap2.put(Integer.valueOf(i5), new j(textureRegion1, i1, i4));
                  } 
                } 
              } 
              HashMap<Object, Object> hashMap1 = hashMap2;
              Array.ArrayIterator<XmlReader.Element> arrayIterator = element2.getChildrenByName("x").iterator();
              while (arrayIterator.hasNext()) {
                n = (element = arrayIterator.next()).getIntAttribute("si");
                if ((element = element.getChildByName("a")) != null) {
                  Array array1 = element.getChildrenByName("f");
                  Array array2 = new Array();
                  Array array3 = new Array();
                  Array array4 = new Array();
                  Array.ArrayIterator<XmlReader.Element> arrayIterator1 = array1.iterator();
                  while (arrayIterator1.hasNext()) {
                    XmlReader.Element element3;
                    int i2 = (element3 = arrayIterator1.next()).getIntAttribute("id");
                    j j1;
                    if ((j1 = (j)hashMap1.get(Integer.valueOf(i2))) != null) {
                      array2.add(j1.j);
                      array3.add(new Vector2(j1.e, j1.f));
                      String str2;
                      String str1 = (str2 = element3.getAttribute("p", "150")).contains(",") ? str2.split(",")[0] : (str2.contains("-") ? str2.split("-")[0] : str2);
                      array4.add(Float.valueOf(Integer.parseInt(str1) / 1000.0F));
                    } 
                  } 
                  if (array2.size != 0) {
                    TextureRegion[] arrayOfTextureRegion = (TextureRegion[])array2.toArray(TextureRegion.class);
                    float[] arrayOfFloat = new float[array4.size];
                    for (byte b1 = 0; b1 < array4.size; b1++)
                      arrayOfFloat[b1] = ((Float)array4.get(b1)).floatValue(); 
                    int[] arrayOfInt1 = new int[array3.size];
                    int[] arrayOfInt2 = new int[array3.size];
                    for (byte b2 = 0; b2 < array3.size; b2++) {
                      arrayOfInt1[b2] = (int)((Vector2)array3.get(b2)).x;
                      arrayOfInt2[b2] = (int)((Vector2)array3.get(b2)).y;
                    } 
                    Integer integer;
                    if ((integer = (Integer)this.e.get(Integer.valueOf(n))) == null || j >= integer.intValue()) {
                      if (integer != null)
                        Gdx.app.log("EffectLoader", "Substituindo effect si=" + n + " do pack " + integer + " pelo do pack " + j + "."); 
                      this.d.put(Integer.valueOf(n), new g(n, arrayOfTextureRegion, arrayOfFloat, arrayOfInt1, arrayOfInt2));
                      this.e.put(Integer.valueOf(n), Integer.valueOf(j));
                      continue;
                    } 
                    Gdx.app.log("EffectLoader", "Ignorando effect si=" + n + " do pack " + j + " (jexiste do pack " + integer + ").");
                  } 
                } 
              } 
            } 
          } catch (Exception exception) {
            Gdx.app.error("EffectLoader", "Erro ao parsear " + fileHandle2.path(), exception);
          }  
      } 
    } 
  }
  
  private FileHandle b(int paramInt, String paramString) {
    String str1 = "" + this.d + "/pack" + this.d + "/";
    paramString = paramString.replace('\\', '/');
    FileHandle fileHandle;
    if ((fileHandle = Gdx.files.absolute(str1 + str1)).exists())
      return fileHandle; 
    int i = a(paramString);
    int[] arrayOfInt = { 4, 2, 1 };
    String str2 = ".png";
    int j = paramString.lastIndexOf('.');
    int k = paramString.lastIndexOf('.', j - 1);
    paramString = (j > 0 && k >= 0) ? paramString.substring(0, k) : ((j > 0) ? paramString.substring(0, j) : paramString);
    arrayOfInt.length;
    for (j = 0; j < 3; j++) {
      FileHandle fileHandle1;
      if ((k = arrayOfInt[j]) != i && (fileHandle1 = Gdx.files.absolute(str1 + str1 + "." + paramString + k)).exists())
        return fileHandle1; 
    } 
    return null;
  }
  
  public final g a(int paramInt) {
    return (g)this.d.get(Integer.valueOf(paramInt));
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
