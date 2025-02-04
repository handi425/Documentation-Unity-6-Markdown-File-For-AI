[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/mesh-vertex-data.html)
  * [中文](/cn/current/Manual/mesh-vertex-data.html)
  * [日本語](/ja/current/Manual/mesh-vertex-data.html)
  * [한국어](/kr/current/Manual/mesh-vertex-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/mesh-vertex-data.html)
  * [中文](/cn/current/Manual/mesh-vertex-data.html)
  * [日本語](/ja/current/Manual/mesh-vertex-data.html)
  * [한국어](/kr/current/Manual/mesh-vertex-data.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Get started with meshes](get-started-with-meshes.html)
  * [Mesh data](AnatomyofaMesh.html)
  * Mesh vertex data

[](AnatomyofaMesh.html)

Mesh data

[](mesh-topology-data.html)

Mesh topology data

# Mesh vertex data

The elements of vertex data are called **vertex attributes**.

Every vertex can have the following attributes:

  * Position
  * NormalThe direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](scripting-vectors.html)  
See in [Glossary](Glossary.html#Normal)

  * Tangent
  * Color
  * Up to 8 texture coordinates
  * Bone weights and blend indices (skinned meshes only)

Internally, all vertex data is stored in separate arrays of the same size. If
your **mesh** The main graphics primitive of Unity. Meshes make up a large
part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) contains an array with 10 vertex
positions, it also has arrays with 10 elements for each other vertex attribute
that it uses.

In C#, Unity describes the available vertex attributes with the
[VertexAttribute](../ScriptReference/Rendering.VertexAttribute.html) enum. You
can check whether an instance of the `Mesh` class has a given vertex attribute
with the
[Mesh.HasVertexAttribute](../ScriptReference/Mesh.HasVertexAttribute.html)
function.

## Position

The **vertex position** represents the position of the vertex in **object
space**.

Unity uses this value to determine the surface of the mesh.

This vertex attribute is required for all meshes.

In the `Mesh` class, the simplest way to access this data is with
[Mesh.GetVertices](../ScriptReference/Mesh.GetVertices.html) and
[Mesh.SetVertices](../ScriptReference/Mesh.SetVertices.html). Unity also
stores this data in [Mesh.vertices](../ScriptReference/Mesh-vertices.html),
but this older property is less efficient and user-friendly.

## Normal

The **vertex normal** represents the direction that points directly “out” from
the surface at the position of the vertex.

Unity uses this value to calculate the way that light reflects off the surface
of a mesh.

This vertex attribute is optional.

In the `Mesh` class, the simplest way to access this data is with
[Mesh.GetNormals](../ScriptReference/Mesh.GetNormals.html) and
[Mesh.SetNormals](../ScriptReference/Mesh.SetNormals.html). Unity also stores
this data in [Mesh.normals](../ScriptReference/Mesh-normals.html), but this
older property is less efficient and user-friendly.

## Tangent

The **vertex tangent** represents the direction that points along the “u”
(horizontal texture) axis of the surface at the position of the vertex.

Unity stores the vertex tangent with an additional piece of data, in a four-
component vector. The x,y,z components of the vector describe the tangent, and
the w component of the vector describes its
[orientation](https://en.wikipedia.org/wiki/Orientation_\(vector_space\)).
Unity uses the w value to compute the **binormal** , which is the cross
product of the tangent and normal.

Unity uses the tangent and binormal values in normal mapping.

This vertex attribute is optional.

In the `Mesh` class, the simplest way to access this data is with
[Mesh.GetTangents](../ScriptReference/Mesh.GetTangents.html) and
[Mesh.SetTangents](../ScriptReference/Mesh.SetTangents.html). Unity also
stores this data in [Mesh.tangents](../ScriptReference/Mesh-tangents.html),
but this older property is less efficient and user-friendly.

## Texture coordinates (UVs)

A mesh can contain up to eight sets of **texture coordinates**. Texture
coordinates are commonly called **UVs** , and the sets are called
**channels**.

Unity uses texture coordinates when it “wraps” a texture around the mesh. The
UVs indicate which part of the texture aligns with the mesh surface at the
vertex position.

UV channels are commonly called “UV0” for the first channel, “UV1” for the
second channel, and so on up to “UV7”. The channels respectively map to the
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) semantics `TEXCOORD0`, `TEXCOORD1`,
and so on up to `TEXCOORD7`.

By default, Unity uses the first channel (UV0) to store UVs for regular
textures such as diffuse maps and specular maps. Unity can use the second
channel (UV1) to store baked **lightmap** A pre-rendered texture that contains
the effects of light sources on static objects in the scene. Lightmaps are
overlaid on top of scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) UVs, and the third channel (UV2) to
store input data for real-time lightmap UVs. For more information on lightmap
UVs and how Unity uses these channels, see [Lightmap UVs](LightingGiUvs.html).

All eight texture coordinate attributes are optional.

In the `Mesh` class, the simplest way to access this data is with
[Mesh.GetUVs](../ScriptReference/Mesh.GetUVs.html) and
[Mesh.SetUVs](../ScriptReference/Mesh.SetUVs.html). Unity also stores this
data in the following properties: [Mesh.uv](../ScriptReference/Mesh-uv.html),
[Mesh.uv2](../ScriptReference/Mesh-uv2.html),
[Mesh.uv3](../ScriptReference/Mesh-uv3.html) and so on, up to
[Mesh.uv8](../ScriptReference/Mesh-uv8.html). Note that these older properties
are less efficient and user-friendly.

## Color

The **vertex color** represents the base color of a vertex, if any.

This color exists independently of any textures that the mesh may use.

This vertex attribute is optional.

In the `Mesh` class, the simplest way to access this data is with
[Mesh.GetColors](../ScriptReference/Mesh.GetColors.html) and
[Mesh.SetColors](../ScriptReference/Mesh.SetColors.html). Unity also stores
this data in [Mesh.colors](../ScriptReference/Mesh-colors.html), but this
older property is less efficient and user-friendly.

## Blend indices and bone weights

In a skinned mesh, **blend indices** indicate which bones affects a vertex,
and **bone weights** describe how much influence those bones have on the
vertex.

In Unity, these vertex attributes are stored together.

Unity uses blend indices and bone weights to deform a skinned mesh based on
the movement of its skeleton. For more information, see [Skinned Mesh
Renderer](class-SkinnedMeshRenderer.html).

These vertex attributes are required for skinned meshes.

In the past, Unity only allowed up to 4 bones to influence a vertex. It stored
this data in a [BoneWeight](../ScriptReference/BoneWeight.html) struct, in the
[Mesh.boneWeights](../ScriptReference/Mesh-boneWeights.html) array. Now, Unity
allows up to 256 bones to influence a vertex. It stores this data in a
[BoneWeight1](../ScriptReference/BoneWeight1.html) struct, and you can access
it with
[Mesh.GetAllBoneWeights](../ScriptReference/Mesh.GetAllBoneWeights.html) and
[Mesh.SetBoneWeights](../ScriptReference/Mesh.SetBoneWeights.html). For more
information, read the linked API documentation.

[](AnatomyofaMesh.html)

Mesh data

[](mesh-topology-data.html)

Mesh topology data

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

