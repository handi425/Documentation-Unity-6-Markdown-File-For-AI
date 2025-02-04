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

#  [PlayableGraph](Playables.PlayableGraph.html).Connect

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

public bool Connect(U source, int sourceOutputPort, V destination, int
destinationInputPort);

### Parameters

source | The source playable or its handle.  
---|---  
sourceOutputPort | The port used in the source playable.  
destination | The destination playable or its handle.  
destinationInputPort | The port used in the destination playable. If set to -1, a new port is created and connected.  
  
### Returns

**bool** Returns true if connection is successful.

### Description

Connects two [Playable](Playables.Playable.html) instances.

The connections determine the topology of the
[PlayableGraph](Playables.PlayableGraph.html) and how it is evaluated.  
  
Playables can be connected together to form a tree structure. Each Playable
has a set of inputs and a set of outputs. These can be viewed as “slots” where
other Playables can be attached to.  
  
When a Playable is first created, its input count is reset to 0, meaning that
it has no children Playables attached. Outputs behave a little
differently—every Playable has a default output created when first created.  
  
You connect Playables together using the method
[PlayableGraph.Connect](Playables.PlayableGraph.Connect.html), and you can
disconnect them from each other using
[PlayableGraph.Disconnect](Playables.PlayableGraph.Disconnect.html).  
  
There is no limit set on the amount of inputs a Playable can have.

    
    
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    public class GraphCreationSample : [MonoBehaviour](MonoBehaviour.html)
    {
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        public [AnimationClip](AnimationClip.html) clipA;
        public [AnimationClip](AnimationClip.html) clipB;  
      
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
      
            // Create the topology, connect the [AnimationClipPlayable](Animations.AnimationClipPlayable.html) to the
            // [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html).
            m_Graph.Connect(clipPlayableA, 0, mixerPlayable, 0);
            m_Graph.Connect(clipPlayableB, 0, mixerPlayable, 1);  
      
            // Use the [AnimationMixerPlayable](Animations.AnimationMixerPlayable.html) as the source for the [AnimationPlayableOutput](Animations.AnimationPlayableOutput.html).
            animOutput.SetSourcePlayable(mixerPlayable);  
      
            // Set the weight for both inputs of the mixer.
            mixerPlayable.SetInputWeight(0, 1);
            mixerPlayable.SetInputWeight(1, 1);  
      
            // Play the graph.
            m_Graph.Play();
        }  
      
        private void OnDestroy()
        {
            // Destroy the graph once done with it.
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

