[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightingBakedAmbientOcclusion.html)
  * [中文](/cn/current/Manual/LightingBakedAmbientOcclusion.html)
  * [日本語](/ja/current/Manual/LightingBakedAmbientOcclusion.html)
  * [한국어](/kr/current/Manual/LightingBakedAmbientOcclusion.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightingBakedAmbientOcclusion.html)
  * [中文](/cn/current/Manual/LightingBakedAmbientOcclusion.html)
  * [日本語](/ja/current/Manual/LightingBakedAmbientOcclusion.html)
  * [한국어](/kr/current/Manual/LightingBakedAmbientOcclusion.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * [Shadows in the Built-In Render Pipeline](shadows-in-birp.html)
  * Add ambient occlusion in the Built-In Render Pipeline

[](shadow-resolution-birp.html)

Configure shadow resolution in the Built-In Render Pipeline

[](LightProbeProxyVolume-landing.html)

Configure a GameObject to sample more Light Probes in the Built-In Render
Pipeline

# Add ambient occlusion in the Built-In Render Pipeline

**Ambient occlusion** A method to approximate how much ambient light (light
not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](Glossary.html#Ambientocclusion) (AO) is a feature that
simulates the soft shadows that occur in creases, holes, and surfaces that are
close to each another. These areas occlude (block out) **ambient light** Light
that doesn’t come from any specific direction, and contributes equal light in
all directions to the Scene. [More info](lighting-window.html)  
See in [Glossary](Glossary.html#Ambientlight), so they appear darker.

It works by approximating how much ambient light can hit a point on a surface.
It then darkens creases, holes and surfaces that are close to each other.

You can use ambient occlusion to add realism to your lighting.

## Baked Ambient Occlusion

If **Baked**Global Illumination** A group of techniques that model both direct
and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination)** is enabled in your
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), Unity can bake ambient occlusion into
the **lightmaps** A pre-rendered texture that contains the effects of light
sources on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap). This is known as **Baked Ambient
Occlusion**.

To enable baked ambient occlusion in your Scene:

  1. Open the **Lighting** window (menu: **Window** > **Rendering** > **Lighting**)
  2. Navigate to the **Mixed Lighting** section
  3. Enable **Baked Global Illumination**
  4. Navigate to the **Lightmapping Settings** section
  5. Enable **Ambient Occlusion**

## Realtime ambient occlusion

If Global Illumination is not enabled in your Scene but you still want the
effect of ambient occlusion, you can use a **post-processing** A process that
improves product visuals by applying filters and effects before the image
appears on screen. You can use post-processing effects to simulate physical
camera and film properties, for example Bloom and Depth of Field. [More
info](PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](Glossary.html#post-processing) effect to apply real-time
ambient occlusion to your Scene.

If ****Enlighten** A lighting system by Geomerics used in Unity for Enlighten
Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination** is
enabled in your scene, the resolution for indirect lighting does not capture
fine details or dynamic objects. We recommend using a real-time ambient
occlusion post-processing effect, which has much more detail and results in
higher quality lighting.

For information on real-time ambient occlusion post-processing effects, see
[post-processing effects](PostProcessingOverview.html).

## Additional resources

  * [Screen space ambient occlusion in URP](urp/post-processing-ssao-landing.html)

[](shadow-resolution-birp.html)

Configure shadow resolution in the Built-In Render Pipeline

[](LightProbeProxyVolume-landing.html)

Configure a GameObject to sample more Light Probes in the Built-In Render
Pipeline

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

