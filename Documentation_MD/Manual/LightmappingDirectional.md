[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightmappingDirectional.html)
  * [中文](/cn/current/Manual/LightmappingDirectional.html)
  * [日本語](/ja/current/Manual/LightmappingDirectional.html)
  * [한국어](/kr/current/Manual/LightmappingDirectional.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightmappingDirectional.html)
  * [中文](/cn/current/Manual/LightmappingDirectional.html)
  * [日本語](/ja/current/Manual/LightmappingDirectional.html)
  * [한국어](/kr/current/Manual/LightmappingDirectional.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Configuring lightmapping](configure-lightmapping-settings.html)
  * Store light direction with Directional Mode

[](ProgressiveLightmapper-CustomFallOff.html)

Change the fade distance of lights with fall-off

[](LightingGiUvs-landing.html)

Lightmap UVs

# Store light direction with Directional Mode

There are two **Directional Modes** for **lightmaps** A pre-rendered texture
that contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap): **Directional** and **Non-
Directional**. Both modes are compatible with real-time lightmaps from Unity’s
**Enlighten** A lighting system by Geomerics used in Unity for Enlighten
Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) system, and baked
lightmaps from Unity’s Progressive **Lightmapper** A tool in Unity that bakes
lightmaps according to the arrangement of lights and geometry in your scene.
[More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper). The default mode is Directional.

When you bake a Directional lightmap, Unity generates two lightmap textures.
One texture stores information about the intensity and color of the lighting
received across the target surface. This is identical to the Non-Directional
lightmap. The other texture stores the dominant light direction, along with a
factor describing how much of the total light received comes from that
dominant direction.

The barrels in this image have baked Non-directional lightmaps.

![](../uploads/Main/DirectionalLightmapping1.jpg)

The barrels in this image have baked Directional lightmaps.

![](../uploads/Main/DirectionalLightmapping2.jpg)

## Performance

Directional mode lightmaps consist of two textures, and **shaders** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) sample both textures during rendering.
The additional texture increases video memory requirements. Generating the
additional directionality texture also has an impact on baking performance.

Non-Directional mode lightmaps only include a single texture. As a result,
they require less video memory and less storage than Directional maps, and are
faster to decode in shaders. These optimizations reduce visual quality.

## Setting your lightmap mode

To set the mode in your [**Lighting Settings
Asset**](https://docs.unity3d.com/2020.1/Documentation/Manual/class-
LightingSettings.html), open the Lighting window (**Window** > **Lighting** >
**Settings**), click **Scene** , navigate to the [Lightmapping
Settings](https://docs.unity3d.com/Manual/lighting-
window.html#LightmappingSettings), and select **Directional Mode**.

You can set the lightmap mode for an instance of the Lighting Settings asset
which can apply to one or more **Scenes** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). You cannot set the lightmap mode for
individual lightmaps.

## Using Directional Mode with additive loading

Unity can load Scenes additively. This means you can use [Multi-Scene
editing](https://docs.unity3d.com/Manual/MultiSceneEditing.html), for example.
When you load Scenes additively, all of them must use the same Directional
Mode. This includes Scenes that are not baked, such as **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) elements or loading screens. Using the
same [Lightmap Parameters asset](https://docs.unity3d.com/Manual/class-
LightmapParameters.html) for all of the Scenes in your project can help you
avoid settings conflicts.

[](ProgressiveLightmapper-CustomFallOff.html)

Change the fade distance of lights with fall-off

[](LightingGiUvs-landing.html)

Lightmap UVs

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

