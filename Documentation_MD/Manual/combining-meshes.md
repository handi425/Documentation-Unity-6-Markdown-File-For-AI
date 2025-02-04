[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/combining-meshes.html)
  * [中文](/cn/current/Manual/combining-meshes.html)
  * [日本語](/ja/current/Manual/combining-meshes.html)
  * [한국어](/kr/current/Manual/combining-meshes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/combining-meshes.html)
  * [中文](/cn/current/Manual/combining-meshes.html)
  * [日本語](/ja/current/Manual/combining-meshes.html)
  * [한국어](/kr/current/Manual/combining-meshes.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * Combine meshes manually

[](dynamic-batching-enable.html)

Enable dynamic batching

[](profile-rendering.html)

Profile rendering

# Combine meshes manually

You can manually combine multiple meshes into a single **mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) as a [draw call
optimization](optimizing-draw-calls.html) technique. Unity renders the
combined mesh in a single draw call instead of one draw call per mesh. This
technique can be a good alternative to [draw call
batching](DrawCallBatching.html) in cases where the meshes are close together
and don’t move relative to one another. For example, for a static cupboard
with lots of drawers, it makes sense to combine everything into a single mesh.

**Warning** : Unity can’t individually cull meshes you combine. This means
that if one part of a combined mesh is onscreen, Unity draws the entire
combined mesh. If the meshes are static and you want Unity to individually
cull them, use [static batching](static-batching.html)A technique Unity uses
to draw GameObjects on the screen that combines static (non-moving)
GameObjects into big Meshes, and renders them in a faster way. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching) instead.

There are two main ways to combine meshes:

  * In your asset generation tool while authoring the mesh.
  * In Unity using [Mesh.CombineMeshes](../ScriptReference/Mesh.CombineMeshes.html).

[](dynamic-batching-enable.html)

Enable dynamic batching

[](profile-rendering.html)

Profile rendering

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

