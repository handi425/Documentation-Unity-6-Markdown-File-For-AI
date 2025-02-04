[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysTrailsModule.html)
  * [中文](/cn/current/Manual/PartSysTrailsModule.html)
  * [日本語](/ja/current/Manual/PartSysTrailsModule.html)
  * [한국어](/kr/current/Manual/PartSysTrailsModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysTrailsModule.html)
  * [中文](/cn/current/Manual/PartSysTrailsModule.html)
  * [日本語](/ja/current/Manual/PartSysTrailsModule.html)
  * [한국어](/kr/current/Manual/PartSysTrailsModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Trails module reference

[](PartSysLightsModule.html)

Lights module reference

[](PartSysCustomDataModule.html)

Custom Data module reference

# Trails module reference

Add trails to a percentage of your particles using this module.

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**Property:** | **Function:**  
---|---  
**Mode** | Choose how trails are generated for the Particle System.   
\- **Particle** A small, simple image or mesh that is emitted by a particle
system. A particle system can display and move particles in great numbers to
represent a fluid or amorphous entity. The effect of all the particles
together creates the impression of the complete entity, such as smoke. [More
info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) mode creates an effect where each
particle leaves a stationary trail in its path.  
\- **Ribbon** mode create a ribbon of trails connecting each particle based on
its age.  
**Ratio** | A value between 0 and 1, describing the proportion of particles that have a Trail assigned to them. Unity assigns trails randomly, so this value represents a probability.  
**Lifetime** | The lifetime of each vertex in the Trail, expressed as a multiplier of the lifetime of the particle it belongs to. When each new vertex is added to the Trail, it disappears after it has been in existence longer than its total lifetime.  
**Minimum Vertex Distance** | Define the distance a particle must travel before its Trail receives a new vertex.  
**World Space** | When enabled, Trail vertices do not move relative to the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem)’s **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), even if using **Local Simulation
Space**. Instead, the Trail vertices are dropped in the world, and ignore any
movement of the Particle System.  
**Die With Particles** | If this box is checked, Trails vanish instantly when their particles die. If this box is not checked, the remaining Trail expires naturally based on its own remaining lifetime.  
**Ribbon Count** | Choose how many ribbons to render throughout the Particle System. A value of 1 creates a single ribbon connecting each particle. However, a value higher than 1 creates ribbons that connect every Nth particle. For example, when using a value of 2, there will be one ribbon connecting particles 1, 3, 5, and another ribbon connecting particles 2, 4, 6, and so on. The ordering of the particles is decided based on their age.  
**Split Sub Emitter Ribbons** | When enabled on a system that is being used as a sub-emitter, particles that were spawned from the same parent system particle share a ribbon.  
**Texture Mode** | Choose how textures are applied to Particle Trails.   
\- **Stretch** mode stretches the texture along the entire length of the
trail.  
\- **Tile** A simple class that allows a sprite to be rendered on a Tilemap.
[More info](tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-
landing.html)  
See in [Glossary](Glossary.html#Tile) repeats the texture every N units of
distance. The repeat rate is controlled based on the **Tiling** parameters in
the **Material** An asset that defines how a surface should be rendered. [More
info](class-Material.html)  
See in [Glossary](Glossary.html#Material).  
\- **Repeat per Segment** mode repeats the texture along the trail, repeating
at a rate of once per trail segment. The repeat rate is controlled based on
the **Tiling** parameters in the **Material**.  
\- **Distribute per Segment** mode maps the texture once along the entire
length of the trail, and assumes that all vertices are evenly spaced.  
**Size affects Width** | If enabled (the box is checked), the Trail width is multiplied by the particle size.  
**Size affects Lifetime** | If enabled (the box is checked), the Trail lifetime is multiplied by the particle size.  
**Inherit Particle Color** | If enabled (the box is checked), the Trail color is modulated by the particle color.  
**Color over Lifetime** | A curve to control the color of the entire Trail over the lifetime of the particle it is attached to.  
**Width over Trail** | A curve to control the width of the Trail over its length.  
**Color over Trail** | A curve to control the color of the Trail over its length.  
**Generate Lighting Data** | Enable this (check the box), to build the Trail geometry with Normals and Tangents included. This allows them to use Materials that use the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) lighting, for example via the Standard
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), or by using a custom shader.  
**Shadow Bias** | Move the shadows along the direction of the light. This removes shadowing artifacts caused by approximating volumes with billboarded trail geometry.  
  
## Additional resources

  * [Particle lights and trails](particle-lights-trails.html)

[](PartSysLightsModule.html)

Lights module reference

[](PartSysCustomDataModule.html)

Custom Data module reference

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

