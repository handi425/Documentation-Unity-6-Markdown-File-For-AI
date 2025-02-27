[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dots-instancing-shaders.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dots-instancing-shaders.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
  * DOTS Instancing shaders in URP

[](batch-renderer-group-writing-shaders.html)

Writing custom shaders for the BatchRendererGroup API

[](dots-instancing-shaders-support.html)

Support DOTS Instancing in a a custom shader in URP

# DOTS Instancing shaders in URP

To render large instance counts efficiently, BRG uses a new **shader** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) instancing mode called DOTS
Instancing. Every shader that BRG uses must support DOTS Instancing. In
traditional instanced shaders, the shader is passed an array for each
instanced property in a constant or uniform buffer, such that each element in
each array contains the property value for a single instance in the draw. In
DOTS Instanced shaders, Unity passes one 32-bit integer to the shader for each
DOTS Instanced property. This 32-bit integer is called a metadata value. This
integer can represent anything you want, but typically it represents an offset
in the buffer from where the shader loads property data for the instance that
the shader is rendering.

DOTS Instancing has many advantages compared to traditional instancing,
including the following:

  * The instance data is stored in a GraphicsBuffer and remains persistent on the GPU, which means that Unity doesn’t need to set it up again each time it renders the instance. Setting up data only when an instance actually changes can significantly improve performance in cases where instance data changes rarely or not at all. This is much more efficient than traditional instancing, which requires an engine to set up all data for every instance every frame.
  * The process for setting up instance data is separate from setting up the draw call. This makes draw call setup lightweight and efficient. BRG makes this possible with a special fast path of the SRP Batcher that only does a minimal amount of work for each draw call. The responsibility for this work moves to you and gives you more control over what to render in each draw call.
  * The size of a draw call is no longer limited by how much instance data can fit in a constant or uniform buffer. This makes it possible for BRG to render larger instance counts with a single draw call.   
**Note** : The number of instance indices still limits the draw call size,
since each index still requires some data. However, an index consumes far less
memory than a full set of instanced properties which means many more instances
can fit inside a constant or uniform buffer. For example, each index requires
16 byes so if the memory limit for a buffer on a particular platform is 64kb,
4096 indices can fit in the buffer.

  * If every instance uses the same value for a given property, it is possible to have all instances load the value from the same place in memory. This saves memory and the number of GPU cycles spent duplicating the value for each instance.

[](batch-renderer-group-writing-shaders.html)

Writing custom shaders for the BatchRendererGroup API

[](dots-instancing-shaders-support.html)

Support DOTS Instancing in a a custom shader in URP

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

