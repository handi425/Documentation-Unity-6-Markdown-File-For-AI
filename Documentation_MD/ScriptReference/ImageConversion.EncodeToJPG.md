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

#  [ImageConversion](ImageConversion.html).EncodeToJPG

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

public static byte[] EncodeToJPG([Texture2D](Texture2D.html) tex, int
quality);

## Declaration

public static byte[] EncodeToJPG([Texture2D](Texture2D.html) tex);

### Parameters

tex | Text texture to convert.  
---|---  
quality | JPG quality to encode with. The range is 1 through 100. 1 is the lowest quality. The default is 75.  
  
### Description

Encodes this texture into JPG format.

This function returns a byte array which is the JPG file data. You can store
the encoded data as a file or send it over the network without further
processing.  
  
This function does not work on any compressed format.
[Texture.isReadable](Texture-isReadable.html) must be `true`. The encoded JPG
data will be either 8bit grayscale, RGB or RGBA (depending on the passed in
format).

    
    
    // Saves screenshot as JPG file.
    using UnityEngine;
    using System.Collections;
    using System.IO;  
      
    public class JPGScreenSaver : [MonoBehaviour](MonoBehaviour.html)
    {
        // Take a shot immediately
        IEnumerator Start()
        {
            yield return SaveScreenJPG();
        }  
      
        IEnumerator SaveScreenJPG()
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
      
            // Encode the texture in JPG format
            byte[] bytes = [ImageConversion.EncodeToJPG](ImageConversion.EncodeToJPG.html)(tex);
            [Object.Destroy](Object.Destroy.html)(tex);  
      
            // Write the returned byte array to a file in the project folder
            [File.WriteAllBytes](Windows.File.WriteAllBytes.html)([Application.dataPath](Application-dataPath.html) + "/../SavedScreen.jpg", bytes);
        }
    }
    

Additional resources:
[EncodeArrayToJPG](ImageConversion.EncodeArrayToJPG.html),
[EncodeNativeArrayToJPG](ImageConversion.EncodeNativeArrayToJPG.html),
[EncodeToPNG](ImageConversion.EncodeToPNG.html),
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

