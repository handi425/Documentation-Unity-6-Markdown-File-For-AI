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

# TransformStreamHandle

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

Position, rotation and scale of an object in the
[AnimationStream](Animations.AnimationStream.html).

    
    
    using UnityEngine;
    using UnityEngine.Playables;
    using UnityEngine.Animations;  
      
    public struct TransformStreamHandleJob : [IAnimationJob](Animations.IAnimationJob.html)
    {
        public [TransformStreamHandle](Animations.TransformStreamHandle.html) handle;
        public [Vector3](Vector3.html) position;
        public [Vector3](Vector3.html) rotation;
        public [Vector3](Vector3.html) scale;  
      
        public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream)
        {
            // Set the new local position.
            handle.SetLocalPosition(stream, position);  
      
            // Set the new local rotation (converted from euler).
            handle.SetLocalRotation(stream, [Quaternion.Euler](Quaternion.Euler.html)(rotation));  
      
            // Set the new local scale.
            handle.SetLocalScale(stream, scale);
        }  
      
        public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
        {
        }
    }  
      
    [[RequireComponent](RequireComponent.html)(typeof([Animator](Animator.html)))]
    public class TransformStreamHandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) position;
        public [Vector3](Vector3.html) rotation;
        public [Vector3](Vector3.html) scale = [Vector3.one](Vector3-one.html);  
      
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
      
        void Start()
        {
            var animator = GetComponent<[Animator](Animator.html)>();  
      
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)("TransformStreamHandleExample");
            var output = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
      
            var animationJob = new TransformStreamHandleJob();
            animationJob.handle = animator.BindStreamTransform(gameObject.transform);
            m_AnimationScriptPlayable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
      
            output.SetSourcePlayable(m_AnimationScriptPlayable);
            m_Graph.Play();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var animationJob = m_AnimationScriptPlayable.GetJobData<TransformStreamHandleJob>();
            animationJob.position = position;
            animationJob.rotation = rotation;
            animationJob.scale = scale;
            m_AnimationScriptPlayable.SetJobData(animationJob);
        }  
      
        void OnDisable()
        {
            m_Graph.Destroy();
        }
    }
    

Additional resources:
[AnimatorJobExtensions.BindStreamTransform](Animations.AnimatorJobExtensions.BindStreamTransform.html),
[PropertyStreamHandle](Animations.PropertyStreamHandle.html),
[PropertySceneHandle](Animations.PropertySceneHandle.html), and
[TransformSceneHandle](Animations.TransformSceneHandle.html).

### Public Methods

[GetGlobalTR](Animations.TransformStreamHandle.GetGlobalTR.html)| Gets the
position and scaled rotation of the transform in world space.  
---|---  
[GetLocalPosition](Animations.TransformStreamHandle.GetLocalPosition.html)|
Gets the position of the transform relative to the parent.  
[GetLocalRotation](Animations.TransformStreamHandle.GetLocalRotation.html)|
Gets the rotation of the transform relative to the parent.  
[GetLocalScale](Animations.TransformStreamHandle.GetLocalScale.html)| Gets the
scale of the transform relative to the parent.  
[GetLocalToParentMatrix](Animations.TransformStreamHandle.GetLocalToParentMatrix.html)|
Gets the local to parent matrix of the transform.  
[GetLocalToWorldMatrix](Animations.TransformStreamHandle.GetLocalToWorldMatrix.html)|
Gets the local to world matrix of the transform.  
[GetLocalTRS](Animations.TransformStreamHandle.GetLocalTRS.html)| Gets the
position, rotation and scale of the transform relative to the parent.  
[GetPosition](Animations.TransformStreamHandle.GetPosition.html)| Gets the
position of the transform in world space.  
[GetPositionReadMask](Animations.TransformStreamHandle.GetPositionReadMask.html)|
Gets the position read mask of the transform.  
[GetRotation](Animations.TransformStreamHandle.GetRotation.html)| Gets the
rotation of the transform in world space.  
[GetRotationReadMask](Animations.TransformStreamHandle.GetRotationReadMask.html)|
Gets the rotation read mask of the transform.  
[GetScaleReadMask](Animations.TransformStreamHandle.GetScaleReadMask.html)|
Gets the scale read mask of the transform.  
[IsResolved](Animations.TransformStreamHandle.IsResolved.html)| Returns
whether this handle is resolved.  
[IsValid](Animations.TransformStreamHandle.IsValid.html)| Returns whether this
is a valid handle.  
[Resolve](Animations.TransformStreamHandle.Resolve.html)| Bind this handle
with an animated values from the AnimationStream.  
[SetGlobalTR](Animations.TransformStreamHandle.SetGlobalTR.html)| Sets the
position and rotation of the transform in world space.  
[SetLocalPosition](Animations.TransformStreamHandle.SetLocalPosition.html)|
Sets the position of the transform relative to the parent.  
[SetLocalRotation](Animations.TransformStreamHandle.SetLocalRotation.html)|
Sets the rotation of the transform relative to the parent.  
[SetLocalScale](Animations.TransformStreamHandle.SetLocalScale.html)| Sets the
scale of the transform relative to the parent.  
[SetLocalTRS](Animations.TransformStreamHandle.SetLocalTRS.html)| Sets the
position, rotation and scale of the transform relative to the parent.  
[SetPosition](Animations.TransformStreamHandle.SetPosition.html)| Sets the
position of the transform in world space.  
[SetRotation](Animations.TransformStreamHandle.SetRotation.html)| Sets the
rotation of the transform in world space.  
  
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

