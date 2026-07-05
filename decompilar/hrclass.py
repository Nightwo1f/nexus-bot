package a;

import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;

final class hr extends ClickListener {
  private final int dT;
  
  private final boolean bb;
  
  private final Actor d;
  
  private Action a;
  
  private boolean bc = false;
  
  private final Vector2 p = new Vector2();
  
  public hr(gb paramgb, int paramInt, boolean paramBoolean, Actor paramActor) {
    this.dT = paramInt;
    this.bb = paramBoolean;
    this.d = paramActor;
  }
  
  public final boolean touchDown(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    if (paramInt2 == 0)
      this.bc = false; 
    if (this.M.q())
      return super.touchDown(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2); 
    if (this.M.c != null) {
      this.M.br();
      return true;
    } 
    if (paramInt2 == 1) {
      bS();
      return true;
    } 
    if (paramInt2 == 0) {
      this.p.set(paramFloat1, paramFloat2);
      if (this.a != null)
        this.d.removeAction(this.a); 
      this.a = (Action)Actions.sequence((Action)Actions.delay(0.7F), (Action)Actions.run(() -> {
              this.bc = true;
              bS();
            }));
      this.d.addAction(this.a);
    } 
    return super.touchDown(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void touchDragged(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt) {
    if (this.a != null && !this.bc && Vector2.dst(this.p.x, this.p.y, paramFloat1, paramFloat2) > 20.0F) {
      this.d.removeAction(this.a);
      this.a = null;
    } 
    super.touchDragged(paramInputEvent, paramFloat1, paramFloat2, paramInt);
  }
  
  public final void touchUp(InputEvent paramInputEvent, float paramFloat1, float paramFloat2, int paramInt1, int paramInt2) {
    if (this.a != null) {
      this.d.removeAction(this.a);
      this.a = null;
    } 
    super.touchUp(paramInputEvent, paramFloat1, paramFloat2, paramInt1, paramInt2);
  }
  
  public final void clicked(InputEvent paramInputEvent, float paramFloat1, float paramFloat2) {
    // Byte code:
    //   0: aload_0
    //   1: getfield bc : Z
    //   4: ifeq -> 8
    //   7: return
    //   8: aload_0
    //   9: getfield M : La/gb;
    //   12: getfield c : Lcom/badlogic/gdx/scenes/scene2d/Group;
    //   15: ifnonnull -> 26
    //   18: aload_1
    //   19: invokevirtual getButton : ()I
    //   22: iconst_1
    //   23: if_icmpne -> 27
    //   26: return
    //   27: aload_0
    //   28: getfield M : La/gb;
    //   31: invokevirtual q : ()Z
    //   34: ifeq -> 290
    //   37: aload_0
    //   38: aload_1
    //   39: astore_2
    //   40: dup
    //   41: astore_1
    //   42: getfield M : La/gb;
    //   45: getfield aS : Z
    //   48: ifne -> 289
    //   51: aload_2
    //   52: invokevirtual getButton : ()I
    //   55: ifne -> 289
    //   58: aload_1
    //   59: getfield bb : Z
    //   62: ifeq -> 75
    //   65: aload_1
    //   66: getfield dT : I
    //   69: bipush #101
    //   71: isub
    //   72: goto -> 81
    //   75: aload_1
    //   76: getfield dT : I
    //   79: iconst_1
    //   80: isub
    //   81: istore_2
    //   82: aload_1
    //   83: iload_2
    //   84: invokevirtual h : (I)Z
    //   87: ifeq -> 289
    //   90: aload_1
    //   91: getfield M : La/gb;
    //   94: dup
    //   95: astore_2
    //   96: getfield F : [I
    //   99: ifnull -> 110
    //   102: aload_2
    //   103: getfield F : [I
    //   106: arraylength
    //   107: ifne -> 114
    //   110: iconst_0
    //   111: goto -> 228
    //   114: aload_2
    //   115: getfield F : [I
    //   118: arraylength
    //   119: istore_3
    //   120: iconst_0
    //   121: istore #4
    //   123: iload #4
    //   125: iload_3
    //   126: if_icmpge -> 227
    //   129: aload_2
    //   130: getfield a : [Z
    //   133: ifnull -> 160
    //   136: iload #4
    //   138: aload_2
    //   139: getfield a : [Z
    //   142: arraylength
    //   143: if_icmpge -> 160
    //   146: aload_2
    //   147: getfield a : [Z
    //   150: iload #4
    //   152: baload
    //   153: ifeq -> 160
    //   156: iconst_1
    //   157: goto -> 161
    //   160: iconst_0
    //   161: istore #5
    //   163: aload_2
    //   164: getfield dD : I
    //   167: ifle -> 183
    //   170: iload #4
    //   172: aload_2
    //   173: getfield dD : I
    //   176: if_icmplt -> 183
    //   179: iconst_1
    //   180: goto -> 184
    //   183: iconst_0
    //   184: istore #6
    //   186: iload #5
    //   188: ifne -> 196
    //   191: iload #6
    //   193: ifeq -> 200
    //   196: iconst_1
    //   197: goto -> 201
    //   200: iconst_0
    //   201: ifne -> 221
    //   204: aload_2
    //   205: getfield F : [I
    //   208: iload #4
    //   210: iaload
    //   211: ifne -> 221
    //   214: iload #4
    //   216: iconst_1
    //   217: iadd
    //   218: goto -> 228
    //   221: iinc #4, 1
    //   224: goto -> 123
    //   227: iconst_0
    //   228: dup
    //   229: istore_2
    //   230: ifeq -> 264
    //   233: aload_1
    //   234: getfield M : La/gb;
    //   237: getfield m : La/br;
    //   240: aload_1
    //   241: getfield dT : I
    //   244: iload_2
    //   245: invokevirtual k : (II)V
    //   248: return
    //   249: astore_1
    //   250: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   253: ldc 'Depot'
    //   255: ldc 'Store fail'
    //   257: aload_1
    //   258: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   263: return
    //   264: aload_1
    //   265: getfield M : La/gb;
    //   268: getfield m : La/br;
    //   271: aload_1
    //   272: getfield M : La/gb;
    //   275: getfield j : La/cq;
    //   278: getfield S : Ljava/lang/String;
    //   281: ldc 'id_no_free_depot_position_found'
    //   283: invokestatic a : (Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    //   286: invokevirtual g : (Ljava/lang/String;)V
    //   289: return
    //   290: aload_0
    //   291: dup
    //   292: astore_1
    //   293: getfield bb : Z
    //   296: ifeq -> 309
    //   299: aload_1
    //   300: getfield dT : I
    //   303: bipush #101
    //   305: isub
    //   306: goto -> 315
    //   309: aload_1
    //   310: getfield dT : I
    //   313: iconst_1
    //   314: isub
    //   315: istore_2
    //   316: aload_1
    //   317: iload_2
    //   318: invokevirtual h : (I)Z
    //   321: ifeq -> 361
    //   324: aload_1
    //   325: getfield M : La/gb;
    //   328: getfield m : La/br;
    //   331: aload_1
    //   332: getfield dT : I
    //   335: invokevirtual A : (I)V
    //   338: return
    //   339: astore_2
    //   340: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   343: ldc 'GameUI'
    //   345: aload_1
    //   346: getfield dT : I
    //   349: <illegal opcode> makeConcatWithConstants : (I)Ljava/lang/String;
    //   354: aload_2
    //   355: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   360: return
    //   361: aload_1
    //   362: getfield bb : Z
    //   365: ifne -> 378
    //   368: aload_1
    //   369: getfield M : La/gb;
    //   372: invokevirtual p : ()Z
    //   375: ifeq -> 414
    //   378: aload_1
    //   379: getfield M : La/gb;
    //   382: getfield m : La/br;
    //   385: aload_1
    //   386: getfield dT : I
    //   389: invokevirtual z : (I)V
    //   392: return
    //   393: astore_2
    //   394: getstatic com/badlogic/gdx/Gdx.app : Lcom/badlogic/gdx/Application;
    //   397: ldc 'GameUI'
    //   399: aload_1
    //   400: getfield dT : I
    //   403: <illegal opcode> makeConcatWithConstants : (I)Ljava/lang/String;
    //   408: aload_2
    //   409: invokeinterface error : (Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V
    //   414: return
    // Exception table:
    //   from	to	target	type
    //   233	248	249	java/lang/Exception
    //   324	338	339	java/lang/Exception
    //   378	392	393	java/lang/Exception
  }
  
  private void bS() {
    Vector2 vector2 = this.d.localToStageCoordinates(new Vector2(0.0F, 0.0F));
    int i = this.bb ? (this.dT - 101) : (this.dT - 1);
    if (h(i)) {
      this.M.b(this.dT, vector2.x, vector2.y);
      return;
    } 
    if (this.bb)
      try {
        this.M.m.z(this.dT);
        return;
      } catch (Exception exception) {
        return;
      }  
    if (this.M.p())
      this.M.c(this.dT, vector2.x, vector2.y); 
  }
  
  private boolean h(int paramInt) {
    return this.bb ? ((paramInt >= 0 && paramInt < this.M.D.length && this.M.D[paramInt] != null)) : ((paramInt >= 0 && paramInt < this.M.C.length && this.M.C[paramInt] != null));
  }
}
