[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/lighting-emissive-materials.html)
  * [中文](/cn/current/Manual/lighting-emissive-materials.html)
  * [日本語](/ja/current/Manual/lighting-emissive-materials.html)
  * [한국어](/kr/current/Manual/lighting-emissive-materials.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/lighting-emissive-materials.html)
  * [中文](/cn/current/Manual/lighting-emissive-materials.html)
  * [日本語](/ja/current/Manual/lighting-emissive-materials.html)
  * [한국어](/kr/current/Manual/lighting-emissive-materials.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * Emit light from a GameObject in the Built-In Render Pipeline

[](PerPixelLights-BuiltIn.html)

Per-pixel and per-vertex lights in the Built-In Render Pipeline

[](creating-cookies-built-in-render-pipeline.html)

Create cookies in the Built-In Render Pipeline

# Emit light from a GameObject in the Built-In Render Pipeline

![](../uploads/GlobalIllumination/EmissiveMaterial.png)

Like area lights, emissive materials emit light across their surface area.
They contribute to bounced light in your **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and associated properties such as color
and intensity can be changed during gameplay. Whilst area lights are not
supported by **Enlighten** A lighting system by Geomerics used in Unity for
Enlighten Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination), similar soft lighting
effects in real-time are still possible using emissive materials.

‘Emission’ is a property of the Standard **Shader** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) which allows static objects in our
scene to emit light. By default the value of ‘Emission’ is set to zero. This
means no light will be emitted by objects assigned materials using the
Standard Shader.

There is no range value for emissive materials but light emitted will again
falloff at a quadratic rate. Emission will only be received by objects marked
as ‘Static’ or “**Lightmap** A pre-rendered texture that contains the effects
of light sources on static objects in the scene. Lightmaps are overlaid on top
of scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) Static’ from the **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). Similarly, emissive materials
applied to non-static, or dynamic geometry such as characters will not
contribute to scene lighting.

However, materials with an emission above zero will still appear to glow
brightly on-screen even if they are not contributing to scene lighting. This
effect can also be produced by selecting ‘None’ from the Standard Shader’s
‘Global Illumination’ Inspector property. Self-illuminating materials like
these are a useful way to create effects such as neons or other visible light
sources.

Emissive materials only directly affect static geometry in your scene. If you
need dynamic, or non-static geometry - such as characters, to pick up light
from emissive materials, **Light Probes** Light probes store information about
how light passes through space in your scene. A collection of light probes
arranged within a given space can improve lighting on moving objects and
static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) must be used.

[](PerPixelLights-BuiltIn.html)

Per-pixel and per-vertex lights in the Built-In Render Pipeline

[](creating-cookies-built-in-render-pipeline.html)

Create cookies in the Built-In Render Pipeline

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

