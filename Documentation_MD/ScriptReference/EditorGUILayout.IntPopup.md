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

#  [EditorGUILayout](EditorGUILayout.html).IntPopup

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

public static int IntPopup(int selectedValue, string[] displayedOptions, int[]
optionValues, params GUILayoutOption[] options);

## Declaration

public static int IntPopup(int selectedValue, string[] displayedOptions, int[]
optionValues, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[]
options);

## Declaration

public static int IntPopup(int selectedValue, GUIContent[] displayedOptions,
int[] optionValues, params GUILayoutOption[] options);

## Declaration

public static int IntPopup(int selectedValue, GUIContent[] displayedOptions,
int[] optionValues, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[]
options);

## Declaration

public static int IntPopup(string label, int selectedValue, string[]
displayedOptions, int[] optionValues, params GUILayoutOption[] options);

## Declaration

public static int IntPopup(string label, int selectedValue, string[]
displayedOptions, int[] optionValues, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

## Declaration

public static int IntPopup([GUIContent](GUIContent.html) label, int
selectedValue, GUIContent[] displayedOptions, int[] optionValues, params
GUILayoutOption[] options);

## Declaration

public static int IntPopup([GUIContent](GUIContent.html) label, int
selectedValue, GUIContent[] displayedOptions, int[] optionValues,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

label | Optional label in front of the field.  
---|---  
selectedValue | The value of the option the field shows.  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option.  
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

**int** The value of the option that has been selected by the user.

### Description

Make an integer popup selection field.

Takes the currently selected integer as a parameter and returns the integer
selected by the user.  
  
![](../StaticFiles/ScriptRefImages/EditorGUILayoutIntPopup.png)  
_Rescales the current selected GameObject._

    
    
    // Simple [Editor](Editor.html) Script that lets you rescale the current selected [GameObject](GameObject.html).
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class IntPopupExample : [EditorWindow](EditorWindow.html)
    {
        int   selectedSize = 1;
        string[] names = new string[] {"Normal", "Double", "Quadruple"};
        int[] sizes = {1, 2, 4};  
      
        [[MenuItem](MenuItem.html)("Examples/Int Popup usage")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(IntPopupExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            selectedSize = [EditorGUILayout.IntPopup](EditorGUILayout.IntPopup.html)("Resize [Scale](UIElements.Scale.html): ", selectedSize, names, sizes);
            if ([GUILayout.Button](GUILayout.Button.html)("[Scale](UIElements.Scale.html)"))
                ReScale();
        }  
      
        void ReScale()
        {
            if ([Selection.activeTransform](Selection-activeTransform.html))
                Selection.activeTransform.localScale =
                    new [Vector3](Vector3.html)(selectedSize, selectedSize, selectedSize);
            else
                [Debug.LogError](Debug.LogError.html)("No Object selected, please select an object to scale.");
        }
    }
    

* * *

**Obsolete** This function is obsolete and the style is not used.

## Declaration

public static void IntPopup([SerializedProperty](SerializedProperty.html)
property, GUIContent[] displayedOptions, int[] optionValues,
[GUIContent](GUIContent.html) label, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

## Declaration

public static void IntPopup([SerializedProperty](SerializedProperty.html)
property, GUIContent[] displayedOptions, int[] optionValues, params
GUILayoutOption[] options);

## Declaration

public static void IntPopup([SerializedProperty](SerializedProperty.html)
property, GUIContent[] displayedOptions, int[] optionValues,
[GUIContent](GUIContent.html) label, params GUILayoutOption[] options);

### Parameters

property | The value of the option the field shows.  
---|---  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option.  
label | Optional label in front of the field.  
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

Make an integer popup selection field.

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

