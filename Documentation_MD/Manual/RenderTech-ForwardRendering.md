[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RenderTech-ForwardRendering.html)
  * [中文](/cn/current/Manual/RenderTech-ForwardRendering.html)
  * [日本語](/ja/current/Manual/RenderTech-ForwardRendering.html)
  * [한국어](/kr/current/Manual/RenderTech-ForwardRendering.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RenderTech-ForwardRendering.html)
  * [中文](/cn/current/Manual/RenderTech-ForwardRendering.html)
  * [日本語](/ja/current/Manual/RenderTech-ForwardRendering.html)
  * [한국어](/kr/current/Manual/RenderTech-ForwardRendering.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * [Rendering paths in the Built-In Render Pipeline](built-in-rendering-paths.html)
  * Forward rendering path in the Built-In Render Pipeline

[](RenderingPaths.html)

Introduction to rendering paths in the Built-In Render Pipeline

[](RenderTech-DeferredShading.html)

Deferred rendering path in the Built-In Render Pipeline

# Forward rendering path in the Built-In Render Pipeline

The Forward **rendering path** The technique that a render pipeline uses to
render graphics. Choosing a different rendering path affects how lighting and
shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) renders each **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in one or more render passes,
depending on the lights that affect the object.

Lights themselves are also treated differently by the **Forward rendering**
path, depending on their settings and intensity. For more information, refer
to [Per-pixel and per-vertex lights](PerPixelLights-BuiltIn.html).

## Render passes

For each GameObject, Unity first renders the Base Pass, which renders the
following:

  * One per-pixel light that affects the GameObject.
  * All the per-vertex and spherical harmonics (SH) lights that affect the GameObject.
  * **Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) data for the GameObject

  * Ambient lighting
  * Emissive lighting
  * Shadows from directional lights

**Note:** Lightmapped objects don’t receive lighting from SH lights.

Unity then renders one Additional Pass for each per-pixel light that affects
the GameObject. Unity doesn’t render shadows for these lights.

## Additional resources

  * [Introduction to rendering paths](rendering-paths-introduction.html)
  * [Per-pixel and per-vertex lights](PerPixelLights-BuiltIn.html)

[](RenderingPaths.html)

Introduction to rendering paths in the Built-In Render Pipeline

[](RenderTech-DeferredShading.html)

Deferred rendering path in the Built-In Render Pipeline

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

