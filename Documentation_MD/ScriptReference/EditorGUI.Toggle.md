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

#  [EditorGUI](EditorGUI.html).Toggle

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

public static bool Toggle([Rect](Rect.html) position, bool value);

## Declaration

public static bool Toggle([Rect](Rect.html) position, string label, bool
value);

## Declaration

public static bool Toggle([Rect](Rect.html) position, bool value,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static bool Toggle([Rect](Rect.html) position, string label, bool
value, [GUIStyle](GUIStyle.html) style);

## Declaration

public static bool Toggle([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, bool value);

## Declaration

public static bool Toggle([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, bool value, [GUIStyle](GUIStyle.html)
style);

### Parameters

position | Rectangle on the screen to use for the toggle.  
---|---  
label | Optional label in front of the toggle.  
value | The shown state of the toggle.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**bool** The selected state of the toggle.

### Description

Makes a toggle.

![](../StaticFiles/ScriptRefImages/EditorGUIToggle.png)  
_Toggle control in an Editor Window._

    
    
    // Use a toggle button to show/hide a button that can close the window.
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class EditorGUIToggle : [EditorWindow](EditorWindow.html)
    {
        bool showClose =  true;  
      
        [[MenuItem](MenuItem.html)("Examples/[EditorGUI](EditorGUI.html) [Toggle](UIElements.Toggle.html) usage")]
        static void Init()
        {
            EditorGUIToggle window = (EditorGUIToggle)GetWindow(typeof(EditorGUIToggle), true, "My Empty Window");
            window.Show();
        }  
      
        void OnGUI()
        {
            showClose = [EditorGUI.Toggle](EditorGUI.Toggle.html)(new [Rect](Rect.html)(0, 5, position.width, 20),
                "Show Close [Button](UIElements.Button.html)",
                showClose);
            if (showClose)
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 25, position.width, 100), "Close Window!"))
                    this.Close();
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

