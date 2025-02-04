[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RenderingStatistics.html)
  * [中文](/cn/current/Manual/RenderingStatistics.html)
  * [日本語](/ja/current/Manual/RenderingStatistics.html)
  * [한국어](/kr/current/Manual/RenderingStatistics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RenderingStatistics.html)
  * [中文](/cn/current/Manual/RenderingStatistics.html)
  * [日本語](/ja/current/Manual/RenderingStatistics.html)
  * [한국어](/kr/current/Manual/RenderingStatistics.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling reference](profiling-landing.html)
  * Rendering Statistics window reference

[](frame-debugger-window-event-information.html)

Frame Debugger Event Information reference

[](Audio.html)

Audio

# Rendering Statistics window reference

The Game view includes a Rendering Statistics window that displays real-time
rendering information about your application during Play mode. To open this
window, click the **Stats** button in the top right corner of the Game view.
Unity displays the Statistics window as an overlay in the top right of the
Game view. The rendering statistics shown in the Graphics section window are
useful for optimizing performance. The exact set of statistics available
varies according to the build target.

![Statistics window showing real-time rendering statistics.
](../uploads/Main/GameViewStats.png) Statistics window showing real-time
rendering statistics.

## **Statistics**

The Graphics section of the Statistics window contains the following
information:

**Statistic** | **Description**  
---|---  
****FPS** See first person shooter, frames per second.  
See in [Glossary](Glossary.html#FPS)** | The current number of frames Unity is able to draw per second.  
**CPU** |  **Main** : The total amount of time taken to process one frame. This number includes the time Unity takes to process the frame update of your application and the time Unity takes in the Editor to update the Scene view, other Editor Windows, or process Editor-only tasks.  
**Render** : The amount of time taken to render one frame. This number
includes the time Unity takes to process the frame update for the Game view;
it doesn’t include the time Unity takes in the Editor.  
**Batches** | The total number of [draw call batches](DrawCallBatching.html) Unity processes during a frame. This number includes static, dynamic, and [instance](GPUInstancing.html) batches.  
**Saved by batching** | The number of draw calls Unity combined into batches. To ensure good draw call batching, share materials between different ****GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)** as often as possible. Batches
group draw calls with the same render state, so changing the material causes
Unity to create a new batch.  
**Tris** | The number of [triangles](../ScriptReference/Mesh-triangles.html) Unity processes during a frame. This value is important when [optimizing for low-end hardware](OptimizingGraphicsPerformance.html).  
**Verts** | The number of [vertices](../ScriptReference/Mesh-vertices.html) Unity processes during a frame. This value is important when [optimizing for low-end hardware](OptimizingGraphicsPerformance.html).  
**Screen** | The resolution of the screen, along with the amount of memory the screen uses.  
**SetPass** | The number of times Unity switches which **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) pass it uses to render GameObjects
during a frame. A shader might contain several shader passes and each pass
renders GameObjects differently. Each pass requires Unity to bind a new
shader, which might introduce CPU overhead.  
**Shadow casters** | The number of GameObjects in the frame that cast shadows.  
**Visible skinned meshes** | The number of [Skinned Mesh Renderers](class-SkinnedMeshRenderer.html) in the frame.  
**Animation components playing** | The number of [Animation](class-Animation.html) components playing during the frame.  
****Animator components** A component on a model that animates that model
using the Animation system. The component has a reference to an Animator
Controller asset that controls the animation. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent) playing** | The number of [Animator](class-Animator.html) components playing during the frame.  
  
For more detailed information about your application’s rendering performance,
see the [Rendering module of the Profiler window](ProfilerRendering.html).

[](frame-debugger-window-event-information.html)

Frame Debugger Event Information reference

[](Audio.html)

Audio

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

