[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/choose-a-lighting-setup.html)
  * [中文](/cn/current/Manual/choose-a-lighting-setup.html)
  * [日本語](/ja/current/Manual/choose-a-lighting-setup.html)
  * [한국어](/kr/current/Manual/choose-a-lighting-setup.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/choose-a-lighting-setup.html)
  * [中文](/cn/current/Manual/choose-a-lighting-setup.html)
  * [日本語](/ja/current/Manual/choose-a-lighting-setup.html)
  * [한국어](/kr/current/Manual/choose-a-lighting-setup.html)

  * [Lighting](LightingOverview.html)
  * [Get started with lighting](lighting-get-started.html)
  * Choose a lighting setup

[](LightingInUnity.html)

Introduction to lighting

[](lighting-light-sources.html)

Light sources

# Choose a lighting setup

## Choose a global illumination system

![](../uploads/Main/BestPracticeLightingPipeline4.svg)

### Warning

The Unity Editor and Player allow you to use both **Enlighten** A lighting
system by Geomerics used in Unity for Enlighten Realtime Global Illumination.
[More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) and baked lighting at the
same time.

However, simultaneously enabling these features greatly increases baking time
and memory usage at runtime, because they do not use the same data sets. You
can expect visual differences between indirect light you have baked and
indirect light provided by Enlighten Realtime Global Illumination, regardless
of the **lightmapper** A tool in Unity that bakes lightmaps according to the
arrangement of lights and geometry in your scene. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) you use for baking. This is
because Enlighten Realtime Global Illumination often operates at a
significantly different resolution than Unity’s baking backends, and relies on
different techniques to simulate indirect lighting.

If you wish to use both Enlighten Realtime Global Illumination and baked
lighting at the same time, limit your simultaneous use of both global
illumination systems to high-end platforms and/or to projects that have
tightly controlled **scenes** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) with predictable costs. Only expert
users who have a very good understanding of all lighting settings can
effectively use this approach. Consequently, picking one of the two global
illumination systems is usually a safer strategy for most projects. Using both
systems is rarely recommended.

## Lighting scenarios

Now that we have introduced the **render pipelines** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) and the main lighting
features, let’s have a look at a few examples of projects and see which
settings could be used to light them. Since every project is unique, you might
use slightly different options based on your requirements.

### 1\. Prototype or quick previsualization

If you rely heavily on the **Asset Store** A growing library of free and
commercial assets created by Unity and members of the community. Offers a wide
variety of assets, from textures, models and animations to whole project
examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) to build your prototype, the
Built-In Render Pipeline could be the only suitable render pipeline, as most
assets found on the Store are not fully compatible with HDRP and URP;
nonetheless, asset compatibility will improve over time. If you are building
all the assets from the ground up and already have a clear idea of your
project’s requirements, then you could pick one of the two SRPs (i.e. URP or
HDRP) or even create a custom one.

When you are in the early stage of (pre-)production and need a quick
turnaround and maximum flexibility for the lighting, you might prefer a full
real-time approach that does not require any precomputation, therefore you
might want to turn off both Baked Global Illumination and Enlighten Realtime
Global Illumination. To alleviate the lack of proper indirect lighting, you
can enable Screen Space **Ambient Occlusion** A method to approximate how much
ambient light (light not coming from a specific direction) can hit a point on
a surface.  
See in [Glossary](Glossary.html#Ambientocclusion): it can help ground the
object in the scene by offering cheap real-time contact shadows.

### 2\. 3D Mobile strategy game

If you are targeting mobile devices, URP could be a great candidate to ensure
solid performance for your game. It is in many cases possible to customise URP
to suit your game’s specific needs, with help from a graphics programmer.

The Built-In Render Pipeline and URP both support **Shadowmask** A Texture
that shares the same UV layout and resolution with its corresponding lightmap.
[More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask) Lighting Mode which makes it
possible for you to bake shadows for static objects while still enabling
dynamic objects to cast real-time shadows. If Shadowmasks are too expensive
for your project, you can fall back to the cheapest Subtractive mode. Finally,
the forward **rendering path** The technique that a render pipeline uses to
render graphics. Choosing a different rendering path affects how lighting and
shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) is probably the best option if
you have a very small number of lights in your level(s), and if you’re
targeting older hardware.

### 3\. AAA corridor shooter (fixed time of day)

If you are aiming for AAA-quality visuals on PC and consoles for your linear
first-person shooter, HDRP should be the preferred render pipeline. Again,
with the help of graphics programmers, a custom SRP could also be developed.

If your levels contain many real-time shadow casting lights (e.g. destructible
light props and moving lights), then using the Baked Global Illumination
system with the Baked Indirect mode should ensure you get great looking
indirect lighting from the Mixed directional light and the **Baked lights**
Light components whose Mode property is set to Baked. Unity pre-calculates the
illumination from Baked Lights before runtime, and does not include them in
any runtime lighting calculations. [More info](LightModes-
introduction.html#baked)  
See in [Glossary](Glossary.html#BakedLights) in static light props. If your
levels consist of a larger proportion of fixed shadow casting lights, then an
approach with Shadowmasks could be recommended because HDRP offers a great
hybrid Shadowmask mode which gives you more control over the blend between
real-time and baked shadows.

If you also plan to support the Nintendo Switch, then using URP would be
recommended, so that you can support most gaming platforms on the market and
not having to go through the potentially tedious process of porting your
project from HDRP to URP, or vice versa.

### 4\. Battle Royale (day-night cycle)

If you plan to release a battle royale game for PC and consoles, that features
large-scale environments and fully dynamic lighting, you should select HDRP,
or extend it to tailor the rendering pipeline to your project. You could
consider URP if you are not aiming for AAA visual fidelity and are targeting
mobile devices or systems with lower specifications.

For this particular scenario, if you are using the Built-in Render Pipeline,
activating both the Enlighten Realtime Global Illumination and a Baked Global
Illumination system is not recommended, because the resulting overhead in
terms of performance and scene management for an immense level could be
problematic. Another argument against the use of both global illumination
systems is the unpredictable nature of such large-scale multiplayer games:
performance estimations are for instance more difficult than in a highly-
scripted linear level.

## Additional resources

  * [Choose a render pipeline](choose-a-render-pipeline.html)
  * [Choose a Light Mode](LightModes-choose.html)
  * [Choose a Lighting Mode](lighting-mode-choose.html)
  * [Lighting in URP](urp/lighting-landing.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * [Manage your templates](https://docs.unity3d.com/hub/manual/Templates.html)
  * [Creating Believable Visuals tutorial (Built-In Rener Pipeline)](https://unity3d.com/learn/tutorials/s/creating-believable-visuals)

[](LightingInUnity.html)

Introduction to lighting

[](lighting-light-sources.html)

Light sources

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

