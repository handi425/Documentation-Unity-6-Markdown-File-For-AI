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

#  [EditorGUILayout](EditorGUILayout.html).EndScrollView

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

public static void EndScrollView();

### Description

Ends a scrollview started with a call to BeginScrollView.

![](../StaticFiles/ScriptRefImages/BeginEndScrollView.png)  
_Label inside a scroll view._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Simple [Editor](Editor.html) Window that creates a scroll view with a [Label](UIElements.Label.html) inside  
      
    public class CreateEndScrollViewCS : [EditorWindow](EditorWindow.html)
    {
        [Vector2](Vector2.html) scrollPos;
        string t = "This is a string inside a Scroll view!";  
      
        [[MenuItem](MenuItem.html)("Examples/Write text on [ScrollView](UIElements.ScrollView.html)")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(CreateEndScrollViewCS));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            scrollPos =
                [EditorGUILayout.BeginScrollView](EditorGUILayout.BeginScrollView.html)(scrollPos, [GUILayout.Width](GUILayout.Width.html)(100), [GUILayout.Height](GUILayout.Height.html)(100));
            [GUILayout.Label](GUILayout.Label.html)(t);
            [EditorGUILayout.EndScrollView](EditorGUILayout.EndScrollView.html)();
            if ([GUILayout.Button](GUILayout.Button.html)("Add More Text", [GUILayout.Width](GUILayout.Width.html)(100), [GUILayout.Height](GUILayout.Height.html)(100)))
                t += " \nAnd this is more text!";
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
            if ([GUILayout.Button](GUILayout.Button.html)("Clear"))
                t = "";
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

