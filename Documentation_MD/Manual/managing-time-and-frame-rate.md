[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/managing-time-and-frame-rate.html)
  * [中文](/cn/current/Manual/managing-time-and-frame-rate.html)
  * [日本語](/ja/current/Manual/managing-time-and-frame-rate.html)
  * [한국어](/kr/current/Manual/managing-time-and-frame-rate.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/managing-time-and-frame-rate.html)
  * [中文](/cn/current/Manual/managing-time-and-frame-rate.html)
  * [日本語](/ja/current/Manual/managing-time-and-frame-rate.html)
  * [한국어](/kr/current/Manual/managing-time-and-frame-rate.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * Managing time and frame rate

[](object-oriented-development.html)

Object-oriented development

[](time-per-frame-updates.html)

Per-frame updates

# Managing time and frame rate

It’s important to understand how Unity handles time to ensure your gameplay
remains stable. Updates occur at regular time intervals to capture changes to
character positions, health status, scores, and so on. If your code makes
changes in the wrong update loop or doesn’t allow for variations in time,
effects like movement might be too fast, too slow, or jumpy instead of smooth.

The `Time` class contains properties through which you can get and in some
cases set various time-related measurements and settings. Refer to
[Time](../ScriptReference/Time.html) in the Scripting API reference for a
complete list of the properties and their meanings.

**Topic** | **Description**  
---|---  
[Per-frame updates](time-per-frame-updates.html) | Updates which happen once per frame and whose frequency therefore depends on frame rate.  
[Fixed updates](fixed-updates.html) | Updates which happen at a configurable fixed time interval.  
[In-game time and real time](time-scale.html) | The configurable relationship between in-game time and real time and the potential effects.  
[Handling variation in time](time-handling-variations.html) | Techniques Unity uses to compensate for variations in time and frame rate and to limit the effects of one-time delays.  
[Capture frame rate](time-capture-frame-rate.html) | Compensating for frame rate when recording video of gameplay.  
  
## Additional resources

  * [Time API reference](../ScriptReference/Time.html)
  * [Time settings in the Editor](class-TimeManager.html)

[](object-oriented-development.html)

Object-oriented development

[](time-per-frame-updates.html)

Per-frame updates

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

