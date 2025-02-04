[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-library-manifest.html)
  * [中文](/cn/current/Manual/android-library-manifest.html)
  * [日本語](/ja/current/Manual/android-library-manifest.html)
  * [한국어](/kr/current/Manual/android-library-manifest.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-library-manifest.html)
  * [中文](/cn/current/Manual/android-library-manifest.html)
  * [日本語](/ja/current/Manual/android-library-manifest.html)
  * [한국어](/kr/current/Manual/android-library-manifest.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Introducing Android](android-introducing.html)
  * Unity Library Manifest

[](android-launcher-manifest.html)

Unity Launcher Manifest

[](how-unity-builds-android-applications.html)

How Unity builds Android applications

# Unity Library Manifest

A Unity Library Manifest is the main Unity manifest and contains information
about the Unity Player and its
[activity](https://developer.android.com/guide/components/activities/intro-
activities). Unity uses a default Unity Library Manifest during the build
process to generate the final [Android App Manifest](android-manifest.html)
for the application. For more information on how to modify this file, refer to
[Modify Gradle project files](android-modify-gradle-project-files.html).

## Settings

A Unity Library Manifest declares:

  * The Unity [activity](https://developer.android.com/guide/components/activities/intro-activities).
  * The theme that the Unity activity uses.
  * Permissions.
  * **VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) modes.

  * VR performance.
  * Whether to allow the user to resize the application window. This is useful for VR.
  * The maximum **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio).

  * How to react to configuration changes.
  * Supported orientations.
  * Supported launch modes.   
**Note** : Unity only supports the [singleTask launch
mode](https://developer.android.com/guide/topics/manifest/activity-
element.html#lmode).

  * Android **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI).

  * Whether to use hardware acceleration.
  * Which features the application uses such as a gamepad or touchscreen.
  * Which graphics APIs the application supports.
  * Whether the application supports notches on the device.
  * The initial window size.
  * Splash screen configuration.
  * Whether to extract native libraries when installing the application.
  * Which devices the application can run on.

[](android-launcher-manifest.html)

Unity Launcher Manifest

[](how-unity-builds-android-applications.html)

How Unity builds Android applications

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

