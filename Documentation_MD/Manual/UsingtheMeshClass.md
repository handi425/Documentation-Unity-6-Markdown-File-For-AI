[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UsingtheMeshClass.html)
  * [中文](/cn/current/Manual/UsingtheMeshClass.html)
  * [日本語](/ja/current/Manual/UsingtheMeshClass.html)
  * [한국어](/kr/current/Manual/UsingtheMeshClass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UsingtheMeshClass.html)
  * [中文](/cn/current/Manual/UsingtheMeshClass.html)
  * [日本語](/ja/current/Manual/UsingtheMeshClass.html)
  * [한국어](/kr/current/Manual/UsingtheMeshClass.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Creating and accessing meshes via script](creating-meshes.html)
  * Access meshes via the Mesh API

[](create-mesh.html)

Create a mesh

[](Example-CreatingaBillboardPlane.html)

Create a quad mesh via script

# Access meshes via the Mesh API

The [Mesh](../ScriptReference/Mesh.html)The main graphics primitive of Unity.
Meshes make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) class is the basic script interface to
an object’s mesh geometry. It uses arrays to represent the triangles, vertex
positions, normals and texture coordinates and also supplies a number of other
useful properties and functions to assist mesh generation.

## Access an object’s Mesh

The mesh data is attached to an object using the [Mesh Filter](class-
MeshFilter.html)A mesh component that takes a mesh from your assets and passes
it to the Mesh Renderer for rendering on the screen. [More info](class-
MeshFilter.html)  
See in [Glossary](Glossary.html#MeshFilter) component (and the object will
also need a [MeshRenderer](class-MeshRenderer.html) to make the geometry
visible). This component is accessed using the familiar GetComponent function:

    
    
    using UnityEngine;
    public class ExampleScript : MonoBehaviour
    {
        MeshFilter mf;
        void Start()
        {
            //if this gameObject has a MeshFilter, mf will reference the component
            mf = GetComponent<MeshFilter>();    
        }
    }
    

## Add mesh data

The Mesh object has properties for the vertices and their associated data
(normals and UV coordinates) and also for the triangle data. The vertices may
be supplied in any order but the arrays of normals and UVs must be ordered so
that the indices all correspond with the vertices (ie, element 0 of the
normals array supplies the normal for vertex 0, etc). The vertices are
[Vector3s](../ScriptReference/Vector3.html) representing points in the
object’s local space. The normals are normalised Vector3s representing the
directions, again in local coordinates. The UVs are specified as
[Vector2s](../ScriptReference/Vector2.html), but since the Vector2 type
doesn’t have fields called U and V, you must mentally convert them to X and Y
respectively.

The triangles are specified as triples of integers that act as indices into
the vertex array. Rather than use a special class to represent a triangle the
array is just a simple list of integer indices. These are taken in groups of
three for each triangle, so the first three elements define the first
triangle, the next three define the second triangle, and so on. An important
detail of the triangles is the ordering of the corner vertices. They should be
arranged so that the corners go around clockwise as you look down on the
visible outer surface of the triangle, although it doesn’t matter which corner
you start with.

### Work with raw mesh data

The [Mesh](../ScriptReference/Mesh.html) class also has a lower-level advanced
API that enables you to work with raw mesh vertex and index buffer data. This
is useful in situations that require maximum performance or the lowest amount
of memory allocations.

  * [Mesh.SetIndexBufferParams](../ScriptReference/Mesh.SetIndexBufferParams.html) and [Mesh.SetIndexBufferData](../ScriptReference/Mesh.SetIndexBufferData.html) for setting up size, format of the index buffer, and updating data inside it.
  * [Mesh.SetVertexBufferParams](../ScriptReference/Mesh.SetVertexBufferParams.html) and [Mesh.SetVertexBufferData](../ScriptReference/Mesh.SetVertexBufferData.html) for setting up size, format of the vertex buffer(s), and updating data inside them.
  * [Mesh.SetSubMesh](../ScriptReference/Mesh.SetSubMesh.html) for setting up index buffer topology and ranges.

## Additional resources

  * [Mesh data](AnatomyofaMesh.html) documentation.
  * [Mesh](../ScriptReference/Mesh.html) API reference.

[](create-mesh.html)

Create a mesh

[](Example-CreatingaBillboardPlane.html)

Create a quad mesh via script

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

