[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysCollisionModule.html)
  * [中文](/cn/current/Manual/PartSysCollisionModule.html)
  * [日本語](/ja/current/Manual/PartSysCollisionModule.html)
  * [한국어](/kr/current/Manual/PartSysCollisionModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysCollisionModule.html)
  * [中文](/cn/current/Manual/PartSysCollisionModule.html)
  * [日本語](/ja/current/Manual/PartSysCollisionModule.html)
  * [한국어](/kr/current/Manual/PartSysCollisionModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Collision module reference

[](PartSysExtForceModule.html)

External Forces module reference

[](PartSysTriggersModule.html)

Triggers module reference

# Collision module reference

This module controls how [particles](class-ParticleSystem.html)A small, simple
image or mesh that is emitted by a particle system. A particle system can
display and move particles in great numbers to represent a fluid or amorphous
entity. The effect of all the particles together creates the impression of the
complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) collide with
[GameObjects](GameObjects.html)The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the
[Scene](CreatingScenes.html)A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

**Property** | **Function**  
---|---  
**Type** | Use the **Type** * drop-down to define whether your **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) settings apply to **Planes** or to
the **World** The area in your scene in which all objects reside. Often used
to specify that coordinates are world-relative, as opposed to object-relative.  
See in [Glossary](Glossary.html#World). If you choose **World** , use the
**Collision Mode** drop-down to define whether your collision settings apply
for a [2D or 3D](2Dor3D.html) world.  
  
## Planes module properties

![](../uploads/Main/PartSysCollisionInsp.png)

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**Property** | **Function**  
---|---  
**Planes popup** | Select **Planes** mode.  
**Planes** | An expandable list of Transforms that define collision planes.  
**Visualization** | Selects whether the collision plane **Gizmos** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) will be shown in the **Scene view** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) as wireframe grids or solid planes.  
**Scale Plane** | Size of planes used for visualization.  
**Dampen** | The fraction of a particle’s speed that it loses after a collision.  
**Bounce** | The fraction of a particle’s speed that rebounds from a surface after a collision.  
**Lifetime Loss** | The fraction of a particle’s total lifetime that it loses if it collides.  
**Min Kill Speed** | Particles travelling below this speed after a collision will be removed from the system.  
**Max Kill Speed** | Particles travelling above this speed after a collision will be removed from the system.  
**Radius Scale** | Allows you to adjust the radius of the particle collision spheres so it more closely fits the visual edges of the particle graphic.  
**Send Collision Messages** | If enabled, particle collisions can be detected from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) by the
[OnParticleCollision](../ScriptReference/MonoBehaviour.OnParticleCollision.html)
function.  
**Visualize Bounds** | Renders the collision bounds of each particle as a wireframe shape in the Scene view.  
  
## World module properties

![](../uploads/Main/PartSysCollisionInsp2.png)

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**_Property_** | **_Function_**  
---|---  
**World popup** | Select **World** mode.  
**Collision Mode** | 3D or 2D.  
**Dampen** | The fraction of a particle’s speed that it loses after a collision.  
**Bounce** | The fraction of a particle’s speed that rebounds from a surface after a collision.  
**Lifetime Loss** | The fraction of a particle’s total lifetime that it loses if it collides.  
**Min Kill Speed** | Particles travelling below this speed after a collision will be removed from the system.  
**Max Kill Speed** | Particles travelling above this speed after a collision will be removed from the system.  
**Radius Scale** | Setting for 2D or 3D.  
**Collision Quality** | Use the drop-down to set the quality of particle collisions. This affects how many particles can pass through a collider. At lower quality levels, particles can sometimes pass through colliders, but are less resource-intensive to calculate.  
High | When **Collision Quality** is set to **High** , collisions always use the physics system for detecting the collision results. This is the most resource-intensive option, but also the most accurate.  
Medium (Static Colliders) | When **Collision Quality** is set to **Medium (Static Colliders)** , collisions use a grid of voxels to cache previous collisions, for faster re-use in later frames. See [Particle collisions: World collisions](particle-collisions.html#WorldCollisions), below, to learn more about this cache.   
  
The only difference between **Medium** and **Low** is how many times per frame
the Particle System queries the physics system. **Medium** makes more queries
per frame than **Low**.  
  
Note that this setting is only suitable for static colliders that never move.  
Low (Static Colliders) | When **Collision Quality** is set to **Low (Static Colliders)** , collisions use a grid of voxels to cache previous collisions, for faster re-use in later frames. See [Particle collisions: World collisions](particle-collisions.html#WorldCollisions), below, to learn more about this cache.   
  
The only difference between **Medium** and **Low** is how many times per frame
the Particle System queries the physics system. **Medium** makes more queries
per frame than **Low**.  
  
Note that this setting is only suitable for static colliders that never move.  
**Collides With** | Particles will only collide with objects on the selected layers.  
**Max Collision Shapes** | How many collision shapes can be considered for particle collisions. Excess shapes are ignored, and **terrains** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) take priority.  
**Enable Dynamic Colliders** | Dynamic colliders are any collider not configured as Kinematic (see documentation on [colliders](CollidersOverview.html)An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) for further information on collider
types).  
  
Check this option to include these collider types in the set of objects that
the particles respond to in collisions. If you uncheck this option, the
particles only respond to collisions against static colliders.  
**Voxel Size** | A voxel represents a value on a regular grid in three-dimensional space. When using **Medium** or **Low** quality collisions, Unity caches collisions in a grid structure. This setting controls the grid size. Smaller values give more accuracy, but cost more memory, and are less efficient.   
  
**Note** : You can only access this property when **Collision Quality** is set
to **Medium** or **Low**.  
**Collider Force** | Apply a force to Physics Colliders after a Particle collision. This is useful for pushing colliders with particles.  
**Multiply by Collision Angle** | When applying forces to Colliders, scale the strength of the force based on the collision angle between the particle and the collider. Grazing angles will generate less force than a head-on collision.  
**Multiply by Particle Speed** | When applying forces to Colliders, scale the strength of the force based on the speed of the particle. Fast-moving particles will generate more force than slower ones.  
**Multiply by Particle Size** | When applying forces to Colliders, scale the strength of the force based on the size of the particle. Larger particles will generate more force than smaller ones.  
**Send Collision Messages** | Check this to be able to detect particle collisions from scripts by the [OnParticleCollision](../ScriptReference/MonoBehaviour.OnParticleCollision.html) function.  
**Visualize Bounds** | Preview the collision spheres for each particle in the Scene view.  
  
## Additional resources

  * [Particle collisions](particle-collisions.html)
  * [Particle triggers](particle-triggers.html)
  * [Configure a particle trigger](configure-particle-trigger.html)

[](PartSysExtForceModule.html)

External Forces module reference

[](PartSysTriggersModule.html)

Triggers module reference

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

