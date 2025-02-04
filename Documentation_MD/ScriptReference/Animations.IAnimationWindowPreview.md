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

# IAnimationWindowPreview

interface in UnityEngine.Animations

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

Allows a class to modify how an [AnimationClip](AnimationClip.html) is sampled
in the Animation window by providing its own
[Playable](Playables.Playable.html) nodes to the Animation window
[PlayableGraph](Playables.PlayableGraph.html). The class must also inherit
from [MonoBehaviour](MonoBehaviour.html).

Additional resources:
[AnimationScriptPlayable](Animations.AnimationScriptPlayable.html)

    
    
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    [[RequireComponent](RequireComponent.html)(typeof([Animator](Animator.html)))]
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html), [IAnimationWindowPreview](Animations.IAnimationWindowPreview.html)
    {
        public [Vector3](Vector3.html) offset = [Vector3.zero](Vector3-zero.html);  
      
        private [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) m_Playable;
        private AnimationJob m_Job;
        private [Vector3](Vector3.html) m_CurrentOffset;  
      
        struct AnimationJob : [IAnimationJob](Animations.IAnimationJob.html)
        {
            public [TransformStreamHandle](Animations.TransformStreamHandle.html) transform;
            public [Vector3](Vector3.html) offset;  
      
            public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream)
            {
                [Vector3](Vector3.html) position = transform.GetLocalPosition(stream);
                position += offset;  
      
                transform.SetLocalPosition(stream, position);
            }  
      
            public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
            {
            }
        }  
      
        public void StartPreview()
        {
            m_CurrentOffset = offset;
        }  
      
        public void StopPreview()
        {
        }  
      
        public void UpdatePreviewGraph([PlayableGraph](Playables.PlayableGraph.html) graph)
        {
            if (m_CurrentOffset != offset)
            {
                m_Job.offset = offset;
                m_Playable.SetJobData(m_Job);  
      
                m_CurrentOffset = offset;
            }
        }  
      
        public [Playable](Playables.Playable.html) BuildPreviewGraph([PlayableGraph](Playables.PlayableGraph.html) graph, [Playable](Playables.Playable.html) input)
        {
            [Animator](Animator.html) animator = GetComponent<[Animator](Animator.html)>();  
      
            m_Job = new AnimationJob();
            m_Job.transform = animator.BindStreamTransform(transform);
            m_Job.offset = offset;  
      
            m_Playable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(graph, m_Job, 1);  
      
            graph.Connect(input, 0, m_Playable, 0);  
      
            return m_Playable;
        }
    }
    

### Public Methods

[BuildPreviewGraph](Animations.IAnimationWindowPreview.BuildPreviewGraph.html)|
Appends custom Playable nodes to the Animation window PlayableGraph.  
---|---  
[StartPreview](Animations.IAnimationWindowPreview.StartPreview.html)|
Notification callback when the Animation window starts previewing an
AnimationClip.  
[StopPreview](Animations.IAnimationWindowPreview.StopPreview.html)|
Notification callback when the Animation window stops previewing an
AnimationClip.  
[UpdatePreviewGraph](Animations.IAnimationWindowPreview.UpdatePreviewGraph.html)|
Notification callback when the Animation Window updates its PlayableGraph
before sampling an AnimationClip.  
  
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

