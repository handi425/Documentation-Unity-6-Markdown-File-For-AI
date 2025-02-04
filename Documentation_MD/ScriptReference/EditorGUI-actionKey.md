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

#  [EditorGUI](EditorGUI.html).actionKey

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

public static bool actionKey;

### Description

Is the platform-dependent "action" modifier key held down? (Read Only)

The key is Command on macOS, Control on Windows.  
  
![](../StaticFiles/ScriptRefImages/EditorGUIActionKey.png)  
_Action Key usage, key not pressed/key pressed._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Shows a password field with some "hidden" text.
    // When the user presses the action key the password field becomes a text field.  
      
    class EditorGUIActionKey : [EditorWindow](EditorWindow.html)
    {
        string text = "This is some text";  
      
        [[MenuItem](MenuItem.html)("Examples/Show Hide password")]
        static void Init()
        {
            var window = GetWindow<EditorGUIActionKey>();
            window.position = new [Rect](Rect.html)(0, 0, 250, 60);
            window.Show();
        }  
      
        void OnGUI()
        {
            // Show the contents
            if ([EditorGUI.actionKey](EditorGUI-actionKey.html))
            {
                text = [EditorGUI.TextField](EditorGUI.TextField.html)(new [Rect](Rect.html)(0, 5, 245, 20), "Shown  Text:", text);
            }
            else
            {
                // show the pasword field
                text = [EditorGUI.PasswordField](EditorGUI.PasswordField.html)(new [Rect](Rect.html)(0, 5, 245, 20), "Hidden Text:", text);
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 30, 250, 20), "Close"))
                this.Close();
        }  
      
        void OnInspectorUpdate()
        {
            Repaint();
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

