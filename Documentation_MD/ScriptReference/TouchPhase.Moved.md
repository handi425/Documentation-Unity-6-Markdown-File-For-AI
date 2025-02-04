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

#  [TouchPhase](TouchPhase.html).Moved

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

A finger moved on the screen.

    
    
    //Attach this script to an empty [GameObject](GameObject.html)
    //Create some UI Text by going to Create>UI>Text.
    //Drag this [GameObject](GameObject.html) into the Text field of your [GameObject](GameObject.html)’s Inspector window.  
      
    using UnityEngine;
    using System.Collections;
    using UnityEngine.UI;  
      
    public class TouchPhaseExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector2](Vector2.html) startPos;
        public [Vector2](Vector2.html) direction;  
      
        public Text m_Text;
        string message;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //[Update](PlayerLoop.Update.html) the Text on the screen depending on current [TouchPhase](TouchPhase.html), and the current direction vector
            m_Text.text = "[Touch](Touch.html) : " + message + "in direction" + direction;  
      
            // Track a single touch as a direction control.
            if ([Input.touchCount](Input-touchCount.html) > 0)
            {
                [Touch](Touch.html) touch = [Input.GetTouch](Input.GetTouch.html)(0);  
      
                // Handle finger movements based on [TouchPhase](TouchPhase.html)
                switch (touch.phase)
                {
                    //When a touch has first been detected, change the message and record the starting position
                    case [TouchPhase.Began](TouchPhase.Began.html):
                        // Record initial touch position.
                        startPos = touch.position;
                        message = "Begun ";
                        break;  
      
                    //Determine if the touch is a moving touch
                    case [TouchPhase.Moved](TouchPhase.Moved.html):
                        // Determine direction by comparing the current touch position with the initial one
                        direction = touch.position - startPos;
                        message = "Moving ";
                        break;  
      
                    case [TouchPhase.Ended](TouchPhase.Ended.html):
                        // Report that the touch has ended when it ends
                        message = "Ending ";
                        break;
                }
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

