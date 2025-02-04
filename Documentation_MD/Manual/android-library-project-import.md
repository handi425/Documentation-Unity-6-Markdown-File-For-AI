[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-library-project-import.html)
  * [中文](/cn/current/Manual/android-library-project-import.html)
  * [日本語](/ja/current/Manual/android-library-project-import.html)
  * [한국어](/kr/current/Manual/android-library-project-import.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-library-project-import.html)
  * [中文](/cn/current/Manual/android-library-project-import.html)
  * [日本語](/ja/current/Manual/android-library-project-import.html)
  * [한국어](/kr/current/Manual/android-library-project-import.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Create and use plug-ins in Android](PluginsForAndroid.html)
  * [Android plug-in types](android-plugin-types.html)
  * [Android Library Projects and Android Archive plug-ins](AndroidAARPlugins.html)
  * Import an Android Library Project

[](android-library-project-and-aar-plugins-introducing.html)

Introducing Android Library Projects and Android Archive plug-ins

[](android-aar-import.html)

Import an Android Archive plug-in

# Import an Android Library Project

To import an [Android Library Project](AndroidAARPlugins.html) into your Unity
Project, perform the following steps:

  1. Copy the Android Library Project to the **Assets** folder of your Unity Project.
  2. If the Android Library Project root folder doesn’t use the `.androidlib` extension, add this extension to the folder. For example, `mylibrary.androidlib`.

Unity now supports the Android Library Project and includes it in the final
project that [Gradle](android-gradle-overview.html)An Android build system
that automates several build processes. This automation means that many common
build errors are less likely to occur. [More info](android-gradle-
overview.html)  
See in [Glossary](Glossary.html#Gradle) uses to build your application. For
more information, refer to [How Unity builds Android applications](how-unity-
builds-android-applications.html).

## Configure an Android Library Project

Android Library Project is a dependency of a built-in module **unityLibrary**.
You can change this default behavior. For example, you can configure an
Android Library Project to depend on **unityLibrary** instead. To do this, use
the following steps:

  1. In the **Project** window, select the `.androidlib` **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) to access the ****Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window.

  2. In the **Select dependent module** section, select **None**.

![](../uploads/Android/android-libproject-dependent-module.png)

  3. Add the following code in your plug-in’s build gradle **dependencies** scope:
    
        dependencies {
        ...
        implementation project(':unityLibrary')
        implementation fileTree(dir: project(':unityLibrary').getProjectDir().toString() + ('\\libs'), include: ['*.jar'])
    }
    

You also have the option to include Android Library Project as a dependency of
the **launcher** or both **unityLibrary** and **launcher** built-in modules.

## Additional resources

  * [Call Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)

[](android-library-project-and-aar-plugins-introducing.html)

Introducing Android Library Projects and Android Archive plug-ins

[](android-aar-import.html)

Import an Android Archive plug-in

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

