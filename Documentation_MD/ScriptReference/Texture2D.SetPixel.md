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

#  [Texture2D](Texture2D.html).SetPixel

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

public void SetPixel(int x, int y, [Color](Color.html) color, int mipLevel =
0);

### Parameters

x | The x coordinate of the pixel to set. The range is `0` through (texture width - 1).  
---|---  
y | The y coordinate of the pixel to set. The range is `0` through (texture height - 1).  
color | The color to set.  
mipLevel | The mipmap level to write to. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
  
### Description

Sets the pixel color at coordinates (`x`,`y`).

This method sets pixel data for the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`, and you must
call [Apply](Texture2D.Apply.html) after `SetPixel` to upload the changed
pixels to the GPU.  
  
[Apply](Texture2D.Apply.html) is an expensive operation because it copies all
the pixels in the texture even if you've only changed some of the pixels, so
change as many pixels as possible before you call it.  
  
`SetPixel` might be slower than some other texture methods because it converts
the [Color](Color.html) struct into the format the texture uses. To set pixel
data more quickly, use [SetPixelData](Texture2D.SetPixelData.html) instead.  
  
The lower left corner is (0, 0). If the pixel coordinate is outside the
texture's dimensions, Unity clamps or repeats it, depending on the texture's
[TextureWrapMode](TextureWrapMode.html).  
  
If you need to get a large block of pixels, it might be faster to use
[SetPixels32](Texture2D.SetPixels32.html).  
  
You can use `SetPixel` with the following [texture
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

For all other formats, Unity ignores `SetPixel`.  
  
Additional resources: [SetPixels](Texture2D.SetPixels.html),
[SetPixelData](Texture2D.SetPixelData.html),
[GetPixel](Texture2D.GetPixel.html), [Apply](Texture2D.Apply.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Texture2D](Texture2D.html) texture = new [Texture2D](Texture2D.html)(128, 128);
            GetComponent<[Renderer](Renderer.html)>().material.mainTexture = texture;  
      
            for (int y = 0; y < texture.height; y++)
            {
                for (int x = 0; x < texture.width; x++)
                {
                    [Color](Color.html) color = ((x & y) != 0 ? [Color.white](Color-white.html) : [Color.gray](Color-gray.html));
                    texture.SetPixel(x, y, color);
                }
            }
            texture.Apply();
        }
    }
    

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

