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

# Cloth

class in UnityEngine

/

Inherits from:[Component](Component.html)

/

Implemented in:[UnityEngine.ClothModule](UnityEngine.ClothModule.html)

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

[Switch to Manual](../Manual/class-Cloth.html "Go to Cloth Component in the
Manual")

### Description

The Cloth class provides an interface to cloth simulation physics.

### Properties

[bendingStiffness](Cloth-bendingStiffness.html)| Bending stiffness of the
cloth.  
---|---  
[capsuleColliders](Cloth-capsuleColliders.html)| An array of CapsuleColliders
which this Cloth instance should collide with.  
[clothSolverFrequency](Cloth-clothSolverFrequency.html)| Number of cloth
solver iterations per second.  
[coefficients](Cloth-coefficients.html)| The cloth skinning coefficients used
to set up how the cloth interacts with the skinned mesh.  
[collisionMassScale](Cloth-collisionMassScale.html)| How much to increase mass
of colliding particles.  
[damping](Cloth-damping.html)| Damp cloth motion.  
[enableContinuousCollision](Cloth-enableContinuousCollision.html)| Enable
continuous collision to improve collision stability.  
[enabled](Cloth-enabled.html)| Is this cloth enabled?  
[externalAcceleration](Cloth-externalAcceleration.html)| A constant, external
acceleration applied to the cloth.  
[friction](Cloth-friction.html)| The friction of the cloth when colliding with
the character.  
[normals](Cloth-normals.html)| The current normals of the cloth object.  
[randomAcceleration](Cloth-randomAcceleration.html)| A random, external
acceleration applied to the cloth.  
[selfCollisionDistance](Cloth-selfCollisionDistance.html)| Minimum distance at
which two cloth particles repel each other (default: 0.0).  
[selfCollisionStiffness](Cloth-selfCollisionStiffness.html)| Self-collision
stiffness defines how strong the separating impulse should be for colliding
particles.  
[sleepThreshold](Cloth-sleepThreshold.html)| Cloth's sleep threshold.  
[sphereColliders](Cloth-sphereColliders.html)| An array of
ClothSphereColliderPairs which this Cloth instance should collide with.  
[stiffnessFrequency](Cloth-stiffnessFrequency.html)| Sets the stiffness
frequency parameter.  
[stretchingStiffness](Cloth-stretchingStiffness.html)| Stretching stiffness of
the cloth.  
[useGravity](Cloth-useGravity.html)| Should gravity affect the cloth
simulation?  
[useTethers](Cloth-useTethers.html)| Use Tether Anchors.  
[useVirtualParticles](Cloth-useVirtualParticles.html)| Add one virtual
particle per triangle to improve collision stability.  
[vertices](Cloth-vertices.html)| The current vertex positions of the cloth
object.  
[worldAccelerationScale](Cloth-worldAccelerationScale.html)| How much world-
space acceleration of the character will affect cloth vertices.  
[worldVelocityScale](Cloth-worldVelocityScale.html)| How much world-space
movement of the character will affect cloth vertices.  
  
### Public Methods

[ClearTransformMotion](Cloth.ClearTransformMotion.html)| Clear the pending
transform changes from affecting the cloth simulation.  
---|---  
[GetSelfAndInterCollisionIndices](Cloth.GetSelfAndInterCollisionIndices.html)|
Get list of particles to be used for self and inter collision.  
[GetVirtualParticleIndices](Cloth.GetVirtualParticleIndices.html)| Get list of
indices to be used when generating virtual particles.  
[GetVirtualParticleWeights](Cloth.GetVirtualParticleWeights.html)| Get weights
to be used when generating virtual particles for cloth.  
[SetEnabledFading](Cloth.SetEnabledFading.html)| Fade the cloth simulation in
or out.  
[SetSelfAndInterCollisionIndices](Cloth.SetSelfAndInterCollisionIndices.html)|
This allows you to set the cloth indices used for self and inter collision.  
[SetVirtualParticleIndices](Cloth.SetVirtualParticleIndices.html)| Set indices
to use when generating virtual particles.  
[SetVirtualParticleWeights](Cloth.SetVirtualParticleWeights.html)| Sets
weights to be used when generating virtual particles for cloth.  
  
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

