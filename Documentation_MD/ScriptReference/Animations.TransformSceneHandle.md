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

# TransformSceneHandle

struct in UnityEngine.Animations

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

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

Handle to read position, rotation and scale of an object in the Scene.

TransformSceneHandle are read-only.  
  
A TransformSceneHandle is a safe handle on a
[TransformAccess](Jobs.TransformAccess.html). The [Animator](Animator.html)
used to create this handle manages the validity of this handle.

    
    
    using UnityEngine;
    using UnityEngine.Playables;
    using UnityEngine.Animations;  
      
    public struct TransformSceneHandleJob : [IAnimationJob](Animations.IAnimationJob.html)
    {
        public [TransformSceneHandle](Animations.TransformSceneHandle.html) handle;  
      
        public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream)
        {
            // Log the local position.
            var position = handle.GetLocalPosition(stream);
            [Debug.LogFormat](Debug.LogFormat.html)("[Position](UIElements.Position.html): {0}", position);  
      
            // Log the local rotation (converted from euler).
            var rotation = handle.GetLocalRotation(stream);
            [Debug.LogFormat](Debug.LogFormat.html)("Rotation: {0}", rotation.eulerAngles);  
      
            // Log the local scale.
            var scale = handle.GetLocalScale(stream);
            [Debug.LogFormat](Debug.LogFormat.html)("[Scale](UIElements.Scale.html): {0}", scale);
        }  
      
        public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
        {
        }
    }  
      
    [[RequireComponent](RequireComponent.html)(typeof([Animator](Animator.html)))]
    public class TransformSceneHandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) sceneTransform;  
      
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
      
        void Start()
        {
            if (sceneTransform == null)
                return;  
      
            var animator = GetComponent<[Animator](Animator.html)>();  
      
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)("TransformSceneHandleExample");
            var output = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
      
            var animationJob = new TransformSceneHandleJob();
            animationJob.handle = animator.BindSceneTransform(sceneTransform);
            m_AnimationScriptPlayable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
      
            output.SetSourcePlayable(m_AnimationScriptPlayable);
            m_Graph.Play();
        }  
      
        void OnDisable()
        {
            if (sceneTransform == null)
                return;  
      
            m_Graph.Destroy();
        }
    }
    

Additional resources:
[AnimatorJobExtensions.BindSceneTransform](Animations.AnimatorJobExtensions.BindSceneTransform.html),
[PropertySceneHandle](Animations.PropertySceneHandle.html),
[PropertyStreamHandle](Animations.PropertyStreamHandle.html), and
[TransformStreamHandle](Animations.TransformStreamHandle.html).

### Public Methods

[GetGlobalTR](Animations.TransformSceneHandle.GetGlobalTR.html)| Gets the
position and scaled rotation of the transform in world space.  
---|---  
[GetLocalPosition](Animations.TransformSceneHandle.GetLocalPosition.html)|
Gets the position of the transform relative to the parent.  
[GetLocalRotation](Animations.TransformSceneHandle.GetLocalRotation.html)|
Gets the rotation of the transform relative to the parent.  
[GetLocalScale](Animations.TransformSceneHandle.GetLocalScale.html)| Gets the
scale of the transform relative to the parent.  
[GetLocalToParentMatrix](Animations.TransformSceneHandle.GetLocalToParentMatrix.html)|
Gets the local to parent matrix of the transform.  
[GetLocalToWorldMatrix](Animations.TransformSceneHandle.GetLocalToWorldMatrix.html)|
Gets the local to world matrix of the transform.  
[GetLocalTRS](Animations.TransformSceneHandle.GetLocalTRS.html)| Gets the
position, rotation and scale of the transform relative to the parent.  
[GetPosition](Animations.TransformSceneHandle.GetPosition.html)| Gets the
position of the transform in world space.  
[GetRotation](Animations.TransformSceneHandle.GetRotation.html)| Gets the
rotation of the transform in world space.  
[IsValid](Animations.TransformSceneHandle.IsValid.html)| Returns whether this
is a valid handle.  
  
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

