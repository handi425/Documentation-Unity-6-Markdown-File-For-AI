[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AndroidJavaSourcePlugins.html)
  * [中文](/cn/current/Manual/AndroidJavaSourcePlugins.html)
  * [日本語](/ja/current/Manual/AndroidJavaSourcePlugins.html)
  * [한국어](/kr/current/Manual/AndroidJavaSourcePlugins.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AndroidJavaSourcePlugins.html)
  * [中文](/cn/current/Manual/AndroidJavaSourcePlugins.html)
  * [日本語](/ja/current/Manual/AndroidJavaSourcePlugins.html)
  * [한국어](/kr/current/Manual/AndroidJavaSourcePlugins.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Create and use plug-ins in Android](PluginsForAndroid.html)
  * [Android plug-in types](android-plugin-types.html)
  * Java and Kotlin source plug-ins

[](android-native-plugins-call.html)

Call native plug-in for Android code

[](android-plugins-java-code-from-c-sharp.html)

Call Java and Kotlin plug-in code from C# scripts

# Java and Kotlin source plug-ins

Unity can interpret individual Java and Kotlin source files as individual
**plug-ins** A set of code created outside of Unity that creates functionality
in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-
ins (managed .NET assemblies created with tools like Visual Studio) and Native
plug-ins (platform-specific native code libraries). [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Plug-in).

Unity supports Java and Kotlin code written in source files with `.java` and
`.kt` extensions. To do this, Unity interprets each source file as an
individual plug-in and compiles them when it builds the Player. This type of
plug-in is useful if you need to write a small amount of code for a single
project. If you plan to reuse the code in multiple projects or distribute it
to other people, then an [Android Library Project or Android Archive plug-
in](AndroidAARPlugins.html) might be more appropriate.

## Create a Java or Kotlin source plug-in

To indicate to Unity to create a plug-in from a Java (`.java`) or Kotlin
(`.kt`) source file:

  1. In the **Assets** folder, place your Java (`.java`) or Kotlin (`.kt`) source file.  
**Tip** : It’s best practice to create a sub-folder to contain your Java and
Kotlin source files.

  2. Select the source file and view it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

  3. In the Inspector, under the **Select Platforms for plugin** section, enable **Android**.
  4. Select **Apply**.

**Note** : You can place the source files in any folder in your Project,
except in special use locations such as StreamingAssets. If you place files in
these locations, the Unity Editor doesn’t display the plug-in inspector.

## Edit Java or Kotlin files in an exported Android Studio project

By default when you [export a Unity project for Android](android-export-
process.html), Unity copies any Java/Kotlin files over to the Android Studio
project. If you edit these files in Android Studio, the changes aren’t
reflected in the original files in the Unity project. If you export the Unity
project again, the export process will overwrite your changes in Android
Studio.

To resolve this, Unity provides the **Symlink Sources** [Build
Setting](android-build-settings.html). If you select this Build Setting, Unity
creates a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link) in the
Android Studio project to Java/Kotlin files in the Unity project, instead of
copying files over. This means that if you edit the files from Android Studio,
the edit affects the files in the original Unity project.

## Additional resources

  * [Android plug-in types](android-plugin-types.html)
  * [Call Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)

[](android-native-plugins-call.html)

Call native plug-in for Android code

[](android-plugins-java-code-from-c-sharp.html)

Call Java and Kotlin plug-in code from C# scripts

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

