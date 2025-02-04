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

# AnimatorState

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

States are the basic building blocks of a state machine. Each state contains a
Motion ( AnimationClip or BlendTree) which will play while the character is in
that state. When an event in the game triggers a state transition, the
character will be left in a new state whose animation sequence will then take
over.

### Properties

[behaviours](Animations.AnimatorState-behaviours.html)| The Behaviour list
assigned to this state.  
---|---  
[cycleOffset](Animations.AnimatorState-cycleOffset.html)| Offset at which the
animation loop starts. Useful for synchronizing looped animations. Units is
normalized time.  
[cycleOffsetParameter](Animations.AnimatorState-cycleOffsetParameter.html)|
The animator controller parameter that drives the cycle offset value.  
[cycleOffsetParameterActive](Animations.AnimatorState-
cycleOffsetParameterActive.html)| Define if the cycle offset value is driven
by an Animator controller parameter or by the value set in the editor.  
[iKOnFeet](Animations.AnimatorState-iKOnFeet.html)| Should Foot IK be
respected for this state.  
[mirror](Animations.AnimatorState-mirror.html)| Whether the animation state is
mirrored.  
[mirrorParameter](Animations.AnimatorState-mirrorParameter.html)| The animator
controller parameter that drives the mirror value.  
[mirrorParameterActive](Animations.AnimatorState-mirrorParameterActive.html)|
Define if the mirror value is driven by an Animator controller parameter or by
the value set in the editor.  
[motion](Animations.AnimatorState-motion.html)| The motion assigned to this
state.  
[nameHash](Animations.AnimatorState-nameHash.html)| The hashed name of the
state.  
[speed](Animations.AnimatorState-speed.html)| The default speed of the motion.  
[speedParameter](Animations.AnimatorState-speedParameter.html)| The animator
controller parameter that drives the speed value.  
[speedParameterActive](Animations.AnimatorState-speedParameterActive.html)|
Define if the speed value is driven by an Animator controller parameter or by
the value set in the editor.  
[tag](Animations.AnimatorState-tag.html)| A tag can be used to identify a
state.  
[timeParameter](Animations.AnimatorState-timeParameter.html)| If
timeParameterActive is true, the value of this Parameter will be used instead
of normalized time.  
[timeParameterActive](Animations.AnimatorState-timeParameterActive.html)| If
true, use value of given Parameter as normalized time.  
[transitions](Animations.AnimatorState-transitions.html)| The transitions that
are going out of the state.  
[writeDefaultValues](Animations.AnimatorState-writeDefaultValues.html)|
Whether or not the AnimatorStates writes back the default values for
properties that are not animated by its Motion.  
  
### Public Methods

[AddExitTransition](Animations.AnimatorState.AddExitTransition.html)| Utility
function to add an outgoing transition to the exit of the state's parent state
machine.  
---|---  
[AddStateMachineBehaviour](Animations.AnimatorState.AddStateMachineBehaviour.html)|
Adds a state machine behaviour class of type T to the AnimatorState. Note that
there is no corresponding "Remove" method. To remove a state machine
behaviour, use Object.Destroy.  
[AddTransition](Animations.AnimatorState.AddTransition.html)| Utility function
to add an outgoing transition to the destination state.  
[RemoveTransition](Animations.AnimatorState.RemoveTransition.html)| Utility
function to remove a transition from the state.  
  
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

