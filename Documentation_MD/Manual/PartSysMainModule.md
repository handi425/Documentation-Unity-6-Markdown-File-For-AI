[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysMainModule.html)
  * [中文](/cn/current/Manual/PartSysMainModule.html)
  * [日本語](/ja/current/Manual/PartSysMainModule.html)
  * [한국어](/kr/current/Manual/PartSysMainModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysMainModule.html)
  * [中文](/cn/current/Manual/PartSysMainModule.html)
  * [日本語](/ja/current/Manual/PartSysMainModule.html)
  * [한국어](/kr/current/Manual/PartSysMainModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Main module reference

[](activate-access-particle-system-modules.html)

Activate and access Particle System modules

[](PartSysEmissionModule.html)

Emission module reference

# Main module reference

The **Particle System** A component that simulates fluid entities such as
liquids, clouds and flames by generating and animating large numbers of small
2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) module contains global
properties that affect the whole system. Most of these properties control the
initial state of newly created particles.

![](../uploads/Main/PartSysPartSysInsp.png)

The name of the module appears in the **inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) as the name of the **GameObject**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that the [Particle System
component](class-ParticleSystem.html) is attached to.

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**Property** | **Function**  
---|---  
**Duration** | The length of time the system runs.  
**Looping** | If enabled, the system starts again at the end of its duration time and continues to repeat the cycle.  
**Prewarm** | If enabled, the system is initialized as though it had already completed a full cycle (only works if **Looping** is also enabled).  
**Start Delay** | Delay in seconds before the system starts emitting once enabled.  
**Start Lifetime** | The initial lifetime for particles.  
**Start Speed** | The initial speed of each particle in the appropriate direction.  
**3D Start Size** | Enable this if you want to control the size of each axis separately.  
**Start Size** | The initial size of each particle.  
**3D Start Rotation** | Enable this if you want to control the rotation of each axis separately.  
**Start Rotation** | The initial rotation angle of each particle.  
**Flip Rotation** | Causes some particles to spin in the opposite direction.  
**Start Color** | The initial color of each particle.  
**Gravity Modifier** | Scales the gravity value set in the [Physics](class-PhysicsManager.html) window. A value of zero switches gravity off.  
**Simulation Space** | Controls whether particles are animated in the parent object’s local space (therefore moving with the parent object), in the world space, or relative to a custom object (moving with a custom object of your choosing).  
**Simulation Speed** | Adjust the speed at which the entire system updates.  
**Delta Time** | Choose between **Scaled** and **Unscaled** , where **Scaled** uses the **Time Scale** value in the [Time](class-TimeManager.html) window, and **Unscaled** ignores it. This is useful for Particle Systems that appear on a Pause Menu, for example.  
**Scaling Mode** | Choose how to use the scale from the transform. Set to **Hierarchy** , **Local** or **Shape**. Local applies only the Particle System transform scale, ignoring any parents. Shape mode applies the scale to the start positions of the particles, but does not affect their size.  
**Play on Awake** Set this to true to make an Audio Source start playing on
awake [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#PlayOnAwake) | If enabled, the Particle System starts automatically when the object is created.  
**Emitter Velocity** | Choose how the Particle System calculates the velocity used by the Inherit Velocity and Emission modules. The system can calculate the velocity using a **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) component, if one exists, or by
tracking the movement of the **Transform component** A Transform component
determines the Position, Rotation, and Scale of each object in the scene.
Every GameObject has a Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent). If no Rigidbody component
exists, the system uses its Transform component by default.  
**Max Particles** | The maximum number of particles in the system at once. If the limit is reached, some particles are removed.  
**Auto Random Seed** | If enabled, the Particle System looks different each time it is played. When set to false, the system is exactly the same every time it is played.  
**Random Seed** | When disabling the automatic random seed, this value is used to create a unique repeatable effect.  
**Stop Action** | When all the particles belonging to the system have finished, it is possible to make the system perform an action. A system is determined to have stopped when all its particles have died, and its age has exceeded its Duration. For looping systems, this only happens if the system is stopped via script.  
Disable | The GameObject is disabled.  
Destroy | The GameObject is destroyed.  
Callback | The OnParticleSystemStopped callback is sent to any **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) attached to the GameObject.  
**Culling Mode** | Choose whether to pause Particle System simulation when particles are offscreen. Culling when offscreen is most efficient, but you may want to continue simulation for off-one effects.  
Automatic | Looping systems use **Pause** , and all other system use **Always Simulate**.  
Pause And Catch-up | The system stops simulating while offscreen. When re-entering the view, the simulation performs a large step to reach the point where it would have been had it not paused. In complex systems, this option can cause performance spikes.  
Pause | The system stops simulating while offscreen.  
Always Simulate | The system processes its simulation on each frame, regardless of whether it is on screen or not. This can be useful for one-shot effects such as fireworks, where during the simulation would be obvious.  
**Ring Buffer Mode** | Keeps particles alive until they reach the **Max Particles** count, at which point new particles recycle the oldest ones, instead of removing particles when their lifetimes elapse.  
Disabled | Disable **Ring Buffer Mode** , so the system removes particles when their lifetime elapses.  
Pause Until Replaced | Pauses old particles at the end of their lifetime until the **Max Particle** limit is reached, at which point the system recycles them, so they reappear as new particles.  
Loop Until Replaced | At the end of their lifetime, particles rewind back to the specified proportion of their lifetime until the **Max Particle** limit is reached, at which point the system recycles them, so they reappear as new particles.  
  
[](activate-access-particle-system-modules.html)

Activate and access Particle System modules

[](PartSysEmissionModule.html)

Emission module reference

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

