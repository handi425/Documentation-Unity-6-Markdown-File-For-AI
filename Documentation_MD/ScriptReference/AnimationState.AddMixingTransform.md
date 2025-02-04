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

#  [AnimationState](AnimationState.html).AddMixingTransform

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

public void AddMixingTransform([Transform](Transform.html) mix, bool recursive
= true);

### Parameters

mix | The transform to animate.  
---|---  
recursive | Whether to also animate all children of the specified transform.  
  
### Description

Adds a transform which should be animated. This allows you to reduce the
number of animations you have to create.

For example you might have a handwaving animation. You might want to play the
hand waving animation on a idle character or on a walking character. Either
you have to create 2 hand waving animations one for idle, one for walking. By
using mixing the hand waving animation will have full control of the shoulder.
But the lower body will not be affected by it, and continue playing the idle
or walk animation. Thus you only need one hand waving animation.  
  
If `recursive` is true all children of the `mix` transform will also be
animated. If you don't call AddMixingTransform, all animation curves will be
used.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Animation](Animation.html) anim;
        public [Transform](Transform.html) shoulder;  
      
        void Start()
        {
            // Add mixing transform
            anim["wave_hand"].AddMixingTransform(shoulder);
        }
    }
    

Another example using a path:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Animation](Animation.html) anim;  
      
        void Start()
        {
            // Adds a mixing transform using a path instead
            [Transform](Transform.html) mixTransform = transform.Find("root/upper_body/left_shoulder");  
      
            // Add mixing transform
            anim["wave_hand"].AddMixingTransform(mixTransform);
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

