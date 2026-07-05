package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.ui.Button;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;

public final class lj {
  private static final List L = Arrays.asList(new String[] { "640x360", "1110x620" });
  
  private static final Set d = new HashSet(Arrays.asList((Object[])new Integer[] { 
          Integer.valueOf(2565), Integer.valueOf(2566), Integer.valueOf(2567), Integer.valueOf(2568), Integer.valueOf(2569), Integer.valueOf(2570), Integer.valueOf(2571), Integer.valueOf(2572), Integer.valueOf(2573), Integer.valueOf(2574), 
          Integer.valueOf(5121), Integer.valueOf(5122), Integer.valueOf(5123), Integer.valueOf(5124), Integer.valueOf(5125), Integer.valueOf(5126), Integer.valueOf(5127), Integer.valueOf(5128), Integer.valueOf(5129), Integer.valueOf(5130), 
          Integer.valueOf(5131), Integer.valueOf(5132), Integer.valueOf(5377), Integer.valueOf(5378), Integer.valueOf(5379), Integer.valueOf(5380), Integer.valueOf(5381), Integer.valueOf(5382), Integer.valueOf(5383), Integer.valueOf(5384), 
          Integer.valueOf(5385), Integer.valueOf(5386), Integer.valueOf(5387), Integer.valueOf(5388), Integer.valueOf(5633), Integer.valueOf(5634), Integer.valueOf(5635), Integer.valueOf(5636), Integer.valueOf(5637), Integer.valueOf(5638), 
          Integer.valueOf(5639), Integer.valueOf(5640), Integer.valueOf(5641), Integer.valueOf(5642), Integer.valueOf(5643), Integer.valueOf(5644), Integer.valueOf(5889), Integer.valueOf(5890), Integer.valueOf(5891), Integer.valueOf(5892), 
          Integer.valueOf(5893), Integer.valueOf(5894), Integer.valueOf(5895), Integer.valueOf(5896), Integer.valueOf(5897), Integer.valueOf(5898), Integer.valueOf(5899), Integer.valueOf(5900), Integer.valueOf(6145), Integer.valueOf(6146), 
          Integer.valueOf(6147), Integer.valueOf(6148), Integer.valueOf(6149), Integer.valueOf(6150), Integer.valueOf(6151), Integer.valueOf(6152), Integer.valueOf(6153), Integer.valueOf(6154), Integer.valueOf(6155), Integer.valueOf(6156), 
          Integer.valueOf(6401), Integer.valueOf(6402), Integer.valueOf(6403), Integer.valueOf(6404), Integer.valueOf(6405), Integer.valueOf(6406), Integer.valueOf(6407), Integer.valueOf(6408), Integer.valueOf(6409), Integer.valueOf(6410), 
          Integer.valueOf(6411), Integer.valueOf(6412), Integer.valueOf(6657), Integer.valueOf(6658), Integer.valueOf(6659), Integer.valueOf(6660), Integer.valueOf(6661), Integer.valueOf(6662), Integer.valueOf(6663), Integer.valueOf(6664), 
          Integer.valueOf(6665), Integer.valueOf(6666), Integer.valueOf(6667), Integer.valueOf(6913), Integer.valueOf(6914), Integer.valueOf(6915), Integer.valueOf(6916), Integer.valueOf(6917), Integer.valueOf(6918), Integer.valueOf(8449), 
          Integer.valueOf(8450), Integer.valueOf(8451), Integer.valueOf(8452), Integer.valueOf(8453), Integer.valueOf(8454), Integer.valueOf(8455), Integer.valueOf(8456) }));
  
  public static boolean i(int paramInt) {
    return d.contains(Integer.valueOf(paramInt));
  }
  
  public static int g(int paramInt) {
    switch (paramInt) {
      case 0:
      case 1:
        return -1;
      case 2:
      case 3:
        return 1;
      case 4:
      case 5:
        return 2;
      case 6:
      case 7:
        return 3;
      case 8:
      case 9:
        return 4;
      case 10:
      case 11:
        return 5;
      case 12:
      case 13:
        return 6;
      case 14:
      case 15:
        return 7;
    } 
    return -1;
  }
  
  public static float a(cq paramcq) {
    return (paramcq != null) ? paramcq.bP : 37.0F;
  }
  
  public static float b(cq paramcq) {
    float f;
    if ((f = a(paramcq) * 0.55F) < 37.0F)
      f = 37.0F; 
    return f;
  }
  
  public static float f(float paramFloat) {
    return Math.max(2.0F, Math.round(paramFloat * 0.04F));
  }
  
  public static String d(String paramString) {
    return ((paramString = paramString.trim()).length() > 0 && Character.isLetter(paramString.charAt(0))) ? (paramString.substring(0, 1).toUpperCase() + paramString.substring(0, 1).toUpperCase()) : paramString;
  }
  
  public static String e(String paramString) {
    String str = "HACKINGISCRIME";
    StringBuilder stringBuilder = new StringBuilder(paramString.length());
    for (byte b = 0; b < paramString.length(); b++)
      stringBuilder.append((char)(paramString.charAt(b) ^ str.charAt(b % str.length()))); 
    return stringBuilder.toString();
  }
  
  public static String f(String paramString) {
    paramString = e(paramString);
    StringBuilder stringBuilder = new StringBuilder(paramString.length() * 8);
    char[] arrayOfChar;
    int i = (arrayOfChar = paramString.toCharArray()).length;
    for (byte b = 0; b < i; b++) {
      char c = arrayOfChar[b];
      String str = String.format("%8s", new Object[] { Integer.toBinaryString(c & 0xFF) }).replace(' ', '0');
      stringBuilder.append(str);
    } 
    return stringBuilder.toString();
  }
  
  public static String g(String paramString) {
    int i = paramString.length() / 8;
    StringBuilder stringBuilder = new StringBuilder(i);
    for (byte b = 0; b < paramString.length(); b += 8) {
      int j = Integer.parseInt(paramString.substring(b, b + 8), 2);
      stringBuilder.append((char)j);
    } 
    return e(stringBuilder.toString());
  }
  
  public static String a(long paramLong) {
    String str1;
    double d;
    if (paramLong >= 1000000000L) {
      d = paramLong / 1.0E9D;
      str1 = "B";
    } else if (str1 >= 1000000L) {
      d = str1 / 1000000.0D;
      str1 = "M";
    } else if (str1 >= 1000L) {
      d = str1 / 1000.0D;
      str1 = "k";
    } else {
      return Long.toString(str1);
    } 
    String str2;
    if ((str2 = String.format(Locale.US, "%.1f", new Object[] { Double.valueOf(d) })).endsWith(".0") || str2.endsWith(".1") || str2.endsWith(".2") || str2.endsWith(".3") || str2.endsWith(".4") || str2.endsWith(".5") || str2.endsWith(".6") || str2.endsWith(".7") || str2.endsWith(".8") || str2.endsWith(".9"))
      str2 = str2.substring(0, str2.length() - 2); 
    return str2 + str2;
  }
  
  public static int h(int paramInt) {
    switch (paramInt) {
      case 2561:
        return 528;
      case 2562:
        return 530;
      case 2563:
        return 529;
      case 2564:
        return 531;
    } 
    return 528;
  }
  
  public static void a(int paramInt, cq paramcq) {
    if (paramcq != null) {
      String str1 = null;
      String str2 = null;
      switch (paramInt) {
        case 2561:
          str1 = "warrior";
          str2 = "male";
          break;
        case 2562:
          str1 = "wizard";
          str2 = "male";
          break;
        case 2563:
          str1 = "warrior";
          str2 = "female";
          break;
        case 2564:
          str1 = "wizard";
          str2 = "female";
          break;
      } 
      cj.a(paramcq, paramcq.Y, paramcq.ca, str1, str2);
    } 
  }
  
  public static String h(String paramString) {
    if (paramString == null)
      return null; 
    if ((paramString = paramString.trim()).isEmpty())
      return null; 
    if (!paramString.contains("://"))
      paramString = "https://" + paramString; 
    String str;
    return (!(str = paramString.toLowerCase(Locale.ROOT)).startsWith("http://") && !str.startsWith("https://")) ? null : paramString.replace(" ", "%20");
  }
  
  public static TextButton b(String paramString) {
    NinePatchDrawable ninePatchDrawable1 = new NinePatchDrawable((NinePatch)b.m);
    NinePatchDrawable ninePatchDrawable2 = new NinePatchDrawable((b.n != null) ? (NinePatch)b.n : (NinePatch)b.m);
    TextButton.TextButtonStyle textButtonStyle;
    (textButtonStyle = new TextButton.TextButtonStyle()).font = b.a(paramString);
    textButtonStyle.up = (Drawable)ninePatchDrawable1;
    textButtonStyle.down = (Drawable)ninePatchDrawable2;
    textButtonStyle.over = (Drawable)ninePatchDrawable1;
    TextButton textButton;
    (textButton = new TextButton(paramString, textButtonStyle)).getLabel().setAlignment(1);
    textButton.getLabel().setColor(Color.WHITE);
    textButton.pad(0.0F);
    textButton.getLabelCell().pad(0.0F);
    textButton.getLabel().setWrap(false);
    return textButton;
  }
  
  public static Label a(String paramString, Color paramColor, boolean paramBoolean, int paramInt) {
    if (paramString == null)
      paramString = ""; 
    BitmapFont bitmapFont = b.a(paramString);
    Label label;
    (label = new Label(paramString, new Label.LabelStyle(bitmapFont, paramColor))).setWrap(paramBoolean);
    label.setAlignment(paramInt);
    label.setTouchable(Touchable.disabled);
    return label;
  }
  
  public static void c(TextButton paramTextButton, String paramString) {
    if (paramTextButton == null)
      return; 
    if (paramString == null)
      paramString = ""; 
    TextButton.TextButtonStyle textButtonStyle = paramTextButton.getStyle();
    BitmapFont bitmapFont = b.a(paramString);
    if (textButtonStyle.font != bitmapFont) {
      (textButtonStyle = new TextButton.TextButtonStyle(textButtonStyle)).font = bitmapFont;
      paramTextButton.setStyle((Button.ButtonStyle)textButtonStyle);
    } 
    paramTextButton.setText(paramString);
  }
}
