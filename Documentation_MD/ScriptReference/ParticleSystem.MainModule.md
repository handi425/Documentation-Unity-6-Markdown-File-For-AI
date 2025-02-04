[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# MainModule

struct in UnityEngine

/

Implemented
in:[UnityEngine.ParticleSystemModule](UnityEngine.ParticleSystemModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

### Description

Script interface for the MainModule of a Particle System.

Additional resources: [ParticleSystem](ParticleSystem.html),
[ParticleSystem.main](ParticleSystem-main.html).

### Properties

[cullingMode](ParticleSystem.MainModule-cullingMode.html)| Configure whether
the Particle System will still be simulated each frame, when it is offscreen.  
---|---  
[customSimulationSpace](ParticleSystem.MainModule-customSimulationSpace.html)|
Simulate particles relative to a custom transform component.  
[duration](ParticleSystem.MainModule-duration.html)| The duration of the
Particle System in seconds.  
[emitterVelocity](ParticleSystem.MainModule-emitterVelocity.html)| The current
Particle System velocity.  
[emitterVelocityMode](ParticleSystem.MainModule-emitterVelocityMode.html)|
Control how the Particle System calculates its velocity, when moving in the
world.  
[flipRotation](ParticleSystem.MainModule-flipRotation.html)| Makes some
particles spin in the opposite direction.  
[gravityModifier](ParticleSystem.MainModule-gravityModifier.html)| A scale
that this Particle System applies to gravity, defined either by
Physics.gravity or [Physics2D.gravity]].  
[gravityModifierMultiplier](ParticleSystem.MainModule-
gravityModifierMultiplier.html)| Change the gravity multiplier.  
[gravitySource](ParticleSystem.MainModule-gravitySource.html)| Specify whether
to use the gravity strength from the 2D or 3D physics system.  
[loop](ParticleSystem.MainModule-loop.html)| Specifies whether the Particle
System is looping.  
[maxParticles](ParticleSystem.MainModule-maxParticles.html)| The maximum
number of particles to emit.  
[playOnAwake](ParticleSystem.MainModule-playOnAwake.html)| If set to true, the
Particle System automatically begins to play on startup.  
[prewarm](ParticleSystem.MainModule-prewarm.html)| If
ParticleSystem.MainModule.loop is true, when you enable this property, the
Particle System looks like it has already simulated for one loop when first
becoming visible.  
[ringBufferLoopRange](ParticleSystem.MainModule-ringBufferLoopRange.html)|
When ParticleSystem.MainModule.ringBufferMode is set to loop, this value
defines the proportion of the particle life that loops.  
[ringBufferMode](ParticleSystem.MainModule-ringBufferMode.html)| Configure the
Particle System to not kill its particles when their lifetimes are exceeded.  
[scalingMode](ParticleSystem.MainModule-scalingMode.html)| Control how the
Particle System applies its Transform component to the particles it emits.  
[simulationSpace](ParticleSystem.MainModule-simulationSpace.html)| This
selects the space in which to simulate particles. It can be either world or
local space.  
[simulationSpeed](ParticleSystem.MainModule-simulationSpeed.html)| Override
the default playback speed of the Particle System.  
[startColor](ParticleSystem.MainModule-startColor.html)| The initial color of
particles when the Particle System first spawns them.  
[startDelay](ParticleSystem.MainModule-startDelay.html)| Start delay in
seconds.  
[startDelayMultiplier](ParticleSystem.MainModule-startDelayMultiplier.html)| A
multiplier for ParticleSystem.MainModule.startDelay in seconds.  
[startLifetime](ParticleSystem.MainModule-startLifetime.html)| The total
lifetime in seconds that each new particle has.  
[startLifetimeMultiplier](ParticleSystem.MainModule-
startLifetimeMultiplier.html)| A multiplier for
ParticleSystem.MainModule.startLifetime.  
[startRotation](ParticleSystem.MainModule-startRotation.html)| The initial
rotation of particles when the Particle System first spawns them.  
[startRotation3D](ParticleSystem.MainModule-startRotation3D.html)| A flag to
enable 3D particle rotation.  
[startRotationMultiplier](ParticleSystem.MainModule-
startRotationMultiplier.html)| A multiplier for
ParticleSystem.MainModule.startRotation.  
[startRotationX](ParticleSystem.MainModule-startRotationX.html)| The initial
rotation of particles around the x-axis when emitted.  
[startRotationXMultiplier](ParticleSystem.MainModule-
startRotationXMultiplier.html)| The initial rotation multiplier of particles
around the x-axis when the Particle System first spawns them.  
[startRotationY](ParticleSystem.MainModule-startRotationY.html)| The initial
rotation of particles around the y-axis when the Particle System first spawns
them.  
[startRotationYMultiplier](ParticleSystem.MainModule-
startRotationYMultiplier.html)| The initial rotation multiplier of particles
around the y-axis when the Particle System first spawns them..  
[startRotationZ](ParticleSystem.MainModule-startRotationZ.html)| The initial
rotation of particles around the z-axis when the Particle System first spawns
them  
[startRotationZMultiplier](ParticleSystem.MainModule-
startRotationZMultiplier.html)| The initial rotation multiplier of particles
around the z-axis when the Particle System first spawns them.  
[startSize](ParticleSystem.MainModule-startSize.html)| The initial size of
particles when the Particle System first spawns them.  
[startSize3D](ParticleSystem.MainModule-startSize3D.html)| A flag to enable
specifying particle size individually for each axis.  
[startSizeMultiplier](ParticleSystem.MainModule-startSizeMultiplier.html)| A
multiplier for the initial size of particles when the Particle System first
spawns them.  
[startSizeX](ParticleSystem.MainModule-startSizeX.html)| The initial size of
particles along the x-axis when the Particle System first spawns them.  
[startSizeXMultiplier](ParticleSystem.MainModule-startSizeXMultiplier.html)| A
multiplier for ParticleSystem.MainModule.startSizeX.  
[startSizeY](ParticleSystem.MainModule-startSizeY.html)| The initial size of
particles along the y-axis when the Particle System first spawns them.  
[startSizeYMultiplier](ParticleSystem.MainModule-startSizeYMultiplier.html)| A
multiplier for ParticleSystem.MainModule.startSizeY.  
[startSizeZ](ParticleSystem.MainModule-startSizeZ.html)| The initial size of
particles along the z-axis when the Particle System first spawns them.  
[startSizeZMultiplier](ParticleSystem.MainModule-startSizeZMultiplier.html)| A
multiplier for ParticleSystem.MainModule.startSizeZ.  
[startSpeed](ParticleSystem.MainModule-startSpeed.html)| The initial speed of
particles when the Particle System first spawns them.  
[startSpeedMultiplier](ParticleSystem.MainModule-startSpeedMultiplier.html)| A
multiplier for ParticleSystem.MainModule.startSpeed.  
[stopAction](ParticleSystem.MainModule-stopAction.html)| Select whether to
Disable or Destroy the GameObject, or to call the
MonoBehaviour.OnParticleSystemStopped script Callback, when the Particle
System stops and all particles have died.  
[useUnscaledTime](ParticleSystem.MainModule-useUnscaledTime.html)| When true,
use the unscaled delta time to simulate the Particle System. Otherwise, use
the scaled delta time.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

