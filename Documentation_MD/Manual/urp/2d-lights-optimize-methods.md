[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2d-lights-optimize-methods.html)
  * [中文](/cn/current/Manual/urp/2d-lights-optimize-methods.html)
  * [日本語](/ja/current/Manual/urp/2d-lights-optimize-methods.html)
  * [한국어](/kr/current/Manual/urp/2d-lights-optimize-methods.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2d-lights-optimize-methods.html)
  * [中文](/cn/current/Manual/urp/2d-lights-optimize-methods.html)
  * [日本語](/ja/current/Manual/urp/2d-lights-optimize-methods.html)
  * [한국어](/kr/current/Manual/urp/2d-lights-optimize-methods.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Optimizing 2D lights](../urp/2d-light-optimize.html)
  * Optimize 2D lights

[](../urp/2d-light-optimize.html)

Optimizing 2D lights

[](../urp/2d-light-batching-intro.html)

Introduction to 2D light batching

# Optimize 2D lights

In addition to the standard optimization techniques such as reducing draw
calls, culling and optimizing **shaders** A program that runs on the GPU.
[More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), there are several techniques and
considerations that are unique to the 2D Lighting graphics pipeline.

## Number of blend styles

The easiest way to increase rendering performance is to reduce the number of
blend styles used. Each blend style is a **Render Texture** A special type of
Texture that is created and updated at runtime. To use them, first create a
new Render Texture and designate one of your Cameras to render into it. Then
you can use the Render Texture in a Material just like a regular Texture.
[More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture) that needs to be rendered
and subsequently uploaded.

Reducing the number of blend styles has a direct impact on the performance.
For simple scenes a single blend style could suffice. It is also common to use
up to 2 blend styles in a **scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

## Light Render Texture scale

The 2D Lighting system relies on screen space Light Render Texture to capture
light contribution. This means there are a lot of Render Texture drawing
subsequent uploading. Choosing the right Render Texture size directly impacts
the performance.

By default it is set at 0.5x of screen resolution. Smaller Light Render
Texture size will give better performance at the cost of visual artifact. Half
screen size resolution provides a good performance with almost no noticeable
artifact in most situations.

Experiment and find a scale suitable for your project.

## Layer Batching

To further reduce the number of Light Render Textures, it is crucial to make
the Sorting Layer batchable. Layers that are batched together share the same
set of Light Render Textures. Uniquely lit layers will have its own set thus
increasing the amount of work needed.

Layers can be batch together if they share the same set of lights.

## Pre-rendering of Light Render Texture

Multiple sets of Light Render Textures can be rendered ahead of drawing the
Renderers. In an ideal situation, all the Light Render Textures will be
rendered upfront and only then will the pipeline proceed with drawing the
Renderers onto the final color output. This reduces the need to
load/unload/reload of final color output.

In a very complex setup with many distinctly lit Layers, it may not be
practical to pre-render all Light Render Textures. The limit can be configured
in the 2D Renderer Data **inspector** A Unity window that displays information
about the currently selected GameObject, asset or project settings, allowing
you to inspect and edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector).

## Normal Maps

Using **normal maps** A type of Bump Map texture that allows you to add
surface detail such as bumps, grooves, and scratches to a model which catch
the light as if they are represented by real geometry.  
See in [Glossary](../Glossary.html#Normalmap) to simulate depth is currently a
very expensive operation. If it is enabled, a full size Render Texture is
created during a depth pre-pass and the Renderers are drawn onto it. This is
done for each Layer batch.

If the normal mapping effect to simulate depth perception is not needed,
ensure that all lights have the normal map option disabled.

[](../urp/2d-light-optimize.html)

Optimizing 2D lights

[](../urp/2d-light-batching-intro.html)

Introduction to 2D light batching

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

