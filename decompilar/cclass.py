package a;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.assets.loaders.FileHandleResolver;
import com.badlogic.gdx.files.FileHandle;

final class c implements FileHandleResolver {
  public final FileHandle resolve(String paramString) {
    FileHandle fileHandle1;
    FileHandle fileHandle2;
    return b.b(paramString) ? Gdx.files.absolute(paramString) : ((fileHandle2 = Gdx.files.internal(paramString)).exists() ? fileHandle2 : ((fileHandle1 = Gdx.files.absolute(paramString)).exists() ? fileHandle1 : fileHandle2));
  }
}
