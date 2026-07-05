package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Net;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.EventListener;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;

final class if implements Net.HttpResponseListener {
  if(hy paramhy) {}
  
  public final void handleHttpResponse(Net.HttpResponse paramHttpResponse) {
    String str = paramHttpResponse.getResultAsString().trim();
    try {
      int i = Integer.parseInt(str);
      int j = this.g.q.f.bJ;
      if (i > j)
        Gdx.app.postRunnable(() -> {
              hy hy1;
              boolean bool;
              String str;
              if ((str = b.a(bool = (hy1 = this.g).q.f.S, "id_update_available")) == null)
                str = "New Update Available! Click to Download"; 
              TextButton textButton;
              (textButton = hy.a(str)).setColor(1.0F, 0.8F, 0.2F, 1.0F);
              textButton.addListener((EventListener)new ig(hy1, textButton, bool));
              hy1.s.row();
              hy1.s.add((Actor)textButton).growX().height(hy1.bG).padTop(10.0F);
            }); 
      return;
    } catch (NumberFormatException numberFormatException) {
      Gdx.app.error("Update", "Error reading server version.", numberFormatException);
      return;
    } 
  }
  
  public final void failed(Throwable paramThrowable) {
    Gdx.app.error("Update", "Failed to connect to update server.", paramThrowable);
  }
  
  public final void cancelled() {}
}
