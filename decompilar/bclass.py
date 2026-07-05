package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.assets.AssetManager;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Animation;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.g2d.freetype.FreeTypeFontGenerator;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.IntMap;
import com.badlogic.gdx.utils.XmlReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public final class b {
  private static final AssetManager a = new AssetManager(new c());
  
  public static NinePatch a;
  
  public static TextureRegion a;
  
  public static Texture a;
  
  public static Texture b;
  
  public static Texture c;
  
  public static Texture d;
  
  public static Texture e;
  
  public static Texture f;
  
  public static Texture g;
  
  public static Texture h;
  
  public static Texture i;
  
  public static Texture j;
  
  public static NinePatch b;
  
  public static NinePatch c;
  
  public static Texture k;
  
  public static Texture l;
  
  public static NinePatch d;
  
  public static NinePatch e;
  
  public static NinePatch f;
  
  public static NinePatch g;
  
  public static Drawable a;
  
  public static Drawable b;
  
  public static NinePatch h;
  
  public static NinePatch i;
  
  public static NinePatch j;
  
  public static NinePatch k;
  
  public static NinePatch l;
  
  public static NinePatch m;
  
  public static NinePatch n;
  
  public static NinePatch o;
  
  public static NinePatch p;
  
  public static Texture m;
  
  public static BitmapFont a;
  
  public static BitmapFont b;
  
  public static Texture n;
  
  public static TextureRegion[] a;
  
  public static Texture o;
  
  public static TextureRegion[] b;
  
  public static TextureRegion b;
  
  public static Texture p;
  
  public static TextureRegion c;
  
  public static Texture q;
  
  public static Texture r;
  
  public static Texture s;
  
  public static Texture t;
  
  public static Texture u;
  
  public static Texture v;
  
  public static Texture w;
  
  public static NinePatch q;
  
  public static NinePatch r;
  
  public static NinePatch s;
  
  public static NinePatch t;
  
  public static NinePatch u;
  
  public static Texture x;
  
  public static Texture y;
  
  public static NinePatchDrawable a;
  
  public static NinePatchDrawable b;
  
  public static Texture z;
  
  public static Texture A;
  
  public static Texture B;
  
  public static Texture C;
  
  public static NinePatch v;
  
  public static NinePatch w;
  
  public static NinePatch x;
  
  public static NinePatch y;
  
  public static NinePatch z;
  
  public static Texture D;
  
  public static Texture E;
  
  public static Texture F;
  
  public static NinePatch A;
  
  public static Drawable c;
  
  public static Drawable d;
  
  public static Drawable e;
  
  public static NinePatch B;
  
  public static NinePatch C;
  
  public static Texture G;
  
  public static TextureRegion d;
  
  public static TextureRegion e;
  
  public static TextureRegion f;
  
  public static TextureRegion g;
  
  public static Texture H;
  
  public static final String[] a = new String[] { "en", "id", "ms", "pt", "th", "pl", "es" };
  
  private static final HashMap a = new HashMap<>();
  
  private static String c = "";
  
  public static Texture I;
  
  public static Texture J;
  
  public static Texture K;
  
  public static Texture L;
  
  public static Texture M;
  
  public static Texture N;
  
  public static Texture O;
  
  public static ai a;
  
  public static o a;
  
  public static h a;
  
  public static l a;
  
  public static ae a;
  
  public static aa a;
  
  public static v a;
  
  public static r a;
  
  public static im a;
  
  public static f a;
  
  public static NinePatch D;
  
  public static NinePatch E;
  
  public static NinePatch F;
  
  public static NinePatch G;
  
  public static Texture P;
  
  public static Texture Q;
  
  public static Texture R;
  
  public static Texture S;
  
  public static Texture T;
  
  public static Texture U;
  
  public static Texture V;
  
  public static Texture W;
  
  public static Texture X;
  
  public static Texture Y;
  
  public static Texture Z;
  
  public static Texture aa;
  
  public static Texture ab;
  
  public static Texture ac;
  
  public static Texture ad;
  
  public static Texture ae;
  
  public static Texture af;
  
  public static Texture ag;
  
  public static Texture ah;
  
  public static Texture ai;
  
  public static Texture aj;
  
  public static Texture ak;
  
  public static Texture al;
  
  public static Texture am;
  
  public static Texture an;
  
  public static Texture ao;
  
  public static Texture ap;
  
  public static Texture aq;
  
  public static Texture ar;
  
  public static Texture as;
  
  public static Texture at;
  
  public static Texture au;
  
  public static Texture av;
  
  public static Texture aw;
  
  public static Texture ax;
  
  public static Texture ay;
  
  public static Texture az;
  
  public static Texture aA;
  
  public static Texture aB;
  
  public static Texture aC;
  
  public static Texture aD;
  
  public static Drawable f;
  
  public static Texture aE;
  
  public static Texture aF;
  
  public static Texture aG;
  
  public static Texture aH;
  
  public static Texture aI;
  
  public static Texture aJ;
  
  public static Texture aK;
  
  public static Texture aL;
  
  public static Texture aM;
  
  public static Texture aN;
  
  public static Texture aO;
  
  public static Texture aP;
  
  public static Texture aQ;
  
  public static Texture aR;
  
  public static Texture aS;
  
  public static Texture aT;
  
  public static Texture aU;
  
  public static Texture aV;
  
  public static Texture aW;
  
  public static Texture aX;
  
  public static TextureRegion[] c;
  
  public static TextureRegion[] d;
  
  public static Texture aY;
  
  public static TextureRegion h;
  
  public static Texture aZ;
  
  public static TextureRegion i;
  
  private static final Set a = new HashSet();
  
  private static final IntMap a = new IntMap();
  
  public static FreeTypeFontGenerator a;
  
  public static FreeTypeFontGenerator b;
  
  public static FreeTypeFontGenerator c;
  
  public static FreeTypeFontGenerator d;
  
  public static BitmapFont c;
  
  public static BitmapFont d;
  
  public static BitmapFont e;
  
  public static BitmapFont f;
  
  static boolean b(String paramString) {
    return (paramString != null && (paramString.matches("^[A-Za-z]:[\\\\/].*") || paramString.startsWith("/")));
  }
  
  public static Texture a(String paramString) {
    if (paramString == null)
      return I; 
    byte b1 = -1;
    switch (paramString.hashCode()) {
      case 3355:
        if (paramString.equals("id"))
          b1 = 0; 
        break;
      case 3580:
        if (paramString.equals("pl"))
          b1 = 1; 
        break;
      case 3494:
        if (paramString.equals("ms"))
          b1 = 2; 
        break;
      case 3588:
        if (paramString.equals("pt"))
          b1 = 3; 
        break;
      case 3700:
        if (paramString.equals("th"))
          b1 = 4; 
        break;
      case 3246:
        if (paramString.equals("es"))
          b1 = 5; 
        break;
      case 3241:
        if (paramString.equals("en"))
          b1 = 6; 
        break;
    } 
    switch (b1) {
      case 0:
        return J;
      case 1:
        return N;
      case 2:
        return K;
      case 3:
        return L;
      case 4:
        return M;
      case 5:
        return O;
      case 6:
        return I;
    } 
    return I;
  }
  
  public static String b(String paramString) {
    int i = -1;
    int j;
    for (j = 0; j < a.length; j++) {
      if (a[j].equals(paramString)) {
        i = j;
        break;
      } 
    } 
    if (i == -1)
      i = 0; 
    j = (i + 1) % a.length;
    return (String)a[j];
  }
  
  private static void a(int paramInt, Texture paramTexture) {
    TextureRegion[][] arrayOfTextureRegion = TextureRegion.split(paramTexture, 32, 32);
    TextureRegion[] arrayOfTextureRegion1 = new TextureRegion[4];
    for (byte b1 = 0; b1 < 4; b1++) {
      arrayOfTextureRegion1[b1] = arrayOfTextureRegion[0][b1];
      arrayOfTextureRegion1[b1].flip(false, true);
    } 
    Animation animation;
    (animation = new Animation(0.15F, (Object[])arrayOfTextureRegion1)).setPlayMode(Animation.PlayMode.LOOP);
    a.put(paramInt, animation);
  }
  
  public static void a() {
    a.load("pack1/news_1.png", Texture.class);
    a.load("pack1/npc_can_take_quest_icon.png", Texture.class);
    a.load("pack1/npc_done_quest_icon.png", Texture.class);
    a.load("pack1/npc_incomplete_quest_icon.png", Texture.class);
    a.load("pack1/backdrop_scrollbar.png", Texture.class);
    a.load("pack1/scrollbar.png", Texture.class);
    a.load("pack1/indicator_listitemarrow.png", Texture.class);
    a.load("pack1/icon_outfit-body.png", Texture.class);
    a.load("pack1/icon_outfit-extras.png", Texture.class);
    a.load("pack1/icon_outfit-face.png", Texture.class);
    a.load("pack1/icon_outfit-hair.png", Texture.class);
    a.load("pack1/icons_symbols.png", Texture.class);
    a.load("pack1/statussymbolsicons.png", Texture.class);
    a.load("pack1/goto_indicator.png", Texture.class);
    a.load("pack1/goto_walk_indicator.png", Texture.class);
    a.load("pack1/more_idle.png", Texture.class);
    a.load("pack1/more_active.png", Texture.class);
    a.load("pack1/background_playerstatus_125.png", Texture.class);
    a.load("pack1/backdrop_monsterstatus_125.png", Texture.class);
    a.load("pack1/statusbar_grey_125.png", Texture.class);
    a.load("pack1/statusbar_health_125.png", Texture.class);
    a.load("pack1/statusbar_mana_125.png", Texture.class);
    a.load("pack1/statusbar_monster_125.png", Texture.class);
    a.load("pack1/statusbar_xp_125.png", Texture.class);
    a.load("pack1/target_white.png", Texture.class);
    a.load("pack1/target_red.png", Texture.class);
    a.load("pack1/target_cyan.png", Texture.class);
    a.load("pack1/tile_button_ShowChat_idle_175.png", Texture.class);
    a.load("pack1/tile_button_ShowChat_active_175.png", Texture.class);
    a.load("pack1/goldplatinum_status.png", Texture.class);
    a.load("pack1/background_zoneindicator.png", Texture.class);
    a.load("pack1/backdrop_chat.png", Texture.class);
    a.load("pack1/backdrop_pleasewait.png", Texture.class);
    a.load("pack1/grid_background_idle.png", Texture.class);
    a.load("pack1/grid_background_active.png", Texture.class);
    a.load("pack1/backdrop_mainmenu.png", Texture.class);
    a.load("pack1/backdrop_header.png", Texture.class);
    a.load("pack1/backdrop_paymentheader.png", Texture.class);
    a.load("pack1/backdrop_header-listbox.png", Texture.class);
    a.load("pack1/backdrop_header-listbox-down.png", Texture.class);
    a.load("pack1/textfield_listitem_idle.png", Texture.class);
    a.load("pack1/textfield_listitem_active.png", Texture.class);
    a.load("pack1/textfield_listitem_highlighted_idle.png", Texture.class);
    a.load("pack1/textfield_listitem_highlighted_active.png", Texture.class);
    a.load("pack1/conversation_backdrop.png", Texture.class);
    a.load("pack1/button_back_idle_125.png", Texture.class);
    a.load("pack1/button_back_active_125.png", Texture.class);
    a.load("pack1/button_save_ui.png", Texture.class);
    a.load("pack1/tile_button_close_idle_175.png", Texture.class);
    a.load("pack1/tile_button_close_active_175.png", Texture.class);
    a.load("pack1/backdrop_menuscreen_125.png", Texture.class);
    a.load("pack1/checkbox_active_125.png", Texture.class);
    a.load("pack1/checkbox_idle_125.png", Texture.class);
    a.load("pack1/button_default_idle.png", Texture.class);
    a.load("pack1/button_default_active.png", Texture.class);
    a.load("pack1/button_green_idle.png", Texture.class);
    a.load("pack1/button_green_active.png", Texture.class);
    a.load("pack1/button_delete_idle.png", Texture.class);
    a.load("pack1/button_delete_active.png", Texture.class);
    a.load("pack1/lock_idleTexture.png", Texture.class);
    a.load("pack1/lock_activeTexture.png", Texture.class);
    a.load("pack1/settings_idle.png", Texture.class);
    a.load("pack1/settings_active.png", Texture.class);
    a.load("pack1/backdrop_smallbox.png", Texture.class);
    a.load("pack1/textfield_usertext_Idle.png", Texture.class);
    a.load("pack1/textfield_usertext_Active.png", Texture.class);
    a.load("pack1/statusbar_loading.png", Texture.class);
    a.load("pack1/statusbar_loading_backdrop.png", Texture.class);
    a.load("pack1/vocation_background_idle.png", Texture.class);
    a.load("pack1/QuestLog.png", Texture.class);
    a.load("pack1/backdrop_button_contextmenu_idle.png", Texture.class);
    a.load("pack1/backdrop_button_contextmenu_active.png", Texture.class);
    a.load("pack1/vocation_background_active.png", Texture.class);
    a.load("pack1/tile_button_contextmenu_attack_175.png", Texture.class);
    a.load("pack1/tile_button_contextmenu_talk_175.png", Texture.class);
    a.load("pack1/tile_button_contextmenu_go_175.png", Texture.class);
    a.load("pack1/tile_button_contextmenu_drop_175.png", Texture.class);
    a.load("pack1/tile_button_contextmenu_lookmagnifier_175.png", Texture.class);
    a.load("pack1/tile_button_contextmenu_useequip_175.png", Texture.class);
    a.load("pack1/tile_button_contextmenu_take_175.png", Texture.class);
    a.load("pack1/indicator_trianglemarker.png", Texture.class);
    a.load("pack1/backdrop_sprites_125.png", Texture.class);
    a.load("pack1/backdrop_interface.png", Texture.class);
    a.load("pack1/Mainmenu_CharacterAdd_125.png", Texture.class);
    a.load("pack1/button_skillAttack_active.png", Texture.class);
    a.load("pack1/button_skillAttack_idle.png", Texture.class);
    a.load("pack1/button_skillDefense_active.png", Texture.class);
    a.load("pack1/button_skillDefense_idle.png", Texture.class);
    a.load("pack1/button_amulet_active_175.png", Texture.class);
    a.load("pack1/button_amulet_idle_175.png", Texture.class);
    a.load("pack1/button_armor_active_175.png", Texture.class);
    a.load("pack1/button_armor_idle_175.png", Texture.class);
    a.load("pack1/button_equipped_active_175.png", Texture.class);
    a.load("pack1/button_equipped_idle_175.png", Texture.class);
    a.load("pack1/button_helmet_active_175.png", Texture.class);
    a.load("pack1/button_helmet_idle_175.png", Texture.class);
    a.load("pack1/button_legs_active_175.png", Texture.class);
    a.load("pack1/button_legs_idle_175.png", Texture.class);
    a.load("pack1/button_ring_active_175.png", Texture.class);
    a.load("pack1/button_ring_idle_175.png", Texture.class);
    a.load("pack1/button_shield_active_175.png", Texture.class);
    a.load("pack1/button_shield_idle_175.png", Texture.class);
    a.load("pack1/tile_button_inventory_active_175.png", Texture.class);
    a.load("pack1/tile_button_inventory_idle_175.png", Texture.class);
    a.load("pack1/tile_button_menu_active_175.png", Texture.class);
    a.load("pack1/tile_button_menu_idle_175.png", Texture.class);
    a.load("pack1/button_marketplace_active.png", Texture.class);
    a.load("pack1/button_marketplace_idle.png", Texture.class);
    a.load("pack1/tile_button_logout_active.png", Texture.class);
    a.load("pack1/tile_button_logout_idle.png", Texture.class);
    a.load("pack1/tile_button_buypot_active.png", Texture.class);
    a.load("pack1/tile_button_buypot_idle.png", Texture.class);
    a.load("pack1/tile_button_switch_active.png", Texture.class);
    a.load("pack1/tile_button_switch_idle.png", Texture.class);
    a.load("pack1/button_passwordhide_idle.png", Texture.class);
    a.load("pack1/button_passwordhide_active.png", Texture.class);
    a.load("pack1/button_passwordshow_idle.png", Texture.class);
    a.load("pack1/button_passwordshow_active.png", Texture.class);
    a.load("pack1/button_randomize_idle.png", Texture.class);
    a.load("pack1/button_randomize_active.png", Texture.class);
    a.load("pack1/tile_button_chat-public_active_175.png", Texture.class);
    a.load("pack1/tile_button_chat-public_idle_175.png", Texture.class);
    a.load("pack1/tile_button_chat-global_active_175.png", Texture.class);
    a.load("pack1/tile_button_chat-global_idle_175.png", Texture.class);
    a.load("pack1/tile_button_chat-guild_active_175.png", Texture.class);
    a.load("pack1/tile_button_chat-guild_idle_175.png", Texture.class);
    a.load("pack1/tile_button_chat-private_active_175.png", Texture.class);
    a.load("pack1/tile_button_chat-private_idle_175.png", Texture.class);
    a.load("pack1/button_okchat_active.png", Texture.class);
    a.load("pack1/button_okchat_idle.png", Texture.class);
    a.load("pack1/flags_eng_125.png", Texture.class);
    a.load("pack1/flags_indo_125.png", Texture.class);
    a.load("pack1/flags_malay_125.png", Texture.class);
    a.load("pack1/flags_pt_125.png", Texture.class);
    a.load("pack1/flags_thai_125.png", Texture.class);
    a.load("pack1/flags_pl_125.png", Texture.class);
    a.load("pack1/flags_es_125.png", Texture.class);
    a.load("pack1/AnalogStick.png", Texture.class);
    a.load("pack1/player_indicator.png", Texture.class);
    a.load("pack1/touch_indicator.png", Texture.class);
    a.load("pack1/arc_bar.png", Texture.class);
    a.load("pack1/object_bars.png", Texture.class);
    a.finishLoading();
  }
  
  public static void a(cq paramcq) {
    if (c != null && d != null && e != null) {
      a = (FreeTypeFontGenerator)c;
      b = (FreeTypeFontGenerator)c;
    } else {
      (c = a(a = new FreeTypeFontGenerator(Gdx.files.internal("fonts/ui_default.ttf")))).getRegion().getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
      (d = a(b = new FreeTypeFontGenerator(Gdx.files.internal("fonts/ui_thai.ttf")))).getRegion().getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
      (f = a((FreeTypeFontGenerator)(d = (BitmapFont)new FreeTypeFontGenerator(Gdx.files.internal("fonts/ui_pl.ttf"))))).getRegion().getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
      (e = a((FreeTypeFontGenerator)(c = (BitmapFont)new FreeTypeFontGenerator(Gdx.files.internal("fonts/ui_lao.ttf"))))).getRegion().getTexture().setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
      a = (FreeTypeFontGenerator)c;
      b = (FreeTypeFontGenerator)c;
    } 
    Texture texture3;
    (texture3 = b("pack1/npc_can_take_quest_icon.png")).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    texture3.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
    a(1, texture3);
    (texture3 = b("pack1/npc_done_quest_icon.png")).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    texture3.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
    a(2, texture3);
    (texture3 = b("pack1/npc_incomplete_quest_icon.png")).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    texture3.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
    a(3, texture3);
    (texture3 = b("pack1/icons_symbols.png")).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    texture3.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
    TextureRegion[][] arrayOfTextureRegion2 = TextureRegion.split(texture3, 23, 23);
    c = (BitmapFont)new TextureRegion[30];
    byte b4 = 0;
    for (byte b5 = 0; b5 < 2; b5++) {
      for (byte b7 = 0; b7 < 15; b7++) {
        TextureRegion textureRegion1;
        a(textureRegion1 = arrayOfTextureRegion2[b5][b7]);
        c[b4++] = (BitmapFont)textureRegion1;
      } 
    } 
    Texture texture6;
    (texture6 = b("pack1/statussymbolsicons.png")).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    texture6.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
    TextureRegion[][] arrayOfTextureRegion4 = TextureRegion.split(texture6, 23, 23);
    d = (BitmapFont)new TextureRegion[30];
    byte b6 = 0;
    for (byte b2 = 0; b2 < 2; b2++) {
      for (b4 = 0; b4 < 15; b4++) {
        TextureRegion textureRegion1;
        a(textureRegion1 = arrayOfTextureRegion4[b2][b4]);
        d[b6++] = (BitmapFont)textureRegion1;
      } 
    } 
    q = (NinePatch)b("pack1/background_playerstatus_125.png");
    r = (NinePatch)b("pack1/backdrop_monsterstatus_125.png");
    s = (NinePatch)b("pack1/statusbar_grey_125.png");
    t = (NinePatch)b("pack1/statusbar_health_125.png");
    u = (NinePatch)b("pack1/statusbar_mana_125.png");
    v = (NinePatch)b("pack1/statusbar_monster_125.png");
    w = (NinePatch)b("pack1/statusbar_xp_125.png");
    (aY = b("pack1/goto_indicator.png")).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    h = new TextureRegion(aY);
    (aZ = b("pack1/goto_walk_indicator.png")).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    i = new TextureRegion(aZ);
    b = (FreeTypeFontGenerator)a("pack1/backdrop_scrollbar.png", 2, 2, 2, 2);
    c = (BitmapFont)a("pack1/scrollbar.png", 2, 2, 2, 2);
    m = b("pack1/indicator_listitemarrow.png");
    q = new NinePatch((Texture)s, 2, 2, 0, 0);
    r = new NinePatch((Texture)t, 2, 2, 0, 0);
    s = new NinePatch((Texture)u, 2, 2, 0, 0);
    t = new NinePatch((Texture)v, 2, 2, 0, 0);
    u = new NinePatch((Texture)w, 2, 2, 0, 0);
    i = (TextureRegion)b("pack1/more_idle.png");
    j = (NinePatch)b("pack1/more_active.png");
    E = a("pack1/backdrop_pleasewait.png", 11, 11, 11, 11);
    D = a("pack1/backdrop_chat.png", 8, 8, 8, 8);
    F = a("pack1/goldplatinum_status.png", 8, 8, 8, 8);
    G = a("pack1/background_zoneindicator.png", 8, 8, 8, 8);
    P = b("pack1/button_skillAttack_active.png");
    Q = b("pack1/button_skillAttack_idle.png");
    R = b("pack1/button_skillDefense_active.png");
    S = b("pack1/button_skillDefense_idle.png");
    aj = b("pack1/tile_button_ShowChat_idle_175.png");
    ak = b("pack1/tile_button_ShowChat_active_175.png");
    T = b("pack1/button_amulet_active_175.png");
    U = b("pack1/button_amulet_idle_175.png");
    V = b("pack1/button_armor_active_175.png");
    W = b("pack1/button_armor_idle_175.png");
    X = b("pack1/button_equipped_active_175.png");
    Y = b("pack1/button_equipped_idle_175.png");
    Z = b("pack1/button_helmet_active_175.png");
    aa = b("pack1/button_helmet_idle_175.png");
    ab = b("pack1/button_legs_active_175.png");
    ac = b("pack1/button_legs_idle_175.png");
    ad = b("pack1/button_ring_active_175.png");
    ae = b("pack1/button_ring_idle_175.png");
    af = b("pack1/button_shield_active_175.png");
    ag = b("pack1/button_shield_idle_175.png");
    ah = b("pack1/tile_button_inventory_active_175.png");
    ai = b("pack1/tile_button_inventory_idle_175.png");
    am = b("pack1/tile_button_menu_active_175.png");
    an = b("pack1/tile_button_menu_idle_175.png");
    ao = b("pack1/button_marketplace_active.png");
    ap = b("pack1/button_marketplace_idle.png");
    aq = b("pack1/tile_button_logout_active.png");
    ar = b("pack1/tile_button_logout_idle.png");
    as = b("pack1/tile_button_buypot_active.png");
    at = b("pack1/tile_button_buypot_idle.png");
    au = b("pack1/tile_button_switch_active.png");
    av = b("pack1/tile_button_switch_idle.png");
    aw = b("pack1/tile_button_contextmenu_attack_175.png");
    ax = b("pack1/tile_button_contextmenu_talk_175.png");
    ay = b("pack1/tile_button_contextmenu_go_175.png");
    az = b("pack1/tile_button_contextmenu_drop_175.png");
    aA = b("pack1/tile_button_contextmenu_lookmagnifier_175.png");
    aB = b("pack1/tile_button_contextmenu_useequip_175.png");
    aC = b("pack1/tile_button_contextmenu_take_175.png");
    aD = b("pack1/indicator_trianglemarker.png");
    aE = b("pack1/icon_outfit-body.png");
    aF = b("pack1/icon_outfit-extras.png");
    aG = b("pack1/icon_outfit-face.png");
    aH = b("pack1/icon_outfit-hair.png");
    aI = b("pack1/tile_button_chat-public_active_175.png");
    aJ = b("pack1/tile_button_chat-public_idle_175.png");
    aK = b("pack1/tile_button_chat-global_active_175.png");
    aL = b("pack1/tile_button_chat-global_idle_175.png");
    aM = b("pack1/tile_button_chat-guild_active_175.png");
    aN = b("pack1/tile_button_chat-guild_idle_175.png");
    aO = b("pack1/tile_button_chat-private_active_175.png");
    aP = b("pack1/tile_button_chat-private_idle_175.png");
    aQ = b("pack1/button_okchat_active.png");
    aR = b("pack1/button_okchat_idle.png");
    aS = b("pack1/button_passwordhide_idle.png");
    aT = b("pack1/button_passwordhide_active.png");
    aU = b("pack1/button_passwordshow_idle.png");
    aV = b("pack1/button_passwordshow_active.png");
    aW = b("pack1/button_randomize_idle.png");
    aX = b("pack1/button_randomize_active.png");
    Texture texture2;
    (texture2 = b("pack1/grid_background_idle.png")).setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat);
    d = (BitmapFont)new ak(texture2, 5, 5, 5, 5);
    Texture texture5;
    (texture5 = b("pack1/grid_background_active.png")).setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat);
    e = (BitmapFont)new ak(texture5, 5, 5, 5, 5);
    (texture6 = b("pack1/backdrop_interface.png")).setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat);
    c = (BitmapFont)new ak(texture6, 8, 8, 8, 8);
    a = (FreeTypeFontGenerator)b("pack1/news_1.png");
    b = (FreeTypeFontGenerator)b("pack1/backdrop_menuscreen_125.png");
    e = (BitmapFont)a("pack1/QuestLog.png", 16, 16, 16, 16);
    d = (BitmapFont)a("pack1/backdrop_mainmenu.png", 16, 16, 16, 16);
    f = (BitmapFont)a("pack1/backdrop_header.png", 32, 32, 16, 16);
    g = (TextureRegion)a("pack1/backdrop_paymentheader.png", 32, 16, 20, 16);
    (texture2 = b("pack1/backdrop_header-listbox.png")).setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat);
    a = (FreeTypeFontGenerator)new ak(texture2, 2, 2, 2, 2);
    (texture2 = b("pack1/backdrop_header-listbox-down.png")).setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat);
    b = (FreeTypeFontGenerator)new ak(texture2, 2, 2, 2, 2);
    h = (TextureRegion)a("pack1/textfield_listitem_idle.png", 16, 16, 8, 8);
    l = a("pack1/conversation_backdrop.png", 8, 8, 8, 8);
    i = (TextureRegion)a("pack1/textfield_listitem_active.png", 16, 16, 8, 8);
    j = a("pack1/textfield_listitem_highlighted_idle.png", 16, 16, 8, 8);
    k = a("pack1/textfield_listitem_highlighted_active.png", 16, 16, 8, 8);
    m = (Texture)a("pack1/button_default_idle.png", 16, 16, 16, 16);
    n = (Texture)a("pack1/button_default_active.png", 16, 16, 16, 16);
    o = (Texture)a("pack1/button_green_idle.png", 16, 16, 16, 16);
    p = (Texture)a("pack1/button_green_active.png", 16, 16, 16, 16);
    B = a("pack1/vocation_background_idle.png", 16, 16, 16, 16);
    C = a("pack1/vocation_background_active.png", 16, 16, 16, 16);
    c = (BitmapFont)b("pack1/button_back_idle_125.png");
    d = (BitmapFont)b("pack1/button_back_active_125.png");
    e = (BitmapFont)b("pack1/button_save_ui.png");
    f = (BitmapFont)b("pack1/tile_button_close_idle_175.png");
    g = (TextureRegion)b("pack1/tile_button_close_active_175.png");
    k = (NinePatch)b("pack1/lock_idleTexture.png");
    l = (NinePatch)b("pack1/lock_activeTexture.png");
    x = (NinePatch)b("pack1/checkbox_active_125.png");
    y = (NinePatch)b("pack1/checkbox_idle_125.png");
    z = (NinePatch)b("pack1/button_delete_idle.png");
    A = (NinePatch)b("pack1/button_delete_active.png");
    B = (NinePatch)b("pack1/settings_idle.png");
    C = (NinePatch)b("pack1/settings_active.png");
    w = a("pack1/backdrop_button_contextmenu_idle.png", 8, 8, 8, 8);
    v = a("pack1/backdrop_smallbox.png", 8, 8, 8, 8);
    x = a("pack1/statusbar_loading.png", 1, 1, 5, 6);
    y = a("pack1/statusbar_loading_backdrop.png", 3, 3, 3, 3);
    z = a("pack1/textfield_usertext_Idle.png", 8, 8, 8, 8);
    A = a("pack1/textfield_usertext_Active.png", 8, 8, 8, 8);
    D = (NinePatch)new Texture(Gdx.files.internal("pack1/target_white.png"));
    E = (NinePatch)new Texture(Gdx.files.internal("pack1/target_red.png"));
    F = (NinePatch)new Texture(Gdx.files.internal("pack1/target_cyan.png"));
    if (y != null)
      a = (FreeTypeFontGenerator)new NinePatchDrawable(new NinePatch((Texture)y, 48, 45, 0, 0)); 
    if (x != null)
      b = (FreeTypeFontGenerator)new NinePatchDrawable(new NinePatch((Texture)x, 45, 48, 0, 0)); 
    (n = b("pack1/AnalogStick.png")).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    TextureRegion[][] arrayOfTextureRegion1 = TextureRegion.split(n, 140, 140);
    a = (FreeTypeFontGenerator)new TextureRegion[5];
    for (byte b3 = 0; b3 < 5; b3++)
      a[b3] = (FreeTypeFontGenerator)arrayOfTextureRegion1[0][b3]; 
    (o = b("pack1/player_indicator.png")).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    TextureRegion[][] arrayOfTextureRegion3 = TextureRegion.split(o, 128, 128);
    b = (FreeTypeFontGenerator)new TextureRegion[5];
    for (byte b1 = 0; b1 < 5; b1++)
      b[b1] = (FreeTypeFontGenerator)arrayOfTextureRegion3[0][b1]; 
    (p = b("pack1/touch_indicator.png")).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    c = (BitmapFont)new TextureRegion(p);
    Texture texture1;
    (texture1 = b("pack1/arc_bar.png")).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    b = (FreeTypeFontGenerator)new TextureRegion(texture1);
    (texture1 = b("pack1/object_bars.png")).setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
    TextureRegion textureRegion = new TextureRegion(texture1, 0, 0, 5, 5);
    a = (FreeTypeFontGenerator)new NinePatch(textureRegion, 1, 1, 1, 1);
    a = (FreeTypeFontGenerator)new TextureRegion(texture1, 6, 1, 3, 3);
    d = (BitmapFont)a((Texture)(G = (NinePatch)b("pack1/backdrop_sprites_125.png")), 0);
    e = (BitmapFont)a((Texture)G, 118);
    f = (BitmapFont)a((Texture)G, 236);
    g = a((Texture)G, 354);
    H = b("pack1/Mainmenu_CharacterAdd_125.png");
    I = b("pack1/flags_eng_125.png");
    J = b("pack1/flags_indo_125.png");
    K = b("pack1/flags_malay_125.png");
    L = b("pack1/flags_pt_125.png");
    M = b("pack1/flags_thai_125.png");
    O = b("pack1/flags_es_125.png");
    N = b("pack1/flags_pl_125.png");
    int i = Math.round(a.getLineHeight());
    Pixmap pixmap;
    (pixmap = new Pixmap(1, i, Pixmap.Format.RGBA8888)).setColor(1.0F, 1.0F, 1.0F, 1.0F);
    pixmap.fill();
    Texture texture4 = new Texture(pixmap);
    pixmap.dispose();
    f = (BitmapFont)new TextureRegionDrawable(new TextureRegion(texture4));
    a(paramcq.S);
    al.b(Gdx.files.getLocalStoragePath() + "JTME/pack5/");
    al.a(paramcq.ag);
    al.b(paramcq.ah);
    c();
  }
  
  private static void a(TextureRegion paramTextureRegion) {
    Texture texture = paramTextureRegion.getTexture();
    float f2 = 0.05F / texture.getWidth();
    float f1 = 0.05F / texture.getHeight();
    paramTextureRegion.setU(paramTextureRegion.getU() + f2);
    paramTextureRegion.setV(paramTextureRegion.getV() + f1);
    paramTextureRegion.setU2(paramTextureRegion.getU2() - f2);
    paramTextureRegion.setV2(paramTextureRegion.getV2() - f1);
  }
  
  public static AssetManager a() {
    return (AssetManager)a;
  }
  
  public static void a(e[] paramArrayOfe, cq paramcq) {
    FreeTypeFontGenerator freeTypeFontGenerator = a;
    FileHandle fileHandle;
    (fileHandle = Gdx.files.local("JTME")).mkdirs();
    String str = fileHandle.file().getAbsolutePath();
    int i = paramArrayOfe.length;
    for (byte b1 = 0; b1 < i; b1++) {
      e e1 = paramArrayOfe[b1];
      if (!a.contains(e1)) {
        switch (d.a[e1.ordinal()]) {
          case 1:
            try {
              (a = (FreeTypeFontGenerator)new l((AssetManager)freeTypeFontGenerator, str)).h();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "IconLoader falhou", exception);
            } 
            try {
              (a = (FreeTypeFontGenerator)new h((AssetManager)freeTypeFontGenerator, str)).g();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "EffectLoader falhou", exception);
            } 
            try {
              (a = (FreeTypeFontGenerator)new r((AssetManager)freeTypeFontGenerator, str)).j();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "LightLoader falhou", exception);
            } 
            try {
              (a = (FreeTypeFontGenerator)new ai((AssetManager)freeTypeFontGenerator, str)).n();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "TileLoader falhou", exception);
            } 
            try {
              (a = (FreeTypeFontGenerator)new o((AssetManager)freeTypeFontGenerator, str)).i();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "ItemLoader falhou", exception);
            } 
            try {
              (a = (FreeTypeFontGenerator)new v((AssetManager)freeTypeFontGenerator, str, paramcq.bP)).k();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "MobLoader falhou", exception);
            } 
            try {
              (a = (FreeTypeFontGenerator)new ae((AssetManager)freeTypeFontGenerator, str)).m();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "SubOutfitLoader falhou", exception);
            } 
            try {
              (a = (FreeTypeFontGenerator)new aa((AssetManager)freeTypeFontGenerator, str, paramcq.bP, paramcq.bP)).l();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "OutfitLoader falhou", exception);
            } 
            break;
          case 2:
            try {
              c();
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "loadDictionary falhou", exception);
            } 
            break;
          case 3:
            try {
              a.clear();
              a(paramcq.S);
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "loadLanguage falhou", exception);
            } 
            break;
          case 4:
            try {
              b(paramcq);
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "loadClientMap falhou", exception);
            } 
            break;
          case 5:
            try {
              String str1 = Gdx.files.getLocalStoragePath() + "JTME/pack5/";
              al.d();
              al.b(str1);
              al.a(paramcq.ag);
              al.b(paramcq.ah);
            } catch (Exception exception) {
              Gdx.app.error("Assets.reload", "Audio reload falhou", exception);
            } 
            break;
        } 
        a.add(e1);
      } 
    } 
  }
  
  public static void b() {
    al.a(3);
  }
  
  public static void a(cq paramcq, int paramInt1, int paramInt2, int paramInt3, int paramInt4, int paramInt5, int paramInt6, int paramInt7, int paramInt8, int paramInt9, int paramInt10, int paramInt11) {
    if (al != null)
      al.dispose(); 
    bl bl;
    (bl = new bl(paramcq)).b(paramInt1, paramInt2, paramInt3, paramInt4, paramInt5, paramInt6, paramInt7, paramInt8, paramInt9, paramInt10, paramInt11);
    al = bl.b();
  }
  
  private static Texture b(String paramString) {
    Texture texture;
    (texture = (Texture)a.get(paramString, Texture.class)).setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear);
    return texture;
  }
  
  private static NinePatch a(String paramString, int paramInt1, int paramInt2, int paramInt3, int paramInt4) {
    Texture texture = b(paramString);
    return new NinePatch(texture, paramInt1, paramInt2, paramInt3, paramInt4);
  }
  
  private static TextureRegion a(Texture paramTexture, int paramInt) {
    return new TextureRegion(paramTexture, paramInt, 0, 118, 118);
  }
  
  private static void a(String paramString) {
    if (c.equals(paramString) && !a.isEmpty())
      return; 
    a.clear();
    c = (BitmapFont)paramString;
    try {
      XmlReader xmlReader = new XmlReader();
      FileHandle fileHandle;
      if (!(fileHandle = Gdx.files.internal("lang/jtme_languages.xml")).exists()) {
        Gdx.app.error("Assets", "Arquivo de idiomas nao encontrado: " + fileHandle.path());
        return;
      } 
      Array.ArrayIterator<XmlReader.Element> arrayIterator = xmlReader.parse(fileHandle).getChildrenByName("text").iterator();
      while (arrayIterator.hasNext()) {
        XmlReader.Element element1;
        String str = (element1 = arrayIterator.next()).getAttribute("id");
        XmlReader.Element element2;
        if ((element2 = element1.getChildByName(paramString)) == null)
          element2 = element1.getChildByName("en"); 
        if (element2 != null) {
          String str1 = element2.getText().replace("\\n", "\n");
          a.put(str, str1);
        } 
      } 
      Gdx.app.log("Assets", "Idiomas carregados com sucesso: " + paramString + " (" + a.size() + " textos)");
      return;
    } catch (Exception exception) {
      Gdx.app.error("Assets", "Erro ao fazer parser do XML de idiomas: ", exception);
      return;
    } 
  }
  
  public static String a(String paramString1, String paramString2) {
    if (paramString2 == null || paramString2.isEmpty())
      return ""; 
    if (paramString1 == null || paramString1.isEmpty())
      paramString1 = "en"; 
    a(paramString1);
    return a.containsKey(paramString2) ? (String)a.get(paramString2) : paramString2;
  }
  
  private static void b(cq paramcq) {
    if (!paramcq.U) {
      if (a != null) {
        a.f();
        a = null;
      } 
      return;
    } 
    String str1 = Gdx.files.getLocalStoragePath() + "JTME/pack6/";
    String str2 = "game_data.dat";
    FileHandle fileHandle;
    if (!(fileHandle = Gdx.files.absolute(str1 + str1)).exists()) {
      Gdx.app.log("Assets", "Mapa nativo nencontrado (serbaixado): " + fileHandle.path());
      return;
    } 
    try {
      byte[] arrayOfByte = fileHandle.readBytes();
      a = (FreeTypeFontGenerator)new f(arrayOfByte);
      return;
    } catch (Exception exception) {
      Gdx.app.error("Assets", "Falha ao ler arquivo do mapa.", exception);
      return;
    } 
  }
  
  public static void c(cq paramcq) {
    if (a != null) {
      a.f();
      a = null;
    } 
    b(paramcq);
  }
  
  private static void c() {
    String str1 = Gdx.files.getLocalStoragePath() + "JTME/pack3/";
    String str2 = "dictionary040.cli";
    FileHandle fileHandle;
    if (!(fileHandle = Gdx.files.absolute(str1 + str1)).exists()) {
      Gdx.app.error("Assets", "Dicionnencontrado em " + fileHandle.path());
      return;
    } 
    try {
      byte[] arrayOfByte = fileHandle.readBytes();
      a = (FreeTypeFontGenerator)new im(arrayOfByte);
      return;
    } catch (IOException iOException) {
      Gdx.app.error("Assets", "Erro ao carregar dicionde " + fileHandle.path(), iOException);
      return;
    } 
  }
  
  public static void d() {
    if (al != null) {
      al.dispose();
      al = null;
    } 
    if (a != null) {
      a.dispose();
      a = null;
    } 
    if (c != null) {
      c.dispose();
      c = null;
    } 
    if (d != null) {
      d.dispose();
      d = null;
    } 
    if (e != null) {
      e.dispose();
      e = null;
    } 
    if (f != null) {
      f.dispose();
      f = null;
    } 
    if (a != null) {
      a.dispose();
      a = null;
    } 
    if (b != null) {
      b.dispose();
      b = null;
    } 
    if (c != null) {
      c.dispose();
      c = null;
    } 
    if (d != null) {
      d.dispose();
      d = null;
    } 
    if (h != null) {
      h.dispose();
      h = null;
    } 
    a.dispose();
  }
  
  private static BitmapFont a(FreeTypeFontGenerator paramFreeTypeFontGenerator) {
    FreeTypeFontGenerator.FreeTypeFontParameter freeTypeFontParameter;
    (freeTypeFontParameter = new FreeTypeFontGenerator.FreeTypeFontParameter()).size = 18;
    freeTypeFontParameter.incremental = true;
    freeTypeFontParameter.hinting = FreeTypeFontGenerator.Hinting.Full;
    freeTypeFontParameter.minFilter = Texture.TextureFilter.Linear;
    freeTypeFontParameter.magFilter = Texture.TextureFilter.Linear;
    freeTypeFontParameter.gamma = 1.2F;
    return paramFreeTypeFontGenerator.generateFont(freeTypeFontParameter);
  }
  
  public static BitmapFont a(String paramString) {
    if (paramString == null || paramString.isEmpty())
      return (BitmapFont)((c != null) ? c : a); 
    boolean bool1 = false;
    boolean bool2 = false;
    boolean bool3 = false;
    for (byte b1 = 0; b1 < paramString.length(); b1++) {
      char c;
      if ((c = paramString.charAt(b1)) >= '&& c <= ') {
        bool1 = true;
        break;
      } 
      if (c >= '&& c <= ') {
        bool2 = true;
        break;
      } 
      if ((c >= '&& c <= ') || c == '|| c == ') {
        bool3 = true;
        break;
      } 
    } 
    return (BitmapFont)((bool1 && d != null) ? d : ((bool2 && e != null) ? e : ((bool3 && f != null) ? f : ((c != null) ? c : a))));
  }
  
  public static void a(Label paramLabel, String paramString) {
    if (paramLabel == null)
      return; 
    BitmapFont bitmapFont = a(paramString);
    Label.LabelStyle labelStyle;
    if ((labelStyle = paramLabel.getStyle()) != null && labelStyle.font != bitmapFont) {
      (labelStyle = new Label.LabelStyle(labelStyle)).font = bitmapFont;
      paramLabel.setStyle(labelStyle);
    } 
    paramLabel.setText((paramString == null) ? "" : paramString);
  }
  
  public static void e() {
    a.clear();
  }
  
  public static boolean a() {
    return Gdx.files.local("JTME/packs.properties").exists();
  }
  
  public static Texture a() {
    if (h == null) {
      Pixmap pixmap;
      (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(1.0F, 1.0F, 1.0F, 1.0F);
      pixmap.fill();
      h = (TextureRegion)new Texture(pixmap);
      pixmap.dispose();
    } 
    return (Texture)h;
  }
}
