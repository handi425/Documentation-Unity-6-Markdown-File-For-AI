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

#  [NavMesh](AI.NavMesh.html).SamplePosition

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

public static bool SamplePosition([Vector3](Vector3.html) sourcePosition, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit, float maxDistance, int areaMask);

### Parameters

sourcePosition | The origin of the sample query.  
---|---  
hit | Holds the properties of the resulting location. The value of `hit.normal` is never computed. It is always (0,0,0).  
maxDistance | Sample within this distance from sourcePosition.  
areaMask | A mask that specifies the NavMesh areas allowed when finding the nearest point.  
  
### Returns

**bool** True if the nearest point is found.

### Description

Finds the nearest point based on the NavMesh within a specified range.

The nearest point is found by projecting the input point onto nearby NavMesh
instances along the vertical axis. This vertical axis has been chosen for each
instance at the time of [creation](AI.NavMesh.AddNavMeshData.html). If this
step does not find a projected point within the specified distance, then
sampling is extended to surrounding NavMesh positions.  
  
Finds the nearest point based on the distance to the query point. This
function does not consider obstructions. For example, in a two story
structure, if the sourcePosition is set to a point on the ceiling on the first
floor, the nearest point might be found on the second floor rather than the
first floor. The ceiling is not considered as an obstruction.  
  
This function may reduce the frame rate if a large search radius is specified.
To avoid frame rate issues, it is recommended that you specify a maxDistance
of twice the agent height.  
  
If you are trying to find a random point on the NavMesh, you should use the
recommended radius and perform the find multiple times instead of using a very
large radius.

    
    
    // RandomPointOnNavMesh
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class RandomPointOnNavMesh : [MonoBehaviour](MonoBehaviour.html)
    {
        public float range = 10.0f;  
      
        bool RandomPoint([Vector3](Vector3.html) center, float range, out [Vector3](Vector3.html) result)
        {
            for (int i = 0; i < 30; i++)
            {
                [Vector3](Vector3.html) randomPoint = center + [Random.insideUnitSphere](Random-insideUnitSphere.html) * range;
                [NavMeshHit](AI.NavMeshHit.html) hit;
                if ([NavMesh.SamplePosition](AI.NavMesh.SamplePosition.html)(randomPoint, out hit, 1.0f, [NavMesh.AllAreas](AI.NavMesh.AllAreas.html)))
                {
                    result = hit.position;
                    return true;
                }
            }
            result = [Vector3.zero](Vector3-zero.html);
            return false;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Vector3](Vector3.html) point;
            if (RandomPoint(transform.position, range, out point))
            {
                [Debug.DrawRay](Debug.DrawRay.html)(point, [Vector3.up](Vector3-up.html), [Color.blue](Color-blue.html), 1.0f);
            }
        }
    }
    

* * *

## Declaration

public static bool SamplePosition([Vector3](Vector3.html) sourcePosition, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit, float maxDistance,
[AI.NavMeshQueryFilter](AI.NavMeshQueryFilter.html) filter);

### Parameters

sourcePosition | The origin of the sample query.  
---|---  
hit | Holds the properties of the resulting location. The value of `hit.normal` is never computed. It is always (0,0,0).  
maxDistance | Sample within this distance from sourcePosition.  
filter | A filter specifying which NavMesh areas are allowed when finding the nearest point.  
  
### Returns

**bool** True if the nearest point is found.

### Description

Samples the position nearest the sourcePosition on any NavMesh built for the
agent type specified by the filter.

Consider only positions on areas defined in the
[NavMeshQueryFilter.areaMask](AI.NavMeshQueryFilter-areaMask.html). A maximum
search radius is set by maxDistance. The information of any found position is
returned in the hit argument.

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

