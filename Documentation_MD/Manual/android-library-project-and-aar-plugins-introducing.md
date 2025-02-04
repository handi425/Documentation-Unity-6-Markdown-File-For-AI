[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-library-project-and-aar-plugins-introducing.html)
  * [中文](/cn/current/Manual/android-library-project-and-aar-plugins-introducing.html)
  * [日本語](/ja/current/Manual/android-library-project-and-aar-plugins-introducing.html)
  * [한국어](/kr/current/Manual/android-library-project-and-aar-plugins-introducing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-library-project-and-aar-plugins-introducing.html)
  * [中文](/cn/current/Manual/android-library-project-and-aar-plugins-introducing.html)
  * [日本語](/ja/current/Manual/android-library-project-and-aar-plugins-introducing.html)
  * [한국어](/kr/current/Manual/android-library-project-and-aar-plugins-introducing.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Create and use plug-ins in Android](PluginsForAndroid.html)
  * [Android plug-in types](android-plugin-types.html)
  * [Android Library Projects and Android Archive plug-ins](AndroidAARPlugins.html)
  * Introducing Android Library Projects and Android Archive plug-ins

[](AndroidAARPlugins.html)

Android Library Projects and Android Archive plug-ins

[](android-library-project-import.html)

Import an Android Library Project

# Introducing Android Library Projects and Android Archive plug-ins

Android Archives are a compiled version of Android Libraries, and are the
recommended way to format plug-ins that you want to distribute. However, while
you create a **plug-in** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in), it’s faster to work with the Android
Library format since that doesn’t require you to compile the plug-in outside
of Unity and re-import the result. If you plan to modify the plug-in at all in
the future, or want to iterate over it often, use an Android Library. After
you finish development for the plug-in, compile it into an Android Archive.

## Android Library projects

An Android Library is a directory with a specific structure that contains all
the plug-in assets and the manifest.

When Unity creates the final **Gradle** An Android build system that automates
several build processes. This automation means that many common build errors
are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project during the build or export
process, it automatically includes all Android Library Projects in it and
builds them together. Unity does this in the same way that Android Studio
projects build when they have multiple subprojects.

## Android Archive plug-ins

An Android Archive (AAR) plug-in is a compiled version of an Android Library
project that you can use as a dependency for an Android app module. The `.aar`
file itself is a `.zip` archive that contains all of the compiled code,
assets, and plug-in manifest. For more information on the structure of an AAR,
see [Anatomy of an AAR
file](https://developer.android.com/studio/projects/android-library.html#aar-
contents).

## Providing additional Android Assets and resources

If you need to add Assets to your Unity application that should be copied as
they are into the output package, include the raw assets in an Android Library
Project or AAR. To access these assets, call the
[getAssets](https://developer.android.com/reference/android/content/res/Resources.html#getAssets\(\))
Android API from your Java code.

## Additional resources

  * [Import an Android Library Project](android-library-project-import.html)
  * [Import an Android Archive plug-in](android-aar-import.html)

[](AndroidAARPlugins.html)

Android Library Projects and Android Archive plug-ins

[](android-library-project-import.html)

Import an Android Library Project

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

