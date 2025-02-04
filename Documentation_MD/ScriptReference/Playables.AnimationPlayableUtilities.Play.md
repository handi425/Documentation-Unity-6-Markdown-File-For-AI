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

**Method group is Obsolete**  

#
[AnimationPlayableUtilities](Playables.AnimationPlayableUtilities.html).Play

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

**Obsolete** This function is no longer used as it overrides the Time Update
Mode of the Playable Graph. Refer to the documentation for an example of an
equivalent function.

## Declaration

public static void Play([Animator](Animator.html) animator,
[Playables.Playable](Playables.Playable.html) playable,
[Playables.PlayableGraph](Playables.PlayableGraph.html) graph);

### Parameters

animator | Target Animator.  
---|---  
playable | The Playable that will be played.  
graph | The Graph that owns the Playable.  
  
### Description

Plays the [Playable](Playables.Playable.html) on the given Animator.  
  
**Note:** This method is deprecated as it overrides the Time Update Mode of
the Playable Graph. For an equivalent function, refer to the example below.

    
    
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    public class Example
    {
        void Play([Animator](Animator.html) animator, [Playable](Playables.Playable.html) playable, [PlayableGraph](Playables.PlayableGraph.html) graph)
        {
            [AnimationPlayableOutput](Animations.AnimationPlayableOutput.html) playableOutput = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(graph, "[AnimationClip](AnimationClip.html)", animator);
            playableOutput.SetSourcePlayable(playable, 0);
            graph.SetTimeUpdateMode([DirectorUpdateMode.GameTime](Playables.DirectorUpdateMode.GameTime.html));
            graph.Play();
        }
    }
    

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

