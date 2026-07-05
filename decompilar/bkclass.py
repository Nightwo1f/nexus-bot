package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.glutils.FrameBuffer;
import com.badlogic.gdx.utils.BufferUtils;
import com.badlogic.gdx.utils.ScreenUtils;
import java.nio.IntBuffer;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class bk {
  private static FrameBuffer a;
  
  private static SpriteBatch a;
  
  private static OrthographicCamera a;
  
  private static final Map u = new HashMap<>();
  
  private static long h = -1L;
  
  private static int aM = 0;
  
  private static final IntBuffer a = BufferUtils.newIntBuffer(16);
  
  public static boolean f() {
    long l;
    if ((l = Gdx.graphics.getFrameId()) != h) {
      h = l;
      aM = 0;
    } 
    return (aM < 2);
  }
  
  public static TextureRegion a(String paramString) {
    return (TextureRegion)u.get(paramString);
  }
  
  public static TextureRegion a(String paramString, List<bb> paramList, Color paramColor1, Color paramColor2, Color paramColor3, Color paramColor4) {
    if (a == null && a == null) {
      a = (IntBuffer)new FrameBuffer(Pixmap.Format.RGBA8888, 128, 128, false);
      a = (IntBuffer)new SpriteBatch();
      (a = (IntBuffer)new OrthographicCamera()).setToOrtho(true, 128.0F, 128.0F);
      ((OrthographicCamera)a).position.set(64.0F, 64.0F, 0.0F);
      a.update();
      a.setProjectionMatrix(((OrthographicCamera)a).combined);
    } 
    aM++;
    a.clear();
    Gdx.gl.glGetIntegerv(2978, a);
    a.begin();
    Gdx.gl.glClearColor(0.0F, 0.0F, 0.0F, 0.0F);
    Gdx.gl.glClear(16384);
    a.begin();
    for (byte b = 0; b < paramList.size(); b++) {
      bb bb;
      switch ((bb = paramList.get(b)).F) {
        case 1:
          a.setColor(paramColor1);
          break;
        case 2:
          a.setColor(paramColor2);
          break;
        case 3:
          a.setColor(paramColor3);
          break;
        case 4:
          a.setColor(paramColor4);
          break;
        default:
          a.setColor(Color.WHITE);
          break;
      } 
      a.draw(bb.j, 64.0F + bb.k.x, 64.0F + bb.k.y + bb.j.getRegionHeight(), bb.j.getRegionWidth(), -bb.j.getRegionHeight());
    } 
    a.end();
    Pixmap pixmap = ScreenUtils.getFrameBufferPixmap(0, 0, 128, 128);
    a.end();
    Gdx.gl.glViewport(a.get(0), a.get(1), a.get(2), a.get(3));
    Texture texture = new Texture(pixmap);
    pixmap.dispose();
    TextureRegion textureRegion;
    (textureRegion = new TextureRegion(texture)).flip(false, true);
    u.put(paramString, textureRegion);
    return textureRegion;
  }
}
