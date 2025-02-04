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
[RectTransformUtility](RectTransformUtility.html).ScreenPointToLocalPointInRectangle

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

public static bool
ScreenPointToLocalPointInRectangle([RectTransform](RectTransform.html) rect,
[Vector2](Vector2.html) screenPoint, [Camera](Camera.html) cam, out
[Vector2](Vector2.html) localPoint);

### Parameters

rect | The RectTransform to find a point inside.  
---|---  
screenPoint | Screen space position.  
cam | The camera associated with the screen space position.  
localPoint | Point in local space of the rect transform.  
  
### Returns

**bool** Returns true if the plane of the RectTransform is hit, regardless of
whether the point is inside the rectangle.

### Description

Transform a screen space point to a position in the local space of a
RectTransform that is on the plane of its rectangle.

The cam parameter should be the camera associated with the screen point. For a
RectTransform in a Canvas set to Screen Space - Overlay mode, the cam
parameter should be null.  
  
When ScreenPointToLocalPointInRectangle is used from within an event handler
that provides a PointerEventData object, the correct camera can be obtained by
using PointerEventData.enterEventData (for hover functionality) or
PointerEventData.pressEventCamera (for click functionality). This will
automatically use the correct camera (or null) for the given event.

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

