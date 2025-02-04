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

#  [Texture2DArray](Texture2DArray.html).CopyPixels

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

[Switch to Manual](../Manual/class-Texture2DArray.html "Go to Texture2DArray
Component in the Manual")

## Declaration

public void CopyPixels([Texture](Texture.html) src);

## Declaration

public void CopyPixels([Texture](Texture.html) src, int srcElement, int
srcMip, int dstElement, int dstMip);

## Declaration

public void CopyPixels([Texture](Texture.html) src, int srcElement, int
srcMip, int srcX, int srcY, int srcWidth, int srcHeight, int dstElement, int
dstMip, int dstX, int dstY);

### Parameters

src | The source texture.  
---|---  
srcElement | The element in the source texture to copy from. For example, the [CubemapFace](CubemapFace.html) in a Cubemap or the slice in a texture array. Set the value to `0` if `src` is a 2D texture.  
srcMip | The mipmap level to copy from. The range is `0` through the source texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
dstElement | The slice index to copy to in this texture array.  
dstMip | The mipmap level to write to. The range is `0` through this texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
srcX | The starting x coordinate of `src` to copy from. `0` is the left of the texture.  
srcY | The starting y coordinate of `src` to copy from. `0` is the bottom of the texture.  
srcWidth | The width of `src` to copy.  
srcHeight | The height of `src` to copy.  
dstX | The x coordinate of this texture to copy to.  
dstY | The y coordinate to this texture to copy to.  
  
### Description

Copies pixel data from another texture on the CPU.

This method copies pixel data from a source texture to this one on the CPU.
[Texture.isReadable](Texture-isReadable.html) must be `true` for both the
texture and `src`, and you must call [Apply](Texture2DArray.Apply.html) after
`CopyPixels` to upload the changed pixels to the GPU.  
  
[Apply](Texture2DArray.Apply.html) is an expensive operation because it copies
all the pixels in the texture even if you've only changed some of the pixels,
so change as many pixels as possible before you call it. If you only need to
copy pixels on the GPU, [Graphics.CopyTexture](Graphics.CopyTexture.html) with
[GraphicsTexture](Rendering.GraphicsTexture.html) parameters is faster to use
instead.  
  
To use `CopyPixels`, the size to be copied must be the same in both textures.
Use the region-based overload to specify a smaller region than a full mipmap
level.  
  
Crunch compressed texture formats are not supported in the element-based
overload. Compressed texture formats are not supported at all for for the
region-based overload. Unity throws a `UnityException` if either texture is
unreadable, and throws an `ArgumentException` if `CopyPixels` fails.  
  
Additional resources: [Apply](Texture2DArray.Apply.html),
[Graphics.CopyTexture](Graphics.CopyTexture.html),
[SetPixels](Texture2DArray.SetPixels.html).

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

