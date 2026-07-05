package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.scenes.scene2d.Action;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.Group;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.Touchable;
import com.badlogic.gdx.scenes.scene2d.actions.Actions;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.Scaling;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public final class lb {
  public static Actor g;
  
  static Group m;
  
  private static final Map D;
  
  private static void c(Stage paramStage) {
    if (m == null || m.getStage() != paramStage) {
      if (m != null)
        m.remove(); 
      (m = new Group()).setName("PopupMessageUpOverlay");
      m.setTransform(false);
      m.setTouchable(Touchable.disabled);
      paramStage.addActor((Actor)m);
    } 
    m.toFront();
    m.setZIndex((paramStage.getRoot().getChildren()).size - 1);
  }
  
  public static void a(Stage paramStage, String paramString) {
    a(paramStage, paramString, null);
  }
  
  private static void a(Stage paramStage, String paramString, cq paramcq) {
    if (g != null && g.getStage() != paramStage) {
      g.remove();
      g = null;
    } 
    if (g != null) {
      String str1 = paramString;
      Stage stage = paramStage;
      g.clearActions();
      g.addAction((Action)Actions.sequence((Action)Actions.fadeOut(0.35F), (Action)Actions.run(() -> {
                g.remove();
                g = null;
                a(paramStage, paramString, paramcq);
              })));
      return;
    } 
    c(paramStage);
    boolean bool;
    if (bool = (Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS) ? true : false) {
      f3 = Math.max(150.0F, paramStage.getViewport().getWorldWidth() * 0.9F);
    } else {
      f3 = Math.max(150.0F, Math.min(350.0F, paramStage.getViewport().getWorldWidth() * 0.9F));
    } 
    String str = c(paramString);
    Label.LabelStyle labelStyle = new Label.LabelStyle(b.a(str), Color.WHITE);
    float f4 = 1.0F;
    if (bool) {
      if ((f4 = Math.min(paramStage.getViewport().getWorldWidth(), paramStage.getViewport().getWorldHeight()) * 0.05F / labelStyle.font.getLineHeight()) < 1.0F)
        f4 = 1.0F; 
      if (f4 > 4.5F)
        f4 = 4.5F; 
    } 
    Table table1;
    (table1 = a(paramString, labelStyle, f3, f4)).pack();
    table1.align(1);
    Table table2;
    (table2 = new Table()).setBackground((Drawable)new NinePatchDrawable(b.v));
    table2.defaults().center();
    table2.setClip(true);
    table2.pad(4.0F);
    table2.add((Actor)table1).pad(4.0F).center().row();
    table2.pack();
    float f1 = paramStage.getViewport().getWorldWidth();
    float f2 = paramStage.getViewport().getWorldHeight();
    float f3 = (fj.au > 0.0F) ? fj.au : (f1 / 2.0F);
    if (bool) {
      float f5 = table2.getWidth();
      float f6 = table2.getHeight();
      f2 = f2 * 0.85F - f6;
      f3 -= f5 / 2.0F;
      f3 = Math.max(10.0F, Math.min(f3, f1 - f5 - 10.0F));
      table2.setPosition(Math.round(f3), Math.round(f2));
    } else {
      float f5 = f3 - table2.getWidth() / 2.0F;
      float f6 = (f2 - table2.getHeight()) * 0.8F;
      table2.setPosition(Math.round(f5), Math.round(f6));
    } 
    (table2.getColor()).a = 0.0F;
    m.addActor((Actor)table2);
    m.toFront();
    table2.toFront();
    table2.setZIndex((m.getChildren()).size - 1);
    g = (Actor)table2;
    table2.addAction((Action)Actions.parallel((Action)Actions.sequence((Action)Actions.fadeIn(0.35F), (Action)Actions.delay(3.0F), (Action)Actions.fadeOut(0.35F), (Action)Actions.run(() -> {
                paramTable.remove();
                if (g == paramTable)
                  g = null; 
              })), (Action)Actions.forever(new lc(paramStage, table2, bool))));
  }
  
  private static List d(String paramString) {
    ArrayList<ld> arrayList = new ArrayList();
    StringBuilder stringBuilder = new StringBuilder();
    for (byte b = 0; b < paramString.length(); b++) {
      int i;
      if ((i = paramString.charAt(b)) == '\n') {
        if (stringBuilder.length() > 0) {
          arrayList.add(ld.a(stringBuilder.toString()));
          stringBuilder.setLength(0);
        } 
        arrayList.add(new ld(le.d, null, -1));
        b++;
        continue;
      } 
      if (b + 2 < paramString.length() && paramString.charAt(b) == '&& paramString.charAt(b + 1) == '&& D.containsKey(Character.valueOf(paramString.charAt(b + 2)))) {
        if (stringBuilder.length() > 0) {
          arrayList.add(ld.a(stringBuilder.toString()));
          stringBuilder.setLength(0);
        } 
        i = ((Integer)D.get(Character.valueOf(paramString.charAt(b + 2)))).intValue();
        arrayList.add(new ld(le.c, null, i));
        b += 3;
        continue;
      } 
      stringBuilder.append(i);
    } 
    if (stringBuilder.length() > 0)
      arrayList.add(ld.a(stringBuilder.toString())); 
    return arrayList;
  }
  
  private static void a(Table paramTable1, Table paramTable2) {
    paramTable1.add((Actor)paramTable2).center().row();
  }
  
  private static Table a(String paramString, Label.LabelStyle paramLabelStyle, float paramFloat1, float paramFloat2) {
    Table table1;
    (table1 = new Table()).top().center();
    table1.defaults().center();
    float f1 = paramLabelStyle.font.getCapHeight() * 1.3F * paramFloat2;
    GlyphLayout glyphLayout = new GlyphLayout();
    Table table2;
    (table2 = (new Table()).center()).defaults().center();
    float f2 = 0.0F;
    Iterator<ld> iterator = d(paramString).iterator();
    while (iterator.hasNext()) {
      Image image;
      ld ld;
      if ((ld = iterator.next()).a == le.d) {
        a(table1, table2);
        (table2 = (new Table()).center()).defaults().center();
        f2 = 0.0F;
        continue;
      } 
      if (ld.a == le.c) {
        float f = f1;
        if (f2 > 0.0F && f2 + f > paramFloat1) {
          a(table1, table2);
          (table2 = (new Table()).center()).defaults().center();
          f2 = 0.0F;
        } 
        BitmapFont bitmapFont = null;
        if (b.c != null && ld.eG >= 0 && ld.eG < b.c.length)
          bitmapFont = b.c[ld.eG]; 
        if (bitmapFont != null && bitmapFont.getTexture() != null) {
          bitmapFont.getTexture().setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
          bitmapFont.getTexture().setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
          (image = new Image((Drawable)new TextureRegionDrawable((TextureRegion)bitmapFont))).setScaling(Scaling.fit);
          table2.add((Actor)image).size(f1).padLeft(2.0F).padRight(2.0F).center();
          f2 += f + 4.0F;
        } 
        continue;
      } 
      String[] arrayOfString;
      int i = (arrayOfString = ((ld)image).aO.split("(?<=\\s)|(?=\\s)")).length;
      for (byte b = 0; b < i; b++) {
        String str;
        if (!(str = arrayOfString[b]).isEmpty()) {
          Label label;
          glyphLayout.setText(paramLabelStyle.font, str);
          float f;
          if ((f = glyphLayout.width * paramFloat2) > paramFloat1) {
            if ((table2.getChildren()).size > 0) {
              a(table1, table2);
              (table2 = (new Table()).center()).defaults().center();
              f2 = 0.0F;
            } 
            StringBuilder stringBuilder = new StringBuilder();
            for (byte b1 = 0; b1 < str.length(); b1++) {
              stringBuilder.append(str.charAt(b1));
              glyphLayout.setText(paramLabelStyle.font, stringBuilder);
              if (glyphLayout.width * paramFloat2 > paramFloat1)
                if (stringBuilder.length() > 1) {
                  char c = stringBuilder.charAt(stringBuilder.length() - 1);
                  stringBuilder.setLength(stringBuilder.length() - 1);
                  Label label1;
                  (label1 = new Label(stringBuilder.toString(), paramLabelStyle)).setFontScale(paramFloat2);
                  label1.setWrap(false);
                  label1.setAlignment(1);
                  table2.add((Actor)label1).center();
                  a(table1, table2);
                  (table2 = (new Table()).center()).defaults().center();
                  float f3 = 0.0F;
                  stringBuilder.setLength(0);
                  stringBuilder.append(c);
                } else {
                  Label label1;
                  (label1 = new Label(stringBuilder.toString(), paramLabelStyle)).setFontScale(paramFloat2);
                  label1.setWrap(false);
                  label1.setAlignment(1);
                  table2.add((Actor)label1).center();
                  a(table1, table2);
                  (table2 = (new Table()).center()).defaults().center();
                  f2 = 0.0F;
                  stringBuilder.setLength(0);
                }  
            } 
            if (stringBuilder.length() > 0) {
              (label = new Label(stringBuilder.toString(), paramLabelStyle)).setFontScale(paramFloat2);
              label.setWrap(false);
              label.setAlignment(1);
              table2.add((Actor)label).center();
              glyphLayout.setText(paramLabelStyle.font, stringBuilder);
              f2 = glyphLayout.width * paramFloat2;
            } 
          } else {
            if (f2 > 0.0F && f2 + label > paramFloat1) {
              a(table1, table2);
              (table2 = (new Table()).center()).defaults().center();
              f2 = 0.0F;
            } 
            Label label1;
            (label1 = new Label(str, paramLabelStyle)).setFontScale(paramFloat2);
            label1.setWrap(false);
            label1.setAlignment(1);
            table2.add((Actor)label1).center();
            f2 += label;
          } 
        } 
      } 
    } 
    if ((table2.getChildren()).size > 0)
      a(table1, table2); 
    return table1;
  }
  
  private static String c(String paramString) {
    if (paramString == null || paramString.isEmpty())
      return ""; 
    StringBuilder stringBuilder = new StringBuilder(paramString.length());
    byte b = 0;
    while (b < paramString.length()) {
      if (b + 2 < paramString.length() && paramString.charAt(b) == '&& paramString.charAt(b + 1) == '&& D.containsKey(Character.valueOf(paramString.charAt(b + 2)))) {
        b += 3;
        continue;
      } 
      stringBuilder.append(paramString.charAt(b++));
    } 
    return stringBuilder.toString();
  }
  
  public static void ck() {
    if (m != null)
      m.toFront(); 
  }
  
  static {
    (D = new HashMap<>()).put(Character.valueOf('), Integer.valueOf(0));
    D.put(Character.valueOf('), Integer.valueOf(1));
    D.put(Character.valueOf('), Integer.valueOf(2));
    D.put(Character.valueOf('), Integer.valueOf(3));
    D.put(Character.valueOf('), Integer.valueOf(4));
    D.put(Character.valueOf('), Integer.valueOf(5));
    D.put(Character.valueOf('), Integer.valueOf(6));
    D.put(Character.valueOf('), Integer.valueOf(7));
    D.put(Character.valueOf('), Integer.valueOf(8));
    D.put(Character.valueOf('), Integer.valueOf(9));
    D.put(Character.valueOf('), Integer.valueOf(10));
    D.put(Character.valueOf('), Integer.valueOf(11));
    D.put(Character.valueOf('), Integer.valueOf(12));
    D.put(Character.valueOf('), Integer.valueOf(13));
    D.put(Character.valueOf('), Integer.valueOf(14));
    D.put(Character.valueOf('), Integer.valueOf(15));
    D.put(Character.valueOf('), Integer.valueOf(16));
    D.put(Character.valueOf('), Integer.valueOf(17));
    D.put(Character.valueOf('), Integer.valueOf(18));
    D.put(Character.valueOf('), Integer.valueOf(19));
    D.put(Character.valueOf('), Integer.valueOf(20));
    D.put(Character.valueOf('), Integer.valueOf(21));
    D.put(Character.valueOf('), Integer.valueOf(22));
    D.put(Character.valueOf('), Integer.valueOf(23));
  }
}
