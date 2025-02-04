[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dots-instancing-shaders-access.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-access.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-access.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-access.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dots-instancing-shaders-access.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-access.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-access.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-access.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
  * Access DOTS Instancing properties in a custom shader

[](dots-instancing-shaders-declare.html)

Declare DOTS Instancing properties in a custom shader in URP

[](dots-instancing-shaders-best-practice.html)

Best practice for DOTS Instancing shaders in URP

# Access DOTS Instancing properties in a custom shader

To access DOTS Instanced properties, your **shader** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) can use one of the access macros that
Unity provides. The access macros assume that instance data in
`unity_DOTSInstanceData` uses the following layout:

  * The 31 least significant bits of the metadata value contain the byte address of the first instance in the batch within the `unity_DOTSInstanceData` buffer.
  * If the most significant bit of the metadata value is `0`, every instance uses the value from instance index zero. This means each instance loads directly from the byte address in the metadata value. In this case, the buffer only needs to store a single value, instead of one value per instance.
  * If the most significant bit of the metadata value is `1`, the address should contain an array where you can find the value for instance index `instanceID` using `AddressOfInstance0 + sizeof(PropertyType) * instanceID`. In this case, you should ensure that every rendered instance index has valid data in buffer. Otherwise, out-of-bounds access and undefined behavior can occur.

You can also set the the metadata value directly which is useful if you want
to use a custom data source that doesn’t use the above layout, such as a
texture.

For an example of how to use these macros, see [Access macro example](dots-
instancing-shaders-per-instance.html).

[](dots-instancing-shaders-declare.html)

Declare DOTS Instancing properties in a custom shader in URP

[](dots-instancing-shaders-best-practice.html)

Best practice for DOTS Instancing shaders in URP

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

