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

# Physics

class in UnityEngine

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

Global physics properties and helper methods.

### Static Properties

[AllLayers](Physics.AllLayers.html)| Layer mask constant to select all layers.  
---|---  
[autoSyncTransforms](Physics-autoSyncTransforms.html)| Whether or not to
automatically sync transform changes with the physics system whenever a
Transform component changes.  
[bounceThreshold](Physics-bounceThreshold.html)| Two colliding objects with a
relative velocity below this will not bounce (default 2). Must be positive.  
[clothGravity](Physics-clothGravity.html)| Cloth Gravity setting. Set gravity
for all cloth components.  
[defaultContactOffset](Physics-defaultContactOffset.html)| The default contact
offset of the newly created colliders.  
[defaultMaxAngularSpeed](Physics-defaultMaxAngularSpeed.html)| Default maximum
angular speed of the dynamic Rigidbody, in radians (default 50).  
[defaultMaxDepenetrationVelocity](Physics-
defaultMaxDepenetrationVelocity.html)| The maximum default velocity needed to
move a Rigidbody's collider out of another collider's surface penetration.
Must be positive.  
[defaultPhysicsScene](Physics-defaultPhysicsScene.html)| The PhysicsScene
automatically created when Unity starts.  
[DefaultRaycastLayers](Physics.DefaultRaycastLayers.html)| Layer mask constant
to select default raycast layers.  
[defaultSolverIterations](Physics-defaultSolverIterations.html)| The
defaultSolverIterations determines how accurately Rigidbody joints and
collision contacts are resolved. (default 6). Must be positive.  
[defaultSolverVelocityIterations](Physics-
defaultSolverVelocityIterations.html)| The defaultSolverVelocityIterations
affects how accurately the Rigidbody joints and collision contacts are
resolved. (default 1). Must be positive.  
[gravity](Physics-gravity.html)| The gravity applied to all rigid bodies in
the Scene.  
[IgnoreRaycastLayer](Physics.IgnoreRaycastLayer.html)| Layer mask constant to
select ignore raycast layer.  
[improvedPatchFriction](Physics-improvedPatchFriction.html)| Enables an
improved patch friction mode that guarantees static and dynamic friction do
not exceed analytical results.  
[interCollisionDistance](Physics-interCollisionDistance.html)| Sets the
minimum separation distance for cloth inter-collision.  
[interCollisionStiffness](Physics-interCollisionStiffness.html)| Sets the
cloth inter-collision stiffness.  
[invokeCollisionCallbacks](Physics-invokeCollisionCallbacks.html)| Whether or
not MonoBehaviour collision messages will be sent by the physics system.  
[queriesHitBackfaces](Physics-queriesHitBackfaces.html)| Whether physics
queries should hit back-face triangles.  
[queriesHitTriggers](Physics-queriesHitTriggers.html)| Specifies whether
queries (raycasts, spherecasts, overlap tests, etc.) hit Triggers by default.  
[reuseCollisionCallbacks](Physics-reuseCollisionCallbacks.html)| Determines
whether the garbage collector should reuse only a single instance of a
Collision type for all collision callbacks.  
[simulationMode](Physics-simulationMode.html)| Controls when Unity executes
the physics simulation.  
[sleepThreshold](Physics-sleepThreshold.html)| The mass-normalized energy
threshold, below which objects start going to sleep.  
  
### Static Methods

[BakeMesh](Physics.BakeMesh.html)| Prepares the mesh for use with a
MeshCollider and uses default cooking options.  
---|---  
[BoxCast](Physics.BoxCast.html)| Casts the box along a ray and returns
detailed information on what was hit.  
[BoxCastAll](Physics.BoxCastAll.html)| Like Physics.BoxCast, but returns all
hits.  
[BoxCastNonAlloc](Physics.BoxCastNonAlloc.html)| Cast the box along the
direction, and store hits in the provided buffer.  
[CapsuleCast](Physics.CapsuleCast.html)| Casts a capsule against all colliders
in the Scene and returns detailed information on what was hit.  
[CapsuleCastAll](Physics.CapsuleCastAll.html)| Like Physics.CapsuleCast, but
this function will return all hits the capsule sweep intersects.  
[CapsuleCastNonAlloc](Physics.CapsuleCastNonAlloc.html)| Casts a capsule
against all colliders in the Scene and returns detailed information on what
was hit into the buffer.  
[CheckBox](Physics.CheckBox.html)| Check whether the given box overlaps with
other colliders or not.  
[CheckCapsule](Physics.CheckCapsule.html)| Checks if any colliders overlap a
capsule-shaped volume in world space.  
[CheckSphere](Physics.CheckSphere.html)| Returns true if there are any
colliders overlapping the sphere defined by position and radius in world
coordinates.  
[ClosestPoint](Physics.ClosestPoint.html)| Returns a point on the given
collider that is closest to the specified location.  
[ComputePenetration](Physics.ComputePenetration.html)| Compute the minimal
translation required to separate the given colliders apart at specified poses.  
[GetIgnoreCollision](Physics.GetIgnoreCollision.html)| Checks whether the
collision detection system will ignore all collisions/triggers between
collider1 and collider2 or not.  
[GetIgnoreLayerCollision](Physics.GetIgnoreLayerCollision.html)| Are
collisions between layer1 and layer2 being ignored?  
[IgnoreCollision](Physics.IgnoreCollision.html)| Makes the collision detection
system ignore all collisions between collider1 and collider2.  
[IgnoreLayerCollision](Physics.IgnoreLayerCollision.html)| Makes the collision
detection system ignore all collisions between any collider in layer1 and any
collider in layer2.Note that IgnoreLayerCollision will reset the trigger state
of affected colliders, so you might receive OnTriggerExit and OnTriggerEnter
messages in response to calling this.  
[Linecast](Physics.Linecast.html)| Returns true if there is any collider
intersecting the line between start and end.  
[OverlapBox](Physics.OverlapBox.html)| Find all colliders touching or inside
of the given box.  
[OverlapBoxNonAlloc](Physics.OverlapBoxNonAlloc.html)| Find all colliders
touching or inside of the given box, and store them into the buffer.  
[OverlapCapsule](Physics.OverlapCapsule.html)| Check the given capsule against
the physics world and return all overlapping colliders.  
[OverlapCapsuleNonAlloc](Physics.OverlapCapsuleNonAlloc.html)| Check the given
capsule against the physics world and return all overlapping colliders in the
user-provided buffer.  
[OverlapSphere](Physics.OverlapSphere.html)| Computes and stores colliders
touching or inside the sphere.  
[OverlapSphereNonAlloc](Physics.OverlapSphereNonAlloc.html)| Computes and
stores colliders touching or inside the sphere into the provided buffer.  
[Raycast](Physics.Raycast.html)| Casts a ray, from point origin, in direction
direction, of length maxDistance, against all colliders in the Scene.  
[RaycastAll](Physics.RaycastAll.html)| Casts a ray through the Scene and
returns all hits. Note that order of the results is undefined.  
[RaycastNonAlloc](Physics.RaycastNonAlloc.html)| Cast a ray through the Scene
and store the hits into the buffer.  
[Simulate](Physics.Simulate.html)| Simulate physics in the Scene.  
[SphereCast](Physics.SphereCast.html)| Casts a sphere along a ray and returns
detailed information on what was hit.  
[SphereCastAll](Physics.SphereCastAll.html)| Like Physics.SphereCast, but this
function will return all hits the sphere sweep intersects.  
[SphereCastNonAlloc](Physics.SphereCastNonAlloc.html)| Cast sphere along the
direction and store the results into buffer.  
[SyncTransforms](Physics.SyncTransforms.html)| Apply Transform changes to the
physics engine.  
  
### Events

[ContactEvent](Physics.ContactEvent.html)| Subscribe to this event to read all
collisions that occurred during the physics simulation step.  
---|---  
[ContactModifyEvent](Physics.ContactModifyEvent.html)| Subscribe to this event
to be able to customize the collision response for contact pairs.  
[ContactModifyEventCCD](Physics.ContactModifyEventCCD.html)| Subscribe to this
event to be able to customize the collision response of CCD generated contact
pairs.  
  
### Delegates

[ContactEventDelegate](Physics.ContactEventDelegate.html)|  
---|---  
  
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

