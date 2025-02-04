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

#  [Physics2D](Physics2D.html).useSubStepContacts

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

public static bool useSubStepContacts;

### Description

Whether to calculate contacts for all simulation sub-steps or only the first
sub-step.

When simulation sub-stepping is enabled with
[Physics2D.useSubStepping](Physics2D-useSubStepping.html), this property is
used to control the whether or not contacts are calculated for all sub-steps
or only the first sub-step.  
  
When enabled, contacts are calculated for all sub-steps. This provides a more
accurate simulation for each sub-step but will reduce performance. In most
cases, this extra contact calculation isn't required.  
  
When disabled, contacts are only calculated for the first sub-step. Subsequent
sub-steps only perform integration and constraint solving. This increases
performance whilst still maintaining a stable simulation. In most cases, this
should be used.  
  
Additional resources:
[Physics2D.useSubStepping](Physics2D-useSubStepping.html),
[Physics2D.minSubStepFPS](Physics2D-minSubStepFPS.html),
[Physics2D.maxSubStepCount](Physics2D-maxSubStepCount.html),
[PhysicsScene2D.subStepCount](PhysicsScene2D-subStepCount.html) and
[PhysicsScene2D.subStepLostTime](PhysicsScene2D-subStepLostTime.html).

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

