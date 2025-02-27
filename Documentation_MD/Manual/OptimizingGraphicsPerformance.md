[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/OptimizingGraphicsPerformance.html)
  * [中文](/cn/current/Manual/OptimizingGraphicsPerformance.html)
  * [日本語](/ja/current/Manual/OptimizingGraphicsPerformance.html)
  * [한국어](/kr/current/Manual/OptimizingGraphicsPerformance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/OptimizingGraphicsPerformance.html)
  * [中文](/cn/current/Manual/OptimizingGraphicsPerformance.html)
  * [日本語](/ja/current/Manual/OptimizingGraphicsPerformance.html)
  * [한국어](/kr/current/Manual/OptimizingGraphicsPerformance.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * Reduce rendering work on the CPU or GPU

[](graphics-performance-profiling.html)

Graphics performance and profiling

[](reduce-draw-calls-landing.html)

Optimizing draw calls

# Reduce rendering work on the CPU or GPU

This page contains some simple guidelines for optimzing rendering performance
in your application.

## Before you begin: locate and understand the problem

Before you make any changes, you must profile your application to identify the
cause of the problem. If you attempt to solve a performance problem before you
understand its cause, you might waste your time or make the problem worse.
Additionally, rendering-related performance problems can occur on the CPU or
the GPU. Strategies for fixing these problems are quite different, so it’s
important to understand where your problem is before taking any action.

The following article on the Unity Learn site is a comprehensive introduction
to graphics performance, and contains information on identifying and fixing
problems: [Fixing performance
problems](https://learn.unity.com/tutorial/fixing-performance-
problems-2019-3). If you are not yet familiar with this subject, read the
article before following any of the advice on this page.

## Reducing the CPU cost of rendering

Usually, the greatest contributor to CPU rendering time is the cost of sending
rendering commands to the GPU. Rendering commands include draw calls (commands
to draw geometry), and commands to change the settings on the GPU before
drawing the geometry. If this is the case, consider these options:

  * You can reduce the number of objects that Unity renders. 
    * Consider reducing the overall number of objects in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene): for example, use a [skybox](sky-
landing.html)A special type of Material used to represent skies. Usually six-
sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) to create the effect of distant
geometry.

    * Perform more rigorous culling, so that Unity draws fewer objects. Consider using [occlusion culling](OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) to prevent Unity from
drawing objects that are hidden behind other objects, reducing the far clip
plane of a [Camera](class-Camera.html)A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) so that more distant objects fall
outside its frustum, or, for a more fine-grained approach, putting objects
into [separate layers](Layers.html) and setting up per-layer cull distances
with [Camera.layerCullDistances](../ScriptReference/Camera-
layerCullDistances.html).

  * You can reduce the number of times that Unity renders each object. 
    * Use [lightmapping](Lightmappers.html) to “bake” (pre-compute) lighting and shadows where appropriate. This increases build time, runtime memory usage and storage space, but can improve runtime performance.
    * If your application uses **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering), reduce the number of per-
pixel real-time lights that affect objects. For more information, see [Forward
rendering path](RenderTech-ForwardRendering.html).

    * Real-time shadows can be very resource-intensive, so use them sparingly and efficiently. For more information, see [Shadow troubleshooting: Shadow performance](ShadowPerformance.html).
    * If your application uses **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe), ensure that you optimize
their usage. For more information, see [Reflection Probe
performance](RefProbePerformance.html)

  * You can reduce the amount of work that Unity must do to prepare and send rendering commands, usually by sending them to the GPU in more efficient “batches”. There are a few different ways to achieve this: for more information, see [Optimizing draw calls](optimizing-draw-calls.html).

Many of these approaches will also reduce the work required on the GPU; for
example, reducing the overall number of objects that Unity renders in a frame
will result in a reduced workload for both the CPU and the GPU.

## Reducing the GPU cost of rendering

There are three main reasons why the GPU might fail to complete its work in
time to render a frame.

If an application is limited by fill rate, the GPU is trying to draw more
**pixels** The smallest unit in a computer image. Pixel size depends on your
screen resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) per frame than it can handle. If this
is the case, consider these options:

  * Identify and reduce overdraw in your application. The most common contributors to overdraw are overlapping transparent elements, such as **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), particles and **sprites** A 2D graphic
objects. If you are used to working in 3D, Sprites are essentially just
standard textures but there are special techniques for combining and managing
sprite textures for efficiency and convenience during development. [More
info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite). In the Unity Editor, use the
[Overdraw Draw mode](ViewModes.html) to identify areas where this is a
problem.

  * Reduce the execution cost of fragment shaders. For information about **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) performance, see the [Shader
Performance](SL-ShaderPerformance.html) page.

  * If you’re using Unity’s built-in shaders, pick ones from the **Mobile** or **Unlit** categories. They work on non-mobile platforms as well, but are simplified and approximated versions of the more complex shaders.
  * [Dynamic Resolution](DynamicResolution-landing.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html)  
See in [Glossary](Glossary.html#dynamicresolution) is a Unity feature that
allows you to dynamically scale individual render targets.

If an application is limited by memory bandwidth, the GPU is trying to read
and write more data to its dedicated memory than it can handle in a frame.
This usually means that that there are too many or textures, or that textures
are too large. If this is the case, consider these options:

  * Enable [mipmaps](class-TextureImporter.html) for textures whose distance from the camera varies at runtime (for example, most textures used in a 3D scene). This increases memory usage and storage space for these textures, but can improve runtime GPU performance.
  * Use suitable [compression formats](class-TextureImporter.html) to decrease the size of your textures in memory. This can result in faster load times, a smaller memory footprint, and improved GPU rendering performance. Compressed textures only use a fraction of the memory bandwidth needed for uncompressed textures.

If an appliction is limited by vertex processing, this means that the GPU is
trying to process more vertices than it can handle in a frame. If this is the
case, consider these options:

  * Reduce the execution cost of **vertex shaders** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader). For information about shader
performance, see the [Shader Performance](SL-ShaderPerformance.html) page.

  * Optimize your geometry: don’t use any more triangles than necessary, and try to keep the number of UV mapping seams and hard edges (doubled-up vertices) as low as possible. For more information, see [Creating models for optimal performance](ModelingOptimizedCharacters.html).
  * Use the [Level Of Detail](LevelOfDetail.html)The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#levelofdetail) system.

## Reducing the frequency of rendering

Sometimes, it might benefit your application to reduce the rendering frame
rate. This doesn’t reduce the CPU or GPU cost of rendering a single frame, but
it reduces the frequency with which Unity does so without affecting the
frequency of other operations (such as script execution).

You can reduce the rendering frame rate for parts of your application, or for
the whole application. Reducing the rendering frame rate to prevents
unnecessary power usage, prolongs battery life, and prevent device temperature
from rising to a point where the CPU frequency may be throttled. This is
particularly useful on handheld devices.

If profiling reveals that rendering consumes a significant proportion of the
resources for your application, consider which parts of your application might
benefit from this. Common use cases include menus or pause screens, turn based
games where the game is awaiting input, and applications where the content is
mostly static, such as automotive UI.

To prevent input lag, you can temporarily increase the rendering frame rate
for the duration of the input so that it still feels responsive.

To adjust the rendering frame rate, use the
[OnDemandRendering](../ScriptReference/Rendering.OnDemandRendering.html) API.
The API works particularly well with the [Adaptive Performance
package](https://docs.unity3d.com/Packages/com.unity.mobile.adaptiveperformance@latest).

_Note:_ **VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) applications don’t support On Demand
Rendering. Not rendering every frame causes the visuals to be out of sync with
head movement and might increase the risk of motion sickness.

## Additional resources

  * [Reduce rendering work on the GPU or CPU in URP](OptimizingGraphicsPerformance-urp.html)

[](graphics-performance-profiling.html)

Graphics performance and profiling

[](reduce-draw-calls-landing.html)

Optimizing draw calls

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

