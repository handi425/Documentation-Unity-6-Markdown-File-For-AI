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

#  [Touch](Touch.html).rawPosition

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

public [Vector2](Vector2.html) rawPosition;

### Description

The first position of the touch contact in screen space pixel coordinates.

Raw position returns the original position of a touch contact and doesn't
change as the touch is dragged. If you need the current position of the touch
see [Touch.position](Touch-position.html).  
  
The bottom-left of the screen or window is at (0, 0). The top-right of the
screen or window is at (Screen.width, Screen.height).

    
    
    // This script outputs the raw position of an active touch contact  
      
    // Attach this script to a [GameObject](GameObject.html)
    // Create a Text [GameObject](GameObject.html) ([GameObject](GameObject.html)>UI>Text)
    // Attach the Text to the Text field in the Inspector window of your [GameObject](GameObject.html)  
      
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class TouchRawPositionExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public Text m_Text;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.touchCount](Input-touchCount.html) > 0)
            {
                [Touch](Touch.html) touch = [Input.GetTouch](Input.GetTouch.html)(0);  
      
                // [Update](PlayerLoop.Update.html) the Text on the screen depending on the raw position of the touch
                // NOTE: rawPosition doesn't change when the touch contact is dragged
                m_Text.text = "Raw [Position](UIElements.Position.html) : " + touch.rawPosition;
            }
            else
            {
                m_Text.text = "No touch contacts";
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

