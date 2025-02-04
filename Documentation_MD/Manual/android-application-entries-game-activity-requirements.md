[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-application-entries-game-activity-requirements.html)
  * [中文](/cn/current/Manual/android-application-entries-game-activity-requirements.html)
  * [日本語](/ja/current/Manual/android-application-entries-game-activity-requirements.html)
  * [한국어](/kr/current/Manual/android-application-entries-game-activity-requirements.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-application-entries-game-activity-requirements.html)
  * [中文](/cn/current/Manual/android-application-entries-game-activity-requirements.html)
  * [日本語](/ja/current/Manual/android-application-entries-game-activity-requirements.html)
  * [한국어](/kr/current/Manual/android-application-entries-game-activity-requirements.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Android application entry points](android-application-entries.html)
  * [The GameActivity application entry point](android-application-entries-game-activity.html)
  * GameActivity requirements and compatibility

[](android-application-entries-game-activity.html)

The GameActivity application entry point

[](android-application-entries-game-activity-modify-bridge.html)

Modify GameActivity bridge code

# GameActivity requirements and compatibility

GameActivity has the following dependencies:

  * CMake build system.
  * AndroidX

## CMake

GameActivity uses CMake to produce the bridge code (`libgame.so`) during the
build process.

**Note** : If you provide a custom Android SDK, be sure the SDK has CMake
3.22.1 included.

### AndroidX

GameActivity requires the following AndroidX **Gradle** An Android build
system that automates several build processes. This automation means that many
common build errors are less likely to occur. [More info](android-gradle-
overview.html)  
See in [Glossary](Glossary.html#Gradle) dependencies:

  * `androidx.appcompat:appcompat`
  * `androidx.games:games-activity`
  * `androidx.core:core`
  * `Androidx.constraintlayout`

Gradle installs AndroidX and these dependencies automatically.

## Plug-in compatibility

If you use GameActivity, your application player loop runs on a native thread
rather than a Java thread. This means that calling Java APIs like
[myLooper](https://developer.android.com/reference/android/os/Looper#myLooper\(\))
from [plug-ins](PluginsForAndroid.html)A set of code created outside of Unity
that creates functionality in Unity. There are two kinds of plug-ins you can
use in Unity: Managed plug-ins (managed .NET assemblies created with tools
like Visual Studio) and Native plug-ins (platform-specific native code
libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) will fail. In the case of `myLooper`
it’s because there’s no Java looper present on the native thread. This also
means that any API that uses APIs such as `myLooper` will also fail. For
example,
[registerInputDeviceListener](https://developer.android.com/reference/android/hardware/input/InputManager#registerInputDeviceListener\(android.hardware.input.InputManager.InputDeviceListener,%20android.os.Handler\))
will fail if the handler is null. It’s important to understand this limitation
when you create [Android plug-ins](PluginsForAndroid.html).

## Choreographer

If you use GameActivity, Unity tries to use the [NDK
choreographer](https://developer.android.com/ndk/reference/group/choreographer)
to synchronize frame times. If the [Device API
Level](../ScriptReference/AndroidSdkVersions.html) is lower than 24, or your
application uses a 32-bit Player and the Device API Level is lower than 29,
Unity uses the [Java
choreographer](https://developer.android.com/reference/android/view/Choreographer).

## Additional resources

  * [The Activity application entry point](android-application-entries-activity.html)

[](android-application-entries-game-activity.html)

The GameActivity application entry point

[](android-application-entries-game-activity-modify-bridge.html)

Modify GameActivity bridge code

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

