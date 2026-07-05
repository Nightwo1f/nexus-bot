package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.Preferences;
import java.util.EnumMap;
import java.util.Map;

public final class cu {
  private static final Map w = new EnumMap<>(ct.class);
  
  private static Preferences a;
  
  public static void ai() {
    if (a != null)
      return; 
    a = Gdx.app.getPreferences("jtme_keybinds");
    ct[] arrayOfCt;
    int i = (arrayOfCt = ct.values()).length;
    for (byte b = 0; b < i; b++) {
      ct ct = arrayOfCt[b];
      int j = a.getInteger(ct.name(), ct.cc);
      w.put(ct, Integer.valueOf(j));
    } 
  }
  
  private static void aj() {
    if (a == null)
      ai(); 
  }
  
  public static void a(ct paramct, int paramInt) {
    aj();
    w.put(paramct, Integer.valueOf(paramInt));
    a.putInteger(paramct.name(), paramInt);
    a.flush();
  }
  
  private static int a(ct paramct) {
    aj();
    return ((Integer)w.getOrDefault(paramct, Integer.valueOf(paramct.cc))).intValue();
  }
  
  public static String a(ct paramct) {
    return Input.Keys.toString(a(paramct));
  }
  
  public static boolean a(ct paramct) {
    aj();
    return Gdx.input.isKeyJustPressed(a(paramct));
  }
  
  public static void ak() {
    aj();
    ct[] arrayOfCt;
    int i = (arrayOfCt = ct.values()).length;
    for (byte b = 0; b < i; b++)
      a(arrayOfCt[b], (arrayOfCt[b]).cc); 
  }
}
