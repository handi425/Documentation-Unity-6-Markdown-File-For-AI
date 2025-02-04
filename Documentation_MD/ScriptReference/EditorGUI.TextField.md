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

#  [EditorGUI](EditorGUI.html).TextField

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

public static string TextField([Rect](Rect.html) position, string text,
[GUIStyle](GUIStyle.html) style = EditorStyles.textField);

## Declaration

public static string TextField([Rect](Rect.html) position, string label,
string text, [GUIStyle](GUIStyle.html) style = EditorStyles.textField);

## Declaration

public static string TextField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, string text, [GUIStyle](GUIStyle.html)
style = EditorStyles.textField);

### Parameters

position | Rectangle on the screen to use for the text field.  
---|---  
label | Optional label to display in front of the text field.  
text | The text to edit.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**string** The text entered by the user.

### Description

Makes a text field.

This works just like [GUI.TextField](GUI.TextField.html), but correctly
responds to select all, copy, paste etc. in the editor, and it can have an
optional label in front.  
  
![](../StaticFiles/ScriptRefImages/EditorGUITextField.png)  
_Text field in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Changes the name of the selected Objects to the one typed in the text field  
      
    class EditorGUITextField : [EditorWindow](EditorWindow.html)
    {
        string objNames = "";  
      
        [[MenuItem](MenuItem.html)("Examples/Bulk Name change")]
        static void Init()
        {
            var window = GetWindow<EditorGUITextField>();
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUI.DropShadowLabel](EditorGUI.DropShadowLabel.html)(new [Rect](Rect.html)(0, 0, position.width, 20),
                "Select the objects to rename.");  
      
            objNames = [EditorGUI.TextField](EditorGUI.TextField.html)(new [Rect](Rect.html)(10, 25, position.width - 20, 20),
                "New Names:",
                objNames);  
      
            if ([Selection.activeTransform](Selection-activeTransform.html))
            {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 50, position.width, 30), "Bulk rename!"))
                {
                    foreach ([Transform](Transform.html) t in [Selection.transforms](Selection-transforms.html))
                    {
                        t.name = objNames;
                    }
                }
            }
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

