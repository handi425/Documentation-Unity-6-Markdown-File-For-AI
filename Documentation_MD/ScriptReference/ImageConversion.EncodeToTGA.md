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

#  [ImageConversion](ImageConversion.html).EncodeToTGA

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

public static byte[] EncodeToTGA([Texture2D](Texture2D.html) tex);

### Parameters

tex | The texture to encode.  
---|---  
  
### Description

Encodes the specified texture in TGA format.

This function returns a byte array which is the TGA file data. You can store
the encoded data as a file or send it over the network without further
processing.  
  
This function does not work on any compressed format.
[Texture.isReadable](Texture-isReadable.html) must be `true`. The encoded TGA
data will be uncompressed 8bit grayscale, RGB or RGBA (depending on the passed
in format). For single-channel red textures ( `R8`, `R16`, `RFloat` and
`RHalf` ), the encoded TGA data will be in 8-bit grayscale.

    
    
    // Saves screenshot as TGA file.
    using UnityEngine;
    using System.Collections;
    using System.IO;  
      
    public class TGAScreenSaver : [MonoBehaviour](MonoBehaviour.html)
    {
        // Take a shot immediately
        IEnumerator Start()
        {
            yield return SaveScreenTGA();
        }  
      
        IEnumerator SaveScreenTGA()
        {
            // Read the screen buffer after rendering is complete
            yield return new [WaitForEndOfFrame](WaitForEndOfFrame.html)();  
      
            // Create a texture in RGB24 format the size of the screen
            int width = [Screen.width](Screen-width.html);
            int height = [Screen.height](Screen-height.html);
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)(width, height, [TextureFormat.RGB24](TextureFormat.RGB24.html), false);  
      
            // Read the screen contents into the texture
            tex.ReadPixels(new [Rect](Rect.html)(0, 0, width, height), 0, 0);
            tex.Apply();  
      
            // Encode the texture in TGA format
            byte[] bytes = [ImageConversion.EncodeToTGA](ImageConversion.EncodeToTGA.html)(tex);
            [Object.Destroy](Object.Destroy.html)(tex);  
      
            // Write the returned byte array to a file in the project folder
            [File.WriteAllBytes](Windows.File.WriteAllBytes.html)([Application.dataPath](Application-dataPath.html) + "/../SavedScreen.tga", bytes);
        }
    }
    

Additional resources: [Texture2D.ReadPixels](Texture2D.ReadPixels.html),
[WaitForEndOfFrame](WaitForEndOfFrame.html),
[LoadImage](ImageConversion.LoadImage.html),
[EncodeArrayToTGA](ImageConversion.EncodeArrayToTGA.html),
[EncodeNativeArrayToTGA](ImageConversion.EncodeNativeArrayToTGA.html),
[EncodeToPNG](ImageConversion.EncodeToPNG.html),
[EncodeToJPG](ImageConversion.EncodeToJPG.html),
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

