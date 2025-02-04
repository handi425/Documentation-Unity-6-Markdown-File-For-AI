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

#  [EditorGUI](EditorGUI.html).PasswordField

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

public static string PasswordField([Rect](Rect.html) position, string
password, [GUIStyle](GUIStyle.html) style = EditorStyles.textField);

## Declaration

public static string PasswordField([Rect](Rect.html) position, string label,
string password, [GUIStyle](GUIStyle.html) style = EditorStyles.textField);

## Declaration

public static string PasswordField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, string password,
[GUIStyle](GUIStyle.html) style = EditorStyles.textField);

### Parameters

position | Rectangle on the screen to use for the password field.  
---|---  
label | Optional label to display in front of the password field.  
password | The password to edit.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**string** The password entered by the user.

### Description

Makes a text field where the user can enter a password.

This works just like [GUI.PasswordField](GUI.PasswordField.html), but
correctly responds to select all, etc. in the editor, and it can have an
optional label in front.  
  
![](../StaticFiles/ScriptRefImages/EditorGUIPasswordField.png)  
_Password Field in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // [Editor](Editor.html) Script that creates a password field and lets you visualize what have you
    // typed in a label.  
      
    class EditorGUIPasswordField : [EditorWindow](EditorWindow.html)
    {
        string text = "Some text here";  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) Password field usage")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow<EditorGUIPasswordField>();
            window.Show();
        }  
      
        void OnGUI()
        {
            text = [EditorGUI.PasswordField](EditorGUI.PasswordField.html)(
                new [Rect](Rect.html)(3, 3, position.width - 6, 20),
                "Type Something:",
                text);  
      
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(
                new [Rect](Rect.html)(3, 25, position.width - 5, 20),
                "Written Text:",
                text);
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

