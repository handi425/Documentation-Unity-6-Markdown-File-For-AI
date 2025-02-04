[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/mesh-topology-data.html)
  * [中文](/cn/current/Manual/mesh-topology-data.html)
  * [日本語](/ja/current/Manual/mesh-topology-data.html)
  * [한국어](/kr/current/Manual/mesh-topology-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/mesh-topology-data.html)
  * [中文](/cn/current/Manual/mesh-topology-data.html)
  * [日本語](/ja/current/Manual/mesh-topology-data.html)
  * [한국어](/kr/current/Manual/mesh-topology-data.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Get started with meshes](get-started-with-meshes.html)
  * [Mesh data](AnatomyofaMesh.html)
  * Mesh topology data

[](mesh-vertex-data.html)

Mesh vertex data

[](mesh-index-data.html)

Mesh index data

# Mesh topology data

Topology describes the type of face that a **mesh** The main graphics
primitive of Unity. Meshes make up a large part of your 3D worlds. Unity
supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv
surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) has.

A mesh’s topology defines the structure of the index buffer, which in turn
describes how the vertex positions combine into faces. Each type of topology
uses a different number of elements in the index array to define a single
face.

Unity supports the following mesh topologies:

  * Triangle
  * Quad
  * Lines
  * LineStrip
  * Points

**Note:** The Points topology doesn’t create faces; instead, Unity renders a
single point at each position. All other mesh topologies use more than one
index to create either faces or edges.

In the `Mesh` class, you can get the topology with
[Mesh.GetTopology](../ScriptReference/Mesh.GetTopology.html), and set it as a
parameter of [Mesh.SetIndices](../ScriptReference/Mesh.SetIndices.html).

For more information on supported mesh topologies, see the documentation for
the MeshTopology enum.

**Note:** You must convert any meshes that use other modelling techniques
(such as NURBS or NURMS/Subdivision Surfaces modelling) into supported formats
in your modelling software before you can use them in Unity.

[](mesh-vertex-data.html)

Mesh vertex data

[](mesh-index-data.html)

Mesh index data

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

