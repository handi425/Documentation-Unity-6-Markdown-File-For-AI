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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).MoveLocation

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

public NavMeshLocation MoveLocation(NavMeshLocation location,
[Vector3](Vector3.html) target, int areaMask);

### Parameters

location | Position to be moved across the NavMesh surface.  
---|---  
target | World position you require the agent to move to.  
areaMask | Bitmask with values of 1 set at the indices corresponding to areas that can be traversed, and with values of 0 for areas that should not be traversed. This parameter can be omitted, in which case it defaults to [NavMesh.AllAreas](AI.NavMesh.AllAreas.html). Additional resources: [Areas and Costs](../Manual/nav-AreasAndCosts.html).  
  
### Returns

**NavMeshLocation** A new location on the NavMesh placed as closely as
possible to the specified `target` position.  
The start `location` is returned when that start is inside an area which is
not allowed by the `areaMask`.

### Description

Translates a NavMesh location to another position without losing contact with
the surface.

Returns the location on the NavMesh that is closest to the `target` position
and that also has a continuous connection on the NavMesh surface through the
allowed area types all the way to the start position specified by the
`location` parameter. If the `target` position is outside the edges of the
surface or of its allowed areas, a position at the edge is returned.  
  
The movement does not cross [NavMeshLinks](../Manual/class-NavMeshLink.html)
or [Off-mesh Links](../Manual/nav-CreateOffMeshLink.html).  
  
The result might not be accurate (the closest) if the `pathNodePoolSize` value
in the NavMeshQuery initialization was not large enough to accommodate all the
nodes that needed to be traversed in order to find a connection between
`location.position` and `target`.  
  
Additional resources: NavMeshQuery.MoveLocations,
NavMeshQuery.MoveLocationsInSameAreas.

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

