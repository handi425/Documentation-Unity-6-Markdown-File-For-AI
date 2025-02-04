[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LoadingTextureandMeshData.html)
  * [中文](/cn/current/Manual/LoadingTextureandMeshData.html)
  * [日本語](/ja/current/Manual/LoadingTextureandMeshData.html)
  * [한국어](/kr/current/Manual/LoadingTextureandMeshData.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LoadingTextureandMeshData.html)
  * [中文](/cn/current/Manual/LoadingTextureandMeshData.html)
  * [日本語](/ja/current/Manual/LoadingTextureandMeshData.html)
  * [한국어](/kr/current/Manual/LoadingTextureandMeshData.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Loading texture and mesh data asynchronously](loading-texture-mesh-data-asynchronously.html)
  * Texture and mesh loading

[](loading-texture-mesh-data-asynchronously.html)

Loading texture and mesh data asynchronously

[](identify-mesh-upload-pipeline.html)

Check whether a mesh uses the asynchronous upload pipeline

# Texture and mesh loading

Unity can load texture and **mesh** The main graphics primitive of Unity.
Meshes make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) data from disk and upload it to the GPU
in two different ways: synchronously or asynchronously. These two processes
are called the synchronous upload pipeline and the asynchronous upload
pipeline.

When Unity uses the synchronous upload pipeline, it cannot perform other tasks
while it loads and uploads the data. This can cause visible pauses in your
application. When Unity uses the asynchronous upload pipeline, it can perform
other tasks while it loads and uploads the data in the background.

If a texture or mesh is eligible for the asynchronous upload pipeline, Unity
uses the asynchronous upload pipeline automatically. If a texture or mesh is
ineligible for the asynchronous upload pipeline, Unity uses the synchronous
upload pipeline automatically.

## How it works

The main difference between the synchronous and asynchronous upload pipelines
is where Unity saves the data at build time, which affects how Unity loads it
at runtime.

In the synchronous upload pipeline, Unity must load both the metadata (header
data) and the texel or vertex data (binary data) for the texture or mesh in a
single frame. In the asynchronous upload pipeline, Unity must load only the
header data in a single frame, and it can stream the binary data to the GPU
over subsequent frames.

In the synchronous upload pipeline:

  * At build time, Unity writes both the header and the binary data for the mesh or texture to the same .res file.
  * At runtime, when the application needs the texture or mesh, Unity loads both the header data and binary data for that texture or mesh from the .res file into memory. When all of the data is in memory, Unity then uploads the binary data from memory to the GPU. The loading and uploading operations occur mainly on the main thread, in a single frame.

In the asynchronous upload pipeline:

  * At build time, Unity writes the header data to a .res file and the binary data to a separate .resS file.
  * At runtime, when the application needs the texture or mesh, Unity loads the header from the .res file into memory. When the header is in memory, Unity then streams the binary data from the .resS file to the GPU using a fixed-sized ring buffer. Unity streams the binary data using multiple threads, over the course of several frames. Note that on some console platforms where Unity already knows the GPU hardware, Unity skips the ring buffer and loads straight into the GPU memory.

## Additional resources

  * Unity blog: [Optimizing loading performance: Understanding the Async Upload Pipeline](https://unity.com/blog/engine-platform/understanding-the-async-upload-pipeline).

[](loading-texture-mesh-data-asynchronously.html)

Loading texture and mesh data asynchronously

[](identify-mesh-upload-pipeline.html)

Check whether a mesh uses the asynchronous upload pipeline

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

