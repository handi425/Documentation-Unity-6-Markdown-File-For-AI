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

#  [CommandBuffer](Rendering.CommandBuffer.html).Blit

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

public void Blit([Texture](Texture.html) source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest);

## Declaration

public void Blit([Texture](Texture.html) source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Material](Material.html) mat);

## Declaration

public void Blit([Texture](Texture.html) source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Material](Material.html) mat, int pass);

## Declaration

public void Blit([Texture](Texture.html) source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Vector2](Vector2.html) scale, [Vector2](Vector2.html) offset);

## Declaration

public void
Blit([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest);

## Declaration

public void
Blit([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Material](Material.html) mat);

## Declaration

public void
Blit([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Material](Material.html) mat, int pass);

## Declaration

public void
Blit([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Vector2](Vector2.html) scale, [Vector2](Vector2.html) offset);

## Declaration

public void
Blit([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, int sourceDepthSlice, int destDepthSlice);

## Declaration

public void
Blit([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Vector2](Vector2.html) scale, [Vector2](Vector2.html) offset, int
sourceDepthSlice, int destDepthSlice);

## Declaration

public void
Blit([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
source,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dest, [Material](Material.html) mat, int pass, int destDepthSlice);

### Parameters

source | The source texture or [RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html).  
---|---  
dest | The destination [RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html).  
mat | The material to use. If you don't provide `mat`, Unity uses a default material.  
pass | If the value is `-1`, Unity draws all the passes in `mat`. Otherwise, Unity draws only the pass you set `pass` to. The default value is `-1`.  
scale | The scale to apply.  
offset | The offset to apply.  
sourceDepthSlice | The element in the source texture to copy from, for example the texture in a texture array. You can't use `sourceDepthSlice` to specify a face in a Cubemap.  
destDepthSlice | The element in the destination texture to copy from, for example the texture in a texture array. You can't use `destDepthSlice` to specify a face in a Cubemap.  
  
### Description

Adds a command to use a shader to copy the pixel data from a texture into a
render texture.

This method adds a command to copy pixel data from a texture on the GPU to a
render texture on the GPU. This is one of the fastest ways to copy a texture.  
  
When you use `Graphics.Blit`, Unity does the following:

  1. Sets the [active render texture](RenderTexture-active.html) to the `dest` texture.
  2. Passes `source` to the `mat` material as the `_MainTex` property.
  3. Uses the material's shader to draw a full-screen surface from the `source` texture to the `dest` texture.

If you provide a `mat` material that doesn't have a `_MainTex` property,
`Blit` doesn't use `source`.  
  
You can use `Graphics.Blit` to create [post-processing
effects](../Manual/PostProcessingOverview.html), by setting `mat` to a
material with a custom shader.  
  
`Blit` changes [RenderTexture.active](RenderTexture-active.html). Store the
active render texture before you use `Blit` if you need to use it afterwards.  
  
Avoid setting `source` and `dest` to the same render texture, as this may
cause undefined behaviour. Use [Custom Render Textures](../Manual/class-
CustomRenderTexture.html) with double buffering instead, or use two render
textures and alternate between them to implement double buffering manually.  
  
In linear color space, set [GL.sRGBWrite](GL-sRGBWrite.html) before using
`Blit`, to make sure the sRGB-to-linear color conversion is what you expect.  
  
To blit to the screen in the Built-in Render Pipeline, follow these steps:

  1. Set `dest` to `null`. Unity now uses `Camera.main.targetTexture` as the destination texture.
  2. Set the [Camera.targetTexture](Camera-targetTexture.html) property of [Camera.main](Camera-main.html) to `null`.

To blit to the screen in the Universal Render Pipeline (URP) or the High
Definition Render Pipeline (HDRP), you must call
[Graphics.Blit](Graphics.Blit.html) or
[CommandBuffer.Blit](Rendering.CommandBuffer.Blit.html) inside a method that
you call from the
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html) callback.  
  
If you want to use a depth or stencil buffer that is part of the `source`
(Render)texture, or blit to a subregion of a texture, you have to manually
write an equivalent of the [Graphics.Blit](Graphics.Blit.html) function - i.e.
[Graphics.SetRenderTarget](Graphics.SetRenderTarget.html) with destination
color buffer and source depth buffer, setup orthographic projection
([GL.LoadOrtho](GL.LoadOrtho.html)), setup material pass
([Material.SetPass](Material.SetPass.html)) and draw a quad
([GL.Begin](GL.Begin.html)).  
  
Often the previous content of the Blit `dest` does not need to be preserved.
In this case, it is recommended to activate the `dest` render target
explicitly with the appropriate load and store actions using SetRenderTarget.
The Blit dest should then be set to
[BuiltinRenderTextureType.CurrentActive](Rendering.BuiltinRenderTextureType.CurrentActive.html).  
  
Additional resources: [Graphics.BlitMultiTap](Graphics.BlitMultiTap.html),
[Post-processing effects](../Manual/PostProcessingOverview.html).

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

