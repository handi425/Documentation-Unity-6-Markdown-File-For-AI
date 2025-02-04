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

#
[AnimationLayerMixerPlayable](Animations.AnimationLayerMixerPlayable.html).SetLayerMaskFromAvatarMask

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

public void SetLayerMaskFromAvatarMask(uint layerIndex,
[AvatarMask](AvatarMask.html) mask);

### Parameters

layerIndex | The layer index.  
---|---  
mask | The AvatarMask used to create the new LayerMask.  
  
### Description

Sets the mask for the current layer.

This function generates a layer mask from the specified AvatarMask, and
applies it to the specified Layer index. If you change the AvatarMask, you
need to call this function again to update the layer mask.

    
    
    using System.Collections.Generic;
    using UnityEngine;  
      
    using UnityEngine.Playables;
    using UnityEngine.Animations;  
      
    public class LayerMixerPlayable : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AnimationClip](AnimationClip.html) clip1;
        public [AnimationClip](AnimationClip.html) clip2;
        public [Transform](Transform.html) leftShoulder;  
      
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        [AnimationLayerMixerPlayable](Animations.AnimationLayerMixerPlayable.html) m_Mixer;  
      
        public float mixLevel = 0.5f;  
      
        [AvatarMask](AvatarMask.html) mask;  
      
        public void Start()
        {
            [Animator](Animator.html) animator = GetComponent<[Animator](Animator.html)>();  
      
            mask = new [AvatarMask](AvatarMask.html)();
            mask.AddTransformPath(leftShoulder, true);  
      
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)();
            var playableOutput = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "LayerMixer", animator);
            playableOutput.SetSourcePlayable(m_Mixer);  
      
            // Create two clip playables
            var clipPlayable1 = [AnimationClipPlayable.Create](Animations.AnimationClipPlayable.Create.html)(m_Graph, clip1);
            var clipPlayable2 = [AnimationClipPlayable.Create](Animations.AnimationClipPlayable.Create.html)(m_Graph, clip2);  
      
            // Create mixer playable
            m_Mixer = [AnimationLayerMixerPlayable.Create](Animations.AnimationLayerMixerPlayable.Create.html)(m_Graph, 2);  
      
            // Create two layers, second is setup to override the first layer and affect only left shoulder and childs
            m_Mixer.ConnectInput(0, clipPlayable1, 0, 1.0f);
            m_Mixer.ConnectInput(1, clipPlayable2, 0, mixLevel);  
      
            m_Mixer.SetLayerMaskFromAvatarMask(1, mask);  
      
            m_Graph.Play();
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            m_Mixer.SetInputWeight(1, mixLevel);
        }  
      
        public void OnDestroy()
        {
            m_Graph.Destroy();
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

