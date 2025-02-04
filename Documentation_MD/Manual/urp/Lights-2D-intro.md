[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/Lights-2D-intro.html)
  * [中文](/cn/current/Manual/urp/Lights-2D-intro.html)
  * [日本語](/ja/current/Manual/urp/Lights-2D-intro.html)
  * [한국어](/kr/current/Manual/urp/Lights-2D-intro.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/Lights-2D-intro.html)
  * [中文](/cn/current/Manual/urp/Lights-2D-intro.html)
  * [日本語](/ja/current/Manual/urp/Lights-2D-intro.html)
  * [한국어](/kr/current/Manual/urp/Lights-2D-intro.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Types of 2D lights](../urp/LightTypes.html)
  * Introduction to the 2D lighting system in URP

[](../urp/LightTypes.html)

Types of 2D lights

[](../urp/create-light-2d.html)

Prepare your project for 2D lighting

# Introduction to the 2D lighting system in URP

Discover the tools and runtime components to create a lit 2D **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

These tools are designed to integrate seamlessly with 2D Renderers such as the
[Sprite Renderer](../sprite/renderer/renderer-landing.html)A component that
lets you display images as Sprites for use in both 2D and 3D scenes. [More
info](../sprite/renderer/renderer-landing.html)  
See in [Glossary](../Glossary.html#SpriteRenderer), [Tilemap
Renderer](../tilemaps/work-with-tilemaps/tilemap-renderer-reference.html), and
[../Sprite Shape Renderer](../sprite/shape-renderer/shape-renderer-
landing.html). This system of tools and components are optimized for mobile
systems, and for running on multiple platforms.

## Differences from 3D Lights

There are a number of key differences between the implementation and behavior
of 2D Lights and 3D Light, which consists of the following:

### New 2D specific components and render pass

The 2D lighting systems includes its own set of 2D Light components, [Shader
Graph](ShaderGraph.html) sub-targets and a custom 2D render pass that are
specifically designed for 2D lighting and rendering. Editor tooling for the 2D
Lights and pass configuration are also included in the package.

### Coplanar

The 2D lighting model was designed specifically to work with 2D worlds that
are coplanar and multi-layered. A 2D Light does not require depth separation
between it and the object it is lighting. The 2D shadow system also works in
coplanar and does not require depth separation.

### Not physically based

The lighting calculation in 2D Lights is not physics-based as it is with 3D
Lights.

### No interoperability with 3D Lights and 3D Renderers

3D and 2D Lights can only affect 3D and 2D Renderers respectively. 2D Lighting
does not work on or effect 3D Renderers such as the [Mesh Renderer](../class-
MeshRenderer.html)A mesh component that takes the geometry from the Mesh
Filter and renders it at the position defined by the object’s Transform
component. [More info](../class-MeshRenderer.html)  
See in [Glossary](../Glossary.html#MeshRenderer), while 3D Lighting will
similarly have no effect on 2D Renderers such as the [Sprite
Renderer](../sprite/renderer/renderer-landing.html). Currently, to achieve a
combination of 2D and 3D Lights and 2D and 3D Renderers in a single Scene, you
can use multiple **cameras** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) and have one of the cameras render
to a [Render Texture](../class-RenderTexture.html)A special type of Texture
that is created and updated at runtime. To use them, first create a new Render
Texture and designate one of your Cameras to render into it. Then you can use
the Render Texture in a Material just like a regular Texture. [More
info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture), and sample that texture in
a material rendered by another camera.

## Technical details of the 2D Lighting graphics pipeline

The 2D Lighting graphics pipeline rendering process can be broken down into 2
distinct phases: 1) Drawing the Light Render Textures 2) Drawing the Renderers

Light Render Textures are [Render Textures](../class-RenderTexture.html) that
contain information about the Light’s color and shape in screen space.

These two phases are only repeated for each distinctly lit set of Light
Layers. In other words, if [Sorting Layers](../class-
TagManager.html#SortingLayers) 1 through 4 have the exact same set of Lights,
it will only perform the above set of operations once.

The default setup allows a number of [batches](../DrawCallBatching.html) to be
drawn ahead of time before drawing the Renderers to reduce target switching.
The ideal setup would allow the pipeline to render the Light Render Textures
for all the batches and only then move on to draw the Renderers. This prevents
loading and unloading of the color target. Refer to [Optimization](2d-light-
optimize.html) for more detailed information.

### Pre-phase: Calculate Sorting Layer batching

Before proceeding with the rendering phases, the 2D Lighting graphics pipeline
first analyses the scene to assess which Layers can be batched together in a
single draw operation. The following is the criteria that determine whether
Layers are batched together: 1\. They are consecutive Layers. 2\. They share
the exact same set of Lights.

It is highly recommended to batch as many Layers as possible to minimize the
number of Light Render Textures draw operations and improve performance.

### Phase 1: Draw Light Render Textures

After the pre-phase batching, the pipeline then draws the Light Textures for
that batch. This essentially draws the Light’s shape onto a Render Texture.
The light’s color and shape can be blended onto the target Light Render
Texture using Additive or Alpha Blended depending on the light’s setup.

![](../../uploads/urp/2D/introduction_phase1.png)

It is worth noting that a Light Render Texture is only created when at least
one 2D Light is targeting it. For example, if all the lights of a Layer only
uses **Blendstyle #1** , then only one Light Render Texture is created.

### Phase 2: Draw Renderers

Once all the Light Render Textures have been drawn, the pipeline proceeds to
draw the Renderers. The system will keep track of which set of Renderers are
drawn by which set of Light Render Textures. They are associated during the
batching process in the pre-phase.

When the Renderers are being drawn, it will have access to all (one for each
blend style) the available Light Render Textures. In the **shader** A program
that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), the final color is calculated by
combining the input color with colors from the Light Render Texture using the
specified operation.

![](../../uploads/urp/2D/introduction_phase2.png)

An example of a setup with four active blend styles illustrating how multiple
blend styles come together. In most cases, you would typically only need two
blend styles for your desired effect.

## Additional resources

  * [Light 2D component reference for URP](2DLightProperties.html)
  * [Configure a 2D light](2d-light-properties-explained.html)

[](../urp/LightTypes.html)

Types of 2D lights

[](../urp/create-light-2d.html)

Prepare your project for 2D lighting

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

