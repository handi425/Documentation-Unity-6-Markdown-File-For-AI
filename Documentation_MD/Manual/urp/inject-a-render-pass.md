[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/inject-a-render-pass.html)
  * [中文](/cn/current/Manual/urp/inject-a-render-pass.html)
  * [日本語](/ja/current/Manual/urp/inject-a-render-pass.html)
  * [한국어](/kr/current/Manual/urp/inject-a-render-pass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/inject-a-render-pass.html)
  * [中文](/cn/current/Manual/urp/inject-a-render-pass.html)
  * [日本語](/ja/current/Manual/urp/inject-a-render-pass.html)
  * [한국어](/kr/current/Manual/urp/inject-a-render-pass.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../urp/customizing-urp.html)
  * Adding a Scriptable Render Pass to the frame rendering loop in URP

[](../urp/render-graph-viewer-reference.html)

Render Graph Viewer window reference for URP

[](../urp/renderer-features/scriptable-renderer-features/scriptable-renderer-
features-landing.html)

Injecting a render pass via a Scriptable Renderer Feature in URP

# Adding a Scriptable Render Pass to the frame rendering loop in URP

Add a custom render pass to the Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) frame rendering loop
by creating a Scriptable Renderer Feature, or using the
`RenderPipelineManager` API.

Page | Description  
---|---  
[Injecting a render pass via a Scriptable Renderer Feature](renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html) | Write a class that inherits `ScriptableRendererFeature`, and use it to creates an instance of the custom render pass you created, and insert the custom render pass into the rendering pipeline.  
[Inject a render pass via scripting](customize/inject-render-pass-via-script.html) | Use the `RenderPipelineManager` API to insert a custom render pass into the rendering pipeline.  
[Injection points reference](customize/custom-pass-injection-points.html) | URP contains multiple injection points that let you inject render passes at different points in the frame rendering loop.  
  
[](../urp/render-graph-viewer-reference.html)

Render Graph Viewer window reference for URP

[](../urp/renderer-features/scriptable-renderer-features/scriptable-renderer-
features-landing.html)

Injecting a render pass via a Scriptable Renderer Feature in URP

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

