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

#  [Animator](Animator.html).GetBool

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

public bool GetBool(string name);

## Declaration

public bool GetBool(int id);

### Parameters

name | The parameter name.  
---|---  
id | The parameter ID.  
  
### Returns

**bool** The value of the parameter.

### Description

Returns the value of the given boolean parameter.

Return the current state of a bool parameter within the Animator Controller.
Use the parameter’s name or ID to search for the appropriate one.

    
    
    //Attach this script to a [GameObject](GameObject.html) with an [Animator](Animator.html) component attached.
    //For this example, create parameters in the [Animator](Animator.html) and name them “Crouch” and “Jump”
    //Apply these parameters to your transitions between states  
      
    //This script allows you to set a Boolean [Animator](Animator.html) parameter on and set another Boolean parameter to off if it is currently playing. Press the space key to do this.  
      
    using UnityEngine;  
      
    public class AnimatorGetBool : [MonoBehaviour](MonoBehaviour.html)
    {
        //Fetch the [Animator](Animator.html)
        [Animator](Animator.html) m_Animator;
        // Use this to decide if the [GameObject](GameObject.html) can jump or not
        bool m_Jump;  
      
        void Start()
        {
            //This gets the [Animator](Animator.html), which should be attached to the [GameObject](GameObject.html) you are intending to animate.
            m_Animator = gameObject.GetComponent<[Animator](Animator.html)>();
            // The [GameObject](GameObject.html) cannot jump
            m_Jump = false;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space bar to enable the "Jump" parameter in the [Animator](Animator.html) Controller
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //Set the "Jump" parameter in the [Animator](Animator.html) Controller to true
                m_Animator.SetBool("Jump", true);
                //Check to see if the "Crouch" parameter is enabled
                if (m_Animator.GetBool("Crouch"))
                {
                    //If the "Crouch" parameter is enabled, disable it as the [Animation](Animation.html) should no longer be crouching
                    m_Animator.SetBool("Crouch", false);
                }
            }
            //Otherwise the "Jump" parameter should be false
            else m_Animator.SetBool("Jump", false);  
      
            //Press the down arrow key to enable the "Crouch" parameter
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.DownArrow](KeyCode.DownArrow.html)))
                m_Animator.SetBool("Crouch", true);
            else
                m_Animator.SetBool("Crouch", false);
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

