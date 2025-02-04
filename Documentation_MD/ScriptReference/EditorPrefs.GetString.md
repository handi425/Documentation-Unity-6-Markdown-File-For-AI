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

#  [EditorPrefs](EditorPrefs.html).GetString

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

public static string GetString(string key);

## Declaration

public static string GetString(string key, string defaultValue = "");

### Description

Returns the value corresponding to `key` in the preference file if it exists.

If the value doesn't exist, it will return `defaultValue`. Note that
EditorPrefs does not support null strings, so if `defaultValue` is null, an
empty string is returned.  
  
![](../StaticFiles/ScriptRefImages/QuickNotes.png)  
_Quick notes that last between Unity Sessions._

    
    
    // Simple [Editor](Editor.html) Script that lets you create / save quick notes
    // Between Unity Sessions.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleClass : [EditorWindow](EditorWindow.html)
    {
        string note = "Notes:\n->\n->";  
      
        [[MenuItem](MenuItem.html)("Examples/QuickNotes")]
        static void Init()
        {
            ExampleClass window = (ExampleClass)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(ExampleClass));
            window.Show();
        }  
      
        void OnGUI()
        {
            note = [EditorGUILayout.TextArea](EditorGUILayout.TextArea.html)(note,
                [GUILayout.Width](GUILayout.Width.html)(position.width - 5),
                [GUILayout.Height](GUILayout.Height.html)(position.height - 30));
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            if ([GUILayout.Button](GUILayout.Button.html)("Reset"))
                note = "";
            if ([GUILayout.Button](GUILayout.Button.html)("Clear Story", [GUILayout.Width](GUILayout.Width.html)(72)))
            {
                note = "Notes:\n->\n->";
            }
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
        }  
      
        void OnFocus()
        {
            if ([EditorPrefs.HasKey](EditorPrefs.HasKey.html)("QuickNotes"))
                note = [EditorPrefs.GetString](EditorPrefs.GetString.html)("QuickNotes");
        }  
      
        void OnLostFocus()
        {
            [EditorPrefs.SetString](EditorPrefs.SetString.html)("QuickNotes", note);
        }  
      
        void OnDestroy()
        {
            [EditorPrefs.SetString](EditorPrefs.SetString.html)("QuickNotes", note);
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

