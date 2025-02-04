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

#  [EditorGUI](EditorGUI.html).MultiPropertyField

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

public static void MultiPropertyField([Rect](Rect.html) position, GUIContent[]
subLabels, [SerializedProperty](SerializedProperty.html) valuesIterator,
[GUIContent](GUIContent.html) label);

## Declaration

public static void MultiPropertyField([Rect](Rect.html) position, GUIContent[]
subLabels, [SerializedProperty](SerializedProperty.html) valuesIterator,
[GUIContent](GUIContent.html) label,
[EditorGUI.PropertyVisibility](EditorGUI.PropertyVisibility.html) visibility);

## Declaration

public static void MultiPropertyField([Rect](Rect.html) position, GUIContent[]
subLabels, [SerializedProperty](SerializedProperty.html) valuesIterator);

## Declaration

public static void MultiPropertyField([Rect](Rect.html) position, GUIContent[]
subLabels, [SerializedProperty](SerializedProperty.html) valuesIterator,
[EditorGUI.PropertyVisibility](EditorGUI.PropertyVisibility.html) visibility);

### Parameters

position | Rectangle on the screen to use for the multi-property field.  
---|---  
valuesIterator | The SerializedProperty of the first property to make a control for.  
label | Optional label to use. If not specified the label of the property itself is used. Use GUIContent.none to not display a label at all.  
subLabels | Array with small labels to show in front of each float field. There is room for one letter per field only.  
visibility | Each SerializedProperty during iteration must have this visibility to be drawn. Use [EditorGUI.PropertyVisibility.All](EditorGUI.PropertyVisibility.All.html) to draw all SerializedProperties, regardless of its actual visibility.  
  
### Description

Makes a multi-control with several property fields in the same line.

The array of labels determine how many properties are shown. No more than 4
properties should be used. The displayed SerializedProperties must be
consecutive. The one provided in the valuesIterator argument should be the
first of them.

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

