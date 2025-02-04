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

# AnimatorClipInfo

struct in UnityEngine

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

Information about clip being played and blended by the Animator.

Additional resources:
[Animator.GetCurrentAnimatorClipInfo](Animator.GetCurrentAnimatorClipInfo.html)
and [Animator.GetNextAnimatorClipInfo](Animator.GetNextAnimatorClipInfo.html).

    
    
    //Create a [GameObject](GameObject.html) and attach an [Animator](Animator.html) component (Click the Add [Component](Component.html) button in the Inspector of the [GameObject](GameObject.html) and go to Miscellaneous>[Animator](Animator.html)). Set up the [Animator](Animator.html) how you would like.
    //Attach this script to the [GameObject](GameObject.html)  
      
    //This script outputs the current clip from the [Animator](Animator.html) to the console
    using UnityEngine;  
      
    public class AnimationClipInfoClipExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [Animator](Animator.html) m_Animator;
        [AnimatorClipInfo](AnimatorClipInfo.html)[] m_AnimatorClipInfo;  
      
        // Use this for initialization
        void Start()
        {
            //Fetch the [Animator](Animator.html) component from the [GameObject](GameObject.html)
            m_Animator = GetComponent<[Animator](Animator.html)>();
            //Get the animator clip information from the [Animator](Animator.html) Controller
            m_AnimatorClipInfo = m_Animator.GetCurrentAnimatorClipInfo(0);
            //Output the name of the starting clip
            [Debug.Log](Debug.Log.html)("Starting clip : " + m_AnimatorClipInfo[0].clip);
        }
    }
    

### Properties

[clip](AnimatorClipInfo-clip.html)| Returns the animation clip played by the
Animator.  
---|---  
[weight](AnimatorClipInfo-weight.html)| Returns the blending weight used by
the Animator to blend this clip.  
  
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

