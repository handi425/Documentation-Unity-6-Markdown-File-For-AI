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

#  [FrameData](Playables.FrameData.html).deltaTime

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

public float deltaTime;

### Description

The interval between this frame and the preceding frame. The interval is
unscaled and expressed in seconds.

To time-scale the interval, multiple the interval by
[FrameData.effectiveSpeed](Playables.FrameData-effectiveSpeed.html).

    
    
    //Attach this script to a [GameObject](GameObject.html) that has an [Animator](Animator.html) and set the [Animator](Animator.html) field.
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    public class MyMonoBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)]
        private [Animator](Animator.html) m_Animator;  
      
        private [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        private void Awake()
        {
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)();
            m_Graph.SetTimeUpdateMode([DirectorUpdateMode.GameTime](Playables.DirectorUpdateMode.GameTime.html));  
      
            var scriptPlayable = ScriptPlayable<MyPlayableBehaviour>.Create(m_Graph);  
      
            // Sets game time's scale, as well as custom playable's speed.
            [Time.timeScale](Time-timeScale.html) = 10f;
            scriptPlayable.SetSpeed(0.5f);  
      
            var playableOutput = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "MyPlayableOutput", m_Animator);
            playableOutput.SetSourcePlayable(scriptPlayable, 0);  
      
            m_Graph.Play();
        }  
      
        private void OnDestroy()
        {
            if (m_Graph.IsValid())
                m_Graph.Destroy();
        }
    }  
      
    public sealed class MyPlayableBehaviour : [PlayableBehaviour](Playables.PlayableBehaviour.html)
    {
        public override void PrepareFrame([Playable](Playables.Playable.html) playable, [FrameData](Playables.FrameData.html) info)
        {
            base.PrepareFrame(playable, info);  
      
            // info.deltaTime is not scaled, and so is 10 times smaller than [Time.deltaTime](Time-deltaTime.html)
            // info.effectiveSpeed is equal to 5 (10 * 0.5). [Time.timeScale](Time-timeScale.html) is accounted for because we use [DirectorUpdateMode.GameTime](Playables.DirectorUpdateMode.GameTime.html).
            // If we had used [DirectorUpdateMode.UnscaledGameTime](Playables.DirectorUpdateMode.UnscaledGameTime.html), info.effectiveSpeed would have been equal to 0.5.
            [Debug.Log](Debug.Log.html)($"info.deltaTime = {info.deltaTime}, speed {info.effectiveSpeed} [Time.deltaTime](Time-deltaTime.html) = {[Time.deltaTime](Time-deltaTime.html)}");
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

