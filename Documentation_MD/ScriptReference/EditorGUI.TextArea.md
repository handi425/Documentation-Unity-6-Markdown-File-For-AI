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

#  [EditorGUI](EditorGUI.html).TextArea

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

public static string TextArea([Rect](Rect.html) position, string text,
[GUIStyle](GUIStyle.html) style = EditorStyles.textField);

### Parameters

position | Rectangle on the screen to use for the text field.  
---|---  
text | The text to edit.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**string** The text entered by the user.

### Description

Makes a text area.

This works just like [GUI.TextArea](GUI.TextArea.html), but correctly responds
to select all, copy, paste etc. in the editor.  
  
![](../StaticFiles/ScriptRefImages/EditorGUITextArea.png)  
_Text Area in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Create a window where you can have notes
    // This doesnt preserve the notes between sessions.
    //
    // check [EditorPrefs](EditorPrefs.html) Get/SetString to save the notes.  
      
    class EditorGUITextArea : [EditorWindow](EditorWindow.html)
    {
        string note = "Notes:\n->";  
      
        [[MenuItem](MenuItem.html)("Examples/Notes")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow<EditorGUITextArea>();
            window.position = new [Rect](Rect.html)(0, 0, 350, 70);
            window.Show();
        }  
      
        void OnGUI()
        {
            note = [EditorGUI.TextArea](EditorGUI.TextArea.html)(new [Rect](Rect.html)(3, 3, position.width - 6, position.height - 35), note);
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, position.height - 30, position.width, 25), "Close"))
            {
                this.Close();
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

