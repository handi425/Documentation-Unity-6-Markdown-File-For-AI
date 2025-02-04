[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-application-entries-game-activity-update-library.html)
  * [中文](/cn/current/Manual/android-application-entries-game-activity-update-library.html)
  * [日本語](/ja/current/Manual/android-application-entries-game-activity-update-library.html)
  * [한국어](/kr/current/Manual/android-application-entries-game-activity-update-library.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-application-entries-game-activity-update-library.html)
  * [中文](/cn/current/Manual/android-application-entries-game-activity-update-library.html)
  * [日本語](/ja/current/Manual/android-application-entries-game-activity-update-library.html)
  * [한국어](/kr/current/Manual/android-application-entries-game-activity-update-library.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Android application entry points](android-application-entries.html)
  * [The GameActivity application entry point](android-application-entries-game-activity.html)
  * Update the GameActivity library

[](android-application-entries-game-activity-modify-bridge.html)

Modify GameActivity bridge code

[](android-application-entries-set.html)

Set the application entry point for your Android application

## Update the GameActivity library

The GameActivity application entry point is implemented as a library separate
from the Unity Editor which means that you can update the library
independently. This is useful if Google provides bug fixes that your project
requires because you can acquire the fixes via a GameActivity library version
update.

**Note** : Unity doesn’t test all combinations of Unity version and
GameActivity library version. If you update to a newer GameActivity library
version, test your application thoroughly.

To update the GameActivity library version, change the value of the
`androidx.games:games-activity` dependency in `build.gradle`. For information
on the possible methods to do this, refer to [Modify Gradle project
files](android-modify-gradle-project-files.html).

**Note** : Make sure that the other AndroidX dependencies support the
GameActivity version that you want to use. If they don’t you must update them
too. For more information, refer to [Declaring
dependencies](https://developer.android.com/jetpack/androidx/releases/games#declaring-
dependencies).

## Additional resources

  * [Modify GameActivity bridge code](android-application-entries-game-activity-modify-bridge.html)

[](android-application-entries-game-activity-modify-bridge.html)

Modify GameActivity bridge code

[](android-application-entries-set.html)

Set the application entry point for your Android application

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

