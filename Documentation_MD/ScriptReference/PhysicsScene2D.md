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

# PhysicsScene2D

struct in UnityEngine

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

Represents a single instance of a 2D physics Scene.

A 2D physics Scene owns all 2D physics component objects added to it and can
perform a simulation of them as well as execute queries against them. All of
this functionality is isolated from any other physics Scene. Using this,
multiple independent physics Scenes can coexist.

### Properties

[subStepCount](PhysicsScene2D-subStepCount.html)| The number of simulation
sub-steps that occurred during the last simulation step.  
---|---  
[subStepLostTime](PhysicsScene2D-subStepLostTime.html)| The amount of
simulation time that has been "lost" due to simulation sub-stepping hitting
the maximum number of allowed sub-steps.  
  
### Public Methods

[BoxCast](PhysicsScene2D.BoxCast.html)| Casts a box against colliders in the
PhysicsScene2D, returning the first intersection only.  
---|---  
[CapsuleCast](PhysicsScene2D.CapsuleCast.html)| Casts a capsule against
colliders in the PhysicsScene2D, returning the first intersection only.  
[CircleCast](PhysicsScene2D.CircleCast.html)| Casts a circle against colliders
in the PhysicsScene2D, returning the first intersection only.  
[GetRayIntersection](PhysicsScene2D.GetRayIntersection.html)| Cast a 3D ray
against the 2D Colliders in the Scene.  
[IsEmpty](PhysicsScene2D.IsEmpty.html)| Determines whether the physics Scene
is empty or not.  
[IsValid](PhysicsScene2D.IsValid.html)| Determines whether the physics Scene
is valid or not.  
[Linecast](PhysicsScene2D.Linecast.html)| Casts a line segment against
colliders in the PhysicsScene2D, returning the first intersection only.  
[OverlapArea](PhysicsScene2D.OverlapArea.html)| Checks an area (non-rotated
box) against Colliders in the PhysicsScene2D, returning the first intersection
only.  
[OverlapBox](PhysicsScene2D.OverlapBox.html)| Checks a box against Colliders
in the PhysicsScene2D, returning the first intersection only.  
[OverlapCapsule](PhysicsScene2D.OverlapCapsule.html)| Checks a capsule against
Colliders in the PhysicsScene2D, returning the first intersection only.  
[OverlapCircle](PhysicsScene2D.OverlapCircle.html)| Checks a circle against
Colliders in the PhysicsScene2D, returning the first intersection only.  
[OverlapPoint](PhysicsScene2D.OverlapPoint.html)| Checks a point against
Colliders in the PhysicsScene2D, returning the first intersection only.  
[Raycast](PhysicsScene2D.Raycast.html)| Casts a ray against colliders in the
PhysicsScene2D, returning the first intersection only.  
[Simulate](PhysicsScene2D.Simulate.html)| Simulate physics associated with
this PhysicsScene.  
  
### Static Methods

[OverlapCollider](PhysicsScene2D.OverlapCollider.html)| Checks a Collider
against Colliders in the PhysicsScene2D, returning all intersections.  
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

