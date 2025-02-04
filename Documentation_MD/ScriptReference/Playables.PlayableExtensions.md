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

# PlayableExtensions

class in UnityEngine.Playables

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

[ ]()

### Description

Extensions for all the types that implements
[IPlayable](Playables.IPlayable.html).

Extension methods are static methods that can be called as if they were
instance methods on the extended type.

    
    
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    public class ExamplePlayableBehaviour : [PlayableBehaviour](Playables.PlayableBehaviour.html)
    {
        void Start()
        {
            [PlayableGraph](Playables.PlayableGraph.html) graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)();
            [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html) mixer = [AnimationMixerPlayable.Create](Animations.AnimationMixerPlayable.Create.html)(graph, 1);  
      
            // Calling method [PlayableExtensions.SetDuration](Playables.PlayableExtensions.SetDuration.html) on [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html) as if it was an instance method.
            mixer.SetDuration(10);  
      
            // The line above is the same as calling directly [PlayableExtensions.SetDuration](Playables.PlayableExtensions.SetDuration.html), but it is more compact and readable.
            [PlayableExtensions.SetDuration](Playables.PlayableExtensions.SetDuration.html)(mixer, 10);
        }
    }
    

### Static Methods

[AddInput](Playables.PlayableExtensions.AddInput.html)| Create a new input
port and connect it to the output port of the given Playable.  
---|---  
[ConnectInput](Playables.PlayableExtensions.ConnectInput.html)| Connect the
output port of a Playable to one of the input ports.  
[Destroy](Playables.PlayableExtensions.Destroy.html)| Destroys the current
Playable.  
[DisconnectInput](Playables.PlayableExtensions.DisconnectInput.html)|
Disconnect the input port of a Playable.  
[GetDuration](Playables.PlayableExtensions.GetDuration.html)| Returns the
duration of the Playable.  
[GetGraph](Playables.PlayableExtensions.GetGraph.html)| Returns the
PlayableGraph that owns this Playable. A Playable can only be used in the
graph that was used to create it.  
[GetInput](Playables.PlayableExtensions.GetInput.html)| Returns the Playable
connected at the given input port index.  
[GetInputCount](Playables.PlayableExtensions.GetInputCount.html)| Returns the
number of inputs supported by the Playable.  
[GetInputWeight](Playables.PlayableExtensions.GetInputWeight.html)| Returns
the weight of the Playable connected at the given input port index.  
[GetLeadTime](Playables.PlayableExtensions.GetLeadTime.html)| Returns the
Playable lead time in seconds.  
[GetOutput](Playables.PlayableExtensions.GetOutput.html)| Returns the Playable
connected at the given output port index.  
[GetOutputCount](Playables.PlayableExtensions.GetOutputCount.html)| Returns
the number of outputs supported by the Playable.  
[GetPlayState](Playables.PlayableExtensions.GetPlayState.html)| Returns the
current PlayState of the Playable.  
[GetPreviousTime](Playables.PlayableExtensions.GetPreviousTime.html)| Returns
the previous local time of the Playable.  
[GetPropagateSetTime](Playables.PlayableExtensions.GetPropagateSetTime.html)|
Returns the time propagation behavior of this Playable.  
[GetSpeed](Playables.PlayableExtensions.GetSpeed.html)| Returns the speed
multiplier that is applied to the the current Playable.  
[GetTime](Playables.PlayableExtensions.GetTime.html)| Returns the current
local time of the Playable.  
[GetTraversalMode](Playables.PlayableExtensions.GetTraversalMode.html)|
Returns the propagation mode for the multi-output playable.  
[IsDone](Playables.PlayableExtensions.IsDone.html)| Returns a flag indicating
that a playable has completed its operation.  
[IsNull](Playables.PlayableExtensions.IsNull.html)| Returns true if the
Playable is null, false otherwise.  
[IsValid](Playables.PlayableExtensions.IsValid.html)| Returns the vality of
the current Playable.  
[Pause](Playables.PlayableExtensions.Pause.html)| Tells to pause the Playable.  
[Play](Playables.PlayableExtensions.Play.html)| Starts to play the Playable.  
[SetDone](Playables.PlayableExtensions.SetDone.html)| Changes a flag
indicating that a playable has completed its operation.  
[SetDuration](Playables.PlayableExtensions.SetDuration.html)| Changes the
duration of the Playable.  
[SetInputCount](Playables.PlayableExtensions.SetInputCount.html)| Changes the
number of inputs supported by the Playable.  
[SetInputWeight](Playables.PlayableExtensions.SetInputWeight.html)| Changes
the weight of the Playable connected to the current Playable.  
[SetLeadTime](Playables.PlayableExtensions.SetLeadTime.html)| Sets the
Playable lead time in seconds.  
[SetOutputCount](Playables.PlayableExtensions.SetOutputCount.html)| Changes
the number of outputs supported by the Playable.  
[SetPropagateSetTime](Playables.PlayableExtensions.SetPropagateSetTime.html)|
Changes the time propagation behavior of this Playable.  
[SetSpeed](Playables.PlayableExtensions.SetSpeed.html)| Changes the speed
multiplier that is applied to the the current Playable.  
[SetTime](Playables.PlayableExtensions.SetTime.html)| Changes the current
local time of the Playable.  
[SetTraversalMode](Playables.PlayableExtensions.SetTraversalMode.html)| Sets
the propagation mode of PrepareFrame and ProcessFrame for the multi-output
playable.  
  
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

