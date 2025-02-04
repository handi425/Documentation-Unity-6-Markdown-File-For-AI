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

#  [Physics](Physics.html).ComputePenetration

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

public static bool ComputePenetration([Collider](Collider.html) colliderA,
[Vector3](Vector3.html) positionA, [Quaternion](Quaternion.html) rotationA,
[Collider](Collider.html) colliderB, [Vector3](Vector3.html) positionB,
[Quaternion](Quaternion.html) rotationB, out [Vector3](Vector3.html)
direction, out float distance);

### Parameters

colliderA | The first collider.  
---|---  
positionA | Position of the first collider.  
rotationA | Rotation of the first collider.  
colliderB | The second collider.  
positionB | Position of the second collider.  
rotationB | Rotation of the second collider.  
direction | Direction along which the translation required to separate the colliders apart is minimal.  
distance | The distance along direction that is required to separate the colliders apart.  
  
### Returns

**bool** True, if the colliders overlap at the given poses.

### Description

Compute the minimal translation required to separate the given colliders apart
at specified poses.

Translating the first collider by direction * distance will separate the
colliders apart if the function returned true. Otherwise, direction and
distance are not defined.  
  
One of the colliders has to be BoxCollider, SphereCollider CapsuleCollider or
a convex MeshCollider. The other one can be any type.  
  
Note that you aren't restricted to the position and rotation the colliders
have at the moment of the call. Passing position or rotation that is different
from the currently set one doesn't have an effect of physically moving any
colliders thus has no side effects on the Scene.  
  
Doesn't depend on any spatial structures to be updated first, so is not bound
to be used only within FixedUpdate timeframe.  
  
Ignores backfaced triangles and doesn't respect
[Physics.queriesHitBackfaces](Physics-queriesHitBackfaces.html).  
  
This function is useful to write custom depenetration functions. One
particular example is an implementation of a character controller where a
specific reaction to collision with the surrounding physics objects is
required. In this case, one would first query for the colliders nearby using
OverlapSphere and then adjust the character's position using the data returned
by ComputePenetration.

    
    
    using UnityEngine;  
      
    // Visualises the minimum translation vectors required to separate apart from other colliders found in a given radius
    // Attach to a [GameObject](GameObject.html) that has a [Collider](Collider.html) attached.
    [[ExecuteInEditMode](ExecuteInEditMode.html)()]
    public class ShowPenetration : [MonoBehaviour](MonoBehaviour.html)
    {
        public float radius = 3f; // show penetration into the colliders located inside a sphere of this radius
        public int maxNeighbours = 16; // maximum amount of neighbours visualised  
      
        private [Collider](Collider.html)[] neighbours;  
      
        public void Start()
        {
            neighbours = new [Collider](Collider.html)[maxNeighbours];
        }  
      
        public void OnDrawGizmos()
        {
            var thisCollider = GetComponent<[Collider](Collider.html)>();  
      
            if (!thisCollider)
                return; // nothing to do without a [Collider](Collider.html) attached  
      
            int count = [Physics.OverlapSphereNonAlloc](Physics.OverlapSphereNonAlloc.html)(transform.position, radius, neighbours);  
      
            for (int i = 0; i < count; ++i)
            {
                var collider = neighbours[i];  
      
                if (collider == thisCollider)
                    continue; // skip ourself  
      
                [Vector3](Vector3.html) otherPosition = collider.gameObject.transform.position;
                [Quaternion](Quaternion.html) otherRotation = collider.gameObject.transform.rotation;  
      
                [Vector3](Vector3.html) direction;
                float distance;  
      
                bool overlapped = [Physics.ComputePenetration](Physics.ComputePenetration.html)(
                    thisCollider, transform.position, transform.rotation,
                    collider, otherPosition, otherRotation,
                    out direction, out distance
                );  
      
                // draw a line showing the depenetration direction if overlapped
                if (overlapped)
                {
                    [Gizmos.color](Gizmos-color.html) = [Color.red](Color-red.html);
                    [Gizmos.DrawRay](Gizmos.DrawRay.html)(otherPosition, direction * distance);
                }
            }
        }
    }
    

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

