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

#  [Animator](Animator.html).speed

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

public float speed;

### Description

The playback speed of the Animator. 1 is normal playback speed.

Use [Animator.speed](Animator-speed.html) to manipulate the playback speed of
the Animator. Any animations currently being played by the Animator are slowed
down or sped up depending on how the speed is altered. Set speed to 1 for
normal playback. Negative playback speed is only supported when the recorder
is enabled. For more details refer to [Animator.recorderMode](Animator-
recorderMode.html).

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Animator](Animator.html) m_Animator;
        //Value from the slider, and it converts to speed level
        float m_MySliderValue;  
      
        void Start()
        {
            //Get the animator, attached to the [GameObject](GameObject.html) you are intending to animate.
            m_Animator = gameObject.GetComponent<[Animator](Animator.html)>();
        }  
      
        void OnGUI()
        {
            //Create a [Label](UIElements.Label.html) in Game view for the [Slider](UIElements.Slider.html)
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 25, 40, 60), "Speed");
            //Create a horizontal [Slider](UIElements.Slider.html) to control the speed of the [Animator](Animator.html). Drag the slider to 1 for normal speed.  
      
            m_MySliderValue = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(45, 25, 200, 60), m_MySliderValue, 0.0F, 1.0F);
            //Make the speed of the [Animator](Animator.html) match the [Slider](UIElements.Slider.html) value
            m_Animator.speed = m_MySliderValue;
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

