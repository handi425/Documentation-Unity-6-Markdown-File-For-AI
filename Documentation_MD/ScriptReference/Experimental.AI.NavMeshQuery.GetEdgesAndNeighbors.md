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

#  [NavMeshQuery](Experimental.AI.NavMeshQuery.html).GetEdgesAndNeighbors

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

public PathQueryStatus GetEdgesAndNeighbors(PolygonId node,
NativeSlice<Vector3> edgeVertices, NativeSlice<PolygonId> neighbors,
NativeSlice<byte> edgeIndices, out int verticesCount, out int neighborsCount);

### Parameters

node | Identifier of a node from a NavMesh surface, [NavMeshLink](../Manual/class-NavMeshLink.html) or [Off-mesh Link](../Manual/nav-CreateOffMeshLink.html) for which the vertices and neighbors need to be retrieved.  
---|---  
edgeVertices | The result buffer that contains the world positions describing the geometry of the input navigation `node`. It can have zero capacity.  
[Polygonal](NavMeshPolyTypes.Ground.html) nodes of the NavMesh have a minimum
of 3 and a maximum of 6 vertices.  
[OffMeshConnection](NavMeshPolyTypes.OffMeshConnection.html) nodes are always
represented by 4 vertices, regardless of their width.  
neighbors | The result buffer that holds the identifiers of all the navigation nodes immediately reachable from the given `node`. It can have zero capacity.  
edgeIndices | The helper result buffer that maps each neighbor node to an edge of the given `node`. It can have zero capacity.  
The index of an element in `edgeIndices` is also an index in the `neighbors`
array and the value of that `edgeIndices` element is an index in the
`edgeVertices` array.  
verticesCount | The total number of vertices that describe the geometry of the input `node`. This is independent of the capacity of the `vertices` result buffer.  
neighborsCount | The total number of navigation nodes the input `node` connects to. This is independent of the capacity of the result buffers (`neighbors` and `edgeIndices`).  
  
### Returns

**PathQueryStatus** `Success` if Unity can evaluate the neighbors and vertices
of the specified node, regardless of the result. The `verticesCount` and
`neighborsCount` are always valid in this case.  
`Failure` if Unity can not use the `node` identifier to retrieve the neighbors
or geometry information. Unity does not modify any of the five result
parameters (`edgeVertices`, `neighbors`, `edgeIndices`, `verticesCount` or
`neighborsCount`) in this case.  
`InvalidParam` is part of the returned flags if the specified navigation node
is not [valid](NavMeshQuery.IsValid.html) in the query's NavMeshWorld.  
`BufferTooSmall` is part of the PathQueryStatus flags, that Unity returns from
this function, when any of the result buffers you provide are not large enough
to hold all the neighbor nodes the input `node` connects to or all of its edge
vertices.

### Description

Retrieves the vertices of a given `node` and the [identifiers](PolygonId.html)
of all the navigation nodes to which it connects.

A [polygon](NavMeshPolyTypes.Ground.html) of a NavMesh surface connects to all
other neighboring polygons with which it shares an edge as well as all the
[OffMeshLinks or NavMeshLinks](NavMeshPolyTypes.OffMeshConnection.html) that
leave from anywhere on its surface. The polygon does not connect to other
polygons with which it shares only a vertex.  
Each point returned in the `edgeVertices` array represents the start of a
`node`'s edge and the subsequent element in the array is the end point of that
edge. All vertices form a closed polygonal line. The last and first elements
define the last edge.  
  
An [off-mesh link](NavMeshPolyTypes.OffMeshConnection.html) connects to all
the NavMesh polygons that each end of the link intersects with, regardless of
whether the link is unidirectional.  
For link nodes the returned `edgeVertices` array contains two pairs of points
at indices [0]-[1] and [2]-[3] that define the end points of the start and end
edges of the link, in this order. These are the world positions established at
the moment when the link is instantiated in the NavMesh world. For nodes added
through [Off-mesh Link](../Manual/nav-CreateOffMeshLink.html) components the
pairs contain the same value in both of their elements.  
  
A node from the `neighbors` array lies at the edge returned in `edgeIndices`
at the same index.  
If both the given `node` and its neighbor are NavMesh
[polygons](NavMeshPolyTypes.Ground.html), then the corresponding `edgeIndices`
value represents the index of the polygon edge that leads from `node` to the
neighbor. E.g. `edgeVertices[edgeIndices[2]]` represents the start point of
the edge that is common between `node` and the `neighbors[2]` node, and
`edgeVertices[edgeIndices[2] + 1]` is the end point of that edge.  
A NavMesh polygon can have a maximum of 6 edges. This means the `edgeIndices`
value corresponding to a polygon-polygon connection is between 0 and 5,
inclusive. An edge usually connects only the two polygons that share it, but
edges that sit at a tile border can connect one polygon in the first tile to
multiple polygons in the second tile. In this case, `edgeIndices` report the
same value for all of those neighbors.  
If either the given `node` or the `neighbor` is a
[link](NavMeshPolyTypes.OffMeshConnection.html), then the corresponding
`edgeIndices` value represents the side on the link where the connection is
made: 0 for [start](AI.NavMeshLinkData-startPosition.html) and 2 for
[end](AI.NavMeshLinkData-endPosition.html). When the `node` is a polygon and
the `neighbor` is a link the value acts only as information about the side of
the link where the two nodes connect and should not be used as an index in the
`edgeVertices` array.  
When the `neighbors` and `edgeIndices` buffers both have positive capacity,
they must be the same size, otherwise you will encounter an
`ArgumentException` when this method executes in the Editor.  
  
You can set any of the buffers to have zero capacity for the cases when you do
not need the results.  
  
The returned `verticesCount` and `neighborsCount` values express the number of
elements that comprise the result in the output buffers of sufficient size.
Buffers that are not large enough are still filled with valid nodes up to
their full capacity.  
  
The five result parameters (`edgeVertices`, `neighbors`, `edgeIndices`,
`verticesCount` and `neighborsCount`) do not act as input and do not change
the internal navigation data in any way. Unity only modifies them in the case
when the operation returns a `Success` status.  
  
Additional resources: NavMeshQuery.GetPolygonType,
NavMeshQuery.GetPortalPoints.

    
    
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.Experimental.AI;  
      
    public class NavMeshNodeEdgesDrawer : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            var query = new NavMeshQuery(NavMeshWorld.GetDefaultWorld(), [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var vertices = new NativeArray<[Vector3](Vector3.html)>(6, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var neighbors = new NativeArray<PolygonId>(10, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var edgeIndices = new NativeArray<byte>(neighbors.Length, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            int totalVertices;
            int totalNeighbors;  
      
            var location = query.MapLocation(transform.position, [Vector3.one](Vector3-one.html), 0);  
      
            var queryStatus = query.GetEdgesAndNeighbors(
                location.polygon, vertices, neighbors, edgeIndices,
                out totalVertices, out totalNeighbors);  
      
            var color = (queryStatus & PathQueryStatus.Success) != 0 ? [Color.green](Color-green.html) : [Color.red](Color-red.html);
            [Debug.DrawLine](Debug.DrawLine.html)(transform.position - [Vector3.up](Vector3-up.html), transform.position + [Vector3.up](Vector3-up.html), color);  
      
            for (int i = 0, j = totalVertices - 1; i < totalVertices; j = i++)
            {
                [Debug.DrawLine](Debug.DrawLine.html)(vertices[i], vertices[j], [Color.grey](Color-grey.html));
            }  
      
            for (var i = 0; i < totalNeighbors; i++)
            {
                if (query.GetPolygonType(neighbors[i]) == NavMeshPolyTypes.OffMeshConnection)
                {
                    // The link neighbor is not connected through any of the polygon's edges.
                    // Call GetEdgesAndNeighbors() on this specific neighbor in order to retrieve its edges.
                    continue;
                }  
      
                var start = edgeIndices[i];
                var end = (start + 1) % totalVertices;
                var neighborColor = [Color.Lerp](Color.Lerp.html)([Color.yellow](Color-yellow.html), [Color.magenta](Color-magenta.html), 1f * start / (totalVertices - 1));
                [Debug.DrawLine](Debug.DrawLine.html)(vertices[start], vertices[end], neighborColor);
            }  
      
            query.Dispose();
            vertices.Dispose();
            neighbors.Dispose();
            edgeIndices.Dispose();
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

