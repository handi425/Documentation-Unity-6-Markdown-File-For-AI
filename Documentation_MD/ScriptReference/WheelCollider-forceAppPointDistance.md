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

#  [WheelCollider](WheelCollider.html).forceAppPointDistance

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

public float forceAppPointDistance;

### Description

Application point of the suspension and tire forces measured from the base of
the resting wheel.

This is specified as a distance along the local up vector of the vehicle's
rigid body from the base of the wheel at its rest coordinate (the rest
coordinate of the wheel is determined by the value
WheelCollider.spring.targetPosition). This parameter simulates the effective
roll center of the suspension geometry. For a standard family car the value of
forceAppPointDistance should be tuned to place the application point
approximately 0.3m below the rigid body center of mass. Moving the application
point downwards introduces more roll when cornering, while moving it upwards
results in less roll when cornering. The force application point is typically
below the rigid body center of mass.  
  
Please note that having this parameter equal to zero could be undesirable as
it contributes to simulation instability in certain configurations. Once you
observe your vehicle failing to go asleep resting on flat surface, exhibiting
jittering behavior or drifting along the surface when no user input is
applied, check the forceAppPointDistance values. In the editor, when a
WheelCollider game object is selected, there is a green spherical gizmo
displayed to show where the force application point is at the moment. Try
increasing forceAppPointDistance value gradually, until you're satisfied with
the result.

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

