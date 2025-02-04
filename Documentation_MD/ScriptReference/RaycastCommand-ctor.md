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

# RaycastCommand Constructor

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

public RaycastCommand([Vector3](Vector3.html) from, [Vector3](Vector3.html)
direction, [QueryParameters](QueryParameters.html) queryParameters, float
distance);

### Parameters

from | The starting point of the ray in world coordinates.  
---|---  
direction | The direction of the ray.  
distance | The maximum distance the ray should check for collisions.  
queryParameters | Structure for specifying additional parameters for a batch query such as layer mask, hit multiple mesh faces, hit triggers and hit backfaces.  
  
### Description

Create a RaycastCommand.

The query is run in the default physics scene.

* * *

## Declaration

public RaycastCommand([PhysicsScene](PhysicsScene.html) physicsScene,
[Vector3](Vector3.html) from, [Vector3](Vector3.html) direction,
[QueryParameters](QueryParameters.html) queryParameters, float distance);

### Parameters

physicsScene | The physics scene to run the raycast query in.  
---|---  
from | The starting point of the ray in world coordinates.  
direction | The direction of the ray.  
distance | The maximum distance the ray should check for collisions.  
queryParameters | Structure for specifying additional parameters for a batch query such as layer mask, hit multiple mesh faces, hit triggers and hit backfaces.  
  
### Description

Create a RaycastCommand.

* * *

**Obsolete** This struct signature is no longer supported. Use struct with a
QueryParameters instead.

## Declaration

public RaycastCommand([Vector3](Vector3.html) from, [Vector3](Vector3.html)
direction, float distance, int layerMask, int maxHits);

### Parameters

from | The starting point of the ray in world coordinates.  
---|---  
direction | The direction of the ray.  
distance | The maximum distance the ray should check for collisions.  
layerMask | A [LayerMask](LayerMask.html) that is used to selectively ignore Colliders when casting a ray.  
maxHits | The maximum number of Colliders the ray can hit.  
  
### Description

Create a RaycastCommand.

The query is run in the default physics scene.

* * *

**Obsolete** This struct signature is no longer supported. Use struct with a
QueryParameters instead.

## Declaration

public RaycastCommand([PhysicsScene](PhysicsScene.html) physicsScene,
[Vector3](Vector3.html) from, [Vector3](Vector3.html) direction, float
distance, int layerMask, int maxHits);

### Parameters

physicsScene | The physics scene to run the raycast query in.  
---|---  
from | The starting point of the ray in world coordinates.  
direction | The direction of the ray.  
distance | The maximum distance the ray should check for collisions.  
layerMask | A [LayerMask](LayerMask.html) that is used to selectively ignore Colliders when casting a ray.  
maxHits | The maximum number of Colliders the ray can hit.  
  
### Description

Create a RaycastCommand.

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

