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

#  [EditorGUI](EditorGUI.html).Slider

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

public static float Slider([Rect](Rect.html) position, float value, float
leftValue, float rightValue);

## Declaration

public static float Slider([Rect](Rect.html) position, string label, float
value, float leftValue, float rightValue);

## Declaration

public static float Slider([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, float value, float leftValue, float
rightValue);

### Parameters

position | Rectangle on the screen to use for the slider.  
---|---  
label | Optional label in front of the slider.  
value | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
  
### Returns

**float** The value that has been set by the user.

### Description

Makes a slider the user can drag to change a value between a min and a max.

![](../StaticFiles/ScriptRefImages/EditorGUISlider.png)  
_Slider in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // [Editor](Editor.html) script that lets you scale the selected [GameObject](GameObject.html) between 1 and 100  
      
    class EditorGUISlider : [EditorWindow](EditorWindow.html)
    {
        float scale = 1.0f;  
      
        [[MenuItem](MenuItem.html)("Examples/[EditorGUI](EditorGUI.html) [Slider](UIElements.Slider.html) usage")]
        static void Init()
        {
            var window = GetWindow<EditorGUISlider>();
            window.position = new [Rect](Rect.html)(0, 0, 150, 30);
            window.Show();
        }  
      
        void OnGUI()
        {
            scale = [EditorGUI.Slider](EditorGUI.Slider.html)(new [Rect](Rect.html)(5, 5, 150, 20), scale, 1, 100);
        }  
      
        void OnInspectorUpdate()
        {
            if ([Selection.activeTransform](Selection-activeTransform.html))
            {
                Selection.activeTransform.localScale = new [Vector3](Vector3.html)(scale, scale, scale);
            }
        }
    }
    

* * *

## Declaration

public static void Slider([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property, float leftValue, float
rightValue);

## Declaration

public static void Slider([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property, float leftValue, float
rightValue, string label);

## Declaration

public static void Slider([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property, float leftValue, float
rightValue, [GUIContent](GUIContent.html) label);

### Parameters

position | Rectangle on the screen to use for the slider.  
---|---  
label | Optional label in front of the slider.  
property | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
  
### Description

Makes a slider the user can drag to change a value between a min and a max.

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

