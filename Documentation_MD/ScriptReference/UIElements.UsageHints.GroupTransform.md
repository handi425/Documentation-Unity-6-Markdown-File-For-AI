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

#  [UsageHints](UIElements.UsageHints.html).GroupTransform

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
changes its transformation and position frequently, and has many descendants
that have their hints set to DynamicTransform.

This option is similar to DynamicTransform in that it allows GPU
transformation of the vertices of the descendants. However it breaks the
batch, and adds an extra draw call. The purpose of this hint is to avoid
having to update the stored matrix of many elements that have DynamicTransform
set when a common ancestor changes its transformation or position. In other
words, this is an optimisation for DynamicTransform.  
  
An example use case is that in Shader Graph, you can set individual nodes with
DynamicTransform, and set the ancestor panner/zoomer with `GroupTransform`, so
that when you pan/zoom, you avoid the need to update hundreds of dynamic
transforms.  
  
**Note** : Don't use both DynamicTransform and GroupTransform at the same time
on a single VisualElement.

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

