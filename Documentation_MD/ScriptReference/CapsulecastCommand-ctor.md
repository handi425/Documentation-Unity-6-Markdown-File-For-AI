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

# CapsulecastCommand Constructor

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

## Declaration

public CapsulecastCommand([Vector3](Vector3.html) p1, [Vector3](Vector3.html)
p2, float radius, [Vector3](Vector3.html) direction,
[QueryParameters](QueryParameters.html) queryParameters, float distance);

### Parameters

p1 | The center of the sphere at the `start` of the capsule.  
---|---  
p2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction of the capsule cast.  
queryParameters | Structure for specifying additional parameters for a batch query such as layer mask, hit triggers and hit backfaces.  
distance | The maximum length of the sweep.  
  
### Description

Creates a CapsulecastCommand.

This command is run in the default physics scene.

* * *

## Declaration

public CapsulecastCommand([PhysicsScene](PhysicsScene.html) physicsScene,
[Vector3](Vector3.html) p1, [Vector3](Vector3.html) p2, float radius,
[Vector3](Vector3.html) direction, [QueryParameters](QueryParameters.html)
queryParameters, float distance);

### Parameters

physicsScene | The physics scene to run the command in.  
---|---  
p1 | The center of the sphere at the `start` of the capsule.  
p2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction of the capsule cast.  
queryParameters | Structure for specifying additional parameters for a batch query such as layer mask, hit triggers and hit backfaces.  
distance | The maximum length of the sweep.  
  
### Description

Creates a CapsulecastCommand.

* * *

**Obsolete** This struct signature is no longer supported. Use struct with a
QueryParameters instead.

## Declaration

public CapsulecastCommand([Vector3](Vector3.html) p1, [Vector3](Vector3.html)
p2, float radius, [Vector3](Vector3.html) direction, float distance, int
layerMask);

### Parameters

p1 | The center of the sphere at the `start` of the capsule.  
---|---  
p2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction of the capsule cast.  
distance | The maximum length of the sweep.  
layerMask | The [LayerMask](LayerMask.html) that selectively ignores Colliders when casting a capsule.  
  
### Description

Creates a CapsulecastCommand.

This command is run in the default physics scene.

* * *

**Obsolete** This struct signature is no longer supported. Use struct with a
QueryParameters instead.

## Declaration

public CapsulecastCommand([PhysicsScene](PhysicsScene.html) physicsScene,
[Vector3](Vector3.html) p1, [Vector3](Vector3.html) p2, float radius,
[Vector3](Vector3.html) direction, float distance, int layerMask);

### Parameters

physicsScene | The physics scene to run the command in.  
---|---  
p1 | The center of the sphere at the `start` of the capsule.  
p2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction of the capsule cast.  
distance | The maximum length of the sweep.  
layerMask | The [LayerMask](LayerMask.html) that selectively ignores Colliders when casting a capsule.  
  
### Description

Creates a CapsulecastCommand.

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

