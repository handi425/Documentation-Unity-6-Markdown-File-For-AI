[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/reduce-rendering-work-on-cpu.html)
  * [中文](/cn/current/Manual/urp/reduce-rendering-work-on-cpu.html)
  * [日本語](/ja/current/Manual/urp/reduce-rendering-work-on-cpu.html)
  * [한국어](/kr/current/Manual/urp/reduce-rendering-work-on-cpu.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/reduce-rendering-work-on-cpu.html)
  * [中文](/cn/current/Manual/urp/reduce-rendering-work-on-cpu.html)
  * [日本語](/ja/current/Manual/urp/reduce-rendering-work-on-cpu.html)
  * [한국어](/kr/current/Manual/urp/reduce-rendering-work-on-cpu.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Graphics performance and profiling](../graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](../graphics-performance-and-profiling-in-urp.html)
  * [Reducing rendering work on the CPU or GPU in URP](../OptimizingGraphicsPerformance-urp.html)
  * Reducing rendering work on the CPU in URP

[](../OptimizingGraphicsPerformance-urp.html)

Reducing rendering work on the CPU or GPU in URP

[](../urp/gpu-resident-drawer.html)

Enable the GPU Resident Drawer in URP

# Reducing rendering work on the CPU in URP

You can use the GPU Resident Drawer or GPU **occlusion culling** A process
that disables rendering GameObjects that are hidden (occluded) from the view
of the camera. [More info](../OcclusionCulling.html)  
See in [Glossary](../Glossary.html#Occlusionculling) to speed up rendering.
When you enable these features, Unity optimizes the rendering pipeline so the
CPU has less work to do each frame, and the GPU draws **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) more efficiently.

**Page** | **Description**  
---|---  
[Enable the GPU Resident Drawer](gpu-resident-drawer.html) | Automatically use the `BatchRendererGroup` API to use instancing and reduce the number of draw calls.  
[Make a GameObject compatible with the GPU Resident Drawer](make-object-compatible-gpu-rendering.html) | Include or exclude a GameObject from the GPU Resident Drawer.  
[Enable GPU occlusion culling](gpu-culling.html) | Use the GPU instead of the CPU to exclude GameObjects from rendering when they’re occluded behind other GameObjects.  
  
## Additional resources

  * [Graphics performance fundamentals](https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html)

[](../OptimizingGraphicsPerformance-urp.html)

Reducing rendering work on the CPU or GPU in URP

[](../urp/gpu-resident-drawer.html)

Enable the GPU Resident Drawer in URP

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

