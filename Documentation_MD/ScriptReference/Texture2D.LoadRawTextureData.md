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

#  [Texture2D](Texture2D.html).LoadRawTextureData

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

public void LoadRawTextureData(byte[] data);

## Declaration

public void LoadRawTextureData(NativeArray<T> data);

## Declaration

public void LoadRawTextureData(IntPtr data, int size);

### Parameters

data | The array of data to use.  
---|---  
size | The size of the data in bytes.  
  
### Description

Sets the raw data of an entire texture in CPU memory.

This method sets pixel data for the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`, and you must
call [Apply](Texture2D.Apply.html) after `LoadRawTextureData` to upload the
changed pixels to the GPU.  
  
You can also use the following to write to a texture:

  * [Texture2D.SetPixelData](Texture2D.SetPixelData.html), which you can use to set a mipmap level instead of the entire texture.
  * [GetRawTextureData](Texture2D.GetRawTextureData.html), which returns a `NativeArray` you can write to, and can be faster because it avoids copying memory.

The size of the `data` array must fill the entire texture according to its
width, height and [mipmapCount](Texture-mipmapCount.html), and the data layout
must match the texture format. Otherwise `LoadRawTextureData` fails.  
  
For example, if the texture is 16 × 8 pixels and RGBA32 format with no
mipmaps, the array must be a size of 512 bytes (16 × 8 × 4 bytes). You can use
the experimental
[GraphicsFormatUtility.ComputeMipmapSize](Experimental.Rendering.GraphicsFormatUtility.ComputeMipmapSize.html)
API to calculate the size of a mipmap level.  
  
The array must start with mipmap level 0.  
  
Additional resources: [SetPixels](Texture2D.SetPixels.html),
[SetPixels32](Texture2D.SetPixels32.html),
[SetPixelData](Texture2D.SetPixelData.html), [Apply](Texture2D.Apply.html),
[GetRawTextureData](Texture2D.GetRawTextureData.html),
[ImageConversion.LoadImage](ImageConversion.LoadImage.html).

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public void Start()
        {
            // Create a 16 x 16 texture with PVRTC RGBA4 format and fill it with raw PVRTC bytes.
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)(16, 16, [TextureFormat.PVRTC_RGBA4](TextureFormat.PVRTC_RGBA4.html), false);  
      
            // Raw PVRTC4 data for a 16 x 16 texture.
            // This format is four bits per pixel, so the data should be 128 (16 x 16 / 2) bytes in size.
            // The texture encoded here is mostly green with some angular blue and red lines.
            byte[] pvrtcBytes = new byte[]
            {
                0x30, 0x32, 0x32, 0x32, 0xe7, 0x30, 0xaa, 0x7f, 0x32, 0x32, 0x32, 0x32, 0xf9, 0x40, 0xbc, 0x7f,
                0x03, 0x03, 0x03, 0x03, 0xf6, 0x30, 0x02, 0x05, 0x03, 0x03, 0x03, 0x03, 0xf4, 0x30, 0x03, 0x06,
                0x32, 0x32, 0x32, 0x32, 0xf7, 0x40, 0xaa, 0x7f, 0x32, 0xf2, 0x02, 0xa8, 0xe7, 0x30, 0xff, 0xff,
                0x03, 0x03, 0x03, 0xff, 0xe6, 0x40, 0x00, 0x0f, 0x00, 0xff, 0x00, 0xaa, 0xe9, 0x40, 0x9f, 0xff,
                0x5b, 0x03, 0x03, 0x03, 0xca, 0x6a, 0x0f, 0x30, 0x03, 0x03, 0x03, 0xff, 0xca, 0x68, 0x0f, 0x30,
                0xaa, 0x94, 0x90, 0x40, 0xba, 0x5b, 0xaf, 0x68, 0x40, 0x00, 0x00, 0xff, 0xca, 0x58, 0x0f, 0x20,
                0x00, 0x00, 0x00, 0xff, 0xe6, 0x40, 0x01, 0x2c, 0x00, 0xff, 0x00, 0xaa, 0xdb, 0x41, 0xff, 0xff,
                0x00, 0x00, 0x00, 0xff, 0xe8, 0x40, 0x01, 0x1c, 0x00, 0xff, 0x00, 0xaa, 0xbb, 0x40, 0xff, 0xff,
            };  
      
            // Load data into the texture and upload it to the GPU.
            tex.LoadRawTextureData(pvrtcBytes);
            tex.Apply();  
      
            // Assign the texture to this [GameObject](GameObject.html)'s material.
            GetComponent<[Renderer](Renderer.html)>().material.mainTexture = tex;
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

