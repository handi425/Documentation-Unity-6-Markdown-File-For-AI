[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/FrameDebugger-debug.html)
  * [中文](/cn/current/Manual/FrameDebugger-debug.html)
  * [日本語](/ja/current/Manual/FrameDebugger-debug.html)
  * [한국어](/kr/current/Manual/FrameDebugger-debug.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/FrameDebugger-debug.html)
  * [中文](/cn/current/Manual/FrameDebugger-debug.html)
  * [日本語](/ja/current/Manual/FrameDebugger-debug.html)
  * [한국어](/kr/current/Manual/FrameDebugger-debug.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * [Frame Debugger](FrameDebugger-landing.html)
  * Debug a frame

[](FrameDebugger.html)

Introduction to the Frame Debugger

[](frame-debugger-window-event-hierarchy.html)

Check or find a rendering event

# Debug a frame

To debug a frame using the Frame Debugger:

  1. Open the Frame Debugger (menu: **Window** > **Analysis** > **Frame Debugger**).
  2. Use the target selector to select the process to attach the Frame Debugger to. If you want to debug a frame in the Unity Editor, set this to **Editor**. If you want to debug a frame in a built application, see [Attach the Frame Debugger to a built project](FrameDebugger-attach.html).
  3. Click **Enable**. When you do this, the Frame Debugger captures a frame. It populates the Event Hierarchy with the draw calls and other events that constitute the frame and renders the frame in the Game view.   
**Note** : If your application is running, the Frame Debugger pauses it.

  4. Select an event from the Event Hierarchy to view the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as it appears up to and including that
event. This also displays information about the event in the Event Information
Panel. You can use the previous event and next event button, the arrow keys,
or the event scrubber to move through the frame linearly. If you don’t know
which event Unity renders the geometry you want to debug in, these navigation
tools are useful to move through the events linearly until you find it.

When a draw call event corresponds to the geometry of a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), Unity highlights that GameObject
in the [Hierarchy](Hierarchy.html).

If an event renders into a [RenderTexture](class-RenderTexture.html), Unity
displays the contents of that RenderTexture in the Game view and Frame
Debugger window. This is useful for inspecting how various off-screen render
targets build up. For example:

![Viewing events that accumulate to produce the diffuse G-buffer during
deferred rendering.](../uploads/Main/frame-debugger-event-accumulation.gif)
Viewing events that accumulate to produce the diffuse G-buffer during deferred
rendering.

[](FrameDebugger.html)

Introduction to the Frame Debugger

[](frame-debugger-window-event-hierarchy.html)

Check or find a rendering event

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

