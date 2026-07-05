package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Preferences;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.XmlReader;
import com.badlogic.gdx.utils.XmlWriter;
import java.io.IOException;
import java.io.StringWriter;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

public final class cj {
  public static String a() {
    return a().getString("last_news_text", "");
  }
  
  public static void d(int paramInt, String paramString) {
    Preferences preferences;
    (preferences = Gdx.app.getPreferences("JTME_SETTINGS_CACHE")).putInteger("last_news_id", paramInt);
    preferences.putString("last_news_text", (paramString != null) ? paramString : "");
    preferences.flush();
  }
  
  public static void d(cq paramcq) {
    try {
      String str1;
      if ((str1 = b()) == null || str1.trim().isEmpty()) {
        String str;
        if ((str = c()) != null && !str.isEmpty()) {
          l(str);
          str1 = str;
        } else {
          g(paramcq);
          str1 = b();
        } 
      } 
      if (str1 == null || str1.trim().isEmpty()) {
        e(paramcq);
        return;
      } 
      XmlReader.Element element1;
      if ((element1 = (new XmlReader()).parse(str1)) == null) {
        e(paramcq);
        return;
      } 
      int j = element1.getInt("lastMessageOfTheDayNumber", paramcq.bL);
      int k = j;
      cq cq3;
      (cq3 = paramcq).bL = k;
      g(cq3);
      String str3 = element1.get("language", paramcq.S);
      paramcq.o(str3);
      boolean bool2 = Boolean.parseBoolean(element1.get("circleBarsEnabled", Boolean.toString(paramcq.V)));
      paramcq.V = bool2;
      bool2 = Boolean.parseBoolean(element1.get("enableLights", Boolean.toString(paramcq.L)));
      paramcq.e(bool2);
      bool2 = Boolean.parseBoolean(element1.get("questIndicatorEnabled", Boolean.toString(paramcq.W)));
      paramcq.W = bool2;
      bool2 = Boolean.parseBoolean(element1.get("showCreatureLevels", Boolean.toString(paramcq.X)));
      paramcq.X = bool2;
      bool2 = Boolean.parseBoolean(element1.get("analogIndicatorEnabled", Boolean.toString(paramcq.M)));
      paramcq.c(bool2);
      bool2 = Boolean.parseBoolean(element1.get("clickWalkEnabled", Boolean.toString(paramcq.Y)));
      paramcq.d(bool2);
      float f2 = element1.getFloat("hudArcSpacing", paramcq.ad);
      paramcq.e(f2);
      String str2;
      if ((str2 = element1.get("imei", "")).isEmpty() || str2.equals("521536412252573")) {
        StringBuilder stringBuilder = new StringBuilder();
        for (byte b = 0; b < 15; b++)
          stringBuilder.append(MathUtils.random(0, 9)); 
        str2 = stringBuilder.toString();
      } 
      String str4 = str2;
      cq cq2;
      (cq2 = paramcq).U = str4;
      g(cq2);
      String[] arrayOfString;
      if ((arrayOfString = element1.get("gameResolution", "" + paramcq.a + "x" + paramcq.a).split("x")).length == 2)
        try {
          int m = Integer.parseInt(arrayOfString[0].trim());
          int n = Integer.parseInt(arrayOfString[1].trim());
          paramcq.L(m);
          paramcq.M(n);
        } catch (NumberFormatException numberFormatException) {} 
      float f1 = element1.getFloat("sound", paramcq.af);
      float f3 = element1.getFloat("soundSfx", f1);
      float f4 = element1.getFloat("soundMusic", f1);
      paramcq.af = MathUtils.clamp(f1, 0.0F, 1.0F);
      paramcq.f(f3);
      paramcq.g(f4);
      element1.getInt("res", paramcq.bP);
      paramcq.bP = 64;
      int i = element1.getInt("zoomMode", paramcq.bX);
      paramcq.bX = i;
      paramcq.af();
      i = element1.getInt("targetFpsIndex", paramcq.bI);
      paramcq.K(i);
      boolean bool1 = Boolean.parseBoolean(element1.get("hasCustomUi", "false"));
      paramcq.K = bool1;
      if (bool1) {
        String[] arrayOfString1 = element1.get("customUiPosX", "").split(",");
        String[] arrayOfString2 = element1.get("customUiPosY", "").split(",");
        float[] arrayOfFloat1 = new float[7];
        float[] arrayOfFloat2 = new float[7];
        byte b;
        for (b = 0; b < 7 && b < arrayOfString1.length; b++) {
          try {
            arrayOfFloat1[b] = Float.parseFloat(arrayOfString1[b]);
          } catch (Exception exception) {}
        } 
        for (b = 0; b < 7 && b < arrayOfString2.length; b++) {
          try {
            arrayOfFloat2[b] = Float.parseFloat(arrayOfString2[b]);
          } catch (Exception exception) {}
        } 
        paramcq.j = arrayOfFloat1;
        paramcq.k = arrayOfFloat2;
      } 
      cq cq1;
      (cq1 = paramcq).n.clear();
      g(cq1);
      XmlReader.Element element2;
      if ((element2 = element1.getChildByName("savedCharacters")) != null) {
        Array.ArrayIterator<XmlReader.Element> arrayIterator = element2.getChildrenByName("character").iterator();
        while (arrayIterator.hasNext()) {
          XmlReader.Element element = arrayIterator.next();
          ck ck = new ck(element.getAttribute("version", ""), element.getAttribute("name", ""), element.getAttribute("password", ""), element.getIntAttribute("worldNr", 0), element.getIntAttribute("levelNr", 0), element.getAttribute("lastLogin", ""), element.getAttribute("vocation", ""), element.getAttribute("gender", ""), element.getAttribute("savePassword", ""), element.getIntAttribute("lookType", 0), element.getIntAttribute("subOutfit", 0), element.getIntAttribute("hair", 0), element.getIntAttribute("skin", 0), element.getIntAttribute("body", 0), element.getIntAttribute("misc", 0), element.getIntAttribute("hairColor", 0), element.getIntAttribute("skinColor", 0), element.getIntAttribute("bodyColorOne", 0), element.getIntAttribute("bodyColorTwo", 0), element.getIntAttribute("miscColor", 0));
          paramcq.a(ck);
        } 
      } 
      Gdx.app.log("ConfigManager", "Settings carregadas com sucesso.");
      return;
    } catch (Exception exception) {
      Gdx.app.error("ConfigManager", "Arquivo de config corrompido ou antigo detectado. Resetando para o padr, exception);
      e(paramcq);
      return;
    } 
  }
  
  private static void e(cq paramcq) {
    Preferences preferences;
    (preferences = a()).remove("settings_xml");
    preferences.flush();
    g(paramcq);
    Gdx.app.log("ConfigManager", "Configuraresetada com sucesso.");
  }
  
  public static void f(cq paramcq) {
    g(paramcq);
  }
  
  private static void g(cq paramcq) {
    StringWriter stringWriter = new StringWriter();
    XmlWriter xmlWriter = new XmlWriter(stringWriter);
    try {
      stringWriter.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n");
      xmlWriter.element("settings").attribute("version", "1.6");
      xmlWriter.element("lastMessageOfTheDayNumber").text(Integer.toString(paramcq.bL)).pop();
      xmlWriter.element("language").text(paramcq.S).pop();
      xmlWriter.element("circleBarsEnabled").text(Boolean.toString(paramcq.V)).pop();
      xmlWriter.element("enableLights").text(Boolean.toString(paramcq.L)).pop();
      xmlWriter.element("questIndicatorEnabled").text(Boolean.toString(paramcq.W)).pop();
      xmlWriter.element("showCreatureLevels").text(Boolean.toString(paramcq.X)).pop();
      xmlWriter.element("analogIndicatorEnabled").text(Boolean.toString(paramcq.M)).pop();
      xmlWriter.element("clickWalkEnabled").text(Boolean.toString(paramcq.Y)).pop();
      xmlWriter.element("gameResolution").text("" + paramcq.a + "x" + paramcq.a).pop();
      xmlWriter.element("hudArcSpacing").text(Float.toString(paramcq.ad)).pop();
      xmlWriter.element("imei").text((paramcq.U != null) ? paramcq.U : "").pop();
      xmlWriter.element("sound").text(Float.toString(paramcq.af)).pop();
      xmlWriter.element("soundSfx").text(Float.toString(paramcq.ag)).pop();
      xmlWriter.element("soundMusic").text(Float.toString(paramcq.ah)).pop();
      xmlWriter.element("res").text(Integer.toString(paramcq.bP)).pop();
      xmlWriter.element("zoomMode").text(Integer.toString(paramcq.bX)).pop();
      xmlWriter.element("targetFpsIndex").text(Integer.toString(paramcq.bI)).pop();
      xmlWriter.element("hasCustomUi").text(Boolean.toString(paramcq.K)).pop();
      if (paramcq.K) {
        StringBuilder stringBuilder1 = new StringBuilder();
        StringBuilder stringBuilder2 = new StringBuilder();
        float[] arrayOfFloat1 = paramcq.j;
        float[] arrayOfFloat2 = paramcq.k;
        for (byte b = 0; b < 7; b++) {
          stringBuilder1.append(arrayOfFloat1[b]).append((b < 6) ? "," : "");
          stringBuilder2.append(arrayOfFloat2[b]).append((b < 6) ? "," : "");
        } 
        xmlWriter.element("customUiPosX").text(stringBuilder1.toString()).pop();
        xmlWriter.element("customUiPosY").text(stringBuilder2.toString()).pop();
      } 
      xmlWriter.element("savedCharacters");
      for (ck ck : paramcq.n)
        xmlWriter.element("character").attribute("version", ck.K).attribute("name", ck.L).attribute("password", ck.M).attribute("worldNr", Integer.toString(ck.bv)).attribute("levelNr", Integer.toString(ck.bw)).attribute("lastLogin", ck.N).attribute("vocation", ck.O).attribute("gender", ck.P).attribute("savePassword", ck.Q).attribute("lookType", Integer.toString(ck.bx)).attribute("subOutfit", Integer.toString(ck.by)).attribute("hair", Integer.toString(ck.bz)).attribute("skin", Integer.toString(ck.bA)).attribute("body", Integer.toString(ck.bB)).attribute("misc", Integer.toString(ck.bC)).attribute("hairColor", Integer.toString(ck.bD)).attribute("skinColor", Integer.toString(ck.bE)).attribute("bodyColorOne", Integer.toString(ck.bF)).attribute("bodyColorTwo", Integer.toString(ck.bG)).attribute("miscColor", Integer.toString(ck.bH)).pop(); 
      xmlWriter.pop();
      xmlWriter.pop();
      xmlWriter.close();
      l(stringWriter.toString());
      return;
    } catch (IOException iOException) {
      Gdx.app.error("ConfigManager", "Erro ao criar settings (cache/arquivo)", iOException);
      return;
    } 
  }
  
  public static Preferences a() {
    return Gdx.app.getPreferences("JTME_SETTINGS_CACHE");
  }
  
  private static void l(String paramString) {
    try {
      Preferences preferences;
      (preferences = a()).putString("settings_xml", paramString);
      preferences.flush();
      return;
    } catch (Exception exception) {
      Gdx.app.error("ConfigManager", "Erro ao escrever no cache", exception);
      return;
    } 
  }
  
  private static String b() {
    String str;
    return ((str = a().getString("settings_xml", null)) == null) ? null : str;
  }
  
  private static String c() {
    try {
      FileHandle fileHandle;
      if ((fileHandle = Gdx.files.local("JTME/settings.xml")).exists())
        return fileHandle.readString("UTF-8"); 
    } catch (Exception exception) {
      Gdx.app.error("ConfigManager", "Falha ao ler arquivo legado.", exception);
    } 
    return null;
  }
  
  private static int a(cq paramcq, String paramString, int paramInt) {
    List<ck> list = paramcq.n;
    for (byte b = 0; b < list.size(); b++) {
      ck ck;
      if ((ck = list.get(b)) != null && ck.L.equalsIgnoreCase(paramString) && ck.bv == paramInt)
        return b; 
    } 
    return -1;
  }
  
  private static void a(cq paramcq, int paramInt, ck paramck) {
    List<ck> list = paramcq.n;
    if (paramInt >= 0 && paramInt < list.size()) {
      list.set(paramInt, paramck);
      return;
    } 
    list.add(paramck);
  }
  
  public static void a(cq paramcq, String paramString1, int paramInt, String paramString2, String paramString3) {
    int i = a(paramcq, paramString1, paramInt);
    String str1 = "1.6";
    String str2 = "";
    String str3 = "false";
    int j = 0;
    String str4 = "";
    String str5 = "";
    String str6 = "";
    int k = 0;
    int m = 0;
    int n = 0;
    int i1 = 0;
    int i2 = 0;
    int i3 = 0;
    int i4 = 0;
    int i5 = 0;
    int i6 = 0;
    int i7 = 0;
    int i8 = 0;
    ck ck2;
    if (i >= 0 && (ck2 = paramcq.n.get(i)) != null) {
      str1 = (ck2.K != null && !ck2.K.isEmpty()) ? ck2.K : str1;
      str2 = (ck2.M != null) ? ck2.M : "";
      str3 = (ck2.Q != null) ? ck2.Q : "false";
      j = ck2.bw;
      str4 = (ck2.O != null) ? ck2.O : "";
      str5 = (ck2.P != null) ? ck2.P : "";
      str6 = (ck2.N != null) ? ck2.N : "";
      k = ck2.bx;
      m = ck2.by;
      n = ck2.bz;
      i1 = ck2.bA;
      i2 = ck2.bB;
      i3 = ck2.bC;
      i4 = ck2.bD;
      i5 = ck2.bE;
      i6 = ck2.bF;
      i7 = ck2.bG;
      i8 = ck2.bH;
    } 
    String str7 = (paramString2 != null) ? paramString2 : str4;
    paramString2 = (paramString3 != null) ? paramString3 : str5;
    if (!str6.isEmpty()) {
      paramString3 = str6;
    } else {
      paramString3 = (new SimpleDateFormat("yyyy-MM-dd HH:mm")).format(new Date());
    } 
    ck ck1 = new ck(str1, paramString1, str2, paramInt, j, paramString3, str7, paramString2, str3, k, m, n, i1, i2, i3, i4, i5, i6, i7, i8);
    a(paramcq, i, ck1);
    g(paramcq);
  }
  
  public static void a(cq paramcq, String paramString, int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, int paramInt6, int paramInt7, int paramInt8, int paramInt9, int paramInt10, int paramInt11, int paramInt12) {
    int i;
    if ((i = a(paramcq, paramString, paramInt1)) >= 0) {
      ck ck = paramcq.n.get(i);
      ck = new ck(ck.K, ck.L, ck.M, ck.bv, ck.bw, ck.N, ck.O, ck.P, ck.Q, paramInt2, paramInt3, paramInt4, paramInt5, paramInt6, paramInt7, paramInt8, paramInt9, paramInt10, paramInt11, paramInt12);
      a(paramcq, i, ck);
      g(paramcq);
    } 
  }
}
