[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LevelOfDetail.html)
  * [中文](/cn/current/Manual/LevelOfDetail.html)
  * [日本語](/ja/current/Manual/LevelOfDetail.html)
  * [한국어](/kr/current/Manual/LevelOfDetail.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LevelOfDetail.html)
  * [中文](/cn/current/Manual/LevelOfDetail.html)
  * [日本語](/ja/current/Manual/LevelOfDetail.html)
  * [한국어](/kr/current/Manual/LevelOfDetail.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](simplifying-distant-meshes-with-level-of-detail-lod.html)
  * Mesh LOD

[](simplifying-distant-meshes-with-level-of-detail-lod.html)

Simplifying distant meshes with level of detail (LOD)

[](configure-mesh-lod.html)

Configure mesh LOD

# Mesh LOD

This page contains information on **level of detail** (LOD) for meshes. For
information on LOD for **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), see [SubShader LOD value](SL-
ShaderLOD.html).

Level of detail (LOD) is a technique that reduces the number of GPU operations
that Unity requires to render distant meshes.

When a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) is far away from the **Camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), you see less detail compared to when
the GameObject is close to the Camera. However, by default, Unity uses the
same number of triangles to render it at both distances. This can result in
wasted GPU operations, which can impact performance in your Scene.

The LOD technique allows Unity to reduce the number of triangles it renders
for a GameObject based on its distance from the Camera. To use it, a
GameObject must have a number of meshes with decreasing levels of detail in
its geometry. These meshes are called LOD levels. The farther a GameObject is
from the Camera, the lower-detail LOD level Unity renders. This technique
reduces the load on the hardware for these distant GameObjects, and can
therefore improve rendering performance.

To understand how to use LOD in Unity, you must first understand what LOD
levels are, and how they work.

## LOD levels

A LOD level is a **mesh** The main graphics primitive of Unity. Meshes make up
a large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) that defines the level of detail Unity
renders for a GameObject’s geometry. When a GameObject uses LOD, Unity
displays the appropriate LOD level for that GameObject based on the
GameObject’s distance from the Camera.

Each LOD level exists in a separate GameObject, each of which has a **Mesh
Renderer** A mesh component that takes the geometry from the Mesh Filter and
renders it at the position defined by the object’s Transform component. [More
info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) component that displays that LOD
level. For the very lowest level of detail, you can use a **Billboard** A
textured 2D object that rotates so that it always faces the Camera. [More
info](class-BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) Asset, which Unity displays instead
of a 3D mesh. Unity shows and hides these GameObjects as required. LOD levels
must be child GameObjects to the GameObject they relate to.

The images below demonstrate how the LOD levels change according to distance
from the Camera.

![At LOD 0, the Camera shows a mesh with a large number of small triangles. At
LOD 1, the Camera shows the mesh with far fewer triangles, which are much
larger in size.](../uploads/Main/LOD0Image.png) At LOD 0, the Camera shows a
mesh with a large number of small triangles. At LOD 1, the Camera shows the
mesh with far fewer triangles, which are much larger in size.

[](simplifying-distant-meshes-with-level-of-detail-lod.html)

Simplifying distant meshes with level of detail (LOD)

[](configure-mesh-lod.html)

Configure mesh LOD

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

