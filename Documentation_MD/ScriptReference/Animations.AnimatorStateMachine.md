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

# AnimatorStateMachine

class in UnityEditor.Animations

/

Inherits from:[Object](Object.html)

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

A graph controlling the interaction of states. Each state references a motion.

### Properties

[anyStatePosition](Animations.AnimatorStateMachine-anyStatePosition.html)| The
position of the AnyState node.  
---|---  
[anyStateTransitions](Animations.AnimatorStateMachine-
anyStateTransitions.html)| The list of AnyState transitions.  
[behaviours](Animations.AnimatorStateMachine-behaviours.html)| The Behaviour
list assigned to this state machine.  
[defaultState](Animations.AnimatorStateMachine-defaultState.html)| The state
that the state machine will be in when it starts.  
[entryPosition](Animations.AnimatorStateMachine-entryPosition.html)| The
position of the entry node.  
[entryTransitions](Animations.AnimatorStateMachine-entryTransitions.html)| The
list of entry transitions in the state machine.  
[exitPosition](Animations.AnimatorStateMachine-exitPosition.html)| The
position of the exit node.  
[parentStateMachinePosition](Animations.AnimatorStateMachine-
parentStateMachinePosition.html)| The position of the parent state machine
node. Only valid when in a hierachic state machine.  
[stateMachines](Animations.AnimatorStateMachine-stateMachines.html)| The list
of sub state machines.  
[states](Animations.AnimatorStateMachine-states.html)| The list of states.  
  
### Public Methods

[AddAnyStateTransition](Animations.AnimatorStateMachine.AddAnyStateTransition.html)|
Utility function to add an AnyState transition to the specified state or
statemachine.  
---|---  
[AddEntryTransition](Animations.AnimatorStateMachine.AddEntryTransition.html)|
Utility function to add an incoming transition to the exit of it's parent
state machine.  
[AddState](Animations.AnimatorStateMachine.AddState.html)| Utility function to
add a state to the state machine.  
[AddStateMachine](Animations.AnimatorStateMachine.AddStateMachine.html)|
Utility function to add a state machine to the state machine.  
[AddStateMachineBehaviour](Animations.AnimatorStateMachine.AddStateMachineBehaviour.html)|
Adds a state machine behaviour class of type T to the AnimatorStateMachine.
Note that there is no corresponding "Remove" method. To remove a state machine
behaviour, use Object.Destroy.  
[AddStateMachineExitTransition](Animations.AnimatorStateMachine.AddStateMachineExitTransition.html)|
Utility function to add an outgoing transition from the source state machine
to the exit of it's parent state machine.  
[AddStateMachineTransition](Animations.AnimatorStateMachine.AddStateMachineTransition.html)|
Utility function to add an outgoing transition from the source state machine
to the destination.  
[GetStateMachineTransitions](Animations.AnimatorStateMachine.GetStateMachineTransitions.html)|
Gets the list of all outgoing state machine transitions from given state
machine.  
[MakeUniqueStateMachineName](Animations.AnimatorStateMachine.MakeUniqueStateMachineName.html)|
Makes a unique state machine name in the context of the parent state machine.  
[MakeUniqueStateName](Animations.AnimatorStateMachine.MakeUniqueStateName.html)|
Makes a unique state name in the context of the parent state machine.  
[RemoveAnyStateTransition](Animations.AnimatorStateMachine.RemoveAnyStateTransition.html)|
Utility function to remove an AnyState transition from the state machine.  
[RemoveEntryTransition](Animations.AnimatorStateMachine.RemoveEntryTransition.html)|
Utility function to remove an entry transition from the state machine.  
[RemoveState](Animations.AnimatorStateMachine.RemoveState.html)| Utility
function to remove a state from the state machine.  
[RemoveStateMachine](Animations.AnimatorStateMachine.RemoveStateMachine.html)|
Utility function to remove a state machine from its parent state machine.  
[RemoveStateMachineTransition](Animations.AnimatorStateMachine.RemoveStateMachineTransition.html)|
Utility function to remove an outgoing transition from source state machine.  
[SetStateMachineTransitions](Animations.AnimatorStateMachine.SetStateMachineTransitions.html)|
Sets the list of all outgoing state machine transitions from given state
machine.  
  
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

