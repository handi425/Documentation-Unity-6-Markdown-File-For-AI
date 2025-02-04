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

# PlayableDirector

class in UnityEngine.Playables

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.DirectorModule](UnityEngine.DirectorModule.html)

Leave feedback

  

Implements interfaces:[IExposedPropertyTable](IExposedPropertyTable.html)

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

Instantiates a [PlayableGraph](Playables.PlayableGraph.html) from a
[PlayableAsset](Playables.PlayableAsset.html) and controls playback of
[Playable](Playables.Playable.html) objects.  
This API is mainly designed to provide scheduling and scene binding support
and scheduling for the Timeline package. Our users may find limited use for it
otherwise.  
Most of the functionality of this class can be replicated by using
[PlayableGraph](Playables.PlayableGraph.html).

### Properties

[duration](Playables.PlayableDirector-duration.html)| The duration of the
currently connected Playable in seconds.  
---|---  
[extrapolationMode](Playables.PlayableDirector-extrapolationMode.html)|
Controls how the time is incremented when it goes beyond the duration of the
playable.  
[initialTime](Playables.PlayableDirector-initialTime.html)| The time at which
the Playable should start when first played.  
[playableAsset](Playables.PlayableDirector-playableAsset.html)| The
PlayableAsset that is used to instantiate a playable for playback.  
[playableGraph](Playables.PlayableDirector-playableGraph.html)| The
PlayableGraph created by the PlayableDirector.  
[playOnAwake](Playables.PlayableDirector-playOnAwake.html)| Whether the
playable asset will start playing back as soon as the component awakes.  
[state](Playables.PlayableDirector-state.html)| The current playing state of
the component. (Read Only)  
[time](Playables.PlayableDirector-time.html)| The component's current time.
This value is incremented according to the PlayableDirector.timeUpdateMode
when it is playing. You can also change this value manually.  
[timeUpdateMode](Playables.PlayableDirector-timeUpdateMode.html)| Controls how
time is incremented when playing back.  
  
### Public Methods

[ClearGenericBinding](Playables.PlayableDirector.ClearGenericBinding.html)|
Clears the binding of a reference object.  
---|---  
[ClearReferenceValue](Playables.PlayableDirector.ClearReferenceValue.html)|
Clears an exposed reference value.  
[DeferredEvaluate](Playables.PlayableDirector.DeferredEvaluate.html)|
Schedules the PlayableDirector to perform PlayableGraph.Evaluate on the
PlayableGraph associated with the PlayableDirector.playableAsset on the next
update.  
[Evaluate](Playables.PlayableDirector.Evaluate.html)| Immediately performs
PlayableGraph.Evaluate on the PlayableGraph associated with the
PlayableDirector.playableAsset at PlayableDirector.time.  
[GetGenericBinding](Playables.PlayableDirector.GetGenericBinding.html)|
Returns a binding to a reference object.  
[GetReferenceValue](Playables.PlayableDirector.GetReferenceValue.html)|
Retreives an ExposedReference binding.  
[Pause](Playables.PlayableDirector.Pause.html)| Pauses playback of the
currently running playable.  
[Play](Playables.PlayableDirector.Play.html)| Instatiates a Playable using the
provided PlayableAsset and starts playback.  
[RebindPlayableGraphOutputs](Playables.PlayableDirector.RebindPlayableGraphOutputs.html)|
Rebinds each PlayableOutput of the PlayableGraph.  
[RebuildGraph](Playables.PlayableDirector.RebuildGraph.html)| Discards the
existing PlayableGraph and creates a new instance.  
[Resume](Playables.PlayableDirector.Resume.html)| Resume playing a paused
playable.  
[SetGenericBinding](Playables.PlayableDirector.SetGenericBinding.html)| Sets
the binding of a reference object from a PlayableBinding.  
[SetReferenceValue](Playables.PlayableDirector.SetReferenceValue.html)| Sets
an ExposedReference value.  
[Stop](Playables.PlayableDirector.Stop.html)| Stops playback of the current
Playable and destroys the corresponding graph.  
  
### Events

[paused](Playables.PlayableDirector-paused.html)| Event that is raised when a
PlayableDirector component has paused.  
---|---  
[played](Playables.PlayableDirector-played.html)| Event that is raised when a
PlayableDirector component has begun playing.  
[stopped](Playables.PlayableDirector-stopped.html)| Event that is raised when
a PlayableDirector component has stopped.  
  
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

