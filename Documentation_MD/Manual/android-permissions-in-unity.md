[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-permissions-in-unity.html)
  * [中文](/cn/current/Manual/android-permissions-in-unity.html)
  * [日本語](/ja/current/Manual/android-permissions-in-unity.html)
  * [한국어](/kr/current/Manual/android-permissions-in-unity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-permissions-in-unity.html)
  * [中文](/cn/current/Manual/android-permissions-in-unity.html)
  * [日本語](/ja/current/Manual/android-permissions-in-unity.html)
  * [한국어](/kr/current/Manual/android-permissions-in-unity.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Device features and permissions](android-device-features-and-permissions.html)
  * Android permissions in Unity

[](android-device-features-and-permissions.html)

Device features and permissions

[](android-permissions-declare.html)

Declare permissions for an application

# Android permissions in Unity

To get permission to access device features or data outside of your Unity
application’s sandbox, there are two stages:

  1. At build time, declare the permission in the application’s [Android App Manifest](android-manifest.html).
  2. At runtime, request permission from the user.

For some permissions, Unity automatically handles both the build-time Android
App Manifest entries and runtime permission requests. For more information,
see Unity-handled permissions.

## Declare permissions

An Android application can only request the user for permission to use device
features or data that it declares in its Android App Manifest. This is the
build-time stage of Android permission handling. For information on how to
declare permissions, see [Declare permissions for an application](android-
permissions-declare.html).

**Note** : If a **plug-in** A set of code created outside of Unity that
creates functionality in Unity. There are two kinds of plug-ins you can use in
Unity: Managed plug-ins (managed .NET assemblies created with tools like
Visual Studio) and Native plug-ins (platform-specific native code libraries).
[More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) declares a permission in its Android
App Manifest, **Gradle** An Android build system that automates several build
processes. This automation means that many common build errors are less likely
to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) automatically adds the permission to
the final Android App Manifest during the Gradle merge stage

## Runtime permissions

You can request runtime permissions at any time while the application is
running. It’s best practice to request permission for restricted data or a
device feature when the application requires the data/feature for the first
time. You should also show the user a message that explains why the
application requires the data/feature before you send the request. This is
important to give users context so they are less likely to deny the permission
out of confusion.

For information on how to request permission at runtime, see [Request runtime
permissions](android-RequestingPermissions.html).

**Important** : If you try to request the user for a permission that the
Android App Manifest doesn’t declare, the device doesn’t show the permission
dialogue.

## Unity-handled permissions

Depending on the [Player Settings](class-PlayerSettingsAndroid.html)Settings
that let you set various player-specific options for the final game built by
Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) and Unity APIs that the
application uses, Unity automatically adds some required permissions to the
Android App Manifest and sends permission requests at runtime. This also
applies to any plug-ins that the application uses.

To stop Unity from automatically sending permission requests at runtime, add
`unityplayer.SkipPermissionsDialog` to the Android App Manifest. This is
useful if you want to provide information about why the application requires
each permission before the user sees the permission request. In this case, you
need to send the permission requests manually. For more information, see
[Request runtime permissions](android-RequestingPermissions.html).

The following list explains which permissions Unity handles automatically:

  * If the application uses vibration such as [Handheld.Vibrate](../ScriptReference/Handheld.Vibrate.html), Unity adds the `VIBRATE` permission to the Android App Manifest.
  * If the application uses the [Application.internetReachability](../ScriptReference/Application-internetReachability.html) property, Unity adds the `ACCESS_NETWORK_STATE` permission to the Android App Manifest.
  * If the application uses a location API such as [LocationService](../ScriptReference/LocationService.html), Unity adds the `ACCESS_FINE_LOCATION` permission to the Android App Manifest and requests permission from the user the first time that the application uses location.
  * If the application uses the [WebCamTexture](../ScriptReference/WebCamTexture.html) class Unity adds the `CAMERA` permission to the Android App Manifest and requests permission from the user the first time that the application uses `WebCamTexture`.
  * If the application uses the [Microphone](../ScriptReference/Microphone.html) class adds the `RECORD_AUDIO` permission to the Android App Manifest and requests permission from the user the first time that the application uses `Microphone`.

## Additional resources

  * [Declare permissions for an application](android-permissions-declare.html)
  * [Request runtime permissions](android-RequestingPermissions.html)

[](android-device-features-and-permissions.html)

Device features and permissions

[](android-permissions-declare.html)

Declare permissions for an application

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

