[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# ShaderRequirements

enumeration

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Shader features required by a specific shader. Features are bit flags.

### Properties

[None](Rendering.ShaderRequirements.None.html)| No shader requirements.  
---|---  
[BaseShaders](Rendering.ShaderRequirements.BaseShaders.html)| Indicates that
basic shader capability i.e. Shader Model level 2.0 is required.  
[Interpolators10](Rendering.ShaderRequirements.Interpolators10.html)|
Indicates that support for at least 10 interpolators is required.  
[Interpolators32](Rendering.ShaderRequirements.Interpolators32.html)|
Indicates that support for at least 32 interpolators is required.  
[MRT4](Rendering.ShaderRequirements.MRT4.html)| Indicates that support for
multiple render targets (at least 4) is required i.e. support for fragment
shaders that can output at least 4 values.  
[MRT8](Rendering.ShaderRequirements.MRT8.html)| Indicates that support for
multiple render targets (at least 8) is required i.e. support for fragment
shaders that can output at least 8 values.  
[Derivatives](Rendering.ShaderRequirements.Derivatives.html)| Indicates that
support for derivative (ddx/ddy) instructions from the fragment shader stage
is required.  
[SampleLOD](Rendering.ShaderRequirements.SampleLOD.html)| Indicates that
support for texture sampling from the fragment shader stage with an explicit
mipmap level is required.  
[FragCoord](Rendering.ShaderRequirements.FragCoord.html)| Indicates that
support for pixel position (SV_Position) input to the fragment shader stage is
required.  
[FragClipDepth](Rendering.ShaderRequirements.FragClipDepth.html)| Indicates
that support for pixel depth (SV_Position.zw) input to the fragment shader
stage is required.  
[Interpolators15Integers](Rendering.ShaderRequirements.Interpolators15Integers.html)|
Indicates that support for at least 15 integers and interpolators in total are
required. Unity bundles them together because it is extremely unlikely a
GPU/API will ever exist that only has part of that.  
[Texture2DArray](Rendering.ShaderRequirements.Texture2DArray.html)| Indicates
that support for 2D array textures (Texture2DArray) is required.  
[Instancing](Rendering.ShaderRequirements.Instancing.html)| Indicates that
support for the SV_InstanceID input semantic is required.  
[Geometry](Rendering.ShaderRequirements.Geometry.html)| Indicates that
geometry shader stage support is required.  
[CubeArray](Rendering.ShaderRequirements.CubeArray.html)| Indicates that
cubemap array (TextureCubeArray) support is required.  
[Compute](Rendering.ShaderRequirements.Compute.html)|  Indicates that compute
shader support is required.  
[RandomWrite](Rendering.ShaderRequirements.RandomWrite.html)| Indicates that
support for random-write textures (UAVs) is required.  
[TessellationCompute](Rendering.ShaderRequirements.TessellationCompute.html)|
Indicates that support for tessellation using a compute shader for control
point processing is required. The Metal graphics API requires this feature for
tessellation.  
[TessellationShaders](Rendering.ShaderRequirements.TessellationShaders.html)|
Indicates that support for tessellation using hull and domain shader stages is
required.  
[SparseTexelResident](Rendering.ShaderRequirements.SparseTexelResident.html)|
Indicates that support of sparse textures with sampling instructions that
return residency information is requred.  
[FramebufferFetch](Rendering.ShaderRequirements.FramebufferFetch.html)|
Indicates that framebuffer fetch support is required. This is the ability to
have fragment shader color arguments with in/out modifiers.  
[MSAATextureSamples](Rendering.ShaderRequirements.MSAATextureSamples.html)|
Indicates that support for MSAA textures (e.g. Texture2DMS) is required.  
[SetRTArrayIndexFromAnyShader](Rendering.ShaderRequirements.SetRTArrayIndexFromAnyShader.html)|
Indicates that support for setting the render target array index
(SV_RenderTargetArrayIndex) from all shader stages (not just from the geometry
shader stage) is required.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

