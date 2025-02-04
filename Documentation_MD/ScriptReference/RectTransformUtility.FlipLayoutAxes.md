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

#  [RectTransformUtility](RectTransformUtility.html).FlipLayoutAxes

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

public static void FlipLayoutAxes([RectTransform](RectTransform.html) rect,
bool keepPositioning, bool recursive);

### Parameters

rect | The RectTransform to flip.  
---|---  
keepPositioning | Flips around the pivot if true. Flips within the parent rect if false.  
recursive | Flip the children as well?  
  
### Description

Flips the horizontal and vertical axes of the RectTransform size and
alignment, and optionally its children as well.

This swaps the horizontal and vertical axis in the size and alignment of the
RectTransform. This can also be thought of as a diagonal flip. Any actual
content such as images or text will not be flipped or rotated but may be
resized and aligned differently.  
  
An example usage is to instantiate a control designed for alignment along one
axis (like a horizontal slider) and flip the axes so the layout becomes
suitable for use along the other axis (like a vertical slider).  
  
When used with the recursive argument set to true, the children are always
flipped with the keepPositioning option set to false so that they properly
follow the flip of the parent.

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

