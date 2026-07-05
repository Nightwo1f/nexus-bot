package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.g2d.freetype.FreeTypeFontGenerator;
import com.badlogic.gdx.math.Interpolation;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Button;
import com.badlogic.gdx.scenes.scene2d.ui.Container;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.ImageButton;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.ScrollPane;
import com.badlogic.gdx.scenes.scene2d.ui.Slider;
import com.badlogic.gdx.scenes.scene2d.ui.Stack;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextArea;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.ui.WidgetGroup;
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public final class in {
  static int ec = -1;
  
  private static Table t;
  
  static Table u;
  
  private static ju a;
  
  private static float bI;
  
  private static float bJ;
  
  private static Table v;
  
  private static Stack c;
  
  private static Table w;
  
  static Table x;
  
  private static Table y;
  
  static TextField j;
  
  static Stage n;
  
  private static ImageButton z;
  
  private static Table z;
  
  private static ScrollPane.ScrollPaneStyle c;
  
  static js a = null;
  
  static js b = null;
  
  static int ed = -1;
  
  static int ee = -1;
  
  static float bK = 0.0F;
  
  static boolean bi = false;
  
  private static float bL = 0.95F;
  
  private static float bM = 0.7F;
  
  static boolean bj = false;
  
  private static float bN = 1.0F;
  
  private static float bO = 8.0F;
  
  private static float bP = 1.0F;
  
  static float bQ = 800.0F;
  
  private static float ak = 0.7F;
  
  private static float al = 0.9F;
  
  private static final List A = new ArrayList();
  
  private static final Map A;
  
  private static Group l;
  
  private static Texture bk;
  
  private static Actor e;
  
  private static Table A;
  
  private static boolean bk = false;
  
  public static void a(Texture paramTexture) {
    if (paramTexture != null)
      A.add(paramTexture); 
  }
  
  static boolean s() {
    cr cr;
    return (Gdx.app.getApplicationListener() instanceof cr && (cr = (cr)Gdx.app.getApplicationListener()).getScreen() instanceof fj) ? ((fj)cr.getScreen()).k() : false;
  }
  
  private static Actor a(String paramString, int paramInt, boolean paramBoolean) {
    // Byte code:
    //   0: aload_0
    //   1: ifnonnull -> 7
    //   4: ldc ''
    //   6: astore_0
    //   7: aload_0
    //   8: dup
    //   9: astore #7
    //   11: ifnull -> 23
    //   14: aload #7
    //   16: invokevirtual length : ()I
    //   19: iconst_3
    //   20: if_icmpge -> 27
    //   23: iconst_0
    //   24: goto -> 104
    //   27: iconst_0
    //   28: istore #9
    //   30: iload #9
    //   32: iconst_2
    //   33: iadd
    //   34: aload #7
    //   36: invokevirtual length : ()I
    //   39: if_icmpge -> 103
    //   42: aload #7
    //   44: iload #9
    //   46: invokevirtual charAt : (I)C
    //   49: sipush #238
    //   52: if_icmpne -> 97
    //   55: aload #7
    //   57: iload #9
    //   59: iconst_1
    //   60: iadd
    //   61: invokevirtual charAt : (I)C
    //   64: sipush #128
    //   67: if_icmpne -> 97
    //   70: getstatic a/in.A : Ljava/util/Map;
    //   73: aload #7
    //   75: iload #9
    //   77: iconst_2
    //   78: iadd
    //   79: invokevirtual charAt : (I)C
    //   82: invokestatic valueOf : (C)Ljava/lang/Character;
    //   85: invokeinterface containsKey : (Ljava/lang/Object;)Z
    //   90: ifeq -> 97
    //   93: iconst_1
    //   94: goto -> 104
    //   97: iinc #9, 1
    //   100: goto -> 30
    //   103: iconst_0
    //   104: ifne -> 126
    //   107: aload_0
    //   108: getstatic com/badlogic/gdx/graphics/Color.WHITE : Lcom/badlogic/gdx/graphics/Color;
    //   111: iload_2
    //   112: iload_1
    //   113: invokestatic a : (Ljava/lang/String;Lcom/badlogic/gdx/graphics/Color;ZI)Lcom/badlogic/gdx/scenes/scene2d/ui/Label;
    //   116: dup
    //   117: astore_3
    //   118: getstatic a/in.bN : F
    //   121: invokevirtual setFontScale : (F)V
    //   124: aload_3
    //   125: areturn
    //   126: aload_0
    //   127: dup
    //   128: astore #7
    //   130: ifnull -> 141
    //   133: aload #7
    //   135: invokevirtual isEmpty : ()Z
    //   138: ifeq -> 146
    //   141: ldc ''
    //   143: goto -> 266
    //   146: new java/lang/StringBuilder
    //   149: dup
    //   150: aload #7
    //   152: invokevirtual length : ()I
    //   155: invokespecial <init> : (I)V
    //   158: astore #9
    //   160: iconst_0
    //   161: istore #10
    //   163: iload #10
    //   165: aload #7
    //   167: invokevirtual length : ()I
    //   170: if_icmpge -> 261
    //   173: iload #10
    //   175: iconst_2
    //   176: iadd
    //   177: aload #7
    //   179: invokevirtual length : ()I
    //   182: if_icmpge -> 242
    //   185: aload #7
    //   187: iload #10
    //   189: invokevirtual charAt : (I)C
    //   192: sipush #238
    //   195: if_icmpne -> 242
    //   198: aload #7
    //   200: iload #10
    //   202: iconst_1
    //   203: iadd
    //   204: invokevirtual charAt : (I)C
    //   207: sipush #128
    //   210: if_icmpne -> 242
    //   213: getstatic a/in.A : Ljava/util/Map;
    //   216: aload #7
    //   218: iload #10
    //   220: iconst_2
    //   221: iadd
    //   222: invokevirtual charAt : (I)C
    //   225: invokestatic valueOf : (C)Ljava/lang/Character;
    //   228: invokeinterface containsKey : (Ljava/lang/Object;)Z
    //   233: ifeq -> 242
    //   236: iinc #10, 3
    //   239: goto -> 163
    //   242: aload #9
    //   244: aload #7
    //   246: iload #10
    //   248: iinc #10, 1
    //   251: invokevirtual charAt : (I)C
    //   254: invokevirtual append : (C)Ljava/lang/StringBuilder;
    //   257: pop
    //   258: goto -> 163
    //   261: aload #9
    //   263: invokevirtual toString : ()Ljava/lang/String;
    //   266: invokestatic a : (Ljava/lang/String;)Lcom/badlogic/gdx/graphics/g2d/BitmapFont;
    //   269: astore_3
    //   270: new com/badlogic/gdx/scenes/scene2d/ui/Label$LabelStyle
    //   273: dup
    //   274: aload_3
    //   275: getstatic com/badlogic/gdx/graphics/Color.WHITE : Lcom/badlogic/gdx/graphics/Color;
    //   278: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/BitmapFont;Lcom/badlogic/gdx/graphics/Color;)V
    //   281: astore #4
    //   283: aload_0
    //   284: ldc '\n'
    //   286: iconst_m1
    //   287: invokevirtual split : (Ljava/lang/String;I)[Ljava/lang/String;
    //   290: astore_0
    //   291: new com/badlogic/gdx/scenes/scene2d/ui/Table
    //   294: dup
    //   295: invokespecial <init> : ()V
    //   298: astore #5
    //   300: iload_1
    //   301: iconst_1
    //   302: if_icmpne -> 317
    //   305: aload #5
    //   307: invokevirtual top : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Table;
    //   310: invokevirtual center : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Table;
    //   313: pop
    //   314: goto -> 344
    //   317: iload_1
    //   318: bipush #16
    //   320: if_icmpne -> 335
    //   323: aload #5
    //   325: invokevirtual top : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Table;
    //   328: invokevirtual right : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Table;
    //   331: pop
    //   332: goto -> 344
    //   335: aload #5
    //   337: invokevirtual top : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Table;
    //   340: invokevirtual left : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Table;
    //   343: pop
    //   344: aload #5
    //   346: getstatic com/badlogic/gdx/scenes/scene2d/Touchable.disabled : Lcom/badlogic/gdx/scenes/scene2d/Touchable;
    //   349: invokevirtual setTouchable : (Lcom/badlogic/gdx/scenes/scene2d/Touchable;)V
    //   352: iload_1
    //   353: bipush #16
    //   355: if_icmpne -> 363
    //   358: bipush #16
    //   360: goto -> 374
    //   363: iload_1
    //   364: iconst_1
    //   365: if_icmpne -> 372
    //   368: iconst_1
    //   369: goto -> 374
    //   372: bipush #8
    //   374: istore_1
    //   375: aload_3
    //   376: invokevirtual getCapHeight : ()F
    //   379: ldc 1.3
    //   381: fmul
    //   382: getstatic a/in.bN : F
    //   385: fmul
    //   386: fstore_3
    //   387: iconst_0
    //   388: istore #6
    //   390: iload #6
    //   392: aload_0
    //   393: arraylength
    //   394: if_icmpge -> 1158
    //   397: aload_0
    //   398: iload #6
    //   400: aaload
    //   401: astore #7
    //   403: new a/io
    //   406: dup
    //   407: invokespecial <init> : ()V
    //   410: dup
    //   411: astore #8
    //   413: fconst_0
    //   414: invokevirtual space : (F)Lcom/badlogic/gdx/scenes/scene2d/ui/HorizontalGroup;
    //   417: pop
    //   418: aload #8
    //   420: iload_2
    //   421: invokevirtual wrap : (Z)Lcom/badlogic/gdx/scenes/scene2d/ui/HorizontalGroup;
    //   424: pop
    //   425: aload #8
    //   427: fconst_0
    //   428: invokevirtual wrapSpace : (F)Lcom/badlogic/gdx/scenes/scene2d/ui/HorizontalGroup;
    //   431: pop
    //   432: aload #8
    //   434: iload_1
    //   435: iconst_1
    //   436: ior
    //   437: invokevirtual align : (I)Lcom/badlogic/gdx/scenes/scene2d/ui/HorizontalGroup;
    //   440: pop
    //   441: aload #8
    //   443: invokevirtual getClass : ()Ljava/lang/Class;
    //   446: ldc 'rowAlign'
    //   448: iconst_1
    //   449: anewarray java/lang/Class
    //   452: dup
    //   453: iconst_0
    //   454: getstatic java/lang/Integer.TYPE : Ljava/lang/Class;
    //   457: aastore
    //   458: invokevirtual getMethod : (Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;
    //   461: aload #8
    //   463: iconst_1
    //   464: anewarray java/lang/Object
    //   467: dup
    //   468: iconst_0
    //   469: iload_1
    //   470: iconst_1
    //   471: ior
    //   472: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   475: aastore
    //   476: invokevirtual invoke : (Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;
    //   479: pop
    //   480: goto -> 484
    //   483: pop
    //   484: new java/util/ArrayList
    //   487: dup
    //   488: invokespecial <init> : ()V
    //   491: astore #9
    //   493: new java/lang/StringBuilder
    //   496: dup
    //   497: invokespecial <init> : ()V
    //   500: astore #10
    //   502: iconst_0
    //   503: istore #11
    //   505: iload #11
    //   507: aload #7
    //   509: invokevirtual length : ()I
    //   512: if_icmpge -> 748
    //   515: aload #7
    //   517: iload #11
    //   519: invokevirtual charAt : (I)C
    //   522: dup
    //   523: istore #12
    //   525: bipush #10
    //   527: if_icmpne -> 586
    //   530: aload #10
    //   532: invokevirtual length : ()I
    //   535: ifle -> 560
    //   538: aload #9
    //   540: aload #10
    //   542: invokevirtual toString : ()Ljava/lang/String;
    //   545: invokestatic a : (Ljava/lang/String;)La/jv;
    //   548: invokeinterface add : (Ljava/lang/Object;)Z
    //   553: pop
    //   554: aload #10
    //   556: iconst_0
    //   557: invokevirtual setLength : (I)V
    //   560: aload #9
    //   562: new a/jv
    //   565: dup
    //   566: getstatic a/jw.d : La/jw;
    //   569: aconst_null
    //   570: iconst_m1
    //   571: invokespecial <init> : (La/jw;Ljava/lang/String;I)V
    //   574: invokeinterface add : (Ljava/lang/Object;)Z
    //   579: pop
    //   580: iinc #11, 1
    //   583: goto -> 505
    //   586: iload #11
    //   588: iconst_2
    //   589: iadd
    //   590: aload #7
    //   592: invokevirtual length : ()I
    //   595: if_icmpge -> 734
    //   598: aload #7
    //   600: iload #11
    //   602: invokevirtual charAt : (I)C
    //   605: sipush #238
    //   608: if_icmpne -> 734
    //   611: aload #7
    //   613: iload #11
    //   615: iconst_1
    //   616: iadd
    //   617: invokevirtual charAt : (I)C
    //   620: sipush #128
    //   623: if_icmpne -> 734
    //   626: getstatic a/in.A : Ljava/util/Map;
    //   629: aload #7
    //   631: iload #11
    //   633: iconst_2
    //   634: iadd
    //   635: invokevirtual charAt : (I)C
    //   638: invokestatic valueOf : (C)Ljava/lang/Character;
    //   641: invokeinterface containsKey : (Ljava/lang/Object;)Z
    //   646: ifeq -> 734
    //   649: aload #10
    //   651: invokevirtual length : ()I
    //   654: ifle -> 679
    //   657: aload #9
    //   659: aload #10
    //   661: invokevirtual toString : ()Ljava/lang/String;
    //   664: invokestatic a : (Ljava/lang/String;)La/jv;
    //   667: invokeinterface add : (Ljava/lang/Object;)Z
    //   672: pop
    //   673: aload #10
    //   675: iconst_0
    //   676: invokevirtual setLength : (I)V
    //   679: aload #9
    //   681: getstatic a/in.A : Ljava/util/Map;
    //   684: aload #7
    //   686: iload #11
    //   688: iconst_2
    //   689: iadd
    //   690: invokevirtual charAt : (I)C
    //   693: invokestatic valueOf : (C)Ljava/lang/Character;
    //   696: invokeinterface get : (Ljava/lang/Object;)Ljava/lang/Object;
    //   701: checkcast java/lang/Integer
    //   704: invokevirtual intValue : ()I
    //   707: istore #12
    //   709: new a/jv
    //   712: dup
    //   713: getstatic a/jw.c : La/jw;
    //   716: aconst_null
    //   717: iload #12
    //   719: invokespecial <init> : (La/jw;Ljava/lang/String;I)V
    //   722: invokeinterface add : (Ljava/lang/Object;)Z
    //   727: pop
    //   728: iinc #11, 3
    //   731: goto -> 505
    //   734: aload #10
    //   736: iload #12
    //   738: invokevirtual append : (C)Ljava/lang/StringBuilder;
    //   741: pop
    //   742: iinc #11, 1
    //   745: goto -> 505
    //   748: aload #10
    //   750: invokevirtual length : ()I
    //   753: ifle -> 772
    //   756: aload #9
    //   758: aload #10
    //   760: invokevirtual toString : ()Ljava/lang/String;
    //   763: invokestatic a : (Ljava/lang/String;)La/jv;
    //   766: invokeinterface add : (Ljava/lang/Object;)Z
    //   771: pop
    //   772: aload #9
    //   774: invokeinterface iterator : ()Ljava/util/Iterator;
    //   779: astore #7
    //   781: aload #7
    //   783: invokeinterface hasNext : ()Z
    //   788: ifeq -> 1139
    //   791: aload #7
    //   793: invokeinterface next : ()Ljava/lang/Object;
    //   798: checkcast a/jv
    //   801: dup
    //   802: astore #9
    //   804: getfield a : La/jw;
    //   807: getstatic a/jw.c : La/jw;
    //   810: if_acmpne -> 960
    //   813: aconst_null
    //   814: astore #10
    //   816: getstatic a/b.c : [Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   819: ifnull -> 853
    //   822: aload #9
    //   824: getfield ep : I
    //   827: iflt -> 853
    //   830: aload #9
    //   832: getfield ep : I
    //   835: getstatic a/b.c : [Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   838: arraylength
    //   839: if_icmpge -> 853
    //   842: getstatic a/b.c : [Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   845: aload #9
    //   847: getfield ep : I
    //   850: aaload
    //   851: astore #10
    //   853: aload #10
    //   855: ifnull -> 957
    //   858: aload #10
    //   860: invokevirtual getTexture : ()Lcom/badlogic/gdx/graphics/Texture;
    //   863: ifnull -> 957
    //   866: aload #10
    //   868: invokevirtual getTexture : ()Lcom/badlogic/gdx/graphics/Texture;
    //   871: getstatic com/badlogic/gdx/graphics/Texture$TextureFilter.Nearest : Lcom/badlogic/gdx/graphics/Texture$TextureFilter;
    //   874: dup
    //   875: invokevirtual setFilter : (Lcom/badlogic/gdx/graphics/Texture$TextureFilter;Lcom/badlogic/gdx/graphics/Texture$TextureFilter;)V
    //   878: aload #10
    //   880: invokevirtual getTexture : ()Lcom/badlogic/gdx/graphics/Texture;
    //   883: getstatic com/badlogic/gdx/graphics/Texture$TextureWrap.ClampToEdge : Lcom/badlogic/gdx/graphics/Texture$TextureWrap;
    //   886: dup
    //   887: invokevirtual setWrap : (Lcom/badlogic/gdx/graphics/Texture$TextureWrap;Lcom/badlogic/gdx/graphics/Texture$TextureWrap;)V
    //   890: new com/badlogic/gdx/scenes/scene2d/ui/Image
    //   893: dup
    //   894: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   897: dup
    //   898: aload #10
    //   900: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   903: invokespecial <init> : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   906: dup
    //   907: astore #9
    //   909: getstatic com/badlogic/gdx/utils/Scaling.fit : Lcom/badlogic/gdx/utils/Scaling;
    //   912: invokevirtual setScaling : (Lcom/badlogic/gdx/utils/Scaling;)V
    //   915: new com/badlogic/gdx/scenes/scene2d/ui/Container
    //   918: dup
    //   919: aload #9
    //   921: invokespecial <init> : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   924: dup
    //   925: astore #11
    //   927: fload_3
    //   928: invokevirtual size : (F)Lcom/badlogic/gdx/scenes/scene2d/ui/Container;
    //   931: pop
    //   932: aload #11
    //   934: iconst_1
    //   935: invokevirtual align : (I)Lcom/badlogic/gdx/scenes/scene2d/ui/Container;
    //   938: pop
    //   939: aload #11
    //   941: fconst_2
    //   942: invokevirtual padLeft : (F)Lcom/badlogic/gdx/scenes/scene2d/ui/Container;
    //   945: fconst_2
    //   946: invokevirtual padRight : (F)Lcom/badlogic/gdx/scenes/scene2d/ui/Container;
    //   949: pop
    //   950: aload #8
    //   952: aload #11
    //   954: invokevirtual addActor : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   957: goto -> 781
    //   960: aload #9
    //   962: getfield a : La/jw;
    //   965: getstatic a/jw.b : La/jw;
    //   968: if_acmpne -> 1136
    //   971: aload #9
    //   973: getfield aG : Ljava/lang/String;
    //   976: astore #10
    //   978: iconst_0
    //   979: istore #9
    //   981: iconst_0
    //   982: istore #11
    //   984: iload #11
    //   986: aload #10
    //   988: invokevirtual length : ()I
    //   991: if_icmpge -> 1080
    //   994: aload #10
    //   996: iload #11
    //   998: invokevirtual charAt : (I)C
    //   1001: bipush #32
    //   1003: if_icmpne -> 1074
    //   1006: new com/badlogic/gdx/scenes/scene2d/ui/Label
    //   1009: dup
    //   1010: iload #11
    //   1012: iload #9
    //   1014: if_icmple -> 1031
    //   1017: aload #10
    //   1019: iload #9
    //   1021: iload #11
    //   1023: iconst_1
    //   1024: iadd
    //   1025: invokevirtual substring : (II)Ljava/lang/String;
    //   1028: goto -> 1033
    //   1031: ldc ' '
    //   1033: aload #4
    //   1035: invokespecial <init> : (Ljava/lang/CharSequence;Lcom/badlogic/gdx/scenes/scene2d/ui/Label$LabelStyle;)V
    //   1038: dup
    //   1039: astore #9
    //   1041: getstatic a/in.bN : F
    //   1044: invokevirtual setFontScale : (F)V
    //   1047: aload #9
    //   1049: iconst_0
    //   1050: invokevirtual setWrap : (Z)V
    //   1053: aload #9
    //   1055: getstatic com/badlogic/gdx/scenes/scene2d/Touchable.disabled : Lcom/badlogic/gdx/scenes/scene2d/Touchable;
    //   1058: invokevirtual setTouchable : (Lcom/badlogic/gdx/scenes/scene2d/Touchable;)V
    //   1061: aload #8
    //   1063: aload #9
    //   1065: invokevirtual addActor : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   1068: iload #11
    //   1070: iconst_1
    //   1071: iadd
    //   1072: istore #9
    //   1074: iinc #11, 1
    //   1077: goto -> 984
    //   1080: iload #9
    //   1082: aload #10
    //   1084: invokevirtual length : ()I
    //   1087: if_icmpge -> 1136
    //   1090: new com/badlogic/gdx/scenes/scene2d/ui/Label
    //   1093: dup
    //   1094: aload #10
    //   1096: iload #9
    //   1098: invokevirtual substring : (I)Ljava/lang/String;
    //   1101: aload #4
    //   1103: invokespecial <init> : (Ljava/lang/CharSequence;Lcom/badlogic/gdx/scenes/scene2d/ui/Label$LabelStyle;)V
    //   1106: dup
    //   1107: astore #11
    //   1109: getstatic a/in.bN : F
    //   1112: invokevirtual setFontScale : (F)V
    //   1115: aload #11
    //   1117: iconst_0
    //   1118: invokevirtual setWrap : (Z)V
    //   1121: aload #11
    //   1123: getstatic com/badlogic/gdx/scenes/scene2d/Touchable.disabled : Lcom/badlogic/gdx/scenes/scene2d/Touchable;
    //   1126: invokevirtual setTouchable : (Lcom/badlogic/gdx/scenes/scene2d/Touchable;)V
    //   1129: aload #8
    //   1131: aload #11
    //   1133: invokevirtual addActor : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)V
    //   1136: goto -> 781
    //   1139: aload #5
    //   1141: aload #8
    //   1143: invokevirtual add : (Lcom/badlogic/gdx/scenes/scene2d/Actor;)Lcom/badlogic/gdx/scenes/scene2d/ui/Cell;
    //   1146: invokevirtual growX : ()Lcom/badlogic/gdx/scenes/scene2d/ui/Cell;
    //   1149: invokevirtual row : ()V
    //   1152: iinc #6, 1
    //   1155: goto -> 390
    //   1158: aload #5
    //   1160: areturn
    // Exception table:
    //   from	to	target	type
    //   441	480	483	java/lang/Exception
  }
  
  public static jm a(cq paramcq) {
    return new jm(paramcq);
  }
  
  public static void cd() {
    if (!t() || n == null || A == null || a == null || bk)
      return; 
    float f1 = n.getWidth();
    float f2 = n.getHeight();
    if (e != null)
      e.setSize(f1, f2); 
    if (bj) {
      f3 = f1 * 0.95F;
      f4 = f2 * 0.9F;
    } else {
      float f9 = (((ju)a).bZ > 0.0F) ? ((ju)a).bZ : (800.0F * bM);
      float f10 = 600.0F * bL;
      f3 = Math.min(f9, f1 * 0.95F);
      f4 = Math.min(f10, f2 * 0.95F);
    } 
    bQ = Math.max(150.0F, f3 - (bj ? (bO * 2.0F) : 20.0F) - 30.0F);
    float f5 = A.getPrefWidth();
    float f6 = A.getPrefHeight();
    boolean bool1 = (((ju)a).F != null) ? (((ju)a).F.size() - a(((ju)a).F)) : false;
    boolean bool2 = (((ju)a).G != null) ? ((ju)a).G.size() : false;
    boolean bool3 = (((ju)a).I == null || ((ju)a).I.isEmpty()) ? true : false;
    boolean bool4 = (((ju)a).H == null || ((ju)a).H.isEmpty()) ? true : false;
    boolean bool5 = (((ju)a).aE == null || ((ju)a).aE.trim().isEmpty()) ? true : false;
    bool5 = (((ju)a).b != null && !((ju)a).b.bu && bool3 && bool4 && bool5 && !bool1 && !bool2) ? true : false;
    bool1 = (((ju)a).aF != null && !((ju)a).aF.isEmpty() && bool3 && bool4 && !bool2 && !bool1) ? true : false;
    bool1 = (bool5 || bool1) ? true : false;
    float f7 = bj ? (f1 * 0.9F) : 450.0F;
    float f8 = bj ? (f2 * 0.75F) : 220.0F;
    float f3 = Math.round(bool1 ? Math.min(f3, Math.max(f7, f5)) : f3);
    float f4 = Math.round(bool1 ? Math.min(f4, Math.max(f8, f6)) : f4);
    A.setSize(f3, f4);
    f1 = Math.round((f1 - f3) * 0.5F);
    f2 = Math.round((f2 - f4) * 0.5F);
    A.clearActions();
    A.setPosition(f1, f2);
    A.invalidateHierarchy();
  }
  
  static List a() {
    ArrayList<jk> arrayList = new ArrayList();
    if (a == null)
      return arrayList; 
    if ((x != null && x.isVisible())) {
      Iterator<jk> iterator = ((ju)a).F.iterator();
      while (iterator.hasNext()) {
        jk jk;
        if ((jk = iterator.next()).bn && (((ju)a).bz || jk.ef == ec))
          arrayList.add(jk); 
      } 
      return arrayList;
    } 
    if (((ju)a).G != null && !((ju)a).G.isEmpty()) {
      Iterator<jr> iterator = ((ju)a).G.iterator();
      while (iterator.hasNext()) {
        jr jr;
        if ((jr = iterator.next()).em != 2) {
          int i = a(((ju)a).F, jr.el);
          if (jr.l != null || i > 0 || jr.em == 3 || jr.em == 5 || jr.em == 4)
            arrayList.add(jr); 
        } 
      } 
    } 
    if (arrayList.isEmpty() && ((ju)a).F != null) {
      Iterator<jk> iterator = ((ju)a).F.iterator();
      while (iterator.hasNext()) {
        jk jk;
        if (!(jk = iterator.next()).bn)
          arrayList.add(jk); 
      } 
    } 
    return arrayList;
  }
  
  static void ce() {
    if (a == null)
      return; 
    if (((ju)a).G != null) {
      Iterator<jr> iterator = ((ju)a).G.iterator();
      while (iterator.hasNext()) {
        jr jr;
        if ((jr = iterator.next()).D != null)
          a(jr.D, jr.em, false); 
      } 
    } 
    if (((ju)a).F != null) {
      Iterator<jk> iterator = ((ju)a).F.iterator();
      while (iterator.hasNext()) {
        jk jk;
        if ((jk = iterator.next()).D != null)
          a(jk.D, 0, false); 
      } 
    } 
    if (b != null && b.g() != null) {
      a(b.g(), b.o(), true);
      return;
    } 
    if (a != null && a.g() != null)
      a(a.g(), 1, false); 
  }
  
  static void an(int paramInt) {
    List<?> list;
    if ((list = a()).isEmpty())
      return; 
    int i;
    if ((i = list.indexOf(a)) == -1) {
      i = (paramInt > 0) ? 0 : (list.size() - 1);
    } else {
      if ((i += paramInt) < 0)
        i = list.size() - 1; 
      if (i >= list.size())
        i = 0; 
    } 
    a = (js)list.get(i);
    ce();
    if (a.g() != null)
      for (Group group = a.g().getParent(); group != null; group = group.getParent()) {
        if (group instanceof ScrollPane) {
          ((ScrollPane)group).scrollTo(a.g().getX(), a.g().getY(), a.g().getWidth(), a.g().getHeight());
          return;
        } 
      }  
  }
  
  public static void a(Stage paramStage, ju paramju) {
    float f5;
    Table table3;
    cf();
    n = paramStage;
    a = (js)paramju;
    boolean bool2 = (Gdx.app.getType() == Application.ApplicationType.Android) ? true : false;
    boolean bool3 = (paramStage.getHeight() > paramStage.getWidth()) ? true : false;
    bj = (bool2 || bool3);
    bP = 1.0F;
    if (bj) {
      float f = bool3 ? 1920.0F : 1080.0F;
      bP = Math.max(0.4F, Math.min(1.0F, paramStage.getHeight() / f));
    } 
    bN = bj ? (2.0F * bP) : 1.0F;
    bO = bj ? (24.0F * bP) : 8.0F;
    float f1 = paramju.l.bP;
    float f2 = bj ? paramju.l.am : 1.0F;
    f2 = f1 * f2;
    f1 = (paramju.ca > 0.0F && paramju.ca != f1) ? paramju.ca : f2;
    (c = new ScrollPane.ScrollPaneStyle()).vScroll = (Drawable)new NinePatchDrawable((NinePatch)b.b);
    c.vScrollKnob = (Drawable)new NinePatchDrawable((NinePatch)b.c);
    float f16 = bj ? 25.0F : 20.0F;
    if (c.vScroll instanceof BaseDrawable)
      ((BaseDrawable)c.vScroll).setMinWidth(f16); 
    if (c.vScrollKnob instanceof BaseDrawable) {
      ((BaseDrawable)c.vScrollKnob).setMinWidth(f16);
      ((BaseDrawable)c.vScrollKnob).setMinHeight(f16 + 10.0F);
    } 
    (l = new Group()).setTouchable(Touchable.enabled);
    paramStage.addActor((Actor)l);
    l.toFront();
    f2 = paramStage.getWidth();
    float f3 = paramStage.getHeight();
    e = null;
    if (paramju.bB) {
      cj();
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(bk)))).setSize(f2, f3);
      image.setColor(0.0F, 0.0F, 0.0F, 0.0F);
      image.setTouchable(Touchable.enabled);
      image.addListener((EventListener)new iz());
      l.addActor((Actor)image);
      image.addAction((Action)Actions.color(new Color(0.0F, 0.0F, 0.0F, 0.55F), 0.12F, Interpolation.smooth));
      e = (Actor)image;
    } 
    if (bj) {
      f4 = f2 * 0.95F;
      f5 = f3 * 0.9F;
    } else {
      float f17 = (paramju.bZ > 0.0F) ? paramju.bZ : (800.0F * bM);
      float f18 = 600.0F * bL;
      f4 = Math.min(f17, f2 * 0.95F);
      f5 = Math.min(f18, f3 * 0.95F);
    } 
    bQ = Math.max(150.0F, f4 - (bj ? (bO * 2.0F) : 20.0F) - 30.0F);
    Table table1;
    (table1 = new Table()).top();
    if (b.d != null) {
      table1.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.d));
    } else {
      Pixmap pixmap;
      (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.DARK_GRAY);
      pixmap.fill();
      table1.setBackground((Drawable)new TextureRegionDrawable(new TextureRegion(new Texture(pixmap))));
    } 
    float f6 = bj ? 8.0F : 10.0F;
    l.addActor((Actor)table1);
    float f7 = bj ? cq.b() : paramju.l.ae;
    Table table2 = new Table();
    if (b.f != null)
      table2.setBackground((Drawable)new NinePatchDrawable((NinePatch)b.f)); 
    table2.pad(0.0F);
    boolean bool5 = (paramju.F != null && !paramju.F.isEmpty() && a(paramju.F) > 0) ? true : false;
    bool5 = (paramju.n != null || bool5) ? true : false;
    float f8 = bj ? (f7 * 0.8F) : (f7 * 1.02F);
    float f9 = 0.71875F;
    if (b.f != null)
      f9 = b.f.getWidth() / Math.max(1.0F, b.f.getHeight()); 
    f9 = f8 * f9;
    float f10 = bj ? 15.0F : -4.0F;
    if (bool5) {
      TextureRegion textureRegion1 = a((Texture)b.c);
      TextureRegion textureRegion2 = a((Texture)b.d);
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)new TextureRegionDrawable(textureRegion1);
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(textureRegion2);
      ImageButton imageButton;
      (imageButton = new ImageButton(imageButtonStyle)).getImage().setScaling(Scaling.fit);
      imageButton.getImageCell().pad(0.0F).expand().fill();
      imageButton.addListener((EventListener)new jc(paramju));
      z = (Table)imageButton;
      imageButton.setVisible((paramju.n != null));
      table2.add((Actor)imageButton).size(f9, f8).left().padLeft(f10);
    } else {
      Actor actor1;
      (actor1 = new Actor()).setTouchable(Touchable.disabled);
      table2.add(actor1).size(f9, f8).left().padLeft(f10);
    } 
    Actor actor = a(paramju.aD, 1, true);
    table2.add(actor).expand().fill().center().minWidth(0.0F);
    if (paramju.bA) {
      TextureRegion textureRegion1 = a((Texture)b.f);
      TextureRegion textureRegion2 = a((Texture)b.g);
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).imageUp = (Drawable)new TextureRegionDrawable(textureRegion1);
      imageButtonStyle.imageDown = (Drawable)new TextureRegionDrawable(textureRegion2);
      ImageButton imageButton;
      (imageButton = new ImageButton(imageButtonStyle)).getImage().setScaling(Scaling.fit);
      imageButton.getImageCell().pad(0.0F).expand().fill();
      imageButton.addListener((EventListener)new jd(paramju));
      table2.add((Actor)imageButton).size(f9, f8).right().padRight(f10);
    } else {
      Actor actor1;
      (actor1 = new Actor()).setTouchable(Touchable.disabled);
      table2.add(actor1).size(f9, f8).right().padRight(f10);
    } 
    float f11 = 0.0F;
    Table table4 = null;
    v = null;
    boolean bool4 = false;
    if (paramju.b != null) {
      if (((jx)paramju.b).aH != null && !((jx)paramju.b).aH.trim().isEmpty())
        bool4 = true; 
      if (((jx)paramju.b).aI != null && !((jx)paramju.b).aI.trim().isEmpty())
        bool4 = true; 
      if (((jx)paramju.b).aJ != null && !((jx)paramju.b).aJ.trim().isEmpty())
        bool4 = true; 
    } 
    if (bool4) {
      f11 = (bj ? (cq.c() * bP) : paramju.l.ae) * 0.65F;
      table4 = new Table();
      if (b.a != null)
        table4.setBackground((Drawable)b.a); 
      f9 = bj ? bO : 8.0F;
      f10 = bj ? 2.0F : 3.0F;
      table4.pad(f10, f9, f10, f9);
      if (paramju.bx && paramju.by) {
        Actor actor1 = a(((jx)paramju.b).aH, 8);
        Actor actor2 = a(((jx)paramju.b).aI, 1);
        Actor actor3 = a(((jx)paramju.b).aJ, 16);
        table4.add(actor1).left().expandX().fillX().minWidth(0.0F);
        table4.add(actor2).center().expandX().fillX().minWidth(0.0F);
        table4.add(actor3).right().expandX().fillX().minWidth(0.0F);
      } else if (!paramju.bx && paramju.by) {
        Actor actor1 = a(((jx)paramju.b).aH, 8);
        Actor actor2 = a(((jx)paramju.b).aJ, 16);
        table4.add(actor1).left().expandX().fillX().minWidth(0.0F);
        table4.add(actor2).right().padLeft(10.0F).minWidth(0.0F);
      } else if (paramju.bx && !paramju.by) {
        Actor actor1 = a(((jx)paramju.b).aH, 8);
        Actor actor2 = a(((jx)paramju.b).aI, 1);
        table4.add(actor1).left().expandX().fillX().minWidth(0.0F);
        table4.add(actor2).center().expandX().fillX().minWidth(0.0F);
      } else {
        Actor actor1 = a(((jx)paramju.b).aH, 8);
        table4.add(actor1).left().expandX().fillX().minWidth(0.0F);
      } 
      v = table4;
    } 
    float f12 = f1;
    f8 = bj ? f1 : paramju.l.ae;
    Container container = null;
    if (paramju.b != null && paramju.b.bu) {
      float f18 = f12;
      ju ju1 = paramju;
      float f19 = bj ? 12.0F : 6.0F;
      float f20 = bj ? bO : 8.0F;
      Table table10;
      (table10 = new Table()).pad(f19, f20, f19, f20);
      String str = (ju1.b.aw != null) ? ju1.b.aw : "";
      BitmapFont bitmapFont = b.a((ju1.b.ax != null) ? ju1.b.ax : "");
      float f21 = bj ? 2.0F : 1.0F;
      float f22 = Math.max(14.0F, bitmapFont.getLineHeight() * 0.8F);
      Pixmap pixmap1;
      (pixmap1 = new Pixmap(bj ? 3 : 2, (int)f22, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
      pixmap1.fill();
      Texture texture1 = new Texture(pixmap1);
      pixmap1.dispose();
      a(texture1);
      TextureRegionDrawable textureRegionDrawable1 = new TextureRegionDrawable(new TextureRegion(texture1));
      Pixmap pixmap2;
      (pixmap2 = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(1.0F, 1.0F, 1.0F, 0.35F);
      pixmap2.fill();
      Texture texture2 = new Texture(pixmap2);
      pixmap2.dispose();
      a(texture2);
      TextureRegionDrawable textureRegionDrawable2 = new TextureRegionDrawable(new TextureRegion(texture2));
      TextField.TextFieldStyle textFieldStyle2 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null);
      TextField.TextFieldStyle textFieldStyle1 = new TextField.TextFieldStyle(bitmapFont, Color.WHITE, (Drawable)textureRegionDrawable1, (Drawable)textureRegionDrawable2, null);
      boolean bool9;
      if (bool9 = (ju1.b.bt && !ju1.b.bs) ? true : false) {
      
      } else {
      
      } 
      TextField textField2;
      (textField2 = new TextField((ju1.b.ax != null) ? ju1.b.ax : "", textFieldStyle2)).setPasswordMode(ju1.b.bs);
      textField2.setPasswordCharacter('*');
      if (ju1.b.ek > 0)
        textField2.setMaxLength(ju1.b.ek); 
      Label label;
      (label = new Label(str, new Label.LabelStyle(bitmapFont, new Color(1.0F, 1.0F, 1.0F, 0.5F)))).setEllipsis(true);
      label.setTouchable(Touchable.disabled);
      byte b1 = bool9 ? 10 : 8;
      label.setAlignment(b1);
      (container = new Container((Actor)label)).align(b1);
      label.addAction(new ji(label, textField2));
      Stack stack;
      (stack = new Stack()).add((Actor)container);
      stack.add((Actor)textField2);
      ip ip;
      (ip = new ip(stack, f21)).setTransform(true);
      ip.setScale(f21);
      ip.setOrigin(12);
      ip.addActor((Actor)stack);
      Table table8;
      (table8 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.z));
      table8.setClip(true);
      f10 = bj ? 16.0F : 8.0F;
      table8.pad(f10);
      table8.add((Actor)ip).grow().left();
      j = textField2;
      textField2.addListener((EventListener)new iq(textField2, textFieldStyle1, textFieldStyle2, table8));
      table8.setTouchable(Touchable.enabled);
      table8.setName("INPUT_WRAPPER");
      Runnable runnable1 = ju1.b.j;
      Table table9 = table8;
      TextField textField1 = textField2;
      Stage stage1 = n;
      cr cr = (cr)Gdx.app.getApplicationListener();
      if (Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS) {
        textField1.setTouchable(Touchable.disabled);
        table9.setTouchable(Touchable.enabled);
        table9.addListener((EventListener)new ja(cr, textField1, stage1, runnable1));
      } 
      textField2.addListener((EventListener)new ir(textField2, bool9, ju1));
      if (!bool9) {
        textField2.setTextFieldListener((paramTextField, paramChar) -> {
              if (paramChar == '\r' || paramChar == '\n') {
                if (n != null) {
                  n.setKeyboardFocus(null);
                  Gdx.input.setOnscreenKeyboardVisible(false);
                } 
                if (paramju.b.j != null)
                  paramju.b.j.run(); 
                g(null);
              } 
            });
      } else if (textField2 instanceof TextArea) {
        ((TextArea)textField2).setPrefRows(6.0F);
      } 
      if (l != null)
        l.addListener((EventListener)new is()); 
      float f17 = (bj && !bool9) ? Math.max(130.0F, f18) : f18;
      if (bj && !bool9) {
        table10.add((Actor)table8).growX().height(f17);
      } else {
        table10.add((Actor)table8).grow().minHeight(f18 * 0.9F);
      } 
      table10.pack();
      table3 = table10;
    } 
    ArrayList arrayList = (paramju.I != null) ? new ArrayList(paramju.I) : new ArrayList();
    List<?> list = (paramju.H != null) ? new ArrayList(paramju.H) : new ArrayList();
    byte b = (paramju.aE != null && !paramju.aE.trim().isEmpty()) ? 1 : 0;
    boolean bool = paramju.bC;
    f1 = (b || bool) ? (bj ? (cq.c() * bP * 0.65F) : (paramju.l.ae * 0.65F)) : 0.0F;
    int i = (paramju.F != null) ? paramju.F.size() : 0;
    int j = a(paramju.F);
    i -= j;
    j = (paramju.G != null) ? paramju.G.size() : 0;
    if (arrayList.isEmpty() && !list.isEmpty()) {
      arrayList = (ArrayList)list;
      list = Collections.emptyList();
    } 
    Table table5 = null;
    Float float_1 = null;
    if (!arrayList.isEmpty()) {
      Table table;
      (table = new Table()).top();
      table.defaults().growX().pad(0.0F).space(bj ? 4.0F : 6.0F);
      Iterator<jl> iterator1 = arrayList.iterator();
      while (iterator1.hasNext()) {
        float f17 = f8;
        int k = jl.eg;
        jl jl;
        String str = (jl = iterator1.next()).as;
        float f18 = bj ? bO : 8.0F;
        Table table9;
        a(table9 = new Table(), k, false);
        table9.setTouchable(Touchable.disabled);
        table9.pad(0.0F, f18, 0.0F, f18);
        Actor actor1 = a((str != null) ? str : "", 8, true);
        table9.add(actor1).expandX().fillX().left().minHeight(f17);
        Table table8 = table9;
        table.add((Actor)table8).growX().row();
      } 
      ScrollPane scrollPane;
      (scrollPane = new ScrollPane((Actor)table, c)).setScrollingDisabled(true, false);
      scrollPane.setFadeScrollBars(false);
      scrollPane.setForceScroll(false, false);
      scrollPane.setFlickScroll(true);
      scrollPane.setCancelTouchFocus(false);
      scrollPane.setOverscroll(false, true);
      (table5 = new Table()).add((Actor)scrollPane).grow();
      if (j > 0) {
        float f17 = 8.0F * f8;
        float f18 = f5 * 0.5F;
        float_1 = Float.valueOf(Math.min(Math.max(f12, f17), f18));
      } 
    } 
    boolean bool7 = (j == 0 && i > 0 && !b && arrayList.isEmpty() && list.isEmpty() && !bool4) ? true : false;
    if (bool4 && !bj)
      bool7 = false; 
    Table table6 = null;
    Float float_2 = null;
    if (bool7) {
      Table table;
      (table = new Table()).top();
      table.defaults().growX().pad(0.0F).space(0.0F);
      Iterator<jk> iterator1 = paramju.F.iterator();
      while (iterator1.hasNext()) {
        jk jk;
        if (!(jk = iterator1.next()).bn) {
          Table table8 = a(jk, f8);
          table.add((Actor)table8).growX().height(f8).row();
        } 
      } 
      ScrollPane scrollPane;
      (scrollPane = new ScrollPane((Actor)table, c)).setScrollingDisabled(true, false);
      scrollPane.setFadeScrollBars(false);
      scrollPane.setForceScroll(false, false);
      scrollPane.setFlickScroll(true);
      scrollPane.setCancelTouchFocus(false);
      scrollPane.setOverscroll(false, true);
      (table6 = new Table()).top();
      table6.add((Actor)scrollPane).grow();
      if (j > 0) {
        b = bj ? 4 : 3;
        float_2 = Float.valueOf(Math.min(i * f8, Math.min(f5 * 0.35F, b * f8)));
      } 
    } 
    Table table7;
    (table7 = new Table()).top();
    table7.defaults().growX().pad(0.0F).space(bj ? 2.0F : 0.0F);
    Iterator<jr> iterator = paramju.G.iterator();
    while (iterator.hasNext()) {
      jr jr1;
      float f18 = (((jr1 = iterator.next()).H != null || (jr1.d != null && jr1.e != null) || jr1.b != null)) ? f12 : f8;
      float f20 = f18;
      jr jr2 = jr1;
      float f21 = bj ? 0.0F : 8.0F;
      Table table9 = new Table();
      jr2.D = table9;
      a(table9, 0, false);
      table9.setTouchable(Touchable.enabled);
      table9.pad(0.0F, f21, 0.0F, 1.1F);
      Actor actor1 = a((jr2.aA != null) ? jr2.aA : "", 8, true);
      float f22 = bj ? bO : 8.0F;
      float f23 = f20;
      table9.add(actor1).expandX().fillX().left().padLeft(f22).minHeight(f23);
      ImageButton.ImageButtonStyle imageButtonStyle;
      (imageButtonStyle = new ImageButton.ImageButtonStyle()).up = (Drawable)b.a;
      imageButtonStyle.checked = (Drawable)b.b;
      ImageButton imageButton;
      (imageButton = new ImageButton(imageButtonStyle)).setChecked(jr2.bw);
      imageButton.setTouchable(Touchable.disabled);
      float f17;
      f21 = (f17 = imageButtonStyle.up.getMinHeight()) * 2.5F;
      float f25 = f23 * 0.8F;
      float f26 = Math.max(1.0F, f25 / f17);
      imageButton.setSize(f21, f17);
      imageButton.setTransform(true);
      imageButton.setOrigin(0.0F, 0.0F);
      imageButton.setScale(f26);
      WidgetGroup widgetGroup1;
      (widgetGroup1 = new WidgetGroup()).addActor((Actor)imageButton);
      float f28 = f21 * f26;
      f26 = f17 * f26;
      table9.add((Actor)widgetGroup1).size(f28, f26).right().padRight(0.0F);
      f17 = Math.max(10.0F, f20 * 0.25F);
      Runnable runnable2 = () -> {
          boolean bool = !paramImageButton.isChecked() ? true : false;
          paramImageButton.setChecked(bool);
          al.a(4);
          if (paramjr.b != null)
            paramjr.b.accept(Boolean.valueOf(bool)); 
        };
      jr2.f = runnable2;
      table9.addListener((EventListener)new jo(runnable2, table9, 0, f17));
      a(table9, jr2);
      table9.pack();
      f20 = f18;
      float f19 = f17;
      f21 = bj ? 0.0F : 8.0F;
      table9 = new Table();
      f19.D = table9;
      a(table9, 0, false);
      table9.setTouchable(Touchable.enabled);
      table9.pad(0.0F, f21, 0.0F, 1.1F);
      actor1 = a((f19.aA != null) ? f19.aA : "", 8, true);
      f22 = bj ? bO : 8.0F;
      f23 = f20;
      table9.add(actor1).expandX().fillX().left().padLeft(f22).minHeight(f23);
      String str = (f19.c != null && f19.c.length > 0) ? f19.c[f19.en] : "";
      TextButton.TextButtonStyle textButtonStyle;
      (textButtonStyle = new TextButton.TextButtonStyle()).font = b.a(str);
      textButtonStyle.up = (Drawable)new NinePatchDrawable((NinePatch)b.m);
      textButtonStyle.down = (Drawable)new NinePatchDrawable((b.n != null) ? (NinePatch)b.n : (NinePatch)b.m);
      TextButton textButton;
      (textButton = new TextButton(str, textButtonStyle)).getLabel().setAlignment(1);
      textButton.getLabel().setWrap(false);
      textButton.getLabel().setEllipsis("...");
      textButton.setTouchable(Touchable.disabled);
      float f24 = (f21 = (b.a != null) ? b.a.getMinHeight() : textButtonStyle.up.getMinHeight()) * 2.5F;
      f26 = f23 * 0.8F;
      float f27 = Math.max(1.0F, f26 / f21);
      textButton.setSize(f24, f21);
      textButton.setTransform(true);
      textButton.setOrigin(0.0F, 0.0F);
      textButton.setScale(f27);
      textButton.getLabel().setFontScale(bN / f27);
      WidgetGroup widgetGroup2;
      (widgetGroup2 = new WidgetGroup()).addActor((Actor)textButton);
      f26 = f24 * f27;
      f21 *= f27;
      table9.add((Actor)widgetGroup2).size(f26, f21).right().padRight(0.0F);
      f24 = Math.max(10.0F, f20 * 0.25F);
      Runnable runnable1 = () -> {
          if (paramjr.c == null || paramjr.c.length == 0)
            return; 
          paramjr.en = (paramjr.en + 1) % paramjr.c.length;
          String str = paramjr.c[paramjr.en];
          paramTextButtonStyle.font = b.a(str);
          paramTextButton.setStyle((Button.ButtonStyle)paramTextButtonStyle);
          paramTextButton.setText(str);
          al.a(4);
          if (paramjr.d != null)
            paramjr.d.accept(Integer.valueOf(paramjr.en)); 
        };
      f19.f = runnable1;
      table9.addListener((EventListener)new jo(runnable1, table9, 0, f24));
      a(table9, f19);
      table9.pack();
      Table table8 = (jr1.em == 3) ? table9 : ((f17.em == 4) ? b(f17, f18) : ((f17.em == 5) ? table9 : ((paramju.b != null) ? a((jr)textButton, f18, paramju.bx, paramju.by) : a((jr)textButton, f18))));
      table7.add((Actor)table8).growX().minHeight(f18).row();
    } 
    ScrollPane scrollPane1;
    (scrollPane1 = new ScrollPane((Actor)table7, c)).setScrollingDisabled(true, false);
    scrollPane1.setFadeScrollBars(false);
    scrollPane1.setScrollbarsOnTop(false);
    scrollPane1.setForceScroll(false, false);
    scrollPane1.setFlickScroll(true);
    scrollPane1.setCancelTouchFocus(false);
    scrollPane1.setOverscroll(false, true);
    (y = new Table()).top();
    y.defaults().growX().pad(0.0F).space(0.0F);
    ScrollPane scrollPane2;
    (scrollPane2 = new ScrollPane((Actor)y, c)).setFadeScrollBars(false);
    scrollPane2.setScrollingDisabled(true, false);
    scrollPane2.setForceScroll(false, false);
    scrollPane2.setFlickScroll(true);
    scrollPane2.setCancelTouchFocus(false);
    scrollPane2.setOverscroll(false, true);
    (x = new Table()).top();
    x.defaults().growX().space(0.0F).pad(0.0F);
    x.add((Actor)scrollPane2).grow().row();
    x.setVisible(false);
    (w = new Table()).add((Actor)scrollPane1).grow();
    (c = (ScrollPane.ScrollPaneStyle)new Stack()).add((Actor)w);
    c.add((Actor)x);
    t = null;
    if ((f1 > 0.0F || !list.isEmpty() || (i > 0 && !bool7) || paramju.b != null)) {
      (t = new Table()).top();
      t.defaults().growX().space(0.0F).pad(0.0F);
      float f = bj ? (cq.c() * bP * 0.65F) : (paramju.l.ae * 0.65F);
      boolean bool9 = (f1 == 0.0F && i > 0 && !bool7) ? true : false;
      if (f1 > 0.0F || bool9) {
        Table table;
        float f17 = (f1 > 0.0F) ? f1 : f;
        if (f1 > 0.0F) {
          boolean bool10 = bool;
          float f18 = f17;
          String str = paramju.aE;
          Table table8 = new Table();
          if (!bool10)
            if (b.b != null) {
              table8.setBackground((Drawable)b.b);
            } else if (b.a != null) {
              table8.setBackground((Drawable)b.a);
            }  
          float f19 = bj ? (bool10 ? 6.0F : 12.0F) : (bool10 ? 3.0F : 4.0F);
          float f20 = bj ? bO : 8.0F;
          table8.pad(f19, f20, f19, f20);
          boolean bool11 = bool10 ? true : true;
          boolean bool12 = bool10;
          Actor actor1 = a((str == null) ? "" : str, bool11, bool12);
          if (bool10) {
            table8.add(actor1).expandX().fillX().left().top();
          } else {
            if (actor1 instanceof Label)
              ((Label)actor1).setEllipsis(true); 
            table8.add(actor1).expandX().fillX().center().minWidth(0.0F);
          } 
          table8.setHeight(f18);
          z = table8;
          table = table8;
        } else {
          table = new Table();
        } 
        t.add((Actor)table).growX().height(f17).row();
      } 
      if (!list.isEmpty()) {
        Table table;
        (table = new Table()).top();
        table.defaults().growX().pad(0.0F).space(0.0F);
        Iterator<?> iterator1 = list.iterator();
        while (iterator1.hasNext()) {
          f16 = f8;
          int k = jl.eg;
          jl jl;
          String str = (jl = (jl)iterator1.next()).as;
          float f17 = bj ? bO : 8.0F;
          Table table9;
          a(table9 = new Table(), k, false);
          table9.setTouchable(Touchable.disabled);
          table9.pad(0.0F, f17, 0.0F, f17);
          Actor actor1 = a((str != null) ? str : "", 8, true);
          table9.add(actor1).expandX().fillX().left().minHeight(f16);
          table9.pack();
          Table table8 = table9;
          table.add((Actor)table8).growX().row();
        } 
        ScrollPane scrollPane;
        (scrollPane = new ScrollPane((Actor)table, c)).setFadeScrollBars(false);
        scrollPane.setScrollingDisabled(true, false);
        scrollPane.setForceScroll(false, false);
        scrollPane.setFlickScroll(true);
        scrollPane.setCancelTouchFocus(false);
        scrollPane.setOverscroll(false, true);
        f = Math.max(f12, Math.min(f5 * 0.35F, 4.0F * f8));
        t.add((Actor)scrollPane).growX().height(f).row();
      } 
      if (i > 0 && !bool7) {
        Table table;
        (table = new Table()).top();
        table.defaults().growX().pad(0.0F).space(bj ? 2.0F : 0.0F);
        Iterator<jk> iterator1 = paramju.F.iterator();
        while (iterator1.hasNext()) {
          jk jk;
          if (!(jk = iterator1.next()).bn) {
            Table table8 = a(jk, f8);
            table.add((Actor)table8).growX().height(f8).row();
          } 
        } 
        ScrollPane scrollPane;
        (scrollPane = new ScrollPane((Actor)table, c)).setScrollingDisabled(true, false);
        scrollPane.setFadeScrollBars(false);
        scrollPane.setForceScroll(false, false);
        scrollPane.setFlickScroll(true);
        scrollPane.setCancelTouchFocus(false);
        scrollPane.setOverscroll(false, true);
        byte b1 = bj ? 4 : 3;
        f = Math.min(i * f8, Math.min(f5 * 0.35F, b1 * f8));
        t.add((Actor)scrollPane).growX().height(f).row();
      } 
      if (paramju.b != null) {
        Table table = a(paramju.b, f8);
        t.add((Actor)table).growX().row();
      } 
    } 
    boolean bool8 = (paramju.b != null && !paramju.b.bu && arrayList.isEmpty() && list.isEmpty() && f1 == 0.0F && i == 0 && j == 0) ? true : false;
    boolean bool6 = (paramju.aF != null && !paramju.aF.isEmpty() && arrayList.isEmpty() && list.isEmpty() && j == 0 && i == 0) ? true : false;
    bool6 = (bool8 || bool6) ? true : false;
    float f13 = f6;
    if (bj && !bool6)
      if (paramju.b != null && paramju.b.bu) {
        f13 = Math.max(f6, f5 * 0.24F);
      } else if (i > 0 && !bool7) {
        f13 = Math.max(f6, f5 * 0.12F);
      }  
    table1.pad(f6, f6, f13, f6);
    A = table1;
    table1.add((Actor)table2).growX().minHeight(f7).row();
    if (table4 != null) {
      float f = f11;
      Table table = table4;
      table1.add((Actor)table).growX().height(new je(table, f)).row();
    } 
    if (table3 != null)
      if (paramju.b.bt && !paramju.b.bs) {
        table1.add((Actor)table3).growX().height(f5 * 0.4F).row();
      } else {
        table1.add((Actor)table3).growX().row();
      }  
    if (table5 != null)
      if (float_1 != null) {
        table1.add((Actor)table5).growX().height(float_1.floatValue()).row();
      } else {
        table1.add((Actor)table5).grow().row();
      }  
    if (table6 != null)
      if (float_2 != null) {
        table1.add((Actor)table6).growX().height(float_2.floatValue()).row();
      } else {
        table1.add((Actor)table6).grow().row();
      }  
    if (paramju.aF != null && !paramju.aF.isEmpty())
      table1.add((Actor)a(paramju.aF)).grow().row(); 
    if (j > 0 || paramju.aF == null || paramju.aF.isEmpty())
      table1.add((Actor)c).grow().row(); 
    if (t != null)
      table1.add((Actor)t).growX().bottom().row(); 
    bI = f12;
    bJ = f8;
    table1.pack();
    float f14 = table1.getPrefWidth();
    float f15 = table1.getPrefHeight();
    f1 = bj ? (f2 * 0.9F) : 450.0F;
    f6 = bj ? (f3 * 0.75F) : 220.0F;
    f1 = Math.round(bool6 ? Math.min(f4, Math.max(f1, f14)) : f4);
    float f4 = Math.round(bool6 ? Math.min(f5, Math.max(f6, f15)) : f5);
    table1.setSize(f1, f4);
    table1.invalidateHierarchy();
    table1.validate();
    f1 = Math.round((f2 - f1) * 0.5F);
    f3 = Math.round((f3 - f4) * 0.5F);
    table1.setPosition(Math.round(f2), f3);
    al.a(1);
    table1.addAction((Action)Actions.moveTo(f1, f3, 0.18F, Interpolation.smooth));
    A = table1;
    bk = false;
    l.addAction(new jf(paramStage));
    l.addCaptureListener((EventListener)new jg(paramju, paramStage));
    if (paramju.b != null && j != null) {
      paramStage.setKeyboardFocus((Actor)j);
    } else {
      paramStage.setKeyboardFocus((Actor)l);
    } 
    paramStage.setScrollFocus((Actor)scrollPane1);
    boolean bool1 = (paramju.b != null && paramju.b.az != null) ? true : false;
    Runnable runnable = () -> {
        if (paramju.o != null) {
          g(paramju.o);
          return;
        } 
        if (paramBoolean) {
          if (paramju.b.k != null)
            paramju.b.k.run(); 
          g(null);
          return;
        } 
      };
    Group group = l;
    Stage stage;
    if ((stage = paramStage) == null || group == null)
      return; 
    stage.setKeyboardFocus((Actor)group);
    group.addCaptureListener((EventListener)new iy(runnable));
  }
  
  public static void g(Runnable paramRunnable) {
    if (l == null || bk)
      return; 
    bk = true;
    al.a(2);
    float f = (n != null) ? n.getHeight() : Gdx.graphics.getHeight();
    if (A != null)
      A.addAction((Action)Actions.moveTo(A.getX(), f, 0.2F, Interpolation.smooth)); 
    i(paramRunnable);
  }
  
  public static void h(Runnable paramRunnable) {
    if (l == null || bk)
      return; 
    bk = true;
    al.a(2);
    if (A != null)
      A.addAction((Action)Actions.moveTo(-A.getWidth(), A.getY(), 0.2F, Interpolation.smooth)); 
    i(paramRunnable);
  }
  
  public static void cf() {
    if (e != null)
      e.clearActions(); 
    if (A != null)
      A.clearActions(); 
    if (l != null)
      l.remove(); 
    z = null;
    l = null;
    A = null;
    e = null;
    j = null;
    z = null;
    bk = false;
    a = null;
    b = null;
    ed = -1;
    ee = -1;
    bK = 0.0F;
    bi = false;
    bj = false;
    bN = 1.0F;
    bO = 8.0F;
    bP = 1.0F;
    if (!A.isEmpty()) {
      for (Texture texture : A) {
        try {
          if (texture != null)
            texture.dispose(); 
        } catch (Throwable throwable) {}
      } 
      A.clear();
    } 
    if (n != null) {
      n.setKeyboardFocus((Actor)n.getRoot());
      n.setScrollFocus(null);
    } 
  }
  
  public static void cg() {
    g(null);
  }
  
  private static Table a(String paramString) {
    float f1 = bj ? 15.0F : 10.0F;
    float f2 = bj ? 15.0F : 12.0F;
    Table table2;
    (table2 = new Table()).pad(f1, f2, f1, f2);
    Actor actor = a((paramString != null) ? paramString : "", 1, true);
    table2.add(actor).expand().fill().center();
    Table table1;
    (table1 = new Table()).add((Actor)table2).expand().center().growX();
    return table1;
  }
  
  private static TextButton a(String paramString, Runnable paramRunnable) {
    TextButton.TextButtonStyle textButtonStyle;
    (textButtonStyle = new TextButton.TextButtonStyle()).font = b.a((paramString != null) ? paramString : "");
    textButtonStyle.up = (Drawable)new NinePatchDrawable((NinePatch)b.m);
    textButtonStyle.down = (Drawable)new NinePatchDrawable((b.n != null) ? (NinePatch)b.n : (NinePatch)b.m);
    textButtonStyle.over = textButtonStyle.up;
    TextButton textButton = new TextButton((paramString != null) ? paramString : "", textButtonStyle);
    if (bj) {
      textButton.pad(24.0F, 24.0F, 24.0F, 24.0F);
    } else {
      textButton.pad(8.0F, 20.0F, 8.0F, 20.0F);
    } 
    textButton.getLabel().setAlignment(1);
    textButton.getLabel().setWrap(false);
    textButton.getLabel().setFontScale(bN);
    textButton.addListener((EventListener)new jh(paramRunnable));
    return textButton;
  }
  
  private static Table a(jq paramjq, float paramFloat) {
    TextButton textButton;
    Table table = new Table();
    float f = bj ? 24.0F : 10.0F;
    table.pad(f);
    paramFloat = bj ? Math.max(paramFloat * 0.9F, cq.b()) : 44.0F;
    f = bj ? 16.0F : 15.0F;
    boolean bool = (paramjq.az != null) ? true : false;
    if (bj) {
      if (bool) {
        TextButton textButton1 = a(paramjq.az, () -> {
              if (paramjq.k != null)
                paramjq.k.run(); 
              g(null);
            });
        table.add((Actor)textButton1).expandX().fillX().height(paramFloat).padRight(f);
      } 
      textButton = a((paramjq.ay != null) ? paramjq.ay : "Ok", () -> {
            if (paramjq.j != null)
              paramjq.j.run(); 
            g(null);
          });
      table.add((Actor)textButton).expandX().fillX().height(paramFloat);
    } else {
      if (textButton != null) {
        textButton = a(paramjq.az, () -> {
              if (paramjq.k != null)
                paramjq.k.run(); 
              g(null);
            });
        table.add((Actor)textButton).left().height(paramFloat).minWidth(120.0F).padRight(f);
      } else {
        table.add().left().height(paramFloat).minWidth(120.0F).padRight(f);
      } 
      table.add().expandX().fillX().height(paramFloat);
      textButton = a((paramjq.ay != null) ? paramjq.ay : "Ok", () -> {
            if (paramjq.j != null)
              paramjq.j.run(); 
            g(null);
          });
      table.add((Actor)textButton).right().height(paramFloat).minWidth(120.0F);
    } 
    return table;
  }
  
  public static String e() {
    return (j != null) ? j.getText() : "";
  }
  
  private static NinePatchDrawable a(int paramInt, boolean paramBoolean) {
    try {
      if (paramInt == 1) {
        if (paramBoolean && b.k != null)
          return new NinePatchDrawable(b.k); 
        if (b.j != null)
          return new NinePatchDrawable(b.j); 
      } else if (paramBoolean && b.i != null) {
        return new NinePatchDrawable((NinePatch)b.i);
      } 
    } catch (Throwable throwable) {}
    return new NinePatchDrawable((NinePatch)b.h);
  }
  
  static void a(Table paramTable, int paramInt, boolean paramBoolean) {
    paramTable.setBackground((Drawable)a(paramInt, paramBoolean));
    if (paramInt == 2) {
      paramTable.setColor(1.0F, 1.0F, 1.0F, 0.55F);
      return;
    } 
    paramTable.setColor(1.0F, 1.0F, 1.0F, 1.0F);
  }
  
  private static void ao(int paramInt) {
    a = null;
    b = null;
    if (y != null && a != null) {
      ec = paramInt;
      y.clearChildren();
      if (((ju)a).bz) {
        Iterator<jk> iterator = ((ju)a).F.iterator();
        while (iterator.hasNext()) {
          jk jk;
          if ((jk = iterator.next()).bn) {
            Table table = a(jk, bJ);
            y.add((Actor)table).growX().height(bJ).row();
          } 
        } 
      } else {
        Iterator<jk> iterator = ((ju)a).F.iterator();
        while (iterator.hasNext()) {
          jk jk;
          if ((jk = iterator.next()).bn && jk.ef == paramInt) {
            Table table = a(jk, bJ);
            y.add((Actor)table).growX().height(bJ).row();
          } 
        } 
      } 
      y.invalidateHierarchy();
    } 
    if (w != null)
      w.setVisible(false); 
    if (x != null)
      x.setVisible(true); 
    if (v != null)
      v.setVisible(false); 
    if (t != null)
      t.setVisible(false); 
    if (z != null && a != null && ((ju)a).n == null)
      z.setVisible(true); 
    if (A != null)
      A.invalidateHierarchy(); 
  }
  
  static void ch() {
    a = null;
    b = null;
    if (w != null)
      w.setVisible(true); 
    if (x != null)
      x.setVisible(false); 
    if (v != null)
      v.setVisible(true); 
    if (t != null)
      t.setVisible(true); 
    ec = -1;
    if (z != null && a != null && ((ju)a).n == null)
      z.setVisible(false); 
    if (A != null)
      A.invalidateHierarchy(); 
  }
  
  private static int a(List paramList, int paramInt) {
    if (paramList == null)
      return 0; 
    if (a != null && ((ju)a).bz) {
      byte b1 = 0;
      iterator = paramList.iterator();
      while (iterator.hasNext()) {
        if (((jk)iterator.next()).bn)
          b1++; 
      } 
      return b1;
    } 
    byte b = 0;
    Iterator<jk> iterator = iterator.iterator();
    while (iterator.hasNext()) {
      jk jk;
      if ((jk = iterator.next()).bn && jk.ef == paramInt)
        b++; 
    } 
    return b;
  }
  
  private static jk a(List paramList, int paramInt) {
    jk jk1;
    if (paramList == null)
      return null; 
    if (a != null && ((ju)a).bz) {
      if (paramList == null)
        return null; 
      jk1 = null;
      iterator = paramList.iterator();
      while (iterator.hasNext()) {
        jk jk;
        if ((jk = iterator.next()).bn) {
          if (jk1 != null)
            return null; 
          jk1 = jk;
        } 
      } 
      return jk1;
    } 
    jk jk2 = null;
    Iterator<jk> iterator = iterator.iterator();
    while (iterator.hasNext()) {
      jk jk;
      if ((jk = iterator.next()).bn && jk.ef == jk1) {
        if (jk2 != null)
          return null; 
        jk2 = jk;
      } 
    } 
    return jk2;
  }
  
  private static int a(List paramList) {
    if (paramList == null)
      return 0; 
    byte b = 0;
    Iterator iterator = paramList.iterator();
    while (iterator.hasNext()) {
      if (((jk)iterator.next()).bn)
        b++; 
    } 
    return b;
  }
  
  static void ci() {
    ec = -1;
    if (t != null)
      t.setVisible(true); 
    if (u != null)
      u.setVisible(false); 
  }
  
  public static int n() {
    return ec;
  }
  
  private static void a(Table paramTable, jr paramjr) {
    if (paramjr.ar != null && !paramjr.ar.isEmpty())
      paramTable.addCaptureListener((EventListener)new it(paramjr)); 
  }
  
  private static void a(Table paramTable, jk paramjk) {
    if (paramjk.ar != null && !paramjk.ar.isEmpty())
      paramTable.addCaptureListener((EventListener)new iu(paramjk)); 
  }
  
  static void C(String paramString) {
    if (z == null)
      return; 
    z.clearChildren();
    Actor actor = a((paramString == null) ? "" : paramString, 8, true);
    z.add(actor).expandX().fillX().left().top();
  }
  
  private static Table a(jk paramjk, float paramFloat) {
    float f2 = bj ? 0.0F : 8.0F;
    Table table = new Table();
    paramjk.D = table;
    a(table, 0, false);
    table.setTouchable(Touchable.enabled);
    table.pad(0.0F, f2, 0.0F, f2);
    if (!bj && paramjk.aq != null && !paramjk.aq.isEmpty()) {
      Label.LabelStyle labelStyle = new Label.LabelStyle(b.a(paramjk.aq), Color.WHITE);
      iv iv;
      (iv = new iv(paramjk.aq, labelStyle)).setAlignment(8);
      iv.setFontScale(bN * 0.9F);
      table.add((Actor)iv).padLeft(8.0F).width(20.0F).left();
    } 
    Actor actor = a((paramjk.ap != null) ? paramjk.ap : "", 1, true);
    table.add(actor).expandX().fillX().center().minHeight(paramFloat);
    if (paramjk.e != null && b.m != null) {
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(b.m)))).setScaling(Scaling.fit);
      float f3 = bj ? (bN * 1.5F) : 1.0F;
      float f4 = 9.0F * f3;
      f3 = 23.0F * f3;
      float f5 = bj ? 16.0F : 4.0F;
      table.add((Actor)image).size(f4, f3).padRight(f5).padLeft(8.0F).right();
    } 
    float f1 = Math.max(10.0F, paramFloat * 0.25F);
    Runnable runnable = () -> {
        al.a(3);
        if (paramjk.e != null)
          paramjk.e.run(); 
        if (paramjk.bm)
          g(null); 
      };
    paramjk.f = runnable;
    table.addListener((EventListener)new jo(runnable, table, 0, f1));
    a(table, paramjk);
    table.pack();
    return table;
  }
  
  private static Table a(jr paramjr, float paramFloat) {
    float f1 = bj ? 0.0F : 8.0F;
    Table table = new Table();
    paramjr.D = table;
    a(table, paramjr.em, false);
    table.setTouchable(Touchable.enabled);
    table.pad(0.0F, f1, 0.0F, f1);
    Image image;
    boolean bool = ((image = (Image)((paramjr.b != null) ? a((jn)paramjr.b) : a((Integer)paramjr.d, paramjr.e, paramjr.H))) != null) ? true : false;
    float f2 = e();
    float f3 = bool ? Math.max(paramFloat, f2) : paramFloat;
    if (bool)
      a(table, image, f2); 
    Actor actor = a((paramjr.aA != null) ? paramjr.aA : "", 8, true);
    f2 = bj ? bO : 8.0F;
    table.add(actor).expandX().fillX().left().minHeight(f3).padRight(f2).padLeft(bool ? 0.0F : f2);
    int i = a((a != null) ? ((ju)a).F : null, paramjr.el);
    if ((((paramjr.l != null || i > 0) && paramjr.em != 2)) && b.m != null) {
      Image image1;
      (image1 = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(b.m)))).setScaling(Scaling.fit);
      float f = bj ? (bN * 1.5F) : 1.0F;
      f2 = 9.0F * f;
      f = 23.0F * f;
      f3 = bj ? 16.0F : 4.0F;
      table.add((Actor)image1).size(f2, f).padRight(f3).padLeft(8.0F).right();
    } 
    Runnable runnable = () -> {
        if (paramjr.em == 2)
          return; 
        int i;
        if ((i = a((a != null) ? ((ju)a).F : null, paramjr.el)) <= 0) {
          al.a(3);
          if (paramjr.l != null) {
            paramjr.l.run();
            if (paramjr.bv)
              g(null); 
          } 
          return;
        } 
        if (i == 1) {
          jk jk = a(((ju)a).F, paramjr.el);
          ec = paramjr.el;
          if (jk != null && jk.e != null)
            jk.e.run(); 
          if (jk != null && jk.bm)
            g(null); 
          return;
        } 
        ao(paramjr.el);
      };
    paramjr.f = runnable;
    table.addListener((EventListener)new jo(runnable, table, paramjr.em, Math.max(10.0F, paramFloat * 0.25F)));
    a(table, paramjr);
    table.pack();
    return table;
  }
  
  private static Table a(jr paramjr, float paramFloat, boolean paramBoolean1, boolean paramBoolean2) {
    float f1 = bj ? 0.0F : 8.0F;
    Table table2 = new Table();
    paramjr.D = table2;
    a(table2, paramjr.em, false);
    table2.setTouchable(Touchable.enabled);
    table2.pad(0.0F, f1, 0.0F, f1);
    Image image;
    boolean bool = ((image = (Image)((paramjr.b != null) ? a((jn)paramjr.b) : a((Integer)paramjr.d, paramjr.e, paramjr.H))) != null) ? true : false;
    float f2 = e();
    float f3 = bool ? Math.max(paramFloat, f2) : paramFloat;
    if (bool)
      a(table2, image, f2); 
    Table table1;
    (table1 = new Table()).setTouchable(Touchable.disabled);
    Actor actor1 = a((paramjr.aA != null) ? paramjr.aA : "", 8, true);
    Actor actor2 = paramBoolean1 ? a((paramjr.aB != null) ? paramjr.aB : "", 1, false) : null;
    Actor actor3 = paramBoolean2 ? a((paramjr.aC != null) ? paramjr.aC : "", 16, false) : null;
    if (actor2 instanceof Label)
      ((Label)actor2).setEllipsis(true); 
    if (actor3 instanceof Label)
      ((Label)actor3).setEllipsis(true); 
    float f4 = bj ? bO : 0.0F;
    if (bj)
      table1.padLeft(bool ? 0.0F : f4).padRight(f4); 
    if (paramBoolean1 && paramBoolean2) {
      table1.add(actor1).left().expandX().fillX();
      table1.add(actor2).center().expandX().fillX().minWidth(0.0F);
      table1.add(actor3).right().expandX().fillX().minWidth(0.0F);
    } else if (!paramBoolean1 && paramBoolean2) {
      table1.add(actor1).left().expandX().fillX();
      table1.add(actor3).right().padLeft(10.0F).minWidth(0.0F);
    } else if (paramBoolean1 && !paramBoolean2) {
      table1.add(actor1).left().expandX().fillX();
      table1.add(actor2).center().expandX().fillX().minWidth(0.0F);
    } else {
      table1.add(actor1).left().expandX().fillX();
    } 
    table2.add((Actor)table1).expand().fill().minHeight(f3);
    int i = a((a != null) ? ((ju)a).F : null, paramjr.el);
    if ((((paramjr.l != null || i > 0) && paramjr.em != 2)) && b.m != null) {
      Image image1;
      (image1 = new Image((Drawable)new TextureRegionDrawable(new TextureRegion(b.m)))).setScaling(Scaling.fit);
      float f5 = bj ? (bN * 1.5F) : 1.0F;
      float f6 = 9.0F * f5;
      f5 = 23.0F * f5;
      float f7 = bj ? 16.0F : 4.0F;
      table2.add((Actor)image1).size(f6, f5).padRight(f7).padLeft(8.0F).right();
    } 
    Runnable runnable = () -> {
        if (paramjr.em == 2)
          return; 
        int i;
        if ((i = a((a != null) ? ((ju)a).F : null, paramjr.el)) <= 0) {
          al.a(3);
          if (paramjr.l != null) {
            paramjr.l.run();
            if (paramjr.bv)
              g(null); 
          } 
          return;
        } 
        if (i == 1) {
          jk jk = a(((ju)a).F, paramjr.el);
          ec = paramjr.el;
          if (jk != null && jk.e != null)
            jk.e.run(); 
          if (jk != null && jk.bm)
            g(null); 
          return;
        } 
        ao(paramjr.el);
      };
    paramjr.f = runnable;
    table2.addListener((EventListener)new jo(runnable, table2, paramjr.em, Math.max(10.0F, paramFloat * 0.25F)));
    a(table2, paramjr);
    table2.pack();
    return table2;
  }
  
  private static void i(Runnable paramRunnable) {
    if (e != null) {
      Color color = e.getColor();
      e.addAction((Action)Actions.color(new Color(color.r, color.g, color.b, 0.0F), 0.2F, Interpolation.smooth));
    } 
    if (l != null)
      l.addAction((Action)Actions.sequence((Action)Actions.delay(0.2F), (Action)Actions.run(() -> {
                cf();
                if (paramRunnable != null)
                  paramRunnable.run(); 
              }))); 
  }
  
  private static void cj() {
    if (bk != null)
      return; 
    Pixmap pixmap;
    (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
    pixmap.fill();
    bk = new Texture(pixmap);
    pixmap.dispose();
  }
  
  static TextureRegion a(Texture paramTexture) {
    if (paramTexture != null)
      return new TextureRegion(paramTexture); 
    cj();
    return new TextureRegion(bk);
  }
  
  private static int d(int paramInt) {
    return ((paramInt &= 0xFFFFFF) == 0) ? 16777215 : paramInt;
  }
  
  private static Image a(jn paramjn) {
    if (paramjn == null)
      return null; 
    try {
      if (lj.i(paramjn.aN))
        return null; 
      if (!(((paramjn.ao | paramjn.ap | paramjn.aq | paramjn.ar) != 0) ? 1 : 0))
        return null; 
      int i = d(paramjn.as);
      int j = d(paramjn.at);
      int k = d(paramjn.au);
      int m = d(paramjn.av);
      int n = d(paramjn.aw);
      bl bl;
      (bl = new bl((a != null && ((ju)a).l != null) ? ((ju)a).l : null)).b(paramjn.am, paramjn.aN, paramjn.ao, paramjn.ap, paramjn.aq, paramjn.ar, i, j, k, m, n);
      Texture texture = bl.b();
      a(texture);
      TextureRegion textureRegion = new TextureRegion(texture);
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable(textureRegion))).setScaling(Scaling.none);
      image.setTouchable(Touchable.disabled);
      return image;
    } catch (Throwable throwable) {
      Gdx.app.error("GameMenuOverlay", "Falha ao renderizar CreatureIconSpec", throwable);
      return null;
    } 
  }
  
  private static Image a(Integer paramInteger1, Integer paramInteger2, TextureRegion paramTextureRegion) {
    // Byte code:
    //   0: aload_2
    //   1: ifnull -> 20
    //   4: new com/badlogic/gdx/scenes/scene2d/ui/Image
    //   7: dup
    //   8: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   11: dup
    //   12: aload_2
    //   13: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   16: invokespecial <init> : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   19: areturn
    //   20: aload_0
    //   21: ifnull -> 28
    //   24: aload_1
    //   25: ifnonnull -> 30
    //   28: aconst_null
    //   29: areturn
    //   30: aload_0
    //   31: invokevirtual intValue : ()I
    //   34: tableswitch default -> 471, 1 -> 68, 2 -> 117, 3 -> 298, 4 -> 167, 5 -> 217
    //   68: getstatic a/b.a : La/ai;
    //   71: ifnull -> 87
    //   74: getstatic a/b.a : La/ai;
    //   77: aload_1
    //   78: invokevirtual intValue : ()I
    //   81: invokevirtual a : (I)La/ah;
    //   84: goto -> 88
    //   87: aconst_null
    //   88: dup
    //   89: astore_2
    //   90: ifnull -> 471
    //   93: new a/jj
    //   96: dup
    //   97: aload_2
    //   98: <illegal opcode> get : (La/ah;)La/jp;
    //   103: aload_2
    //   104: <illegal opcode> get : (La/ah;)La/jt;
    //   109: aload_2
    //   110: invokevirtual a : ()Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   113: invokespecial <init> : (La/jp;La/jt;Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   116: areturn
    //   117: getstatic a/b.a : La/o;
    //   120: ifnull -> 136
    //   123: getstatic a/b.a : La/o;
    //   126: aload_1
    //   127: invokevirtual intValue : ()I
    //   130: invokevirtual a : (I)La/n;
    //   133: goto -> 137
    //   136: aconst_null
    //   137: dup
    //   138: astore_2
    //   139: ifnull -> 471
    //   142: new a/jj
    //   145: dup
    //   146: aload_2
    //   147: <illegal opcode> get : (La/n;)La/jp;
    //   152: aload_2
    //   153: <illegal opcode> get : (La/n;)La/jt;
    //   158: aload_2
    //   159: fconst_0
    //   160: invokevirtual c : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   163: invokespecial <init> : (La/jp;La/jt;Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   166: areturn
    //   167: getstatic a/b.a : La/l;
    //   170: ifnull -> 186
    //   173: getstatic a/b.a : La/l;
    //   176: aload_1
    //   177: invokevirtual intValue : ()I
    //   180: invokevirtual a : (I)La/k;
    //   183: goto -> 187
    //   186: aconst_null
    //   187: dup
    //   188: astore_2
    //   189: ifnull -> 471
    //   192: new a/jj
    //   195: dup
    //   196: aload_2
    //   197: <illegal opcode> get : (La/k;)La/jp;
    //   202: aload_2
    //   203: <illegal opcode> get : (La/k;)La/jt;
    //   208: aload_2
    //   209: fconst_0
    //   210: invokevirtual b : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   213: invokespecial <init> : (La/jp;La/jt;Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   216: areturn
    //   217: getstatic a/b.a : La/h;
    //   220: ifnull -> 236
    //   223: getstatic a/b.a : La/h;
    //   226: aload_1
    //   227: invokevirtual intValue : ()I
    //   230: invokevirtual a : (I)La/g;
    //   233: goto -> 237
    //   236: aconst_null
    //   237: dup
    //   238: astore_2
    //   239: ifnonnull -> 269
    //   242: aload_1
    //   243: invokevirtual intValue : ()I
    //   246: sipush #255
    //   249: iand
    //   250: istore_2
    //   251: getstatic a/b.a : La/h;
    //   254: ifnull -> 267
    //   257: getstatic a/b.a : La/h;
    //   260: iload_2
    //   261: invokevirtual a : (I)La/g;
    //   264: goto -> 268
    //   267: aconst_null
    //   268: astore_2
    //   269: aload_2
    //   270: ifnull -> 471
    //   273: new a/jj
    //   276: dup
    //   277: aload_2
    //   278: <illegal opcode> get : (La/g;)La/jp;
    //   283: aload_2
    //   284: <illegal opcode> get : (La/g;)La/jt;
    //   289: aload_2
    //   290: fconst_0
    //   291: invokevirtual a : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   294: invokespecial <init> : (La/jp;La/jt;Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   297: areturn
    //   298: getstatic a/b.a : La/v;
    //   301: ifnull -> 308
    //   304: aload_1
    //   305: ifnonnull -> 310
    //   308: aconst_null
    //   309: areturn
    //   310: getstatic a/b.a : La/v;
    //   313: aload_1
    //   314: invokevirtual intValue : ()I
    //   317: invokevirtual a : (I)La/t;
    //   320: dup
    //   321: astore_2
    //   322: ifnonnull -> 327
    //   325: aconst_null
    //   326: areturn
    //   327: bipush #13
    //   329: newarray int
    //   331: dup
    //   332: iconst_0
    //   333: iconst_1
    //   334: iastore
    //   335: dup
    //   336: iconst_1
    //   337: iconst_3
    //   338: iastore
    //   339: dup
    //   340: iconst_2
    //   341: iconst_2
    //   342: iastore
    //   343: dup
    //   344: iconst_3
    //   345: iconst_4
    //   346: iastore
    //   347: dup
    //   348: iconst_4
    //   349: iconst_5
    //   350: iastore
    //   351: dup
    //   352: iconst_5
    //   353: bipush #7
    //   355: iastore
    //   356: dup
    //   357: bipush #6
    //   359: bipush #6
    //   361: iastore
    //   362: dup
    //   363: bipush #7
    //   365: bipush #8
    //   367: iastore
    //   368: dup
    //   369: bipush #8
    //   371: bipush #9
    //   373: iastore
    //   374: dup
    //   375: bipush #9
    //   377: bipush #11
    //   379: iastore
    //   380: dup
    //   381: bipush #10
    //   383: bipush #10
    //   385: iastore
    //   386: dup
    //   387: bipush #11
    //   389: bipush #12
    //   391: iastore
    //   392: dup
    //   393: bipush #12
    //   395: bipush #13
    //   397: iastore
    //   398: dup
    //   399: astore_3
    //   400: arraylength
    //   401: pop
    //   402: iconst_0
    //   403: istore #4
    //   405: iload #4
    //   407: bipush #13
    //   409: if_icmpge -> 442
    //   412: aload_3
    //   413: iload #4
    //   415: iaload
    //   416: istore #5
    //   418: aload_2
    //   419: iload #5
    //   421: fconst_0
    //   422: invokevirtual a : (IF)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   425: dup
    //   426: astore #5
    //   428: ifnull -> 436
    //   431: aload #5
    //   433: goto -> 448
    //   436: iinc #4, 1
    //   439: goto -> 405
    //   442: aload_2
    //   443: iconst_1
    //   444: fconst_0
    //   445: invokevirtual a : (IF)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   448: dup
    //   449: astore_2
    //   450: ifnonnull -> 455
    //   453: aconst_null
    //   454: areturn
    //   455: new com/badlogic/gdx/scenes/scene2d/ui/Image
    //   458: dup
    //   459: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   462: dup
    //   463: aload_2
    //   464: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   467: invokespecial <init> : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   470: areturn
    //   471: goto -> 493
    //   474: astore_2
    //   475: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   478: ldc 'GameMenuOverlay'
    //   480: aload_0
    //   481: aload_1
    //   482: <illegal opcode> makeConcatWithConstants : (Ljava/lang/Integer;Ljava/lang/Integer;)Ljava/lang/String;
    //   487: aload_2
    //   488: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   493: aconst_null
    //   494: astore_2
    //   495: aload_0
    //   496: invokevirtual intValue : ()I
    //   499: tableswitch default -> 714, 1 -> 532, 2 -> 572, 3 -> 714, 4 -> 610, 5 -> 648
    //   532: getstatic a/b.a : La/ai;
    //   535: ifnull -> 551
    //   538: getstatic a/b.a : La/ai;
    //   541: aload_1
    //   542: invokevirtual intValue : ()I
    //   545: invokevirtual a : (I)La/ah;
    //   548: goto -> 552
    //   551: aconst_null
    //   552: dup
    //   553: astore_2
    //   554: ifnull -> 567
    //   557: aload_2
    //   558: fconst_0
    //   559: fconst_0
    //   560: fconst_0
    //   561: invokevirtual a : (FFF)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   564: goto -> 568
    //   567: aconst_null
    //   568: astore_2
    //   569: goto -> 714
    //   572: getstatic a/b.a : La/o;
    //   575: ifnull -> 591
    //   578: getstatic a/b.a : La/o;
    //   581: aload_1
    //   582: invokevirtual intValue : ()I
    //   585: invokevirtual a : (I)La/n;
    //   588: goto -> 592
    //   591: aconst_null
    //   592: dup
    //   593: astore_2
    //   594: ifnull -> 605
    //   597: aload_2
    //   598: fconst_0
    //   599: invokevirtual c : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   602: goto -> 606
    //   605: aconst_null
    //   606: astore_2
    //   607: goto -> 714
    //   610: getstatic a/b.a : La/l;
    //   613: ifnull -> 629
    //   616: getstatic a/b.a : La/l;
    //   619: aload_1
    //   620: invokevirtual intValue : ()I
    //   623: invokevirtual a : (I)La/k;
    //   626: goto -> 630
    //   629: aconst_null
    //   630: dup
    //   631: astore_2
    //   632: ifnull -> 643
    //   635: aload_2
    //   636: fconst_0
    //   637: invokevirtual b : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   640: goto -> 644
    //   643: aconst_null
    //   644: astore_2
    //   645: goto -> 714
    //   648: getstatic a/b.a : La/h;
    //   651: ifnull -> 667
    //   654: getstatic a/b.a : La/h;
    //   657: aload_1
    //   658: invokevirtual intValue : ()I
    //   661: invokevirtual a : (I)La/g;
    //   664: goto -> 668
    //   667: aconst_null
    //   668: dup
    //   669: astore_2
    //   670: ifnonnull -> 700
    //   673: aload_1
    //   674: invokevirtual intValue : ()I
    //   677: sipush #255
    //   680: iand
    //   681: istore_2
    //   682: getstatic a/b.a : La/h;
    //   685: ifnull -> 698
    //   688: getstatic a/b.a : La/h;
    //   691: iload_2
    //   692: invokevirtual a : (I)La/g;
    //   695: goto -> 699
    //   698: aconst_null
    //   699: astore_2
    //   700: aload_2
    //   701: ifnull -> 712
    //   704: aload_2
    //   705: fconst_0
    //   706: invokevirtual a : (F)Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   709: goto -> 713
    //   712: aconst_null
    //   713: astore_2
    //   714: aload_2
    //   715: ifnull -> 734
    //   718: new com/badlogic/gdx/scenes/scene2d/ui/Image
    //   721: dup
    //   722: new com/badlogic/gdx/scenes/scene2d/utils/TextureRegionDrawable
    //   725: dup
    //   726: aload_2
    //   727: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;)V
    //   730: invokespecial <init> : (Lcom/badlogic/gdx/scenes/scene2d/utils/Drawable;)V
    //   733: areturn
    //   734: aconst_null
    //   735: areturn
    //   736: astore_2
    //   737: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   740: ldc 'GameMenuOverlay'
    //   742: aload_0
    //   743: aload_1
    //   744: <illegal opcode> makeConcatWithConstants : (Ljava/lang/Integer;Ljava/lang/Integer;)Ljava/lang/String;
    //   749: aload_2
    //   750: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   755: aconst_null
    //   756: areturn
    // Exception table:
    //   from	to	target	type
    //   30	116	474	java/lang/Exception
    //   117	166	474	java/lang/Exception
    //   167	216	474	java/lang/Exception
    //   217	297	474	java/lang/Exception
    //   298	309	474	java/lang/Exception
    //   310	326	474	java/lang/Exception
    //   327	454	474	java/lang/Exception
    //   455	470	474	java/lang/Exception
    //   493	735	736	java/lang/Exception
  }
  
  private static Actor a(String paramString, int paramInt) {
    Actor actor;
    if (actor = a((paramString == null) ? "" : paramString, paramInt, false) instanceof Label)
      ((Label)actor).setEllipsis(true); 
    return actor;
  }
  
  private static Table b(jr paramjr, float paramFloat) {
    NinePatchDrawable ninePatchDrawable1;
    float f1 = bj ? bO : 8.0F;
    Table table = new Table();
    paramjr.D = table;
    paramjr.f = null;
    a(table, 0, false);
    table.setTouchable(Touchable.enabled);
    table.pad(0.0F, f1, 0.0F, f1);
    Actor actor;
    if (actor = a((paramjr.aA != null) ? paramjr.aA : "", 8, false) instanceof Label)
      ((Label)actor).setEllipsis(true); 
    table.add(actor).expandX().fillX().left().padRight(10.0F).minWidth(0.0F);
    if (b.a != null) {
      FreeTypeFontGenerator freeTypeFontGenerator = b.a;
    } else {
      ninePatchDrawable1 = new NinePatchDrawable((NinePatch)b.h);
    } 
    if (ninePatchDrawable1 instanceof BaseDrawable)
      ((BaseDrawable)ninePatchDrawable1).setMinHeight(bj ? 18.0F : 10.0F); 
    NinePatchDrawable ninePatchDrawable2 = new NinePatchDrawable((b.m != null) ? (NinePatch)b.m : (NinePatch)b.h);
    float f3 = bj ? 50.0F : 20.0F;
    ninePatchDrawable2.setMinWidth(f3);
    ninePatchDrawable2.setMinHeight(f3);
    Slider.SliderStyle sliderStyle = new Slider.SliderStyle((Drawable)ninePatchDrawable1, (Drawable)ninePatchDrawable2);
    Slider slider = new Slider(paramjr.bW, paramjr.bX, paramjr.bY, false, sliderStyle);
    float f2 = 0.0F;
    try {
      if (paramjr.a != null)
        f2 = ((Float)paramjr.a.get()).floatValue(); 
    } catch (Throwable throwable) {}
    slider.setValue(f2);
    f2 = bj ? 350.0F : 120.0F;
    paramFloat *= 0.8F;
    table.add((Actor)slider).width(f2).height(paramFloat).padRight(12.0F);
    Label label = lj.a("" + Math.round(slider.getValue() * 100.0F) + "%", Color.WHITE, false, 16);
    table.add((Actor)label).minWidth(50.0F).right();
    slider.addListener((EventListener)new iw(slider, label, paramjr));
    slider.addListener((EventListener)new ix(paramjr));
    a(table, paramjr);
    table.pack();
    return table;
  }
  
  private static float e() {
    float f1 = (a != null && ((ju)a).l != null) ? ((ju)a).l.bP : 32.0F;
    float f2 = bj ? ((a != null && ((ju)a).l != null) ? ((ju)a).l.am : 1.0F) : 1.0F;
    return f1 * f2;
  }
  
  private static void a(Table paramTable, Image paramImage, float paramFloat) {
    float f1 = (a != null && ((ju)a).l != null) ? ((ju)a).l.bP : 32.0F;
    float f2 = bj ? ((a != null && ((ju)a).l != null) ? ((ju)a).l.am : 1.0F) : 1.0F;
    paramImage.setScaling(Scaling.none);
    paramImage.setSize(f1, f1);
    paramImage.setTouchable(Touchable.disabled);
    Group group;
    (group = new Group()).setTransform(true);
    group.setSize(f1, f1);
    group.addActor((Actor)paramImage);
    group.setScale(f2);
    group.setOrigin(1);
    Table table;
    (table = new Table()).defaults().center();
    table.add((Actor)group).size(f1, f1).center();
    f1 = bj ? bO : 0.0F;
    paramTable.add((Actor)table).size(paramFloat, paramFloat).padRight(10.0F).padLeft(f1).center();
  }
  
  public static boolean t() {
    return (l != null);
  }
  
  public static void ck() {
    if (l != null)
      l.toFront(); 
  }
  
  static {
    (A = (Table)new HashMap<>()).put(Character.valueOf('), Integer.valueOf(0));
    A.put(Character.valueOf('), Integer.valueOf(1));
    A.put(Character.valueOf('), Integer.valueOf(2));
    A.put(Character.valueOf('), Integer.valueOf(3));
    A.put(Character.valueOf('), Integer.valueOf(4));
    A.put(Character.valueOf('), Integer.valueOf(5));
    A.put(Character.valueOf('), Integer.valueOf(6));
    A.put(Character.valueOf('), Integer.valueOf(7));
    A.put(Character.valueOf('), Integer.valueOf(8));
    A.put(Character.valueOf('), Integer.valueOf(9));
    A.put(Character.valueOf('), Integer.valueOf(10));
    A.put(Character.valueOf('), Integer.valueOf(11));
    A.put(Character.valueOf('), Integer.valueOf(12));
    A.put(Character.valueOf('), Integer.valueOf(13));
    A.put(Character.valueOf('), Integer.valueOf(14));
    A.put(Character.valueOf('), Integer.valueOf(15));
    A.put(Character.valueOf('), Integer.valueOf(16));
    A.put(Character.valueOf('), Integer.valueOf(17));
    A.put(Character.valueOf('), Integer.valueOf(18));
    A.put(Character.valueOf('), Integer.valueOf(19));
    A.put(Character.valueOf('), Integer.valueOf(20));
    A.put(Character.valueOf('), Integer.valueOf(21));
    A.put(Character.valueOf('), Integer.valueOf(22));
    A.put(Character.valueOf('), Integer.valueOf(23));
  }
}
