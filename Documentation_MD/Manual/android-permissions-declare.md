[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-permissions-declare.html)
  * [中文](/cn/current/Manual/android-permissions-declare.html)
  * [日本語](/ja/current/Manual/android-permissions-declare.html)
  * [한국어](/kr/current/Manual/android-permissions-declare.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-permissions-declare.html)
  * [中文](/cn/current/Manual/android-permissions-declare.html)
  * [日本語](/ja/current/Manual/android-permissions-declare.html)
  * [한국어](/kr/current/Manual/android-permissions-declare.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Device features and permissions](android-device-features-and-permissions.html)
  * Declare permissions for an application

[](android-permissions-in-unity.html)

Android permissions in Unity

[](android-RequestingPermissions.html)

Request runtime permissions

# Declare permissions for an application

Android applications declare what permissions they require in their [Android
App Manifest](android-manifest.html). This page explains how to manage
permissions for an Android application. For a list of the possible
permissions, see
[Manifest.permission](https://developer.android.com/reference/android/Manifest.permission).

You can use one of the following methods to modify the Android App Manifest
file and manage permissions:

  * Create a custom [Unity Library Manifest](android-library-manifest.html) template for Unity to generate the application’s Android App Manifest file from.
  * Export the project and modify the Android App Manifest file in Android Studio.
  * Use the Android Project Configuration manager to modify Android App Manifest file set up in the custom modules of your **gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project.

**Note** : Depending on the [Player Settings](class-
PlayerSettingsAndroid.html)Settings that let you set various player-specific
options for the final game built by Unity. [More info](class-
PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) and Unity APIs that the
application uses, Unity automatically adds some required permissions to the
Unity Library Manifest. For more information, see [Unity-handled
permissions](android-permissions-in-unity.html#unity-handled-permissions).

## Create a template Unity Library Manifest

Unity uses templates to produce the final Gradle project files. You can
override the template that Unity uses and new permissions for an application
via the template.

For more information, refer to [Modify Gradle project files with Gradle
template files](android-modify-gradle-project-files-templates.html).

## Use Android Studio

To have complete control over which permissions are in the final Android App
Manifest file, export the project and edit the Android App Manifest in Android
Studio.

For more information, refer to [Modify Gradle project files with Android
Studio](android-modify-gradle-project-files-android-studio.html).

## Use the Android Project Configuration Manager

Use Android Project Configuration Manager to set up and modify custom Gradle
project files in C#. You cannot modify the manifest stored in the default
`unityLibrary` and `launcher` modules of your gradle project. You can use the
API to set up a custom manifest file in a custom module and add new
permissions for your application.

For more information, refer to [Modify Gradle project files with Android
Project Configuration Manager](android-modify-gradle-project-files-agp.html).

## Additional resources

  * [Android permissions in Unity](android-permissions-in-unity.html)
  * [Request runtime permissions](android-RequestingPermissions.html)

[](android-permissions-in-unity.html)

Android permissions in Unity

[](android-RequestingPermissions.html)

Request runtime permissions

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

