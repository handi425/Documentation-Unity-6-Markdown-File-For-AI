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

#  [EditorGUILayout](EditorGUILayout.html).ToggleLeft

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

public static bool ToggleLeft(string label, bool value, params
GUILayoutOption[] options);

## Declaration

public static bool ToggleLeft([GUIContent](GUIContent.html) label, bool value,
params GUILayoutOption[] options);

## Declaration

public static bool ToggleLeft(string label, bool value,
[GUIStyle](GUIStyle.html) labelStyle, params GUILayoutOption[] options);

## Declaration

public static bool ToggleLeft([GUIContent](GUIContent.html) label, bool value,
[GUIStyle](GUIStyle.html) labelStyle, params GUILayoutOption[] options);

### Parameters

label | Label to display next to the toggle.  
---|---  
value | The value to edit.  
labelStyle | Optional [GUIStyle](GUIStyle.html) to use for the label.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Description

Make a toggle field where the toggle is to the left and the label immediately
to the right of it.

[EditorGUILayout.ToggleLeft](EditorGUILayout.ToggleLeft.html) is similar to
[GUILayout.Toggle](GUILayout.Toggle.html) but respects the
[EditorGUI.showMixedValue](EditorGUI-showMixedValue.html) property and handles
keyboard focus consistent with other Editor controls.
[EditorGUILayout.ToggleLeft](EditorGUILayout.ToggleLeft.html) has the label
close and to the left of the toggle. (The
[EditorGUILayout.Toggle](EditorGUILayout.Toggle.html) has the opposite with
the label at a distance from the toggle and to the right.)

![](../StaticFiles/ScriptRefImages/EditorGUILayoutToggleLeft.png)  
_Show a button if the toggle control is selected._

    
    
    // Creates a new menu in the [Editor](Editor.html) called "Examples" with a new menu item called "ToggleLeft example"  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [EditorWindow](EditorWindow.html)
    {
        bool showBtn = true;  
      
        [[MenuItem](MenuItem.html)("Examples/ToggleLeft example")]
        static void Init()
        {
            Example window = (Example)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(Example), true, "ToggleLeft example");
            window.Show();
        }  
      
        void OnGUI()
        {
            showBtn = [EditorGUILayout.ToggleLeft](EditorGUILayout.ToggleLeft.html)("Show [Button](UIElements.Button.html)", showBtn);
            if (showBtn)
            {
                if ([GUILayout.Button](GUILayout.Button.html)("Close"))
                {
                    this.Close();
                }
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

