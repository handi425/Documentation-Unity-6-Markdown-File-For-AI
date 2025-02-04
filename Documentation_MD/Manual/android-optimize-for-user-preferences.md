[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-optimize-for-user-preferences.html)
  * [中文](/cn/current/Manual/android-optimize-for-user-preferences.html)
  * [日本語](/ja/current/Manual/android-optimize-for-user-preferences.html)
  * [한국어](/kr/current/Manual/android-optimize-for-user-preferences.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-optimize-for-user-preferences.html)
  * [中文](/cn/current/Manual/android-optimize-for-user-preferences.html)
  * [日本語](/ja/current/Manual/android-optimize-for-user-preferences.html)
  * [한국어](/kr/current/Manual/android-optimize-for-user-preferences.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Optimization for Android](android-optimization.html)
  * Optimize for user preferences

[](android-game-state-hinting.html)

Game state hinting

[](android-large-screen-and-foldable-support.html)

Large screen and foldable device support

# Optimize for user preferences

Android’s [game
mode](https://developer.android.com/games/optimize/adpf/gamemode/about-API-
and-interventions) feature indicates how the user wants to optimize your
application. It enables users to say whether they want your application to run
normally, optimize for battery life, or optimize for best performance.

## Requirements and compatibility

Android’s game mode feature requires Android version 13.

## Use game mode in Unity

Unity provides the
[AndroidGame.GameMode](../ScriptReference/Android.AndroidGame.GameMode.html)
property that you can use to retrieve the current game mode for your
application.

Depending on the current game mode, you should adapt your Unity application to
accommodate the user’s preference. For example, if the game mode is [battery
saving](../ScriptReference/Android.AndroidGameMode.Battery.html), the user
expects your application to run for as long as possible. In this case, you
should reduce the resource intensity of effects and calculations to reduce the
impact your application has on the device’s battery life. This includes things
like:

  * Decrease the frame rate or resolution of the application.
  * Reduce the **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) bias to make Unity display lower detail
LODs closer to the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).

  * Reduce the cull distance of particular layers.
  * Reduce or possible batch network calls and/or sensor usage.

If the game mode is set to [maximize
performance](../ScriptReference/Android.AndroidGameMode.Performance.html), the
user expects your application to look and play as well as possible. In this
case, you can enable more effects and not be as wary of battery consumption.

**Tip** : If your application is resource intensive and you want to enhance
its overall performance, consider the [Adaptive Performance
package](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@latest/index.html).
It provides feedback about the thermal and power state of a mobile device and
enables you to react appropriately to prevent thermal throttling or excessive
battery consumption.

[](android-game-state-hinting.html)

Game state hinting

[](android-large-screen-and-foldable-support.html)

Large screen and foldable device support

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

