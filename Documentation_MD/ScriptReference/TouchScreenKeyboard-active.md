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

#  [TouchScreenKeyboard](TouchScreenKeyboard.html).active

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

public bool active;

### Description

Is the keyboard visible or sliding into the position on the screen?

Use this property to bring previously hidden keyboard back on the screen.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Hides the keyboard if the device is facing down
        // and resumes input if the device is facing up.  
      
        [TouchScreenKeyboard](TouchScreenKeyboard.html) keyboard;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (keyboard != null)
            {
                if ([Input.deviceOrientation](Input-deviceOrientation.html) == [DeviceOrientation.FaceDown](DeviceOrientation.FaceDown.html))
                    keyboard.active = false;
                if ([Input.deviceOrientation](Input-deviceOrientation.html) == [DeviceOrientation.FaceUp](DeviceOrientation.FaceUp.html))
                    keyboard.active = true;
            }
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 10, 200, 32), "Open keyboard"))
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("text");
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

