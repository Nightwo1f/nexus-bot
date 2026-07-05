package jtme.game.lwjgl3;

import com.badlogic.gdx.backends.lwjgl3.Lwjgl3ApplicationConfiguration;

public class Lwjgl3Launcher {
  public static void main(String[] paramArrayOfString) {
    Lwjgl3ApplicationConfiguration lwjgl3ApplicationConfiguration;
    (lwjgl3ApplicationConfiguration = new Lwjgl3ApplicationConfiguration()).setTitle("JTME");
    lwjgl3ApplicationConfiguration.useVsync(true);
    lwjgl3ApplicationConfiguration.setForegroundFPS((Lwjgl3ApplicationConfiguration.getDisplayMode()).refreshRate + 1);
    lwjgl3ApplicationConfiguration.setWindowedMode(640, 360);
    lwjgl3ApplicationConfiguration.setResizable(true);
    lwjgl3ApplicationConfiguration.setWindowSizeLimits(800, 600, -1, -1);
    lwjgl3ApplicationConfiguration.setWindowIcon(new String[] { "libgdx128.png", "libgdx64.png", "libgdx32.png", "libgdx16.png" });
    lwjgl3ApplicationConfiguration.setInitialVisible(false);
  }
}
