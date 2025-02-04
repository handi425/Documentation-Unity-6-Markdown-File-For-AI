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

#  [EditorGUILayout](EditorGUILayout.html).TextArea

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

public static string TextArea(string text, params GUILayoutOption[] options);

## Declaration

public static string TextArea(string text, [GUIStyle](GUIStyle.html) style,
params GUILayoutOption[] options);

### Parameters

text | The text to edit.  
---|---  
style | Optional [GUIStyle](GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**string** The text entered by the user.

### Description

Make a text area.

This works just like @@[GUILayout.TextArea](GUILayout.TextArea.html)@@ with
proper responsiveness to actions like **Select all** , **Copy** , **Paste** in
the Editor.  
For Undo support, see [Undo.RecordObject](Undo.RecordObject.html).  
To make the text wrap, set **EditorStyles.textField.wordWrap**.  
  
![](../StaticFiles/ScriptRefImages/EditorGUILayoutTextArea.png)  
_Quick script editor._

    
    
    // Simple script that lets you visualize your scripts in an editor window
    // This can be expanded to save your scripts also in the editor window.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class TextAreaExample : [EditorWindow](EditorWindow.html)
    {
        string text = "Nothing Opened...";
        [TextAsset](TextAsset.html) txtAsset;
        [Vector2](Vector2.html) scroll;  
      
        [[MenuItem](MenuItem.html)("Examples/TextArea usage")]
        static void Init()
        {
            TextAreaExample window = (TextAreaExample)GetWindow(typeof(TextAreaExample), true, "[EditorGUILayout.TextArea](EditorGUILayout.TextArea.html)");
            window.Show();
        }  
      
        Object source;  
      
        void OnGUI()
        {
            source = [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(source, typeof(Object), true);
            [TextAsset](TextAsset.html) newTxtAsset = ([TextAsset](TextAsset.html))source;  
      
            if (newTxtAsset != txtAsset)
                ReadTextAsset(newTxtAsset);  
      
            scroll = [EditorGUILayout.BeginScrollView](EditorGUILayout.BeginScrollView.html)(scroll, [GUILayout.Height](GUILayout.Height.html)(position.height - 30));
            text = [EditorGUILayout.TextArea](EditorGUILayout.TextArea.html)(text);
            [EditorGUILayout.EndScrollView](EditorGUILayout.EndScrollView.html)();
        }  
      
        void ReadTextAsset([TextAsset](TextAsset.html) txt)
        {
            text = txt.text;
            txtAsset = txt;
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

