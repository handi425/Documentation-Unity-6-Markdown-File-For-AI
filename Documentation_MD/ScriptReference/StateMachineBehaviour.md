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

# StateMachineBehaviour

class in UnityEngine

/

Inherits from:[ScriptableObject](ScriptableObject.html)

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

[ ]()

### Description

StateMachineBehaviour is a component that can be added to a state machine
state. It's the base class any script on a state must derive from.

State machines can have up to three different active states at the same time:
the current state, the next state and the interrupted state.  
The state machine always has a current state. When the state machine
transitions to a new state, a "next state" is added. Once the transition is
complete, the current state is terminated and the next state becomes the new
current state.  
If an ongoing transition is interrupted by a transition to a new state, then
the next state becomes the interrupted state and the state targeted by the new
transition is now the next state. The current state will remain the same until
all interrupted transitions have completed. Once the last transition is
complete and there are no more interruptions, the current and interrupted
states are terminated, and the next state becomes the new current state.  
  
StateMachineBehaviour has some predefined state-related messages that you can
implement:[OnStateEnter](StateMachineBehaviour.OnStateEnter.html),
[OnStateExit](StateMachineBehaviour.OnStateExit.html),
[OnStateIK](StateMachineBehaviour.OnStateIK.html),
[OnStateMove](StateMachineBehaviour.OnStateMove.html),
[OnStateUpdate](StateMachineBehaviour.OnStateUpdate.html).  
Whenever appropriate, these messages will be invoked for the active states
mentioned above in the following order: current state, then interrupted state,
then next state.  
See the description of each message for more information.  
  
StateMachineBehaviour also has some predefined messages related to transitions
in and out of state machines:  
[OnStateMachineEnter](StateMachineBehaviour.OnStateMachineEnter.html),
[OnStateMachineExit](StateMachineBehaviour.OnStateMachineExit.html).  
These are invoked whenever a state machine transition is taken.  
  
**Layer considerations** :  
If an [AnimatorController](Animations.AnimatorController.html) contains
sychronized layers, the messages may be invoked multiple times for a single
state. In that situation, the messages will be invoked once per synchronized
layer that contains the state, in ascending order.  
  
**Additional considerations** :  
By default the Animator instantiates a new instance of each behaviour defined
in the controller. If you wish to share behaviour instances, use the class
attribute
[SharedBetweenAnimatorsAttribute](SharedBetweenAnimatorsAttribute.html) to
control how behaviours are instantiated.

    
    
    using UnityEngine;  
      
    public class AttackBehaviour : [StateMachineBehaviour](StateMachineBehaviour.html)
    {
        public [GameObject](GameObject.html) particle;
        public float radius;
        public float power;  
      
        protected [GameObject](GameObject.html) clone;  
      
        override public void OnStateEnter([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            clone = Instantiate(particle, animator.rootPosition, [Quaternion.identity](Quaternion-identity.html)) as [GameObject](GameObject.html);
            [Rigidbody](Rigidbody.html) rb = clone.GetComponent<[Rigidbody](Rigidbody.html)>();
            rb.AddExplosionForce(power, animator.rootPosition, radius, 3.0f);
        }  
      
        override public void OnStateExit([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            Destroy(clone);
        }  
      
        override public void OnStateUpdate([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            [Debug.Log](Debug.Log.html)("On Attack [Update](PlayerLoop.Update.html) ");
        }  
      
        override public void OnStateMove([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            [Debug.Log](Debug.Log.html)("On Attack Move ");
        }  
      
        override public void OnStateIK([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            [Debug.Log](Debug.Log.html)("On Attack IK ");
        }
    }
    

### Public Methods

[OnStateMachineEnter](StateMachineBehaviour.OnStateMachineEnter.html)| Invoked
on the first update frame when taking a transition into a state machine.
Implement this message to influence the entry transition into the sub-state
machine.  
---|---  
[OnStateMachineExit](StateMachineBehaviour.OnStateMachineExit.html)| Invoked
on the last update frame when taking a transition out of a StateMachine.
Implement this message to influence the exit transition out of the sub-state
machine  
  
### Messages

[OnStateEnter](StateMachineBehaviour.OnStateEnter.html)| Invoked on the first
update frame when a state machine evaluates this state. Implement this message
to react to a new state starting.  
---|---  
[OnStateExit](StateMachineBehaviour.OnStateExit.html)| Invoked on the last
update frame when a state machine evaluates this state. Implement this message
to react to a state ending.  
[OnStateIK](StateMachineBehaviour.OnStateIK.html)| Invoked during the Animator
IK pass. Implement this message to modify the result of the animation after
the evaluation of the state machine on a state by state basis.  
[OnStateMove](StateMachineBehaviour.OnStateMove.html)| Invoked during the
Animator Root Motion pass. Implement this message to modify the result of the
animation root motion on a state by state basis.  
[OnStateUpdate](StateMachineBehaviour.OnStateUpdate.html)| Invoked on each
update frame except for the first and last frame. Implement this message to
execute custom logic on a state by state basis.  
  
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
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
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

