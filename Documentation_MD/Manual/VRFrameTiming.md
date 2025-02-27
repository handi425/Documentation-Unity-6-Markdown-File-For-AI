[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VRFrameTiming.html)
  * [中文](/cn/current/Manual/VRFrameTiming.html)
  * [日本語](/ja/current/Manual/VRFrameTiming.html)
  * [한국어](/kr/current/Manual/VRFrameTiming.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VRFrameTiming.html)
  * [中文](/cn/current/Manual/VRFrameTiming.html)
  * [日本語](/ja/current/Manual/VRFrameTiming.html)
  * [한국어](/kr/current/Manual/VRFrameTiming.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR graphics](xr-graphics.html)
  * VR frame timing 

[](xr-foveated-rendering.html)

Foveated rendering

[](xr-audio.html)

XR audio

# VR frame timing

Frame timing in **VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) mode works exactly like it does in VSync-
enabled non-VR mode (see documentation on the [Execution order of event
functions](execution-order.html)). The only difference is that Unity does not
depend on the underlying 3D SDK’s **VSync** Vertical synchronization (VSync)
is a display setting that caps a game’s frame rate to match the refresh rate
of a monitor, to prevent image tearing.  
See in [Glossary](Glossary.html#VSync), but instead whichever VR SDK it
currently renders with. There is no benefit to rendering faster than the
display can refresh. Instead, Unity focuses on utilizing the time most
efficiently.

In multithreaded rendering, Unity synchronizes the simulation thread and the
rendering thread on the CPU. This reduces latency. The simulation thread
primarily executes the **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts), sounds, AI, and other tasks needed
for the simulation to run. The render thread focuses on submitting draw calls
to the graphics driver, which in turn validates them and sends them to the
GPU. To achieve the greatest parallelism between threads, Unity executes
graphics commands as they come in, and simulates the next frame at the same
time.

Unity waits for the GPU to completely render and display the last frame, then
submits rendering commands for the next frame.

## Lowest possible latency

Before Unity can submit the first rendering command that depends on the view
transformation matrix, it must first get the view matrix from the VR SDK. To
keep latency as low as possible, the VR SDK predicts the head transform twice
per frame:

  * One prediction to render the current frame. This prediction corresponds with where your head actually is, in real space, when the frame arrives on the screen.

  * One prediction to simulate the following frame.

Unity applies the rendering prediction for the current frame to **cameras** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), controllers, and anything that needs
information for **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) rendering. Unity uses the simulation
prediction for the following frame if it is unable to render the following
frame.

For more information on how the hardware handles rendering, see the
manufacturer documentation for your head-mounted display.

## What happens when Unity drops a frame?

If Unity doesn’t submit the fully rendered frame in time for it to be ready
for the next display refresh, a few things might happen, depending on which VR
SDK is active. The VR SDK might:

  * Display the previously submitted frame. This looks like judder, and greatly reduces the quality of the experience.

  * Rotationally reproject the previously submitted frame based on the current head pose. This is a crude approximation that works well as a fallback for static content, but any content with animation or positional movement does not look correct. 

  * Apply some form of positional reprojection. This might be temporal to fill in missing details.

For more information on reprojection (sometimes called time warping), see the
XinReality wiki entry on [Timewarp](https://xinreality.com/wiki/Timewarp).

This all happens automatically. At this point, it’s usually too late for Unity
to successfully finish the next frame that it should already be rendering.
Instead, the VR SDK takes the last frame it received and reprojects it to the
latest predicted pose, and Unity waits until the next opportunity to render a
full frame to get back on track. If your app continually drops frames, Unity
only renders every other frame.

For more information on how the hardware handles rendering, see the
manufacturer documentation for your head-mounted display.

## GPU-bound vs. CPU-bound in VR

Each display has a specific refresh rate that Unity is bound to. You can get
this at run time with [VRDevice.refreshRate](../ScriptReference/XR.XRDevice-
refreshRate.html). A value of 1 divided by the `refreshRate` gives you the
time allocated to a single frame.

For example, this might be 11.1 milliseconds in the case of a refresh rate of
90 hz.

  * If your app is GPU-bound, the Unity **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) displays `XR.WaitForGPU` in excess
of one frame’s time in milliseconds.

  * If your app is CPU-bound, a frame takes longer than the designated frame time, but the Unity Profiler displays `XR.WaitForGPU` shorter than the one frame.

[](xr-foveated-rendering.html)

Foveated rendering

[](xr-audio.html)

XR audio

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

