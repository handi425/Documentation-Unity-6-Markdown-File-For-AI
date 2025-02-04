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

#  [EditorGUI](EditorGUI.html).FloatField

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

public static float FloatField([Rect](Rect.html) position, float value,
[GUIStyle](GUIStyle.html) style = EditorStyles.numberField);

## Declaration

public static float FloatField([Rect](Rect.html) position, string label, float
value, [GUIStyle](GUIStyle.html) style = EditorStyles.numberField);

## Declaration

public static float FloatField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, float value, [GUIStyle](GUIStyle.html)
style = EditorStyles.numberField);

### Parameters

position | Rectangle on the screen to use for the float field.  
---|---  
label | Optional label to display in front of the float field.  
value | The value to edit.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**float** The value entered by the user.

### Description

Makes a text field for entering floats.

![](../StaticFiles/ScriptRefImages/EditorGUIFloatField.png)  
_Float Field in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorGUIFloatField : [EditorWindow](EditorWindow.html)
    {
        float sizeMultiplier = 1;  
      
        [[MenuItem](MenuItem.html)("Examples/[Scale](UIElements.Scale.html) selected Object")]
        static void Init()
        {
            var window = GetWindow<EditorGUIFloatField>();
            window.position = new [Rect](Rect.html)(0, 0, 210, 30);
            window.Show();
        }  
      
        void OnGUI()
        {
            sizeMultiplier = [EditorGUI.FloatField](EditorGUI.FloatField.html)(new [Rect](Rect.html)(3, 3, 150, 20),
                "Increase scale by:",
                sizeMultiplier);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(160, 3, 45, 20), "[Scale](UIElements.Scale.html)!"))
            {
                Selection.activeTransform.localScale = Selection.activeTransform.localScale * sizeMultiplier;
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

