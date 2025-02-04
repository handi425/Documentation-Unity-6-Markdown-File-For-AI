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

#  [CubemapArray](CubemapArray.html).GetPixelData

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

[Switch to Manual](../Manual/class-CubemapArray.html "Go to CubemapArray
Component in the Manual")

## Declaration

public NativeArray<T> GetPixelData(int mipLevel,
[CubemapFace](CubemapFace.html) face, int element);

### Parameters

mipLevel | The mipmap level to read from. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
---|---  
face | The [CubemapFace](CubemapFace.html) to read from.  
element | The array slice to read from.  
  
### Returns

**NativeArray <T>** A native array that points directly to the texture's data
buffer in CPU memory.

### Description

Gets the raw data from a texture.

This method returns a [NativeArray<T0>](Unity.Collections.NativeArray_1.html)
that points directly to the texture's data on the CPU and has the size of the
mipmap level. The array doesn't contain a copy of the data, so `GetPixelData`
doesn't allocate any memory.  
  
For example, if the slice is 16 × 16 pixels and RGBA32 format, and you set
`mipLevel` to `1`, the method returns an array with 64 elements (8 × 8 pixels)
and a size of 256 bytes if you use [Color32](Color32.html) for `T` (4 bytes
per pixel). You can use the experimental
[GraphicsFormatUtility.ComputeMipmapSize](Experimental.Rendering.GraphicsFormatUtility.ComputeMipmapSize.html)
API to calculate the size of a mipmap level.  
  
You usually use a struct for `T` that matches the structure of a pixel in the
texture, for example [Color32](Color32.html) if the texture format uses RGBA
pixels in 32-bit format, such as
[TextureFormat.RGBA32](TextureFormat.RGBA32.html).  
  
You can read from and write to the returned array to get and change the data
directly in CPU memory. If you write to the array, you must then call the
[Apply](CubemapArray.Apply.html) method to upload the texture to the GPU.  
  
Use the returned array immediately. If you store the array and use it later,
it might not point to the correct memory location if the texture has been
modified or updated.  
  
If you use a small type for `T` such as `byte`, `GetPixelData` may fail
because the `NativeArray` would exceed the maximum length (`Int32.MaxValue`).
To avoid this, use a larger type or struct.  
  
`GetPixelData` throws an exception when it fails.  
  
Additional resources: [Apply](CubemapArray.Apply.html),
[SetPixels](CubemapArray.SetPixels.html),
[SetPixels32](CubemapArray.SetPixels32.html),
[GetPixelData](CubemapArray.GetPixelData.html).

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public void Start()
        {  
      
            // Create a cubemap array
            var m_CubemapArray = new [CubemapArray](CubemapArray.html)(16, 3, [TextureFormat.RGBA32](TextureFormat.RGBA32.html), true);  
      
            // Use GetPixelData to get an array that points to mipmap level 1, +z face
            var mip1Face4element1 = m_CubemapArray.GetPixelData<[Color32](Color32.html)>(1, [CubemapFace.PositiveZ](CubemapFace.PositiveZ.html), 1);  
      
            // Fill pixels in mipmap level 1 with white
            for (int i = 0; i < mip1Face4element1.Length; i++)
            {
                mip1Face4element1[i] = new [Color32](Color32.html)(255, 255, 255, 255);
            }  
      
            // Copy the texture changes to the GPU
            m_CubemapArray.Apply(false);
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

