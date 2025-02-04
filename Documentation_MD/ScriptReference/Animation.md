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

# Animation

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

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

[Switch to Manual](../Manual/class-Animation.html "Go to Animation Component
in the Manual")

### Description

The animation component is used to play back animations.

You can assign animation clips to the animation component and control playback
from your script. The animation system in Unity is weight-based and supports
Animation Blending, Additive animations, Animation Mixing, Layers and full
control over all aspects of playback.  
  
For an overview of animation scripting in Unity please [read this
introduction](../Manual/AnimationOverview.html).  
  
[AnimationState](AnimationState.html) can be used to change the layer of an
animation, modify playback speed, and for direct control over blending and
mixing.  
  
Also [Animation](Animation.html) supports enumerators. Looping through all
AnimationStates is performed like this:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Animation](Animation.html) anim;  
      
        void Start()
        {
            anim = GetComponent<[Animation](Animation.html)>();
            foreach ([AnimationState](AnimationState.html) state in anim)
            {
                state.speed = 0.5F;
            }
        }
    }
    

Additional resources: An overview of animation scripting in Unity is
[here](../Manual/AnimationOverview.html).

### Properties

[animatePhysics](Animation-animatePhysics.html)| When enabled, the physics
system uses animated transforms from GameObjects with kinematic Rigidbody
components to influence other GameObjects.  
---|---  
[clip](Animation-clip.html)| The default animation.  
[cullingType](Animation-cullingType.html)| Controls culling of this Animation
component.  
[isPlaying](Animation-isPlaying.html)| Is an animation currently being played?  
[localBounds](Animation-localBounds.html)| AABB of this Animation animation
component in local space.  
[playAutomatically](Animation-playAutomatically.html)| Should the default
animation clip (the Animation.clip property) automatically start playing on
startup?  
[this[string]](Animation.Index_operator.html)| Returns the animation state
named name.  
[updateMode](Animation-updateMode.html)| Specifies the update mode of the
Animation.  
[wrapMode](Animation-wrapMode.html)| How should time beyond the playback range
of the clip be treated?  
  
### Public Methods

[AddClip](Animation.AddClip.html)| Adds a clip to the animation with name
newName.  
---|---  
[Blend](Animation.Blend.html)| Blends the animation named animation towards
targetWeight over the next time seconds.  
[CrossFade](Animation.CrossFade.html)| Fades in the animation with the name
animation over a period of time defined by fadeLength.  
[CrossFadeQueued](Animation.CrossFadeQueued.html)| Cross fades an animation
after previous animations has finished playing.  
[GetClipCount](Animation.GetClipCount.html)| Get the number of clips currently
assigned to this animation.  
[IsPlaying](Animation.IsPlaying.html)| Is the animation named name playing?  
[Play](Animation.Play.html)| Plays an animation without blending.  
[PlayQueued](Animation.PlayQueued.html)| Plays an animation after previous
animations has finished playing.  
[RemoveClip](Animation.RemoveClip.html)| Remove clip from the animation list.  
[Rewind](Animation.Rewind.html)| Rewinds the animation named name.  
[Sample](Animation.Sample.html)| Samples animations at the current state.  
[Stop](Animation.Stop.html)| Stops all playing animations that were started
with this Animation.  
  
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

