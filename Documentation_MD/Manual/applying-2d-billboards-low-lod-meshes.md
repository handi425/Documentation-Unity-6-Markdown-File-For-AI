[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/applying-2d-billboards-low-lod-meshes.html)
  * [中文](/cn/current/Manual/applying-2d-billboards-low-lod-meshes.html)
  * [日本語](/ja/current/Manual/applying-2d-billboards-low-lod-meshes.html)
  * [한국어](/kr/current/Manual/applying-2d-billboards-low-lod-meshes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/applying-2d-billboards-low-lod-meshes.html)
  * [中文](/cn/current/Manual/applying-2d-billboards-low-lod-meshes.html)
  * [日本語](/ja/current/Manual/applying-2d-billboards-low-lod-meshes.html)
  * [한국어](/kr/current/Manual/applying-2d-billboards-low-lod-meshes.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](simplifying-distant-meshes-with-level-of-detail-lod.html)
  * [2D images for low level of detail (LOD)](2d-images-lod.html)
  * Applying 2D billboards for low LOD meshes

[](2d-images-lod.html)

2D images for low level of detail (LOD)

[](class-BillboardRenderer.html)

Billboard Renderer component reference

# Applying 2D billboards for low LOD meshes

Billboards are a level-of-detail (LOD) method for drawing complicated 3D
Meshes in a simpler way when they are far away from the **Camera** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). When a **Mesh** The main graphics
primitive of Unity. Meshes make up a large part of your 3D worlds. Unity
supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv
surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) is far away from the Camera, its size on
screen means there is no need to draw it in full detail. Instead, you can
replace the complex 3D Mesh with a 2D **billboard** A textured 2D object that
rotates so that it always faces the Camera. [More info](class-
BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) representation.

The [Billboard Renderer](class-BillboardRenderer.html) renders [Billboard
assets](class-BillboardAsset.html).

A Billboard asset is a collection of pre-rendered images of a mesh. Use it
with the [Billboard Renderer](class-BillboardRenderer.html) to an object that
is distant from the Camera at a low [level of detail
(LOD)](LevelOfDetail.html).

The most common way to generate a Billboard Asset is to create files in
[SpeedTree Modeler](https://unity.com/products/speedtree), and then import
them into Unity.

It is also possible to create your own Billboard Assets from script. For more
information, see the API reference for
[BillboardAsset](../ScriptReference/BillboardAsset.html).

Certain features, such as SpeedTree, export Billboard Assets, but you can also
create them yourself. For information on how to create a Billboard Asset, see
the [BillboardAssets](class-BillboardAsset.html) Manual page and the
[BillboardAsset](../ScriptReference/BillboardAsset.html) Script reference
page.

[](2d-images-lod.html)

2D images for low level of detail (LOD)

[](class-BillboardRenderer.html)

Billboard Renderer component reference

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

