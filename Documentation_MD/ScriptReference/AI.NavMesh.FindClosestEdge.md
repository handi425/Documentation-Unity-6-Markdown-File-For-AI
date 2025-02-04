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

#  [NavMesh](AI.NavMesh.html).FindClosestEdge

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

public static bool FindClosestEdge([Vector3](Vector3.html) sourcePosition, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit, int areaMask);

### Parameters

sourcePosition | The origin of the distance query.  
---|---  
hit | Holds the properties of the resulting location.  
areaMask | A bitfield mask specifying which NavMesh areas can be passed when finding the nearest edge.  
  
### Returns

**bool** True if the nearest edge is found.

### Description

Locate the closest NavMesh edge from a point on the NavMesh.

The returned [NavMeshHit](AI.NavMeshHit.html) object contains the position and
details of the nearest point on the nearest edge of the navmesh. This can be
used to query how much extra space there is around the agent.

    
    
    // MeasureSpace
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class MeasureSpace : [MonoBehaviour](MonoBehaviour.html)
    {
        void DrawCircle([Vector3](Vector3.html) center, float radius, [Color](Color.html) color)
        {
            [Vector3](Vector3.html) prevPos = center + new [Vector3](Vector3.html)(radius, 0, 0);
            for (int i = 0; i < 30; i++)
            {
                float angle = (float)(i + 1) / 30.0f * [Mathf.PI](Mathf.PI.html) * 2.0f;
                [Vector3](Vector3.html) newPos = center + new [Vector3](Vector3.html)([Mathf.Cos](Mathf.Cos.html)(angle) * radius, 0, [Mathf.Sin](Mathf.Sin.html)(angle) * radius);
                [Debug.DrawLine](Debug.DrawLine.html)(prevPos, newPos, color);
                prevPos = newPos;
            }
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [NavMeshHit](AI.NavMeshHit.html) hit;
            if ([NavMesh.FindClosestEdge](AI.NavMesh.FindClosestEdge.html)(transform.position, out hit, [NavMesh.AllAreas](AI.NavMesh.AllAreas.html)))
            {
                DrawCircle(transform.position, hit.distance, [Color.red](Color-red.html));
                [Debug.DrawRay](Debug.DrawRay.html)(hit.position, [Vector3.up](Vector3-up.html), [Color.red](Color-red.html));
            }
        }
    }
    

* * *

## Declaration

public static bool FindClosestEdge([Vector3](Vector3.html) sourcePosition, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit,
[AI.NavMeshQueryFilter](AI.NavMeshQueryFilter.html) filter);

### Parameters

sourcePosition | The origin of the distance query.  
---|---  
hit | Holds the properties of the resulting location.  
filter | A filter specifying which NavMesh areas can be passed when finding the nearest edge.  
  
### Returns

**bool** True if the nearest edge is found.

### Description

Locate the closest NavMesh edge from a point on the NavMesh, subject to the
constraints of the filter argument.

The returned NavMeshHit object contains the position and details of the
nearest point on the nearest edge of the NavMesh. This can be used to query
how much extra space there is around the agent.

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

