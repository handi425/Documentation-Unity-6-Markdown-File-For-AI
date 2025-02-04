[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/customizing-urp.html)
  * [中文](/cn/current/Manual/urp/customizing-urp.html)
  * [日本語](/ja/current/Manual/urp/customizing-urp.html)
  * [한국어](/kr/current/Manual/urp/customizing-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/customizing-urp.html)
  * [中文](/cn/current/Manual/urp/customizing-urp.html)
  * [日本語](/ja/current/Manual/urp/customizing-urp.html)
  * [한국어](/kr/current/Manual/urp/customizing-urp.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * Custom rendering and post-processing in URP

[](../urp/anti-aliasing.html)

Add anti-aliasing in the Universal Render Pipeline

[](../urp/renderer-features/intro-to-scriptable-render-passes.html)

Introduction to Scriptable Render Passes in URP

# Custom rendering and post-processing in URP

Customize and extend the rendering process in the Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP). Create a custom
render pass in a C# script and inject it into the URP frame rendering loop.

Page | Description  
---|---  
[Introduction to Scriptable Render Passes](renderer-features/intro-to-scriptable-render-passes.html) | Learn about using Scriptable Render Passes to alter how Unity renders a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) or the objects within a scene.  
[Adding pre-built effects with Renderer Features in URP](urp-renderer-feature-landing.html) | Resources for adding pre-built render passes to URP, and configuring their behaviour.  
[Custom render pass workflow in URP](renderer-features/custom-rendering-pass-workflow-in-urp.html) | Add and inject a custom render pass.  
[Blit](customize/blit-overview.html)A shorthand term for “bit block transfer”.
A blit operation is the process of transferring blocks of data from one place
in memory to another.  
See in [Glossary](../Glossary.html#blit) | Understand the different ways to perform a blit operation in URP and best practices to follow when writing custom render passes.  
[Render graph system](render-graph.html) | Resources and approaches for using the `RenderGraph` APIs to create a Scriptable Render Pass.  
[Adding a Scriptable Render Pass to the frame rendering loop](inject-a-render-pass.html) | Resources and techniques for injecting a custom render pass via a Scriptable Renderer Feature, or the `RenderPipelineManager` API.  
[Compatibility Mode](compatibility-mode.html) | Write a Scriptable Render Pass if you enable **Compatibility Mode (Render Graph Disabled)** in URP graphics settings. Unity no longer develops or improves this **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath).  
  
## Additional resources

  * [Rendering](rendering-in-universalrp.html)
  * [Render pipeline concepts](urp-concepts.html)
  * [Pre-built effects (Renderer Features)](urp-renderer-feature.html)
  * [How to create a custom post-processing effect](post-processing/post-processing-custom-effect-low-code.html)
  * [Execute rendering commands in a custom render pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/srp-using-scriptable-render-context.html)

[](../urp/anti-aliasing.html)

Add anti-aliasing in the Universal Render Pipeline

[](../urp/renderer-features/intro-to-scriptable-render-passes.html)

Introduction to Scriptable Render Passes in URP

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

