package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.files.FileHandle;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class a {
  private static Map a;
  
  private static String a;
  
  private static Map b;
  
  private static String b;
  
  private static String a(String paramString) {
    return (paramString == null) ? "" : paramString.replace('\\', '/');
  }
  
  private static boolean a(String paramString) {
    FileHandle fileHandle;
    return (paramString == null || paramString.isEmpty()) ? false : (((fileHandle = Gdx.files.absolute(paramString)).exists() && fileHandle.isDirectory()));
  }
  
  private static FileHandle a(String paramString1, int paramInt, String paramString2) {
    FileHandle fileHandle;
    if (!(fileHandle = Gdx.files.absolute(paramString1).child("pack" + paramInt)).exists())
      return null; 
    for (String paramString2 : a(paramString2)) {
      FileHandle fileHandle1;
      if ((fileHandle1 = fileHandle.child(paramString2)).exists())
        return fileHandle1; 
    } 
    return null;
  }
  
  private static FileHandle a(String paramString1, String paramString2) {
    if (b == null || !Objects.equals(b, paramString1)) {
      b = (String)new HashMap<>();
      b = paramString1;
      if (a(paramString1)) {
        FileHandle[] arrayOfFileHandle;
        int i = (arrayOfFileHandle = Gdx.files.absolute(paramString1).list()).length;
        for (byte b = 0; b < i; b++) {
          FileHandle fileHandle;
          if ((fileHandle = arrayOfFileHandle[b]).isDirectory() && fileHandle.name().startsWith("pack")) {
            FileHandle[] arrayOfFileHandle1;
            int j = (arrayOfFileHandle1 = fileHandle.list()).length;
            for (byte b1 = 0; b1 < j; b1++) {
              FileHandle fileHandle1;
              if (!(fileHandle1 = arrayOfFileHandle1[b1]).isDirectory() && "png".equalsIgnoreCase(fileHandle1.extension())) {
                String str = fileHandle1.name().toLowerCase(Locale.ROOT);
                ((List<FileHandle>)b.computeIfAbsent(str, paramString -> new ArrayList())).add(fileHandle1);
              } 
            } 
          } 
        } 
      } 
    } 
    List<FileHandle> list;
    return ((list = (List)b.get(paramString2.toLowerCase(Locale.ROOT))) != null && !list.isEmpty()) ? list.get(0) : null;
  }
  
  private static FileHandle a(int paramInt, String paramString) {
    String str = "pack" + paramInt + "/";
    for (String str1 : a(paramString)) {
      FileHandle fileHandle;
      if ((fileHandle = Gdx.files.internal(str + str)).exists())
        return fileHandle; 
    } 
    return null;
  }
  
  private static FileHandle a(String paramString) {
    String str = "assets.txt";
    a = (String)new HashMap<>();
    a = str;
    FileHandle fileHandle2;
    if ((a == null || !Objects.equals(a, str)) && (fileHandle2 = Gdx.files.internal("assets.txt")).exists())
      try {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(fileHandle2.read(), StandardCharsets.UTF_8));
        try {
          String str1;
          while ((str1 = bufferedReader.readLine()) != null) {
            if (!(str1 = a(str1).trim()).isEmpty() && str1.endsWith(".png") && str1.startsWith("pack")) {
              String str2 = str1.substring(str1.lastIndexOf('/') + 1).toLowerCase(Locale.ROOT);
              ((List<String>)a.computeIfAbsent(str2, paramString -> new ArrayList())).add(str1);
            } 
          } 
          bufferedReader.close();
        } catch (Throwable throwable) {
          try {
            bufferedReader.close();
          } catch (Throwable throwable1) {
            throwable.addSuppressed(throwable1);
          } 
          throw throwable;
        } 
      } catch (Exception exception) {} 
    FileHandle fileHandle1;
    List<String> list;
    return ((list = (List)a.get(paramString.toLowerCase(Locale.ROOT))) != null && !list.isEmpty() && (fileHandle1 = Gdx.files.internal(list.get(0))).exists()) ? fileHandle1 : null;
  }
  
  private static List a(String paramString) {
    paramString = a(paramString);
    ArrayList<String> arrayList;
    (arrayList = new ArrayList<>()).add(paramString);
    if (paramString.endsWith(".png")) {
      paramString = paramString.substring(0, paramString.length() - 4);
      arrayList.add(paramString + ".png");
      paramString = paramString.replaceFirst("\\.\\d+$", "");
      arrayList.add(paramString + ".4.png");
      arrayList.add(paramString + ".2.png");
      arrayList.add(paramString + ".1.png");
    } 
    return arrayList;
  }
  
  public static FileHandle a(String paramString1, String paramString2, int paramInt) {
    FileHandle fileHandle1;
    FileHandle fileHandle2;
    String str1;
    String str2;
    if (((str2 = paramString2 = a(paramString2)) != null && (str2.matches("^[A-Za-z]:[\\\\/].*") || str2.startsWith("/")))) {
      FileHandle fileHandle5;
      if ((fileHandle5 = Gdx.files.absolute(paramString2)).exists())
        return fileHandle5; 
      FileHandle fileHandle6 = fileHandle5.parent();
      for (String str : a(fileHandle5.name())) {
        if ((fileHandle2 = fileHandle6.child(str)).exists())
          return fileHandle2; 
      } 
      return null;
    } 
    Matcher matcher;
    if ((matcher = Pattern.compile("^pack(\\d+)/(.*)$").matcher((CharSequence)fileHandle2)).find()) {
      int i = Integer.parseInt(matcher.group(1));
      String str = matcher.group(2);
      if (a(paramString1)) {
        FileHandle fileHandle6;
        if ((fileHandle6 = a(paramString1, i, str)) != null)
          return fileHandle6; 
        str1 = str.substring(str.lastIndexOf('/') + 1);
        FileHandle fileHandle5;
        if ((fileHandle5 = a(paramString1, str1)) != null)
          return fileHandle5; 
      } 
      FileHandle fileHandle;
      return ((fileHandle = a(i, str)) != null) ? fileHandle : (((fileHandle1 = a(str.substring(str.lastIndexOf('/') + 1))) != null) ? fileHandle1 : null);
    } 
    if (a((String)fileHandle1)) {
      FileHandle fileHandle5;
      if ((fileHandle5 = a((String)fileHandle1, paramInt, str1)) != null)
        return fileHandle5; 
      String str = str1.substring(str1.lastIndexOf('/') + 1);
      FileHandle fileHandle6;
      if ((fileHandle6 = a((String)fileHandle1, str)) != null)
        return fileHandle6; 
    } 
    FileHandle fileHandle3;
    FileHandle fileHandle4;
    return ((fileHandle3 = a(paramInt, str1)) != null) ? fileHandle3 : (((fileHandle4 = a(str1.substring(str1.lastIndexOf('/') + 1))) != null) ? fileHandle4 : null);
  }
}
