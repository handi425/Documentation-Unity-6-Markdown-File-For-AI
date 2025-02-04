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
[VisualElementExtensions](UIElements.VisualElementExtensions.html).WorldToLocal

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

public static [Vector2](Vector2.html)
WorldToLocal([UIElements.VisualElement](UIElements.VisualElement.html) ele,
[Vector2](Vector2.html) p);

### Parameters

ele | The element to use as a reference for the local space.  
---|---  
p | The point to transform, in world space.  
  
### Returns

**Vector2** A point in the local space of the element.

### Description

Transforms a point from the world space to the local space of the element.

This element needs to be attached to a panel and must have a valid
[VisualElement.layout](UIElements.VisualElement-layout.html). Otherwise, this
method might return invalid results.

* * *

## Declaration

public static [Rect](Rect.html)
WorldToLocal([UIElements.VisualElement](UIElements.VisualElement.html) ele,
[Rect](Rect.html) r);

### Parameters

ele | The element to use as a reference for the local space.  
---|---  
r | The rectangle to transform, in world space.  
  
### Returns

**Rect** A rectangle in the local space of the element.

### Description

Transforms a rectangle from the world space to the local space of the element.

This element needs to be attached to a panel and must receive a valid
[VisualElement.layout](UIElements.VisualElement-layout.html). Otherwise, this
method may return invalid results.

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

