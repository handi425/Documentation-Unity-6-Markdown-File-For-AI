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

# CameraEditorUtils

class in UnityEditor

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

Utilities for cameras.

### Static Properties

[GameViewAspectRatio](CameraEditorUtils.GameViewAspectRatio.html)| The aspect
ratio of the game view.  
---|---  
[virtualCameraPreviewInstantiator](CameraEditorUtils-
virtualCameraPreviewInstantiator.html)| Override this function to pass your
own Camera provider to generate previews for virtual cameras.  
  
### Static Methods

[DrawFrustumGizmo](CameraEditorUtils.DrawFrustumGizmo.html)| Draw the frustrum
gizmo of a camera.  
---|---  
[GetFrustumAspectRatio](CameraEditorUtils.GetFrustumAspectRatio.html)|
Calculate the frustrum aspect ratio of a camera.  
[GetFrustumPlaneAt](CameraEditorUtils.GetFrustumPlaneAt.html)| Calculate the
points of the frustrum plane facing the viewer at a specific distance.The
points array will be filled with the calculated points in the following order:
left bottom, left top, right top and right bottom.  
[HandleFrustum](CameraEditorUtils.HandleFrustum.html)| Draw the frustrum
handles for a camera.  
[IsViewportRectValidToRender](CameraEditorUtils.IsViewportRectValidToRender.html)|
Check whether a viewport is valid.  
[PerspectiveClipToWorld](CameraEditorUtils.PerspectiveClipToWorld.html)|
Calculate the world space position of a point in clip space.The z component
will be used to get the point at the distance z from the viewer.  
[TryGetFrustum](CameraEditorUtils.TryGetFrustum.html)| Calculate the frustrum
corners.Corners are calculated in this order: left bottom, left top, right
top, right bottom.  
[TryGetSensorGateFrustum](CameraEditorUtils.TryGetSensorGateFrustum.html)|
Calculate the frustrum corners from the sensor physical properties, without
taking gate fitting into account. To get the actual frustum with gate fit
adjustment, use CameraEditorUtils.TryGetFrustum. This method is equivalent to
CameraEditorUtils.TryGetFrustum for non-physical cameras.Corners are
calculated in this order: left bottom, left top, right top, right bottom.  
  
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

