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

#  [Graphics](Graphics.html).BlitMultiTap

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

## Declaration

public static void BlitMultiTap([Texture](Texture.html) source,
[RenderTexture](RenderTexture.html) dest, [Material](Material.html) mat,
params Vector2[] offsets);

## Declaration

public static void BlitMultiTap([Texture](Texture.html) source,
[RenderTexture](RenderTexture.html) dest, [Material](Material.html) mat, int
destDepthSlice, params Vector2[] offsets);

## Declaration

public static void BlitMultiTap([Texture](Texture.html) source,
[Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) dest,
[Material](Material.html) mat, params Vector2[] offsets);

## Declaration

public static void BlitMultiTap([Texture](Texture.html) source,
[Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) dest,
[Material](Material.html) mat, int destDepthSlice, params Vector2[] offsets);

### Parameters

source | Source texture.  
---|---  
dest | Destination [RenderTexture](RenderTexture.html), [GraphicsTexture](Rendering.GraphicsTexture.html), or `null` to blit directly to screen.  
mat | Material to use for copying. Material's shader should do some post-processing effect.  
offsets | Variable number of filtering offsets. Offsets are given in pixels.  
destDepthSlice | The texture array destination slice to blit to.  
  
### Description

Copies source texture into destination, for multi-tap shader.

This is mostly used for implementing some [post-processing
effects](../Manual/PostProcessingOverview.html). For example, Gaussian or
iterative Cone blurring samples source texture at multiple different
locations.  
  
BlitMultiTap sets `dest` to be the active render target (changing
[RenderTexture.active](RenderTexture-active.html) and
[GraphicsTexture.active](Rendering.GraphicsTexture-active.html)), sets
`source` as `_MainTex` property on the material, and draws a full-screen quad.
Each vertex of the quad has multiple texture coordinates set up, offset by
`offsets` pixels.  
  
BlitMultiTap has the same limitations as [Graphics.Blit](Graphics.Blit.html).  
  
Additional resources: [Graphics.Blit](Graphics.Blit.html), [post-processing
effects](../Manual/PostProcessingOverview.html).

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

