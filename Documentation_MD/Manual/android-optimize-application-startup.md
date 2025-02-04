[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-optimize-application-startup.html)
  * [中文](/cn/current/Manual/android-optimize-application-startup.html)
  * [日本語](/ja/current/Manual/android-optimize-application-startup.html)
  * [한국어](/kr/current/Manual/android-optimize-application-startup.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-optimize-application-startup.html)
  * [中文](/cn/current/Manual/android-optimize-application-startup.html)
  * [日本語](/ja/current/Manual/android-optimize-application-startup.html)
  * [한국어](/kr/current/Manual/android-optimize-application-startup.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Optimization for Android](android-optimization.html)
  * Optimize application startup times

[](android-thread-configuration.html)

Android thread configuration

[](android-game-state-hinting.html)

Game state hinting

# Optimize application startup times

Android devices can optimize the startup process for an application to reduce
the time it takes the application to become interactive. For Android to do
this, the application must indicate when it finishes initialization and
becomes interactive for end users. Android then prioritizes work that must
complete before the application is initialized.

Android applications use the
[Activity.reportFullyDrawn](https://developer.android.com/reference/android/app/Activity#reportFullyDrawn\(\))
API to indicate that they have finished start-up. By default, Unity calls this
method as the first **scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) loads, before
[Awake](../ScriptReference/MonoBehaviour.Awake.html). However, if your
application must do some extra work before users can interact with it, for
example if the application needs to load some resources before it can show
anything on the screen, you should call this API yourself on the frame that
your application becomes interactive. To do this, call
[DiagnosticsReporting.CallReportFullyDrawn](../ScriptReference/Android.DiagnosticsReporting.CallReportFullyDrawn.html).
If you call this method somewhere in your code, Unity no longer calls the
method automatically when the first scene loads.

**Note** : Android only counts the first time you call `CallReportFullyDrawn`,
so there is no reason to call it multiple times.

[](android-thread-configuration.html)

Android thread configuration

[](android-game-state-hinting.html)

Game state hinting

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

