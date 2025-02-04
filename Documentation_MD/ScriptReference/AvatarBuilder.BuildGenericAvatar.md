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

#  [AvatarBuilder](AvatarBuilder.html).BuildGenericAvatar

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

public static [Avatar](Avatar.html)
BuildGenericAvatar([GameObject](GameObject.html) go, string
rootMotionTransformName);

### Parameters

go | Root object of your transform hierarchy.  
---|---  
rootMotionTransformName | Transform name of the root motion transform. If empty no root motion is defined and you must take care of avatar movement yourself.  
  
### Description

Create a new generic avatar.

All transforms under the root game object will be part of this generic avatar.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [GameObject](GameObject.html) activeGameObject = [Selection.activeGameObject](Selection-activeGameObject.html);  
      
            if (activeGameObject != null &&
                activeGameObject.GetComponent<[Animator](Animator.html)>() != null)
            {
                [Avatar](Avatar.html) avatar = [AvatarBuilder.BuildGenericAvatar](AvatarBuilder.BuildGenericAvatar.html)(activeGameObject, "");
                avatar.name = "InsertYourName";
                [Debug.Log](Debug.Log.html)(avatar.isHuman ? "is human" : "is generic");  
      
                [Animator](Animator.html) animator = activeGameObject.GetComponent<[Animator](Animator.html)>() as [Animator](Animator.html);
                animator.avatar = avatar;
            }
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

