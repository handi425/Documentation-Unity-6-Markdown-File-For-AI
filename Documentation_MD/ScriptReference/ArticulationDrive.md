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

# ArticulationDrive

struct in UnityEngine

/

Implemented in:[UnityEngine.PhysicsModule](UnityEngine.PhysicsModule.html)

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

Drive applies forces and torques to the connected bodies.

Drive moves the body along one degree of freedom, be it a linear motion along
a particular axis or a rotational motion around a particular axis. The drive
will apply force to the body that is calculated from the current value of the
drive, using this formula: F = stiffness * (currentPosition - target) -
damping * (currentVelocity - targetVelocity). In this formula, currentPosition
and currentVelocity are linear position and linear velocity in case of the
linear drive. In case of the rotational drive, currentPosition and
currentVelocity correspond to the angle and angular velocity respectively.

### Properties

[damping](ArticulationDrive-damping.html)| The damping of the spring attached
to this drive.  
---|---  
[driveType](ArticulationDrive-driveType.html)| Specifies which drive type to
use for this drive.  
[forceLimit](ArticulationDrive-forceLimit.html)| The maximum force this drive
can apply to a body.  
[lowerLimit](ArticulationDrive-lowerLimit.html)| The lower limit of motion for
a particular degree of freedom.  
[stiffness](ArticulationDrive-stiffness.html)| The stiffness of the spring
connected to this drive.  
[target](ArticulationDrive-target.html)| The target value the drive will try
to reach.  
[targetVelocity](ArticulationDrive-targetVelocity.html)| The velocity of the
body this drive will try to reach.  
[upperLimit](ArticulationDrive-upperLimit.html)| The upper limit of motion for
a particular degree of freedom.  
  
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

