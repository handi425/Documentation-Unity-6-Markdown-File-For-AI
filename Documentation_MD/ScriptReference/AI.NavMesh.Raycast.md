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

#  [NavMesh](AI.NavMesh.html).Raycast

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

public static bool Raycast([Vector3](Vector3.html) sourcePosition,
[Vector3](Vector3.html) targetPosition, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit, int areaMask);

### Parameters

sourcePosition | The origin of the ray.  
---|---  
targetPosition | The end of the ray.  
hit | Holds the properties of the ray cast resulting location.  
areaMask | A bitfield mask specifying which NavMesh areas can be passed when tracing the ray.  
  
### Returns

**bool** True if the ray is terminated before reaching target position.
Otherwise returns false.

### Description

Trace a line between two points on the NavMesh.

The source and destination points are first mapped on the NavMesh, then a ray
is traced from the source point towards the target. If the ray hits a NavMesh
boundary, the function returns true and the hit data is filled. If the path
from the source to target is unobstructed, the function returns false.  
  
If the raycast terminates on an outer edge, `hit.mask` is 0; otherwise it
contains the area mask of the blocking polygon.  
  
This function can be used to check if an agent can walk unobstructed between
two points on the NavMesh. For example if you character has an evasive dodge
move which needs space, you can shoot a ray from the characters location to
multiple directions to find a spot where the character can dodge to.  
  
The Raycast is different from physics ray cast because it works on “2.5D”, on
the NavMesh. The difference to physics ray casts is that NavMesh ray casts can
detect all kinds of navigation obstructions, such as holes in the ground, and
it can also climb up slopes, if the area is navigable.

    
    
    // TargetReachable
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class TargetReachable : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        private [NavMeshHit](AI.NavMeshHit.html) hit;
        private bool blocked = false;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            blocked = [NavMesh.Raycast](AI.NavMesh.Raycast.html)(transform.position, target.position, out hit, [NavMesh.AllAreas](AI.NavMesh.AllAreas.html));
            [Debug.DrawLine](Debug.DrawLine.html)(transform.position, target.position, blocked ? [Color.red](Color-red.html) : [Color.green](Color-green.html));  
      
            if (blocked)
                [Debug.DrawRay](Debug.DrawRay.html)(hit.position, [Vector3.up](Vector3-up.html), [Color.red](Color-red.html));
        }
    }
    

If you want to find the nearest point on the NavMesh, use physics ray cast to
find a point in the world. For more information, refer to the [Move an Agent
to a Position Clicked by the
Mouse](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/NavMoveToClickPoint.html)
example.

* * *

## Declaration

public static bool Raycast([Vector3](Vector3.html) sourcePosition,
[Vector3](Vector3.html) targetPosition, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit,
[AI.NavMeshQueryFilter](AI.NavMeshQueryFilter.html) filter);

### Parameters

sourcePosition | The origin of the ray.  
---|---  
targetPosition | The end of the ray.  
hit | Holds the properties of the ray cast resulting location.  
filter | A filter specifying which NavMesh areas can be passed when tracing the ray.  
  
### Returns

**bool** True if the ray is terminated before reaching target position.
Otherwise returns false.

### Description

Traces a line between two positions on the NavMesh, subject to the constraints
defined by the filter argument.

The line is terminated on outer edges or a non-passable area.

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

