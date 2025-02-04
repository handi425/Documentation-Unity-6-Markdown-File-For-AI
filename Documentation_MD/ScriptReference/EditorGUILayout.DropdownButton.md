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

#  [EditorGUILayout](EditorGUILayout.html).DropdownButton

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

public static bool DropdownButton([GUIContent](GUIContent.html) content,
[FocusType](FocusType.html) focusType, params GUILayoutOption[] options);

## Declaration

public static bool DropdownButton([GUIContent](GUIContent.html) content,
[FocusType](FocusType.html) focusType, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

### Parameters

content | Text, image and tooltip for this button.  
---|---  
focusType | Whether the button should be selectable by keyboard or not.  
style | Optional style to use.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**bool** `true` when the user clicks the button.

### Description

Make a button that reacts to mouse down, for displaying your own dropdown
content.

This control does not do anything but returns true on mouse down when clicked,
as opposed to regular buttons that return true on mouse up.  
  
This can be used for buttons that should open a
[GenericMenu](GenericMenu.html) or your own custom
[EditorWindow](EditorWindow.html) in dropdown form.  
  
When used with a GenericMenu, use GenericMenu.Dropdown and pass the same rect
to the method as was used for the button, which you can obtain using
[GUILayoutUtility.GetLastRect](GUILayoutUtility.GetLastRect.html). Note that
this will only return a valid rect when
[EditorGUILayout.DropdownButton](EditorGUILayout.DropdownButton.html) returns
false. This happens because the last layout event is not used when the click
goes through to open a menu.  
  
When used with a custom EditorWindow, use EditorWindow.ShowAsDropdown and pass
the same rect to the method as was used for the button, which you can obtain
using [GUILayoutUtility.GetLastRect](GUILayoutUtility.GetLastRect.html).

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

