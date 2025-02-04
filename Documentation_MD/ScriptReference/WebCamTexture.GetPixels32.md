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

#  [WebCamTexture](WebCamTexture.html).GetPixels32

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

public Color32[] GetPixels32(Color32[] colors = null);

### Parameters

colors | An optional array to write the pixel data to.  
---|---  
  
### Returns

**Color32[]** An array that contains the pixel colors.

### Description

Gets the pixel color data for a mipmap level as [Color32](Color32.html)
structs.

This method gets pixel data from the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
The array contains the pixels row by row, starting at the bottom left of the
texture. The size of the array is the width × height of the texture.  
  
Each pixel is a [Color32](Color32.html) struct.  
  
A single call to `GetPixels32` is usually faster than multiple calls to
[GetPixel](WebCamTexture.GetPixel.html), especially for large textures.  
  
If `GetPixels32` fails, Unity throws an exception. `GetPixels32` might fail if
the array contains too much data.  
  
You can optionally pass in an array of [Color32](Color32.html) structs to
avoid allocating new memory each frame. This can improve performance if you
are continuously reading data from the camera. The array must be initialized
to the dimensions `width * height` of the texture. If you don't pass an array,
Unity will allocate one and return it.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [WebCamTexture](WebCamTexture.html) webcamTexture;
        [Color32](Color32.html)[] data;  
      
        void Start()
        {
            // Start web cam feed
            webcamTexture = new [WebCamTexture](WebCamTexture.html)();
            webcamTexture.Play();
            data = new [Color32](Color32.html)[webcamTexture.width * webcamTexture.height];
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            webcamTexture.GetPixels32(data);
            // Do processing of data here.
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

