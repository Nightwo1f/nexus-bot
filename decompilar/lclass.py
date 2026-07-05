package a;

import com.badlogic.gdx.assets.AssetManager;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

public final class l {
  private final AssetManager c;
  
  private final String f;
  
  private final Map f = new HashMap<>();
  
  private static final Pattern c = Pattern.compile("\\d+");
  
  public l(AssetManager paramAssetManager, String paramString) {
    this.c = (Pattern)paramAssetManager;
    this.f = (Map)paramString;
  }
  
  public final void h() {
    // Byte code:
    //   0: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   3: aload_0
    //   4: getfield f : Ljava/lang/String;
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
    //   35: if_icmpge -> 1694
    //   38: aload_1
    //   39: iload #4
    //   41: aaload
    //   42: dup
    //   43: astore #5
    //   45: invokevirtual isDirectory : ()Z
    //   48: ifeq -> 1688
    //   51: aload #5
    //   53: invokevirtual name : ()Ljava/lang/String;
    //   56: ldc 'pack'
    //   58: invokevirtual startsWith : (Ljava/lang/String;)Z
    //   61: ifeq -> 1688
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
    //   84: if_icmpge -> 1688
    //   87: aload #5
    //   89: iload #7
    //   91: aaload
    //   92: dup
    //   93: astore #8
    //   95: invokevirtual nameWithoutExtension : ()Ljava/lang/String;
    //   98: astore #9
    //   100: getstatic a/l.c : Ljava/util/regex/Pattern;
    //   103: aload #9
    //   105: invokevirtual matcher : (Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;
    //   108: invokevirtual matches : ()Z
    //   111: ifeq -> 1682
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
    //   158: ldc 'icons'
    //   160: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   163: dup
    //   164: astore #10
    //   166: ifnonnull -> 172
    //   169: goto -> 1682
    //   172: aload #10
    //   174: ldc 'packid'
    //   176: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   179: istore #11
    //   181: aload_0
    //   182: aload #9
    //   184: iload #11
    //   186: istore #13
    //   188: astore #12
    //   190: astore #9
    //   192: new java/util/HashMap
    //   195: dup
    //   196: invokespecial <init> : ()V
    //   199: astore #14
    //   201: aload #12
    //   203: ldc 'images'
    //   205: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   208: dup
    //   209: astore #12
    //   211: ifnull -> 1104
    //   214: new java/util/ArrayList
    //   217: dup
    //   218: invokespecial <init> : ()V
    //   221: astore #15
    //   223: aload #12
    //   225: ldc 'texture'
    //   227: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   230: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   233: astore #16
    //   235: aload #16
    //   237: invokeinterface hasNext : ()Z
    //   242: ifeq -> 736
    //   245: aload #16
    //   247: invokeinterface next : ()Ljava/lang/Object;
    //   252: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   255: ldc 'file'
    //   257: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   260: astore #18
    //   262: aload #9
    //   264: getfield f : Ljava/lang/String;
    //   267: aload #18
    //   269: iload #13
    //   271: istore #22
    //   273: astore #21
    //   275: astore #20
    //   277: aload #21
    //   279: ldc '/'
    //   281: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   284: ifne -> 297
    //   287: aload #21
    //   289: ldc '\'
    //   291: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   294: ifeq -> 373
    //   297: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   300: aload #20
    //   302: aload #21
    //   304: bipush #92
    //   306: bipush #47
    //   308: invokevirtual replace : (CC)Ljava/lang/String;
    //   311: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   316: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   321: dup
    //   322: astore #23
    //   324: invokevirtual exists : ()Z
    //   327: ifeq -> 335
    //   330: aload #23
    //   332: goto -> 660
    //   335: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   338: aload #20
    //   340: aload #21
    //   342: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   347: bipush #92
    //   349: bipush #47
    //   351: invokevirtual replace : (CC)Ljava/lang/String;
    //   354: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   359: dup
    //   360: astore #24
    //   362: invokevirtual exists : ()Z
    //   365: ifeq -> 373
    //   368: aload #24
    //   370: goto -> 660
    //   373: aload #20
    //   375: iload #22
    //   377: aload #21
    //   379: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   384: astore #23
    //   386: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   389: aload #23
    //   391: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   396: dup
    //   397: astore #24
    //   399: invokevirtual exists : ()Z
    //   402: ifeq -> 410
    //   405: aload #24
    //   407: goto -> 660
    //   410: aload #21
    //   412: ldc '.4.png'
    //   414: invokevirtual endsWith : (Ljava/lang/String;)Z
    //   417: ifeq -> 508
    //   420: aload #21
    //   422: ldc '.4.png'
    //   424: ldc '.2.png'
    //   426: invokevirtual replace : (Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    //   429: astore #23
    //   431: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   434: aload #20
    //   436: iload #22
    //   438: aload #23
    //   440: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   445: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   450: dup
    //   451: astore #24
    //   453: invokevirtual exists : ()Z
    //   456: ifeq -> 464
    //   459: aload #24
    //   461: goto -> 660
    //   464: aload #21
    //   466: ldc '.4.png'
    //   468: ldc '.1.png'
    //   470: invokevirtual replace : (Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    //   473: astore #25
    //   475: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   478: aload #20
    //   480: iload #22
    //   482: aload #25
    //   484: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   489: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   494: dup
    //   495: astore #24
    //   497: invokevirtual exists : ()Z
    //   500: ifeq -> 508
    //   503: aload #24
    //   505: goto -> 660
    //   508: iconst_1
    //   509: istore #23
    //   511: iload #23
    //   513: bipush #99
    //   515: if_icmpgt -> 659
    //   518: aload #20
    //   520: iload #23
    //   522: aload #21
    //   524: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   529: astore #25
    //   531: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   534: aload #25
    //   536: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   541: dup
    //   542: astore #24
    //   544: invokevirtual exists : ()Z
    //   547: ifeq -> 555
    //   550: aload #24
    //   552: goto -> 660
    //   555: aload #21
    //   557: ldc '.4.png'
    //   559: invokevirtual endsWith : (Ljava/lang/String;)Z
    //   562: ifeq -> 653
    //   565: aload #21
    //   567: ldc '.4.png'
    //   569: ldc '.2.png'
    //   571: invokevirtual replace : (Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    //   574: astore #26
    //   576: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   579: aload #20
    //   581: iload #23
    //   583: aload #26
    //   585: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   590: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   595: dup
    //   596: astore #24
    //   598: invokevirtual exists : ()Z
    //   601: ifeq -> 609
    //   604: aload #24
    //   606: goto -> 660
    //   609: aload #21
    //   611: ldc '.4.png'
    //   613: ldc '.1.png'
    //   615: invokevirtual replace : (Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    //   618: astore #27
    //   620: getstatic com/badlogic/gdx/Gdx.files : Lcom/badlogic/gdx/Files;
    //   623: aload #20
    //   625: iload #23
    //   627: aload #27
    //   629: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   634: invokeinterface absolute : (Ljava/lang/String;)Lcom/badlogic/gdx/files/FileHandle;
    //   639: dup
    //   640: astore #24
    //   642: invokevirtual exists : ()Z
    //   645: ifeq -> 653
    //   648: aload #24
    //   650: goto -> 660
    //   653: iinc #23, 1
    //   656: goto -> 511
    //   659: aconst_null
    //   660: dup
    //   661: astore #19
    //   663: ifnonnull -> 688
    //   666: new com/badlogic/gdx/utils/GdxRuntimeException
    //   669: dup
    //   670: aload #18
    //   672: iload #13
    //   674: aload #9
    //   676: getfield f : Ljava/lang/String;
    //   679: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
    //   684: invokespecial <init> : (Ljava/lang/String;)V
    //   687: athrow
    //   688: aload #19
    //   690: invokevirtual file : ()Ljava/io/File;
    //   693: invokevirtual getAbsolutePath : ()Ljava/lang/String;
    //   696: astore #18
    //   698: aload #9
    //   700: getfield c : Lcom/badlogic/gdx/assets/AssetManager;
    //   703: aload #18
    //   705: ldc com/badlogic/gdx/graphics/Texture
    //   707: invokevirtual isLoaded : (Ljava/lang/String;Ljava/lang/Class;)Z
    //   710: ifne -> 725
    //   713: aload #9
    //   715: getfield c : Lcom/badlogic/gdx/assets/AssetManager;
    //   718: aload #18
    //   720: ldc com/badlogic/gdx/graphics/Texture
    //   722: invokevirtual load : (Ljava/lang/String;Ljava/lang/Class;)V
    //   725: aload #15
    //   727: aload #18
    //   729: invokevirtual add : (Ljava/lang/Object;)Z
    //   732: pop
    //   733: goto -> 235
    //   736: aload #9
    //   738: getfield c : Lcom/badlogic/gdx/assets/AssetManager;
    //   741: invokevirtual finishLoading : ()V
    //   744: iconst_0
    //   745: istore #16
    //   747: aload #12
    //   749: ldc 'texture'
    //   751: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   754: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   757: astore #17
    //   759: aload #17
    //   761: invokeinterface hasNext : ()Z
    //   766: ifeq -> 1104
    //   769: aload #17
    //   771: invokeinterface next : ()Ljava/lang/Object;
    //   776: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   779: astore #18
    //   781: aload #9
    //   783: getfield c : Lcom/badlogic/gdx/assets/AssetManager;
    //   786: aload #15
    //   788: iload #16
    //   790: iinc #16, 1
    //   793: invokevirtual get : (I)Ljava/lang/Object;
    //   796: checkcast java/lang/String
    //   799: ldc com/badlogic/gdx/graphics/Texture
    //   801: invokevirtual get : (Ljava/lang/String;Ljava/lang/Class;)Ljava/lang/Object;
    //   804: checkcast com/badlogic/gdx/graphics/Texture
    //   807: astore #19
    //   809: aload #18
    //   811: ldc 't'
    //   813: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   816: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   819: astore #18
    //   821: aload #18
    //   823: invokeinterface hasNext : ()Z
    //   828: ifeq -> 1101
    //   831: aload #18
    //   833: invokeinterface next : ()Ljava/lang/Object;
    //   838: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   841: dup
    //   842: astore #12
    //   844: ldc 'id'
    //   846: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   849: istore #13
    //   851: aload #12
    //   853: ldc 's'
    //   855: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   858: ldc ','
    //   860: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   863: dup
    //   864: astore #20
    //   866: iconst_0
    //   867: aaload
    //   868: invokestatic parseInt : (Ljava/lang/String;)I
    //   871: istore #21
    //   873: aload #20
    //   875: iconst_1
    //   876: aaload
    //   877: invokestatic parseInt : (Ljava/lang/String;)I
    //   880: istore #20
    //   882: aload #12
    //   884: ldc 'p'
    //   886: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   889: ldc ','
    //   891: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   894: dup
    //   895: astore #22
    //   897: iconst_0
    //   898: aaload
    //   899: invokestatic parseInt : (Ljava/lang/String;)I
    //   902: istore #23
    //   904: aload #22
    //   906: iconst_1
    //   907: aaload
    //   908: invokestatic parseInt : (Ljava/lang/String;)I
    //   911: istore #22
    //   913: aload #19
    //   915: iload #23
    //   917: iload #22
    //   919: iload #21
    //   921: iload #20
    //   923: istore #24
    //   925: istore #23
    //   927: istore #22
    //   929: istore #21
    //   931: astore #20
    //   933: new com/badlogic/gdx/graphics/g2d/TextureRegion
    //   936: dup
    //   937: aload #20
    //   939: iload #21
    //   941: iload #22
    //   943: iload #23
    //   945: iload #24
    //   947: invokespecial <init> : (Lcom/badlogic/gdx/graphics/Texture;IIII)V
    //   950: astore #25
    //   952: fconst_1
    //   953: aload #20
    //   955: invokevirtual getWidth : ()I
    //   958: i2f
    //   959: fdiv
    //   960: fstore #26
    //   962: fconst_1
    //   963: aload #20
    //   965: invokevirtual getHeight : ()I
    //   968: i2f
    //   969: fdiv
    //   970: fstore #27
    //   972: iload #21
    //   974: i2f
    //   975: ldc 0.1
    //   977: fadd
    //   978: fload #26
    //   980: fmul
    //   981: fstore #20
    //   983: iload #22
    //   985: i2f
    //   986: ldc 0.1
    //   988: fadd
    //   989: fload #27
    //   991: fmul
    //   992: fstore #28
    //   994: iload #21
    //   996: iload #23
    //   998: iadd
    //   999: i2f
    //   1000: ldc 0.1
    //   1002: fsub
    //   1003: fload #26
    //   1005: fmul
    //   1006: fstore #21
    //   1008: iload #22
    //   1010: iload #24
    //   1012: iadd
    //   1013: i2f
    //   1014: ldc 0.1
    //   1016: fsub
    //   1017: fload #27
    //   1019: fmul
    //   1020: fstore #22
    //   1022: aload #25
    //   1024: fload #20
    //   1026: fload #28
    //   1028: fload #21
    //   1030: fload #22
    //   1032: invokevirtual setRegion : (FFFF)V
    //   1035: aload #25
    //   1037: astore #20
    //   1039: aload #12
    //   1041: ldc 'o'
    //   1043: ldc '0,0'
    //   1045: invokevirtual getAttribute : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   1048: ldc ','
    //   1050: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   1053: dup
    //   1054: astore #12
    //   1056: iconst_0
    //   1057: aaload
    //   1058: invokestatic parseInt : (Ljava/lang/String;)I
    //   1061: istore #21
    //   1063: aload #12
    //   1065: iconst_1
    //   1066: aaload
    //   1067: invokestatic parseInt : (Ljava/lang/String;)I
    //   1070: istore #12
    //   1072: aload #14
    //   1074: iload #13
    //   1076: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1079: new a/m
    //   1082: dup
    //   1083: aload #20
    //   1085: iload #21
    //   1087: iload #12
    //   1089: invokespecial <init> : (Lcom/badlogic/gdx/graphics/g2d/TextureRegion;II)V
    //   1092: invokeinterface put : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   1097: pop
    //   1098: goto -> 821
    //   1101: goto -> 759
    //   1104: aload #14
    //   1106: astore #9
    //   1108: aload #10
    //   1110: ldc 'x'
    //   1112: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   1115: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   1118: astore #10
    //   1120: aload #10
    //   1122: invokeinterface hasNext : ()Z
    //   1127: ifeq -> 1655
    //   1130: aload #10
    //   1132: invokeinterface next : ()Ljava/lang/Object;
    //   1137: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   1140: dup
    //   1141: astore #12
    //   1143: ldc 'si'
    //   1145: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   1148: istore #13
    //   1150: aload #12
    //   1152: ldc 'a'
    //   1154: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   1157: ldc 'f'
    //   1159: invokevirtual getChildrenByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/Array;
    //   1162: astore #14
    //   1164: aload #12
    //   1166: ldc 'light'
    //   1168: invokevirtual getChildByName : (Ljava/lang/String;)Lcom/badlogic/gdx/utils/XmlReader$Element;
    //   1171: astore #12
    //   1173: iconst_0
    //   1174: istore #15
    //   1176: aconst_null
    //   1177: astore #16
    //   1179: aload #12
    //   1181: ifnull -> 1276
    //   1184: aload #12
    //   1186: ldc 's'
    //   1188: iconst_0
    //   1189: invokevirtual getIntAttribute : (Ljava/lang/String;I)I
    //   1192: istore #15
    //   1194: aload #12
    //   1196: ldc 'c'
    //   1198: invokevirtual getAttribute : (Ljava/lang/String;)Ljava/lang/String;
    //   1201: ldc ','
    //   1203: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   1206: dup
    //   1207: astore #12
    //   1209: iconst_0
    //   1210: aaload
    //   1211: invokestatic parseInt : (Ljava/lang/String;)I
    //   1214: i2f
    //   1215: ldc 255.0
    //   1217: fdiv
    //   1218: fstore #17
    //   1220: aload #12
    //   1222: iconst_1
    //   1223: aaload
    //   1224: invokestatic parseInt : (Ljava/lang/String;)I
    //   1227: i2f
    //   1228: ldc 255.0
    //   1230: fdiv
    //   1231: fstore #18
    //   1233: aload #12
    //   1235: iconst_2
    //   1236: aaload
    //   1237: invokestatic parseInt : (Ljava/lang/String;)I
    //   1240: i2f
    //   1241: ldc 255.0
    //   1243: fdiv
    //   1244: fstore #19
    //   1246: aload #12
    //   1248: iconst_3
    //   1249: aaload
    //   1250: invokestatic parseInt : (Ljava/lang/String;)I
    //   1253: i2f
    //   1254: ldc 255.0
    //   1256: fdiv
    //   1257: fstore #20
    //   1259: new com/badlogic/gdx/graphics/Color
    //   1262: dup
    //   1263: fload #17
    //   1265: fload #18
    //   1267: fload #19
    //   1269: fload #20
    //   1271: invokespecial <init> : (FFFF)V
    //   1274: astore #16
    //   1276: new com/badlogic/gdx/utils/Array
    //   1279: dup
    //   1280: invokespecial <init> : ()V
    //   1283: astore #12
    //   1285: new com/badlogic/gdx/utils/Array
    //   1288: dup
    //   1289: invokespecial <init> : ()V
    //   1292: astore #17
    //   1294: new com/badlogic/gdx/utils/Array
    //   1297: dup
    //   1298: invokespecial <init> : ()V
    //   1301: astore #18
    //   1303: aload #14
    //   1305: invokevirtual iterator : ()Lcom/badlogic/gdx/utils/Array$ArrayIterator;
    //   1308: astore #19
    //   1310: aload #19
    //   1312: invokeinterface hasNext : ()Z
    //   1317: ifeq -> 1469
    //   1320: aload #19
    //   1322: invokeinterface next : ()Ljava/lang/Object;
    //   1327: checkcast com/badlogic/gdx/utils/XmlReader$Element
    //   1330: dup
    //   1331: astore #20
    //   1333: ldc 'id'
    //   1335: invokevirtual getIntAttribute : (Ljava/lang/String;)I
    //   1338: istore #14
    //   1340: aload #9
    //   1342: iload #14
    //   1344: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1347: invokeinterface get : (Ljava/lang/Object;)Ljava/lang/Object;
    //   1352: checkcast a/m
    //   1355: astore #21
    //   1357: aload #12
    //   1359: aload #21
    //   1361: getfield k : Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   1364: invokevirtual add : (Ljava/lang/Object;)V
    //   1367: aload #17
    //   1369: new com/badlogic/gdx/math/Vector2
    //   1372: dup
    //   1373: aload #21
    //   1375: getfield i : I
    //   1378: i2f
    //   1379: aload #21
    //   1381: getfield j : I
    //   1384: i2f
    //   1385: invokespecial <init> : (FF)V
    //   1388: invokevirtual add : (Ljava/lang/Object;)V
    //   1391: aload #20
    //   1393: ldc 'p'
    //   1395: ldc '150'
    //   1397: invokevirtual getAttribute : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   1400: dup
    //   1401: astore #22
    //   1403: ldc ','
    //   1405: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   1408: ifeq -> 1423
    //   1411: aload #22
    //   1413: ldc ','
    //   1415: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   1418: iconst_0
    //   1419: aaload
    //   1420: goto -> 1447
    //   1423: aload #22
    //   1425: ldc '-'
    //   1427: invokevirtual contains : (Ljava/lang/CharSequence;)Z
    //   1430: ifeq -> 1445
    //   1433: aload #22
    //   1435: ldc '-'
    //   1437: invokevirtual split : (Ljava/lang/String;)[Ljava/lang/String;
    //   1440: iconst_0
    //   1441: aaload
    //   1442: goto -> 1447
    //   1445: aload #22
    //   1447: astore #14
    //   1449: aload #18
    //   1451: aload #14
    //   1453: invokestatic parseInt : (Ljava/lang/String;)I
    //   1456: i2f
    //   1457: ldc 1000.0
    //   1459: fdiv
    //   1460: invokestatic valueOf : (F)Ljava/lang/Float;
    //   1463: invokevirtual add : (Ljava/lang/Object;)V
    //   1466: goto -> 1310
    //   1469: aload #12
    //   1471: ldc com/badlogic/gdx/graphics/g2d/TextureRegion
    //   1473: invokevirtual toArray : (Ljava/lang/Class;)[Ljava/lang/Object;
    //   1476: checkcast [Lcom/badlogic/gdx/graphics/g2d/TextureRegion;
    //   1479: astore #19
    //   1481: aload #18
    //   1483: getfield size : I
    //   1486: newarray float
    //   1488: astore #20
    //   1490: iconst_0
    //   1491: istore #14
    //   1493: iload #14
    //   1495: aload #18
    //   1497: getfield size : I
    //   1500: if_icmpge -> 1527
    //   1503: aload #20
    //   1505: iload #14
    //   1507: aload #18
    //   1509: iload #14
    //   1511: invokevirtual get : (I)Ljava/lang/Object;
    //   1514: checkcast java/lang/Float
    //   1517: invokevirtual floatValue : ()F
    //   1520: fastore
    //   1521: iinc #14, 1
    //   1524: goto -> 1493
    //   1527: aload #17
    //   1529: getfield size : I
    //   1532: newarray int
    //   1534: astore #14
    //   1536: aload #17
    //   1538: getfield size : I
    //   1541: newarray int
    //   1543: astore #21
    //   1545: iconst_0
    //   1546: istore #22
    //   1548: iload #22
    //   1550: aload #17
    //   1552: getfield size : I
    //   1555: if_icmpge -> 1602
    //   1558: aload #14
    //   1560: iload #22
    //   1562: aload #17
    //   1564: iload #22
    //   1566: invokevirtual get : (I)Ljava/lang/Object;
    //   1569: checkcast com/badlogic/gdx/math/Vector2
    //   1572: getfield x : F
    //   1575: f2i
    //   1576: iastore
    //   1577: aload #21
    //   1579: iload #22
    //   1581: aload #17
    //   1583: iload #22
    //   1585: invokevirtual get : (I)Ljava/lang/Object;
    //   1588: checkcast com/badlogic/gdx/math/Vector2
    //   1591: getfield y : F
    //   1594: f2i
    //   1595: iastore
    //   1596: iinc #22, 1
    //   1599: goto -> 1548
    //   1602: iload #11
    //   1604: bipush #8
    //   1606: ishl
    //   1607: iload #13
    //   1609: ior
    //   1610: istore #22
    //   1612: new a/k
    //   1615: dup
    //   1616: iload #22
    //   1618: aload #19
    //   1620: aload #20
    //   1622: aload #14
    //   1624: aload #21
    //   1626: iload #15
    //   1628: aload #16
    //   1630: invokespecial <init> : (I[Lcom/badlogic/gdx/graphics/g2d/TextureRegion;[F[I[IILcom/badlogic/gdx/graphics/Color;)V
    //   1633: astore #14
    //   1635: aload_0
    //   1636: getfield f : Ljava/util/Map;
    //   1639: iload #22
    //   1641: invokestatic valueOf : (I)Ljava/lang/Integer;
    //   1644: aload #14
    //   1646: invokeinterface put : (Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    //   1651: pop
    //   1652: goto -> 1120
    //   1655: goto -> 1682
    //   1658: astore #9
    //   1660: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   1663: ldc 'IconLoader'
    //   1665: aload #8
    //   1667: invokevirtual path : ()Ljava/lang/String;
    //   1670: <illegal opcode> makeConcatWithConstants : (Ljava/lang/String;)Ljava/lang/String;
    //   1675: aload #9
    //   1677: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   1682: iinc #7, 1
    //   1685: goto -> 80
    //   1688: iinc #4, 1
    //   1691: goto -> 32
    //   1694: return
    // Exception table:
    //   from	to	target	type
    //   114	169	1658	java/lang/Exception
    //   172	1655	1658	java/lang/Exception
  }
  
  public final k a(int paramInt) {
    return (k)this.f.get(Integer.valueOf(paramInt));
  }
}
