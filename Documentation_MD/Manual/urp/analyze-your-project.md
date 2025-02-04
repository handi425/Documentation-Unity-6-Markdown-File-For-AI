[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/analyze-your-project.html)
  * [中文](/cn/current/Manual/urp/analyze-your-project.html)
  * [日本語](/ja/current/Manual/urp/analyze-your-project.html)
  * [한국어](/kr/current/Manual/urp/analyze-your-project.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/analyze-your-project.html)
  * [中文](/cn/current/Manual/urp/analyze-your-project.html)
  * [日本語](/ja/current/Manual/urp/analyze-your-project.html)
  * [한국어](/kr/current/Manual/urp/analyze-your-project.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Graphics performance and profiling](../graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](../graphics-performance-and-profiling-in-urp.html)
  * Analyze your project in URP

[](../urp/understand-performance.html)

Understand performance in URP

[](../OptimizingGraphicsPerformance-urp.html)

Reducing rendering work on the CPU or GPU in URP

# Analyze your project in URP

You can use the [Unity
Profiler](https://docs.unity3d.com/Manual/Profiler.html) to get data on the
performance of your project in areas such as the CPU and memory.

## Profiler markers

The following table lists markers that appear in the Unity **Profiler** A
window that helps you to optimize your game. It shows how much time is spent
in the various areas of your game. For example, it can report the percentage
of time spent rendering, animating, or in your game logic. [More
info](../Profiler.html)  
See in [Glossary](../Glossary.html#Profiler) for a URP frame and have a
significant effect on performance.

The table doesn’t include a marker if it’s deep in the Profiler hierarchy, or
the label already describes what URP does.

**Marker** | **Sub-marker** | **Description**  
---|---|---  
**Inl_UniversalRenderPipeline. RenderSingleCameraInternal** | URP builds a list of rendering commands in the [`ScriptableRenderContext`](https://docs.unity3d.com/ScriptReference/Rendering.ScriptableRenderContext.html), for a single **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera). URP only records rendering
commands in this marker, but doesn’t yet execute them. The marker includes the
camera name, for example **Main Camera**.  
| **Inl_ScriptableRenderer.Setup** | URP prepares for rendering, for example preparing **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture) for the camera and shadow
maps.  
| **CullScriptable** | URP generates a list of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) and lights to render, and culls
(excludes) any that are outside the camera’s view. The time this takes depends
on the number of GameObjects and lights in your **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).  
**Inl_ScriptableRenderContext.Submit** | URP submits the list of commands in the `ScriptableRenderContext` to the graphics API. This marker might appear more than once if URP submits commands more than once per frame, or you call [`ScriptableRenderContext.Submit`](https://docs.unity3d.com/ScriptReference/Rendering.ScriptableRenderContext.Submit.html) in your own code.  
| **MainLightShadow** | URP renders a [shadow map](https://docs.unity3d.com/Manual/shadow-mapping.html) for the main Directional Light.  
| **AdditionalLightsShadow** | URP renders shadow maps for other lights.  
| **UberPostProcess** | URP renders [post-processing effects](EffectList.html) you enable. This marker contains separate markers for some **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](../Glossary.html#post-processing) effects.  
| **RenderLoop.DrawSRPBatcher** | URP uses the [Scriptable Render Pipeline Batcher](https://docs.unity3d.com/Manual/SRPBatcher.html) to render one or more batches of objects.  
**CopyColor** | URP copies the color buffer from one render texture to another. You can disable **Opaque Texture** in the [URP Asset](universalrp-asset.html), so that URP only copies the color buffer if it needs to.  
**CopyDepth** | URP copies the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#depthbuffer) from one render texture to
another. You can disable **Depth Texture** in the [URP Asset](universalrp-
asset.html) unless you need the depth texture (for example, if you use a
shader that uses scene depth).  
**FinalBlit** | URP copies a render texture to the current camera render target.  
  
## Use a GPU profiler to analyze your project

You can use a platform GPU profiler such as
[Xcode](https://docs.unity3d.com/Manual/XcodeFrameDebuggerIntegration.html) to
get data on the performance of the GPU during rendering. You can also use a
profiler such as
[RenderDoc](https://docs.unity3d.com/Manual/RenderDocIntegration.html), but it
might provide less accurate performance data.

Data from a GPU profiler includes URP markers for rendering events, such as
different render passes.

## Use other tools to analyze your project

You can also use the following tools to analyze the performance of your
project:

  * [Scene view View Options](https://docs.unity3d.com/Manual/ViewModes.html)
  * [Rendering Debugger](features/rendering-debugger.html)
  * [Frame Debugger](https://docs.unity3d.com/Manual/frame-debugger-window.html)
  * [Graphics performance and profiling reference](../profiling-landing.html)

[](../urp/understand-performance.html)

Understand performance in URP

[](../OptimizingGraphicsPerformance-urp.html)

Reducing rendering work on the CPU or GPU in URP

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

