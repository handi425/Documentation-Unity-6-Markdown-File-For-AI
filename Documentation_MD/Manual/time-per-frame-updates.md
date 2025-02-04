[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/time-per-frame-updates.html)
  * [中文](/cn/current/Manual/time-per-frame-updates.html)
  * [日本語](/ja/current/Manual/time-per-frame-updates.html)
  * [한국어](/kr/current/Manual/time-per-frame-updates.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/time-per-frame-updates.html)
  * [中文](/cn/current/Manual/time-per-frame-updates.html)
  * [日本語](/ja/current/Manual/time-per-frame-updates.html)
  * [한국어](/kr/current/Manual/time-per-frame-updates.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Managing time and frame rate](managing-time-and-frame-rate.html)
  * Per-frame updates

[](managing-time-and-frame-rate.html)

Managing time and frame rate

[](fixed-updates.html)

Fixed updates

# Per-frame updates

Unity performs some updates once per frame. Your MonoBehaviour **scripts** A
piece of code that allows you to create your own Components, trigger game
events, modify Component properties over time and respond to user input in any
way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) can hook into this update loop
through the
[`MonoBehaviour.Update`](../ScriptReference/MonoBehaviour.Update.html) method.
For example, in your game character’s `Update` method, you might read the user
input from a joypad, and move the character forward a certain amount. It’s
important to remember when handling time-based actions like this that the
game’s frame rate can vary and so the length of time between `Update` calls
also varies.

The variable frame rate of a game is often expressed in **frames per second**
The frequency at which consecutive frames are displayed in a running game.
[More info](RenderingStatistics.html)  
See in [Glossary](Glossary.html#framespersecond), or **FPS** See first person
shooter, frames per second.  
See in [Glossary](Glossary.html#FPS). Frame rate varies according to factors
like the capabilities of the host device and the complexity of the graphics
and computation required to draw each frame. For example, your game may run at
a slower frame rate when there are 100 active, on-screen characters than when
there is only one.

Unless otherwise constrained by your [quality settings](class-
QualitySettings.html) or by the [Adaptive Performance
package](com.unity.adaptiveperformance.html), Unity tries to run your game at
the fastest frame rate possible. You can see more details of what occurs each
frame in the **Game Logic** section of the [execution order
diagram](execution-order.html).

Consider the task of moving an object forward gradually, one frame at a time.
It might seem at first that you could just translate the object by a fixed
distance each frame:

    
    
    //C# script example
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        public float distancePerFrame;
        
        void Update() {
            transform.Translate(0, 0, distancePerFrame); // this is incorrect
        }
    }
    

However with this code, as the frame rate varies, the object’s apparent speed
also varies. If the game is running at 100 FPS, the object moves
`distancePerFrame` 100 times per second. But if the frame rate slows to 60 FPS
(due to CPU load, for example) then it only steps forward 60 times per second
and therefore covers a shorter distance over the same amount of time.

In most cases this is undesirable, particularly with games and animation. It’s
much more common to want your in-game objects to move at steady and
predictable speeds regardless of the frame rate. The solution is to scale the
amount of movement each frame by the amount of time elapsed each frame, which
you can read from the [Time.deltaTime](../ScriptReference/Time-deltaTime.html)
property:

    
    
    //C# script example
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        public float distancePerSecond;
        
        void Update() {
            transform.Translate(0, 0, distancePerSecond * Time.deltaTime);
        }
    }
    

Note that the movement is now given as `distancePerSecond` rather than
`distancePerFrame`. As the frame rate varies, the size of the movement step
will vary accordingly and so the object’s speed will be constant.

Depending on your target platform, use either
[Application.targetFrameRate](../ScriptReference/Application-
targetFrameRate.html) or
[QualitySettings.vSyncCount](../ScriptReference/QualitySettings-
vSyncCount.html) to set the frame rate of your application. For more
information, see the [Application.targetFrameRate API
documentation](../ScriptReference/Application-targetFrameRate.html).

## Additional resources

  * [Fixed updates](fixed-updates.html)
  * [Handling variations in time](time-handling-variations.html)
  * [In-game versus real time](time-scale.html)
  * [Capture frame rate](time-capture-frame-rate.html)

[](managing-time-and-frame-rate.html)

Managing time and frame rate

[](fixed-updates.html)

Fixed updates

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

