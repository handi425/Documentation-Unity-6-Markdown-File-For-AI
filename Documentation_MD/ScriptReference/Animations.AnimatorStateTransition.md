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

# AnimatorStateTransition

class in UnityEditor.Animations

/

Inherits
from:[Animations.AnimatorTransitionBase](Animations.AnimatorTransitionBase.html)

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

Transitions define when and how the state machine switch from one state to
another. [AnimatorStateTransition](Animations.AnimatorStateTransition.html)
always originate from an Animator State (or AnyState) and have timing
parameters.

A transition happens when all its conditions are met.
[AnimatorStateTransition](Animations.AnimatorStateTransition.html) derives
from [AnimatorTransitionBase](Animations.AnimatorTransitionBase.html).

### Properties

[canTransitionToSelf](Animations.AnimatorStateTransition-
canTransitionToSelf.html)| Set to true to allow or disallow transition to self
during AnyState transition.  
---|---  
[duration](Animations.AnimatorStateTransition-duration.html)| The duration of
the transition.  
[exitTime](Animations.AnimatorStateTransition-exitTime.html)| If
AnimatorStateTransition.hasExitTime is true, exitTime represents the exact
time at which the transition can take effect. This is represented in
normalized time, so for example an exit time of 0.75 means that on the first
frame where 75% of the animation has played, the Exit Time condition will be
true. On the next frame, the condition will be false. For looped animations,
transitions with exit times smaller than 1 will be evaluated every loop, so
you can use this to time your transition with the proper timing in the
animation, every loop. Transitions with exit times greater than one will be
evaluated only once, so they can be used to exit at a specific time, after a
fixed number of loops. For example, a transition with an exit time of 3.5 will
be evaluated once, after three and a half loops.  
[hasExitTime](Animations.AnimatorStateTransition-hasExitTime.html)| When
active the transition will have an exit time condition.  
[hasFixedDuration](Animations.AnimatorStateTransition-hasFixedDuration.html)|
Determines whether the duration of the transition is reported in a fixed
duration in seconds or as a normalized time.  
[interruptionSource](Animations.AnimatorStateTransition-
interruptionSource.html)| Which AnimatorState transitions can interrupt the
Transition.  
[offset](Animations.AnimatorStateTransition-offset.html)| The time at which
the destination state will start.  
[orderedInterruption](Animations.AnimatorStateTransition-
orderedInterruption.html)| The Transition can be interrupted by a transition
that has a higher priority.  
  
### Constructors

[AnimatorStateTransition](Animations.AnimatorStateTransition-ctor.html)|
Creates a new animator state transition.  
---|---  
  
### Inherited Members

### Properties

[conditions](Animations.AnimatorTransitionBase-conditions.html)|
AnimatorCondition conditions that need to be met for a transition to happen.  
---|---  
[destinationState](Animations.AnimatorTransitionBase-destinationState.html)|
The destination state of the transition.  
[destinationStateMachine](Animations.AnimatorTransitionBase-
destinationStateMachine.html)| The destination state machine of the
transition.  
[isExit](Animations.AnimatorTransitionBase-isExit.html)| Is the transition
destination the exit of the current state machine.  
[mute](Animations.AnimatorTransitionBase-mute.html)| Mutes the transition. The
transition will never occur.  
[solo](Animations.AnimatorTransitionBase-solo.html)| Mutes all other
transitions in the source state.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[AddCondition](Animations.AnimatorTransitionBase.AddCondition.html)| Utility
function to add a condition to a transition.  
---|---  
[RemoveCondition](Animations.AnimatorTransitionBase.RemoveCondition.html)|
Utility function to remove a condition from the transition.  
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

