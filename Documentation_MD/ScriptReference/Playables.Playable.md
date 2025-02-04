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

# Playable

struct in UnityEngine.Playables

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

  

Implements interfaces:[IPlayable](Playables.IPlayable.html)

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

Playables are customizable runtime objects that can be connected together and
are contained in a [PlayableGraph](Playables.PlayableGraph.html) to create
complex behaviours.

Playables can be used to create complex and flexible data evaluation trees.
Playables are nodes that can be connected together, after which each Playable
can set the "weight" or "influence" of each of its children.  
  
The playables of the same graph are contained in a
[PlayableGraph](Playables.PlayableGraph.html). A PlayableGraph can have
several outputs, also called "players", which implement
[IPlayableOutput](Playables.IPlayableOutput.html). The PlayableOutput takes
the result of their source playable and apply it to an object in the Scene.
For instance, the
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html) is linked
to a playable node in the graph (the "source playable") and to an
[Animator](Animator.html) in the Scene. When the graph is played, the
animation pose resulting of the graph evaluation is applied by the Animator.
There are as many PlayableOutputs as there are different playable types:
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html),
[AudioPlayableOutput](Audio.AudioPlayableOutput.html),
[TexturePlayableOutput](Experimental.Playables.TexturePlayableOutput.html),
[ScriptPlayableOutput](Playables.ScriptPlayableOutput.html), etc...  
  
The ScriptPlayable<T> is a special kind of playable. It's main role is to be a
"custom" playable. It is a templated struct where `T` must derived from
[PlayableBehaviour](Playables.PlayableBehaviour.html). These custom
PlayableBehaviours allow to write behaviours at specific moments in the graph
evaluation (see
[PlayableBehaviour.PrepareFrame](Playables.PlayableBehaviour.PrepareFrame.html)
and
[PlayableBehaviour.ProcessFrame](Playables.PlayableBehaviour.ProcessFrame.html)).
A good example of a ScriptPlayable is the TimelinePlayable which is
controlling the Timeline graph. It creates and links together the playables in
charge of the tracks and the clips.  
  
When a [PlayableGraph](Playables.PlayableGraph.html) is played, each
PlayableOutput will be traversed. During this traversal, it will call the
PrepareFrame method on each Playable. This allows the Playable to "prepare
itself for the next evaluation". It is during the PrepareFrame stage that each
Playable can modify its children (either by adding new inputs or by removing
some of them). This enables Playable to "spawn" new children branches in the
Playable tree at runtime. This means that Playable trees are not static
structures. They can adapt and change over time.  
  
Once the preparation is done, the PlayableOutputs are in charge of processing
the result, that's why they are also called "players". In the case of an
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html), the
[Animator](Animator.html) is in charge of processing the graph. And in the
case of a [ScriptPlayableOutput](Playables.ScriptPlayableOutput.html),
[PlayableBehaviour.ProcessFrame](Playables.PlayableBehaviour.ProcessFrame.html)
will be called on each ScriptPlayable.  
  
**Note:** You can use the
[PlayableExtensions](Playables.PlayableExtensions.html) methods on any struct
implementing [IPlayable](Playables.IPlayable.html).  
  
**Note:** The Manual has detailed documentation about the [Playables
API](../Manual/Playables.html).

### Static Properties

[Null](Playables.Playable.Null.html)| Returns an invalid Playable.  
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

