[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/progressive-lightmapper.html)
  * [中文](/cn/current/Manual/progressive-lightmapper.html)
  * [日本語](/ja/current/Manual/progressive-lightmapper.html)
  * [한국어](/kr/current/Manual/progressive-lightmapper.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/progressive-lightmapper.html)
  * [中文](/cn/current/Manual/progressive-lightmapper.html)
  * [日本語](/ja/current/Manual/progressive-lightmapper.html)
  * [한국어](/kr/current/Manual/progressive-lightmapper.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Baking lightmaps before runtime](Lightmapping-baking-before-runtime.html)
  * [Configuring lightmaps and baking](Lightmapping-configure.html)
  * Select the CPU or GPU for baking

[](Lightmapping-configure.html)

Configuring lightmaps and baking

[](Lightmapping-baked-tags.html)

Group GameObjects together in a lightmap with Baked Tags

# Select the CPU or GPU for baking

You can choose between two backends for the Progressive Lightmapper. The
Progressive CPU Lightmapper backend is a backend for the Progressive
Lightmapper that uses your computer’s CPU and system RAM. The Progressive GPU
Lightmapper is a backend for the Progressive Lightmapper that uses your
computer’s GPU and VRAM.

For information on the Progressive GPU Lightmapper backend, see the
[Progressive GPU Lightmapper](GPUProgressiveLightmapper.html).

## GPU lightmapper

The **Progressive GPU Lightmapper** is a backend for the [Progressive
Lightmapper](progressive-lightmapper.html) which uses your computer’s GPU and
Dedicated Video Ram (VRAM) to generate baked **lightmaps** A pre-rendered
texture that contains the effects of light sources on static objects in the
scene. Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) and **Light Probes** Light probes
store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).

## Hardware and software requirements

In order to use the Progressive GPU Lightmapper, your computer must meet these
minimum specifications:

  * At least one GPU with OpenCL 1.2 support
  * At least 2GB of VRAM dedicated to that GPU
  * A CPU that supports SSE4.1 instructions

If the **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) you are baking requires more VRAM than
is available on the designated GPU, bake times can significantly increase. See
Performance for information to help you reduce the time it takes to bake your
Scene.

The Progressive GPU Lightmapper does not support OpenCL CPU devices.

The Apple silicon version of the Unity Editor is not compatible with the CPU
Progressive Lightmapper. However, it is compatible with the [Progressive GPU
Lightmapper](GPUProgressiveLightmapper.html).

## Render pipeline support

See [render pipeline feature comparison](render-pipelines-feature-
comparison.html) for more information about support for the Progressive
Lightmapper across **render pipelines** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline).

## Select the Progressive Lightmapper

To select the Progressive Lightmapper:

  1. Go to **Window** > **Rendering** > **Lighting**
  2. Navigate to **Lightmapping Settings**
  3. Set **Lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) to **Progressive CPU** or
**Progressive GPU**

You can perform many of the functions available in this window via **scripts**
A piece of code that allows you to create your own Components, trigger game
events, modify Component properties over time and respond to user input in any
way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), using the
[LightmapEditorSettings](../ScriptReference/LightmapEditorSettings.html) and
[Lightmapping](../ScriptReference/Lightmapping.html) APIs.

[](Lightmapping-configure.html)

Configuring lightmaps and baking

[](Lightmapping-baked-tags.html)

Group GameObjects together in a lightmap with Baked Tags

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

