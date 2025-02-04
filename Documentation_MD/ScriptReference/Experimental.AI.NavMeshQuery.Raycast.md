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

**Method group is Obsolete**  

**Experimental** : this API is experimental and might be changed or removed in
the future.

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).Raycast

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

**Obsolete** The experimental NavMeshQuery struct has been deprecated without
replacement.

## Declaration

public PathQueryStatus Raycast(out [AI.NavMeshHit](AI.NavMeshHit.html) hit,
NavMeshLocation start, [Vector3](Vector3.html) targetPosition, int areaMask,
NativeArray<float> costs);

### Parameters

hit | Holds the properties of the raycast resulting location.  
---|---  
start | The start location of the ray on the NavMesh. `start.polygon` must be of the type NavMeshPolyTypes.Ground.  
targetPosition | The desired end of the ray, in world coordinates.  
areaMask | Bitmask that correlates index positions with area types. The index goes from 0 to 31. In each relevant index position, you have to set the value to either 1 or 0. 1 indicates area types that the ray can pass through. 0 indicates area types that block the ray. This parameter is optional. If you leave out this parameter, it defaults to [NavMesh.AllAreas](AI.NavMesh.AllAreas.html). To learn more, see: [Areas and Costs](../Manual/nav-AreasAndCosts.html).  
costs | Array of custom cost values for all of the 32 possible area types. They act as multipliers to the distance reported by the ray when crossing various areas. This parameter is optional. If you omit it, it defaults to the area costs that you configured in the Project settings. To learn more, see [NavMesh.GetAreaCost](AI.NavMesh.GetAreaCost.html).  
  
### Returns

**PathQueryStatus** `Success` if the ray can be correctly traced using the
provided arguments.  
`Failure` if the `start` location is not valid in the query's NavMeshWorld, or
if it is inside an area not permitted by the `areaMask` argument, or when it
is on a [NavMeshLink](../Manual/class-NavMeshLink.html)/OffMeshLink.

### Description

Trace a line between two points on the NavMesh.

This method is similar to [NavMesh.Raycast](AI.NavMesh.Raycast.html), both of
them sharing the same underlying implementation.  
The properties that make this one different are:

  * it can be used in parallel [jobs](../Manual/JobSystem.html);
  * it returns status flags indicating whether the operation succeeded or failed;
  * the reported `hit.distance` is affected by the area costs;
  * the resulting `hit.position` is not adjusted on the vertical axis according to the [Height Mesh](../Manual/nav-HeightMesh.html), if that exists;
  * it has the variant described below that returns also the list of polygons through which the ray passes.

The returned `hit.distance` represents the straight line between the start and
termination point. It also takes into account the list of the provided area
costs. It is the result of summing up all the distances covered by the ray
over each separate area, multiplied by the cost of that respective area.  
  
First, the start location is verified to be valid in the NavMeshWorld, and the
target point is mapped on the NavMesh. Then, a ray is traced from the start
point towards the target. If the computation is successful, the `hit` data is
filled with information about the furthest point that the ray has reached.
This happens regardless of whether the path from the source to target has been
obstructed.  
If the computation fails, the returned `hit` is filled with invalid data. Most
notably, the `hit.distance` field gets the value `positiveInfinity`.  
  
If the raycast terminates on an outer edge, `hit.mask` is 0; otherwise it
contains the area mask of the blocking polygon.  
  
You can use this function to check if an agent can walk unobstructed between
two points on the NavMesh. For example, if your character has an evasive dodge
move that needs space, you can shoot a ray from the character's location to
multiple directions. This finds a spot where the character can dodge to.  
  
The NavMeshQuery.Raycast is different from the Physics raycast. The
NavMeshQuery.Raycast can detect all kinds of navigation obstructions, for
example holes in the ground. It can also climb up slopes, if the area is
navigable.

    
    
    // TargetReachable
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.AI;
    using UnityEngine.Experimental.AI;  
      
    public class TargetReachable : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        NavMeshQuery m_NavQuery;
        [NavMeshHit](AI.NavMeshHit.html) m_Hit;  
      
        void OnEnable()
        {
            m_NavQuery = new NavMeshQuery(NavMeshWorld.GetDefaultWorld(), [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var startLocation = m_NavQuery.MapLocation(transform.position, [Vector3.one](Vector3-one.html), 0);
            var status = m_NavQuery.Raycast(out m_Hit, startLocation, target.position, [NavMesh.AllAreas](AI.NavMesh.AllAreas.html), new NativeArray<float>());
            if ((status & PathQueryStatus.Success) != 0)
            {
                [Debug.DrawLine](Debug.DrawLine.html)(transform.position, target.position, m_Hit.hit ? [Color.red](Color-red.html) : [Color.green](Color-green.html));  
      
                if (m_Hit.hit)
                    [Debug.DrawRay](Debug.DrawRay.html)(m_Hit.position, [Vector3.up](Vector3-up.html), [Color.red](Color-red.html));
            }
        }  
      
        void OnDisable()
        {
            m_NavQuery.Dispose();
        }
    }
    

* * *

**Obsolete** The experimental NavMeshQuery struct has been deprecated without
replacement.

## Declaration

public PathQueryStatus Raycast(out [AI.NavMeshHit](AI.NavMeshHit.html) hit,
NativeSlice<PolygonId> path, out int pathCount, NavMeshLocation start,
[Vector3](Vector3.html) targetPosition, int areaMask, NativeArray<float>
costs);

### Parameters

hit | Holds the properties of the raycast resulting location.  
---|---  
path | A buffer that will be filled with the sequence of polygons through which the ray passes.  
pathCount | The reported number of polygons through which the ray has passed, all stored in the `path` buffer. It will not be greater than `path.Length`.  
start | The start location of the ray on the NavMesh. `start.polygon` must be of the type NavMeshPolyTypes.Ground.  
targetPosition | The desired end of the ray, in world coordinates.  
areaMask | A bitfield that specifies which NavMesh areas can be traversed when the ray is traced. This parameter is optional. If you do not fill out this parameter, it defaults to [NavMesh.AllAreas](AI.NavMesh.AllAreas.html).  
costs | Cost multipliers that affect the distance reported by the ray over different area types. This parameter is optional. If you omit it, it defaults to the area costs that you configured in the Project settings.  
  
### Returns

**PathQueryStatus** `Success` if the ray can be correctly traced using the
provided arguments.  
`Failure` if the `start` location is not valid in the query's NavMeshWorld, or
if it is inside an area not permitted by the `areaMask` argument, or when it
is on a [NavMeshLink](../Manual/class-NavMeshLink.html)/OffMeshLink.  
`BufferTooSmall` is part of the returned flags when the provided `path` buffer
is not large enough to hold all the polygons that the ray passed through.

### Description

Trace a line between two points on the NavMesh, and return the list of
polygons through which it passed.

Even if the `path` buffer is too small it will still hold as many polygons as
it has room for, starting from the ray's origin location.  
  
Additional resources: PolygonId.

    
    
    // StraightPathFromRay
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.AI;
    using UnityEngine.Experimental.AI;  
      
    public class StraightPathFromRay : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        NavMeshQuery m_NavQuery;
        [NavMeshHit](AI.NavMeshHit.html) m_Hit;
        NativeArray<PolygonId> m_Path;
        int m_PathCount;  
      
        void OnEnable()
        {
            m_Path = new NativeArray<PolygonId>(3, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            m_NavQuery = new NavMeshQuery(NavMeshWorld.GetDefaultWorld(), [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var startLocation = m_NavQuery.MapLocation(transform.position, [Vector3.one](Vector3-one.html), 0);
            PathQueryStatus status = m_NavQuery.Raycast(out m_Hit, m_Path, out m_PathCount, startLocation, target.position, [NavMesh.AllAreas](AI.NavMesh.AllAreas.html), new NativeArray<float>());
            if ((status & PathQueryStatus.Success) != 0)
            {
                var bufferTooSmall = (status & PathQueryStatus.BufferTooSmall) != 0;
                [Debug.DrawLine](Debug.DrawLine.html)(transform.position, m_Hit.position, bufferTooSmall ? [Color.black](Color-black.html) : [Color.green](Color-green.html));  
      
                if (m_Hit.hit)
                    [Debug.DrawRay](Debug.DrawRay.html)(m_Hit.position, [Vector3.up](Vector3-up.html), [Color.red](Color-red.html));
            }
        }  
      
        void OnDisable()
        {
            m_NavQuery.Dispose();
            m_Path.Dispose();
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

