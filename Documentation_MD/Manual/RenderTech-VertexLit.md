[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RenderTech-VertexLit.html)
  * [中文](/cn/current/Manual/RenderTech-VertexLit.html)
  * [日本語](/ja/current/Manual/RenderTech-VertexLit.html)
  * [한국어](/kr/current/Manual/RenderTech-VertexLit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RenderTech-VertexLit.html)
  * [中文](/cn/current/Manual/RenderTech-VertexLit.html)
  * [日本語](/ja/current/Manual/RenderTech-VertexLit.html)
  * [한국어](/kr/current/Manual/RenderTech-VertexLit.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * [Rendering paths in the Built-In Render Pipeline](built-in-rendering-paths.html)
  * Legacy Vertex Lit rendering path in the Built-In Render Pipeline

[](RenderTech-DeferredShading.html)

Deferred rendering path in the Built-In Render Pipeline

[](built-in-rendering-order-landing.html)

Rendering order in the Built-In Render Pipeline

# Legacy Vertex Lit rendering path in the Built-In Render Pipeline

This page describes details of the Vertex Lit [rendering
path](RenderingPaths.html)The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) in Unity’s Built-in **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline).

The Vertex Lit path generally renders each object in one pass, with lighting
from all lights calculated for each vertex.

It’s the fastest rendering path and has the widest hardware support.

Since all lighting is calculated at the vertex level, this rendering path does
not support most per-pixel effects: shadows, normal mapping, light cookies,
and highly detailed specular highlights are not supported.

[](RenderTech-DeferredShading.html)

Deferred rendering path in the Built-In Render Pipeline

[](built-in-rendering-order-landing.html)

Rendering order in the Built-In Render Pipeline

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

