package a;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.NinePatch;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.ui.WidgetGroup;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;

public final class ll {
  private static WidgetGroup a;
  
  private static Texture bl;
  
  private static Image G;
  
  private static Table P;
  
  private static Table Q;
  
  private static boolean bL;
  
  public static void a(cr paramcr, Stage paramStage, boolean paramBoolean) {
    cg();
    bL = paramBoolean;
    (a = new lm()).setFillParent(true);
    if (bl == null) {
      Pixmap pixmap;
      (pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888)).setColor(Color.WHITE);
      pixmap.fill();
      bl = new Texture(pixmap);
      pixmap.dispose();
    } 
    (G = new Image(bl)).setColor(0.0F, 0.0F, 0.0F, paramBoolean ? 1.0F : 0.6F);
    G.addListener((EventListener)new ln());
    a.addActor((Actor)G);
    P = new Table();
    Q = new Table();
    if (b.E != null)
      Q.setBackground((Drawable)new NinePatchDrawable(b.E)); 
    boolean bool = (paramStage.getHeight() > paramStage.getWidth()) ? true : false;
    String str1 = "Cancelar";
    String str2;
    if (paramcr.f != null && (str2 = b.a(paramcr.f.S, "id_cancel")) != null && !str2.isEmpty())
      str1 = str2; 
    TextButton.TextButtonStyle textButtonStyle;
    (textButtonStyle = new TextButton.TextButtonStyle()).font = b.a(str1);
    textButtonStyle.up = (Drawable)new NinePatchDrawable((NinePatch)b.m);
    textButtonStyle.down = (Drawable)new NinePatchDrawable((b.n != null) ? (NinePatch)b.n : (NinePatch)b.m);
    textButtonStyle.over = textButtonStyle.up;
    TextButton textButton = new TextButton(str1, textButtonStyle);
    if (bL) {
      if (bool) {
        textButton.pad(30.0F, 100.0F, 30.0F, 100.0F);
        textButton.getLabel().setFontScale(3.0F);
      } else {
        textButton.pad(15.0F, 40.0F, 15.0F, 40.0F);
        textButton.getLabel().setFontScale(1.5F);
      } 
    } else if (bool) {
      textButton.pad(24.0F, 80.0F, 24.0F, 80.0F);
      textButton.getLabel().setFontScale(2.0F);
    } else {
      textButton.pad(8.0F, 20.0F, 8.0F, 20.0F);
      textButton.getLabel().setFontScale(1.0F);
    } 
    textButton.getLabel().setAlignment(1);
    textButton.addListener((EventListener)new lo(paramcr));
    float f = bool ? 24.0F : 15.0F;
    Q.add((Actor)textButton).expand().bottom().left().pad(f);
    P.add((Actor)Q).center();
    a.addActor((Actor)P);
    paramStage.addActor((Actor)a);
    a.setSize(paramStage.getWidth(), paramStage.getHeight());
    g(paramStage.getWidth(), paramStage.getHeight());
    a.toFront();
  }
  
  static void g(float paramFloat1, float paramFloat2) {
    if (G != null)
      G.setSize(paramFloat1, paramFloat2); 
    if (P != null) {
      P.setSize(paramFloat1, paramFloat2);
      if (Q != null && P.getCell((Actor)Q) != null) {
        if (bL) {
          P.getCell((Actor)Q).width(paramFloat1).height(paramFloat2);
        } else {
          if ((paramFloat2 > paramFloat1)) {
            paramFloat1 = Math.min(paramFloat1 * 0.85F, 650.0F);
            paramFloat2 = Math.min(paramFloat2 * 0.6F, 850.0F);
          } else {
            paramFloat1 = Math.min(paramFloat1 * 0.7F, 300.0F);
            paramFloat2 = Math.min(paramFloat2 * 0.8F, 450.0F);
          } 
          P.getCell((Actor)Q).width(paramFloat1).height(paramFloat2);
        } 
        P.invalidate();
      } 
    } 
  }
  
  public static void cg() {
    if (a != null) {
      a.remove();
      a = null;
    } 
  }
}
