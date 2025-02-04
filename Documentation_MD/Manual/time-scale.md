[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/time-scale.html)
  * [中文](/cn/current/Manual/time-scale.html)
  * [日本語](/ja/current/Manual/time-scale.html)
  * [한국어](/kr/current/Manual/time-scale.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/time-scale.html)
  * [中文](/cn/current/Manual/time-scale.html)
  * [日本語](/ja/current/Manual/time-scale.html)
  * [한국어](/kr/current/Manual/time-scale.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Managing time and frame rate](managing-time-and-frame-rate.html)
  * In-game time and real time

[](time-handling-variations.html)

Handling variation in time

[](time-capture-frame-rate.html)

Capturing frame rate

# In-game time and real time

The [Time.timeScale](../ScriptReference/Time-timeScale.html) property defines
the rate at which time passes in your game world relative to real time. A
`Time.timeScale` value of 1.0 means your in-game time matches real time. A
value of 2.0 makes time pass twice as quickly in your game as in the real
world, which speeds up the action in your game. A value of 0.5 slows gameplay
down to half speed. A value of zero makes your in-game time stop completely.

`Time.timeScale` doesn’t actually slow execution but instead changes the time
step reported to the `Update` and `FixedUpdate` functions with
[Time.deltaTime](../ScriptReference/Time-deltaTime.html) and
[Time.fixedDeltaTime](../ScriptReference/Time-fixedDeltaTime.html).

Your `Update` function may be called just as often when you reduce the time
scale, but the value of `Time.deltaTime` each frame will be less. Other script
functions aren’t affected by the time scale, so you can for example display a
GUI with normal interaction when the game is paused.

For special time effects such as slow-motion, it’s sometimes useful to slow
the passage of game time so that animations and time-based calculations in
your code happen at a slower pace. Furthermore, you may sometimes want to
freeze game time completely, as when the game is paused.

The [Time](class-TimeManager.html) window has a property to let you set the
time scale globally but it’s usually more useful to set the value from a
script using the [Time-timeScale](../ScriptReference/Time-timeScale.html)
property:

    
    
    //C# script example
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        void Pause() {
            Time.timeScale = 0;
        }
        
        void Resume() {
            Time.timeScale = 1;
        }
    }
    

## Additional resources

  * [Per-frame updates](time-per-frame-updates.html)
  * [Capture frame rate](time-capture-frame-rate.html)

[](time-handling-variations.html)

Handling variation in time

[](time-capture-frame-rate.html)

Capturing frame rate

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

