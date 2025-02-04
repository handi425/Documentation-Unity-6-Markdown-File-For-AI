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

# ParticleSystem

class in UnityEngine

/

Inherits from:[Component](Component.html)

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

Script interface for the Built-in Particle System. Unity's powerful and
versatile particle system implementation.

**General parameters**  
  
The Particle System's general parameters are kept inside a special Main
module. These parameters are visible in the Inspector above all the other
modules:  
  
![](../StaticFiles/ScriptRefImages/ParticleSystemInspector.png)  
  
In script, these parameters are accessible through
[ParticleSystem.main](ParticleSystem-main.html).  
  
**Accessing module properties**  
  
Particle System properties are grouped by the module they belong to, such as
[ParticleSystem.noise](ParticleSystem-noise.html) and
[ParticleSystem.emission](ParticleSystem-emission.html). These properties are
structs, but do not behave like normal C# structs. They are simply interfaces
directly into the native code, so it is important to know how to use them,
compared to a normal C# struct.  
  
The key difference is that it is not necessary to assign the struct back to
the Particle System component. When you set any property on a module struct,
Unity immediately assigns that value to the Particle System.  
  
Also, because each module is a struct, you must cache it in a local variable
before you can assign any new values to the module. For example, instead of:  
`ParticleSystem.emission.enabled = true; // Doesn't compile`  
write:  
`var emission = ParticleSystem.emission; // Stores the module in a local
variable`  
`emission.enabled = true; // Applies the new value directly to the Particle
System`  
  
  
**Module effect multipliers**  
  
Every module has special multiplier properties that allow you to change the
overall effect of a curve without having to edit the curve itself. These
multiplier properties are all named after the curve they affect - for instance
ParticleSystem.emission.rateMultiplier controls the overall effect of
ParticleSystem.emission.rate in a given system.  
  
**Constant value shorthand**  
  
Parameters support a shorthand notation for simple constant values. To set a
constant value for a parameter, all you need to do is assign a number to it.
It is not necessary to create a [MinMaxCurve](ParticleSystem.MinMaxCurve.html)
or [MinMaxGradient](ParticleSystem.MinMaxGradient.html) object in the
[ParticleSystemCurveMode.Constant](ParticleSystemCurveMode.Constant.html)
mode.  
  
For example, instead of:  
`var emission = ParticleSystem.emission;`  
`emission.rate = new ParticleSystem.MinMaxCurve(5.0f);`  
write:  
`var emission = ParticleSystem.emission;`  
`emission.rate = 5.0f;`  
  
**Performance note** : When setting properties on particle modules, the
settings are passed immediately into native code. This gives the best
performance. This means that setting properties on a module struct doesn't set
something in script that requires setting back to the Particle System; it all
happens automatically.  
  
Additional resources: [Particle](ParticleSystem.Particle.html).

### Properties

[collision](ParticleSystem-collision.html)| Script interface for the
CollisionModule of a Particle System.  
---|---  
[colorBySpeed](ParticleSystem-colorBySpeed.html)| Script interface for the
ColorByLifetimeModule of a Particle System.  
[colorOverLifetime](ParticleSystem-colorOverLifetime.html)| Script interface
for the ColorOverLifetimeModule of a Particle System.  
[customData](ParticleSystem-customData.html)| Script interface for the
CustomDataModule of a Particle System.  
[emission](ParticleSystem-emission.html)| Script interface for the
EmissionModule of a Particle System.  
[externalForces](ParticleSystem-externalForces.html)| Script interface for the
ExternalForcesModule of a Particle System.  
[forceOverLifetime](ParticleSystem-forceOverLifetime.html)| Script interface
for the ForceOverLifetimeModule of a Particle System.  
[has3DParticleRotations](ParticleSystem-has3DParticleRotations.html)|
Determines whether the Particle System rotates its particles around only the Z
axis, or whether the system specifies separate values for the X, Y and Z axes.  
[hasNonUniformParticleSizes](ParticleSystem-hasNonUniformParticleSizes.html)|
Determines whether the Particle System uses a single value for the width and
height (and depth, when using meshes), or if the system specifies different
values for each axis.  
[inheritVelocity](ParticleSystem-inheritVelocity.html)| Script interface for
the InheritVelocityModule of a Particle System.  
[isEmitting](ParticleSystem-isEmitting.html)| Determines whether the Particle
System is emitting particles. A Particle System may stop emitting when its
emission module has finished, it has been paused or if the system has been
stopped using Stop with the StopEmitting flag. Resume emitting by calling
Play.  
[isPaused](ParticleSystem-isPaused.html)| Determines whether the Particle
System is paused.  
[isPlaying](ParticleSystem-isPlaying.html)| Determines whether the Particle
System is playing.  
[isStopped](ParticleSystem-isStopped.html)| Determines whether the Particle
System is in the stopped state.  
[lifetimeByEmitterSpeed](ParticleSystem-lifetimeByEmitterSpeed.html)| Script
interface for the Particle System Lifetime By Emitter Speed module.  
[lights](ParticleSystem-lights.html)| Script interface for the LightsModule of
a Particle System.  
[limitVelocityOverLifetime](ParticleSystem-limitVelocityOverLifetime.html)|
Script interface for the LimitVelocityOverLifetimeModule of a Particle System.
.  
[main](ParticleSystem-main.html)| Access the main Particle System settings.  
[noise](ParticleSystem-noise.html)| Script interface for the NoiseModule of a
Particle System.  
[particleCount](ParticleSystem-particleCount.html)| The current number of
particles (Read Only). The number doesn't include particles of child Particle
Systems  
[proceduralSimulationSupported](ParticleSystem-
proceduralSimulationSupported.html)| Determines whether this system supports
Procedural Simulation.  
[randomSeed](ParticleSystem-randomSeed.html)| Override the random seed used
for the Particle System emission.  
[rotationBySpeed](ParticleSystem-rotationBySpeed.html)| Script interface for
the RotationBySpeedModule of a Particle System.  
[rotationOverLifetime](ParticleSystem-rotationOverLifetime.html)| Script
interface for the RotationOverLifetimeModule of a Particle System.  
[shape](ParticleSystem-shape.html)| Script interface for the ShapeModule of a
Particle System.  
[sizeBySpeed](ParticleSystem-sizeBySpeed.html)| Script interface for the
SizeBySpeedModule of a Particle System.  
[sizeOverLifetime](ParticleSystem-sizeOverLifetime.html)| Script interface for
the SizeOverLifetimeModule of a Particle System.  
[subEmitters](ParticleSystem-subEmitters.html)| Script interface for the
SubEmittersModule of a Particle System.  
[textureSheetAnimation](ParticleSystem-textureSheetAnimation.html)| Script
interface for the TextureSheetAnimationModule of a Particle System.  
[time](ParticleSystem-time.html)| Playback position in seconds.  
[totalTime](ParticleSystem-totalTime.html)| Total playback time in seconds,
including the Start Delay setting.  
[trails](ParticleSystem-trails.html)| Script interface for the TrailsModule of
a Particle System.  
[trigger](ParticleSystem-trigger.html)| Script interface for the TriggerModule
of a Particle System.  
[useAutoRandomSeed](ParticleSystem-useAutoRandomSeed.html)| Controls whether
the Particle System uses an automatically-generated random number to seed the
random number generator.  
[velocityOverLifetime](ParticleSystem-velocityOverLifetime.html)| Script
interface for the VelocityOverLifetimeModule of a Particle System.  
  
### Public Methods

[AllocateAxisOfRotationAttribute](ParticleSystem.AllocateAxisOfRotationAttribute.html)|
Ensures that the axisOfRotations particle attribute array is allocated.  
---|---  
[AllocateCustomDataAttribute](ParticleSystem.AllocateCustomDataAttribute.html)|
Ensures that the customData1 and customData2 particle attribute arrays are
allocated.  
[AllocateMeshIndexAttribute](ParticleSystem.AllocateMeshIndexAttribute.html)|
Ensures that the meshIndices particle attribute array is allocated.  
[Clear](ParticleSystem.Clear.html)| Remove all particles in the Particle
System.  
[Emit](ParticleSystem.Emit.html)| Emit count particles immediately.  
[GetCustomParticleData](ParticleSystem.GetCustomParticleData.html)| Get a
stream of custom per-particle data.  
[GetParticles](ParticleSystem.GetParticles.html)| Gets the particles of this
Particle System.  
[GetPlaybackState](ParticleSystem.GetPlaybackState.html)| Returns all the data
that relates to the current internal state of the Particle System.  
[GetTrails](ParticleSystem.GetTrails.html)| Returns all the data relating to
the current internal state of the Particle System Trails.  
[IsAlive](ParticleSystem.IsAlive.html)| Does the Particle System contain any
live particles, or will it produce more?  
[Pause](ParticleSystem.Pause.html)| Pauses the system so no new particles are
emitted and the existing particles are not updated.  
[Play](ParticleSystem.Play.html)| Starts the Particle System.  
[SetCustomParticleData](ParticleSystem.SetCustomParticleData.html)| Set a
stream of custom per-particle data.  
[SetParticles](ParticleSystem.SetParticles.html)| Sets the particles of this
Particle System.  
[SetPlaybackState](ParticleSystem.SetPlaybackState.html)| Use this method with
the results of an earlier call to ParticleSystem.GetPlaybackState, in order to
restore the Particle System to the state stored in the playbackState object.  
[SetTrails](ParticleSystem.SetTrails.html)| Use this method with the results
of an earlier call to ParticleSystem.GetTrails, in order to restore the
Particle System to the state stored in the Trails object.  
[Simulate](ParticleSystem.Simulate.html)| Fast-forwards the Particle System by
simulating particles over the given period of time, then pauses it.  
[Stop](ParticleSystem.Stop.html)| Stops playing the Particle System using the
supplied stop behaviour.  
[TriggerSubEmitter](ParticleSystem.TriggerSubEmitter.html)| Triggers the
specified sub emitter on all particles of the Particle System.  
  
### Static Methods

[ResetPreMappedBufferMemory](ParticleSystem.ResetPreMappedBufferMemory.html)|
Reset the cache of reserved graphics memory used for efficient rendering of
Particle Systems.  
---|---  
[SetMaximumPreMappedBufferCounts](ParticleSystem.SetMaximumPreMappedBufferCounts.html)|
Limits the amount of graphics memory Unity reserves for efficient rendering of
Particle Systems.  
  
### Inherited Members

### Properties

[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
---|---  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

