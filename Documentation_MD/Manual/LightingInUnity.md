[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightingInUnity.html)
  * [中文](/cn/current/Manual/LightingInUnity.html)
  * [日本語](/ja/current/Manual/LightingInUnity.html)
  * [한국어](/kr/current/Manual/LightingInUnity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightingInUnity.html)
  * [中文](/cn/current/Manual/LightingInUnity.html)
  * [日本語](/ja/current/Manual/LightingInUnity.html)
  * [한국어](/kr/current/Manual/LightingInUnity.html)

  * [Lighting](LightingOverview.html)
  * [Get started with lighting](lighting-get-started.html)
  * Introduction to lighting

[](lighting-get-started.html)

Get started with lighting

[](choose-a-lighting-setup.html)

Choose a lighting setup

# Introduction to lighting

This page introduces you to how lighting works in Unity.

Lighting in Unity works by approximating how light behaves in the real world.
Unity uses detailed models of how light works for a more realistic result, or
simplified models for a more stylized result.

## Lighting pipeline

The following flowchart provides a high-level perspective of the entire
lighting pipeline in Unity, from the point of view of a content creator.

![](../uploads/Main/BestPracticeLightingPipeline15.svg)

You start by [selecting a render pipeline](choose-a-render-pipeline.html).
Then you decide how the indirect lighting is generated and pick a **Global
Illumination** A group of techniques that model both direct and indirect
lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) system accordingly. After
you’ve made sure all the global lighting settings are tuned appropriately for
your project, you can continue adding
[Lights](https://docs.unity3d.com/Manual/Lighting.html), [Emissive
Surfaces](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterEmission.html),
[Reflection Probes](https://docs.unity3d.com/Manual/class-
ReflectionProbe.html)A rendering component that captures a spherical view of
its surroundings in all directions, rather like a camera. The captured image
is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe), [Light
Probes](https://docs.unity3d.com/Manual/LightProbes.html)Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe), and [Light Probe Proxy Volumes
(LPPVs)](https://docs.unity3d.com/Manual/class-LightProbeProxyVolume.html).

## Lights

**Lights** are an essential part of every **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). While meshes and textures define the
shape and look of a scene, lights define the color and mood of your 3D
environment. You’ll likely work with more than one light in each scene. Making
them work together requires a little practice but the results can be quite
amazing.

![](../uploads/Main/StandardShaderChangingSkyboxesEffect.gif)

Lights can be added to your scene from the **GameObject- >Light** menu. You
will choose the light format that you want from the sub-menu that appears.
Once a light has been added, you can manipulate it like any other GameObject.
Additionally, you can add a Light Component to any selected GameObject by
using **Component- >Rendering->Light**.

There are many different options within the Light Component in the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

By simply changing the **Color** of a light, you can give a whole different
mood to the scene.

![Bright, sunny lights](../uploads/Main/LightMood1.jpg) Bright, sunny lights
![Dark, medieval lights](../uploads/Main/LightMood2.jpg) Dark, medieval lights
![Spooky night lights](../uploads/Main/LightMood3.jpg) Spooky night lights

## Direct and indirect lighting

Direct light is light that is emitted, hits a surface once, and is then
reflected directly into a sensor (for example, the eye’s retina or a camera).
Indirect light is all other light that is ultimately reflected into a sensor,
including light that hits surfaces several times, and sky light. To achieve
realistic lighting results, you need to simulate both direct and indirect
light.

Unity can calculate direct lighting, indirect lighting, or both direct and
indirect lighting. The lighting techniques that Unity uses depends on how you
configure your Project.

## Real-time and baked lighting

Real-time lighting is when Unity calculates lighting at runtime. Baked
lighting is when Unity performs lighting calculations in advance and saves the
results as lighting data, which is then applied at runtime. In Unity, your
Project can use real-time lighting, baked lighting, or a mix of the two
(called mixed lighting).

For information on configuring Light components to contribute real-time,
baked, or mixed lighting, see [Light Modes](LightModes.html)A Light property
that defines the use of the Light. Can be set to Realtime, Baked and Mixed.
[More info](LightModes.html)  
See in [Glossary](Glossary.html#LightMode).

## Global illumination

Global illumination is a group of techniques that model both direct and
indirect lighting to provide realistic lighting results. Unity has two global
illumination systems, which combine direct and indirect lighting.

The Global Illumination systems available in Unity are:

  1. [Realtime Global Illumination](realtime-gi-using-enlighten.html): This system builds upon **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten), a third-party middleware solution.
It enables you to adjust your lighting in real-time if you do a precompute and
do not modify **GameObjects** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in your scene with the
**ContributeGI** setting enabled.

  2. Baked Global Illumination: When you select this system, Unity uses the Progressive **Lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) (CPU or GPU) to bake lighting
data into Light Probes, textures called **lightmaps** A pre-rendered texture
that contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), and Reflection Probes.

The Progressive Lightmapper calculates indirect lighting values using path
tracing. It can prioritize precomputing lighting that affects objects visible
to the **scene view** An interactive view into the world you are creating. You
use the Scene View to select and position scenery, characters, cameras,
lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) **camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Although only updating lighting for
parts of lightmaps increases the overall bake time, it also enables you to
more quickly iterate on your lighting design.

See [render pipeline feature comparison](render-pipelines-feature-
comparison.html) for more information about support for Lighting features
across **render pipelines** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline).

## Rendering paths

Unity supports different **Rendering Paths** The technique that a render
pipeline uses to render graphics. Choosing a different rendering path affects
how lighting and shading are calculated. Some rendering paths are more suited
to different platforms and hardware than others. [More
info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath). These paths affect mainly
Lights and Shadows, so choosing the correct rendering path depending on your
game requirements can improve your project’s performance. For more info about
rendering paths you can visit the [Rendering paths
section](RenderingPaths.html).

[](lighting-get-started.html)

Get started with lighting

[](choose-a-lighting-setup.html)

Choose a lighting setup

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

