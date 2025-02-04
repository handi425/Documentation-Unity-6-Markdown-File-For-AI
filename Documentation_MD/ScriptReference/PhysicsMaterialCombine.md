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

# PhysicsMaterialCombine

enumeration

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

Describes how physics materials of the colliding objects are combined.  
  
The friction force as well as the residual bounce impulse are applied
symmetrically to both of the colliders in contact, so each pair of overlapping
colliders must have a single set of friction and bouciness settings. However,
one can set arbitrary physics materials to any colliders. For that particular
reason, there is a mechanism that allows the combination of two different sets
of properties that correspond to each of the colliders in contact into one set
to be used in the solver.  
  
Specifying Average, Maximum, Minimum or Multiply as the physics material
combine mode, you directly set the function that is used to combine the
settings corresponding to the two overlapping colliders into one set of
settings that can be used to apply the material effect.  
  
Note that there is a special case when the two overlapping colliders have
physics materials with different combine modes set. In this particular case,
the function that has the highest priority is used. The priority order is as
follows: Average < Minimum < Multiply < Maximum. For example, if one material
has Average set but the other one has Maximum, then the combine function to be
used is Maximum, since it has higher priority.

Additional resources: [PhysicsMaterial.frictionCombine](PhysicsMaterial-
frictionCombine.html), [PhysicsMaterial.bounceCombine](PhysicsMaterial-
bounceCombine.html).

### Properties

[Average](PhysicsMaterialCombine.Average.html)| Averages the friction/bounce
of the two colliding materials.  
---|---  
[Multiply](PhysicsMaterialCombine.Multiply.html)| Multiplies the
friction/bounce of the two colliding materials.  
[Minimum](PhysicsMaterialCombine.Minimum.html)| Uses the smaller
friction/bounce of the two colliding materials.  
[Maximum](PhysicsMaterialCombine.Maximum.html)| Uses the larger
friction/bounce of the two colliding materials.  
  
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

