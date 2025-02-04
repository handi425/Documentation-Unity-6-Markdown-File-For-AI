[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-native-plugins-create.html)
  * [中文](/cn/current/Manual/android-native-plugins-create.html)
  * [日本語](/ja/current/Manual/android-native-plugins-create.html)
  * [한국어](/kr/current/Manual/android-native-plugins-create.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-native-plugins-create.html)
  * [中文](/cn/current/Manual/android-native-plugins-create.html)
  * [日本語](/ja/current/Manual/android-native-plugins-create.html)
  * [한국어](/kr/current/Manual/android-native-plugins-create.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Create and use plug-ins in Android](PluginsForAndroid.html)
  * [Android plug-in types](android-plugin-types.html)
  * [Native plug-ins for Android](AndroidNativePlugins.html)
  * Create a native plug-in for Android

[](android-native-plugins-introducing.html)

Introducing native plug-ins for Android

[](android-native-plugins-import.html)

Import a native plug-in for Android

# Create a native plug-in for Android

To compile a C++ **plug-in** A set of code created outside of Unity that
creates functionality in Unity. There are two kinds of plug-ins you can use in
Unity: Managed plug-ins (managed .NET assemblies created with tools like
Visual Studio) and Native plug-ins (platform-specific native code libraries).
[More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) for Android, use the [Android
NDK](https://developer.android.com/ndk/index.html) and familiarize yourself
with the steps required to build a shared library or a static library.

If you use C++ to implement the plug-in, you must declare with C linkage to
avoid [name mangling issues](http://en.wikipedia.org/wiki/Name_mangling). By
default, only C source files that have a .c file extension in the plug-ins
have C linkage (not C++).

    
    
    extern "C" {
      float Foopluginmethod ();
    }
    

**Note** : If your static library isn’t compiled with `-fno-exceptions` and
`-fno-rtti` flags, compatibility issues might cause application build failure.

## Additional resources

  * [Import a native plug-in for Android](android-native-plugins-import.html)

[](android-native-plugins-introducing.html)

Introducing native plug-ins for Android

[](android-native-plugins-import.html)

Import a native plug-in for Android

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

