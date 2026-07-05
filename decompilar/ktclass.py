package a;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.MathUtils;
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

public final class kt {
  private static Actor g;
  
  static Group m;
  
  private static final Map B;
  
  public static void ck() {
    if (m != null)
      m.toFront(); 
  }
  
  public static void a(Stage paramStage, int paramInt1, int paramInt2, String paramString1, String paramString2, String paramString3, cq paramcq) {
    k k;
    if (g != null) {
      g.remove();
      g = null;
    } 
    Stage stage = paramStage;
    if (m == null || m.getStage() != stage) {
      if (m != null)
        m.remove(); 
      (m = new Group()).setName("PopupOverlay");
      m.setTransform(false);
      m.setTouchable(Touchable.disabled);
      stage.addActor((Actor)m);
    } 
    m.toFront();
    m.setZIndex((stage.getRoot().getChildren()).size - 1);
    boolean bool = (Gdx.app.getType() == Application.ApplicationType.Android || Gdx.app.getType() == Application.ApplicationType.iOS) ? true : false;
    Label.LabelStyle labelStyle = new Label.LabelStyle(b.a(paramString1), Color.WHITE);
    float f4 = 1.0F;
    if (bool) {
      if ((f4 = Math.min(paramStage.getViewport().getWorldWidth(), paramStage.getViewport().getWorldHeight()) * 0.045F / labelStyle.font.getLineHeight()) < 1.0F)
        f4 = 1.0F; 
      if (f4 > 4.5F)
        f4 = 4.5F; 
    } 
    float f5 = labelStyle.font.getCapHeight() * 1.3F * f4;
    TextureRegion textureRegion = null;
    if (paramInt2 == 4) {
      if ((k = b.a.a(paramInt1)) != null)
        textureRegion = k.b(0.0F); 
    } else {
      n n;
      if ((n = b.a.a(k)) != null)
        textureRegion = n.c(0.0F); 
    } 
    if (textureRegion != null && textureRegion.getTexture() != null) {
      textureRegion.getTexture().setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
      textureRegion.getTexture().setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
    } 
    float f1 = paramStage.getViewport().getWorldWidth();
    float f2 = paramStage.getViewport().getWorldHeight();
    float f7 = bool ? paramcq.am : 1.0F;
    float f8 = (textureRegion != null) ? (paramcq.bP * f7) : 0.0F;
    if (bool) {
      f9 = f1 * 0.9F;
    } else {
      f9 = Math.min(500.0F, f1 * 0.9F);
    } 
    float f9 = Math.max(150.0F, f9 - ((f8 > 0.0F) ? (f8 + 8.0F) : 0.0F) - 12.0F);
    Table table1;
    (table1 = new Table()).setTransform(false);
    table1.setBackground((Drawable)new NinePatchDrawable(b.v));
    table1.pad(6.0F);
    table1.setTouchable(Touchable.disabled);
    if (textureRegion != null) {
      float f = paramcq.bP;
      Image image;
      (image = new Image((Drawable)new TextureRegionDrawable(textureRegion))).setScaling(Scaling.none);
      image.setSize(textureRegion.getRegionWidth(), textureRegion.getRegionHeight());
      Group group;
      (group = new Group()).setTransform(true);
      group.setSize(f, f);
      group.addActor((Actor)image);
      image.setPosition(MathUtils.round((f - textureRegion.getRegionWidth()) / 2.0F), MathUtils.round((f - textureRegion.getRegionHeight()) / 2.0F));
      if (bool) {
        group.setScale(f7);
        group.setOrigin(1);
      } 
      Table table;
      (table = new Table()).defaults().center();
      table.add((Actor)group).size(f, f).center();
      table1.add((Actor)table).width(f8).height(f8).padRight(8.0F).expandY().center();
    } 
    Table table2 = new Table();
    Label label;
    (label = new Label(paramString1, labelStyle)).setAlignment(8);
    label.setFontScale(f4);
    label.setWrap(true);
    if (paramString2 != null && !paramString2.isEmpty()) {
      table2.add((Actor)label).width(f9 * 0.7F).expandX().left();
      Table table = a(paramString2, labelStyle, f5, Float.POSITIVE_INFINITY, f4);
      table2.add((Actor)table).right().padRight(4.0F);
    } else {
      table2.add((Actor)label).width(f9).expandX().left();
    } 
    table2.row();
    Table table3 = a(paramString3, labelStyle, f5, f9, f4);
    table2.add((Actor)table3).colspan(2).minWidth(f9).padTop(6.0F).left();
    table1.add((Actor)table2).expandY().center().row();
    table1.pack();
    float f6 = paramcq.bP;
    if (table1.getHeight() < f6)
      table1.setHeight(f6); 
    float f3 = (fj.au > 0.0F) ? fj.au : (f1 / 2.0F);
    if (bool) {
      float f10 = table1.getWidth();
      float f11 = table1.getHeight();
      f3 -= f10 / 2.0F;
      f3 = Math.max(10.0F, Math.min(f3, f1 - f10 - 10.0F));
      if ((f1 = f2 * 0.5F - f11 / 2.0F) < 10.0F)
        f1 = 10.0F; 
      table1.setPosition(Math.round(f3), Math.round(f1));
    } else {
      float f10 = f3 - table1.getWidth() / 2.0F;
      float f11 = (f2 - table1.getHeight()) / 2.0F - 90.0F;
      table1.setPosition(Math.round(f10), Math.round(f11));
    } 
    (table1.getColor()).a = 0.0F;
    m.addActor((Actor)table1);
    m.toFront();
    table1.toFront();
    table1.setZIndex((m.getChildren()).size - 1);
    g = (Actor)table1;
    table1.addAction((Action)Actions.parallel((Action)Actions.sequence((Action)Actions.fadeIn(0.05F), (Action)Actions.delay(4.0F), (Action)Actions.fadeOut(0.05F), (Action)Actions.run(() -> {
                paramTable.remove();
                if (g == paramTable)
                  g = null; 
              })), (Action)Actions.forever(new ku(paramStage, table1, bool))));
  }
  
  private static List d(String paramString) {
    ArrayList<kv> arrayList = new ArrayList();
    StringBuilder stringBuilder = new StringBuilder();
    for (byte b = 0; b < paramString.length(); b++) {
      int i;
      if ((i = paramString.charAt(b)) == '\n') {
        if (stringBuilder.length() > 0) {
          arrayList.add(kv.a(stringBuilder.toString()));
          stringBuilder.setLength(0);
        } 
        arrayList.add(new kv(kw.d, null, -1));
        b++;
        continue;
      } 
      if (b + 2 < paramString.length() && paramString.charAt(b) == '&& paramString.charAt(b + 1) == '&& B.containsKey(Character.valueOf(paramString.charAt(b + 2)))) {
        if (stringBuilder.length() > 0) {
          arrayList.add(kv.a(stringBuilder.toString()));
          stringBuilder.setLength(0);
        } 
        i = ((Integer)B.get(Character.valueOf(paramString.charAt(b + 2)))).intValue();
        arrayList.add(new kv(kw.c, null, i));
        b += 3;
        continue;
      } 
      stringBuilder.append(i);
    } 
    if (stringBuilder.length() > 0)
      arrayList.add(kv.a(stringBuilder.toString())); 
    return arrayList;
  }
  
  private static Table a(String paramString, Label.LabelStyle paramLabelStyle, float paramFloat1, float paramFloat2, float paramFloat3) {
    Table table1;
    (table1 = new Table()).top().left();
    table1.defaults().left();
    GlyphLayout glyphLayout = new GlyphLayout();
    Table table2;
    (table2 = (new Table()).left()).defaults().left();
    float f = 0.0F;
    Iterator<kv> iterator = d(paramString).iterator();
    while (iterator.hasNext()) {
      Image image;
      kv kv;
      if ((kv = iterator.next()).a == kw.d) {
        table1.add((Actor)table2).left().row();
        (table2 = (new Table()).left()).defaults().left();
        f = 0.0F;
        continue;
      } 
      if (kv.a == kw.c) {
        float f1 = paramFloat1;
        if (f > 0.0F && f + f1 > paramFloat2) {
          table1.add((Actor)table2).left().row();
          (table2 = (new Table()).left()).defaults().left();
          f = 0.0F;
        } 
        BitmapFont bitmapFont = null;
        if (b.c != null && kv.eE >= 0 && kv.eE < b.c.length)
          bitmapFont = b.c[kv.eE]; 
        if (bitmapFont != null && bitmapFont.getTexture() != null) {
          bitmapFont.getTexture().setFilter(Texture.TextureFilter.Nearest, Texture.TextureFilter.Nearest);
          bitmapFont.getTexture().setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge);
          (image = new Image((Drawable)new TextureRegionDrawable((TextureRegion)bitmapFont))).setScaling(Scaling.fit);
          table2.add((Actor)image).size(paramFloat1).padLeft(2.0F).padRight(2.0F).center();
          f += f1 + 4.0F;
        } 
        continue;
      } 
      String[] arrayOfString;
      int i = (arrayOfString = ((kv)image).aM.split("(?<=\\s)|(?=\\s)")).length;
      for (byte b = 0; b < i; b++) {
        String str;
        if (!(str = arrayOfString[b]).isEmpty()) {
          Label label;
          glyphLayout.setText(paramLabelStyle.font, str);
          float f1;
          if ((f1 = glyphLayout.width * paramFloat3) > paramFloat2) {
            if ((table2.getChildren()).size > 0) {
              table1.add((Actor)table2).left().row();
              (table2 = (new Table()).left()).defaults().left();
              f = 0.0F;
            } 
            StringBuilder stringBuilder = new StringBuilder();
            for (byte b1 = 0; b1 < str.length(); b1++) {
              stringBuilder.append(str.charAt(b1));
              glyphLayout.setText(paramLabelStyle.font, stringBuilder);
              if (glyphLayout.width * paramFloat3 > paramFloat2)
                if (stringBuilder.length() > 1) {
                  char c = stringBuilder.charAt(stringBuilder.length() - 1);
                  stringBuilder.setLength(stringBuilder.length() - 1);
                  Label label1;
                  (label1 = new Label(stringBuilder.toString(), paramLabelStyle)).setFontScale(paramFloat3);
                  label1.setWrap(false);
                  label1.setAlignment(8);
                  table2.add((Actor)label1).left();
                  table1.add((Actor)table2).left().row();
                  (table2 = (new Table()).left()).defaults().left();
                  float f2 = 0.0F;
                  stringBuilder.setLength(0);
                  stringBuilder.append(c);
                } else {
                  Label label1;
                  (label1 = new Label(stringBuilder.toString(), paramLabelStyle)).setFontScale(paramFloat3);
                  label1.setWrap(false);
                  label1.setAlignment(8);
                  table2.add((Actor)label1).left();
                  table1.add((Actor)table2).left().row();
                  (table2 = (new Table()).left()).defaults().left();
                  f = 0.0F;
                  stringBuilder.setLength(0);
                }  
            } 
            if (stringBuilder.length() > 0) {
              (label = new Label(stringBuilder.toString(), paramLabelStyle)).setFontScale(paramFloat3);
              label.setWrap(false);
              label.setAlignment(8);
              table2.add((Actor)label).left();
              glyphLayout.setText(paramLabelStyle.font, stringBuilder);
              f = glyphLayout.width * paramFloat3;
            } 
          } else {
            if (f > 0.0F && f + label > paramFloat2) {
              table1.add((Actor)table2).left().row();
              (table2 = (new Table()).left()).defaults().left();
              f = 0.0F;
            } 
            Label label1;
            (label1 = new Label(str, paramLabelStyle)).setFontScale(paramFloat3);
            label1.setWrap(false);
            label1.setAlignment(8);
            table2.add((Actor)label1).left();
            f += label;
          } 
        } 
      } 
    } 
    if ((table2.getChildren()).size > 0)
      table1.add((Actor)table2).left().row(); 
    return table1;
  }
  
  static {
    (B = new HashMap<>()).put(Character.valueOf('), Integer.valueOf(0));
    B.put(Character.valueOf('), Integer.valueOf(1));
    B.put(Character.valueOf('), Integer.valueOf(2));
    B.put(Character.valueOf('), Integer.valueOf(3));
    B.put(Character.valueOf('), Integer.valueOf(4));
    B.put(Character.valueOf('), Integer.valueOf(5));
    B.put(Character.valueOf('), Integer.valueOf(6));
    B.put(Character.valueOf('), Integer.valueOf(7));
    B.put(Character.valueOf('), Integer.valueOf(8));
    B.put(Character.valueOf('), Integer.valueOf(9));
    B.put(Character.valueOf('), Integer.valueOf(10));
    B.put(Character.valueOf('), Integer.valueOf(11));
    B.put(Character.valueOf('), Integer.valueOf(12));
    B.put(Character.valueOf('), Integer.valueOf(13));
    B.put(Character.valueOf('), Integer.valueOf(14));
    B.put(Character.valueOf('), Integer.valueOf(15));
    B.put(Character.valueOf('), Integer.valueOf(16));
    B.put(Character.valueOf('), Integer.valueOf(17));
    B.put(Character.valueOf('), Integer.valueOf(18));
    B.put(Character.valueOf('), Integer.valueOf(19));
    B.put(Character.valueOf('), Integer.valueOf(20));
    B.put(Character.valueOf('), Integer.valueOf(21));
    B.put(Character.valueOf('), Integer.valueOf(22));
    B.put(Character.valueOf('), Integer.valueOf(23));
  }
}
