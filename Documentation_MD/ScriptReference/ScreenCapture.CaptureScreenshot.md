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

#  [ScreenCapture](ScreenCapture.html).CaptureScreenshot

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

public static void CaptureScreenshot(string filename, int superSize);

## Declaration

public static void CaptureScreenshot(string filename,
[ScreenCapture.StereoScreenCaptureMode](ScreenCapture.StereoScreenCaptureMode.html)
stereoCaptureMode);

### Parameters

filename | The path to save the screenshot file to.  
---|---  
superSize | The factor to increase resolution with.  
stereoCaptureMode | The eye texture to capture when stereo rendering is enabled.  
  
### Description

Captures a screenshot and saves it as a .png file to a specified path.

If the screenshot exists already, `ScreenCapture.CaptureScreenshot` overwrites
it with a new screenshot.  
  
Add `.png` to the end of `filename` to save the screenshot as a .png file.  
  
On mobile platforms, `filename` is appended to the persistent data path. Refer
to [Application.persistentDataPath](Application-persistentDataPath.html) for
more information on persistent data paths.  
  
On platforms that aren't mobile, `filename` is a file path relative to the
executable directory. In the Editor, `filename` is a filepath relative to the
project directory.  
  
When the `superSize` parameter is more than 1, a larger resolution screenshot
is produced. For example, if you pass 4, you create a screenshot 4x4 larger
than normal. This is useful to produce screenshots you want to print.

    
    
    using UnityEngine;  
      
    // Generate a screenshot and save it to disk with the name SomeLevel.png.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnMouseDown()
        {
            [ScreenCapture.CaptureScreenshot](ScreenCapture.CaptureScreenshot.html)("SomeLevel.png");
        }
    }
    

The [CaptureScreenshot](ScreenCapture.CaptureScreenshot.html) returns
immediately on Android. The screen capture continues in the background. The
resulting screen shot is saved in the file system after a few seconds.

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

