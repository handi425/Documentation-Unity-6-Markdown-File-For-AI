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

# GraphicsFormatUsage

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

Use this format usages to figure out the capabilities of specific
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)

Each graphics card may not support all usages across formats. Use
[SystemInfo.IsFormatSupported](SystemInfo.IsFormatSupported.html) to check
which usages the graphics card supports.  
  
Additional resources: [Texture2D](Texture2D.html), [texture
assets](../Manual/Textures.html).

### Properties

[None](Experimental.Rendering.GraphicsFormatUsage.None.html)| No flags are
set.  
---|---  
[Sample](Experimental.Rendering.GraphicsFormatUsage.Sample.html)| Use this to
create and sample textures.  
[Linear](Experimental.Rendering.GraphicsFormatUsage.Linear.html)| Use this to
sample textures with a linear filter. This is for regular texture sampling
(non-shadow compare). Rentertextures created using
ShadowSamplingMode.CompareDepths always support linear filtering on the
comparison result.  
[Sparse](Experimental.Rendering.GraphicsFormatUsage.Sparse.html)| Use this to
create sparse textures  
[Render](Experimental.Rendering.GraphicsFormatUsage.Render.html)| Use this to
create and render to a rendertexture.  
[Blend](Experimental.Rendering.GraphicsFormatUsage.Blend.html)| Use this to
blend on a rendertexture.  
[GetPixels](Experimental.Rendering.GraphicsFormatUsage.GetPixels.html)| Use
this to get pixel data from a texture.  
[SetPixels](Experimental.Rendering.GraphicsFormatUsage.SetPixels.html)| Use
this to set pixel data to a texture.  
[SetPixels32](Experimental.Rendering.GraphicsFormatUsage.SetPixels32.html)|
Use this to set pixel data to a texture using `SetPixels32`.  
[ReadPixels](Experimental.Rendering.GraphicsFormatUsage.ReadPixels.html)| Use
this to read back pixels data from a rendertexture.  
[LoadStore](Experimental.Rendering.GraphicsFormatUsage.LoadStore.html)| Use
this to perform resource load and store on a texture  
[MSAA2x](Experimental.Rendering.GraphicsFormatUsage.MSAA2x.html)| Use this to
create and render to a MSAA 2X rendertexture.  
[MSAA4x](Experimental.Rendering.GraphicsFormatUsage.MSAA4x.html)| Use this to
create and render to a MSAA 4X rendertexture.  
[MSAA8x](Experimental.Rendering.GraphicsFormatUsage.MSAA8x.html)| Use this to
create and render to a MSAA 8X rendertexture.  
[StencilSampling](Experimental.Rendering.GraphicsFormatUsage.StencilSampling.html)|
Use this to create and render to the Stencil sub element of a RenderTexture.  
  
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

