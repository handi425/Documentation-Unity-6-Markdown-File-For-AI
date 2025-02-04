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

# SearchField

class in UnityEditor.IMGUI.Controls

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

The SearchField control creates a text field for a user to input text that can
be used for searching.

It comes in two UI styles: one for normal usage and one for toolbars.

### Properties

[autoSetFocusOnFindCommand](IMGUI.Controls.SearchField-
autoSetFocusOnFindCommand.html)| Changes the keyboard focus to the search
field when the user presses ‘Ctrl/Cmd + F’ when set to true. It is true by
default.  
---|---  
[searchFieldControlID](IMGUI.Controls.SearchField-searchFieldControlID.html)|
This is the controlID used for the text field to obtain keyboard focus.  
  
### Public Methods

[HasFocus](IMGUI.Controls.SearchField.HasFocus.html)| This function returns
true if the search field has keyboard focus.  
---|---  
[OnGUI](IMGUI.Controls.SearchField.OnGUI.html)| This function displays the
search field with the default UI style and uses the GUILayout class to
automatically calculate the position and size of the Rect it is rendered to.
Pass an optional list to specify extra layout properties.  
[OnToolbarGUI](IMGUI.Controls.SearchField.OnToolbarGUI.html)| This function
displays the search field with the toolbar UI style and uses the GUILayout
class to automatically calculate the position and size of the Rect it is
rendered to. Pass an optional list to specify extra layout properties.  
[SetFocus](IMGUI.Controls.SearchField.SetFocus.html)| This function changes
keyboard focus to the search field so a user can start typing.  
  
### Events

[downOrUpArrowKeyPressed](IMGUI.Controls.SearchField-
downOrUpArrowKeyPressed.html)| This event is dispatched when the focused
search field detects that the down or up key is pressed and can be used to
change keyboard focus to another control, such as the TreeView.  
---|---  
  
### Delegates

[SearchFieldCallback](IMGUI.Controls.SearchField.SearchFieldCallback.html)|
This is a generic callback delegate for SearchField events and does not take
any parameters.  
---|---  
  
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

