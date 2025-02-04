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

# WheelHit

struct in UnityEngine

/

Implemented in:[UnityEngine.VehiclesModule](UnityEngine.VehiclesModule.html)

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

Contact information for the wheel, reported by
[WheelCollider](WheelCollider.html).

Friction for the [WheelCollider](WheelCollider.html) is computed separately
from the rest of the physics, using a slip based tire friction model. This
allows for more realistic behaviour, but makes wheel colliders ignore standard
[PhysicsMaterial](PhysicsMaterial.html) settings.  
  
The way to simulate different ground materials is to query
[WheelCollider](WheelCollider.html) for its collision information (see
[WheelCollider.GetGroundHit](WheelCollider.GetGroundHit.html)). Usually, you
get the other collider the wheel is hitting, and modify the wheel's
[WheelCollider.forwardFriction](WheelCollider-forwardFriction.html) and
[WheelCollider.sidewaysFriction](WheelCollider-sidewaysFriction.html) based on
the physics material of the ground.  
  
The other members of the WheelHit structure are usually queried for
information purposes or special effects. For example, a "slipping tire" sound
can be played if [forwardSlip](WheelHit-forwardSlip.html) or
[sidewaysSlip](WheelHit-sidewaysSlip.html) exceed some threshold.  
  
Additional resources:
[WheelCollider.GetGroundHit](WheelCollider.GetGroundHit.html).

### Properties

[collider](WheelHit-collider.html)| The other Collider the wheel is hitting.  
---|---  
[force](WheelHit-force.html)| The magnitude of the force being applied for the
contact.  
[forwardDir](WheelHit-forwardDir.html)| The direction the wheel is pointing
in.  
[forwardSlip](WheelHit-forwardSlip.html)| Tire slip in the rolling direction.
Acceleration slip is negative, braking slip is positive.  
[normal](WheelHit-normal.html)| The normal at the point of contact.  
[point](WheelHit-point.html)| The point of contact between the wheel and the
ground.  
[sidewaysDir](WheelHit-sidewaysDir.html)| The sideways direction of the wheel.  
[sidewaysSlip](WheelHit-sidewaysSlip.html)| Tire slip in the sideways
direction.  
  
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

