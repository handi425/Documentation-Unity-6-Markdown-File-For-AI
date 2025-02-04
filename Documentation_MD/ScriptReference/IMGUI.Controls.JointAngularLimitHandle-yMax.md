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

#  [JointAngularLimitHandle](IMGUI.Controls.JointAngularLimitHandle.html).yMax

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

public float yMax;

### Description

Returns or specifies the maximum angular motion about the y-axis.

The value returned by this property depends on the current value of the
[yMotion](IMGUI.Controls.JointAngularLimitHandle-yMotion.html) property. If it
is [ConfigurableJointMotion.Locked](ConfigurableJointMotion.Locked.html), then
it will always return 0. If it is
[ConfigurableJointMotion.Free](ConfigurableJointMotion.Free.html), then it
will always return the upper limit of
[yRange](IMGUI.Controls.JointAngularLimitHandle-yRange.html). If it is
[ConfigurableJointMotion.Limited](ConfigurableJointMotion.Limited.html), then
it will be clamped between the upper limit of
[yRange](IMGUI.Controls.JointAngularLimitHandle-yRange.html) and the current
value of [yMin](IMGUI.Controls.JointAngularLimitHandle-yMin.html).  
  
Additional resources: [yMin](IMGUI.Controls.JointAngularLimitHandle-
yMin.html), [yMotion](IMGUI.Controls.JointAngularLimitHandle-yMotion.html),
[yRange](IMGUI.Controls.JointAngularLimitHandle-yRange.html).

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

