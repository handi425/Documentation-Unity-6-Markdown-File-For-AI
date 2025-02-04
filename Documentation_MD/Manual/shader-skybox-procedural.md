[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-skybox-procedural.html)
  * [中文](/cn/current/Manual/shader-skybox-procedural.html)
  * [日本語](/ja/current/Manual/shader-skybox-procedural.html)
  * [한국어](/kr/current/Manual/shader-skybox-procedural.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-skybox-procedural.html)
  * [中文](/cn/current/Manual/shader-skybox-procedural.html)
  * [日本語](/ja/current/Manual/shader-skybox-procedural.html)
  * [한국어](/kr/current/Manual/shader-skybox-procedural.html)

  * [World building](CreatingEnvironments.html)
  * [Sky](sky-landing.html)
  * [Skybox Shader Material Inspector window reference](skybox-material-reference.html)
  * Procedural Skybox Shader Material Inspector Window reference

[](shader-skybox-panoramic.html)

Panoramic Skybox Shader Material Inspector Window reference

[](script-Terrain.html)

Terrain

# Procedural Skybox Shader Material Inspector Window reference

For information on how to create a Material that uses this **skybox** A
special type of Material used to represent skies. Usually six-sided. [More
info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) **Shader** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), as well as details on how to render
the skybox in your **Scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), see [Using skyboxes](skyboxes-
using.html).

## Render pipeline compatibility

**Feature** | **Built-in**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline)** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
**Procedural skybox** | Yes | Yes | No  
  
## Properties

**Property** | **Description**  
---|---  
**Sun** | The method Unity uses the generate a sun disk in the skybox. The options are:  
• **None:** Disables the sun disk in the skybox.  
• **Simple:** Draws a simplified sun disk into the skybox  
• **High Quality:** Draws a sun disk into the skybox. This is similar to the
**Simple** sun disk, but with this mode, you can use **Sun Size Convergence**
to further customize the appearance of the sun disk.  
**Sun Size** | The size modifier for the sun disk. Larger values make the sun disk appear larger and setting this value to **0** makes the sun disk disappear.  
**Sun Size Convergence** | The size convergence of the sun. Smaller values make the sun disk appear larger. This property only appears if you set **Sun** to **High Quality**.  
**Atmosphere Thickness** | The density of the atmosphere. An atmosphere of higher density absorbs more light. Unity uses the Rayleigh scattering method to absorb light.  
**Sky Tint** | The color to tint the sky to.  
**Ground** | The color of the ground (the area below the horizon).  
**Exposure** | Adjusts the sky’s exposure. This allows you to change tonal values in the skybox this Material generates. Larger values produce a more exposed, seemingly brighter, skybox. Smaller values produce a less exposed, seemingly darker, skybox.  
  
[](shader-skybox-panoramic.html)

Panoramic Skybox Shader Material Inspector Window reference

[](script-Terrain.html)

Terrain

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

