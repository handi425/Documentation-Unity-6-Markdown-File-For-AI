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

#  [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html).Create

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

## Declaration

public static
[Animations.AnimationScriptPlayable](Animations.AnimationScriptPlayable.html)
Create([Playables.PlayableGraph](Playables.PlayableGraph.html) graph, T
jobData, int inputCount);

### Parameters

graph | The PlayableGraph object that will own the AnimationScriptPlayable.  
---|---  
job | The [IAnimationJob](Animations.IAnimationJob.html) to execute when processing the playable.  
inputCount | The number of inputs on the playable.  
  
### Returns

**AnimationScriptPlayable** A new
[AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) linked to
the [PlayableGraph](Playables.PlayableGraph.html).

### Description

Creates an [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html)
in the [PlayableGraph](Playables.PlayableGraph.html).

This playable contains a job implementing an
[IAnimationJob](Animations.IAnimationJob.html). This interface defines two
methods that will be called while processing the
[PlayableGraph](Playables.PlayableGraph.html).  
  
Here is an example of how to create an
[AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) with a
simple [IAnimationJob](Animations.IAnimationJob.html):

    
    
    using UnityEngine;
    using UnityEngine.Playables;
    using UnityEngine.Animations;  
      
    public struct AnimationJob : [IAnimationJob](Animations.IAnimationJob.html)
    {
        public int userData;  
      
        public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream)
        {
            // This method is called during the root motion process pass.
        }  
      
        public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
        {
            // This method is called during the animation process pass.
            [Debug.Log](Debug.Log.html)(string.Format("Value of the userData: {0}", userData));
        }
    }  
      
    [[RequireComponent](RequireComponent.html)(typeof([Animator](Animator.html)))]
    public class AnimationScriptExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
      
        void OnEnable()
        {
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)("AnimationScriptExample");
            var output = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "ouput", GetComponent<[Animator](Animator.html)>());  
      
            var animationJob = new AnimationJob();
            m_AnimationScriptPlayable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
      
            output.SetSourcePlayable(m_AnimationScriptPlayable);
            m_Graph.Play();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var animationJob = m_AnimationScriptPlayable.GetJobData<AnimationJob>();
            ++animationJob.userData;
            m_AnimationScriptPlayable.SetJobData(animationJob);
        }  
      
        void OnDisable()
        {
            m_Graph.Destroy();
        }
    }
    

Additional resources: [IAnimationJob](Animations.IAnimationJob.html),
[AnimatorJobExtensions](Animations.AnimatorJobExtensions.html).

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

