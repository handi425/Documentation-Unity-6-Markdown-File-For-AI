[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LoadingTextureandMeshData-make-compatible.html)
  * [中文](/cn/current/Manual/LoadingTextureandMeshData-make-compatible.html)
  * [日本語](/ja/current/Manual/LoadingTextureandMeshData-make-compatible.html)
  * [한국어](/kr/current/Manual/LoadingTextureandMeshData-make-compatible.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LoadingTextureandMeshData-make-compatible.html)
  * [中文](/cn/current/Manual/LoadingTextureandMeshData-make-compatible.html)
  * [日本語](/ja/current/Manual/LoadingTextureandMeshData-make-compatible.html)
  * [한국어](/kr/current/Manual/LoadingTextureandMeshData-make-compatible.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Loading textures in the background](LoadingTextureandMeshData-introduction.html)
  * Make a texture compatible with asynchronous texture loading

[](LoadingTextureandMeshData.html)

Texture and mesh loading

[](TextureStreaming.html)

Optimizing GPU texture memory with mipmap streaming

# Make a texture compatible with asynchronous texture loading

A texture is eligible for the asynchronous upload pipeline if the following
conditions are met:

  * The texture is not read/write enabled.
  * The texture is not in the Resources folder.
  * If the build target is Android, LZ4 **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) is enabled in the [Build
Profiles](build-profiles.html)A set of customizable configuration settings to
use when creating a build for your target platform. [More info](build-
profiles.html)  
See in [Glossary](Glossary.html#Buildprofile) window.

Note that if you load a texture using `LoadImage(byte[] data)`, this forces
Unity to use the synchronous upload pipeline, even if the above conditions are
met.

A **mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) is eligible for the asynchronous upload
pipeline if the following conditions are met:

  * The mesh is not read/write enabled.
  * The mesh is not in the Resources folder.
  * The mesh has no [BlendShapes](../ScriptReference/Mesh-blendShapeCount.html).
  * Unity has not applied **Dynamic Batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) to the mesh, either because
the mesh is ineligible for Dynamic Batching or because Dynamic Batching is
disabled. For more information on Dynamic Batching, see [Draw call
batching](DrawCallBatching.html).

  * The mesh vertex/index data is not needed by a **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem), a **Terrain** The landscape
in your scene. A Terrain GameObject adds a large flat plane to your scene and
you can use the Terrain’s Inspector window to create a detailed landscape.
[More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain), or a Mesh **Collider** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider).

  * The mesh has no [bone weights](../ScriptReference/Mesh-boneWeights.html).
  * The mesh [topology](../ScriptReference/MeshTopology.html) is not [quads](../ScriptReference/MeshTopology.Quads.html)A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](PrimitiveObjects.html)  
See in [Glossary](Glossary.html#Quad).

  * The [meshCompression](../ScriptReference/ModelImporter-meshCompression.html) for the mesh asset is set to [Off](../ScriptReference/ModelImporterMeshCompression.Off.html). If the build target is Android, LZ4 compression is enabled in the [Build Profiles](build-profiles.html) window.

In all other circumstances, Unity loads textures and meshes synchronously.

[](LoadingTextureandMeshData.html)

Texture and mesh loading

[](TextureStreaming.html)

Optimizing GPU texture memory with mipmap streaming

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

