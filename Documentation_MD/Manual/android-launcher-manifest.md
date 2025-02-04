[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-launcher-manifest.html)
  * [中文](/cn/current/Manual/android-launcher-manifest.html)
  * [日本語](/ja/current/Manual/android-launcher-manifest.html)
  * [한국어](/kr/current/Manual/android-launcher-manifest.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-launcher-manifest.html)
  * [中文](/cn/current/Manual/android-launcher-manifest.html)
  * [日本語](/ja/current/Manual/android-launcher-manifest.html)
  * [한국어](/kr/current/Manual/android-launcher-manifest.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Introducing Android](android-introducing.html)
  * Unity Launcher Manifest

[](android-manifest.html)

Android App Manifest

[](android-library-manifest.html)

Unity Library Manifest

# Unity Launcher Manifest

A Unity Launcher Manifest configures how the application looks and behaves
before the application launches. For example, it contains the application’s
icon, name, and install location. The Unity Launcher Manifest is a Unity-
specific concept for Android development and you can overwrite it to integrate
Unity as a component into an existing project. For more information, see
[Integrating Unity into Android applications](UnityasaLibrary-Android.html).

## Settings

You can configure all the settings in the Unity Launcher Manifest from
[Unity’s Player Settings](class-PlayerSettingsAndroid.html). This means,
unless you want to integrate Unity as a component into an existing project,
you don’t need to overwrite the Unity Launcher Manifest or manually edit any
settings directly in the file.

A Unity Launcher Manifest file declares the following:

  * The package’s name.
  * The application’s icons.
  * The application’s name.
  * The application’s [starting activity](https://developer.android.com/guide/components/activities/intro-activities) and its intents.
  * The application’s install location.
  * The application’s supported screen sizes.
  * The application’s `isGame` flag.  
**Note** : This setting is exclusively used by AndroidTV. If you don’t enable
AndroidTV support in [Player Settings](class-
PlayerSettingsAndroid.html)Settings that let you set various player-specific
options for the final game built by Unity. [More info](class-
PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings), Unity doesn’t declare this
setting.

[](android-manifest.html)

Android App Manifest

[](android-library-manifest.html)

Unity Library Manifest

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

