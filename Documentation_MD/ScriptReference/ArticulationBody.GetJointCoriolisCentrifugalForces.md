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

#  [ArticulationBody](ArticulationBody.html).GetJointCoriolisCentrifugalForces

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

[Switch to Manual](../Manual/class-ArticulationBody.html "Go to
ArticulationBody Component in the Manual")

## Declaration

public int GetJointCoriolisCentrifugalForces(List<float> forces);

### Parameters

forces | Supplied list of floats to store the counteracting Coriolis/centrifugal force data.  
---|---  
  
### Returns

**int** Total degrees of freedom (DoF) for the entire hierarchy of
articulation bodies.

### Description

Fills the supplied list of floats with the forces required to counteract the
Coriolis and centrifugal forces for each Articulation Body in the
articulation.

This returns the forces required to counteract the Coriolis and centrifugal
forces in the reduced coordinate space for the entire articulation hierarchy
starting from root to the supplied list of floats. Every joint drive force DOF
is represented by one float value. Depending on the type of the articulation
joint there might be zero, one or three DOFs per joint. To find the exact
location of the data in the resulting list for the specific articulation body,
call
[ArticulationBody.GetDofStartIndices](ArticulationBody.GetDofStartIndices.html)
and index the returned dofStartIndices list by the particular body index via
[ArticulationBody.index](ArticulationBody-index.html). To find the number of
DOF for the articulation body, use
[ArticulationBody.dofCount](ArticulationBody-dofCount.html).  
ArticulationDrives and potential damping terms are not considered in the
computation (for example, linear/angular damping or joint friction).  
Additional resources: [index](ArticulationBody-index.html),
[GetDofStartIndices](ArticulationBody.GetDofStartIndices.html),
[dofCount](ArticulationBody-dofCount.html),
[SetDriveTargets](ArticulationBody.SetDriveTargets.html).

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

