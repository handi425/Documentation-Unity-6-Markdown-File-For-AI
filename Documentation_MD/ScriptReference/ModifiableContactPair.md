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

# ModifiableContactPair

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

A light-weight proxy that allows to access the contact buffers directly.

### Properties

[bodyAngularVelocity](ModifiableContactPair-bodyAngularVelocity.html)| Angular
velocity of the first body in the contact pair.  
---|---  
[bodyInstanceID](ModifiableContactPair-bodyInstanceID.html)| Instance ID of
the first body in this contact pair.  
[bodyVelocity](ModifiableContactPair-bodyVelocity.html)| Linear velocity of
the first body in the contact pair.  
[colliderInstanceID](ModifiableContactPair-colliderInstanceID.html)| Instance
ID of the first Collider in this contact pair.  
[contactCount](ModifiableContactPair-contactCount.html)| The amount of the
contact points generated for this contact pair.  
[massProperties](ModifiableContactPair-massProperties.html)| Mass-related
properties of this contact pair, such as the mass ratio.  
[otherBodyAngularVelocity](ModifiableContactPair-
otherBodyAngularVelocity.html)| Angular velocity of the second body in the
contact pair.  
[otherBodyInstanceID](ModifiableContactPair-otherBodyInstanceID.html)|
Instance ID of the second body in this contact pair.  
[otherBodyVelocity](ModifiableContactPair-otherBodyVelocity.html)| Linear
velocity of the second body in the contact pair.  
[otherColliderInstanceID](ModifiableContactPair-otherColliderInstanceID.html)|
Instance ID of the second collider in this contact pair.  
[otherPosition](ModifiableContactPair-otherPosition.html)| World-space
position of the second collider in this contact pair as seen by the solver.  
[otherRotation](ModifiableContactPair-otherRotation.html)| World-space
rotation of the second collider in this contact pair as seen by the solver.  
[position](ModifiableContactPair-position.html)| World-space position of the
first collider in this contact pair as seen by the solver.  
[rotation](ModifiableContactPair-rotation.html)| World-space rotation of the
first collider in this contact pair as seen by the solver.  
  
### Public Methods

[GetBounciness](ModifiableContactPair.GetBounciness.html)| Get the restitution
value for the specified contact point in this contact pair.  
---|---  
[GetDynamicFriction](ModifiableContactPair.GetDynamicFriction.html)| Get the
value of the dynamic friction for a specified contact point in this contact
pair.  
[GetFaceIndex](ModifiableContactPair.GetFaceIndex.html)| Get the index of a
face a particular contact point belongs to in this contact pair. Use this with
Mesh.triangles.  
[GetMaxImpulse](ModifiableContactPair.GetMaxImpulse.html)| Get the maximum
impulse that the solver can apply at a particular contact point in this
contact pair.  
[GetNormal](ModifiableContactPair.GetNormal.html)| Get the normal at a
particular contact point in this contact pair.  
[GetPoint](ModifiableContactPair.GetPoint.html)| Get the location of a
particular contact point in this contact pair.  
[GetSeparation](ModifiableContactPair.GetSeparation.html)| Get the separation
value at a particular contact point in this contact pair.  
[GetStaticFriction](ModifiableContactPair.GetStaticFriction.html)| Get the
static friction coefficient at a particular point of the contact pair.  
[GetTargetVelocity](ModifiableContactPair.GetTargetVelocity.html)| Get the
target velocity the solver should aim reaching at a particular contact point
in this contact pair.  
[IgnoreContact](ModifiableContactPair.IgnoreContact.html)| Ignore the
specified contact point in this contact pair.  
[SetBounciness](ModifiableContactPair.SetBounciness.html)| Set the restitution
value for the specified contact point in this contact pair.  
[SetDynamicFriction](ModifiableContactPair.SetDynamicFriction.html)| Set the
value of the dynamic friction for a specified contact point in this contact
pair.  
[SetMaxImpulse](ModifiableContactPair.SetMaxImpulse.html)| Set the maximum
impulse that the solver can apply at a particular contact point in this
contact pair.  
[SetNormal](ModifiableContactPair.SetNormal.html)| Set the normal at a
particular contact point in this contact pair.  
[SetPoint](ModifiableContactPair.SetPoint.html)| Set the location of a
particular contact point in this contact pair.  
[SetSeparation](ModifiableContactPair.SetSeparation.html)| Set the separation
value at a particular contact point in this contact pair.  
[SetStaticFriction](ModifiableContactPair.SetStaticFriction.html)| Set the
static friction coefficient at a particular point of the contact pair.  
[SetTargetVelocity](ModifiableContactPair.SetTargetVelocity.html)| Set the
target velocity the solver should aim reaching at a particular contact point
in this contact pair.  
  
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

