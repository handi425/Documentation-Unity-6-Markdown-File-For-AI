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

#  [ArticulationBody](ArticulationBody.html).SetDriveTargets

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

public void SetDriveTargets(List<float> targets);

### Parameters

targets | Supplied list of floats used to set the joint drive targets.   
---|---  
  
### Description

Assigns articulation body joint drive targets for the entire hierarchy of
bodies.

This sets joint drive targets in the reduced coordinate space for the entire
articulation hierarchy starting from root using the supplied list of floats.
Every joint drive target DOF is represented by one float value, however
depending on the type of the articulation joint there might be zero, one or 3
DOFs per joint. The exact location of the data to be set in the supplied list
for the specific articulation body can be found by calling
[ArticulationBody.GetDofStartIndices](ArticulationBody.GetDofStartIndices.html)
and indexing returned dofStartIndices list by the particular body index via
[ArticulationBody.index](ArticulationBody-index.html). Number of degrees of
freedom(DOF) for the articulation body can be found using
[ArticulationBody.dofCount](ArticulationBody-dofCount.html).  
  
Units of measurement - meters for linear and radians for angular motion.  
  
Additional resources: [index](ArticulationBody-index.html),
[GetDofStartIndices](ArticulationBody.GetDofStartIndices.html),
[dofCount](ArticulationBody-dofCount.html),
[GetDriveTargets](ArticulationBody.GetDriveTargets.html).

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

