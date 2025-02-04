[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gpu-instancing-troubleshoot.html)
  * [中文](/cn/current/Manual/gpu-instancing-troubleshoot.html)
  * [日本語](/ja/current/Manual/gpu-instancing-troubleshoot.html)
  * [한국어](/kr/current/Manual/gpu-instancing-troubleshoot.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gpu-instancing-troubleshoot.html)
  * [中文](/cn/current/Manual/gpu-instancing-troubleshoot.html)
  * [日本語](/ja/current/Manual/gpu-instancing-troubleshoot.html)
  * [한국어](/kr/current/Manual/gpu-instancing-troubleshoot.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [GPU instancing](GPUInstancing-landing.html)
  * Troubleshooting GPU instancing

[](gpu-instancing-enable.html)

Enable GPU instancing

[](DrawCallBatching-landing.html)

Batching draw calls

# Troubleshooting GPU instancing

Meshes that have a low number of vertices can’t be processed efficiently using
GPU instancing because the GPU can’t distribute the work in a way that fully
uses the GPU’s resources. This processing inefficiency can have a detrimental
effect on performance. The threshold at which inefficiencies begin depends on
the GPU, but as a general rule, don’t use GPU instancing for meshes that have
fewer than 256 vertices.

If you want to render a **mesh** The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) with a low number of vertices many
times, best practice is to create a single buffer that contains all the mesh
information and use that to draw the meshes.

## Additional resources

  * [Make materials incompatible with the SRP Batcher in URP](SRPBatcher-Incompatible.html)

[](gpu-instancing-enable.html)

Enable GPU instancing

[](DrawCallBatching-landing.html)

Batching draw calls

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

