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

#  [EditorGUI](EditorGUI.html).PrefixLabel

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

public static [Rect](Rect.html) PrefixLabel([Rect](Rect.html) totalPosition,
[GUIContent](GUIContent.html) label);

## Declaration

public static [Rect](Rect.html) PrefixLabel([Rect](Rect.html) totalPosition,
[GUIContent](GUIContent.html) label, [GUIStyle](GUIStyle.html) style);

## Declaration

public static [Rect](Rect.html) PrefixLabel([Rect](Rect.html) totalPosition,
int id, [GUIContent](GUIContent.html) label);

## Declaration

public static [Rect](Rect.html) PrefixLabel([Rect](Rect.html) totalPosition,
int id, [GUIContent](GUIContent.html) label, [GUIStyle](GUIStyle.html) style);

### Parameters

totalPosition | Rectangle on the screen to use in total for both the label and the control.  
---|---  
id | The unique ID of the control. If none specified, the ID of the following control is used.  
label | Label to show in front of the control.  
style | Style to use for the label.  
  
### Returns

**Rect** Rectangle on the screen to use just for the control itself.

### Description

Makes a label in front of some control.

![](../StaticFiles/ScriptRefImages/EditorGUIPrefixLabel.png)  
_Prefix Label in an Editor Window._  
  
Note that most editor controls already have built-in optional labels that can
be specified as one of the parameters. PrefixLabel can be used when there is
no such built-in label available, or when you're creating your own editor
control from scratch.  
  
PrefixLabel takes a rect that's the rect for the entire control, including the
label, and returns a rect that's for just the control itself, without the
label.  
  
PrefixLabel also ensures that when the label is clicked, the linked control
will get keyboard focus (if the control supports keyboard focus). The ID of
the linked control can optionally be specified, or if no ID is given, the
label is automatically linked to the following control coming after it.

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

