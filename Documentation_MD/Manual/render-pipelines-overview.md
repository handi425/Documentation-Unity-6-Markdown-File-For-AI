[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/render-pipelines-overview.html)
  * [中文](/cn/current/Manual/render-pipelines-overview.html)
  * [日本語](/ja/current/Manual/render-pipelines-overview.html)
  * [한국어](/kr/current/Manual/render-pipelines-overview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/render-pipelines-overview.html)
  * [中文](/cn/current/Manual/render-pipelines-overview.html)
  * [日本語](/ja/current/Manual/render-pipelines-overview.html)
  * [한국어](/kr/current/Manual/render-pipelines-overview.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * Introduction to render pipelines

[](render-pipelines.html)

Render pipelines

[](scriptable-render-pipeline-introduction.html)

Scriptable Render Pipeline fundamentals

# Introduction to render pipelines

A **render pipeline** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) takes the objects in a
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and displays them on-screen.

## How a render pipeline works

![](../uploads/Main/BestPracticeLightingPipeline3.svg)

A render pipeline follows these steps:

  1. Culling, where the pipeline decides which objects from the scene to display. This usually means it removes objects that are outside the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) view ([frustum
culling](https://docs.unity3d.com/Manual/UnderstandingFrustum.html)) or hidden
behind other objects ([occlusion
culling](https://docs.unity3d.com/Manual/OcclusionCulling.html)A process that
disables rendering GameObjects that are hidden (occluded) from the view of the
camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling)).

  2. Rendering, where the pipeline draws the objects with their correct lighting into **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) buffers.

  3. **Post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing), where the pipeline modifies
the pixel buffers to generate the final output frame for the display. Example
of modifications include color grading, bloom, and **depth of field** A post-
processing effect that simulates the focus properties of a camera lens. [More
info](PostProcessingOverview.html)  
See in [Glossary](Glossary.html#DepthofField).

A render pipeline repeats these steps each time Unity generates a new frame.

## Render pipelines in Unity

In Unity, you can choose between different render pipelines. Unity provides
three prebuilt render pipelines with different capabilities and performance
characteristics, or you can create your own.

The [Universal Render Pipeline (URP)](universal-render-pipeline.html) is a
Scriptable Render Pipeline that you can customize. It lets you create scalable
graphics across a wide range of platforms.

![](../uploads/Main/render-pipelines-overview-urp.jpg)

The [High Definition Render Pipeline (HDRP)](high-definition-render-
pipeline.html) is a Scriptable Render Pipeline that lets you create cutting-
edge, high-fidelity graphics on high-end platforms.

![](../uploads/Main/render-pipelines-overview-hdrp.jpg)

The [Built-In Render Pipeline](built-in-render-pipeline.html) is a general
purpose render pipeline with limited options for customization.

![](../uploads/Main/render-pipelines-overview-builtin.jpg)

The Scriptable Render Pipelines let you inspect and change how culling,
rendering, and post-processing work directly in C#. This level of
customization is also possible in the Built-In Render Pipeline when you
[purchase access to the Unity engine’s source
code](https://unity.com/products/source-code) in C++.

If you’re an experienced graphics developer with advanced customization needs,
you can also [create your own custom render
pipeline](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/manual/srp-custom.html) using Unity’s Scriptable Render
Pipeline API.

Refer to [Choose a render pipeline](choose-a-render-pipeline.html) for more
information about choosing the right pipeline for your project.

## Additional resources

  * [Introduction to Lighting and Rendering tutorial](https://learn.unity.com/tutorial/introduction-to-lighting-and-rendering-2019-3)

[](render-pipelines.html)

Render pipelines

[](scriptable-render-pipeline-introduction.html)

Scriptable Render Pipeline fundamentals

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

