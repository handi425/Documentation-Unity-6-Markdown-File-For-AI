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

#  [EditorGUILayout](EditorGUILayout.html).FloatField

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

public static float FloatField(float value, params GUILayoutOption[] options);

## Declaration

public static float FloatField(float value, [GUIStyle](GUIStyle.html) style,
params GUILayoutOption[] options);

## Declaration

public static float FloatField(string label, float value, params
GUILayoutOption[] options);

## Declaration

public static float FloatField(string label, float value,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static float FloatField([GUIContent](GUIContent.html) label, float
value, params GUILayoutOption[] options);

## Declaration

public static float FloatField([GUIContent](GUIContent.html) label, float
value, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

label | Optional label to display in front of the float field.  
---|---  
value | The value to edit.  
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

**float** The value entered by the user.

### Description

Make a text field for entering float values.

![](../StaticFiles/ScriptRefImages/EditorGUILayoutFloatField.png)  
_Multiply the scale of the selected GameObject._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // [Editor](Editor.html) Script that multiplies the scale of the current selected [GameObject](GameObject.html)  
      
    public class FloatFieldExample : [EditorWindow](EditorWindow.html)
    {
        float sizeMultiplier = 1.0f;  
      
        [[MenuItem](MenuItem.html)("Examples/[Scale](UIElements.Scale.html) selected Object")]
        static void Init()
        {
            var window = (FloatFieldExample)GetWindow(typeof(FloatFieldExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            sizeMultiplier = [EditorGUILayout.FloatField](EditorGUILayout.FloatField.html)("Increase scale by:", sizeMultiplier);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("[Scale](UIElements.Scale.html)"))
            {
                if (![Selection.activeGameObject](Selection-activeGameObject.html))
                {
                    [Debug.Log](Debug.Log.html)("Select a [GameObject](GameObject.html) first");
                    return;
                }  
      
                Selection.activeTransform.localScale =
                    Selection.activeTransform.localScale * sizeMultiplier;
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

