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

#  [Collider2D](Collider2D.html).CreateMesh

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

public [Mesh](Mesh.html) CreateMesh(bool useBodyPosition, bool
useBodyRotation, bool useDelaunay = true);

### Parameters

useBodyPosition | Should the mesh be transformed by the position of the attached [Rigidbody2D](Rigidbody2D.html)?  
---|---  
useBodyRotation | Should the mesh be transformed by the rotation of the attached [Rigidbody2D](Rigidbody2D.html)?  
useDelaunay | When true, Delaunay triangulation is used to generate the mesh. This can reduce the number of vertices created in the Collider mesh and reduce the number of small triangle fans produced, both of which can improve overall mesh size and performance.  
  
### Returns

**Mesh** The planar [Mesh](Mesh.html) created that matches the collider
geometry or NULL if no [Mesh](Mesh.html) could be created.

### Description

Creates a planar [Mesh](Mesh.html) that is identical to the area defined by
the [Collider2D](Collider2D.html) geometry.

In simple terms, this method will create a [Mesh](Mesh.html) that exactly
represents the area defined by the [Collider2D](Collider2D.html). The created
[Mesh](Mesh.html) can then be used for any purpose including but not limited
to navigation meshes for 2D navigation. The [Collider2D](Collider2D.html) does
not own the created [Mesh](Mesh.html) and you are responsible for its lifetime
therefore not deleting the [Mesh](Mesh.html) will result in a memory leak. The
[Collider2D](Collider2D.html) is not altered in any way during this call. The
[Collider2D](Collider2D.html) must have valid shapes present for a
[Mesh](Mesh.html) to be created otherwise NULL will be returned indicating
that no [Mesh](Mesh.html) was created.  
  
All [Collider2D](Collider2D.html) geometry lives in the space of the
[Rigidbody2D](Rigidbody2D.html) it is attached to. You can select whether the
[Mesh](Mesh.html) vertices are transformed by the
[Rigidbody2D](Rigidbody2D.html) position and rotation using `useBodyPosition`
and `useBodyRotation` respectively. If the [Collider2D](Collider2D.html) is
not attached to a [Rigidbody2D](Rigidbody2D.html) then the geometry is
permanently in world-space and both `useBodyPosition` and `useBodyRotation`
should always be set to false.  
  
What follows is more detail on how the [Collider2D](Collider2D.html) shapes
are considered when creating a [Mesh](Mesh.html). Whilst there are many types
of [Collider2D](Collider2D.html), they only produce collision geometry which
comprise of the following primitive shape types: Circle, Capsule, Polygon and
Edge. These primitive types are split into two groups known as closed convex
primitives and open primitives. Primitives of type Circle, Capsule and Polygon
are closed convex primitives which define a closed convex area bounded by the
primitive. The Edge primitive is an open type that defines geometry with no
internal area.  
  
A [CircleCollider2D](CircleCollider2D.html) will produce a single circle
primitive. A [CapsuleCollider2D](CapsuleCollider2D.html) will produce a single
capsule primitive. A [BoxCollider2D](BoxCollider2D.html) will produce a single
polygon primitive. A [PolygonCollider2D](PolygonCollider2D.html) can produce
multiple polygon primitives to convert a potentially concave area into
multiple convex polygons. An [EdgeCollider2D](EdgeCollider2D.html) can produce
multiple edge primitives. A
[TilemapCollider2D](Tilemaps.TilemapCollider2D.html) can produce multiple
polygon primitives (per-tile). A
[CompositeCollider2D](CompositeCollider2D.html) can produce either multiple
polygon primitives (in Polygon mode) or produce multiple edge primitives (in
Outline mode).  
  
When creating a [Mesh](Mesh.html) to represent [Collider2D](Collider2D.html)
geometry, all closed convex primitives (circle, capsule and polygon) produce
the respective filled area defined by those primitives. In the case where
there are multiple polygons, the total area of all the polygons is created.
Note that when [BoxCollider2D.edgeRadius](BoxCollider2D-edgeRadius.html) that
is greater than zero is used (to produce radial edges), the [Mesh](Mesh.html)
is created to also represent that geometry.  
  
When creating a [Mesh](Mesh.html) to represent [Collider2D](Collider2D.html)
geometry, all open primitives (edges) have special handling. When the start
vertex of the first edge is coincident with the end vertex of the last edge
(to define a pseudo-closed area) then a mesh is created to represent that
closed area even though 2D physics doesn't itself treat it as such. If the
vertex are not coincident then a [Mesh](Mesh.html) will only be created if
[EdgeCollider2D.edgeRadius](EdgeCollider2D-edgeRadius.html) is greater than
zero as this produces edges with an area.  
  
An [EdgeCollider2D](EdgeCollider2D.html) when used with coincident start/end
vertex will create a [Mesh](Mesh.html) that is a convex hull of all edge
vertices. Any concave vertex (producing a concave configuration) will be
considered as being on the convex hull resulting in a convex planar
[Mesh](Mesh.html). If a convex [Mesh](Mesh.html) is required then multiple
polygon primitives should be used i.e. a
[PolygonCollider2D](PolygonCollider2D.html) or a
[CompositeCollider2D](CompositeCollider2D.html) in polygon mode. A
[CompositeCollider2D](CompositeCollider2D.html) in outline mode produces edges
with coincident start/end vertex so will always create a closed shape
[Mesh](Mesh.html) which also supports
[CompositeCollider2D.edgeRadius](CompositeCollider2D-edgeRadius.html).  
  
Additional resources: [Collider2D.GetShapeHash](Collider2D.GetShapeHash.html).

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

