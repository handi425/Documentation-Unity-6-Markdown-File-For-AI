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

# PropertySceneHandle

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

Handle to read a [Component](Component.html) property on an object in the
Scene.

PropertySceneHandle are read-only.

    
    
    using UnityEngine;
    using UnityEngine.Playables;
    using UnityEngine.Animations;  
      
    public struct PropertySceneHandleJob : [IAnimationJob](Animations.IAnimationJob.html)
    {
        public [PropertySceneHandle](Animations.PropertySceneHandle.html) handleR;
        public [PropertySceneHandle](Animations.PropertySceneHandle.html) handleG;
        public [PropertySceneHandle](Animations.PropertySceneHandle.html) handleB;  
      
        public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream)
        {
        }  
      
        public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
        {
            // Log the light color.
            var r = handleR.GetFloat(stream);
            var g = handleG.GetFloat(stream);
            var b = handleB.GetFloat(stream);
            [Debug.LogFormat](Debug.LogFormat.html)("[Light](Light.html) color: (R: {0}, G: {1}, B: {2})", r, g, b);
        }
    }  
      
    [[RequireComponent](RequireComponent.html)(typeof([Animator](Animator.html)))]
    [[RequireComponent](RequireComponent.html)(typeof([Light](Light.html)))]
    public class PropertySceneHandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Light](Light.html) sceneLight;  
      
        [PlayableGraph](Playables.PlayableGraph.html) m_Graph;
        [AnimationScriptPlayable](Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
      
        void Start()
        {
            if (sceneLight == null)
                return;  
      
            var animator = GetComponent<[Animator](Animator.html)>();  
      
            m_Graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)("PropertySceneHandleExample");
            var output = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
      
            var animationJob = new PropertySceneHandleJob();
            animationJob.handleR = animator.BindSceneProperty(sceneLight.transform, typeof([Light](Light.html)), "m_Color.r");
            animationJob.handleG = animator.BindSceneProperty(sceneLight.transform, typeof([Light](Light.html)), "m_Color.g");
            animationJob.handleB = animator.BindSceneProperty(sceneLight.transform, typeof([Light](Light.html)), "m_Color.b");
            m_AnimationScriptPlayable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
      
            output.SetSourcePlayable(m_AnimationScriptPlayable);
            m_Graph.Play();
        }  
      
        void OnDisable()
        {
            if (sceneLight == null)
                return;  
      
            m_Graph.Destroy();
        }
    }
    

Additional resources:
[AnimatorJobExtensions.BindSceneProperty](Animations.AnimatorJobExtensions.BindSceneProperty.html),
[TransformSceneHandle](Animations.TransformSceneHandle.html),
[PropertyStreamHandle](Animations.PropertyStreamHandle.html), and
[TransformStreamHandle](Animations.TransformStreamHandle.html).

### Public Methods

[GetBool](Animations.PropertySceneHandle.GetBool.html)| Gets the boolean
property value from an object in the Scene.  
---|---  
[GetFloat](Animations.PropertySceneHandle.GetFloat.html)| Gets the float
property value from an object in the Scene.  
[GetInt](Animations.PropertySceneHandle.GetInt.html)| Gets the integer
property value from an object in the Scene.  
[IsResolved](Animations.PropertySceneHandle.IsResolved.html)| Returns whether
or not the handle is resolved.  
[IsValid](Animations.PropertySceneHandle.IsValid.html)| Returns whether or not
the handle is valid.  
[Resolve](Animations.PropertySceneHandle.Resolve.html)| Resolves the handle.  
  
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

