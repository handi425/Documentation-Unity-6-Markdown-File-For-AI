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
[VisualElementExtensions](UIElements.VisualElementExtensions.html).ChangeCoordinatesTo

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
ChangeCoordinatesTo([UIElements.VisualElement](UIElements.VisualElement.html)
src, [UIElements.VisualElement](UIElements.VisualElement.html) dest,
[Vector2](Vector2.html) point);

### Parameters

src | The element to use as a reference as the source local space.  
---|---  
dest | The element to use as a reference as the destination local space.  
point | The point to transform, in the local space of the source element.  
  
### Returns

**Vector2** A point in the local space of destination element.

### Description

Transforms a point from the local space of an element to the local space of
another element.

The elements both need to be attached to a panel and must receive a valid
[VisualElement.layout](UIElements.VisualElement-layout.html). Otherwise, this
method may return invalid results.

* * *

## Declaration

public static [Rect](Rect.html)
ChangeCoordinatesTo([UIElements.VisualElement](UIElements.VisualElement.html)
src, [UIElements.VisualElement](UIElements.VisualElement.html) dest,
[Rect](Rect.html) rect);

### Parameters

src | The element to use as a reference as the source local space.  
---|---  
dest | The element to use as a reference as the destination local space.  
rect | The rectangle to transform, in the local space of the source element.  
  
### Returns

**Rect** A rectangle in the local space of destination element.

### Description

Transforms a rectangle from the local space of an element to the local space
of another element.

The elements both need to be attached to a panel and have received a valid
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

