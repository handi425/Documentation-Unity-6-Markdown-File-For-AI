[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/gpu-resident-drawer.html)
  * [中文](/cn/current/Manual/urp/gpu-resident-drawer.html)
  * [日本語](/ja/current/Manual/urp/gpu-resident-drawer.html)
  * [한국어](/kr/current/Manual/urp/gpu-resident-drawer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/gpu-resident-drawer.html)
  * [中文](/cn/current/Manual/urp/gpu-resident-drawer.html)
  * [日本語](/ja/current/Manual/urp/gpu-resident-drawer.html)
  * [한국어](/kr/current/Manual/urp/gpu-resident-drawer.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Graphics performance and profiling](../graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](../graphics-performance-and-profiling-in-urp.html)
  * [Reducing rendering work on the CPU or GPU in URP](../OptimizingGraphicsPerformance-urp.html)
  * [Reducing rendering work on the CPU in URP](../urp/reduce-rendering-work-on-cpu.html)
  * Enable the GPU Resident Drawer in URP

[](../urp/reduce-rendering-work-on-cpu.html)

Reducing rendering work on the CPU in URP

[](../urp/make-object-compatible-gpu-rendering.html)

Make a GameObject compatible with the GPU Resident Drawer in URP

# Enable the GPU Resident Drawer in URP

The GPU Resident Drawer automatically uses the
[`BatchRendererGroup`](https://docs.unity3d.com/Manual/batch-renderer-
group.html) API to draw **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) with GPU instancing, which
reduces the number of draw calls and frees CPU processing time. For more
information, refer to [How BatchRendererGroup
works](https://docs.unity3d.com/Manual/batch-renderer-group-how.html).

The GPU Resident Drawer works only with the following:

  * The [Forward+](rendering/forward-rendering-paths.html) **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath).

  * [Graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html) and platforms that support compute **shaders** A program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), except OpenGL ES.

  * GameObjects that have a [Mesh Renderer component](https://docs.unity3d.com/Manual/class-MeshRenderer.html).

Otherwise, Unity falls back to drawing the GameObject without GPU instancing.

If you enable the GPU Resident Drawer, the following applies:

  * Build times are longer because Unity compiles all the `BatchRendererGroup` shader variants into your build.

## Enable the GPU Resident Drawer

Follow these steps:

  1. Go to **Project Settings** > **Graphics** , then in the **Shader Stripping** section set **BatchRendererGroup Variants** to **Keep All**.
  2. Go to the active [URP Asset](universalrp-asset.html) and enable **SRP Batcher**.
  3. Double-click the renderer in the **Renderer List** to open the Universal Renderer, then set **Rendering Path** to **Forward+**.
  4. Set **GPU Resident Drawer** to **Instanced Drawing**.

If you change or create GameObjects each frame, the GPU Resident Drawer
updates with the changes.

To include or exclude GameObjects from the GPU Resident Drawer, refer to [Make
a GameObject compatible with the GPU Resident Drawer](make-object-compatible-
gpu-rendering.html).

## Analyze the GPU Resident Drawer

To analyze the results of the GPU Resident Drawer, you can use the following:

  * [Frame Debugger](https://docs.unity3d.com/Manual/FrameDebugger.html). The GPU Resident Drawer groups GameObjects into draw calls with the name **Hybrid Batch Group**.
  * [Rendering Debugger](features/rendering-debugger-reference.html).
  * [Rendering Statistics](https://docs.unity3d.com/Manual/RenderingStatistics.html) to check if the number of **frames per second** The frequency at which consecutive frames are displayed in a running game. [More info](../RenderingStatistics.html)  
See in [Glossary](../Glossary.html#framespersecond) increases, and the CPU
processing time and SetPass calls decreases.

  * [Unity Profiler](optimize-for-better-performance.html)

## Optimize the GPU Resident Drawer

How much the GPU Resident Drawer speeds up rendering depends on your **scene**
A Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). The GPU Resident Drawer is most
effective in the following setups:

  * The scene is large.
  * Multiple GameObjects use the same **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](../mesh.html)  
See in [Glossary](../Glossary.html#Mesh), so Unity can group them into a
single draw call.

Rendering usually speeds up less in the **Scene view** An interactive view
into the world you are creating. You use the Scene View to select and position
scenery, characters, cameras, lights, and all other types of Game Object.
[More info](../UsingTheSceneView.html)  
See in [Glossary](../Glossary.html#SceneView) and the Game view, compared to
Play mode or your final built project.

The following might speed up the GPU Resident Drawer:

  * Go to **Project Settings** > **Player** , then in the **Other Settings** section disable **Static Batching**.
  * Go to **Window** > **Panels** > **Lighting** , then in the **Lightmapping Settings** section enable **Fixed Lightmap Size** and disable **Use Mipmap Limits**.

## Additional resources

  * [Reduce rendering work on the CPU](reduce-rendering-work-on-cpu.html)
  * [Graphics performance fundamentals](https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html)
  * [GPU occlusion culling](gpu-culling.html)

[](../urp/reduce-rendering-work-on-cpu.html)

Reducing rendering work on the CPU in URP

[](../urp/make-object-compatible-gpu-rendering.html)

Make a GameObject compatible with the GPU Resident Drawer in URP

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

