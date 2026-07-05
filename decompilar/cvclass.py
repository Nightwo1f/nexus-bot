package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.scenes.scene2d.Event;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;
import com.badlogic.gdx.scenes.scene2d.Stage;

public final class cv {
  private static ct r = null;
  
  private static InputListener a = null;
  
  public static void a(cr paramcr, Stage paramStage) {
    boolean bool;
    String str1 = (b.a(bool = paramcr.f.S, "id_options") != null) ? b.a(bool, "id_options") : "Options";
    String str3 = b.a(bool, "id_help_options_default");
    String str7 = str1;
    jm jm2;
    (jm2 = in.a(paramcr.f)).w = str7;
    jm2.bq = true;
    str7 = str3;
    (jm2 = jm2).at = str7;
    jm jm1 = jm2;
    str3 = (b.a(bool, "id_cat_controls") != null) ? b.a(bool, "id_cat_controls") : "CONTROLES";
    jm1.a(10, 1, " " + str3.toUpperCase(), (Runnable)null);
    str3 = b.a(bool, "id_controls_keybinds");
    str7 = b.a(bool, "id_help_controls");
    (jm2 = jm1).au = str7;
    jm2.a(11, 0, str3, () -> {
          in.cf();
          Gdx.app.postRunnable(());
        });
    str3 = (b.a(bool, "id_cat_video") != null) ? b.a(bool, "id_cat_video") : "VE GR;
    jm1.a(20, 1, " " + str3.toUpperCase(), (Runnable)null);
    str3 = (b.a(bool, "id_show_fps") != null) ? b.a(bool, "id_show_fps") : "Show FPS";
    str7 = b.a(bool, "id_help_fps");
    (jm2 = jm1).au = str7;
    jm2.a(21, str3, paramcr.f.Q, paramBoolean -> {
          paramcr.f.f(paramBoolean.booleanValue());
          cj.f(paramcr.f);
        });
    String[] arrayOfString2 = { "V-Sync", "30 FPS", "60 FPS", "120 FPS", "Ilimitado" };
    String str6 = (b.a(bool, "id_fps_limit") != null) ? b.a(bool, "id_fps_limit") : "Limite de FPS";
    str7 = (b.a(bool, "id_help_fps_limit") != null) ? b.a(bool, "id_help_fps_limit") : "Controla o limite de quadros. Valores menores economizam bateria.";
    (jm2 = jm1).au = str7;
    jm2.a(22, str6, arrayOfString2, paramcr.f.bI, paramInteger -> {
          paramcr.f.K(paramInteger.intValue());
          paramcr.f.ag();
          cj.f(paramcr.f);
        });
    String str2 = (b.a(bool, "id_enable_lights") != null) ? b.a(bool, "id_enable_lights") : "Enable Lights";
    str7 = (b.a(bool, "id_help_enable_lights") != null) ? b.a(bool, "id_help_enable_lights") : "Ativa ou desativa a iluminadinDesligue para mais desempenho.";
    (jm2 = jm1).au = str7;
    jm2.a(23, str2, paramcr.f.L, paramBoolean -> {
          paramcr.f.e(paramBoolean.booleanValue());
          cj.f(paramcr.f);
        });
    str2 = b.a(bool, "id_view_distance");
    String[] arrayOfString3 = { b.a(bool, "id_view_near"), b.a(bool, "id_view_far"), b.a(bool, "id_view_very_far") };
    str7 = b.a(bool, "id_help_view_distance");
    (jm2 = jm1).au = str7;
    jm2.a(24, str2, arrayOfString3, paramcr.f.bX, paramInteger -> {
          int i = paramInteger.intValue();
          Stage stage = paramStage;
          cr cr1;
          (cr1 = paramcr).f.bX = i;
          if (Gdx.app.getType() == Application.ApplicationType.Desktop) {
            int j = (Gdx.graphics.getDisplayMode()).width;
            int k = (Gdx.graphics.getDisplayMode()).height;
            if (i == 0) {
              i = (int)(j * 0.55F);
              j = (int)(k * 0.55F);
            } else if (i == 1) {
              i = (int)(j * 0.75F);
              j = (int)(k * 0.75F);
            } else {
              i = (int)(j * 0.95F);
              j = (int)(k * 0.9F);
            } 
            i = Math.max(i, 800);
            j = Math.max(j, 600);
            Gdx.graphics.setWindowedMode(i, j);
            cr1.f.L(i);
            cr1.f.M(j);
          } 
          cr1.f.af();
          cj.f(cr1.f);
          if (cr1.getScreen() instanceof fj)
            ((fj)cr1.getScreen()).resize(Gdx.graphics.getWidth(), Gdx.graphics.getHeight()); 
          a(cr1, stage);
          Gdx.app.postRunnable(());
        });
    str2 = (b.a(bool, "id_cat_interface") != null) ? b.a(bool, "id_cat_interface") : "INTERFACE E HUD";
    jm1.a(30, 1, " " + str2.toUpperCase(), (Runnable)null);
    str2 = (b.a(bool, "id_click_to_walk") != null) ? b.a(bool, "id_click_to_walk") : "Click to Walk";
    String str5 = (b.a(bool, "id_help_click_to_walk") != null) ? b.a(bool, "id_help_click_to_walk") : "Enables or disables moving by tapping on the screen.";
    str7 = str5;
    (jm2 = jm1).au = str7;
    jm2.a(31, str2, paramcr.f.Y, paramBoolean -> {
          paramcr.f.d(paramBoolean.booleanValue());
          cj.f(paramcr.f);
        });
    str2 = (b.a(bool, "id_analog_indicator") != null) ? b.a(bool, "id_analog_indicator") : "Movement Indicator";
    str7 = (b.a(bool, "id_help_analog_indicator") != null) ? b.a(bool, "id_help_analog_indicator") : "Exibe um indicador visual abaixo do personagem ao se movimentar.";
    (jm2 = jm1).au = str7;
    jm2.a(32, str2, paramcr.f.M, paramBoolean -> {
          paramcr.f.c(paramBoolean.booleanValue());
          cj.f(paramcr.f);
        });
    str2 = b.a(bool, "id_circular_bars");
    str7 = b.a(bool, "id_help_circular_bars");
    (jm2 = jm1).au = str7;
    jm2.a(33, str2, paramcr.f.V, paramBoolean -> {
          paramcr.f.V = paramBoolean.booleanValue();
          cj.f(paramcr.f);
        });
    String[] arrayOfString1 = new String[21];
    for (byte b = 0; b <= 20; b++)
      arrayOfString1[b] = "" + b * 5 + "%"; 
    String str4 = (b.a(bool, "id_bar_distance") != null) ? b.a(bool, "id_bar_distance") : "Bar Distance";
    int i = MathUtils.clamp(Math.round((paramcr.f.ad - 0.5F) / 0.1F), 0, 20);
    str7 = (b.a(bool, "id_help_bar_distance") != null) ? b.a(bool, "id_help_bar_distance") : "Ajusta a distdas barras de HP e MP em relaao personagem.";
    (jm2 = jm1).au = str7;
    jm2.a(34, str4, arrayOfString1, i, paramInteger -> {
          float f = 0.5F + paramInteger.intValue() * 0.1F;
          paramcr.f.e(f);
          cj.f(paramcr.f);
        });
    str4 = b.a(bool, "id_quest_indicator");
    str7 = b.a(bool, "id_help_quest_indicator");
    (jm2 = jm1).au = str7;
    jm2.a(35, str4, paramcr.f.W, paramBoolean -> {
          paramcr.f.W = paramBoolean.booleanValue();
          cj.f(paramcr.f);
        });
    str4 = b.a(bool, "id_show_creature_levels");
    str7 = b.a(bool, "id_help_creature_levels");
    (jm2 = jm1).au = str7;
    jm2.a(36, str4, paramcr.f.X, paramBoolean -> {
          paramcr.f.X = paramBoolean.booleanValue();
          cj.f(paramcr.f);
        });
    str4 = (b.a(bool, "id_cat_audio") != null) ? b.a(bool, "id_cat_audio") : ";
    jm1.a(40, 1, " " + str4.toUpperCase(), (Runnable)null);
    str4 = b.a(bool, "id_sound_effect_volume");
    i = Math.round(paramcr.f.ag * 20.0F);
    str7 = b.a(bool, "id_help_sfx_volume");
    (jm2 = jm1).au = str7;
    jm2.a(41, str4, arrayOfString1, i, paramInteger -> {
          float f = paramInteger.intValue() * 0.05F;
          paramcr.f.f(f);
          al.a(f);
          cj.f(paramcr.f);
        });
    str4 = b.a(bool, "id_ambient_volume");
    i = Math.round(paramcr.f.ah * 20.0F);
    str7 = b.a(bool, "id_help_music_volume");
    (jm2 = jm1).au = str7;
    jm2.a(42, str4, arrayOfString1, i, paramInteger -> {
          float f = paramInteger.intValue() * 0.05F;
          paramcr.f.g(f);
          al.b(f);
          cj.f(paramcr.f);
        });
    in.a(paramStage, jm1.a());
  }
  
  public static void b(cr paramcr, Stage paramStage) {
    boolean bool;
    String str1;
    if ((str1 = b.a(bool = paramcr.f.S, "id_controls_keybinds")) == null)
      str1 = "Controls"; 
    jm jm2;
    (jm2 = in.a(paramcr.f)).w = str1;
    jm2.bq = true;
    Runnable runnable1 = () -> a(paramStage);
    (jm2 = jm2).h = runnable1;
    runnable1 = (() -> {
        a(paramStage);
        a(paramcr, paramStage);
      });
    (jm2 = jm2).g = runnable1;
    jm jm1 = jm2;
    byte b1 = 100;
    ct[] arrayOfCt;
    int i = (arrayOfCt = ct.values()).length;
    for (byte b2 = 0; b2 < i; b2++) {
      boolean bool2;
      ct ct1;
      String str4 = "id_action_" + (ct1 = arrayOfCt[b2]).name().toLowerCase();
      if ((str4 = b.a(bool, str4)) == null)
        str4 = ct1.ac; 
      boolean bool1;
      if (bool1 = (ct1 == r) ? true : false) {
        if ((str5 = b.a(bool, "id_press_key")) == null)
          str5 = "Press Key..."; 
        str5 = "[ " + str5 + " ]";
        bool2 = true;
      } else {
        str5 = "[" + cu.a(ct1) + "]";
        bool2 = false;
      } 
      Runnable runnable = () -> {
          if (paramBoolean) {
            a(paramStage);
            b(paramcr, paramStage);
            return;
          } 
          ct ct1 = paramct;
          paramStage = paramStage;
          cr cr1 = paramcr;
          a(paramStage);
          r = ct1;
          b(cr1, paramStage);
          a = new cw(paramStage, cr1, ct1);
          paramStage.addCaptureListener((EventListener)a);
        };
      String str6 = str5;
      String str5 = str4;
      bool1 = bool2;
      byte b = b1++;
      jm jm = jm1;
      jr jr = new jr(b, bool1, str5, null, str6, runnable, false);
      jm.c(jr);
      jm.B.add(jr);
    } 
    String str2;
    if ((str2 = b.a(bool, "id_reset_defaults")) == null)
      str2 = "Reset Defaults"; 
    Runnable runnable2 = () -> {
        a(paramStage);
        cu.ak();
        b(paramcr, paramStage);
      };
    String str3 = str2;
    byte b3 = b1;
    jm jm3 = jm1;
    jk jk = new jk(b3, str3, false, runnable2, false, null);
    jm3.b(jk);
    jm3.C.add(jk);
    in.a(paramStage, jm1.a());
  }
  
  static void a(Stage paramStage) {
    r = null;
    if (a != null && paramStage != null) {
      paramStage.removeCaptureListener((EventListener)a);
      a = null;
    } 
  }
  
  public static boolean a(Event paramEvent) {
    return (paramEvent instanceof InputEvent && ((InputEvent)paramEvent).getType() == InputEvent.Type.touchDown);
  }
  
  public static void a(cr paramcr, Stage paramStage, Runnable paramRunnable) {
    boolean bool;
    String str4 = b.a(bool = paramcr.f.S, "id_really_delete_header");
    String str5 = b.a(bool, "id_really_delete_character_entry_text");
    String str6 = b.a(bool, "id_yes");
    String str2 = b.a(bool, "id_no");
    String str1 = (str4 != null) ? str4 : "Delete Character";
    jm jm3;
    (jm3 = in.a(paramcr.f)).w = str1;
    String str3 = (str5 != null) ? str5 : "Are you sure?";
    jm jm1;
    (jm1 = jm3).av = str3;
    jm1.eh = 0;
    jm jm2;
    (jm2 = jm1).bq = false;
    jm1 = jm2.a((str6 != null) ? str6 : "Yes", (str2 != null) ? str2 : "No", paramRunnable, (Runnable)null);
    in.a(paramStage, jm1.a());
  }
}
