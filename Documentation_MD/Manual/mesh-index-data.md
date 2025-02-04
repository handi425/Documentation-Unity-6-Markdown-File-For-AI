[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/mesh-index-data.html)
  * [中文](/cn/current/Manual/mesh-index-data.html)
  * [日本語](/ja/current/Manual/mesh-index-data.html)
  * [한국어](/kr/current/Manual/mesh-index-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/mesh-index-data.html)
  * [中文](/cn/current/Manual/mesh-index-data.html)
  * [日本語](/ja/current/Manual/mesh-index-data.html)
  * [한국어](/kr/current/Manual/mesh-index-data.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Get started with meshes](get-started-with-meshes.html)
  * [Mesh data](AnatomyofaMesh.html)
  * Mesh index data

[](mesh-topology-data.html)

Mesh topology data

[](mesh-data-deformable-meshes.html)

Mesh data for deformable meshes

# Mesh index data

The index array contains integers that refer to elements in the vertex
positions array. These integers are called indices.

Unity uses the indices to connect the vertex positions into faces. The number
of indices that make up each face depends on the topology of the **mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh).

In the `Mesh` class, you can get this data with
[Mesh.GetIndices](../ScriptReference/Mesh.GetIndices.html), and set it with
[Mesh.SetIndices](../ScriptReference/Mesh.SetIndices.html). Unity also stores
this data in [Mesh.triangles](../ScriptReference/Mesh-triangles.html), but
this older property is less efficient and user-friendly.

**Note:** The Points topology doesn’t create faces; instead, Unity renders a
single point at each position. All other mesh topologies use more than one
index to create either faces or edges.

For example, for a mesh that has an index array that contains the following
values:

0,1,2,3,4,5

If the mesh has a triangular topology, then the first three elements (0,1,2)
identify one triangle, and the following three elements (3, 4, 5) identify
another triangle. There is no limit to the number of faces that a vertex can
contribute to. This means that the same vertex can appear in the index array
multiple times. For example, an index array could contain these values:

0,1,2,1,2,3

If the mesh has a triangular topology, then the first three elements (0,1,2)
identify one triangle, and the following three elements (1,2,3) identify
another triangle that shares vertices with the first.

## Winding order

The order of the vertices in each group in the index array is called the
**winding order**. Unity uses winding order to determine whether a face is
front-facing or back-facing, and in turn whether it should render a face or
cull it (exclude it from rendering). By default, Unity renders front-facing
polygons and culls back-facing polygons. Unity uses a clockwise winding order,
which means that Unity considers any face where the indices connect in a
clockwise direction is front facing.

![Unity’s winding order visualized on a prism](../uploads/Main/mesh-winding-
order.png) Unity’s winding order visualized on a prism

The above diagram demonstrates how Unity uses winding order. The order of the
vertices in each face determines the direction of the normal for that face and
Unity compares this to the forward direction of the current **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) perspective. If the normal points away
from the current camera’s forward direction, it is back-facing. The closer
triangle is ordered (1, 2, 3), which is a clockwise direction in relation to
the current perspective, so the triangle is front-facing. The further triangle
is ordered (4, 5, 6), which from this perspective is an anti-clockwise
direction, so the triangle is back-facing.

[](mesh-topology-data.html)

Mesh topology data

[](mesh-data-deformable-meshes.html)

Mesh data for deformable meshes

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

