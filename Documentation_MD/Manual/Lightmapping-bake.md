[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Lightmapping-bake.html)
  * [中文](/cn/current/Manual/Lightmapping-bake.html)
  * [日本語](/ja/current/Manual/Lightmapping-bake.html)
  * [한국어](/kr/current/Manual/Lightmapping-bake.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Lightmapping-bake.html)
  * [中文](/cn/current/Manual/Lightmapping-bake.html)
  * [日本語](/ja/current/Manual/Lightmapping-bake.html)
  * [한국어](/kr/current/Manual/Lightmapping-bake.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Baking lightmaps before runtime](Lightmapping-baking-before-runtime.html)
  * Bake lighting

[](Lightmapping-preview.html)

Preview baked lighting

[](Lightmapping-configure.html)

Configuring lightmaps and baking

# Bake lighting

To generate **lightmaps** A pre-rendered texture that contains the effects of
light sources on static objects in the scene. Lightmaps are overlaid on top of
scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) for your Scene:

  1. Open the [Lighting window](lighting-window.html) (menu: **Window** > **Rendering** > **Lighting**)

  2. At the bottom of the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) tab on the Lighting window, select
**Generate Lighting**.

  3. A progress bar appears in Unity Editor’s status bar, in the bottom-right corner.

When lightmapping is complete, Unity’s Scene and Game views update
automatically and you can view the resulting lightmaps by going to the **Baked
Lightmaps** tab in the Lighting Window.

When you generate lighting, Unity adds [Lighting Data
Assets](LightmapSnapshot.html), [baked lightmaps](lighting-window.html) and
[Reflection Probes](ReflectionProbes.html)A rendering component that captures
a spherical view of its surroundings in all directions, rather like a camera.
The captured image is then stored as a Cubemap that can be used by objects
with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) to the
[Assets](SpecialFolders.html)Any media or data that can be used in your game
or project. An asset may come from a file created outside of Unity, such as a
3D Model, an audio file or an image. You can also create some asset types in
Unity, such as an Animator Controller, an Audio Mixer or a Render Texture.
[More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) folder.

## Bake lightmaps automatically

To set Unity to bake lightmaps automatically when you open a scene that has no
lighting data, follow these steps:

  1. Go to **Window** > **Rendering** > **Lighting**.

  2. Set **Bake on Scene Load** to **If Missing Lighting Data**.

If you share your project with someone else, you can use this option to reduce
the size of your project by not including lighting data. When a scene is
opened by someone else, Unity calculates the missing lighting data.

[](Lightmapping-preview.html)

Preview baked lighting

[](Lightmapping-configure.html)

Configuring lightmaps and baking

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

