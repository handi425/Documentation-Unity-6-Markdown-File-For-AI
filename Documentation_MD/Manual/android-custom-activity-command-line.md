[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-custom-activity-command-line.html)
  * [中文](/cn/current/Manual/android-custom-activity-command-line.html)
  * [日本語](/ja/current/Manual/android-custom-activity-command-line.html)
  * [한국어](/kr/current/Manual/android-custom-activity-command-line.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-custom-activity-command-line.html)
  * [中文](/cn/current/Manual/android-custom-activity-command-line.html)
  * [日本語](/ja/current/Manual/android-custom-activity-command-line.html)
  * [한국어](/kr/current/Manual/android-custom-activity-command-line.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Android application entry points](android-application-entries.html)
  * [The Activity application entry point](android-application-entries-activity.html)
  * [Extend the default Unity activity](AndroidUnityPlayerActivity.html)
  * Specify Android Player command-line arguments

[](android-custom-activity.html)

Create a custom activity

[](android-application-entries-game-activity.html)

The GameActivity application entry point

# Specify Android Player command-line arguments

A use-case for extending the custom Unity activity is to pass command-line
arguments when you launch the Android Player. For information on the available
command-line arguments, refer to [Command-line
arguments](CommandLineArguments.html).

To specify startup command-line arguments in custom activity:

  1. [Create a custom activity](android-custom-activity.html) and set it as the application entry point.
  2. In the custom activity, override the `String UnityPlayerActivity.updateUnityCommandLineArguments(String cmdLine)` method.
  3. In the method, concatenate the `cmdLine` argument with your own startup arguments then return the result. **Important** : The `cmdLine` argument can be an empty string or null so make sure your code handles these possible values.

The following example shows how to specify startup arguments to select the
graphics API based on the current device:

    
    
    package com.company.product;
    import com.unity3d.player.UnityPlayerActivity;
    import android.os.Bundle;
    import android.os.Build;
    
    public class OverrideExample extends UnityPlayerActivity {
        private boolean preferVulkan() {
            // Use Vulkan on Google Pixel devices
            if (Build.MANUFACTURER.equals("Google") && Build.MODEL.startsWith("Pixel"))
                return true;
            else
                return false;
        }
    
        private String appendCommandLineArgument(String cmdLine, String arg) {
            if (arg == null || arg.isEmpty())
                return cmdLine;
            else if (cmdLine == null || cmdLine.isEmpty())
                return arg;
            else
                return cmdLine + " " + arg; 
        } 
    
        @Override protected String updateUnityCommandLineArguments(String cmdLine)
        {
            if (preferVulkan())
                return appendCommandLineArgument(cmdLine, "-force-vulkan");
            else
                return cmdLine; // let Unity pick the Graphics API based on PlayerSettings
        }
    
        @Override protected void onCreate(Bundle savedInstanceState)
        {
            super.onCreate(savedInstanceState);
        }
    }
    

### Additional ways to specify command-line arguments

Apart from the custom activity, you can specify command-line arguments in the
following ways:

  * **In Android Studio** : If you open your project in Android Studio, you can pass startup command-line arguments to Unity through Launch Flags in [Run/Debug Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
  * **Via Android Debug Bridge (adb)** : You can pass command-line arguments by launching an Android application via **adb** An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building. [More info](https://developer.android.com/studio/command-line/adb.html)  
See in [Glossary](Glossary.html#ADB) using the following code.

    
    
    adb shell am start -n "<package_name>/<activity_name>" -e unity <command_line_arguments>
    

The following example shows how to pass `-systemallocator` command-line
argument to your application.

    
    
    adb shell am start -n "com.Company.MyGame/com.unity3d.player.UnityPlayerActivity" -e unity -systemallocator
    
    

[](android-custom-activity.html)

Create a custom activity

[](android-application-entries-game-activity.html)

The GameActivity application entry point

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

