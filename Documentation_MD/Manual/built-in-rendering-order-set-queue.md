[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-rendering-order-set-queue.html)
  * [中文](/cn/current/Manual/built-in-rendering-order-set-queue.html)
  * [日本語](/ja/current/Manual/built-in-rendering-order-set-queue.html)
  * [한국어](/kr/current/Manual/built-in-rendering-order-set-queue.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-rendering-order-set-queue.html)
  * [中文](/cn/current/Manual/built-in-rendering-order-set-queue.html)
  * [日本語](/ja/current/Manual/built-in-rendering-order-set-queue.html)
  * [한국어](/kr/current/Manual/built-in-rendering-order-set-queue.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * [Rendering order in the Built-In Render Pipeline](built-in-rendering-order-landing.html)
  * Set the render queue for a material in the Built-In Render Pipeline

[](built-in-rendering-order.html)

Render queues and sorting behaviours in the Built-in Render Pipeline

[](built-in-rendering-order-sorting.html)

Set how a camera sorts materials in the Built-In Render Pipeline

# Set the render queue for a material in the Built-In Render Pipeline

By default, Unity places objects in the render queue specified in their Unity
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). You define this value using the
`[Queue]` [SubShader tag](SL-SubShaderTags.html).

You can override this value on a per-material basis.

In the Unity Editor, you can do this in the [material Inspector](class-
Material.html) by setting the **Render Queue** property. In a C# script, you
can do this by setting the value of
[Material.renderQueue](../ScriptReference/Material-renderQueue.html) using the
[Rendering.RenderQueue](../ScriptReference/Rendering.RenderQueue.html) enum.

[](built-in-rendering-order.html)

Render queues and sorting behaviours in the Built-in Render Pipeline

[](built-in-rendering-order-sorting.html)

Set how a camera sorts materials in the Built-In Render Pipeline

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

