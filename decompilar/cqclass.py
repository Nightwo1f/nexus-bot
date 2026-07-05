package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.math.MathUtils;
import java.util.ArrayList;
import java.util.List;

public final class cq {
  public boolean K = false;
  
  public float[] j = new float[7];
  
  public float[] k = new float[7];
  
  public static float Z = 120.0F;
  
  public static float aa = 90.0F;
  
  public static float ab = 90.0F;
  
  public static float ac = 2.0F;
  
  public boolean L = true;
  
  public boolean M = true;
  
  public boolean N = true;
  
  public boolean O = false;
  
  public boolean P = false;
  
  public float ad = 1.7F;
  
  public float ae = 37.0F;
  
  public boolean Q = false;
  
  public int bI = 0;
  
  public int a = 640;
  
  public int b = 360;
  
  public String S;
  
  public boolean R = true;
  
  public boolean S = "en";
  
  public int bJ;
  
  public int bK;
  
  public String T;
  
  public String U;
  
  float af;
  
  public float ag;
  
  public float ah;
  
  int bL;
  
  public final List n;
  
  public String V;
  
  public String W;
  
  public int bM;
  
  public int bN;
  
  public int bO;
  
  public int bP;
  
  public boolean T;
  
  public boolean U;
  
  private float ai;
  
  private float aj;
  
  public static float ak = 0.65F;
  
  public static float al = 0.9F;
  
  public float am;
  
  public int aD;
  
  public int aE;
  
  public int aF;
  
  private int bQ;
  
  private int bR;
  
  private int bS;
  
  public int bT;
  
  public int bU;
  
  public int bV;
  
  public int bW;
  
  public int bX;
  
  public int bY;
  
  public int bZ;
  
  private String X;
  
  public String Y;
  
  public String Z;
  
  public int ca;
  
  public int cb;
  
  public final List o;
  
  public boolean V;
  
  public boolean W;
  
  public boolean X;
  
  public boolean Y;
  
  public boolean Z;
  
  public String aa;
  
  public String ab;
  
  public boolean aa;
  
  public cq() {
    this.S = false;
    this.bJ = 126;
    this.bK = 22;
    this.T = "jtme_client";
    this.U = "";
    this.af = 0.35F;
    this.ag = 0.35F;
    this.ah = 0.35F;
    this.bL = 0;
    this.n = new ArrayList();
    this.V = "login.otjtme.com";
    this.W = "login.otjtme.com";
    this.bM = 9191;
    this.bN = 9191;
    this.bO = 600;
    this.bP = 64;
    this.T = true;
    this.U = true;
    this.ai = -1.0F;
    this.aj = -1.0F;
    this.am = 1.9F;
    this.bV = 19;
    this.bW = 17;
    this.bX = 2;
    this.bY = 14;
    this.bZ = 40;
    this.X = "jtme_client";
    this.Y = "";
    this.Z = "";
    this.ca = 0;
    this.cb = 200;
    this.o = new ArrayList();
    this.V = true;
    this.W = true;
    this.X = false;
    this.Y = true;
    this.Z = true;
    this.aa = "https://otjtme.com/Downloads/version.txt";
    this.ab = "https://otjtme.com/Downloads/JTME-Official-Client.zip";
    this.aa = true;
  }
  
  public final void c(boolean paramBoolean) {
    this.M = paramBoolean;
    cj.f(this);
  }
  
  public static float b() {
    return Z;
  }
  
  public static float c() {
    return ab;
  }
  
  public final void e(float paramFloat) {
    this.ad = paramFloat;
    cj.f(this);
  }
  
  public final void af() {
    int i;
    int j;
    boolean bool;
    if (bool = (Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS) ? true : false) {
      float f1 = 9.0F;
      if (this.bX == 0) {
        f1 = 6.0F;
      } else if (this.bX == 1) {
        f1 = 7.5F;
      } 
      int k = Gdx.graphics.getWidth();
      float f2 = Gdx.graphics.getHeight() / k;
      float f3 = f1 * f2;
      i = (int)Math.ceil(f1) + 2;
      j = (int)Math.ceil(f3) + 2;
    } else {
      float f;
      i = Math.max(1, this.bP);
      int k = (Gdx.graphics.getDisplayMode()).width;
      j = (Gdx.graphics.getDisplayMode()).height;
      int m = 3 * i + 4;
      k = (int)Math.ceil(((k - m) / i));
      j = (int)Math.ceil((j / i));
      if (this.bX == 0) {
        f = 0.5F;
      } else if (this.bX == 1) {
        f = 0.75F;
      } else {
        f = 1.0F;
      } 
      i = (int)(k * f) + 2;
      j = (int)(j * f) + 2;
    } 
    if (i % 2 == 0)
      i++; 
    if (j % 2 == 0)
      j++; 
    if (i < 17)
      i = 17; 
    if (j < 17)
      j = 17; 
    if (!bool) {
      if (i < 19)
        i = 19; 
      if (j < 19)
        j = 19; 
      if (i > 43)
        i = 43; 
      if (j > 43)
        j = 43; 
    } 
    this.bV = i;
    this.bW = j;
    if (i > 15 || j > 15) {
      this.R = true;
    } else {
      this.R = false;
    } 
    System.out.println("[GameSettings] ZoomMode: " + this.bX + " | Tiles: W=" + i + ", H=" + j + " | WebClient(2Bytes): " + this.R);
  }
  
  public final void d(boolean paramBoolean) {
    this.Y = paramBoolean;
    cj.f(this);
  }
  
  public final boolean g() {
    return this.U;
  }
  
  public final int i() {
    return this.bV;
  }
  
  public final void f(float paramFloat) {
    this.ag = MathUtils.clamp(paramFloat, 0.0F, 1.0F);
  }
  
  public final void e(boolean paramBoolean) {
    this.L = paramBoolean;
    cj.f(this);
  }
  
  public final void g(float paramFloat) {
    this.ah = MathUtils.clamp(paramFloat, 0.0F, 1.0F);
  }
  
  public final void f(boolean paramBoolean) {
    this.Q = paramBoolean;
    cj.f(this);
  }
  
  public final void K(int paramInt) {
    this.bI = paramInt;
    cj.f(this);
  }
  
  public final void ag() {
    byte b = 0;
    boolean bool = false;
    switch (this.bI) {
      case 0:
        bool = true;
      case 1:
        b = 30;
        break;
      case 2:
        b = 60;
        break;
      case 3:
        b = 120;
        break;
      case 4:
        b = 0;
        break;
    } 
    Gdx.graphics.setVSync(bool);
    Gdx.graphics.setForegroundFPS(b);
  }
  
  public final void o(String paramString) {
    this.S = paramString;
    cj.f(this);
  }
  
  public final String d() {
    return this.o.isEmpty() ? "" : this.o.get(0);
  }
  
  public final void L(int paramInt) {
    this.a = paramInt;
    cj.f(this);
  }
  
  public final void M(int paramInt) {
    this.b = paramInt;
    cj.f(this);
  }
  
  public final void a(ck paramck) {
    this.n.add(paramck);
    cj.f(this);
  }
  
  public final int j() {
    return this.aD;
  }
  
  public final int k() {
    return this.aE;
  }
  
  public final int l() {
    return this.aF;
  }
  
  public final be a() {
    return new be(this.aD, this.aE, this.aF);
  }
  
  public final void g(int paramInt1, int paramInt2, int paramInt3) {
    this.bQ = this.aD;
    this.bR = this.aE;
    this.bS = this.aF;
    this.aD = paramInt1;
    this.aE = paramInt2;
    this.aF = paramInt3;
  }
  
  public final void h(float paramFloat) {
    float f;
    if ((f = this.bP) <= 0.0F)
      f = 32.0F; 
    paramFloat /= 8.0F;
    this.am = paramFloat / f;
    this.am = MathUtils.clamp(this.am, 1.0F, 3.5F);
  }
  
  public static boolean c(int paramInt) {
    return (paramInt == 1);
  }
  
  public static boolean d(int paramInt) {
    return (paramInt == 3);
  }
  
  public static boolean e(int paramInt) {
    return (paramInt == 2 || paramInt == 4);
  }
  
  public static boolean f(int paramInt) {
    return c(paramInt);
  }
}
