[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/frame-debugger-window-event-hierarchy.html)
  * [中文](/cn/current/Manual/frame-debugger-window-event-hierarchy.html)
  * [日本語](/ja/current/Manual/frame-debugger-window-event-hierarchy.html)
  * [한국어](/kr/current/Manual/frame-debugger-window-event-hierarchy.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/frame-debugger-window-event-hierarchy.html)
  * [中文](/cn/current/Manual/frame-debugger-window-event-hierarchy.html)
  * [日本語](/ja/current/Manual/frame-debugger-window-event-hierarchy.html)
  * [한국어](/kr/current/Manual/frame-debugger-window-event-hierarchy.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * [Frame Debugger](FrameDebugger-landing.html)
  * Check or find a rendering event

[](FrameDebugger-debug.html)

Debug a frame

[](FrameDebugger-attach.html)

Attach the Frame Debugger to a built project

# Check or find a rendering event

The Event Hierarchy panel in the [Frame Debugger window](frame-debugger-
window.html) displays the sequence of rendering events that constitute the
frame. The panel organizes the events into a hierarchy so you can see where
each event originates from.

![The Event Hierarchy for the URP template scene.](../uploads/Main/frame-
debugger-event-hierarchy.png) The Event Hierarchy for the URP template scene.

To view information about an event, select the event in the Event Hierarchy.
When you select an event:

  * The Frame Debugger displays information about the event in the [event information](frame-debugger-window-event-information.html) panel.
  * Unity processes events up to and including the selected event and displays the result in the Game view.
  * If there is a single **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) associated with the event, you can
double click or CTRL + click the event to highlight the GameObject in the
[Hierarchy](Hierarchy.html). If the event represents a batch that contains
multiple GameObjects, Unity doesn’t highlight the GameObjects.

For more information, see [Frame Debugger](FrameDebugger.html).

## Hierarchy search bar

The search bar at the top of the Event Hierarchy can filter events by name.
Use it to quickly find specific events by name.

[](FrameDebugger-debug.html)

Debug a frame

[](FrameDebugger-attach.html)

Attach the Frame Debugger to a built project

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

