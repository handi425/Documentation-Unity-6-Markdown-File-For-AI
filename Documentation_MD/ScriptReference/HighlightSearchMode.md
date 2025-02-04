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

# HighlightSearchMode

enumeration

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

### Description

Used to specify how to find a given element in the editor to highlight.

Let's consider various approaches to highlighting the Scale control in the
Transform component.  
  
Using the
[HighlightSearchMode.PrefixLabel](HighlightSearchMode.PrefixLabel.html) mode
you can specify the label text "Scale" as the identifier to highlight the
entire Scale control with both label and all three number fields included.
This mode can't be used if you want to only highlight the X component of the
Scale control. Since the label text of the X component is simply "X", you
would get the X component of the Position control instead if you attempted
that. The
[HighlightSearchMode.PrefixLabel](HighlightSearchMode.PrefixLabel.html) mode
works for any control that uses
[EditorGUI.PrefixLabel](EditorGUI.PrefixLabel.html) or
[EditorGUI.HandlePrefixLabel](EditorGUI.HandlePrefixLabel.html).  
  
If you use the [HighlightSearchMode.Content](HighlightSearchMode.Content.html)
mode to search for the text "Scale", only the label itself will be
highlighted. This mode can highlight what corresponds to a single
[GUIStyle.Draw](GUIStyle.Draw.html) call and hence cannot highlight composite
controls. It is particularly useful for highlighting buttons.  
  
The [HighlightSearchMode.Identifier](HighlightSearchMode.Identifier.html) mode
searches for rects explicitly marked to be highlightable using the
[Highlighter.HighlightIdentifier](Highlighter.HighlightIdentifier.html)
function. This is for example done for all controls that uses the
[SerializedProperty](SerializedProperty.html) system, using the
[SerializedProperty.propertyPath](SerializedProperty-propertyPath.html) as the
identifier. This means you could use this mode to highlight the X component of
the Scale control by searching for "m_LocalScale.x".  
  
The [HighlightSearchMode.Auto](HighlightSearchMode.Auto.html) mode searches
using all the above modes and can be used in most cases. Searching for "Scale"
using this mode will highlight the entire Scale control rather than just the
label, since the PrefixLabel handling is hit before the
[GUIStyle.Draw](GUIStyle.Draw.html) call of the label.  
  
Additional resources: [Highlighter](Highlighter.html).

### Properties

[None](HighlightSearchMode.None.html)| Highlights nothing.  
---|---  
[Auto](HighlightSearchMode.Auto.html)| Highlights the first element found
using any of the search modes.  
[Identifier](HighlightSearchMode.Identifier.html)| Highlights an element with
a given identifier text.  
[PrefixLabel](HighlightSearchMode.PrefixLabel.html)| Highlights an entire
editor control using its label text as identifier.  
[Content](HighlightSearchMode.Content.html)| Highlights an element containing
text using the text as identifier.  
  
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

