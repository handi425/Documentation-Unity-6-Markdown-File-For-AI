[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shaders-in-universalrp-srp-batcher.html)
  * [中文](/cn/current/Manual/urp/shaders-in-universalrp-srp-batcher.html)
  * [日本語](/ja/current/Manual/urp/shaders-in-universalrp-srp-batcher.html)
  * [한국어](/kr/current/Manual/urp/shaders-in-universalrp-srp-batcher.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shaders-in-universalrp-srp-batcher.html)
  * [中文](/cn/current/Manual/urp/shaders-in-universalrp-srp-batcher.html)
  * [日本語](/ja/current/Manual/urp/shaders-in-universalrp-srp-batcher.html)
  * [한국어](/kr/current/Manual/urp/shaders-in-universalrp-srp-batcher.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](../urp/writing-custom-shaders-urp.html)
  * Make a URP shader compatible with the SRP Batcher

[](../urp/urp-shaders/urp-shaderlab-pass-tags.html)

ShaderLab Pass tags in URP reference

[](../urp/shaders-in-universalrp-reference.html)

Shader Material Inspector window reference for URP

# Make a URP shader compatible with the SRP Batcher

To ensure that a **Shader** A program that runs on the GPU. [More
info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) is SRP Batcher compatible:

  * Declare all Material properties in a single CBUFFER called `UnityPerMaterial`.
  * Declare all built-in engine properties, such as `unity_ObjectToWorld` or `unity_WorldTransformParams`, in a single CBUFFER called `UnityPerDraw`.

For more information on the SRP Batcher, refer to the documentation on the
[Scriptable Render Pipeline (SRP)
Batcher](https://docs.unity3d.com/Manual/SRPBatcher.html).

[](../urp/urp-shaders/urp-shaderlab-pass-tags.html)

ShaderLab Pass tags in URP reference

[](../urp/shaders-in-universalrp-reference.html)

Shader Material Inspector window reference for URP

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

