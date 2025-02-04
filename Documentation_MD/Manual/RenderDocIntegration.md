[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RenderDocIntegration.html)
  * [中文](/cn/current/Manual/RenderDocIntegration.html)
  * [日本語](/ja/current/Manual/RenderDocIntegration.html)
  * [한국어](/kr/current/Manual/RenderDocIntegration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RenderDocIntegration.html)
  * [中文](/cn/current/Manual/RenderDocIntegration.html)
  * [日本語](/ja/current/Manual/RenderDocIntegration.html)
  * [한국어](/kr/current/Manual/RenderDocIntegration.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * RenderDoc Integration

[](VisualStudioIntegration.html)

Visual Studio C# integration

[](EditorAnalytics.html)

Editor analytics

# RenderDoc Integration

The Editor supports integrated launching and capture of the
[RenderDoc](https://github.com/baldurk/renderdoc) graphics debugger, for
detailed frame introspection and debugging.

The integration is only supported for RenderDoc versions 0.26 or later, so if
an earlier version is currently installed it is required that you update to at
least version 0.26.

**Note:** While the integration is only available in the Editor, it is quite
possible to use RenderDoc as normal with no extra setup in standalone player
builds.

**Note:** Frames can only be captured if Unity is running on a platform and
API that RenderDoc supports. If another API is in use, the RenderDoc
integration will be temporarily disabled until a supported API is enabled.
Refer to the [RenderDoc
documentation](https://renderdoc.org/docs/getting_started/features.html#) for
more information on supported platforms and APIs.

## Loading RenderDoc

If a RenderDoc installation is detected, then at any time after loading the
Editor you can right click on the tab for the [Game View](GameView.html) or
[Scene View](UsingTheSceneView.html)An interactive view into the world you are
creating. You use the Scene View to select and position scenery, characters,
cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) and click the ‘Load RenderDoc’
option. This will reload the graphics device so you must save any changes, but
afterwards RenderDoc will be ready to capture without having to restart the
editor or build a standalone player.

**Note:** You can also launch the Editor via RenderDoc as normal, or pass the
-load-renderdoc command line option to load RenderDoc from startup.

## Capturing a frame with RenderDoc

When a compatible version of RenderDoc is detected as loaded into the Editor,
a new button will appear on the right side of the **toolbar** A row of buttons
and basic controls at the top of the Unity Editor that allows you to interact
with the Editor in various ways (e.g. scaling, translation). [More
info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) on the Game and **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) Views.

![Capturing a frame with
RenderDoc](../uploads/Main/RenderDocCaptureButton.png) Capturing a frame with
RenderDoc

Pressing this button will trigger a capture of the next frame of rendering for
the view. If the RenderDoc tool **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) has not been opened, a new instance will
be launched to show the capture, and if it is already running the newest
capture will automatically appear there. From there you can open the capture
and debug using the tool.

![List of frame captures in
RenderDoc](../uploads/Main/RenderDocCaptureList.jpg) List of frame captures in
RenderDoc

## Including shader debug information

By default to optimise the size of DirectX11 shaders, debugging information is
stripped out. This means that constants and resources will have no names, and
the **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) source will not be available. To
include this debugging information in your shader, include **#pragma
enable_d3d11_debug_symbols** in your shader’s CGPROGRAM block.

## Alternative graphics debugging techniques

If you build a standalone player using D3D11, you can capture a frame and
debug using the [Visual Studio graphics debugger](SL-
DebuggingD3D11ShadersWithVS.html).

[](VisualStudioIntegration.html)

Visual Studio C# integration

[](EditorAnalytics.html)

Editor analytics

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

