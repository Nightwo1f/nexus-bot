package a;

import com.badlogic.gdx.assets.AssetManager;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

public final class ai {
  private final AssetManager i;
  
  private final String m;
  
  private final Map o = new HashMap<>();
  
  private static final Pattern j = Pattern.compile("\\d+");
  
  public ai(AssetManager paramAssetManager, String paramString) {
    this.i = paramAssetManager;
    this.m = paramString;
  }
  
  public final void n() {
    // Byte code:
    //   0: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   3: aload_0
    //   4: getfield m : Ljava/lang/String;
    //   7: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   12: astore_1
    //   13: new com/badlogic/gdx/utils/XmlReader
    //   16: dup
    //   17: invokespecial <init> : ()V
    //   20: astore_2
    //   21: aload_1
    //   22: invokevirtual list : ()[Lcom/badlogic/gdx/files/FileHandle;
    //   25: dup
    //   26: astore_1
    //   27: arraylength
    //   28: istore_3
    //   29: iconst_0
    //   30: istore #4
    //   32: iload #4
    //   34: iload_3
    //   35: if_icmpge -> 1728
    //   38: aload_1
    //   39: iload #4
    //   41: aaload
    //   42: dup
    //   43: astore #5
    //   45: invokevirtual isDirectory : ()Z
    //   48: ifeq -> 1722
    //   51: aload #5
    //   53: invokevirtual name : ()Ljava/lang/String;
    //   56: ldc 'pack'
    //   58: invokevirtual startsWith : (Ljava/lang/String;)Z
    //   61: ifeq -> 1722
    //   64: aload #5
    //   66: ldc 'xml'
    //   68: invokevirtual list : (Ljava/lang/String;)[Lcom/badlogic/gdx/files/FileHandle;
    //   71: dup
    //   72: astore #5
    //   74: arraylength
    //   75: istore #6
    //   77: iconst_0
    //   78: istore #7
    //   80: iload #7
    //   82: iload #6
    //   84: if_icmpge -> 1722
    //   87: aload #5
    //   89: iload #7
    //   91: aaload
    //   92: dup
    //   93: astore #8
    //   95: invokevirtual nameWithoutExtension : ()Ljava/lang/String;
    //   98: astore #9
    //   100: getstatic a/ai.j : Ljava/util/regex/Pattern;
    //   103: aload #9
    //   105: invokevirtual matcher : (Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;
    //   108: invokevirtual matches : ()Z
    //   111: ifeq -> 1716
    //   114: aload #8
    //   116: ldc 'UTF-8'
    //   118: invokevirtual readString : (Ljava/lang/String;)Ljava/lang/String;
    //   121: dup
    //   122: astore #9
    //   124: invokevirtual isEmpty : ()Z
    //   127: ifne -> 149
    //   130: aload #9
    //   132: iconst_0
    //   133: invokevirtual charAt : (I)C
    //   136: ldc 65279
    //   138: if_icmpne -> 149
    //   141: aload #9
    //   143: iconst_1
    //   144: invokevirtual substring : (I)Ljava/lang/String;
    //   147: astore #9
    //   149: aload_2
    //   150: aload #9
    //   152: invokevirtual parse : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   155: dup
    //   156: astore #9
    //   158: ldc 'statics'
    //   160: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   163: dup
    //   164: astore #10
    //   166: ifnull -> 177
    //   169: aload #10
    //   171: invokevirtual getChildCount : ()I
    //   174: ifne -> 180
    //   177: goto -> 1716
    //   180: aload #10
    //   182: ldc 'packid'
    //   184: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   187: istore #11
    //   189: aload_0
    //   190: aload #9
    //   192: iload #11
    //   194: istore #13
    //   196: astore #12
    //   198: astore #9
    //   200: new java/util/HashMap
    //   203: dup
    //   204: invokespecial <init> : ()V
    //   207: astore #14
    //   209: aload #12
    //   211: ldc 'images'
    //   213: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   216: dup
    //   217: astore #12
    //   219: ifnull -> 747
    //   222: new java/util/ArrayList
    //   225: dup
    //   226: invokespecial <init> : ()V
    //   229: astore #15
    //   231: new java/util/ArrayList
    //   234: dup
    //   235: invokespecial <init> : ()V
    //   238: astore #16
    //   240: aload #12
    //   242: ldc 'texture'
    //   244: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   247: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   250: astore #17
    //   252: aload #17
    //   254: invokeinterface hasNext : ()Z
    //   259: ifeq -> 375
    //   262: aload #17
    //   264: invokeinterface next : ()Ljava/lang/Object;
    //   269: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   272: ldc 'file'
    //   274: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   277: astore #19
    //   279: aload #9
    //   281: getfield m : Ljava/lang/String;
    //   284: aload #19
    //   286: iload #13
    //   288: invokestatic a : (Ljava/lang/String;Ljava/lang/String;I)Lcom/badlogic/gdx/files/FileHandle;
    //   291: dup
    //   292: astore #20
    //   294: ifnonnull -> 319
    //   297: new com/badlogic/gdx/utils/GdxRuntimeException
    //   300: dup
    //   301: aload #19
    //   303: iload #13
    //   305: aload #9
    //   307: getfield m : Ljava/lang/String;
    //   310: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   315: invokespecial <init> : (Ljava/lang/String;)V
    //   318: athrow
    //   319: aload #20
    //   321: invokevirtual file : ()Ljava/io/File;
    //   324: invokevirtual getAbsolutePath : ()Ljava/lang/String;
    //   327: astore #21
    //   329: aload #9
    //   331: getfield i : Lcom/badlogic/gdx/assets/AssetManager;
    //   334: aload #21
    //   336: ldc com/badlogic/gdx/graphics/Texture
    //   338: invokevirtual isLoaded : (Ljava/lang/String;Ljava/lang/Class;)Z
    //   341: ifne -> 356
    //   344: aload #9
    //   346: getfield i : Lcom/badlogic/gdx/assets/AssetManager;
    //   349: aload #21
    //   351: ldc com/badlogic/gdx/graphics/Texture
    //   353: invokevirtual load : (Ljava/lang/String;Ljava/lang/Class;)V
    //   356: aload #15
    //   358: aload #21
    //   360: invokevirtual add : (Ljava/lang/Object;)Z
    //   363: pop
    //   364: aload #16
    //   366: aload #20
    //   368: invokevirtual add : (Ljava/lang/Object;)Z
    //   371: pop
    //   372: goto -> 252
    //   375: aload #9
    //   377: getfield i : Lcom/badlogic/gdx/assets/AssetManager;
    //   380: invokevirtual finishLoading : ()V
    //   383: iconst_0
    //   384: istore #17
    //   386: aload #12
    //   388: ldc 'texture'
    //   390: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   393: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   396: astore #18
    //   398: aload #18
    //   400: invokeinterface hasNext : ()Z
    //   405: ifeq -> 747
    //   408: aload #18
    //   410: invokeinterface next : ()Ljava/lang/Object;
    //   415: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   418: astore #19
    //   420: aload #15
    //   422: iload #17
    //   424: iinc #17, 1
    //   427: invokevirtual get : (I)Ljava/lang/Object;
    //   430: checkcast java/lang/String
    //   433: astore #20
    //   435: aload #9
    //   437: getfield i : Lcom/badlogic/gdx/assets/AssetManager;
    //   440: aload #20
    //   442: ldc com/badlogic/gdx/graphics/Texture
    //   444: invokevirtual get : (Ljava/lang/String;Ljava/lang/Class;)Ljava/lang/Object;
    //   447: checkcast com/badlogic/gdx/graphics/Texture
    //   450: astore #21
    //   452: aload #19
    //   454: ldc 't'
    //   456: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   459: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   462: astore #12
    //   464: aload #12
    //   466: invokeinterface hasNext : ()Z
    //   471: ifeq -> 744
    //   474: aload #12
    //   476: invokeinterface next : ()Ljava/lang/Object;
    //   481: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   484: dup
    //   485: astore #13
    //   487: ldc 'id'
    //   489: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   492: istore #16
    //   494: aload #13
    //   496: ldc 's'
    //   498: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   501: ldc ','
    //   503: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   506: dup
    //   507: astore #19
    //   509: iconst_0
    //   510: aaload
    //   511: invokestatic parseInt : (Ljava/lang/String;)I
    //   514: istore #20
    //   516: aload #19
    //   518: iconst_1
    //   519: aaload
    //   520: invokestatic parseInt : (Ljava/lang/String;)I
    //   523: istore #19
    //   525: aload #13
    //   527: ldc 'p'
    //   529: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   532: ldc ','
    //   534: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   537: dup
    //   538: astore #22
    //   540: iconst_0
    //   541: aaload
    //   542: invokestatic parseInt : (Ljava/lang/String;)I
    //   545: istore #23
    //   547: aload #22
    //   549: iconst_1
    //   550: aaload
    //   551: invokestatic parseInt : (Ljava/lang/String;)I
    //   554: istore #22
    //   556: aload #21
    //   558: iload #23
    //   560: iload #22
    //   562: iload #20
    //   564: iload #19
    //   566: istore #24
    //   568: istore #23
    //   570: istore #22
    //   572: istore #20
    //   574: astore #19
    //   576: new com/badlogic/gdx/graphics/g2d/TextureRegion
    //   579: dup
    //   580: aload #19
    //   582: iload #20
    //   584: iload #22
    //   586: iload #23
    //   588: iload #24
    //   590: invokespecial <init> : (Lcom/badlogic/gdx/graphics/Texture;IIII)V
    //   593: astore #25
    //   595: fconst_1
    //   596: aload #19
    //   598: invokevirtual getWidth : ()I
    //   601: i2f
    //   602: fdiv
    //   603: fstore #26
    //   605: fconst_1
    //   606: aload #19
    //   608: invokevirtual getHeight : ()I
    //   611: i2f
    //   612: fdiv
    //   613: fstore #19
    //   615: iload #20
    //   617: i2f
    //   618: ldc 0.1
    //   620: fadd
    //   621: fload #26
    //   623: fmul
    //   624: fstore #27
    //   626: iload #22
    //   628: i2f
    //   629: ldc 0.1
    //   631: fadd
    //   632: fload #19
    //   634: fmul
    //   635: fstore #28
    //   637: iload #20
    //   639: iload #23
    //   641: iadd
    //   642: i2f
    //   643: ldc 0.1
    //   645: fsub
    //   646: fload #26
    //   648: fmul
    //   649: fstore #20
    //   651: iload #22
    //   653: iload #24
    //   655: iadd
    //   656: i2f
    //   657: ldc 0.1
    //   659: fsub
    //   660: fload #19
    //   662: fmul
    //   663: fstore #19
    //   665: aload #25
    //   667: fload #27
    //   669: fload #28
    //   671: fload #20
    //   673: fload #19
    //   675: invokevirtual setRegion : (FFFF)V
    //   678: aload #25
    //   680: astore #19
    //   682: aload #13
    //   684: ldc 'o'
    //   686: ldc '0,0'
    //   688: invokevirtual getAttribute : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   691: ldc ','
    //   693: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   696: dup
    //   697: astore #13
    //   699: iconst_0
    //   700: aaload
    //   701: invokestatic parseInt : (Ljava/lang/String;)I
    //   704: istore #20
    //   706: aload #13
    //   708: iconst_1
    //   709: aaload
    //   710: invokestatic parseInt : (Ljava/lang/String;)I
    //   713: istore #13
    //   715: aload #14
    //   717: iload #16
    //   719: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   722: new a/aj
    //   725: dup
    //   726: aload #19
    //   728: iload #20
    //   730: iload #13
    //   732: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;II)V
    //   735: invokeinterface put : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   740: pop
    //   741: goto -> 464
    //   744: goto -> 398
    //   747: aload #14
    //   749: astore #9
    //   751: aload #10
    //   753: ldc 'x'
    //   755: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   758: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   761: astore #10
    //   763: aload #10
    //   765: invokeinterface hasNext : ()Z
    //   770: ifeq -> 1689
    //   773: aload #10
    //   775: invokeinterface next : ()Ljava/lang/Object;
    //   780: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   783: dup
    //   784: astore #12
    //   786: ldc 'si'
    //   788: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   791: istore #13
    //   793: aload #12
    //   795: ldc 'up'
    //   797: iconst_0
    //   798: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   801: iconst_1
    //   802: if_icmpne -> 809
    //   805: iconst_1
    //   806: goto -> 810
    //   809: iconst_0
    //   810: istore #14
    //   812: aload #12
    //   814: ldc 'sh'
    //   816: iconst_0
    //   817: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   820: iconst_1
    //   821: if_icmpne -> 828
    //   824: iconst_1
    //   825: goto -> 829
    //   828: iconst_0
    //   829: istore #15
    //   831: aload #12
    //   833: ldc 'fo'
    //   835: iconst_0
    //   836: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   839: iconst_1
    //   840: if_icmpne -> 847
    //   843: iconst_1
    //   844: goto -> 848
    //   847: iconst_0
    //   848: istore #16
    //   850: aload #12
    //   852: ldc 'dl'
    //   854: iconst_0
    //   855: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   858: iconst_1
    //   859: if_icmpne -> 866
    //   862: iconst_1
    //   863: goto -> 867
    //   866: iconst_0
    //   867: istore #17
    //   869: aload #12
    //   871: ldc 'mc'
    //   873: iconst_m1
    //   874: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   877: istore #18
    //   879: aload #12
    //   881: ldc 'light'
    //   883: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   886: astore #19
    //   888: iconst_0
    //   889: istore #20
    //   891: aconst_null
    //   892: astore #21
    //   894: aload #19
    //   896: ifnull -> 991
    //   899: aload #19
    //   901: ldc 's'
    //   903: iconst_0
    //   904: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   907: istore #20
    //   909: aload #19
    //   911: ldc 'c'
    //   913: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   916: ldc ','
    //   918: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   921: dup
    //   922: astore #22
    //   924: iconst_0
    //   925: aaload
    //   926: invokestatic parseInt : (Ljava/lang/String;)I
    //   929: i2f
    //   930: ldc 255.0
    //   932: fdiv
    //   933: fstore #23
    //   935: aload #22
    //   937: iconst_1
    //   938: aaload
    //   939: invokestatic parseInt : (Ljava/lang/String;)I
    //   942: i2f
    //   943: ldc 255.0
    //   945: fdiv
    //   946: fstore #24
    //   948: aload #22
    //   950: iconst_2
    //   951: aaload
    //   952: invokestatic parseInt : (Ljava/lang/String;)I
    //   955: i2f
    //   956: ldc 255.0
    //   958: fdiv
    //   959: fstore #19
    //   961: aload #22
    //   963: iconst_3
    //   964: aaload
    //   965: invokestatic parseInt : (Ljava/lang/String;)I
    //   968: i2f
    //   969: ldc 255.0
    //   971: fdiv
    //   972: fstore #25
    //   974: new com/badlogic/gdx/graphics/Color
    //   977: dup
    //   978: fload #23
    //   980: fload #24
    //   982: fload #19
    //   984: fload #25
    //   986: invokespecial <init> : (FFFF)V
    //   989: astore #21
    //   991: aload #12
    //   993: ldc 'a'
    //   995: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   998: astore #19
    //   1000: iconst_0
    //   1001: istore #22
    //   1003: aload #19
    //   1005: ifnull -> 1054
    //   1008: aload #19
    //   1010: ldc 'f'
    //   1012: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   1015: dup
    //   1016: astore #23
    //   1018: getfield size : I
    //   1021: iconst_1
    //   1022: if_icmple -> 1029
    //   1025: iconst_1
    //   1026: goto -> 1030
    //   1029: iconst_0
    //   1030: istore #24
    //   1032: aload #19
    //   1034: ldc 's'
    //   1036: iconst_0
    //   1037: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   1040: iconst_1
    //   1041: if_icmpne -> 1048
    //   1044: iconst_1
    //   1045: goto -> 1049
    //   1048: iconst_0
    //   1049: istore #22
    //   1051: goto -> 1083
    //   1054: aload #12
    //   1056: ldc 'f'
    //   1058: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   1061: dup
    //   1062: astore #23
    //   1064: ifnull -> 1080
    //   1067: aload #23
    //   1069: getfield size : I
    //   1072: iconst_1
    //   1073: if_icmple -> 1080
    //   1076: iconst_1
    //   1077: goto -> 1081
    //   1080: iconst_0
    //   1081: istore #24
    //   1083: new com/badlogic/gdx/utils/Array
    //   1086: dup
    //   1087: invokespecial <init> : ()V
    //   1090: astore #19
    //   1092: new com/badlogic/gdx/utils/Array
    //   1095: dup
    //   1096: invokespecial <init> : ()V
    //   1099: astore #25
    //   1101: iload #24
    //   1103: ifeq -> 1429
    //   1106: new com/badlogic/gdx/utils/Array
    //   1109: dup
    //   1110: invokespecial <init> : ()V
    //   1113: astore #24
    //   1115: new com/badlogic/gdx/utils/Array
    //   1118: dup
    //   1119: invokespecial <init> : ()V
    //   1122: astore #26
    //   1124: aload #23
    //   1126: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   1129: astore #27
    //   1131: aload #27
    //   1133: invokeinterface hasNext : ()Z
    //   1138: ifeq -> 1353
    //   1141: aload #27
    //   1143: invokeinterface next : ()Ljava/lang/Object;
    //   1148: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   1151: dup
    //   1152: astore #28
    //   1154: ldc 'id'
    //   1156: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   1159: istore #12
    //   1161: aload #9
    //   1163: iload #12
    //   1165: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1168: invokeinterface get : (Ljava/lang/Object;)Ljava/lang/Object;
    //   1173: checkcast a/aj
    //   1176: astore #12
    //   1178: aload #19
    //   1180: aload #12
    //   1182: getfield r : Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   1185: invokevirtual add : (Ljava/lang/Object;)V
    //   1188: aload #25
    //   1190: new com/badlogic/gdx/math/Vector2
    //   1193: dup
    //   1194: aload #12
    //   1196: getfield N : I
    //   1199: i2f
    //   1200: aload #12
    //   1202: getfield O : I
    //   1205: i2f
    //   1206: invokespecial <init> : (FF)V
    //   1209: invokevirtual add : (Ljava/lang/Object;)V
    //   1212: aload #28
    //   1214: ldc 'p'
    //   1216: ldc '150'
    //   1218: invokevirtual getAttribute : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   1221: dup
    //   1222: astore #12
    //   1224: ldc ','
    //   1226: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   1229: ifeq -> 1269
    //   1232: aload #12
    //   1234: ldc ','
    //   1236: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   1239: dup
    //   1240: astore #23
    //   1242: iconst_0
    //   1243: aaload
    //   1244: invokestatic parseInt : (Ljava/lang/String;)I
    //   1247: i2f
    //   1248: ldc 1000.0
    //   1250: fdiv
    //   1251: fstore #12
    //   1253: aload #23
    //   1255: iconst_1
    //   1256: aaload
    //   1257: invokestatic parseInt : (Ljava/lang/String;)I
    //   1260: i2f
    //   1261: ldc 1000.0
    //   1263: fdiv
    //   1264: fstore #23
    //   1266: goto -> 1330
    //   1269: aload #12
    //   1271: ldc '-'
    //   1273: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   1276: ifeq -> 1316
    //   1279: aload #12
    //   1281: ldc '-'
    //   1283: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   1286: dup
    //   1287: astore #23
    //   1289: iconst_0
    //   1290: aaload
    //   1291: invokestatic parseInt : (Ljava/lang/String;)I
    //   1294: i2f
    //   1295: ldc 1000.0
    //   1297: fdiv
    //   1298: fstore #12
    //   1300: aload #23
    //   1302: iconst_1
    //   1303: aaload
    //   1304: invokestatic parseInt : (Ljava/lang/String;)I
    //   1307: i2f
    //   1308: ldc 1000.0
    //   1310: fdiv
    //   1311: fstore #23
    //   1313: goto -> 1330
    //   1316: aload #12
    //   1318: invokestatic parseInt : (Ljava/lang/String;)I
    //   1321: i2f
    //   1322: ldc 1000.0
    //   1324: fdiv
    //   1325: dup
    //   1326: fstore #23
    //   1328: fstore #12
    //   1330: aload #24
    //   1332: fload #12
    //   1334: invokestatic valueOf : (F)Ljava/lang/Float;
    //   1337: invokevirtual add : (Ljava/lang/Object;)V
    //   1340: aload #26
    //   1342: fload #23
    //   1344: invokestatic valueOf : (F)Ljava/lang/Float;
    //   1347: invokevirtual add : (Ljava/lang/Object;)V
    //   1350: goto -> 1131
    //   1353: aload #24
    //   1355: getfield size : I
    //   1358: newarray float
    //   1360: astore #12
    //   1362: aload #26
    //   1364: getfield size : I
    //   1367: newarray float
    //   1369: astore #23
    //   1371: iconst_0
    //   1372: istore #27
    //   1374: iload #27
    //   1376: aload #24
    //   1378: getfield size : I
    //   1381: if_icmpge -> 1426
    //   1384: aload #12
    //   1386: iload #27
    //   1388: aload #24
    //   1390: iload #27
    //   1392: invokevirtual get : (I)Ljava/lang/Object;
    //   1395: checkcast java/lang/Float
    //   1398: invokevirtual floatValue : ()F
    //   1401: fastore
    //   1402: aload #23
    //   1404: iload #27
    //   1406: aload #26
    //   1408: iload #27
    //   1410: invokevirtual get : (I)Ljava/lang/Object;
    //   1413: checkcast java/lang/Float
    //   1416: invokevirtual floatValue : ()F
    //   1419: fastore
    //   1420: iinc #27, 1
    //   1423: goto -> 1374
    //   1426: goto -> 1535
    //   1429: aload #23
    //   1431: ifnull -> 1454
    //   1434: aload #23
    //   1436: getfield size : I
    //   1439: ifle -> 1454
    //   1442: aload #23
    //   1444: iconst_0
    //   1445: invokevirtual get : (I)Ljava/lang/Object;
    //   1448: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   1451: goto -> 1455
    //   1454: aconst_null
    //   1455: dup
    //   1456: astore #24
    //   1458: ifnull -> 1517
    //   1461: aload #9
    //   1463: aload #24
    //   1465: ldc 'id'
    //   1467: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   1470: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1473: invokeinterface get : (Ljava/lang/Object;)Ljava/lang/Object;
    //   1478: checkcast a/aj
    //   1481: astore #26
    //   1483: aload #19
    //   1485: aload #26
    //   1487: getfield r : Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   1490: invokevirtual add : (Ljava/lang/Object;)V
    //   1493: aload #25
    //   1495: new com/badlogic/gdx/math/Vector2
    //   1498: dup
    //   1499: aload #26
    //   1501: getfield N : I
    //   1504: i2f
    //   1505: aload #26
    //   1507: getfield O : I
    //   1510: i2f
    //   1511: invokespecial <init> : (FF)V
    //   1514: invokevirtual add : (Ljava/lang/Object;)V
    //   1517: iconst_1
    //   1518: newarray float
    //   1520: dup
    //   1521: iconst_0
    //   1522: fconst_0
    //   1523: fastore
    //   1524: astore #12
    //   1526: iconst_1
    //   1527: newarray float
    //   1529: dup
    //   1530: iconst_0
    //   1531: fconst_0
    //   1532: fastore
    //   1533: astore #23
    //   1535: aload #19
    //   1537: ldc com/badlogic/gdx/graphics/g2d/TextureRegion
    //   1539: invokevirtual toArray : (Ljava/lang/Class;)[Ljava/lang/Object;
    //   1542: checkcast [Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   1545: astore #24
    //   1547: aload #25
    //   1549: getfield size : I
    //   1552: newarray int
    //   1554: astore #26
    //   1556: aload #25
    //   1558: getfield size : I
    //   1561: newarray int
    //   1563: astore #27
    //   1565: iconst_0
    //   1566: istore #28
    //   1568: iload #28
    //   1570: aload #25
    //   1572: getfield size : I
    //   1575: if_icmpge -> 1622
    //   1578: aload #26
    //   1580: iload #28
    //   1582: aload #25
    //   1584: iload #28
    //   1586: invokevirtual get : (I)Ljava/lang/Object;
    //   1589: checkcast com/badlogic/gdx/math/Vector2
    //   1592: getfield x : F
    //   1595: f2i
    //   1596: iastore
    //   1597: aload #27
    //   1599: iload #28
    //   1601: aload #25
    //   1603: iload #28
    //   1605: invokevirtual get : (I)Ljava/lang/Object;
    //   1608: checkcast com/badlogic/gdx/math/Vector2
    //   1611: getfield y : F
    //   1614: f2i
    //   1615: iastore
    //   1616: iinc #28, 1
    //   1619: goto -> 1568
    //   1622: iload #11
    //   1624: bipush #8
    //   1626: ishl
    //   1627: iload #13
    //   1629: ior
    //   1630: istore #28
    //   1632: new a/ah
    //   1635: dup
    //   1636: iload #28
    //   1638: aload #24
    //   1640: aload #12
    //   1642: aload #23
    //   1644: aload #26
    //   1646: aload #27
    //   1648: iload #14
    //   1650: iload #18
    //   1652: iload #15
    //   1654: iload #16
    //   1656: iload #17
    //   1658: iload #20
    //   1660: aload #21
    //   1662: iload #22
    //   1664: invokespecial <init> : (I[Lcom/badlogic/gdx/graphics/g2d/TextureRegion;[F[F[I[IZIZZZILcom/badlogic/gdx/graphics/Color;Z)V
    //   1667: astore #12
    //   1669: aload_0
    //   1670: getfield o : Ljava/util/Map;
    //   1673: iload #28
    //   1675: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1678: aload #12
    //   1680: invokeinterface put : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   1685: pop
    //   1686: goto -> 763
    //   1689: goto -> 1716
    //   1692: astore #9
    //   1694: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   1697: ldc 'TileLoader'
    //   1699: aload #8
    //   1701: invokevirtual path : ()Ljava/lang/String;
    //   1704: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;)Ljava/lang/String;
    //   1709: aload #9
    //   1711: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   1716: iinc #7, 1
    //   1719: goto -> 80
    //   1722: iinc #4, 1
    //   1725: goto -> 32
    //   1728: return
    // Exception table:
    //   from	to	target	type
    //   114	177	1692	java/lang/Exception
    //   180	1689	1692	java/lang/Exception
  }
  
  public final ah a(int paramInt) {
    return (ah)this.o.get(Integer.valueOf(paramInt));
  }
}
