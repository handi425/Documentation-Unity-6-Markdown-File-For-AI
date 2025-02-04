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

#  [Matrix4x4](Matrix4x4.html).Frustum

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

public static [Matrix4x4](Matrix4x4.html) Frustum(float left, float right,
float bottom, float top, float zNear, float zFar);

## Declaration

public static [Matrix4x4](Matrix4x4.html)
Frustum([FrustumPlanes](FrustumPlanes.html) fp);

### Parameters

left | The X coordinate of the left side of the near projection plane in view space.  
---|---  
right | The X coordinate of the right side of the near projection plane in view space.  
bottom | The Y coordinate of the bottom side of the near projection plane in view space.  
top | The Y coordinate of the top side of the near projection plane in view space.  
zNear | Z distance to the near plane from the origin in view space.  
zFar | Z distance to the far plane from the origin in view space.  
frustumPlanes | Frustum planes struct that contains the view space coordinates of that define a viewing frustum.  
  
### Returns

**Matrix4x4** A projection matrix with a viewing frustum defined by the plane
coordinates passed in.

### Description

This function returns a projection matrix with viewing frustum that has a near
plane defined by the coordinates that were passed in.

The corners of the near plane of the viewing frustum of the projection matrix
are as follows:  
top-left : (left, top, zNear)  
top-right : (right, top, zNear)  
bottom-right : (right, bottom, zNear)  
bottom-left : (left, bottom, zNear)  
  
The returned matrix embeds a z-flip operation whose purpose is to cancel the
z-flip performed by the camera view matrix. If the view matrix is an identity
or some custom matrix that doesn't perform a z-flip, consider multiplying the
third column of the projection matrix (i.e. m02, m12, m22 and m32) by -1.  
  
See also [glFrustum](https://msdn.microsoft.com/en-
us/library/dd373537\(v=vs.85\).aspx).

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

