[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/FrameDebugger.html)
  * [中文](/cn/current/Manual/FrameDebugger.html)
  * [日本語](/ja/current/Manual/FrameDebugger.html)
  * [한국어](/kr/current/Manual/FrameDebugger.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/FrameDebugger.html)
  * [中文](/cn/current/Manual/FrameDebugger.html)
  * [日本語](/ja/current/Manual/FrameDebugger.html)
  * [한국어](/kr/current/Manual/FrameDebugger.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * [Frame Debugger](FrameDebugger-landing.html)
  * Introduction to the Frame Debugger

[](FrameDebugger-landing.html)

Frame Debugger

[](FrameDebugger-debug.html)

Debug a frame

# Introduction to the Frame Debugger

Debug frames to help identify rendering artefacts and other issues. Unity
includes a dedicated [Frame Debugger](frame-debugger-window.html) that can
pause the application on a particular frame and display the list of rendering
events that constitute the frame. The Frame Debugger can step through each
event and display the graphical state of the **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) at that point in the rendering process.
You can use this to find where graphical issues arise or to just see how Unity
constructs the scene from graphical elements.

## Render Pipeline compatibility

**Feature** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Frame Debugger** | Yes | Yes | Yes | Yes  
  
## 3rd-party frame debugging software

If you need information about a frame that Unity’s Frame Debugger doesn’t
provide, there are 3rd-party frame debugging programs that support Unity. The
Unity Editor supports native launching and frame capturing for
[RenderDoc](RenderDocIntegration.html). You can also build a standalone Player
and attach a supported frame debugger. For information about supported frame
debugging software, see [Profiling tools](performance-profiling-tools.html).

[](FrameDebugger-landing.html)

Frame Debugger

[](FrameDebugger-debug.html)

Debug a frame

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

