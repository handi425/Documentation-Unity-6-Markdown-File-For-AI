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

#  [EditorGUI](EditorGUI.html).IntPopup

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

public static int IntPopup([Rect](Rect.html) position, int selectedValue,
string[] displayedOptions, int[] optionValues, [GUIStyle](GUIStyle.html) style
= EditorStyles.popup);

## Declaration

public static int IntPopup([Rect](Rect.html) position, int selectedValue,
GUIContent[] displayedOptions, int[] optionValues, [GUIStyle](GUIStyle.html)
style = EditorStyles.popup);

## Declaration

public static int IntPopup([Rect](Rect.html) position, string label, int
selectedValue, string[] displayedOptions, int[] optionValues,
[GUIStyle](GUIStyle.html) style = EditorStyles.popup);

## Declaration

public static int IntPopup([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, int selectedValue, GUIContent[]
displayedOptions, int[] optionValues, [GUIStyle](GUIStyle.html) style =
EditorStyles.popup);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label in front of the field.  
selectedValue | The value of the option the field shows.  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option. If optionValues a direct mapping of selectedValue to displayedOptions is assumed.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**int** The value of the option that has been selected by the user.

### Description

Makes an integer popup selection field.

Takes the currently selected integer as a parameter and returns the integer
selected by the user.  
  
![](../StaticFiles/ScriptRefImages/EditorGUIIntPopup.png)  
_Int Popup in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Multiplies the scale of the selected transform.  
      
    class EditorGUIIntPopup : [EditorWindow](EditorWindow.html)
    {
        int selectedSize = 1;
        string[] names = { "Double", "Triple", "Quadruple" };
        int[] sizes = { 2, 3, 4 };  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUI](GUI.html) Int Popup usage")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow<EditorGUIIntPopup>();
            window.position = new [Rect](Rect.html)(0, 0, 180, 60);
            window.Show();
        }  
      
        void OnGUI()
        {
            selectedSize = [EditorGUI.IntPopup](EditorGUI.IntPopup.html)(
                new [Rect](Rect.html)(3, 3, position.width - 6, 20),
                "Size:",
                selectedSize,
                names,
                sizes);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 25, position.width, position.height - 27), "Modify"))
            {
                Rescale();
            }
        }  
      
        void Rescale()
        {
            if ([Selection.activeTransform](Selection-activeTransform.html))
            {
                Selection.activeTransform.localScale *= selectedSize;
            }
            else
            {
                [Debug.LogError](Debug.LogError.html)("No Object selected, please select an object to scale.");
            }
        }
    }
    

* * *

## Declaration

public static void IntPopup([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property, GUIContent[]
displayedOptions, int[] optionValues, [GUIContent](GUIContent.html) label =
null);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
property | The SerializedProperty to use for the control.  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option. If optionValues a direct mapping of selectedValue to displayedOptions is assumed.  
label | Optional label in front of the field.  
  
### Description

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

