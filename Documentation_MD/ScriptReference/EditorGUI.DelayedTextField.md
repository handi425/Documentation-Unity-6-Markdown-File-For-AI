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

#  [EditorGUI](EditorGUI.html).DelayedTextField

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

public static string DelayedTextField([Rect](Rect.html) position, string text,
[GUIStyle](GUIStyle.html) style = EditorStyles.textField);

## Declaration

public static string DelayedTextField([Rect](Rect.html) position, string
label, string text, [GUIStyle](GUIStyle.html) style = EditorStyles.textField);

## Declaration

public static string DelayedTextField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, string text, [GUIStyle](GUIStyle.html)
style = EditorStyles.textField);

### Parameters

position | Rectangle on the screen to use for the text field.  
---|---  
label | Optional label to display in front of the int field.  
text | The value to edit.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**string** The value entered by the user. Note that the return value will not
change until the user has pressed enter or focus is moved away from the text
field.

### Description

Makes a delayed text field.

Similar to [EditorGUI.TextField](EditorGUI.TextField.html) but will not return
the new value until the user has pressed enter or focus is moved away from the
text field.

* * *

## Declaration

public static void DelayedTextField([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property,
[GUIContent](GUIContent.html) label = null);

### Parameters

position | Rectangle on the screen to use for the text field.  
---|---  
property | The text property to edit.  
label | Optional label to display in front of the int field. Pass [GUIContent.none](GUIContent-none.html) to hide label.  
  
### Description

Makes a delayed text field.

Similar to [EditorGUI.TextField](EditorGUI.TextField.html) but will not return
the new value until the user has pressed enter or focus is moved away from the
text field.

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

