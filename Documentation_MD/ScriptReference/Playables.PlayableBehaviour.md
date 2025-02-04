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

# PlayableBehaviour

class in UnityEngine.Playables

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

  

Implements interfaces:[IPlayableBehaviour](Playables.IPlayableBehaviour.html)

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

PlayableBehaviour is the base class from which every custom playable script
derives.

A PlayableBehaviour can be used to add user-defined behaviour to a
[PlayableGraph](Playables.PlayableGraph.html).  
  
A PlayableBehaviour must be part of a branch of a
[PlayableGraph](Playables.PlayableGraph.html) that is connected to an output
to be active.  
  
In the following example, two [AnimationClip](AnimationClip.html) are
controlled by two
[AnimationClipPlayable](Animations.AnimationClipPlayable.html), which are
blended by a [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html).
A custom BlenderPlayableBehaviour is modifying the inputs weigth of the
[AnimationMixerPlayable](Animations.AnimationMixerPlayable.html) every frame.

    
    
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    public class BlenderPlayableBehaviour : [PlayableBehaviour](Playables.PlayableBehaviour.html)
    {
        public [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html) mixerPlayable;  
      
        public override void PrepareFrame([Playable](Playables.Playable.html) playable, [FrameData](Playables.FrameData.html) info)
        {
            float blend = [Mathf.PingPong](Mathf.PingPong.html)((float)playable.GetTime(), 1.0f);  
      
            mixerPlayable.SetInputWeight(0, blend);
            mixerPlayable.SetInputWeight(1, 1.0f - blend);  
      
            base.PrepareFrame(playable, info);
        }
    }  
      
    public class PlayableBehaviourSample : [MonoBehaviour](MonoBehaviour.html)
    {
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        public [AnimationClip](AnimationClip.html) clipA;
        public [AnimationClip](AnimationClip.html) clipB;  
      
        // Use this for initialization
        void Start()
        {
            // Create the [PlayableGraph](Playables.PlayableGraph.html).
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)();  
      
            // Add an [AnimationPlayableOutput](Animations.AnimationPlayableOutput.html) to the graph.
            var animOutput = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "AnimationOutput", GetComponent<[Animator](Animator.html)>());  
      
            // Add an [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html) to the graph.
            var mixerPlayable = [AnimationMixerPlayable.Create](Animations.AnimationMixerPlayable.Create.html)(m_Graph, 2);  
      
            // Add two [AnimationClipPlayable](Animations.AnimationClipPlayable.html) to the graph.
            var clipPlayableA = [AnimationClipPlayable.Create](Animations.AnimationClipPlayable.Create.html)(m_Graph, clipA);
            var clipPlayableB = [AnimationClipPlayable.Create](Animations.AnimationClipPlayable.Create.html)(m_Graph, clipB);  
      
            // Add a custom [PlayableBehaviour](Playables.PlayableBehaviour.html) to the graph.
            // This behavior will change the weights of the mixer dynamically.
            var blenderPlayable = ScriptPlayable<BlenderPlayableBehaviour>.Create(m_Graph, 1);
            blenderPlayable.GetBehaviour().mixerPlayable = mixerPlayable;  
      
            // Create the topology, connect the [AnimationClipPlayable](Animations.AnimationClipPlayable.html) to the
            // [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html).  Also add the BlenderPlayableBehaviour.
            m_Graph.Connect(clipPlayableA, 0, mixerPlayable, 0);
            m_Graph.Connect(clipPlayableB, 0, mixerPlayable, 1);
            m_Graph.Connect(mixerPlayable, 0, blenderPlayable, 0);  
      
            // Use the ScriptPlayable as the source for the [AnimationPlayableOutput](Animations.AnimationPlayableOutput.html).
            // Since it's a ScriptPlayable, also set the source input port to make the
            // passthrough to the [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html).
            animOutput.SetSourcePlayable(blenderPlayable);
            animOutput.SetSourceInputPort(0);  
      
            // Play the graph.
            m_Graph.Play();
        }  
      
        private void OnDestroy()
        {
            // Destroy the graph once done with it.
            m_Graph.Destroy();
        }
    }
    

### Public Methods

[OnBehaviourPause](Playables.PlayableBehaviour.OnBehaviourPause.html)| This
method is invoked when one of the following situations occurs: The effective
play state during traversal is changed to PlayState.Paused. This state is
indicated by FrameData.effectivePlayState. The PlayableGraph is stopped while
the playable play state is Playing. This state is indicated by
PlayableGraph.IsPlaying returning true.  
---|---  
[OnBehaviourPlay](Playables.PlayableBehaviour.OnBehaviourPlay.html)| This
function is called when the Playable play state is changed to
PlayState.Playing.  
[OnGraphStart](Playables.PlayableBehaviour.OnGraphStart.html)| This function
is called when the PlayableGraph that owns this PlayableBehaviour starts.  
[OnGraphStop](Playables.PlayableBehaviour.OnGraphStop.html)| This function is
called when the PlayableGraph that owns this PlayableBehaviour stops.  
[OnPlayableCreate](Playables.PlayableBehaviour.OnPlayableCreate.html)| This
function is called when the Playable that owns the PlayableBehaviour is
created.  
[OnPlayableDestroy](Playables.PlayableBehaviour.OnPlayableDestroy.html)| This
function is called when the Playable that owns the PlayableBehaviour is
destroyed.  
[PrepareData](Playables.PlayableBehaviour.PrepareData.html)| This function is
called during the PrepareData phase of the PlayableGraph.  
[PrepareFrame](Playables.PlayableBehaviour.PrepareFrame.html)| This function
is called during the PrepareFrame phase of the PlayableGraph.  
[ProcessFrame](Playables.PlayableBehaviour.ProcessFrame.html)| This function
is called during the ProcessFrame phase of the PlayableGraph.  
  
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

