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

#  [EditorGUILayout](EditorGUILayout.html).Toggle

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

public static bool Toggle(bool value, params GUILayoutOption[] options);

## Declaration

public static bool Toggle(string label, bool value, params GUILayoutOption[]
options);

## Declaration

public static bool Toggle([GUIContent](GUIContent.html) label, bool value,
params GUILayoutOption[] options);

## Declaration

public static bool Toggle(bool value, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

## Declaration

public static bool Toggle(string label, bool value, [GUIStyle](GUIStyle.html)
style, params GUILayoutOption[] options);

## Declaration

public static bool Toggle([GUIContent](GUIContent.html) label, bool value,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

label | Optional label in front of the toggle.  
---|---  
value | The shown state of the toggle.  
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

**bool** The selected state of the toggle.

### Description

Make a toggle.

![](../StaticFiles/ScriptRefImages/EditorGUILayoutToggle.png)  
_Show a button if the toggle control is selected._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorGUILayoutToggle : UnityEditor.EditorWindow
    {
        bool showBtn = true;  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUILayout](GUILayout.html) [Toggle](UIElements.Toggle.html) Usage")]
        static void Init()
        {
            EditorGUILayoutToggle window = (EditorGUILayoutToggle)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(EditorGUILayoutToggle), true, "My Empty Window");
            window.Show();
        }  
      
        void OnGUI()
        {
            showBtn = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Show [Button](UIElements.Button.html)", showBtn);
            if (showBtn)
                if ([GUILayout.Button](GUILayout.Button.html)("Close"))
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

