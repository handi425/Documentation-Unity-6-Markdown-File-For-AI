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

#  [ImageConversion](ImageConversion.html).EncodeNativeArrayToJPG

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

public static NativeArray<byte> EncodeNativeArrayToJPG(NativeArray<T> input,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format, uint width, uint height, uint rowBytes, int quality);

### Parameters

input | The native array to convert.  
---|---  
format | The pixel format of the image data.  
width | The width of the image data in pixels.  
height | The height of the image data in pixels.  
rowBytes | The length of a single row in bytes. The default is 0, which means Unity calculates the length automatically.  
quality | JPG quality to encode with. The range is 1 through 100. 1 is the lowest quality. The default is 75.  
  
### Description

Encodes this native array into JPG format.

This function returns a NativeArray<byte> which is the JPG data. You can store
the encoded data as a file or send it over the network without further
processing.  
  
This function does not work on any compressed format. The encoded JPG data
will be either 8bit grayscale, RGB or RGBA (depending on the passed in
format).  
  
The native array that this function returns is allocated with the persistent
allocator, so this function should only be called from the main thread.

    
    
    // Saves screenshot as JPG file.
    using System.Collections;
    using System.IO;
    using Unity.Collections;
    using UnityEngine;  
      
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
      
            // Encode the bytes in JPG format
            NativeArray<byte> imageBytes = new NativeArray<byte>(tex.GetRawTextureData(), [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var bytes = [ImageConversion.EncodeNativeArrayToJPG](ImageConversion.EncodeNativeArrayToJPG.html)(imageBytes, tex.graphicsFormat, (uint)width, (uint)height);
            [Object.Destroy](Object.Destroy.html)(tex);  
      
            // Write the returned byte array to a file in the project folder
            [File.WriteAllBytes](Windows.File.WriteAllBytes.html)([Application.dataPath](Application-dataPath.html) + "/../SavedScreen.jpg", bytes.ToArray());
        }
    }
    

Additional resources: [EncodeToJPG](ImageConversion.EncodeToJPG.html),
[EncodeArrayToJPG](ImageConversion.EncodeArrayToJPG.html),
[EncodeNativeArrayToPNG](ImageConversion.EncodeNativeArrayToPNG.html),
[EncodeNativeArrayToTGA](ImageConversion.EncodeNativeArrayToTGA.html),
[EncodeNativeArrayToEXR](ImageConversion.EncodeNativeArrayToEXR.html).

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

