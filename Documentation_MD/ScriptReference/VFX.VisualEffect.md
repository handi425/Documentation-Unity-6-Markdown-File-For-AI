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

# VisualEffect

class in UnityEngine.VFX

/

Inherits from:[Behaviour](Behaviour.html)

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

The visual effect class that references an
[VisualEffectAsset](VFX.VisualEffectAsset.html) instance within the Scene.

### Properties

[aliveParticleCount](VFX.VisualEffect-aliveParticleCount.html)| Returns the
sum of all alive particles within the visual effect.  
---|---  
[culled](VFX.VisualEffect-culled.html)| Use this property to determine if this
visual effect is not visible from any Camera. (Read Only)  
[initialEventID](VFX.VisualEffect-initialEventID.html)| The default event name
ID. To retrieve this value, use the Shader.PropertyID after VisualEffect has
awakened or after you've invoked VisualEffect.Reinit.  
[initialEventName](VFX.VisualEffect-initialEventName.html)| The default event
name. Unity calls this event when the VisualEffect awakes, or when you call
VisualEffect.Reinit.  
[outputEventReceived](VFX.VisualEffect-outputEventReceived.html)| Output event
are reported trough this callback.  
[pause](VFX.VisualEffect-pause.html)| Use this property to set the pause state
of the visual effect.  
[playRate](VFX.VisualEffect-playRate.html)| A multiplier that Unity applies to
the delta time when it updates the VisualEffect. The default value is 1.0f.  
[resetSeedOnPlay](VFX.VisualEffect-resetSeedOnPlay.html)| This property
controls whether the visual effect generates a new seed for the random number
generator with each call to VisualEffect.Play function.  
[startSeed](VFX.VisualEffect-startSeed.html)| The initial seed used for
internal random number generator.  
[visualEffectAsset](VFX.VisualEffect-visualEffectAsset.html)| The
VisualEffectAsset that the VisualEffect uses.  
  
### Constructors

[VisualEffect](VFX.VisualEffect-ctor.html)| The VisualEffect constructor.  
---|---  
  
### Public Methods

[AdvanceOneFrame](VFX.VisualEffect.AdvanceOneFrame.html)| If
VisualEffect.pause is true, this method processes the next visual effect
update for exactly one frame with the current delta time.  
---|---  
[CreateVFXEventAttribute](VFX.VisualEffect.CreateVFXEventAttribute.html)| Use
this method to create a new VFXEventAttribute.  
[GetAnimationCurve](VFX.VisualEffect.GetAnimationCurve.html)| Gets the value
of a named Animation Curve property.  
[GetBool](VFX.VisualEffect.GetBool.html)| Gets the value of a named bool
property.  
[GetFloat](VFX.VisualEffect.GetFloat.html)| Gets the value of a named float
property.  
[GetGradient](VFX.VisualEffect.GetGradient.html)| Gets the value of a named
Gradient property.  
[GetInt](VFX.VisualEffect.GetInt.html)| Get a named exposed integer.  
[GetMatrix4x4](VFX.VisualEffect.GetMatrix4x4.html)| Gets the value of a named
Matrix4x4 property.  
[GetMesh](VFX.VisualEffect.GetMesh.html)| Gets the value of a named Mesh
property.  
[GetOutputEventNames](VFX.VisualEffect.GetOutputEventNames.html)| Gets the
name of every output event system.  
[GetParticleSystemInfo](VFX.VisualEffect.GetParticleSystemInfo.html)| Gets
information on a particle system.  
[GetParticleSystemNames](VFX.VisualEffect.GetParticleSystemNames.html)| Gets
the name of every particle system.  
[GetSkinnedMeshRenderer](VFX.VisualEffect.GetSkinnedMeshRenderer.html)| Gets
the value of a named Skinned Mesh Renderer property.  
[GetSpawnSystemInfo](VFX.VisualEffect.GetSpawnSystemInfo.html)| Gets state on
a spawn system.  
[GetSpawnSystemNames](VFX.VisualEffect.GetSpawnSystemNames.html)| Gets the
name of every spawn system.  
[GetSystemNames](VFX.VisualEffect.GetSystemNames.html)| Gets the name of every
system.  
[GetTexture](VFX.VisualEffect.GetTexture.html)| Gets the value of a named
texture property.  
[GetTextureDimension](VFX.VisualEffect.GetTextureDimension.html)| Gets
expected texture dimension for a named exposed texture.  
[GetUInt](VFX.VisualEffect.GetUInt.html)| Gets the value of a named unsigned
integer property.  
[GetVector2](VFX.VisualEffect.GetVector2.html)| Gets the value of a named
Vector2 property.  
[GetVector3](VFX.VisualEffect.GetVector3.html)| Gets the value of a named
Vector3 property.  
[GetVector4](VFX.VisualEffect.GetVector4.html)| Gets the value of a named
Vector4 or Color property.  
[HasAnimationCurve](VFX.VisualEffect.HasAnimationCurve.html)| Checks if the
Visual Effect can override an Animation Curve with the name you pass in.  
[HasAnySystemAwake](VFX.VisualEffect.HasAnySystemAwake.html)| Checks if any
particle system in the effect is awake.  
[HasBool](VFX.VisualEffect.HasBool.html)| Checks if the Visual Effect can
override a bool with the name you pass in.  
[HasFloat](VFX.VisualEffect.HasFloat.html)| Checks if the Visual Effect can
override a float with the name you pass in.  
[HasGradient](VFX.VisualEffect.HasGradient.html)| Checks if the Visual Effect
can override a Gradient with the name you pass in.  
[HasGraphicsBuffer](VFX.VisualEffect.HasGraphicsBuffer.html)| Checks if the
Visual Effect can override a GraphicsBuffer with the name you pass in.  
[HasInt](VFX.VisualEffect.HasInt.html)| Checks if the Visual Effect can
override an integer with the name you pass in.  
[HasMatrix4x4](VFX.VisualEffect.HasMatrix4x4.html)| Checks if the Visual
Effect can override a Matrix4x4 with the name you pass in.  
[HasMesh](VFX.VisualEffect.HasMesh.html)| Checks if the Visual Effect can
override a Mesh with the name you pass in.  
[HasSkinnedMeshRenderer](VFX.VisualEffect.HasSkinnedMeshRenderer.html)| Checks
if the Visual Effect can override a Skinned Mesh Renderer with the name you
pass in.  
[HasSystem](VFX.VisualEffect.HasSystem.html)| Use this function to determine
if the VisualEffect has the system you pass in.  
[HasTexture](VFX.VisualEffect.HasTexture.html)| Checks if the Visual Effect
can override a texture with the name you pass in.  
[HasUInt](VFX.VisualEffect.HasUInt.html)| Checks if the Visual Effect can
override an unsigned integer with the name you pass in.  
[HasVector2](VFX.VisualEffect.HasVector2.html)| Checks if the Visual Effect
can override a Vector2 with the name you pass in.  
[HasVector3](VFX.VisualEffect.HasVector3.html)| Checks if the Visual Effect
can override a Vector3 with the name you pass in.  
[HasVector4](VFX.VisualEffect.HasVector4.html)| Checks if the Visual Effect
can override a Vector4 or Color with the name you pass in.  
[Play](VFX.VisualEffect.Play.html)| Use this method to send a play event to
every Spawn system.  
[Reinit](VFX.VisualEffect.Reinit.html)| Reintialize visual effect.  
[ResetOverride](VFX.VisualEffect.ResetOverride.html)| Use this method to set
the overridden state to false. This restores the default value that the Visual
Effect Asset specifies.  
[SendEvent](VFX.VisualEffect.SendEvent.html)| Use this method to send a custom
named event.  
[SetAnimationCurve](VFX.VisualEffect.SetAnimationCurve.html)| Sets the value
of a named Animation Curve property.  
[SetBool](VFX.VisualEffect.SetBool.html)| Sets the value of a named bool
property.  
[SetFloat](VFX.VisualEffect.SetFloat.html)| Sets the value of a named float
property.  
[SetGradient](VFX.VisualEffect.SetGradient.html)| Sets the value of a named
Gradient property.  
[SetGraphicsBuffer](VFX.VisualEffect.SetGraphicsBuffer.html)| Sets the value
of a named GraphicsBuffer property.  
[SetInt](VFX.VisualEffect.SetInt.html)| Sets the value of a named integer
property.  
[SetMatrix4x4](VFX.VisualEffect.SetMatrix4x4.html)| Sets the value of a named
Matrix4x4 property.  
[SetMesh](VFX.VisualEffect.SetMesh.html)| Sets the value of a named Mesh
property.  
[SetSkinnedMeshRenderer](VFX.VisualEffect.SetSkinnedMeshRenderer.html)| Sets
the value of a named Skinned Mesh Renderer property.  
[SetTexture](VFX.VisualEffect.SetTexture.html)| Sets the value of a named
texture property.  
[SetUInt](VFX.VisualEffect.SetUInt.html)| Sets the value of a named unsigned
integer property.  
[SetVector2](VFX.VisualEffect.SetVector2.html)| Sets the value of a named
Vector2 property.  
[SetVector3](VFX.VisualEffect.SetVector3.html)| Sets the value of a named
Vector3 property.  
[SetVector4](VFX.VisualEffect.SetVector4.html)| Sets the value of a named
Vector4 or Color property.  
[Simulate](VFX.VisualEffect.Simulate.html)| Use this method to fast-forward
the visual effect by simulating all systems for several step counts using the
specified delta time.  
[Stop](VFX.VisualEffect.Stop.html)| Use this method to send a stop event to
all Spawn systems.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
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

