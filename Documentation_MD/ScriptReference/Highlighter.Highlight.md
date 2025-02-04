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

#  [Highlighter](Highlighter.html).Highlight

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

public static bool Highlight(string windowTitle, string text);

## Declaration

public static bool Highlight(string windowTitle, string text,
[HighlightSearchMode](HighlightSearchMode.html) mode);

### Parameters

windowTitle | The title of the window the element is inside.  
---|---  
text | The text to identify the element with.  
mode | Optional mode to specify how to search for the element.  
  
### Returns

**bool** `true` if the requested element was found; otherwise `false`.

### Description

Highlights an element in the editor.

This function will highlight the specified element in the specified window. If
the element could not be found, the function returns false. If the element is
inside a scrollview and is not currently visible, the scrollview will first
automatically scroll to reveal the element and then highlight it.  
  
Once the element is highlighted it will stay highlighted until either the
[Highlighter.Stop](Highlighter.Stop.html) function is called, or the element
disappears from view. The element could disappear from view if the user
scrolls away from it, the window is closed, the section of the GUI with the
element in it is collapsed or otherwise hidden, or when starting or stopping
Play Mode.  
  
Most EditorGUI controls can be highlighted using their label as identifier.  
  
Any control that uses the [SerializedProperty](SerializedProperty.html) system
can be highlighted using its
[SerializedProperty.propertyPath](SerializedProperty-propertyPath.html).  
  
Any element with text in it can be highlighted using that text as identifier,
which is for example useful for buttons.  
  
See the [HighlightSearchMode](HighlightSearchMode.html) enum for more details
on identifying elements.  
  
Additional resources: [Highlighter.Stop](Highlighter.Stop.html),
[Highlighter.HighlightIdentifier](Highlighter.HighlightIdentifier.html).

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

