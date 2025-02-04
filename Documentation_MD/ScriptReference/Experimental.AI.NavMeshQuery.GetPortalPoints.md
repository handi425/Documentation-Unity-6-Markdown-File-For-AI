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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).GetPortalPoints

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

public bool GetPortalPoints(PolygonId polygon, PolygonId neighbourPolygon, out
[Vector3](Vector3.html) left, out [Vector3](Vector3.html) right);

### Parameters

polygon | First NavMesh node.  
---|---  
neighbourPolygon | Second NavMesh node.  
left | One of the world points for the resulting separation edge which must be passed through when traversing between the two specified nodes. This point is the left side of the edge when traversing from the first node to the second.  
right | One of the world points for the resulting separation edge which must be passed through when traversing between the two specified nodes. This point is the right side of the edge when traversing from the first node to the second.  
  
### Returns

**bool** `True` if a connection exists between the two NavMesh nodes. `False`
if no connection exists between the two NavMesh nodes.

### Description

Obtains the end points of the line segment common to two adjacent NavMesh
nodes.

For two polygons that are part of a NavMesh surface, this method returns the
edge where both polygons meet. If the two polygons are in different NavMesh
tiles the connected edges can be of different length or have different start
and end positions from each other. If this happens the resulting separation
edge is the overlapping part of the edges, which may be shorter than either of
the individual edges.  
  
When one node is a link and the other is a polygon, the returned points are
placed where the link intersects the polygon.  
  
The resulting positions are expressed in world space and can be transformed
into a NavMesh's local space by the use of
NavMeshQuery.PolygonWorldToLocalMatrix.  
  
Additional resources: NavMeshQuery.GetEdgesAndNeighbors.

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

