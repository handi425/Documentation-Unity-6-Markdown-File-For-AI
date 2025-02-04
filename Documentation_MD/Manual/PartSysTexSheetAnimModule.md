[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysTexSheetAnimModule.html)
  * [中文](/cn/current/Manual/PartSysTexSheetAnimModule.html)
  * [日本語](/ja/current/Manual/PartSysTexSheetAnimModule.html)
  * [한국어](/kr/current/Manual/PartSysTexSheetAnimModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysTexSheetAnimModule.html)
  * [中文](/cn/current/Manual/PartSysTexSheetAnimModule.html)
  * [日本語](/ja/current/Manual/PartSysTexSheetAnimModule.html)
  * [한국어](/kr/current/Manual/PartSysTexSheetAnimModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Texture Sheet Animation module reference

[](PartSysSubEmitModule.html)

Sub Emitters module reference

[](PartSysLightsModule.html)

Lights module reference

# Texture Sheet Animation module reference

A particle’s graphic need not be a still image. This module lets you treat the
Texture as a grid of separate sub-images that can be played back as frames of
animation.

## Grid mode properties

![](../uploads/Main/PartSysTexSheetAnimModule-0.png) **Property** | **Function**  
---|---  
**Mode popup** | Select **Grid** mode.  
**Tiles** A simple class that allows a sprite to be rendered on a Tilemap.
[More info](tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-
landing.html)  
See in [Glossary](Glossary.html#Tile) | The number of tiles the Texture is divided into in the X (horizontal) and Y (vertical) directions.  
**Animation** | The Animation mode can be set to **Whole Sheet** or **Single Row** (that is, each row of the sheet represents a separate Animation sequence).  
**Time Mode** | Choose how the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) samples frames in the
animation.  
Lifetime | Sample frames using an Animation Curve over the lifetime of the particle.  
Speed | Sample frames based on the speed of the particle. A speed range specifies the minimum and maximum speed range for the frame selection.  
**FPS** See first person shooter, frames per second.  
See in [Glossary](Glossary.html#FPS) | Sample frames based on the specified frames-per-second value.  
**Row Mode** | Make the Particle System choose a row from the Texture sheet to produce the animation. This property is only available when the **Animation** mode is set to **Single Row**.  
Custom | Use a specific row of the Texture sheet for the animation.  
Random | Randomly select a row for each particle when producing the animation.  
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Index | Select a row based on the Mesh index assigned to a particle. This is useful when you want to ensure that a particle using a particular Mesh also uses the same Texture.  
**Random Row** | Chooses a row from the sheet at random to produce the animation. This option is only available when **Single Row** is selected as the **Animation** mode.  
**Row** | Selects a particular row from the sheet to produce the animation This option is only available when **Single Row** mode is selected and **Random Row** is disabled.  
**Frame over Time** | A curve that specifies how the frame of animation increases as time progresses.  
**Start Frame** | Allows you to specify which frame the particle animation should start on (useful for randomly phasing the animation on each particle).  
**Cycles** | The number of times the animation sequence repeats over the particle’s lifetime.  
**Affected UV Channels** | Allows you to specify exactly which UV streams are affected by the Particle System.  
  
## Sprite mode properties

![](../uploads/Main/PartSysTexSheetAnimModule-1.png)

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**Property** | **Function**  
---|---  
**Mode popup** | Select **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) mode.  
**Frame over Time** | A curve that specifies how the frame of animation increases as time progresses.  
**Start Frame** | Allows you to specify which frame the particle animation should start on (useful for randomly phasing the animation on each particle).  
**Cycles** | The number of times the animation sequence repeats over the particle’s lifetime.  
**Enabled UV Channels** | Allows you to specify exactly which UV streams are affected by the Particle System.  
  
## Additional resources

  * [Particle animation](particle-animation.html)

[](PartSysSubEmitModule.html)

Sub Emitters module reference

[](PartSysLightsModule.html)

Lights module reference

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

