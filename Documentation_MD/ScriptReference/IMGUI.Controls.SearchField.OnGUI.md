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

#  [SearchField](IMGUI.Controls.SearchField.html).OnGUI

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

public string OnGUI(string text, params GUILayoutOption[] options);

### Parameters

text | Text string to display in the search field.  
---|---  
options | An optional list of layout options that specify extra layout properties.   
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**string** The text entered in the search field. The original input string is
returned instead if the search field text was not changed.

### Description

This function displays the search field with the default UI style and uses the
GUILayout class to automatically calculate the position and size of the Rect
it is rendered to. Pass an optional list to specify extra layout properties.

* * *

## Declaration

public string OnGUI([Rect](Rect.html) rect, string text);

### Parameters

rect | Rectangle to use for the search field.  
---|---  
text | Text string to display in the search field.  
  
### Returns

**string** The text entered in the search field. The original input string is
returned instead if the search field text was not changed.

### Description

This function displays the search field with the default UI style in the given
Rect.

* * *

## Declaration

public string OnGUI([Rect](Rect.html) rect, string text,
[GUIStyle](GUIStyle.html) style, [GUIStyle](GUIStyle.html) cancelButtonStyle,
[GUIStyle](GUIStyle.html) emptyCancelButtonStyle);

### Parameters

rect | Rectangle to use for the search field.  
---|---  
text | Text string to display in the search field.  
style | The text field style.  
cancelButtonStyle | The cancel button style used when there is text in the search field.  
emptyCancelButtonStyle | The cancel button style used when there is no text in the search field.  
  
### Returns

**string** The text entered in the SearchField. The original input string is
returned instead if the search field text was not changed.

### Description

This function displays a search text field with the given Rect and UI style
parameters.

Use this function to customize the UI style of the search text field. You must
set cancelButtonStyle.fixedWidth to a suitable and desired width as this
affects the placement of the close button to the right of the search text
field.

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

