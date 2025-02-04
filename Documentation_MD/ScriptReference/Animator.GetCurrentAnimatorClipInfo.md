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

#  [Animator](Animator.html).GetCurrentAnimatorClipInfo

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

[Switch to Manual](../Manual/class-Animator.html "Go to Animator Component in
the Manual")

## Declaration

public AnimatorClipInfo[] GetCurrentAnimatorClipInfo(int layerIndex);

### Parameters

layerIndex | The layer index.  
---|---  
  
### Returns

**AnimatorClipInfo[]** An array of all the
[AnimatorClipInfo](AnimatorClipInfo.html) in the current state.

### Description

Returns an array of all the [AnimatorClipInfo](AnimatorClipInfo.html) in the
current state of the given layer.

    
    
    //This script outputs the name and length of the [Animation](Animation.html) clip played at start-up.  
      
    using UnityEngine;  
      
    public class GetCurrentAnimatorClipInfoExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [Animator](Animator.html) m_Animator;
        string m_ClipName;
        [AnimatorClipInfo](AnimatorClipInfo.html)[] m_CurrentClipInfo;  
      
        float m_CurrentClipLength;  
      
        void Start()
        {
            //Get them_Animator, which you attach to the [GameObject](GameObject.html) you intend to animate.
            m_Animator = gameObject.GetComponent<[Animator](Animator.html)>();
            //Fetch the current [Animation](Animation.html) clip information for the base layer
            m_CurrentClipInfo = this.m_Animator.GetCurrentAnimatorClipInfo(0);
            //Access the current length of the clip
            m_CurrentClipLength = m_CurrentClipInfo[0].clip.length;
            //Access the [Animation](Animation.html) clip name
            m_ClipName = m_CurrentClipInfo[0].clip.name;
        }  
      
        void OnGUI()
        {
            //Output the current [Animation](Animation.html) name and length to the screen
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 0, 200, 20),  "Clip Name : " + m_ClipName);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 30, 200, 20),  "Clip [Length](UIElements.Length.html) : " + m_CurrentClipLength);
        }
    }
    

* * *

## Declaration

public void GetCurrentAnimatorClipInfo(int layerIndex, List<AnimatorClipInfo>
clips);

### Parameters

layerIndex | The layer index.  
---|---  
clips | The list of [AnimatorClipInfo](AnimatorClipInfo.html) to fill.  
  
### Description

Fills `clips` with the list of all the
[AnimatorClipInfo](AnimatorClipInfo.html) in the current state of the given
layer.

Additional resources:
[GetCurrentAnimatorClipInfoCount](Animator.GetCurrentAnimatorClipInfoCount.html).

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

