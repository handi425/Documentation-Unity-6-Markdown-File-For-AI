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

#  [GUI](GUI.html).GetNameOfFocusedControl

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

public static string GetNameOfFocusedControl();

### Description

Get the name of named control that has focus.

Control names are set up by using
[SetNextControlName](GUI.SetNextControlName.html). When a named control has
focus, this function will return its name. If no control has focus or the
focused control has no name set, an empty string will be returned instead.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string login = "username";
        public string login2 = "no action here";  
      
        void OnGUI()
        {
            [GUI.SetNextControlName](GUI.SetNextControlName.html)("user");
            login = [GUI.TextField](GUI.TextField.html)(new [Rect](Rect.html)(10, 10, 130, 20), login);  
      
            login2 = [GUI.TextField](GUI.TextField.html)(new [Rect](Rect.html)(10, 40, 130, 20), login2);
            if (Event.current.isKey && Event.current.keyCode == [KeyCode.Return](KeyCode.Return.html) && [GUI.GetNameOfFocusedControl](GUI.GetNameOfFocusedControl.html)() == "user")
                [Debug.Log](Debug.Log.html)("Login");  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(150, 10, 50, 20), "Login"))
                [Debug.Log](Debug.Log.html)("Login");
        }
    }
    

Additional resources: [SetNextControlName](GUI.SetNextControlName.html),
[FocusControl](GUI.FocusControl.html).

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

