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

# TextCursorPlacement

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

Where to place the cursor in the text. (see
[ISearchView.SetSearchText](Search.ISearchView.SetSearchText.html)).

    
    
    [[MenuItem](MenuItem.html)("Examples/[ISearchView](Search.ISearchView.html)/SetSearchText_WithCursorPosition")]
    public static void SetSearchText_WithCursorPosition()
    {
        var view = [SearchService.ShowContextual](Search.SearchService.ShowContextual.html)("asset");
        view.SetSearchText("t:material", [TextCursorPlacement.MoveLineStart](Search.TextCursorPlacement.MoveLineStart.html));
    }
    

### Properties

[None](Search.TextCursorPlacement.None.html)| Do not move the cursor.  
---|---  
[MoveLineEnd](Search.TextCursorPlacement.MoveLineEnd.html)| Move the cursor to
the end of the line of text.  
[MoveLineStart](Search.TextCursorPlacement.MoveLineStart.html)| Move the
cursor to the beginning of the line of text.  
[MoveToEndOfPreviousWord](Search.TextCursorPlacement.MoveToEndOfPreviousWord.html)|
Move the cursor to the end of the previous word.  
[MoveToStartOfNextWord](Search.TextCursorPlacement.MoveToStartOfNextWord.html)|
Move the cursor to the start of the previous word.  
[MoveWordLeft](Search.TextCursorPlacement.MoveWordLeft.html)| Move the cursor
one word to the left.  
[MoveWordRight](Search.TextCursorPlacement.MoveWordRight.html)| Move the
cursor one word to the right.  
[MoveAutoComplete](Search.TextCursorPlacement.MoveAutoComplete.html)| Default
cursor position (end of the line of text).  
[Default](Search.TextCursorPlacement.Default.html)| Do not move the cursor.  
  
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

