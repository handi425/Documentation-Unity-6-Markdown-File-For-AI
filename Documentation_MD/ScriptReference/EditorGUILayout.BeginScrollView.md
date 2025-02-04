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

#  [EditorGUILayout](EditorGUILayout.html).BeginScrollView

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

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, params GUILayoutOption[] options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, params
GUILayoutOption[] options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, [GUIStyle](GUIStyle.html) horizontalScrollbar,
[GUIStyle](GUIStyle.html) verticalScrollbar, params GUILayoutOption[]
options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[]
options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical,
[GUIStyle](GUIStyle.html) horizontalScrollbar, [GUIStyle](GUIStyle.html)
verticalScrollbar, [GUIStyle](GUIStyle.html) background, params
GUILayoutOption[] options);

### Parameters

scrollPosition | The position to use display.  
---|---  
style | Optional [GUIStyle](GUIStyle.html) to use for the background.  
background | Optional [GUIStyle](GUIStyle.html) to use for the background.  
alwaysShowHorizontal | Optional parameter to always show the horizontal scrollbar. If false or left out, it is only shown when the content inside the ScrollView is wider than the scrollview itself.  
alwaysShowVertical | Optional parameter to always show the vertical scrollbar. If false or left out, it is only shown when content inside the ScrollView is taller than the scrollview itself.  
horizontalScrollbar | Optional [GUIStyle](GUIStyle.html) to use for the horizontal scrollbar. If left out, the `horizontalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
verticalScrollbar | Optional [GUIStyle](GUIStyle.html) to use for the vertical scrollbar. If left out, the `verticalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
  
### Returns

**Vector2** The modified scrollPosition. Feed this back into the variable you
pass in, as shown in the example.

### Description

Begin an automatically laid out scrollview.

These work just like
[GUILayout.BeginScrollView](GUILayout.BeginScrollView.html) but feel more
application-like and should be used in the editor  
  
![](../StaticFiles/ScriptRefImages/BeginEndScrollView.png)  
_Label inside a scroll view._

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class BeginScrollViewExample : [EditorWindow](EditorWindow.html)
    {
        [Vector2](Vector2.html) scrollPos;
        string t = "This is a string inside a Scroll view!";  
      
        [[MenuItem](MenuItem.html)("Examples/Modify internal [Quaternion](Quaternion.html)")]
        static void Init()
        {
            BeginScrollViewExample window = (BeginScrollViewExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(BeginScrollViewExample), true, "My Empty Window");
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

