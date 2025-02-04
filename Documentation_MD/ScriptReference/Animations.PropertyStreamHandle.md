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

# PropertyStreamHandle

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

Handle for a [Component](Component.html) property on an object in the
[AnimationStream](Animations.AnimationStream.html).

    
    
    using UnityEngine;
    using UnityEngine.Playables;
    using UnityEngine.Animations;  
      
    public struct PropertyStreamHandleJob : [IAnimationJob](Animations.IAnimationJob.html)
    {
        public [PropertyStreamHandle](Animations.PropertyStreamHandle.html) handleR;
        public [PropertyStreamHandle](Animations.PropertyStreamHandle.html) handleG;
        public [PropertyStreamHandle](Animations.PropertyStreamHandle.html) handleB;
        public [Color](Color.html) color;  
      
        public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream)
        {
        }  
      
        public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
        {
            // Set the new light color.
            handleR.SetFloat(stream, color.r);
            handleG.SetFloat(stream, color.g);
            handleB.SetFloat(stream, color.b);
        }
    }  
      
    [[RequireComponent](RequireComponent.html)(typeof([Animator](Animator.html)))]
    [[RequireComponent](RequireComponent.html)(typeof([Light](Light.html)))]
    public class PropertyStreamHandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Color](Color.html) color = [Color.white](Color-white.html);  
      
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
      
        void Start()
        {
            var animator = GetComponent<[Animator](Animator.html)>();  
      
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)("PropertyStreamHandleExample");
            var output = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
      
            var animationJob = new PropertyStreamHandleJob();
            animationJob.handleR = animator.BindStreamProperty(gameObject.transform, typeof([Light](Light.html)), "m_Color.r");
            animationJob.handleG = animator.BindStreamProperty(gameObject.transform, typeof([Light](Light.html)), "m_Color.g");
            animationJob.handleB = animator.BindStreamProperty(gameObject.transform, typeof([Light](Light.html)), "m_Color.b");
            m_AnimationScriptPlayable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
      
            output.SetSourcePlayable(m_AnimationScriptPlayable);
            m_Graph.Play();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var animationJob = m_AnimationScriptPlayable.GetJobData<PropertyStreamHandleJob>();
            animationJob.color = color;
            m_AnimationScriptPlayable.SetJobData(animationJob);
        }  
      
        void OnDisable()
        {
            m_Graph.Destroy();
        }
    }
    

Additional resources:
[AnimatorJobExtensions.BindStreamProperty](Animations.AnimatorJobExtensions.BindStreamProperty.html),
[TransformStreamHandle](Animations.TransformStreamHandle.html),
[PropertySceneHandle](Animations.PropertySceneHandle.html), and
[TransformSceneHandle](Animations.TransformSceneHandle.html).

### Public Methods

[GetBool](Animations.PropertyStreamHandle.GetBool.html)| Gets the boolean
property value from a stream.  
---|---  
[GetFloat](Animations.PropertyStreamHandle.GetFloat.html)| Gets the float
property value from a stream.  
[GetInt](Animations.PropertyStreamHandle.GetInt.html)| Gets the integer
property value from a stream.  
[GetReadMask](Animations.PropertyStreamHandle.GetReadMask.html)| Gets the read
mask of the property.  
[IsResolved](Animations.PropertyStreamHandle.IsResolved.html)| Returns whether
or not the handle is resolved.  
[IsValid](Animations.PropertyStreamHandle.IsValid.html)| Returns whether or
not the handle is valid.  
[Resolve](Animations.PropertyStreamHandle.Resolve.html)| Resolves the handle.  
[SetBool](Animations.PropertyStreamHandle.SetBool.html)| Sets the boolean
property value into a stream.  
[SetFloat](Animations.PropertyStreamHandle.SetFloat.html)| Sets the float
property value into a stream.  
[SetInt](Animations.PropertyStreamHandle.SetInt.html)| Sets the integer
property value into a stream.  
  
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

