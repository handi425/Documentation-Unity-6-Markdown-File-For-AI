[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/video-clock.html)
  * [中文](/cn/current/Manual/video-clock.html)
  * [日本語](/ja/current/Manual/video-clock.html)
  * [한국어](/kr/current/Manual/video-clock.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/video-clock.html)
  * [中文](/cn/current/Manual/video-clock.html)
  * [日本語](/ja/current/Manual/video-clock.html)
  * [한국어](/kr/current/Manual/video-clock.html)

  * [Video and cutscenes](Video.html)
  * [Video Player](VideoPlayer.html)
  * Clock management with the Video Player component

[](VideoPlayer-MigratingFromMovieTexture.html)

Migrating from MovieTexture to VideoPlayer

[](VideoPanoramic.html)

Panoramic video

# Clock management with the Video Player component

This section describes the different time update modes available for the Video
Player component and how it interacts with them.

You can use the Video Player component to control how to time video playback
relative to other interactive behaviors. For example, you can synchronize
video playback with animation or with audio. You can do this through the
following time update modes:

  * Audio Digital Signal Processing (DSP) clock
  * Game time
  * Unscaled game time

The Video Player follows Unity’s capture frame rate
[(`Time.captureFramerate`)](../ScriptReference/Time-captureFramerate.html) and
capture delta time [(`Time.captureDeltaTime`)](../ScriptReference/Time-
captureDeltaTime.html).

When you specify a capture frame rate, a Video Player’s playback becomes
synchronous, which means the Video Player displays all frames at the expected
time stamp even if it has to delay the overall game execution. Another
advantage of the capture frame rate is that, it also blocks preparation and
seek operations, which leads to consistent and accurate results. However, this
might slow down game execution especially when the video must remain
synchronized with the rest of the **scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). For example, Unity Recorder uses this
special behavior of time to produce smooth recordings.

The capture frame rate only affects game time. If a Video Player uses unscaled
game time or audio DSP clock while capture frame rate is in use, the Video
Player ignores the capture frame rate and uses asynchronous playback. That
means, the Video Player skips or repeats frames if needed, and preparation or
seek tasks are asynchronous to prevent blocking of playback. However, this
only happens if you select game time as the time update mode for Video Player.

**Note:** On the Web platform, Unity’s Video Player doesn’t support
synchronous playback with `captureFramerate`. By default, it uses the normal
asynchronous playback that’s described with the Game time update mode.

## Audio DSP clock

The audio DSP clock comes from the Audio module. You can access it through
[`AudioSettings.dspTime`](../ScriptReference/AudioSettings-dspTime.html).

## Game time

Game time is set in the Time module. You can access it using C# through
[`Time.time`](../ScriptReference/Time-time.html). When you use game time, also
known as scaled game time, Unity follows the Time Scale value set in the Time
window. You can also modify the Time Scale value using C# through
[`Time.timeScale`](../ScriptReference/Time-timeScale.html). However, if the
capture frame rate or capture delta time have non-zero values, game time
changes according to the rules that govern the **time manager** A Unity
Settings Manager that lets you set a number of properties that control timing
within your game. [More info](class-TimeManager.html)  
See in [Glossary](Glossary.html#TimeManager)’s capture frame rate feature.

Note: Capture delta time is the same as 1 divided by the capture frame rate.
It’s another view of the same information.

## Unscaled game time

When you use Unscaled game time, the Video Player ignores the Time Scale
value. Unscaled game time comes from the Time module. You can access it using
C# through [`Time.unscaledTime`](../ScriptReference/Time-unscaledTime.html).

## Additional resources

  * [Important classes - Time](managing-time-and-frame-rate.html)
  * [TimeManager class description](class-TimeManager.html)
  * [Time scripting API](../ScriptReference/Time.html)

[](VideoPlayer-MigratingFromMovieTexture.html)

Migrating from MovieTexture to VideoPlayer

[](VideoPanoramic.html)

Panoramic video

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

