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

#  [ImageConversion](ImageConversion.html).EncodeToPNG

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

public static byte[] EncodeToPNG([Texture2D](Texture2D.html) tex);

### Parameters

tex | The texture to convert.  
---|---  
  
### Description

Encodes this texture into PNG format.

This function returns a byte array which is the PNG file data. You can store
the encoded data as a file or send it over the network without further
processing.  
  
This function does not work on any compressed format.
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
The encoded PNG data will be either 8bit grayscale, RGB or RGBA (depending on
the passed in format). For single-channel red textures ( `R8`, `R16`, `RFloat`
and `RHalf` ), the encoded PNG data will be in grayscale. PNG data will not
contain gamma correction or color profile information.

    
    
    // Saves screenshot as PNG file.
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;
    using System.IO;  
      
    public class PNGUploader : [MonoBehaviour](MonoBehaviour.html)
    {
        // Take a shot immediately
        IEnumerator Start()
        {
            yield return UploadPNG();
        }  
      
        IEnumerator UploadPNG()
        {
            // We should only read the screen buffer after rendering is complete
            yield return new [WaitForEndOfFrame](WaitForEndOfFrame.html)();  
      
            // Create a texture the size of the screen, RGB24 format
            int width = [Screen.width](Screen-width.html);
            int height = [Screen.height](Screen-height.html);
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)(width, height, [TextureFormat.RGB24](TextureFormat.RGB24.html), false);  
      
            // Read screen contents into the texture
            tex.ReadPixels(new [Rect](Rect.html)(0, 0, width, height), 0, 0);
            tex.Apply();  
      
            // Encode texture into PNG
            byte[] bytes = [ImageConversion.EncodeToPNG](ImageConversion.EncodeToPNG.html)(tex);
            [Object.Destroy](Object.Destroy.html)(tex);  
      
            // For testing purposes, also write to a file in the project folder
            // [File.WriteAllBytes](Windows.File.WriteAllBytes.html)([Application.dataPath](Application-dataPath.html) + "/../SavedScreen.png", bytes);  
      
    
            // Create a Web Form
            [WWWForm](WWWForm.html) form = new [WWWForm](WWWForm.html)();
            form.AddField("frameCount", Time.frameCount.ToString());
            form.AddBinaryData("fileUpload", bytes);  
      
            // Upload to a cgi script
            var w = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)("http://localhost/cgi-bin/env.cgi?post", form);
            yield return w.SendWebRequest();  
      
            if (w.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
            {
                [Debug.Log](Debug.Log.html)(w.error);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("Finished Uploading Screenshot");
            }
        }
    }
    

Additional resources: [ReadPixels](Texture2D.ReadPixels.html),
[WaitForEndOfFrame](WaitForEndOfFrame.html),
[LoadImage](ImageConversion.LoadImage.html),
[EncodeArrayToPNG](ImageConversion.EncodeArrayToPNG.html),
[EncodeNativeArrayToPNG](ImageConversion.EncodeNativeArrayToPNG.html),
[EncodeToJPG](ImageConversion.EncodeToJPG.html),
[EncodeToTGA](ImageConversion.EncodeToTGA.html),
[EncodeToEXR](ImageConversion.EncodeToEXR.html).

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

