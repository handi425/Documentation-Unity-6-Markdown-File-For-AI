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

#  [EditorGUILayout](EditorGUILayout.html).GetControlRect

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

public static [Rect](Rect.html) GetControlRect(params GUILayoutOption[]
options);

## Declaration

public static [Rect](Rect.html) GetControlRect(bool hasLabel, params
GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) GetControlRect(bool hasLabel, float height,
params GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) GetControlRect(bool hasLabel, float height,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

hasLabel | Optional boolean to specify if the control has a label. Default is true.  
---|---  
height | The height in pixels of the control. Default is [EditorGUIUtility.singleLineHeight](EditorGUIUtility-singleLineHeight.html).  
style | Optional [GUIStyle](GUIStyle.html) to use for the control.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`. Additional resources: [GUILayout.Width](GUILayout.Width.html), [GUILayout.Height](GUILayout.Height.html), [GUILayout.MinWidth](GUILayout.MinWidth.html), [GUILayout.MaxWidth](GUILayout.MaxWidth.html), [GUILayout.MinHeight](GUILayout.MinHeight.html), [GUILayout.MaxHeight](GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Description

Get a rect for an Editor control.

When creating a new Editor control it is a sound design to implement the
actual control without relying on GUILayout and instead have the control take
a [Rect](Rect.html) as parameter, similar to the controls in the
[EditorGUI](EditorGUI.html) class. This ensures the control can also be used
in for example a [PropertyDrawer](PropertyDrawer.html), which does not allow
GUILayout.  
  
Once a non-layout version of the control is implemented, a layout version can
easily be made as well, which simply calls into the non-layout version. In
order to get a rect fitting for the control, the GetControlRect function can
be used.

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

