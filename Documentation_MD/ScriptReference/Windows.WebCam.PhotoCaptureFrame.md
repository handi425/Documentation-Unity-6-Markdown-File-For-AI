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

# PhotoCaptureFrame

class in UnityEngine.Windows.WebCam

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Contains information captured from the web camera.

Information captured can include the image has well as spatial data.

### Properties

[dataLength](Windows.WebCam.PhotoCaptureFrame-dataLength.html)| The length of
the raw IMFMediaBuffer which contains the image captured.  
---|---  
[hasLocationData](Windows.WebCam.PhotoCaptureFrame-hasLocationData.html)|
Specifies whether or not spatial data was captured.  
[pixelFormat](Windows.WebCam.PhotoCaptureFrame-pixelFormat.html)| The raw
image data pixel format.  
  
### Public Methods

[CopyRawImageDataIntoBuffer](Windows.WebCam.PhotoCaptureFrame.CopyRawImageDataIntoBuffer.html)|
Will copy the raw IMFMediaBuffer image data into a byte list.  
---|---  
[Dispose](Windows.WebCam.PhotoCaptureFrame.Dispose.html)| Disposes the
PhotoCaptureFrame and any resources it uses.  
[GetUnsafePointerToBuffer](Windows.WebCam.PhotoCaptureFrame.GetUnsafePointerToBuffer.html)|
Provides a COM pointer to the native IMFMediaBuffer that contains the image
data.  
[TryGetCameraToWorldMatrix](Windows.WebCam.PhotoCaptureFrame.TryGetCameraToWorldMatrix.html)|
This method will return the camera to world matrix at the time the photo was
captured if location data if available.  
[TryGetProjectionMatrix](Windows.WebCam.PhotoCaptureFrame.TryGetProjectionMatrix.html)|
This method will return the projection matrix at the time the photo was
captured if location data if available.  
[UploadImageDataToTexture](Windows.WebCam.PhotoCaptureFrame.UploadImageDataToTexture.html)|
This method will copy the captured image data into a user supplied texture for
use in Unity.  
  
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

