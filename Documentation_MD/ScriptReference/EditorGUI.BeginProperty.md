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

#  [EditorGUI](EditorGUI.html).BeginProperty

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

public static [GUIContent](GUIContent.html) BeginProperty([Rect](Rect.html)
totalPosition, [GUIContent](GUIContent.html) label,
[SerializedProperty](SerializedProperty.html) property);

### Parameters

totalPosition | Rectangle on the screen to use for the control, including label if applicable.  
---|---  
label | Optional label in front of the slider. Use null to use the name from the SerializedProperty. Use GUIContent.none to not display a label.  
property | The SerializedProperty to use for the control.  
  
### Returns

**GUIContent** The actual label to use for the control.

### Description

Create a Property wrapper, useful for making regular GUI controls work with
[SerializedProperty](SerializedProperty.html).

Most [EditorGUI](EditorGUI.html) and [EditorGUILayout](EditorGUILayout.html)
GUI controls already have overloads that work with SerializedProperty.
However, for GUI controls that don't handle SerializedProperty you can wrap
them inside BeginProperty and EndProperty as shown in the example below. You
can use this for your own custom GUI controls too.  
  
BeginProperty and EndProperty automatically handle default labels, bold font
for Prefab overrides, revert to Prefab right click menu, and setting
[showMixedValue](EditorGUI-showMixedValue.html) to true if the values of the
property are different when multi-object editing.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // A slider function that takes a [SerializedProperty](SerializedProperty.html)
        void [Slider](UIElements.Slider.html)([Rect](Rect.html) position, [SerializedProperty](SerializedProperty.html) property, float leftValue, float rightValue, [GUIContent](GUIContent.html) label)
        {
            label = [EditorGUI.BeginProperty](EditorGUI.BeginProperty.html)(position, label, property);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            var newValue = [EditorGUI.Slider](EditorGUI.Slider.html)(position, label, property.floatValue, leftValue, rightValue);
            // Only assign the value back if it was actually changed by the user.
            // Otherwise a single value will be assigned to all objects when multi-object editing,
            // even when the user didn't touch the control.
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                property.floatValue = newValue;
            }
            [EditorGUI.EndProperty](EditorGUI.EndProperty.html)();
        }
    }
    

Additional resources: [EndProperty](EditorGUI.EndProperty.html).

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

