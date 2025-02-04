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

#  [Application](Application.html).RequestUserAuthorization

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

public static [AsyncOperation](AsyncOperation.html)
RequestUserAuthorization([UserAuthorization](UserAuthorization.html) mode);

### Description

Request authorization to use the webcam or microphone on iOS, and the webcam
only on WebGL.

`Application.RequestUserAuthorization` is called to request permission for
microphone and camera. The application shows a dialog box to the user and
waits for the operation to complete before being able to use these features.  
  
**Note:** Use
[Application.HasUserAuthorization](Application.HasUserAuthorization.html) to
query the result of the operation.

    
    
    using UnityEngine;
    using UnityEngine.iOS;
    using System.Collections;  
      
    // Show WebCams and Microphones on an iPhone/iPad.
    // Make sure NSCameraUsageDescription and NSMicrophoneUsageDescription
    // are in the Info.plist.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Start()
        {
            FindWebCams();  
      
            yield return [Application.RequestUserAuthorization](Application.RequestUserAuthorization.html)([UserAuthorization.WebCam](UserAuthorization.WebCam.html));
            if ([Application.HasUserAuthorization](Application.HasUserAuthorization.html)([UserAuthorization.WebCam](UserAuthorization.WebCam.html)))
            {
                [Debug.Log](Debug.Log.html)("webcam found");
            }
            else
            {
                [Debug.Log](Debug.Log.html)("webcam not found");
            }  
      
            FindMicrophones();  
      
            yield return [Application.RequestUserAuthorization](Application.RequestUserAuthorization.html)([UserAuthorization.Microphone](UserAuthorization.Microphone.html));
            if ([Application.HasUserAuthorization](Application.HasUserAuthorization.html)([UserAuthorization.Microphone](UserAuthorization.Microphone.html)))
            {
                [Debug.Log](Debug.Log.html)("[Microphone](Microphone.html) found");
            }
            else
            {
                [Debug.Log](Debug.Log.html)("[Microphone](Microphone.html) not found");
            }
        }  
      
        void FindWebCams()
        {
            foreach (var device in [WebCamTexture.devices](WebCamTexture-devices.html))
            {
                [Debug.Log](Debug.Log.html)("Name: " + device.name);
            }
        }  
      
        void FindMicrophones()
        {
            foreach (var device in [Microphone.devices](Microphone-devices.html))
            {
                [Debug.Log](Debug.Log.html)("Name: " + device);
            }
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

