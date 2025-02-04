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

# UnityEngine.ParticleSystemModule

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

[ ]()

### Description

The ParticleSystem module implements Unity's Particle System.

### Classes

[IJobParticleSystemExtensions](ParticleSystemJobs.IJobParticleSystemExtensions.html)|
Extension methods for Jobs using the IJobParticleSystem interface.  
---|---  
[IJobParticleSystemParallelForBatchExtensions](ParticleSystemJobs.IJobParticleSystemParallelForBatchExtensions.html)|
Extension methods for Jobs using the IJobParticleSystemParallelForBatch
interface.  
[IJobParticleSystemParallelForExtensions](ParticleSystemJobs.IJobParticleSystemParallelForExtensions.html)|
Extension methods for Jobs using the IJobParticleSystemParallelFor interface.  
[ParticlePhysicsExtensions](ParticlePhysicsExtensions.html)| Method extension
for Physics in Particle System.  
[ParticleSystem](ParticleSystem.html)| Script interface for the Built-in
Particle System. Unity's powerful and versatile particle system
implementation.  
[ParticleSystemForceField](ParticleSystemForceField.html)| Script interface
for Particle System Force Fields.  
[ParticleSystemRenderer](ParticleSystemRenderer.html)| Use this class to
render particles on to the screen.  
  
### Structs

[ParticleCollisionEvent](ParticleCollisionEvent.html)| Information about a
particle collision.  
---|---  
[ParticleSystemJobData](ParticleSystemJobs.ParticleSystemJobData.html)| This
struct specifies all the per-particle data.  
[ParticleSystemNativeArray3](ParticleSystemJobs.ParticleSystemNativeArray3.html)|
A container to hold x, y, and z-axis data for particles.  
[ParticleSystemNativeArray4](ParticleSystemJobs.ParticleSystemNativeArray4.html)|
A container to hold 4 arrays of data for particles.  
  
### Enumerations

[ParticleSystemAnimationMode](ParticleSystemAnimationMode.html)| The animation
mode.  
---|---  
[ParticleSystemAnimationRowMode](ParticleSystemAnimationRowMode.html)| The
mode used for selecting rows of an animation in the Texture Sheet Animation
Module.  
[ParticleSystemAnimationTimeMode](ParticleSystemAnimationTimeMode.html)|
Control how animation frames are selected.  
[ParticleSystemAnimationType](ParticleSystemAnimationType.html)| The animation
type.  
[ParticleSystemBakeMeshOptions](ParticleSystemBakeMeshOptions.html)| Configure
how a Particle System is baked into a mesh.  
[ParticleSystemBakeTextureOptions](ParticleSystemBakeTextureOptions.html)|
Configure how a Particle System is baked into a texture.  
[ParticleSystemColliderQueryMode](ParticleSystemColliderQueryMode.html)|
Whether collider information is available when using the
[[ParticleSystem::GetTriggerParticles]] method.  
[ParticleSystemCollisionMode](ParticleSystemCollisionMode.html)| Whether to
use 2D or 3D colliders for particle collisions.  
[ParticleSystemCollisionQuality](ParticleSystemCollisionQuality.html)| Quality
of world collisions. Medium and low quality are approximate and may leak
particles.  
[ParticleSystemCollisionType](ParticleSystemCollisionType.html)| The type of
collisions to use for a given Particle System.  
[ParticleSystemCullingMode](ParticleSystemCullingMode.html)| The action to
perform when the Particle System is offscreen.  
[ParticleSystemCurveMode](ParticleSystemCurveMode.html)| The particle curve
mode.  
[ParticleSystemCustomData](ParticleSystemCustomData.html)| Which stream of
custom particle data to set.  
[ParticleSystemCustomDataMode](ParticleSystemCustomDataMode.html)| Which mode
CustomDataModule uses to generate its data.  
[ParticleSystemEmitterVelocityMode](ParticleSystemEmitterVelocityMode.html)|
Control how a Particle System calculates its velocity.  
[ParticleSystemForceFieldShape](ParticleSystemForceFieldShape.html)| The type
of shape used for influencing particles in the Force Field Component.  
[ParticleSystemGameObjectFilter](ParticleSystemGameObjectFilter.html)| The
particle GameObject filtering mode that specifies which objects are used by
specific Particle System modules.  
[ParticleSystemGradientMode](ParticleSystemGradientMode.html)| The particle
gradient mode.  
[ParticleSystemGravitySource](ParticleSystemGravitySource.html)| Options for
which physics system to use the gravity setting from.  
[ParticleSystemInheritVelocityMode](ParticleSystemInheritVelocityMode.html)|
How to apply emitter velocity to particles.  
[ParticleSystemMeshDistribution](ParticleSystemMeshDistribution.html)| Sets
which method Unity uses to randomly assign Meshes to particles.  
[ParticleSystemMeshShapeType](ParticleSystemMeshShapeType.html)| The mesh
emission type.  
[ParticleSystemNoiseQuality](ParticleSystemNoiseQuality.html)| The quality of
the generated noise.  
[ParticleSystemOverlapAction](ParticleSystemOverlapAction.html)| What action
to perform when the particle trigger module passes a test.  
[ParticleSystemRenderMode](ParticleSystemRenderMode.html)| The rendering mode
for particle systems.  
[ParticleSystemRenderSpace](ParticleSystemRenderSpace.html)| How particles are
aligned when rendered.  
[ParticleSystemRingBufferMode](ParticleSystemRingBufferMode.html)| Control how
particles are removed from the Particle System.  
[ParticleSystemScalingMode](ParticleSystemScalingMode.html)| Control how
particle systems apply transform scale.  
[ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html)|
The mode used to generate new points in a shape.  
[ParticleSystemShapeTextureChannel](ParticleSystemShapeTextureChannel.html)|
The texture channel.  
[ParticleSystemShapeType](ParticleSystemShapeType.html)| The emission shape.  
[ParticleSystemSimulationSpace](ParticleSystemSimulationSpace.html)| The space
to simulate particles in.  
[ParticleSystemSortMode](ParticleSystemSortMode.html)| The sorting mode for
particle systems.  
[ParticleSystemStopAction](ParticleSystemStopAction.html)| The action to
perform when the Particle System stops.  
[ParticleSystemStopBehavior](ParticleSystemStopBehavior.html)| The behavior to
apply when calling Stop.  
[ParticleSystemSubEmitterProperties](ParticleSystemSubEmitterProperties.html)|
The properties of sub-emitter particles.  
[ParticleSystemSubEmitterType](ParticleSystemSubEmitterType.html)| The events
that cause new particles to be spawned.  
[ParticleSystemTrailMode](ParticleSystemTrailMode.html)| Choose how Particle
Trails are generated.  
[ParticleSystemTrailTextureMode](ParticleSystemTrailTextureMode.html)| Choose
how textures are applied to Particle Trails.  
[ParticleSystemTriggerEventType](ParticleSystemTriggerEventType.html)| The
different types of particle triggers.  
[ParticleSystemVertexStream](ParticleSystemVertexStream.html)| All possible
Particle System vertex shader inputs.  
[UVChannelFlags](Rendering.UVChannelFlags.html)| A flag representing each UV
channel.  
  
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

