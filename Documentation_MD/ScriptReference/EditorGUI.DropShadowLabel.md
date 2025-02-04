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

#  [EditorGUI](EditorGUI.html).DropShadowLabel

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

public static void DropShadowLabel([Rect](Rect.html) position, string text);

## Declaration

public static void DropShadowLabel([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content);

## Declaration

public static void DropShadowLabel([Rect](Rect.html) position, string text,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static void DropShadowLabel([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style);

### Parameters

position | Where to show the label.  
---|---  
content | Text to show @style style to use.  
  
### Description

Draws a label with a drop shadow.

Not superfast, so use with caution.  
  
![](../StaticFiles/ScriptRefImages/EditorGUIDropShadowLabel.png)  
_Shadow Label in and editor window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorGUIDropShadowLabel : [EditorWindow](EditorWindow.html)
    {
        // Write some text using a Shadow [Label](UIElements.Label.html).
        string text = "This is some text with a Shadow [Label](UIElements.Label.html)";  
      
        [[MenuItem](MenuItem.html)("Examples/Shadow [Label](UIElements.Label.html)")]
        static void Init()
        {
            var window = GetWindow<EditorGUIDropShadowLabel>();
            window.position = new [Rect](Rect.html)(0, 0, 250, 60);
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUI.DropShadowLabel](EditorGUI.DropShadowLabel.html)(new [Rect](Rect.html)(0, 5, 245, 20), text);  
      
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

