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

#  [Animator](Animator.html).GetCurrentAnimatorStateInfo

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

public [AnimatorStateInfo](AnimatorStateInfo.html)
GetCurrentAnimatorStateInfo(int layerIndex);

### Parameters

layerIndex | The layer index.  
---|---  
  
### Returns

**AnimatorStateInfo** An [AnimatorStateInfo](AnimatorStateInfo.html) with the
information on the current state.

### Description

Returns an [AnimatorStateInfo](AnimatorStateInfo.html) with the information on
the current state.

Fetches the data from the current state in the Animator. Use this to get
details from the state, including accessing the state’s speed, length, name
and other variables. For gathering information from the clips that the states
hold, see
[Animator.GetCurrentAnimatorClipInfo](Animator.GetCurrentAnimatorClipInfo.html).

    
    
    //Create a [GameObject](GameObject.html) and attach an [Animator](Animator.html) component (Click the **Add Component** button in the Inspector window, go to **Miscellaneous** >**Animator**).
    //Create an [Animator](Animator.html) by going to **Assets** >  **Create** > **Animator Controller**. Attach this Controller to the [Animator](Animator.html) attached to your [GameObject](GameObject.html)
    //In the [Animator](Animator.html) Controller, create a Trigger parameter in the **Parameters** tab and name it “Jump”. Then create states and transition arrows that use this parameter.  
      
    //This script triggers an [Animation](Animation.html) parameter when you press the space key.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Animator](Animator.html) m_Animator;
        //Use to output current speed of the state to the screen
        float m_CurrentSpeed;  
      
        void Start()
        {
            //Get the [Animator](Animator.html), which you attach to the [GameObject](GameObject.html) you intend to animate.
            m_Animator = gameObject.GetComponent<[Animator](Animator.html)>();
            //The current speed of the first [Animator](Animator.html) state
            m_CurrentSpeed = m_Animator.GetCurrentAnimatorStateInfo(0).speed;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space bar to tell the [Animator](Animator.html) to trigger the Jump [Animation](Animation.html)
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                m_Animator.SetTrigger("Jump");
            }  
      
            //When entering the Jump state in the [Animator](Animator.html), output the message in the console
            if (m_Animator.GetCurrentAnimatorStateInfo(0).IsName("Jump"))
            {
                [Debug.Log](Debug.Log.html)("Jumping");
            }
        }  
      
        void OnGUI()
        {
            //Output the first [Animation](Animation.html) speed to the screen
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 25, 200, 20),  "Speed of [State](Random.State.html) : " + m_CurrentSpeed);
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

