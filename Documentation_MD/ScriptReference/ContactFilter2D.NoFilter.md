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

#  [ContactFilter2D](ContactFilter2D.html).NoFilter

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

public [ContactFilter2D](ContactFilter2D.html) NoFilter();

### Returns

**ContactFilter2D** A copy of the contact filter set to not filter any
[ContactPoint2D](ContactPoint2D.html).

### Description

Sets the contact filter to not filter any
[ContactPoint2D](ContactPoint2D.html).

When you are using a function that requires a
[ContactFilter2D](ContactFilter2D.html), but you don't want to perform any
filtering, then use this function to return a
[ContactFilter2D](ContactFilter2D.html) that turns off any filtering.  
  
Call this function to set the contact filter to
[layerMask](ContactFilter2D-layerMask.html) =
[Physics2D.AllLayers](Physics2D.AllLayers.html),
[minDepth](ContactFilter2D-minDepth.html) =
[Mathf.Infinity](Mathf.Infinity.html),
[maxDepth](ContactFilter2D-maxDepth.html) =
[Mathf.Infinity](Mathf.Infinity.html),
[minNormalAngle](ContactFilter2D-minNormalAngle.html) =
[Mathf.Infinity](Mathf.Infinity.html) and
[maxNormalAngle](ContactFilter2D-maxNormalAngle.html) =
[Mathf.Infinity](Mathf.Infinity.html).

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

