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

#  [ImageConversion](ImageConversion.html).EncodeToEXR

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

public static byte[] EncodeToEXR([Texture2D](Texture2D.html) tex,
[Texture2D.EXRFlags](Texture2D.EXRFlags.html) flags);

### Parameters

tex | The texture to convert.  
---|---  
flags | Flags used to control compression and the output format. The default is [Texture2D.EXRFlags.None](Texture2D.EXRFlags.None.html)  
  
### Description

Encodes this texture into the EXR format.

This function returns a byte array which is the EXR file data. You can store
the encoded data as a file or send it over the network without further
processing.  
  
This function does not work on any compressed format. Although it is best to
use this function for HDR texture formats (either 16-bit or 32-bit floats), it
can be used with other formats (and the data is converted on the fly). The
default output format is uncompressed 16-bit float EXR and can be controlled
using the passed in flags. For the texture pass in,
[Texture.isReadable](Texture-isReadable.html) must be `true`. The encoded EXR
data will only contain an alpha channel when the passed-in format has one. For
single-channel red textures ( `R8`, `R16`, `RFloat` and `RHalf` ), the encoded
data will be in grayscale mode.  
  
Additional resources: [EXRFlags](Texture2D.EXRFlags.html),
[EncodeToJPG](ImageConversion.EncodeToJPG.html),
[EncodeToPNG](ImageConversion.EncodeToPNG.html).

    
    
    // Saves HDR [RenderTexture](RenderTexture.html) as an EXR file.
    using UnityEngine;
    using System.Collections;
    using System.IO;  
      
    public class SaveRenderTextureToEXR : [MonoBehaviour](MonoBehaviour.html)
    {
        [RenderTexture](RenderTexture.html) m_InputTexture;  
      
        void SaveRenderTexture()
        {
            if (m_InputTexture != null)
            {
                int width = m_InputTexture.width;
                int height = m_InputTexture.height;  
      
                [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)(width, height, [TextureFormat.RGBAFloat](TextureFormat.RGBAFloat.html), false);  
      
                // Read screen contents into the texture
                [Graphics.SetRenderTarget](Graphics.SetRenderTarget.html)(m_InputTexture);
                tex.ReadPixels(new [Rect](Rect.html)(0, 0, width, height), 0, 0);
                tex.Apply();  
      
                // Encode texture into the EXR
                byte[] bytes = [ImageConversion.EncodeToEXR](ImageConversion.EncodeToEXR.html)(tex, [Texture2D.EXRFlags.CompressZIP](Texture2D.EXRFlags.CompressZIP.html));
                [File.WriteAllBytes](Windows.File.WriteAllBytes.html)([Application.dataPath](Application-dataPath.html) + "/../SavedRenderTexture.exr", bytes);  
      
                [Object.DestroyImmediate](Object.DestroyImmediate.html)(tex);
            }
        }
    }
    

Additional resources:
[EncodeArrayToEXR](ImageConversion.EncodeArrayToEXR.html),
[EncodeNativeArrayToEXR](ImageConversion.EncodeNativeArrayToEXR.html),
[EncodeToPNG](ImageConversion.EncodeToPNG.html),
[EncodeToJPG](ImageConversion.EncodeToJPG.html),
[EncodeToTGA](ImageConversion.EncodeToTGA.html).

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

