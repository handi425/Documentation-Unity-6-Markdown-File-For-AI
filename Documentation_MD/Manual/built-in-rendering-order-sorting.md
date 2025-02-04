[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-rendering-order-sorting.html)
  * [中文](/cn/current/Manual/built-in-rendering-order-sorting.html)
  * [日本語](/ja/current/Manual/built-in-rendering-order-sorting.html)
  * [한국어](/kr/current/Manual/built-in-rendering-order-sorting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-rendering-order-sorting.html)
  * [中文](/cn/current/Manual/built-in-rendering-order-sorting.html)
  * [日本語](/ja/current/Manual/built-in-rendering-order-sorting.html)
  * [한국어](/kr/current/Manual/built-in-rendering-order-sorting.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * [Rendering order in the Built-In Render Pipeline](built-in-rendering-order-landing.html)
  * Set how a camera sorts materials in the Built-In Render Pipeline

[](built-in-rendering-order-set-queue.html)

Set the render queue for a material in the Built-In Render Pipeline

[](GraphicsCommandBuffers-landing.html)

Custom rendering in the Built-In Render Pipeline

# Set how a camera sorts materials in the Built-In Render Pipeline

How you change the sorting behavior within a render queue depends on the index
of the render queue:

  * For queues with an index up to and including 2500 (Geometry + 500), you can change the opaque sort mode for a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) by using the
[Camera.opaqueSortMode](../ScriptReference/Camera-opaqueSortMode.html) API.

  * For queues with an index of 2501 or above, you can change the default transparent sort mode by using the [Rendering.GraphicsSettings-transparencySortMode](../ScriptReference/Rendering.GraphicsSettings-transparencySortMode.html) API. You can change the transparent sort mode for a Camera by using the [Camera.transparencySortMode](../ScriptReference/Camera-transparencySortMode.html) API.

[](built-in-rendering-order-set-queue.html)

Set the render queue for a material in the Built-In Render Pipeline

[](GraphicsCommandBuffers-landing.html)

Custom rendering in the Built-In Render Pipeline

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

