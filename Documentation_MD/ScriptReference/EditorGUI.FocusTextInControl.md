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

#  [EditorGUI](EditorGUI.html).FocusTextInControl

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

public static void FocusTextInControl(string name);

### Parameters

name | Name set using [GUI.SetNextControlName](GUI.SetNextControlName.html).  
---|---  
  
### Description

Move keyboard focus to a named text field and begin editing of the content.

In Editor GUI, text fields can have keyboard focus without the text being
edited. For example you may switch focus between text fields or other controls
by using the up and down arrow keys. Once you click inside the text field,
editing of the text itself begins and the arrow keys are then used to navigate
the text content.
[EditorGUI.FocusTextInControl](EditorGUI.FocusTextInControl.html) is like
[GUI.FocusControl](GUI.FocusControl.html) in that it gives keyboard focus to a
control, but it also begins editing of the text itself.  
  
Additional resources: [GUI.SetNextControlName](GUI.SetNextControlName.html),
[GUI.GetNameOfFocusedControl](GUI.GetNameOfFocusedControl.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [EditorWindow](EditorWindow.html)
    {
        // When pressed the button, selects the "username" Textfield.
        string username = "username";
        string pwd = "a pwd";
        void OnInspectorGUI()
        {
            // Set the internal name of the textfield
            [GUI.SetNextControlName](GUI.SetNextControlName.html)("MyTextField");  
      
            // Make the actual text field.
            username = [EditorGUI.TextField](EditorGUI.TextField.html)(new [Rect](Rect.html)(10, 10, 100, 20), username);
            pwd = [EditorGUI.TextField](EditorGUI.TextField.html)(new [Rect](Rect.html)(10, 40, 100, 20), pwd);  
      
            // If the user presses this button, keyboard focus will move.
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 70, 80, 20), "Move Focus"))
            {
                [EditorGUI.FocusTextInControl](EditorGUI.FocusTextInControl.html)("MyTextField");
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

