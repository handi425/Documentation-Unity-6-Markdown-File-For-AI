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

# UsageHints

enumeration

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

Offers a set of options that describe the intended usage patterns of a
[VisualElement](UIElements.VisualElement.html). These options serve as
guidance for optimizations. You can set multiple usage hints on an element.
For example, if both position and color change, you can set both
DynamicTransform and DynamicColor.  
  
**Note** : Set the usage hints at edit time or before you add the
[VisualElement](UIElements.VisualElement.html) to a panel. In the case of
transition, when it starts, the system might automatically add missing
relevant usage hints to avoid regenerating geometry in every frame. However,
this causes a one-frame performance penalty because the rendering data for the
VisualElement and its descendants is regenerated.

### Properties

[None](UIElements.UsageHints.None.html)|  No particular hints applicable.  
---|---  
[DynamicTransform](UIElements.UsageHints.DynamicTransform.html)|  Optimizes
rendering of a VisualElement for frequent position and transformation changes.  
[GroupTransform](UIElements.UsageHints.GroupTransform.html)|  Optimizes
rendering of a VisualElement that changes its transformation and position
frequently, and has many descendants that have their hints set to
DynamicTransform.  
[MaskContainer](UIElements.UsageHints.MaskContainer.html)|  Optimizes
rendering of a VisualElement that has multiple descendants with nested masks.  
[DynamicColor](UIElements.UsageHints.DynamicColor.html)|  Optimizes rendering
of a VisualElement for frequent color changes, such as a built-in style color
being animated.  
  
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

