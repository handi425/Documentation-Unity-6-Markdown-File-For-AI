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

#  [Texture3D](Texture3D.html).SetPixelData

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

public void SetPixelData(T[] data, int mipLevel, int sourceDataStartIndex =
0);

## Declaration

public void SetPixelData(NativeArray<T> data, int mipLevel, int
sourceDataStartIndex = 0);

### Parameters

data | The array of data to use.  
---|---  
mipLevel | The mipmap level to write to. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
sourceDataStartIndex | The index in the source array to start copying from. The default value is `0`.  
  
### Description

Sets the raw data of an entire mipmap level directly in CPU memory.

This method sets pixel data for the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`, and you must
call [Apply](Texture3D.Apply.html) after `SetPixelData` to upload the changed
pixels to the GPU.  
  
`SetPixelData` is useful if you want to load compressed or other non-color
texture format data into a texture.  
  
The size of the `data` array must be the width × height × depth of the mipmap
level, and the data layout must match the texture format, otherwise
`SetPixelData` fails. You can use `byte` for `T` if you don't want to define a
custom struct to match the texture format.  
  
Unity throws an exception when `SetPixelData` fails.  
  
Additional resources: [SetPixels](Texture3D.SetPixels.html),
[GetPixelData](Texture3D.GetPixelData.html), [Apply](Texture3D.Apply.html).

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture3D](Texture3D.html) texture;
        public void Start()
        {
            texture = new [Texture3D](Texture3D.html)(2, 2, 2, [TextureFormat.RGB24](TextureFormat.RGB24.html), true);
            var data = new byte[]
            {
                255, 0, 0, // red
                0, 255, 0, // green
                0, 0, 255, // blue
                255, 235, 4, // yellow
                128, 0, 0, // dark red
                0, 128, 0, // dark green
                0, 0, 128, // dark blue
                128, 117, 4, // dark yellow
            };
            texture.SetPixelData(data, 0);
            texture.filterMode = [FilterMode.Point](FilterMode.Point.html);
            texture.Apply(updateMipmaps: false);
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

