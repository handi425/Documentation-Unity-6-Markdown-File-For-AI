[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [中文](/cn/current/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [中文](/cn/current/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [日本語](/ja/current/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [한국어](/kr/current/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * Custom render pass workflow in URP

[](../../urp/renderer-features/renderer-feature-render-objects.html)

Render Objects Renderer Feature reference for URP

[](../../urp/customize/blit-overview.html)

Blit in URP

# Custom render pass workflow in URP

A custom render pass is a way to change how the Universal **Render Pipeline**
A series of operations that take the contents of a Scene, and displays them on
a screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP) renders a
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) or the objects within a scene. A
custom render pass contains your own rendering code, which you insert into the
rendering pipeline at an injection point.

To add a custom render pass, complete the following tasks:

  * Create the code for a custom render pass using the Scriptable Render Pass API.
  * Add the custom render pass to URP’s frame rendering loop by creating a Scriptable Renderer Feature, or using the `RenderPipelineManager` API.

##  Create the code for a custom render pass

To create the code for a custom render pass, write a class that inherits
`ScriptableRenderPass`. In the class, use the [render graph API](../render-
graph-introduction.html) to tell Unity what textures and render targets to
use, and what operations to do on them.

Refer to [Scriptable Render Passes](intro-to-scriptable-render-passes.html)
for more information.

##  Create a Scriptable Renderer Feature

To add your custom render pass to URP’s frame rendering loop, write a class
that inherits `ScriptableRendererFeature`.

The Scriptable Renderer Feature does the following:

  1. Creates an instance of the custom render pass you created.
  2. Inserts the custom render pass into the rendering pipeline.

Refer to [Inject a pass using a Scriptable Renderer Feature](scriptable-
renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html) for
more information.

##  Use the RenderPipelineManager API

To add your custom render pass to URP’s frame rendering loop, you can also
subscribe a method to one of the events in the
[RenderPipelineManager](https://docs.unity3d.com/ScriptReference/Rendering.RenderPipelineManager.html)
class.

Refer to [Inject a render pass via scripting](../customize/inject-render-pass-
via-script.html) for more information.

## Additional resources

  * [Render graph system](../render-graph-introduction.html)
  * [Example of a complete Scriptable Renderer Feature](../renderer-features/create-custom-renderer-feature.html)

[](../../urp/renderer-features/renderer-feature-render-objects.html)

Render Objects Renderer Feature reference for URP

[](../../urp/customize/blit-overview.html)

Blit in URP

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

