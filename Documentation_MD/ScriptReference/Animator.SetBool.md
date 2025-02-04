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

#  [Animator](Animator.html).SetBool

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

public void SetBool(string name, bool value);

## Declaration

public void SetBool(int id, bool value);

### Parameters

name | The parameter name.  
---|---  
id | The parameter ID.  
value | The new parameter value.  
  
### Description

Sets the value of the given boolean parameter.

Use Animator.SetBool to pass Boolean values to an [Animator
Controller](../Manual/class-AnimatorController.html) via script.  
  
Use this to trigger transitions between Animator states. For example,
triggering a death animation by setting an “alive” boolean to false. See
documentation on [Animation](../Manual/AnimatorControllerCreation.html) for
more information on setting up Animators.  
  
Note: You can identify the parameter by name or by ID number, but the name or
ID number must be the same as the parameter you want to change in the
Animator.

    
    
    //Set up a new Boolean parameter in the Unity [Animator](Animator.html) and name it, in this case “Jump”.
    //Set up transitions between each state that the animation could follow. For example, the player could be running or idle before they jump, so both would need transitions into the animation.
    //If the “Jump” boolean is set to true at any point, the m_Animator plays the animation. However, if it is ever set to false, the animation would return to the appropriate state (“Idle”).
    //This script enables and disables this boolean in this case by listening for the mouse click or a tap of the screen.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Fetch the [Animator](Animator.html)
        [Animator](Animator.html) m_Animator;
        // Use this for deciding if the [GameObject](GameObject.html) can jump or not
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
            //Click the mouse or tap the screen to change the animation
            if ([Input.GetMouseButtonDown](Input.GetMouseButtonDown.html)(0))
                m_Jump = true;  
      
            //Otherwise the [GameObject](GameObject.html) cannot jump.
            else m_Jump = false;  
      
            //If the [GameObject](GameObject.html) is not jumping, send that the Boolean “Jump” is false to the [Animator](Animator.html). The jump animation does not play.
            if (m_Jump == false)
                m_Animator.SetBool("Jump", false);  
      
            //The [GameObject](GameObject.html) is jumping, so send the Boolean as enabled to the [Animator](Animator.html). The jump animation plays.
            if (m_Jump == true)
                m_Animator.SetBool("Jump", true);
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

