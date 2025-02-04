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

#  [Joint2D](Joint2D.html).breakForce

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

public float breakForce;

### Description

The force that needs to be applied for this joint to break.

When a joint tries to constrain a [Rigidbody2D](Rigidbody2D.html) it may need
to apply a force to do so. This is known as the
[reactionForce](Joint2D-reactionForce.html). Each physics update, the
[breakForce](Joint2D-breakForce.html) is compared to the size of the
[reactionForce](Joint2D-reactionForce.html); if it exceeds it then
[Joint2D.OnJointBreak2D](Joint2D.OnJointBreak2D.html) is called with a
reference to the joint that broke. Knowing the joint that broke, you can check
the actual reaction force that broke the joint using
[reactionForce](Joint2D-reactionForce.html) or
[Joint2D.GetReactionForce](Joint2D.GetReactionForce.html).  
  
The break force can be set to [Mathf.Infinity](Mathf.Infinity.html) to make
the joint unbreakable by any amount of reaction force. Alternately, setting
the [breakAction](Joint2D-breakAction.html) to
[JointBreakAction2D.Ignore](JointBreakAction2D.Ignore.html) will make the
joint unbreakable by either [breakForce](Joint2D-breakForce.html) or
[breakTorque](Joint2D-breakTorque.html).  
  
The action taken when a joint exceeds the breakForce is controlled by
[breakAction](Joint2D-breakAction.html).  
  
Additional resources: [Joint2D.reactionForce](Joint2D-reactionForce.html),
[Joint2D.GetReactionForce](Joint2D.GetReactionForce.html) &
[Joint2D.OnJointBreak2D](Joint2D.OnJointBreak2D.html).

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

