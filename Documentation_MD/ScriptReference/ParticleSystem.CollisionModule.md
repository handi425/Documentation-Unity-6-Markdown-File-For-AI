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

# CollisionModule

struct in UnityEngine

/

Implemented
in:[UnityEngine.ParticleSystemModule](UnityEngine.ParticleSystemModule.html)

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

### Description

Script interface for the CollisionModule of a Particle System.

Additional resources: [ParticleSystem](ParticleSystem.html),
[ParticleSystem.collision](ParticleSystem-collision.html).

### Properties

[bounce](ParticleSystem.CollisionModule-bounce.html)| How much force is
applied to each particle after a collision.  
---|---  
[bounceMultiplier](ParticleSystem.CollisionModule-bounceMultiplier.html)| A
multiplier for ParticleSystem.CollisionModule.bounce.  
[colliderForce](ParticleSystem.CollisionModule-colliderForce.html)| How much
force is applied to a Collider when hit by particles from this Particle
System.  
[collidesWith](ParticleSystem.CollisionModule-collidesWith.html)| Control
which Layers this Particle System collides with.  
[dampen](ParticleSystem.CollisionModule-dampen.html)| How much speed does each
particle lose after a collision.  
[dampenMultiplier](ParticleSystem.CollisionModule-dampenMultiplier.html)|
Change the dampen multiplier.  
[enabled](ParticleSystem.CollisionModule-enabled.html)| Specifies whether the
CollisionModule is enabled or disabled.  
[enableDynamicColliders](ParticleSystem.CollisionModule-
enableDynamicColliders.html)| Allow particles to collide with dynamic
colliders when using world collision mode.  
[lifetimeLoss](ParticleSystem.CollisionModule-lifetimeLoss.html)| How much a
collision reduces a particle's lifetime.  
[lifetimeLossMultiplier](ParticleSystem.CollisionModule-
lifetimeLossMultiplier.html)| Change the lifetime loss multiplier.  
[maxCollisionShapes](ParticleSystem.CollisionModule-maxCollisionShapes.html)|
The maximum number of collision shapes Unity considers for particle
collisions. It ignores excess shapes. Terrains take priority.  
[maxKillSpeed](ParticleSystem.CollisionModule-maxKillSpeed.html)| Kill
particles whose speed goes above this threshold, after a collision.  
[minKillSpeed](ParticleSystem.CollisionModule-minKillSpeed.html)| Kill
particles whose speed falls below this threshold, after a collision.  
[mode](ParticleSystem.CollisionModule-mode.html)| Choose between 2D and 3D
world collisions.  
[multiplyColliderForceByCollisionAngle](ParticleSystem.CollisionModule-
multiplyColliderForceByCollisionAngle.html)| Specifies whether the physics
system considers the collision angle when it applies forces from particles to
Colliders.  
[multiplyColliderForceByParticleSize](ParticleSystem.CollisionModule-
multiplyColliderForceByParticleSize.html)| Specifies whether the physics
system considers particle sizes when it applies forces to Colliders.  
[multiplyColliderForceByParticleSpeed](ParticleSystem.CollisionModule-
multiplyColliderForceByParticleSpeed.html)| Specifies whether the physics
system considers particle speeds when it applies forces to Colliders.  
[planeCount](ParticleSystem.CollisionModule-planeCount.html)| Shows the number
of planes currently set as Colliders.  
[quality](ParticleSystem.CollisionModule-quality.html)| Specifies the accuracy
of particle collisions against colliders in the Scene.  
[radiusScale](ParticleSystem.CollisionModule-radiusScale.html)| A multiplier
that Unity applies to the size of each particle before collisions are
processed.  
[sendCollisionMessages](ParticleSystem.CollisionModule-
sendCollisionMessages.html)| Send collision callback messages.  
[type](ParticleSystem.CollisionModule-type.html)| The type of particle
collision to perform.  
[voxelSize](ParticleSystem.CollisionModule-voxelSize.html)| Size of voxels in
the collision cache.  
  
### Public Methods

[AddPlane](ParticleSystem.CollisionModule.AddPlane.html)| Adds a collision
plane to use with this Particle System.  
---|---  
[GetPlane](ParticleSystem.CollisionModule.GetPlane.html)| Get a collision
plane associated with this Particle System.  
[RemovePlane](ParticleSystem.CollisionModule.RemovePlane.html)| Removes a
collision plane associated with this Particle System.  
[SetPlane](ParticleSystem.CollisionModule.SetPlane.html)| Set a collision
plane to use with this Particle System.  
  
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

