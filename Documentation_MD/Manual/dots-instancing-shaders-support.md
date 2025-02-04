[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dots-instancing-shaders-support.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-support.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-support.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-support.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dots-instancing-shaders-support.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-support.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-support.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-support.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
  * Support DOTS Instancing in a a custom shader in URP

[](dots-instancing-shaders.html)

DOTS Instancing shaders in URP

[](dots-instancing-shaders-declare.html)

Declare DOTS Instancing properties in a custom shader in URP

# Support DOTS Instancing in a a custom shader in URP

To support DOTS Instancing, a **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) needs to do the following:

  * Use shader model 4.5 or newer. Specify `#pragma target 4.5` or higher.
  * Support the `DOTS_INSTANCING_ON` keyword. Declare this with `#pragma multi_compile _ DOTS_INSTANCING_ON`.
  * Declare at least one block of DOTS Instanced properties each of which has least one property. For more information, see [Declaring DOTS Instanced properties](dots-instancing-shaders-unity-dots-instanced-prop.html).

**Note** : Shader Graphs and shaders that Unity provides in URP and HDRP
support DOTS Instancing.

[](dots-instancing-shaders.html)

DOTS Instancing shaders in URP

[](dots-instancing-shaders-declare.html)

Declare DOTS Instancing properties in a custom shader in URP

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

