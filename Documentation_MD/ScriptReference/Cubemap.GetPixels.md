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

#  [Cubemap](Cubemap.html).GetPixels

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

public Color[] GetPixels([CubemapFace](CubemapFace.html) face, int miplevel);

## Declaration

public Color[] GetPixels([CubemapFace](CubemapFace.html) face);

### Parameters

face | The [CubemapFace](CubemapFace.html) to read from.  
---|---  
miplevel | The mipmap level to get. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
  
### Returns

**Color[]** An array that contains the pixel colors.

### Description

Gets the pixel color data for a mipmap level of a face as [Color](Color.html)
structs.

This method gets pixel data from the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
The array contains the pixels row by row, starting at the bottom left of the
face texture. The size of the array is the width × height of the mipmap level.  
  
Each pixel is a [Color](Color.html) struct. `GetPixels` might be slower than
some other texture methods because it converts the format the texture uses
into [Color](Color.html). `GetPixels` also needs to decompress compressed
textures, and use memory to store the decompressed area. To get pixel data
more quickly, use [GetPixelData](Cubemap.GetPixelData.html) instead.  
  
A single call to `GetPixels` is usually faster than multiple calls to
[GetPixel](Cubemap.GetPixel.html), especially for large textures.  
  
If `GetPixels` fails, Unity throws an exception. `GetPixels` might fail if the
array contains too much data. Use [GetPixelData](Cubemap.GetPixelData.html)
instead for very large textures.  
  
You can't use `GetPixel` with textures that use Crunch texture compression.

    
    
    using UnityEngine;  
      
    public class CubemapExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Cubemap](Cubemap.html) source;
        public [Cubemap](Cubemap.html) destination;  
      
        void Start()
        {
            // Get a copy of the color data from the source [Cubemap](Cubemap.html), in high-precision float format.
            // Each element in the array represents the color data for an individual pixel.
            [CubemapFace](CubemapFace.html) sourceFace = [CubemapFace.PositiveX](CubemapFace.PositiveX.html);
            int sourceMipLevel = 0;
            [Color](Color.html)[] pixels = source.GetPixels(sourceFace, sourceMipLevel);  
      
            // If required, manipulate the pixels before applying them to the destination texture.
            // This example code reverses the array, which rotates the image 180 degrees.
            System.Array.Reverse(pixels, 0, pixels.Length);  
      
            // Set the pixels of the destination [Cubemap](Cubemap.html).
            [CubemapFace](CubemapFace.html) destinationFace = [CubemapFace.PositiveX](CubemapFace.PositiveX.html);
            int destinationMipLevel = 0;
            destination.SetPixels(pixels, destinationFace, destinationMipLevel);  
      
            // Apply changes to the destination [Cubemap](Cubemap.html), which uploads its data to the GPU.
            destination.Apply();
        }
    }
    

Additional resources: [SetPixels](Cubemap.SetPixels.html),
[GetPixelData](Cubemap.GetPixelData.html), [mipmapCount](Texture-
mipmapCount.html).

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

