[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/render-graph-frame-data.html)
  * [中文](/cn/current/Manual/urp/render-graph-frame-data.html)
  * [日本語](/ja/current/Manual/urp/render-graph-frame-data.html)
  * [한국어](/kr/current/Manual/urp/render-graph-frame-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/render-graph-frame-data.html)
  * [中文](/cn/current/Manual/urp/render-graph-frame-data.html)
  * [日本語](/ja/current/Manual/urp/render-graph-frame-data.html)
  * [한국어](/kr/current/Manual/urp/render-graph-frame-data.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * [Render graph system in URP](../urp/render-graph.html)
  * Frame data in the render graph system in URP

[](../urp/render-graph-pass-textures-between-passes.html)

Transfer a texture between render passes in URP

[](../urp/accessing-frame-data.html)

Get data from the current frame in URP

# Frame data in the render graph system in URP

Fetch the textures that the Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) creates for the
current frame or previous frames, for example a color texture or a depth
texture.

**Page** | **Description**  
---|---  
[Get data from the current frame](accessing-frame-data.html) | Fetch the textures URP creates for the current frame.  
[Get data from previous frames](render-graph-get-previous-frames.html) | To fetch the previous frames the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) rendered, use the
`UniversalCameraData.historyManager` API.  
[Add textures to the camera history](render-graph-add-textures-to-camera-history.html) | To add your own texture to the camera history, create a camera history type to store the texture between frames.  
[Get the current framebuffer from GPU memory](render-graph-framebuffer-fetch.html) | To speed up rendering, use the `SetInputAttachment` API to read the frame that Unity has rendered so far.  
[Frame data textures reference](render-graph-frame-data-reference.html) | Explore the textures you can fetch from the current frame or previous frames.  
  
[](../urp/render-graph-pass-textures-between-passes.html)

Transfer a texture between render passes in URP

[](../urp/accessing-frame-data.html)

Get data from the current frame in URP

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

