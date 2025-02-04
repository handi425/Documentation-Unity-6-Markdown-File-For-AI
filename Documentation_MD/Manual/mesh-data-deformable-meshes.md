[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/mesh-data-deformable-meshes.html)
  * [中文](/cn/current/Manual/mesh-data-deformable-meshes.html)
  * [日本語](/ja/current/Manual/mesh-data-deformable-meshes.html)
  * [한국어](/kr/current/Manual/mesh-data-deformable-meshes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/mesh-data-deformable-meshes.html)
  * [中文](/cn/current/Manual/mesh-data-deformable-meshes.html)
  * [日本語](/ja/current/Manual/mesh-data-deformable-meshes.html)
  * [한국어](/kr/current/Manual/mesh-data-deformable-meshes.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Get started with meshes](get-started-with-meshes.html)
  * [Mesh data](AnatomyofaMesh.html)
  * Mesh data for deformable meshes

[](mesh-index-data.html)

Mesh index data

[](view-mesh-data-visualizations.html)

View mesh data visualizations

# Mesh data for deformable meshes

Deformable meshes hold data specific to the deformation of the **mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh). Deformable meshes contain either:

  * Blend shapes: Data that describes different deformed versions of the mesh, for use with animation.
  * Bind poses: Data that describes the “base” pose of the skeleton in a skinned mesh.

## Blend shapes

Blend shapes describe versions of the mesh that are deformed into different
shapes. Unity interpolates between these shapes. You use blend shapes for
[morph target
animation](https://en.wikipedia.org/wiki/Morph_target_animation), which is a
common technique for facial animation.

Blend shape data is stored as blend shape vertices. Blend shape data is
“sparse”. This means that there isn’t a blend shape vertex for every mesh
vertex; there is only a corresponding blend shape vertex if the mesh vertex
deforms.

A blend shape vertex contains deltas for position, normal, and tangent, and an
index value. The meaning of the index value depends on how you request the
data.

In the `Mesh` class, you can access blend shape vertex data with
[Mesh.GetBlendShapeBuffer](../ScriptReference/Mesh.GetBlendShapeBuffer.html).
This returns a [GraphicsBuffer](../ScriptReference/GraphicsBuffer.html) that
provides access to the blend shape vertex data on the GPU. This method allows
you to choose between two different buffers; one that orders the data by blend
shape, and one that orders the data by mesh vertex. The choice of buffer
determines the meaning of the index value and the layout of the data in the
buffer. For more information on buffer layouts, see
[BlendShapeBufferLayout](../ScriptReference/Rendering.BlendShapeBufferLayout.html).

For information on using blend shapes with animations, see [Working with blend
shapes](BlendShapes.html).

This data is optional.

## Bind poses

In a skinned mesh, the **bind pose** of a bone describes its position when the
skeleton is in its default position (also called its bind pose or rest pose).

In the `Mesh` class, you can get and set this data with
[Mesh.bindposes](../ScriptReference/Mesh-bindposes.html). Each element
contains data for the bone with the same index.

This data is required for skinned meshes.

[](mesh-index-data.html)

Mesh index data

[](view-mesh-data-visualizations.html)

View mesh data visualizations

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

