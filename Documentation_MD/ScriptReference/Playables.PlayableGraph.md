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

# PlayableGraph

struct in UnityEngine.Playables

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

Use the PlayableGraph to manage [Playable](Playables.Playable.html) creations
and destructions.

The PlayableGraph is also the link to different systems, through structs that
implement [IPlayableOutput](Playables.IPlayableOutput.html). For example,
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html) or
[AudioPlayableOutput](Audio.AudioPlayableOutput.html).

### Public Methods

[Connect](Playables.PlayableGraph.Connect.html)| Connects two Playable
instances.  
---|---  
[Destroy](Playables.PlayableGraph.Destroy.html)| Destroys the graph.  
[DestroyOutput](Playables.PlayableGraph.DestroyOutput.html)| Destroys the
PlayableOutput.  
[DestroyPlayable](Playables.PlayableGraph.DestroyPlayable.html)| Destroys the
Playable.  
[DestroySubgraph](Playables.PlayableGraph.DestroySubgraph.html)| Destroys the
Playable and all its inputs, recursively.  
[Disconnect](Playables.PlayableGraph.Disconnect.html)| Disconnects the
Playable. The connections determine the topology of the PlayableGraph and how
it is evaluated.  
[Evaluate](Playables.PlayableGraph.Evaluate.html)| Evaluates all the
PlayableOutputs in the graph, and updates all the connected Playables in the
graph.  
[GetEditorName](Playables.PlayableGraph.GetEditorName.html)| Returns the name
of the PlayableGraph.  
[GetOutput](Playables.PlayableGraph.GetOutput.html)| Get PlayableOutput at the
given index in the graph.  
[GetOutputByType](Playables.PlayableGraph.GetOutputByType.html)| Get
PlayableOutput of the requested type at the given index in the graph.  
[GetOutputCount](Playables.PlayableGraph.GetOutputCount.html)| Returns the
number of PlayableOutput in the graph.  
[GetOutputCountByType](Playables.PlayableGraph.GetOutputCountByType.html)| Get
the number of PlayableOutput of the requested type in the graph.  
[GetPlayableCount](Playables.PlayableGraph.GetPlayableCount.html)| Returns the
number of Playable owned by the Graph.  
[GetResolver](Playables.PlayableGraph.GetResolver.html)| Returns the table
used by the graph to resolve ExposedReferences.  
[GetRootPlayable](Playables.PlayableGraph.GetRootPlayable.html)| Returns the
Playable with no output connections at the given index.  
[GetRootPlayableCount](Playables.PlayableGraph.GetRootPlayableCount.html)|
Returns the number of Playable owned by the Graph that have no connected
outputs.  
[GetTimeUpdateMode](Playables.PlayableGraph.GetTimeUpdateMode.html)| Returns
how time is incremented when playing back.  
[IsDone](Playables.PlayableGraph.IsDone.html)| Indicates that a graph has
completed its operations.  
[IsPlaying](Playables.PlayableGraph.IsPlaying.html)| Indicates that a graph is
presently running.  
[IsValid](Playables.PlayableGraph.IsValid.html)| Returns true if the
PlayableGraph has been properly constructed using PlayableGraph.CreateGraph
and is not deleted.  
[Play](Playables.PlayableGraph.Play.html)| Plays the graph.  
[SetResolver](Playables.PlayableGraph.SetResolver.html)| Changes the table
used by the graph to resolve ExposedReferences.  
[SetTimeUpdateMode](Playables.PlayableGraph.SetTimeUpdateMode.html)| Changes
how time is incremented when playing back.  
[Stop](Playables.PlayableGraph.Stop.html)| Stops the graph, if it is playing.  
  
### Static Methods

[Create](Playables.PlayableGraph.Create.html)| Creates a PlayableGraph.  
---|---  
  
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

