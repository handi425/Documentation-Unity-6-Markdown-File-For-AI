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

# Physics2D

class in UnityEngine

/

Implemented in:[UnityEngine.Physics2DModule](UnityEngine.Physics2DModule.html)

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

Global settings and helpers for 2D physics.

### Static Properties

[AllLayers](Physics2D.AllLayers.html)| Layer mask constant that includes all
layers.  
---|---  
[angularSleepTolerance](Physics2D-angularSleepTolerance.html)| A Rigidbody
cannot sleep if its angular velocity is above this tolerance threshold.  
[autoSyncTransforms](Physics2D-autoSyncTransforms.html)| Set whether to
automatically sync changes to the Transform component with the physics engine.  
[baumgarteScale](Physics2D-baumgarteScale.html)| The scale factor that
controls how fast overlaps are resolved.  
[baumgarteTOIScale](Physics2D-baumgarteTOIScale.html)| The scale factor that
controls how fast TOI overlaps are resolved.  
[bounceThreshold](Physics2D-bounceThreshold.html)| Any collisions with a
relative linear velocity below this threshold will be treated as inelastic so
no bounce will occur.  
[callbacksOnDisable](Physics2D-callbacksOnDisable.html)| Use this to control
whether or not the appropriate OnCollisionExit2D or OnTriggerExit2D callbacks
should be called when a Collider2D is disabled.  
[contactThreshold](Physics2D-contactThreshold.html)| A threshold below which a
contact is automatically disabled.  
[defaultContactOffset](Physics2D-defaultContactOffset.html)| The default
contact offset of the newly created Colliders.  
[defaultPhysicsScene](Physics2D-defaultPhysicsScene.html)| The PhysicsScene2D
automatically created when Unity starts.  
[DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html)| Layer mask
constant that includes all layers participating in raycasts by default.  
[gravity](Physics2D-gravity.html)| Acceleration due to gravity.  
[IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html)| Layer mask constant
for the default layer that ignores raycasts.  
[jobOptions](Physics2D-jobOptions.html)| A set of options that control how
physics operates when using the job system to multithread the physics
simulation.  
[linearSleepTolerance](Physics2D-linearSleepTolerance.html)| A rigid-body
cannot sleep if its linear velocity is above this tolerance.  
[maxAngularCorrection](Physics2D-maxAngularCorrection.html)| The maximum
angular position correction used when solving constraints. This helps to
prevent overshoot.  
[maxLinearCorrection](Physics2D-maxLinearCorrection.html)| The maximum linear
position correction used when solving constraints. This helps to prevent
overshoot.  
[MaxPolygonShapeVertices](Physics2D.MaxPolygonShapeVertices.html)| The maximum
number of vertices allowed per primitive polygon shape type
(PhysicsShapeType2D.Polygon). (Read Only)  
[maxRotationSpeed](Physics2D-maxRotationSpeed.html)| The maximum angular speed
of a rigid-body per physics update. Increasing this can cause numerical
problems.  
[maxSubStepCount](Physics2D-maxSubStepCount.html)| The maximum number of
simulation sub-steps allowed per-frame when simulation sub-stepping is
enabled.  
[maxTranslationSpeed](Physics2D-maxTranslationSpeed.html)| The maximum linear
speed of a rigid-body per physics update. Increasing this can cause numerical
problems.  
[minSubStepFPS](Physics2D-minSubStepFPS.html)| The minimum FPS allowed for a
simulation step before sub-stepping will be used.  
[positionIterations](Physics2D-positionIterations.html)| The number of
iterations of the physics solver when considering objects' positions.  
[queriesHitTriggers](Physics2D-queriesHitTriggers.html)| Do raycasts detect
Colliders configured as triggers?  
[queriesStartInColliders](Physics2D-queriesStartInColliders.html)| Set the
raycasts or linecasts that start inside Colliders to detect or not detect
those Colliders.  
[reuseCollisionCallbacks](Physics2D-reuseCollisionCallbacks.html)| Determines
whether the garbage collector should reuse only a single instance of a
Collision2D type for all collision callbacks.  
[simulationLayers](Physics2D-simulationLayers.html)| The Rigidbody2D and
Collider2D layers to simulate.  
[simulationMode](Physics2D-simulationMode.html)| Controls when Unity executes
the 2D physics simulation.  
[timeToSleep](Physics2D-timeToSleep.html)| The time in seconds that a rigid-
body must be still before it will go to sleep.  
[useSubStepContacts](Physics2D-useSubStepContacts.html)| Whether to calculate
contacts for all simulation sub-steps or only the first sub-step.  
[useSubStepping](Physics2D-useSubStepping.html)| Whether to use simulation
sub-stepping during a simulation step.  
[velocityIterations](Physics2D-velocityIterations.html)| The number of
iterations of the physics solver when considering objects' velocities.  
  
### Static Methods

[BoxCast](Physics2D.BoxCast.html)| Casts a box against Colliders in the Scene,
returning the first Collider to contact with it.  
---|---  
[BoxCastAll](Physics2D.BoxCastAll.html)| Casts a box against Colliders in the
Scene, returning all Colliders that contact with it.  
[CapsuleCast](Physics2D.CapsuleCast.html)| Casts a capsule against Colliders
in the Scene, returning the first Collider to contact with it.  
[CapsuleCastAll](Physics2D.CapsuleCastAll.html)| Casts a capsule against
Colliders in the Scene, returning all Colliders that contact with it.  
[CircleCast](Physics2D.CircleCast.html)| Casts a circle against Colliders in
the Scene, returning the first Collider to contact with it.  
[CircleCastAll](Physics2D.CircleCastAll.html)| Casts a circle against
Colliders in the Scene, returning all Colliders that contact with it.  
[ClosestPoint](Physics2D.ClosestPoint.html)| Returns a point on the perimeter
of the Collider that is closest to the specified position.  
[Distance](Physics2D.Distance.html)| Calculates the minimum distance between
two Colliders.  
[GetContacts](Physics2D.GetContacts.html)| Retrieves all Colliders in contact
with the Collider.  
[GetIgnoreCollision](Physics2D.GetIgnoreCollision.html)| Checks whether the
collision detection system will ignore all collisions/triggers between
collider1 and collider2 or not.  
[GetIgnoreLayerCollision](Physics2D.GetIgnoreLayerCollision.html)| Checks
whether collisions between the specified layers be ignored or not.  
[GetLayerCollisionMask](Physics2D.GetLayerCollisionMask.html)| Get the
collision layer mask that indicates which layer(s) the specified layer can
collide with.  
[GetRayIntersection](Physics2D.GetRayIntersection.html)| Cast a 3D ray against
the 2D Colliders in the Scene.  
[GetRayIntersectionAll](Physics2D.GetRayIntersectionAll.html)| Cast a 3D ray
against the 2D Colliders in the Scene.  
[GetRayIntersectionNonAlloc](Physics2D.GetRayIntersectionNonAlloc.html)| Cast
a 3D ray against the 2D Colliders in the Scene.  
[IgnoreCollision](Physics2D.IgnoreCollision.html)| Makes the collision
detection system ignore all collisions/triggers between collider1 and
collider2.  
[IgnoreLayerCollision](Physics2D.IgnoreLayerCollision.html)| Choose whether to
detect or ignore collisions between a specified pair of layers.  
[IsTouching](Physics2D.IsTouching.html)| Checks whether the passed Colliders
are in contact or not.  
[IsTouchingLayers](Physics2D.IsTouchingLayers.html)| Checks whether the
Collider is touching any Colliders on the specified layerMask or not.  
[Linecast](Physics2D.Linecast.html)| Casts a line segment against Colliders in
the Scene.  
[LinecastAll](Physics2D.LinecastAll.html)| Casts a line against Colliders in
the Scene.  
[OverlapArea](Physics2D.OverlapArea.html)| Checks if a Collider falls within a
rectangular area.  
[OverlapAreaAll](Physics2D.OverlapAreaAll.html)| Get a list of all Colliders
that fall within a rectangular area.  
[OverlapBox](Physics2D.OverlapBox.html)| Checks if a Collider falls within a
box area.  
[OverlapBoxAll](Physics2D.OverlapBoxAll.html)| Get a list of all Colliders
that fall within a box area.  
[OverlapCapsule](Physics2D.OverlapCapsule.html)| Checks if a Collider falls
within a capsule area.  
[OverlapCapsuleAll](Physics2D.OverlapCapsuleAll.html)| Get a list of all
Colliders that fall within a capsule area.  
[OverlapCircle](Physics2D.OverlapCircle.html)| Checks if a Collider falls
within a circular area.  
[OverlapCircleAll](Physics2D.OverlapCircleAll.html)| Get a list of all
Colliders that fall within a circular area.  
[OverlapCollider](Physics2D.OverlapCollider.html)| Gets a list of all
Colliders that overlap the given Collider.  
[OverlapPoint](Physics2D.OverlapPoint.html)| Checks if a Collider overlaps a
point in space.  
[OverlapPointAll](Physics2D.OverlapPointAll.html)| Get a list of all Colliders
that overlap a point in space.  
[Raycast](Physics2D.Raycast.html)| Casts a ray against Colliders in the Scene.  
[RaycastAll](Physics2D.RaycastAll.html)| Casts a ray against Colliders in the
Scene, returning all Colliders that contact with it.  
[SetLayerCollisionMask](Physics2D.SetLayerCollisionMask.html)| Set the
collision layer mask that indicates which layer(s) the specified layer can
collide with.  
[Simulate](Physics2D.Simulate.html)| Simulate physics in the default physics
scene.  
[SyncTransforms](Physics2D.SyncTransforms.html)| Synchronizes.  
  
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

