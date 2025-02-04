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

#  [UsageHints](UIElements.UsageHints.html).MaskContainer

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

Optimizes rendering of a [VisualElement](UIElements.VisualElement.html) that
has multiple descendants with nested masks.

This option reduces stencil state changes and capitalizes on consecutive mask
push/pop operations for efficiency.  
  
Apply this option to a VisualElement with multiple nested masks among its
descendants. For example, a child element has the `overflow: hidden;` style
with rounded corners or SVG background.  
  
The following illustration shows the number of batches in a single-level
masking, a nested masking, and a nested masking with MaskContainer. The yellow
color indicates the masking elements. The orange color indicates the masking
element with MaskContainer applied. The numbers indicate the number of
batches.  
  
![](../StaticFiles/ScriptRefImages/MaskContainer.png)  
A: Single-level masking (1 batch)  
B: Nested masking (5 batches)  
C: Nested masking with MaskContainer (2 batches)  
  
**Note** : Don't use GroupTransform in scenarios with many subtrees, where
each subtree uses two or more levels of masking. This helps minimize
consecutive push/push or pop/pop operations.

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

