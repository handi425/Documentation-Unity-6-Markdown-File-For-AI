[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/fixed-updates.html)
  * [中文](/cn/current/Manual/fixed-updates.html)
  * [日本語](/ja/current/Manual/fixed-updates.html)
  * [한국어](/kr/current/Manual/fixed-updates.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/fixed-updates.html)
  * [中文](/cn/current/Manual/fixed-updates.html)
  * [日本語](/ja/current/Manual/fixed-updates.html)
  * [한국어](/kr/current/Manual/fixed-updates.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Managing time and frame rate](managing-time-and-frame-rate.html)
  * Fixed updates

[](time-per-frame-updates.html)

Per-frame updates

[](time-handling-variations.html)

Handling variation in time

## Fixed updates

Unlike the main [frame update](time-per-frame-updates.html), Unity’s physics
system updates at a fixed time interval, which is important for the accuracy
and consistency of physics simulations. The interval between fixed updates is
often referred to as the **fixed timestep** A customizable frame-rate-
independent interval that dictates when physics calculations and FixedUpdate()
events are performed. [More info](class-TimeManager.html)  
See in [Glossary](Glossary.html#FixedTimestep). You can read or change the
fixed timestep in two ways:

  * In code, by setting the value of the [`Time.fixedDeltaTime`](../ScriptReference/Time-fixedDeltaTime.html) property .
  * In the Unity Editor’s [Time](class-TimeManager.html) window, by modifying the **Fixed Timestep** value.

In both cases the fixed time step is specified in seconds. For example, a
value of 0.01 means each fixed time step is one hundredth of a second in
duration, so there are 100 fixed updates per second.

The fixed update loop simulates code running at fixed time intervals but in
practice the interval between fixed updates isn’t fixed. This is because a
fixed update always needs a frame to run in and the duration of a frame and
the length of the fixed time step are not in perfect sync. If a fixed time
step completes during the current frame, the associated fixed update can’t run
until the next frame. When frame rates are low, a single frame might span
several fixed time steps. In this case a backlog of fixed updates accumulates
during the current frame and Unity executes all of them in the next frame to
catch up.

**Note:** There is a maximum timestep period beyond which Unity will not
attempt to catch up with the simulation. For more information, refer to
[Handling variation in time](time-handling-variations.html).

Unity provides the
[`MonoBehaviour.FixedUpdate`](../ScriptReference/MonoBehaviour.FixedUpdate.html)
method as an entry point for you to execute your own code on each fixed
update. This is most commonly used for executing your own physics-related
code, such as [applying a force](../ScriptReference/Rigidbody.AddForce.html)
to a [Rigidbody](../ScriptReference/Rigidbody.html)A component that allows a
GameObject to be affected by simulated gravity and other forces. [More
info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody).

You can see more details of what occurs during the fixed update cycle in the
**Physics** section of the [execution order diagram](execution-order.html)
diagram.

## When frame rate is higher than the fixed update rate

If your application runs at a higher frame rate than the number of fixed time
steps per second then the average frame duration is less than the duration of
a single fixed time step. In this case, each frame has one fixed update or
none at all. For example, if the fixed time step value is 0.02, there are 50
fixed updates per second. If your application runs at 80 **frames per second**
The frequency at which consecutive frames are displayed in a running game.
[More info](RenderingStatistics.html)  
See in [Glossary](Glossary.html#framespersecond), a fixed update occurs every
two or three frames, as shown below.

![An example showing FixedUpdate running at 50 updates per second \(0.02s per
fixed update\) and the Player Loop running at approximately 80 frames per
second. Some frame updates \(marked in yellow\) have a corresponding
FixedUpdate \(marked in green\) if a new complete fixed timestep has elapsed
by the start of the frame.](../uploads/Main/TimingFixedUpdateFastFPS.png) An
example showing FixedUpdate running at 50 updates per second (0.02s per fixed
update) and the Player Loop running at approximately 80 frames per second.
Some frame updates (marked in yellow) have a corresponding FixedUpdate (marked
in green) if a new complete fixed timestep has elapsed by the start of the
frame.

This diagram shows the frame rate running faster than the fixed update
timestep rate. Time progresses to the right, each frame is numbered, and shows
its `Update` call at the start of the frame in orange. The fixed timestep here
is 0.02 seconds (50 times per second), and the game is running faster, at
about 80 frames per second. In this situation there are some frames with one
fixed update call, and some frames with none, depending on whether a full
fixed update timestep has completed by the time the frame starts. The fixed
time step periods are marked with letters A, B, C, D, E, and the frames in
which their corresponding fixed update calls occur are marked in green. The
fixed update call for timestep A occurs at the start of frame 4, the fixed
update call for timestep B occurs at the start of frame 7, and so on.

## When frame rate is lower than the fixed update rate

If your application runs at a lower frame rate than the fixed timestep value
then the average frame duration is longer than a single fixed timestep. This
means a backlog of fixed updates can accumulate during some frames and so each
frame has one or more fixed updates to allow the physics simulation to catch
up with the backlog. For example, if the fixed timestep value is 0.01, there
are 100 fixed updates per second. If your application runs at 40 frames per
second, Unity performs an average of two or three fixed updates per frame to
keep up. You might want a scenario like this when it’s more important to model
more accurate physics than to have a high frame rate.

![An example showing Update running at 25 FPS and FixedUpdate running at 100
updates per second. You can see there are four occurrences of a FixedUpdate
during one frame, marked in
yellow.](../uploads/Main/TimingFixedUpdateSlowFPS.png) An example showing
Update running at 25 FPS and FixedUpdate running at 100 updates per second.
You can see there are four occurrences of a FixedUpdate during one frame,
marked in yellow.

This diagram shows what happens when the fixed update cycle is running faster
than the frame rate. The fixed timestep here is 0.01 seconds (100 times per
second), and the game frame rate is running slower, at about 40 frames per
second. In this situation most frames have multiple fixed update calls before
each update call, the number depending on how many whole update timesteps have
elapsed since the previous frame. The fixed update time step periods are
marked with letters A, B, C, and so on, and frames in which their
corresponding fixed update calls occur are marked in green. The fixed update
call for timestep A and B occurs at the start of frame 2, the fixed update
call for frames C, D & E occur at the start of frame 3, and so on.

**Note:** A lower timestep value means more frequent physics updates and more
precise simulations, which leads to higher CPU load.

## Additional resources

  * [Managing variable frame rate](time-per-frame-updates.html)
  * [Handling variations in time](time-handling-variations.html)
  * [Time scale](time-scale.html)
  * [Capture frame rate](time-capture-frame-rate.html)

[](time-per-frame-updates.html)

Per-frame updates

[](time-handling-variations.html)

Handling variation in time

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

