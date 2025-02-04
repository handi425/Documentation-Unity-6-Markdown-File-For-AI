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

#  [GUILayout](GUILayout.html).PasswordField

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

public static string PasswordField(string password, char maskChar, params
GUILayoutOption[] options);

## Declaration

public static string PasswordField(string password, char maskChar, int
maxLength, params GUILayoutOption[] options);

## Declaration

public static string PasswordField(string password, char maskChar,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static string PasswordField(string password, char maskChar, int
maxLength, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

password | Password to edit. The return value of this function should be assigned back to the string as shown in the example.  
---|---  
maskChar | Character to mask the password with.  
maxLength | The maximum length of the string. If left out, the user can type for ever and ever.  
style | The style to use. If left out, the `textField` style from the current [GUISkin](GUISkin.html) is used.  
  
### Returns

**string** The edited password.

### Description

Make a text field where the user can enter a password.

![](../StaticFiles/ScriptRefImages/GUILayoutPasswordField.png)  
_Password field in the Game View._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        string passwordToEdit = "My Password";  
      
        void OnGUI()
        {
            // Make a password field that modifies passwordToEdit.
            passwordToEdit = [GUILayout.PasswordField](GUILayout.PasswordField.html)(passwordToEdit, "*"[0], 25);
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

