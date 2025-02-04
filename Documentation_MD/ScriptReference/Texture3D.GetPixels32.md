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

#  [Texture3D](Texture3D.html).GetPixels32

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

public Color32[] GetPixels32(int miplevel);

## Declaration

public Color32[] GetPixels32();

### Parameters

miplevel | The mipmap level to get. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
---|---  
  
### Returns

**Color32[]** An array that contains the pixel colors.

### Description

Gets the pixel color data for a mipmap level as [Color32](Color32.html)
structs.

This method gets pixel data from the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
The array contains the pixels slice by slice starting at the front of the
texture. Each slice contains the pixels row by row, starting at the bottom
left of the texture. The size of the array is the width × height × depth of
the mipmap level.  
  
Each pixel is a [Color32](Color32.html) struct. `GetPixels32` might be slower
than some other texture methods because it converts the format the texture
uses into [Color32](Color32.html). To get pixel data more quickly, use
[GetPixelData](Texture3D.GetPixelData.html) instead.  
  
A single call to `GetPixels32` is usually faster than multiple calls to
[GetPixel](Texture3D.GetPixel.html), especially for large textures.  
  
If `GetPixels32` fails, Unity throws an exception. `GetPixels32` might fail if
the array contains too much data. Use
[GetPixelData](Texture3D.GetPixelData.html) instead for very large textures.

    
    
    using UnityEngine;  
      
    public class Texture3DExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture3D](Texture3D.html) source;
        public [Texture3D](Texture3D.html) destination;  
      
        void Start()
        {
            // Get a copy of the color data from the source [Texture3D](Texture3D.html), in lower-precision int format.
            // Each element in the array represents the color data for an individual pixel.
            int sourceMipLevel = 0;
            [Color32](Color32.html)[] pixels = source.GetPixels32(sourceMipLevel);  
      
            // If required, manipulate the pixels before applying them to the destination texture.
            // This example code reverses the array, which rotates the image 180 degrees.
            System.Array.Reverse(pixels, 0, pixels.Length);  
      
            // Set the pixels of the destination [Texture3D](Texture3D.html).
            int destinationMipLevel = 0;
            destination.SetPixels32(pixels, destinationMipLevel);  
      
            // Apply changes to the destination [Texture3D](Texture3D.html), which uploads its data to the GPU.
            destination.Apply();
        }
    }
    

Additional resources: [SetPixel](Texture3D.SetPixel.html),
[SetPixels](Texture3D.SetPixels.html),
[SetPixels32](Texture3D.SetPixels32.html),
[GetPixel](Texture3D.GetPixel.html),
[GetPixelBilinear](Texture3D.GetPixelBilinear.html),
[GetPixels](Texture3D.GetPixels.html),
[GetPixelData](Texture3D.GetPixelData.html), [Apply](Texture3D.Apply.html)
functions.

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

