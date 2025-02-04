[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-large-screen-and-foldable-support.html)
  * [中文](/cn/current/Manual/android-large-screen-and-foldable-support.html)
  * [日本語](/ja/current/Manual/android-large-screen-and-foldable-support.html)
  * [한국어](/kr/current/Manual/android-large-screen-and-foldable-support.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-large-screen-and-foldable-support.html)
  * [中文](/cn/current/Manual/android-large-screen-and-foldable-support.html)
  * [日本語](/ja/current/Manual/android-large-screen-and-foldable-support.html)
  * [한국어](/kr/current/Manual/android-large-screen-and-foldable-support.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Optimization for Android](android-optimization.html)
  * Large screen and foldable device support

[](android-optimize-for-user-preferences.html)

Optimize for user preferences

[](PluginsForAndroid.html)

Create and use plug-ins in Android

# Large screen and foldable device support

On large screen and foldable devices running Android 12 or newer, your
application can run simultaneously with other applications in multi-window
mode, irrespective of its default configuration. If your application is
designed for a specific orientation or **aspect ratio** The relationship of an
image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio), or is non-resizable, the Android
OS automatically switches it into [compatibility
mode](https://developer.android.com/guide/topics/large-screens/large-screen-
compatibility-mode). In this mode, the Android OS scales your application to
fit the available screen size. However, in some cases, the application might
not be optimized for a specific screen size, resulting in a suboptimal user
experience.

**Note** : For devices running Android 12 or newer versions, [multi-window
mode](https://developer.android.com/guide/topics/large-screens/multi-window-
support) is the default behavior.

To ensure consistent user experience, consider designing your application to
adapt to various screen sizes, including large screen and foldable devices.
You can use the following settings and APIs.

## Resizeable Activity Player setting

The [**Resizeable Activity**](class-PlayerSettingsAndroid.html#resizeable)
Player setting enables multi-window mode in your application and allows the
Android OS to consider it resizable. For new projects, Unity enables this
setting by default and sets `android.resizeableActivity="true"` in the Android
manifest file. In this case, the aspect ratio restrictions are ignored.

If you choose to set `android.resizeableActivity="false"`, the Android OS
behaves in the following way:

**Android OS version** | **Behavior**  
---|---  
**Older than Android 12** | Displays your application as full-screen and disables multi-window mode.  
**Android 12 and newer** | Enables multi-window mode by default and activates the compatibility mode for your application to adjust it to the available screen dimensions.  
  
In the compatibility mode, the application might not display as expected. In
scenarios such as transitioning between screens on large screens and foldable
devices, the OS might prompt the user to restart the application. Restarting
the application causes loss of activity and the overall application state.

**Note** : On small-screen devices running Android 12 or newer versions, a
resizable application supports multi-window mode based on the
[minWidth](https://developer.android.com/reference/android/content/pm/ActivityInfo.WindowLayout#attr_android:minWidth)
and
[minHeight](https://developer.android.com/reference/android/content/pm/ActivityInfo.WindowLayout#attr_android:minHeight)
of the activity. A non-resizable application doesn’t support multi-window mode
on small-screen devices.

## Application and Configuration APIs

The [AndroidApplication
API](../ScriptReference/Android.AndroidApplication.html) provides information
on your Android application while it runs on a device. You can use this API to
perform the following actions:

  * Access the current activity’s Java instance.
  * Invoke events on the **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) thread or main thread of your application.

  * Detect and handle configuration changes while your application runs on a device.

Using the
[AndroidApplication.onConfigurationChanged](../ScriptReference/Android.AndroidApplication-
onConfigurationChanged.html) method, you can detect any device configuration
changes. You can retrieve device information, such as screen layout, screen
size, and orientation. The method also retrieves additional configuration
details, such as whether the screen is folded or unfolded, the type of
keyboard in use, and user preferences for language and region. For more
information on which device properties you can retrieve, refer to
[AndroidConfiguration
API](../ScriptReference/Android.AndroidConfiguration.html). Use the
[AndroidApplication.onConfigurationChanged](../ScriptReference/Android.AndroidApplication-
onConfigurationChanged.html) method to make necessary adjustments, such as
rearranging the user interface, to ensure your application adapts seamlessly
to different device configurations.

## Additional resources

  * [Android documentation on resizeableActivity](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity)

[](android-optimize-for-user-preferences.html)

Optimize for user preferences

[](PluginsForAndroid.html)

Create and use plug-ins in Android

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

