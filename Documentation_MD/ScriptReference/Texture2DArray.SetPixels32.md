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

#  [Texture2DArray](Texture2DArray.html).SetPixels32

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

public void SetPixels32(Color32[] colors, int arrayElement, int miplevel);

## Declaration

public void SetPixels32(Color32[] colors, int arrayElement);

### Parameters

colors | The array of pixel colours to use. This is a 2D image flattened to a 1D array.  
---|---  
arrayElement | The array slice to write `colors` to.  
miplevel | The mipmap level to write `colors` to. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
  
### Description

Sets the pixel colors of an entire mipmap level of a slice.

This method sets pixel data for the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`, and you must
call [Apply](Texture2DArray.Apply.html) after `SetPixels32` to upload the
changed pixels to the GPU.  
  
`colors` must contain the pixels row by row, starting at the bottom left of
the texture. The size of the array must be the width x height of the mipmap
level.  
  
`SetPixels32` might be slower than some other texture methods because it
converts the [Color32](Color32.html) struct into the format the texture uses.
To set pixel data more quickly, use
[SetPixelData](Texture2DArray.SetPixelData.html) instead.  
  
You can use `SetPixels32` with the following [texture
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

For all other formats, `SetPixels32` fails. Unity throws an exception when
`SetPixels32` fails.  
  
Additional resources: [SetPixels](Texture2DArray.SetPixels.html),
[SetPixelData](Texture2DArray.SetPixelData.html),
[GetPixels32](Texture2DArray.GetPixels32.html),
[GetPixels](Texture2DArray.GetPixels.html),
[Apply](Texture2DArray.Apply.html), [mipmapCount](Texture-mipmapCount.html).

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

