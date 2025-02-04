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

# PlayableOutputExtensions

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
[IPlayableOutput](Playables.IPlayableOutput.html).

Extension methods are static methods that can be called as if they were
instance methods on the extended type.

    
    
    using UnityEngine;
    using UnityEngine.Playables;  
      
    public class ExamplePlayableBehaviour : [PlayableBehaviour](Playables.PlayableBehaviour.html)
    {
        void Start()
        {
            [PlayableGraph](Playables.PlayableGraph.html) graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)();
            [ScriptPlayableOutput](Playables.ScriptPlayableOutput.html) scriptOutput = [ScriptPlayableOutput.Create](Playables.ScriptPlayableOutput.Create.html)(graph, "MyOutput");  
      
            // Calling method PlayableExtensions.SetWeight on [ScriptPlayableOutput](Playables.ScriptPlayableOutput.html) as if it was an instance method.
            scriptOutput.SetWeight(10);  
      
            // The line above is the same as calling directly [PlayableExtensions.SetDuration](Playables.PlayableExtensions.SetDuration.html), but it is more compact and readable.
            [PlayableOutputExtensions.SetWeight](Playables.PlayableOutputExtensions.SetWeight.html)(scriptOutput, 10);
        }
    }
    

### Static Methods

[AddNotificationReceiver](Playables.PlayableOutputExtensions.AddNotificationReceiver.html)|
Registers a new receiver that listens for notifications.  
---|---  
[GetNotificationReceivers](Playables.PlayableOutputExtensions.GetNotificationReceivers.html)|
Retrieves the list of notification receivers currently registered on the
output.  
[GetSourceOutputPort](Playables.PlayableOutputExtensions.GetSourceOutputPort.html)|
Returns the source playable's output connection index.  
[GetSourcePlayable](Playables.PlayableOutputExtensions.GetSourcePlayable.html)|
Returns the source playable.  
[GetUserData](Playables.PlayableOutputExtensions.GetUserData.html)| Returns
the opaque user data. This is the same value as the last last argument of
ProcessFrame.  
[GetWeight](Playables.PlayableOutputExtensions.GetWeight.html)| Returns the
weight of the connection from the PlayableOutput to the source playable.  
[IsOutputNull](Playables.PlayableOutputExtensions.IsOutputNull.html)| Returns
true if the PlayableOutput is null, false otherwise.  
[IsOutputValid](Playables.PlayableOutputExtensions.IsOutputValid.html)|  
[PushNotification](Playables.PlayableOutputExtensions.PushNotification.html)|
Queues a notification to be sent through the Playable system.  
[RemoveNotificationReceiver](Playables.PlayableOutputExtensions.RemoveNotificationReceiver.html)|
Unregisters a receiver on the output.  
[SetReferenceObject](Playables.PlayableOutputExtensions.SetReferenceObject.html)|
Sets the bound object to a new value. Used to associate an output to an object
(Track asset in case of Timeline).  
[SetSourcePlayable](Playables.PlayableOutputExtensions.SetSourcePlayable.html)|
Sets which playable that computes the output and which sub-tree index.  
[SetUserData](Playables.PlayableOutputExtensions.SetUserData.html)| Sets the
opaque user data. This same data is passed as the last argument to
ProcessFrame.  
[SetWeight](Playables.PlayableOutputExtensions.SetWeight.html)| Sets the
weight of the connection from the PlayableOutput to the source playable.  
  
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

