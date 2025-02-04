[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-quit.html)
  * [中文](/cn/current/Manual/android-quit.html)
  * [日本語](/ja/current/Manual/android-quit.html)
  * [한국어](/kr/current/Manual/android-quit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-quit.html)
  * [中文](/cn/current/Manual/android-quit.html)
  * [日本語](/ja/current/Manual/android-quit.html)
  * [한국어](/kr/current/Manual/android-quit.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * Quit a Unity Android application

[](android-handle-crashes.html)

Handle Android crashes

[](android-building-and-delivering.html)

Building and delivering for Android

# Quit a Unity Android application

The Android operating system has a built-in user interface to hide and close
applications (refer to [Close
apps](https://support.google.com/android/answer/9079646?hl=en-
GB#zippy=%2Cclose-apps)) so you shouldn’t add your own interface to quit your
application. Users recognize Android’s interface as the way to close
applications so if you create your own, users will have an inconsistent user
experience between your application and other Android applications. If you
must programmatically close an Android application, it’s best practice to use
[Activity.moveTaskToBack](https://developer.android.com/reference/android/app/Activity#moveTaskToBack\(boolean\))
instead of [Application.Quit](../ScriptReference/Application.Quit.html).
`Activity.moveTaskToBack` pauses the application and moves it to the
background, which is closer to the standard Android application lifecycle than
what `Application.Quit` does. For more information, refer to [Processes and
app
lifecycle](https://developer.android.com/guide/components/activities/process-
lifecycle).

The following code sample shows how to move your application to the back of
the activity stack.

    
    
    using UnityEngine;
    
    public class QuitApplicationUtility
    {
        public static void MoveAndroidApplicationToBack()
        {
            AndroidJavaObject activity = new AndroidJavaClass("com.unity3d.player.UnityPlayer").GetStatic<AndroidJavaObject>("currentActivity");
            activity.Call<bool>("moveTaskToBack", true);
        }
    }
    

[](android-handle-crashes.html)

Handle Android crashes

[](android-building-and-delivering.html)

Building and delivering for Android

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

