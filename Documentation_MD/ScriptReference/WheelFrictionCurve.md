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

# WheelFrictionCurve

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

WheelFrictionCurve is used by the [WheelCollider](WheelCollider.html) to
describe friction properties of the wheel tire.

The curve takes a measure of tire slip as an input and gives a force as
output. The curve is approximated by a two-piece spline. The first section
goes from _(0,0)_ to _(extremumSlip,extremumValue)_ , at which point the
curve's tangent is zero. The second section goes from
_(extremumSlip,extremumValue)_ to _(asymptoteSlip,asymptoteValue)_ , where
curve's tangent is again zero:  
  
![](../StaticFiles/ScriptRefImages/WheelFrictionCurve.png)  
  
Wheel collider computes friction separately from the rest of physics engine,
using a slip based friction model. It separates the overall friction force
into a "forwards" component (in the direction of rolling, and responsible for
acceleration and braking) and "sideways" component (orthogonal to rolling,
responsible for keeping the car oriented). Tire friction is described
separately in these directions using
[WheelCollider.forwardFriction](WheelCollider-forwardFriction.html) and
[WheelCollider.sidewaysFriction](WheelCollider-sidewaysFriction.html). In both
directions it is first determined how much the tire is slipping (what is the
speed difference between the rubber and the road). Then this slip value is
used to find out tire force exerted on the contact.  
  
The property of real tires is that for low slip they can exert high forces as
the rubber compensates for the slip by stretching. Later when the slip gets
really high, the forces are reduced as the tire starts to slide or spin. Thus
tire friction curves have a shape like in the image above.  
  
Because the friction for the tires is computed separately, the
[PhysicsMaterial](PhysicsMaterial.html) of the ground does not affect the
wheels. Simulation of different road materials is done by changing the
[WheelCollider.forwardFriction](WheelCollider-forwardFriction.html) and
[WheelCollider.sidewaysFriction](WheelCollider-sidewaysFriction.html) of the
wheel, based on what material the wheel is hitting.  
  
Additional resources: [WheelCollider](WheelCollider.html),
[WheelCollider.forwardFriction](WheelCollider-forwardFriction.html),
[WheelCollider.sidewaysFriction](WheelCollider-sidewaysFriction.html).

### Properties

[asymptoteSlip](WheelFrictionCurve-asymptoteSlip.html)| Asymptote point slip
(default 2).  
---|---  
[asymptoteValue](WheelFrictionCurve-asymptoteValue.html)| Force at the
asymptote slip (default 10000).  
[extremumSlip](WheelFrictionCurve-extremumSlip.html)| Extremum point slip
(default 1).  
[extremumValue](WheelFrictionCurve-extremumValue.html)| Force at the extremum
slip (default 20000).  
[stiffness](WheelFrictionCurve-stiffness.html)| Multiplier for the
extremumValue and asymptoteValue values (default 1).  
  
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

