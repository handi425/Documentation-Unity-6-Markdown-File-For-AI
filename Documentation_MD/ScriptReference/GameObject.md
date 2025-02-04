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

# GameObject

class in UnityEngine

/

Inherits from:[Object](Object.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

### Description

Base class for all objects that can exist in a scene. Add components to a
GameObject to control its appearance and behavior.

The `GameObject` is the fundamental object type in Unity. Use `GameObject` to
represent everything in your project, including characters, props, and
scenery. A `GameObject` acts as a container for functional
[components](Component.html) that determine how the GameObject looks and
behaves.  
  
Any script that derives from [MonoBehaviour](MonoBehaviour.html) can be added
to a `GameObject` as a component. Use the [Component.gameObject](Component-
gameObject.html) property from your `MonoBehaviour` code to access the
`GameObject` the component is attached to.  
  
`MonoBehaviour` [event functions](../Manual/event-functions.html) such as the
regular per-frame `MonoBehaviour.Update` allow you to make the object
responsive to events. To receive these event callbacks the `GameObject` must
be active in the scene, which means both the `activeSelf` and
`activeInHierarchy` properties must be `true`.  
  
You can create an empty `GameObject` from code by invoking one of the
[constructors](GameObject-ctor.html). However, a more common method is to
instantiate a `GameObject` in [Prefab](../Manual/Prefabs.html) form, with
preconfigured components, property values, and child objects. For more
information, refer to [Instantiating Prefabs at
runtime](../Manual/instantiating-prefabs.html) in the Manual.  
  
You can modify many of the properties of this class in the Editor using the
Inspector window. For a more comprehensive guide to using the GameObject
class, refer to [GameObject](../Manual/class-GameObject.html) in the Manual.  
  
The following example creates a `GameObject` named "myExampleGO" and adds a
component of type [AudioSource](AudioSource.html):

    
    
      using UnityEngine;  
      
      public class Example_GameObject : [MonoBehaviour](MonoBehaviour.html)
      {
          private void Start()
          {
              [GameObject](GameObject.html) myExampleGO = new [GameObject](GameObject.html)("myExampleGO", typeof([AudioSource](AudioSource.html)));
          }
      }
    

Additional resources: [Component](Component.html).

### Properties

[activeInHierarchy](GameObject-activeInHierarchy.html)| The active state of
the GameObject in the Scene hierarchy. True if active, false if inactive.
(Read Only)  
---|---  
[activeSelf](GameObject-activeSelf.html)| The local active state of the
GameObject. True if active, false if inactive. (Read Only)  
[isStatic](GameObject-isStatic.html)| Whether there are any Static Editor
Flags set for the GameObject.  
[layer](GameObject-layer.html)| Integer identifying the layer the GameObject
is assigned to.  
[scene](GameObject-scene.html)| The Scene that contains the GameObject.  
[sceneCullingMask](GameObject-sceneCullingMask.html)| The Scene culling mask
defined for the GameObject. (Read Only)  
[tag](GameObject-tag.html)| The tag assigned to the GameObject.  
[transform](GameObject-transform.html)| The Transform attached to the
GameObject (Read Only).  
  
### Constructors

[GameObject](GameObject-ctor.html)| Creates a new GameObject, with optional
parameters to specify a name and set of components to attach.  
---|---  
  
### Public Methods

[AddComponent](GameObject.AddComponent.html)| Adds a component of the
specified type to the GameObject.  
---|---  
[BroadcastMessage](GameObject.BroadcastMessage.html)| Calls the specified
method on every MonoBehaviour attached to the GameObject or any of its
children.  
[CompareTag](GameObject.CompareTag.html)| Checks if the specified tag is
attached to the GameObject.  
[GetComponent](GameObject.GetComponent.html)| Retrieves a reference to a
component of the specified type, by providing the component type as a type
parameter to the generic method.  
[GetComponentAtIndex](GameObject.GetComponentAtIndex.html)| Retrieves a
reference to a component at a specified index of the GameObject's array of
components.  
[GetComponentCount](GameObject.GetComponentCount.html)| Retrieves the total
number of components currently attached to the GameObject.  
[GetComponentInChildren](GameObject.GetComponentInChildren.html)| Retrieves a
reference to a component of type T on the specified GameObject, or any child
of the GameObject.  
[GetComponentIndex](GameObject.GetComponentIndex.html)| Retrieves the index of
the specified component in the array of components attached to the GameObject.  
[GetComponentInParent](GameObject.GetComponentInParent.html)| Retrieves a
reference to a component of type T on the specified GameObject, or any parent
of the GameObject.  
[GetComponents](GameObject.GetComponents.html)| Retrieves references to all
components of type T on the specified GameObject.  
[GetComponentsInChildren](GameObject.GetComponentsInChildren.html)| Retrieves
references to all components of type T on the specified GameObject, and any
child of the GameObject.  
[GetComponentsInParent](GameObject.GetComponentsInParent.html)| Retrieves
references to all components of type T on the specified GameObject, and any
parent of the GameObject.  
[SendMessage](GameObject.SendMessage.html)| Calls the specified method on
every MonoBehaviour attached to the GameObject.  
[SendMessageUpwards](GameObject.SendMessageUpwards.html)| Calls the specified
method on every MonoBehaviour attached to the GameObject and on every ancestor
of the behaviour.  
[SetActive](GameObject.SetActive.html)| Activates or deactivates the
GameObject locally, according to the value of the supplied parameter.  
[TryGetComponent](GameObject.TryGetComponent.html)| Retrieves the component of
the specified type, if it exists.  
  
### Static Methods

[CreatePrimitive](GameObject.CreatePrimitive.html)| Creates a GameObject of
the specified PrimtiveType with a mesh renderer and appropriate collider.  
---|---  
[Find](GameObject.Find.html)| Finds and returns a GameObject with the
specified name.  
[FindGameObjectsWithTag](GameObject.FindGameObjectsWithTag.html)| Retrieves an
array of all active GameObjects tagged with the specified tag. Returns an
empty array if no GameObjects have the tag.  
[FindWithTag](GameObject.FindWithTag.html)| Retrieves the first active
GameObject tagged with the specified tag. Returns null if no GameObject has
the tag.  
[GetScene](GameObject.GetScene.html)| Retrieves the Scene which contains the
GameObject with the specified instance ID.  
[InstantiateGameObjects](GameObject.InstantiateGameObjects.html)| Creates a
specified number of instances of a GameObject identified by its instance ID
and populates NativeArrays with the instance IDs of the new GameObjects and
their Transform components.  
[SetGameObjectsActive](GameObject.SetGameObjectsActive.html)| Activates or
deactivates multiple GameObjects identified by instance ID.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
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

