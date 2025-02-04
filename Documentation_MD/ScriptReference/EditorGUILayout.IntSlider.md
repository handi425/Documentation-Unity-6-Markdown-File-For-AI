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

#  [EditorGUILayout](EditorGUILayout.html).IntSlider

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

public static int IntSlider(int value, int leftValue, int rightValue, params
GUILayoutOption[] options);

## Declaration

public static int IntSlider(string label, int value, int leftValue, int
rightValue, params GUILayoutOption[] options);

## Declaration

public static int IntSlider([GUIContent](GUIContent.html) label, int value,
int leftValue, int rightValue, params GUILayoutOption[] options);

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

**int** The value that has been set by the user.

### Description

Make a slider the user can drag to change an integer value between a min and a
max.

![](../StaticFiles/ScriptRefImages/EditorGUILayoutIntSlider.png)  
_Create a grid of cloned Objects._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // Simple editor script that lets you clone your object in a grid  
      
    public class IntSliderExample : [EditorWindow](EditorWindow.html)
    {
        int cloneTimesX  = 1;
        int cloneTimesY  = 1;
        int cloneTimesZ  = 1;
        int spacing   = 2;  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUILayout](GUILayout.html) IntSlider usage")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(IntSliderExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            cloneTimesX = [EditorGUILayout.IntSlider](EditorGUILayout.IntSlider.html)(cloneTimesX, 1, 10);
            cloneTimesY = [EditorGUILayout.IntSlider](EditorGUILayout.IntSlider.html)(cloneTimesY, 1, 10);
            cloneTimesZ = [EditorGUILayout.IntSlider](EditorGUILayout.IntSlider.html)(cloneTimesZ, 1, 10);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Duplicate object"))
                CloneSelected();
        }  
      
        void CloneSelected()
        {
            if (![Selection.activeGameObject](Selection-activeGameObject.html))
            {
                [Debug.LogError](Debug.LogError.html)("Select a [GameObject](GameObject.html) first");
                return;
            }  
      
            for (int i = 0; i < cloneTimesX; i++)
                for (int j = 0; j < cloneTimesY; j++)
                    for (int k = 0; k < cloneTimesZ; k++)
                        Instantiate([Selection.activeGameObject](Selection-activeGameObject.html), new [Vector3](Vector3.html)(i, j, k) * spacing, Selection.activeGameObject.transform.rotation);
        }
    }
    

* * *

## Declaration

public static void IntSlider([SerializedProperty](SerializedProperty.html)
property, int leftValue, int rightValue, params GUILayoutOption[] options);

## Declaration

public static void IntSlider([SerializedProperty](SerializedProperty.html)
property, int leftValue, int rightValue, string label, params
GUILayoutOption[] options);

## Declaration

public static void IntSlider([SerializedProperty](SerializedProperty.html)
property, int leftValue, int rightValue, [GUIContent](GUIContent.html) label,
params GUILayoutOption[] options);

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

Make a slider the user can drag to change an integer value between a min and a
max.

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

