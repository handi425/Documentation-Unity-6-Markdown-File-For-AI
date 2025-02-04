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

#  [Texture2D](Texture2D.html).GetRawTextureData

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

public NativeArray<T> GetRawTextureData();

### Returns

**NativeArray <T>** A native array that points directly to the texture's data
buffer in CPU memory.

### Description

Gets the raw data from a texture, as an array that points to memory.

This version of the `GetRawTextureData` method returns a
[NativeArray<T0>](Unity.Collections.NativeArray_1.html) that points directly
to the texture's data on the CPU. The array doesn't contain a copy of the
data, so `GetRawTextureData` doesn't allocate any memory. To return a copy,
use the version that returns a `byte[]` array instead.  
  
You can also use [GetPixelData](Texture2D.GetPixelData.html). You can use
`GetPixelData` to get a mipmap level instead of the entire texture.  
  
You usually use a struct for `T` that matches the structure of a pixel in the
texture, for example [Color32](Color32.html) if the texture format uses RGBA
pixels in 32-bit format, such as
[TextureFormat.RGBA32](TextureFormat.RGBA32.html).  
  
The returned array contains the entire texture according to its width, height,
data [format](Texture2D-format.html) and [mipmapCount](Texture-
mipmapCount.html). For example, if the texture is 16 × 8 pixels and RGBA32
format with no mipmaps, the method returns an array with a size of 512 bytes
(16 × 8 × 4 bytes), and contains 128 elements if you use
[Color32](Color32.html) for `T` (4 bytes per pixel). You can use the
experimental
[GraphicsFormatUtility.ComputeMipmapSize](Experimental.Rendering.GraphicsFormatUtility.ComputeMipmapSize.html)
API to calculate the size of a mipmap level.  
  
The array starts with mipmap level 0.  
  
You can read from and write to the returned array to get and change the data
directly in CPU memory. If you write to the array, you must then call the
[Apply](Texture2D.Apply.html) method to upload the texture to the GPU.  
  
Use the returned array immediately. If you store the array and use it later,
it might not point to the correct memory location if the texture has been
modified or updated.  
  
If you use a small type for `T` such as `byte`, `GetRawTextureData` may fail
because the `NativeArray` would exceed the maximum length (`Int32.MaxValue`).
To avoid this, use a larger type or struct.  
  
`GetRawTextureData` throws an exception when it fails.  
  
Additional resources: [Apply](Texture2D.Apply.html),
[SetPixels](Texture2D.SetPixels.html),
[SetPixels32](Texture2D.SetPixels32.html),
[LoadRawTextureData](Texture2D.LoadRawTextureData.html),
[GetPixelData](Texture2D.GetPixelData.html).

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var texture = new [Texture2D](Texture2D.html)(128, 128, [TextureFormat.RGBA32](TextureFormat.RGBA32.html), false);
            GetComponent<[Renderer](Renderer.html)>().material.mainTexture = texture;  
      
            // RGBA32 texture format data layout exactly matches [Color32](Color32.html) struct
            var data = texture.GetRawTextureData<[Color32](Color32.html)>();  
      
            // fill texture data with a simple pattern
            [Color32](Color32.html) orange = new [Color32](Color32.html)(255, 165, 0, 255);
            [Color32](Color32.html) teal = new [Color32](Color32.html)(0, 128, 128, 255);
            int index = 0;
            for (int y = 0; y < texture.height; y++)
            {
                for (int x = 0; x < texture.width; x++)
                {
                    data[index++] = ((x & y) == 0 ? orange : teal);
                }
            }
            // upload to the GPU
            texture.Apply();
        }
    }
    

* * *

## Declaration

public byte[] GetRawTextureData();

### Returns

**byte[]** A byte array that contains raw texture data.

### Description

Gets the raw data from a texture, as a copy.

This version of the `GetRawTextureData` method returns a copy of the raw
texture data on the CPU. [Texture.isReadable](Texture-isReadable.html) must be
`true`.  
  
If you don't need a copy or if you want to modify the data directly, use the
version of this function that returns a `NativeArray`, or
[Texture2D.GetPixelData](Texture2D.GetPixelData.html).  
  
You can use the returned array with
[LoadRawTextureData](Texture2D.LoadRawTextureData.html). This allows you to
serialize and load a textures of any format, including compressed textures,
and load the data into a texture later.  
  
The CPU texture might not match the GPU texture if you used a method such as
[Graphics.CopyTexture](Graphics.CopyTexture.html) that only updates GPU
textures, so the CPU texture is out of sync.  
  
The maximum size of the returned array is 2 gigabytes, because C# arrays have
a maximum of 2 billion elements. If you need more than 2 gigabytes of data,
use the version of this function that returns a `NativeArray`, and use
[Color32](Color32.html) for `T` or a struct that matches the format of the
texture.  
  
`GetRawTextureData` throws an exception when it fails.

    
    
    using UnityEngine;  
      
    class CopyTexture : [MonoBehaviour](MonoBehaviour.html)
    {
        // the source texture.
        [Texture2D](Texture2D.html) tex;  
      
        void Start()
        {
            // Create a copy of the texture by reading and applying the raw texture data.
            [Texture2D](Texture2D.html) texCopy = new [Texture2D](Texture2D.html)(tex.width, tex.height, tex.format, tex.mipmapCount > 1);
            texCopy.LoadRawTextureData(tex.GetRawTextureData());
            texCopy.Apply();
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

