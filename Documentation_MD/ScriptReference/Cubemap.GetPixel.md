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

#  [Cubemap](Cubemap.html).GetPixel

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

public [Color](Color.html) GetPixel([CubemapFace](CubemapFace.html) face, int
x, int y, int mip = 0);

### Parameters

x | The x coordinate of the pixel to get. The range is `0` through (texture width - 1).  
---|---  
y | The y coordinate of the pixel to get. The range is `0` through (texture height - 1).  
mip | The mipmap level to sample. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
face | The [CubemapFace](CubemapFace.html) to sample.  
  
### Returns

**Color** The pixel color.

### Description

Gets the pixel color at coordinates (`x`, `y`).

This method gets pixel data from the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
The lower left corner of a face is (0, 0). If the pixel coordinate is outside
the texture's dimensions, Unity clamps or repeats it, depending on the
texture's [TextureWrapMode](TextureWrapMode.html).  
  
`GetPixel` might be slower than some other texture methods because it converts
the format the texture uses into [Color](Color.html). `GetPixel` also needs to
decompress compressed textures, and use memory to store the decompressed area.
To get pixel data more quickly, use [GetPixelData](Cubemap.GetPixelData.html)
instead.  
  
If you need to get a large block of pixels, it might be faster to use
[GetPixels](Cubemap.GetPixels.html).  
  
You can't use `GetPixel` with textures that use Crunch texture compression.  
  
Additional resources: [GetPixels](Cubemap.GetPixels.html),
[SetPixel](Cubemap.SetPixel.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Cubemap](Cubemap.html) texture;  
      
        void Start()
        {
            // prints the color of the pixel at (0,0) of the +X face
            [Debug.Log](Debug.Log.html)(texture.GetPixel([CubemapFace.PositiveX](CubemapFace.PositiveX.html), 0, 0));
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

