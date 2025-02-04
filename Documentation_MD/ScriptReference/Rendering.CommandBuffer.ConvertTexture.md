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

#  [CommandBuffer](Rendering.CommandBuffer.html).ConvertTexture

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

public void
ConvertTexture([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
src, [Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
dst);

## Declaration

public void
ConvertTexture([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
src, int srcElement,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html) dst,
int dstElement);

### Parameters

src | The source texture. The texture must be a Texture2D or Cubemap.  
---|---  
dst | The destination texture. The texture must be a Texture2D, Texture2DArray, Cubemap, or CubemapArray. The texture must also be uncompressed and correspond to a supported [RenderTextureFormat](RenderTextureFormat.html).  
srcElement | The element in the source texture to copy from. Use [CubemapFace](CubemapFace.html) if `src` is a Cubemap. Set the value to `0` if `src` is a 2D texture.  
dstElement | The element in the source texture to copy to. For example, the [CubemapFace](CubemapFace.html) in a Cubemap or the slice in a texture array. Set the value to `0` if `dst` is a 2D texture.  
  
### Description

Adds a command to copy the pixel data from one texture, convert the data into
a different format, and copy it into another texture.

This method adds a command to convert and copy pixel data from one texture to
another on the GPU.  
  
When you use `ConvertTexture`, Unity does the following:

  1. Creates a temporary [RenderTexture](RenderTexture.html) that matches the size and format of the `dst` texture.
  2. Uses [Graphics.Blit](Graphics.Blit.html) to copy from the `src` texture to the temporary render texture, and converts to the format of `dst`.
  3. Uses [Graphics.CopyTexture](Graphics.CopyTexture.html) to copy from the temporary render texture to the `dst` texture.

This means it might be faster to convert the texture before you load it into
Unity. Or if you can create `dst` as a render texture, you can use
[CommandBuffer.Blit](Rendering.CommandBuffer.Blit.html) instead.  
  
You can use textures with different sizes for `src` and `dst`.  
  
`ConvertTexture` doesn't support the following conversions:

  * Cubemap to Texture2D.
  * Conversions that use RenderTextures - use [CommandBuffer.Blit](Rendering.CommandBuffer.Blit.html) instead.

You can't use `ConvertTexture` if you use OpenGL with MacOS. Depending on your
graphics API, you might not be able to do some types of conversions. For more
information on compatibility, see [SystemInfo.copyTextureSupport](SystemInfo-
copyTextureSupport.html),
[CopyTextureSupport](Rendering.CopyTextureSupport.html) and
[CommandBuffer.CopyTexture](Rendering.CommandBuffer.CopyTexture.html).  
  
To copy the converted texture from the GPU to the CPU, use
Texture2D.RequestIntoNativeArray.  
  
Additional resources: [CopyTextureSupport](Rendering.CopyTextureSupport.html).

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

