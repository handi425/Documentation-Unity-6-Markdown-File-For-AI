[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightModes-introduction.html)
  * [中文](/cn/current/Manual/LightModes-introduction.html)
  * [日本語](/ja/current/Manual/LightModes-introduction.html)
  * [한국어](/kr/current/Manual/LightModes-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightModes-introduction.html)
  * [中文](/cn/current/Manual/LightModes-introduction.html)
  * [日本語](/ja/current/Manual/LightModes-introduction.html)
  * [한국어](/kr/current/Manual/LightModes-introduction.html)

  * [Lighting](LightingOverview.html)
  * [Light sources](lighting-light-sources.html)
  * [Light components](lighting-light-components.html)
  * [Configuring Light components](lighting-light-components-configuring.html)
  * [Setting a light as realtime or baked](LightModes-landing.html)
  * Light Modes

[](LightModes-landing.html)

Setting a light as realtime or baked

[](LightModes-choose.html)

Choose a Light Mode

# Light Modes

There are three [Light Modes](LightModes.html)A Light property that defines
the use of the Light. Can be set to Realtime, Baked and Mixed. [More
info](LightModes.html)  
See in [Glossary](Glossary.html#LightMode) available in the [Light
Inspector](class-Light.html):

  * Baked: The direct and indirect lighting from these lights is baked into **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), which can be a time-consuming
process. There is no runtime cost to process these lights, however applying
the resulting lightmaps to the **scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) does have a minor cost.

  * Realtime: The direct lighting and shadows from these lights are real-time and therefore not baked into lightmaps. Their runtime cost can be high, depending on the complexity of the scene, the number of shadow casting lights, the number of overlapping lights, etc. Furthermore, if you enable **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination), further performance costs
will be incurred to update the indirect lighting at runtime.

  * Mixed: This is a hybrid mode that offers a mix of baked and real-time features, such as baked indirect lighting and real-time direct lighting. The behavior of all Mixed lights in your Scene and their performance impact depends on the [Lighting Mode](lighting-mode.html) for that Scene.

It is important to note that the mode of a light is only relevant if the Baked
Global Illumination system is enabled. If you do not use any global
illumination system or only use Enlighten Realtime Global Illumination system,
then all Baked and Mixed lights will behave as though their Mode property was
set to Realtime.

## Realtime

These are also known as Realtime Lights.

Unity performs the lighting calculations for Realtime Lights at runtime, once
per frame. You can change the properties of Realtime Lights at runtime to
create effects such as flickering light bulbs, or a torch being carried
through a dark room.

Realtime Lights are useful for lighting and casting shadows on characters or
moveable geometry.

### Realtime Light behavior

  * Realtime Lights cast shadows up to the **Shadow Distance**.
  * By default, Realtime Lights contribute only realtime direct lighting to a Scene. If you’re using the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) and you enable **Enlighten
Realtime Global Illumination** in your Project, Realtime Lights also
contribute realtime indirect lighting to your Scene.

### Limitations of Realtime Lights

  * Performing runtime calculations for Realtime Lights might be costly, especially in complex scenes or on low-end hardware.
  * Because Realtime Lights only contribute direct lighting to the Scene by default, shadows appear completely black and there aren’t any indirect lighting effects, such as color bounce. This might cause unrealistic lighting in the Scene.

## Mixed

These are also known as Mixed Lights.

Mixed Lights combine elements of both real-time and baked lighting. You can
use Mixed Lights to combine dynamic shadows with baked lighting from the same
light source, or when you want a light to contribute direct real-time lighting
and baked indirect lighting.

To use Mixed Lights, you must first understand the benefits and limitations of
Realtime LightsLight components whose Mode property is set to Realtime. Unity
calculates and updates the lighting of Realtime Lights every frame at runtime.
No Realtime Lights are precomputed. [More info](LightModes-
introduction.html#realtime)  
See in [Glossary](Glossary.html#RealtimeLights) and Baked LightsLight
components whose Mode property is set to Baked. Unity pre-calculates the
illumination from Baked Lights before runtime, and does not include them in
any runtime lighting calculations. [More info](LightModes-
introduction.html#baked)  
See in [Glossary](Glossary.html#BakedLights).

### Mixed Light behavior

  * The behavior of all Mixed Lights in a Scene depends on the **Lighting Mode** setting in the Lighting window. The different Lighting Modes have very different performance characteristics, and different levels of visual fidelity. For more information, see [Lighting Modes](lighting-mode.html).
  * You can change properties of Mixed Lights at runtime. This updates their real-time lighting but not their baked lighting. When doing this, take care to avoid unwanted visual effects.

### Limitations of Mixed Lights

  * The performance cost of Mixed Lights differs considerably, depending on the Lighting Mode. However, because Mixed Lights always combine at least some real-time and some baked lighting, Mixed Lights always involve more runtime calculations than fully baked lighting, and higher memory usage than fully real-time lighting.

Note that if you disable **Baked Global Illumination** in your Scene, Unity
forces Mixed Lights to behave as though you set their **Mode** to
**Realtime**. When this happens, Unity displays a warning on the Light
component **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

## Baked

These are also known as Baked Lights.

Unity performs the calculations for Baked Lights in the Unity Editor, and
saves the results to disk as lighting data. This process is called baking. At
runtime, Unity loads the baked lighting data, and uses it to light the Scene.
Because the complex calculations are performed in advance, Baked Lights reduce
shading cost at runtime, and reduce the rendering cost of shadows.

Baked Lights are useful for lighting things that won’t change at runtime, such
as scenery.

### Baked Light behavior

  * Unity bakes both direct lighting and indirect lighting from Baked Lights into lightmaps. For more information on using lightmaps, see [lightmapping](Lightmappers.html).
  * Unity bakes both direct and indirect lighting from Baked Lights into Light Probes. For more information on using Light Probes, see [Light Probes](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).

### Limitations of Baked Lights

  * You cannot change the properties of Baked Lights at runtime.
  * Baked Lights do not contribute to specular lighting.
  * Dynamic **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) do not receive light or shadow
from Baked Lights.

Note that if you disable **Baked Global Illumination** in your Scene, Unity
forces Baked Lights to behave as though you set their **Mode** to
**Realtime**. When this happens, Unity displays a warning on the Light
component Inspector.

[](LightModes-landing.html)

Setting a light as realtime or baked

[](LightModes-choose.html)

Choose a Light Mode

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

