package com.example.pengguolong.testpremithook;

import android.app.Activity;
import android.view.View;
import android.view.WindowManager;

/**
 * @author pengguolong
 * created 2023-04-19 21:16:44
 */
public class WallpaperActivity  extends Activity {

    @Override
    public void setContentView(View view) {
        super.setContentView(view);

        setContentView(R.layout.activity_wallpaper);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER);
    }
}