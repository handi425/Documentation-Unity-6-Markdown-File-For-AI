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

#  [BuoyancyEffector2D](BuoyancyEffector2D.html).flowMagnitude

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

public float flowMagnitude;

### Description

The magnitude of the force used to similate fluid flow.

Fluid flow can be defined to move in any direction with a specific magnitude
and a random variation on that magnitude.  
  
This property defines the size of the force to be applied in the direction
defined by [flowAngle](BuoyancyEffector2D-flowAngle.html). This magnitude can
be randomly varied by using
[flowVariation](BuoyancyEffector2D-flowVariation.html).  
  
The flow forces are applied to the center of any submerged region of a
[Collider2D](Collider2D.html) so it will not produce any torque (rotation) if
the [Collider2D](Collider2D.html) is fully submerged (fully below the
[surfaceLevel](BuoyancyEffector2D-surfaceLevel.html)) but will produce torque
if the [Collider2D](Collider2D.html) is partially submerged (overlapping the
[surfaceLevel](BuoyancyEffector2D-surfaceLevel.html)).  
  
Additional resources: [flowAngle](BuoyancyEffector2D-flowAngle.html),
[flowVariation](BuoyancyEffector2D-flowVariation.html).

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

