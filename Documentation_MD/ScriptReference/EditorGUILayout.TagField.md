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

#  [EditorGUILayout](EditorGUILayout.html).TagField

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

public static string TagField(string tag, params GUILayoutOption[] options);

## Declaration

public static string TagField(string tag, [GUIStyle](GUIStyle.html) style,
params GUILayoutOption[] options);

## Declaration

public static string TagField(string label, string tag, params
GUILayoutOption[] options);

## Declaration

public static string TagField(string label, string tag,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static string TagField([GUIContent](GUIContent.html) label, string tag,
params GUILayoutOption[] options);

## Declaration

public static string TagField([GUIContent](GUIContent.html) label, string tag,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

label | Optional label in front of the field.  
---|---  
tag | The tag the field shows.  
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

**string** The tag selected by the user.

### Description

Make a tag selection field.

![](../StaticFiles/ScriptRefImages/EditorGUILayoutTagField.png)  
_Assign tags on the selected GameObjects._

    
    
    // Simple editor script that lets you set a tag for the selected GameObjects.
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class EditorGUILayoutTagField : [EditorWindow](EditorWindow.html)
    {
        static string tagStr = "";  
      
        [[MenuItem](MenuItem.html)("Examples/Set Tags For [Selection](Selection.html)")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(EditorGUILayoutTagField));
            window.Show();
        }  
      
        void OnGUI()
        {
            tagStr = [EditorGUILayout.TagField](EditorGUILayout.TagField.html)("Tag for Objects:", tagStr);
            if ([GUILayout.Button](GUILayout.Button.html)("Set Tag!"))
            {
                SetTags();
            }
        }  
      
        static void SetTags()
        {
            foreach ([GameObject](GameObject.html) go in [Selection.gameObjects](Selection-gameObjects.html))
            {
                go.tag = tagStr;
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

