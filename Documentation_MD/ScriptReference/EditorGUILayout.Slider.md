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

#  [EditorGUILayout](EditorGUILayout.html).Slider

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

public static float Slider(float value, float leftValue, float rightValue,
params GUILayoutOption[] options);

## Declaration

public static float Slider(string label, float value, float leftValue, float
rightValue, params GUILayoutOption[] options);

## Declaration

public static float Slider([GUIContent](GUIContent.html) label, float value,
float leftValue, float rightValue, params GUILayoutOption[] options);

### Parameters

label | Optional label in front of the slider.  
---|---  
value | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
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

**float** The value that has been set by the user.

### Description

Make a slider the user can drag to change a value between a min and a max.

![](../StaticFiles/ScriptRefImages/EditorGUILayoutSlider.png)  
_Scale the selected object between a range._

    
    
    // [Editor](Editor.html) script that lets you scale the selected [GameObject](GameObject.html) between 1 and 100  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class EditorGUILayoutSlider : [EditorWindow](EditorWindow.html)
    {
        static float scale = 0.0f;  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUILayout](GUILayout.html) [Slider](UIElements.Slider.html) usage")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(EditorGUILayoutSlider));
            window.Show();
        }  
      
        void OnGUI()
        {
            scale = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)(scale, 1, 100);
        }  
      
        void OnInspectorUpdate()
        {
            if ([Selection.activeTransform](Selection-activeTransform.html))
                Selection.activeTransform.localScale = new [Vector3](Vector3.html)(scale, scale, scale);
        }
    }
    

* * *

## Declaration

public static void Slider([SerializedProperty](SerializedProperty.html)
property, float leftValue, float rightValue, params GUILayoutOption[]
options);

## Declaration

public static void Slider([SerializedProperty](SerializedProperty.html)
property, float leftValue, float rightValue, string label, params
GUILayoutOption[] options);

## Declaration

public static void Slider([SerializedProperty](SerializedProperty.html)
property, float leftValue, float rightValue, [GUIContent](GUIContent.html)
label, params GUILayoutOption[] options);

### Parameters

label | Optional label in front of the slider.  
---|---  
property | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
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

Make a slider the user can drag to change a value between a min and a max.

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

