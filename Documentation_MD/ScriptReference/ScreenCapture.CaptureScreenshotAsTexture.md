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

#  [ScreenCapture](ScreenCapture.html).CaptureScreenshotAsTexture

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

public static [Texture2D](Texture2D.html) CaptureScreenshotAsTexture(int
superSize);

## Declaration

public static [Texture2D](Texture2D.html)
CaptureScreenshotAsTexture([ScreenCapture.StereoScreenCaptureMode](ScreenCapture.StereoScreenCaptureMode.html)
stereoCaptureMode);

### Parameters

superSize | Factor by which to increase resolution.  
---|---  
stereoCaptureMode | Specifies the eye texture to capture when stereo rendering is enabled.  
  
### Description

Captures a screenshot of the game view into a Texture2D object.

When `superSize` parameter is larger than 1, a larger resolution screenshot
will be produced. For example, passing 4 will make the screenshot be 4x4
larger than it normally would. This is useful to produce screenshots for
printing.  
  
To get a reliable output from this method you must make sure it is called once
the frame rendering has ended, and not during the rendering process. A simple
way of ensuring this is to call it from a coroutine that yields on
WaitForEndOfFrame. If you call this method during the rendering process you
will get unpredictable and undefined results.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ScreenShotter : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator RecordFrame()
        {
            yield return new [WaitForEndOfFrame](WaitForEndOfFrame.html)();
            var texture = [ScreenCapture.CaptureScreenshotAsTexture](ScreenCapture.CaptureScreenshotAsTexture.html)();
            // do something with texture  
      
            // cleanup
            [Object.Destroy](Object.Destroy.html)(texture);
        }  
      
        public void LateUpdate()
        {
            StartCoroutine(RecordFrame());
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

