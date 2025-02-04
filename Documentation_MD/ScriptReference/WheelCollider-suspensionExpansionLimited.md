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

#  [WheelCollider](WheelCollider.html).suspensionExpansionLimited(bool)

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

[Switch to Manual](../Manual/class-WheelCollider.html "Go to WheelCollider
Component in the Manual")

### Parameters

active | Turns on/off the property  
---|---  
  
### Description

Limits the expansion velocity of the Wheel Collider's suspension. If you set
this property on a Rigidbody that has several Wheel Colliders, such as a
vehicle, then it affects all other Wheel Colliders on the Rigidbody.

If you use a Wheel Collider that has extreme values for Suspension Spring
properties, such as [suspensionSpring.damper](JointSpring-spring.html) or
[suspensionSpring.spring](JointSpring-spring.html), the large damping forces
might make the vehicle stick to the ground, instead of lifting off. While it's
best practice to use realistic damping ratios, you can use this property to
limit the velocity of suspension.  
  
In more detail, the simulation checks whether the suspension can extend to the
target length in the given simulation time step. If it can, Unity computes the
suspension force as usual, otherwise it sets the force to zero. If you use
this feature, it results in a slightly more realistic behavior at the
potential cost of losing control when steering the vehicle.

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

