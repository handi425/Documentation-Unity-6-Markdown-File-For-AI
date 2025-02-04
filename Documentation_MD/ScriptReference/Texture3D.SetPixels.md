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

#  [Texture3D](Texture3D.html).SetPixels

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

[Switch to Manual](../Manual/class-Texture3D.html "Go to Texture3D Component
in the Manual")

## Declaration

public void SetPixels(Color[] colors, int miplevel);

## Declaration

public void SetPixels(Color[] colors);

### Parameters

colors | The array of pixel colours to use. This is a 3D texture flattened to a 1D array.  
---|---  
miplevel | The mipmap level to write `colors` to. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
  
### Description

Sets the pixel colors of an entire mipmap level.

This method sets pixel data for the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`, and you must
call [Apply](Texture3D.Apply.html) after `SetPixels` to upload the changed
pixels to the GPU.  
  
[Apply](Texture3D.Apply.html) is an expensive operation because it copies all
the pixels in the texture even if you've only changed some of the pixels, so
change as many pixels as possible before you call it.  
  
`colors` must contain the pixels slice by slice starting at the front of the
texture. Each slice must contain the pixels row by row, starting at the bottom
left of the texture. The size of the array must be the width × height × depth
of the mipmap level.  
  
A single call to `SetPixels` is usually faster than multiple calls to
[SetPixel](Texture3D.SetPixel.html), especially for large textures.  
  
`SetPixels` might be slower than some other texture methods because it
converts the [Color](Color.html) struct into the format the texture uses. To
set pixel data more quickly, use [SetPixelData](Texture3D.SetPixelData.html)
instead.  
  
You can use `SetPixels` with the following [texture
formats](TextureFormat.html):

  * Alpha8
  * ARGB32
  * ARGB4444
  * BGRA32
  * R16
  * R16_SIGNED
  * R8
  * R8_SIGNED
  * RFloat
  * RG16
  * RG16_SIGNED
  * RG32
  * RG32_SIGNED
  * RGB24
  * RGB24_SIGNED
  * RGB48
  * RGB48_SIGNED
  * RGB565
  * RGB9e5Float
  * RGBA32
  * RGBA32_SIGNED
  * RGBA4444
  * RGBA64
  * RGBA64_SIGNED
  * RGBAFloat
  * RGBAHalf
  * RGFloat
  * RGHalf
  * RHalf

For all other formats, `SetPixels` fails. Unity throws an exception when
`SetPixels` fails.  
  
Additional resources: [GetPixels](Texture3D.GetPixels.html),
[SetPixels32](Texture3D.SetPixels32.html),
[SetPixelData](Texture3D.SetPixelData.html), [Apply](Texture3D.Apply.html),
[mipmapCount](Texture-mipmapCount.html).

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

