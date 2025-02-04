[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/identify-mesh-upload-pipeline.html)
  * [中文](/cn/current/Manual/identify-mesh-upload-pipeline.html)
  * [日本語](/ja/current/Manual/identify-mesh-upload-pipeline.html)
  * [한국어](/kr/current/Manual/identify-mesh-upload-pipeline.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/identify-mesh-upload-pipeline.html)
  * [中文](/cn/current/Manual/identify-mesh-upload-pipeline.html)
  * [日本語](/ja/current/Manual/identify-mesh-upload-pipeline.html)
  * [한국어](/kr/current/Manual/identify-mesh-upload-pipeline.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Loading texture and mesh data asynchronously](loading-texture-mesh-data-asynchronously.html)
  * Check whether a mesh uses the asynchronous upload pipeline

[](LoadingTextureandMeshData.html)

Texture and mesh loading

[](configure-asynchronous-upload-pipeline.html)

Configure the asynchronous upload pipeline

# Check whether a mesh uses the asynchronous upload pipeline

To identify which upload pipeline Unity is using for a **mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), you can use the
[Profiler](Profiler.html)A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) or another profiling tool and
observe thread activity and **profiler markers** Placed in code to describe a
CPU or GPU event that is then displayed in the Unity Profiler window. Added to
Unity code by default, or you can use [ProfilerMarker
API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-
guide.html) to add your own custom markers. [More info](profiler-markers.html)  
See in [Glossary](Glossary.html#Profilermarker).

The following indicate that Unity is using the asynchronous upload pipeline to
upload textures or meshes:

  * The `AsyncUploadManager.ScheduleAsyncRead`, `AsyncReadManager.ReadFile`, and `Async.DirectTextureLoadBegin` profiler markers.
  * Activity on the `AsyncRead` thread.

If you do not see this activity, then Unity is not using the asynchronous
upload pipeline.

Note that the following profiler markers do not indicate that Unity is using
the asynchronous upload pipeline; Unity calls them to check whether any
asynchronous upload work needs to occur:

  * `Initialization.AsyncUploadTimeSlicedUpdate`
  * `AsyncUploadManager.AsyncResourceUpload`
  * `AsyncUploadManager.ScheduleAsyncCommands`

[](LoadingTextureandMeshData.html)

Texture and mesh loading

[](configure-asynchronous-upload-pipeline.html)

Configure the asynchronous upload pipeline

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

