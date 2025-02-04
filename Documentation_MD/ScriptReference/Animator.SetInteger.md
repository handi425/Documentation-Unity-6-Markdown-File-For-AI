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

#  [Animator](Animator.html).SetInteger

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

public void SetInteger(string name, int value);

## Declaration

public void SetInteger(int id, int value);

### Parameters

name | The parameter name.  
---|---  
id | The parameter ID.  
value | The new parameter value.  
  
### Description

Sets the value of the given integer parameter.

Use this as a way to trigger transitions between Animator states. One way of
using Integers instead of Floats or Booleans is to use it for something that
has multiple states, for example directions (turn left, turn right etc.). Each
direction could correspond to a number instead of having multiple Booleans
that have to be reset each time.  
  
See documentation on [Animation](../Manual/Animator.html) for more information
on setting up Animators.  
  
Note: You can identify the parameter by name or by ID number, but the name or
ID number must be the same as the parameter you want to change in the
Animator.

    
    
    //This script sends messages to an [Animator](Animator.html) component to tell it to make transitions based on an integer named “[States](VersionControl.Asset.States.html)”. You change and send this integer to the [Animator](Animator.html) by pressing the space and arrow keys.  
      
    //In order for this script to work, you have to set up your [Animator](Animator.html) Controller so the script can interact with it.
    //Create a new [Animator](Animator.html) Controller if you do not already have one you want to use. To do this, click on the [GameObject](GameObject.html) you want to animate and go to its Inspector window. Click the **Add Component** button and go to **Miscellaneous** >**Animator**).
    //Double click the [Animator](Animator.html) to see the [Animator](Animator.html) Controller window.  Open the **Parameters** tab and click the plus icon to add a new parameter. Choose Int from the dropdown. Name the new Integer (for this script, call it “[States](VersionControl.Asset.States.html)”).
    //Create a few animation states (right click the grid and choose **Create State** >**Empty**) and choose an [Animation](Animation.html) for each in the **Motion** field.
    //Next create transitions between each of the states (right click the state, choose **Make Transition** and click on the state you want it to transition to).
    //Finally, click on one of the arrows to bring up its Inspector. Click the + icon under the Conditions section and choose the parameter you made (“[States](VersionControl.Asset.States.html)”). Change **Greater** to **Equals** and choose a number that you want to represent this state. Do the same with any other states.
    //You may want to set up transitions back to the first animation state so that when the button is let go, it will return to the first state. You may also want to uncheck the **Has Exit Time** box for each transition. Otherwise transitions will wait for an animation to finish before proceeding.  
      
    using UnityEngine;  
      
    public class AnimatorSetIntExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [Animator](Animator.html) m_Animator;  
      
        void Start()
        {
            //Fetch the [Animator](Animator.html) from the [GameObject](GameObject.html) you attached the script to
            m_Animator = GetComponent<[Animator](Animator.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Check if the horizontal buttons (A,D, left and right arrow keys) are being pressed
            if ([Input.GetAxis](Input.GetAxis.html)("Horizontal") > 0 || [Input.GetAxis](Input.GetAxis.html)("Horizontal") < 0)
                //Set the integer named "[States](VersionControl.Asset.States.html)" in your [Animator](Animator.html) to 1. If the [Animator](Animator.html) is set up properly, this should trigger an animation.
                m_Animator.SetInteger("[States](VersionControl.Asset.States.html)", 1);
            //Press the down arrow key to start another animation transition
            else if ([Input.GetKey](Input.GetKey.html)([KeyCode.DownArrow](KeyCode.DownArrow.html)))
                //Set the "[States](VersionControl.Asset.States.html)" integer to 2. This triggers the animation that should start when "[States](VersionControl.Asset.States.html)" is equal to 2
                m_Animator.SetInteger("[States](VersionControl.Asset.States.html)", 2);
            //Press the space key to set the "[States](VersionControl.Asset.States.html) integer to 3
            else if ([Input.GetKey](Input.GetKey.html)([KeyCode.Space](KeyCode.Space.html)))
                m_Animator.SetInteger("[States](VersionControl.Asset.States.html)", 3);
            else
                //If all the other keys are let go, set the "[States](VersionControl.Asset.States.html)" integer to 0.
                m_Animator.SetInteger("[States](VersionControl.Asset.States.html)", 0);
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

