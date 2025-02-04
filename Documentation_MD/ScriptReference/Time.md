[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# Time

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Provides an interface to get time information from Unity.

For more information, see the following pages in the User Manual:

  * [Time and Framerate Management](../Manual/managing-time-and-frame-rate.html)
  * [Order of execution for event functions](../Manual/execution-order.html).

### Static Properties

[captureDeltaTime](Time-captureDeltaTime.html)| Slows your application’s
playback time to allow Unity to save screenshots in between frames.  
---|---  
[captureDeltaTimeRational](Time-captureDeltaTimeRational.html)| Slows your
application’s playback time to allow Unity to save screenshots in between
frames.  
[captureFramerate](Time-captureFramerate.html)| The reciprocal of
Time.captureDeltaTime.  
[deltaTime](Time-deltaTime.html)| The interval in seconds from the last frame
to the current one (Read Only).  
[fixedDeltaTime](Time-fixedDeltaTime.html)| The interval in seconds of in-game
time at which physics and other fixed frame rate updates (like MonoBehaviour's
FixedUpdate) are performed.  
[fixedTime](Time-fixedTime.html)| The time at which the current FixedUpdate
started in seconds since the start of the game (Read Only).  
[fixedTimeAsDouble](Time-fixedTimeAsDouble.html)| The double precision time
since the last FixedUpdate started (Read Only). This is the time in seconds
since the start of the game.  
[fixedUnscaledDeltaTime](Time-fixedUnscaledDeltaTime.html)| The interval in
seconds of timeScale-independent ("real") time at which physics and other
fixed frame rate updates (like MonoBehaviour's FixedUpdate) are
performed.(Read Only).  
[fixedUnscaledTime](Time-fixedUnscaledTime.html)| The timeScale-independent
time at the beginning of the last MonoBehaviour.FixedUpdate phase (Read Only).
This is the time in seconds since the start of the game.  
[fixedUnscaledTimeAsDouble](Time-fixedUnscaledTimeAsDouble.html)| The double
precision timeScale-independent time at the beginning of the last FixedUpdate
(Read Only). This is the time in seconds since the start of the game.  
[frameCount](Time-frameCount.html)| The total number of frames since the start
of the game (Read Only).  
[inFixedTimeStep](Time-inFixedTimeStep.html)| Returns true if called inside a
fixed time step callback (like MonoBehaviour's FixedUpdate), otherwise returns
false (Read Only).  
[maximumDeltaTime](Time-maximumDeltaTime.html)| The maximum value of
Time.deltaTime in any given frame. This is a time in seconds that limits the
increase of Time.time between two frames.  
[maximumParticleDeltaTime](Time-maximumParticleDeltaTime.html)| The maximum
time a frame can spend on particle updates. If the frame takes longer than
this, then updates are split into multiple smaller updates.  
[realtimeSinceStartup](Time-realtimeSinceStartup.html)| The real time in
seconds since the game started (Read Only).  
[realtimeSinceStartupAsDouble](Time-realtimeSinceStartupAsDouble.html)| The
real time in seconds since the game started (Read Only). Double precision
version of realtimeSinceStartup.  
[smoothDeltaTime](Time-smoothDeltaTime.html)| A smoothed out Time.deltaTime
(Read Only).  
[time](Time-time.html)| The time at the beginning of the current frame in
seconds since the start of the application (Read Only).  
[timeAsDouble](Time-timeAsDouble.html)| The double precision time at the
beginning of this frame (Read Only). This is the time in seconds since the
start of the game.  
[timeAsRational](Time-timeAsRational.html)| The time this frame has started
(Read Only). This is the time in seconds since the start of the game
represented as a RationalTime.  
[timeScale](Time-timeScale.html)| The scale at which time passes.  
[timeSinceLevelLoad](Time-timeSinceLevelLoad.html)| The time in seconds since
the last non-additive scene finished loading (Read Only).  
[timeSinceLevelLoadAsDouble](Time-timeSinceLevelLoadAsDouble.html)| The double
precision time in seconds since the last non-additive scene finished loading
(Read Only).  
[unscaledDeltaTime](Time-unscaledDeltaTime.html)| The timeScale-independent
interval in seconds from the last frame to the current one (Read Only).  
[unscaledTime](Time-unscaledTime.html)| The timeScale-independent time for
this frame (Read Only). This is the time in seconds since the start of the
game.  
[unscaledTimeAsDouble](Time-unscaledTimeAsDouble.html)| The double precision
timeScale-independent time for this frame (Read Only). This is the time in
seconds since the start of the game.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

