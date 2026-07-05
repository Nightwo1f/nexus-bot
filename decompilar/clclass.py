package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.Version;
import com.badlogic.gdx.utils.TimeUtils;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.atomic.AtomicBoolean;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;

public final class cl {
  private static final AtomicBoolean a = new AtomicBoolean(false);
  
  public static void a(cr paramcr) {
    Thread.setDefaultUncaughtExceptionHandler((paramThread, paramThrowable) -> a(paramcr, paramThread, paramThrowable));
  }
  
  public static void a(cr paramcr, Thread paramThread, Throwable paramThrowable) {
    Throwable throwable1;
    if (!a.compareAndSet(false, true)) {
      throwable1 = paramThrowable;
      try {
        throwable1.printStackTrace();
      } catch (Throwable throwable) {}
      ae();
      return;
    } 
    Throwable throwable2 = paramThrowable;
    String str1 = a(paramThread, paramThrowable);
    String str2 = str1;
    try {
      if (Gdx.app != null)
        Gdx.app.error("CrashReporter", str2, throwable2); 
    } catch (Throwable throwable) {}
    str2 = str1;
    try {
      if (Gdx.files != null) {
        String str = "crash_" + (new SimpleDateFormat("yyyyMMdd_HHmmss")).format(new Date()) + "_" + TimeUtils.millis() + ".log";
        Gdx.files.local("crashes").child(str).writeString(str2, false, "UTF-8");
      } 
    } catch (Throwable throwable) {}
    try {
      if (Gdx.app != null) {
        Gdx.app.postRunnable(() -> {
              try {
                paramcr.setScreen((Screen)new cm(paramcr, paramString));
                return;
              } catch (Throwable throwable) {
                try {
                  throwable.printStackTrace();
                } catch (Throwable throwable1) {}
                m(paramString);
                ae();
                return;
              } 
            });
        return;
      } 
    } catch (Throwable throwable) {}
    m(str1);
    ae();
  }
  
  private static String a(Thread paramThread, Throwable paramThrowable) {
    StringWriter stringWriter = new StringWriter(8192);
    PrintWriter printWriter;
    (printWriter = new PrintWriter(stringWriter)).println("=== JTME CRASH REPORT ===");
    printWriter.println("Time: " + String.valueOf(new Date()));
    printWriter.println("Thread: " + ((paramThread == null) ? "?" : paramThread.getName()));
    try {
      printWriter.println("OS: " + System.getProperty("os.name") + " " + System.getProperty("os.version") + " (" + System.getProperty("os.arch") + ")");
    } catch (Throwable throwable) {}
    try {
      printWriter.println("Java: " + System.getProperty("java.version"));
    } catch (Throwable throwable) {}
    try {
      printWriter.println("LibGDX: " + Version.VERSION);
    } catch (Throwable throwable) {}
    printWriter.println();
    try {
      paramThrowable.printStackTrace(printWriter);
    } catch (Throwable throwable) {}
    printWriter.flush();
    return stringWriter.toString();
  }
  
  private static void ae() {
    try {
      if (Gdx.app != null)
        Gdx.app.exit(); 
    } catch (Throwable throwable) {}
    try {
      System.exit(1);
      return;
    } catch (Throwable throwable) {
      return;
    } 
  }
  
  private static void m(String paramString) {
    try {
      SwingUtilities.invokeLater(() -> {
            try {
              JTextArea jTextArea;
              (jTextArea = new JTextArea(paramString, 25, 90)).setEditable(false);
              JScrollPane jScrollPane = new JScrollPane(jTextArea);
              JOptionPane.showMessageDialog(null, jScrollPane, "JTME - Erro", 0);
              return;
            } catch (Throwable throwable) {
              return;
            } 
          });
      return;
    } catch (Throwable throwable) {
      return;
    } 
  }
}
