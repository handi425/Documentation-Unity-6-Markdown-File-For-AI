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

#  [EditorGUI](EditorGUI.html).HandlePrefixLabel

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

public static void HandlePrefixLabel([Rect](Rect.html) totalPosition,
[Rect](Rect.html) labelPosition, [GUIContent](GUIContent.html) label, int id =
0, [GUIStyle](GUIStyle.html) style = EditorStyles.label);

### Parameters

totalPosition | Rectangle on the screen to use in total for both the label and the control.  
---|---  
labelPosition | Rectangle on the screen to use for the label.  
label | Label to show for the control.  
id | The unique ID of the control. If none specified, the ID of the following control is used.  
style | Optional [GUIStyle](GUIStyle.html) to use for the label.  
  
### Description

Makes a label for some control.

HandlePrefixLabel is like PrefixLabel but allows custom control over the label
position by supplying its [Rect](Rect.html) explicitly. PrefixLabel or
HandlePrefixLabel should be used when creating a control with a connected
label. It ensures that when the label is clicked, the control will get
keyboard focus. For this reason it is important that the same ID is supplied
to PrefixLabel or HandlePrefixLabel as to the control itself. It is also
possible to not supply a Control ID, in which case the one from the
immediately following control is automatically used.

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

