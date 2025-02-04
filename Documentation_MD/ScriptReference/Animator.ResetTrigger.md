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

#  [Animator](Animator.html).ResetTrigger

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

public void ResetTrigger(string name);

## Declaration

public void ResetTrigger(int id);

### Parameters

name | The parameter name.  
---|---  
id | The parameter ID.  
  
### Description

Resets the value of the given trigger parameter.

Use this to reset a Trigger [parameter](../Manual/AnimationParameters.html) in
an Animator Controller that could still be active. Make sure to create a
parameter in the Animator Controller with the same name. See
[Animator.SetTrigger](Animator.SetTrigger.html) for more information about how
to set a Trigger.

    
    
    //Attach this script to a [GameObject](GameObject.html) with an [Animator](Animator.html) component attached.
    //For this example, create parameters in the [Animator](Animator.html) and name them “Crouch” and “Jump”
    //Apply these parameters to your transitions between states  
      
    //This script allows you to trigger an [Animator](Animator.html) parameter and reset the other that could possibly still be active. Press the up and down arrow keys to do this.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Animator](Animator.html) m_Animator;  
      
        void Start()
        {
            //Get the [Animator](Animator.html) attached to the [GameObject](GameObject.html) you are intending to animate.
            m_Animator = gameObject.GetComponent<[Animator](Animator.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the up arrow button to reset the trigger and set another one
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.UpArrow](KeyCode.UpArrow.html)))
            {
                //Reset the "Crouch" trigger
                m_Animator.ResetTrigger("Crouch");
                //Send the message to the [Animator](Animator.html) to activate the trigger parameter named "Jump"
                m_Animator.SetTrigger("Jump");
            }  
      
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.DownArrow](KeyCode.DownArrow.html)))
            {
                //Reset the "Jump" trigger
                m_Animator.ResetTrigger("Jump");
                //Send the message to the [Animator](Animator.html) to activate the trigger parameter named "Crouch"
                m_Animator.SetTrigger("Crouch");
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

