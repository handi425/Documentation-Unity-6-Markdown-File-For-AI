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

#
[PhotoCaptureFrame](Windows.WebCam.PhotoCaptureFrame.html).TryGetProjectionMatrix

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

public bool TryGetProjectionMatrix(float nearClipPlane, float farClipPlane,
out [Matrix4x4](Matrix4x4.html) projectionMatrix);

## Declaration

public bool TryGetProjectionMatrix(out [Matrix4x4](Matrix4x4.html)
projectionMatrix);

### Parameters

nearClipPlane | The near clip plane distance.  
---|---  
farClipPlane | The far clip plane distance.  
projectionMatrix | A matrix to be populated by the Projection Matrix.  
  
### Returns

**bool** True if a valid matrix is returned or false otherwise. This will be
false if the frame has no location data.

### Description

This method will return the projection matrix at the time the photo was
captured if location data if available.

If the near and far clip values are not specified, then the projection matrix
returned will be the raw HoloLens projection matrix. However if the near and
far clip values are provided, they will be encoded into the returned
projection matrix. The provided near and far clip values will be validated
prior to encoding them into the projection matrix. The near clip value will be
set to 0.01 if the provided value is less than 0.01. Likewise, if the far clip
value is less than the near clip value then the far clip value will be set to
the near clip value plus 0.01.  
  
If location data is unavailable then the projection matrix will be set to the
identity matrix.

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

