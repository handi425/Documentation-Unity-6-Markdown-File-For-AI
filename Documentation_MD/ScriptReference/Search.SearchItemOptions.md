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

# SearchItemOptions

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

Indicates how the search item description needs to be formatted when presented
to the user.

    
    
    private static [SearchItem](Search.SearchItem.html) SearchLogEntry([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider, LogEntry logEntry)
    {
        if (![SearchUtils.MatchSearchGroups](Search.SearchUtils.MatchSearchGroups.html)(context, logEntry.msgLowerCased, true))
            return null;
    
        var logItem = provider.CreateItem(context, logEntry.id, ~logEntry.lineNumber, logEntry.msg, null, null, logEntry);
        logItem.options = [SearchItemOptions.Ellipsis](Search.SearchItemOptions.Ellipsis.html) | [SearchItemOptions.RightToLeft](Search.SearchItemOptions.RightToLeft.html) | [SearchItemOptions.Highlight](Search.SearchItemOptions.Highlight.html);
        return logItem;
    }
    

### Properties

[None](Search.SearchItemOptions.None.html)| Uses default description.  
---|---  
[Ellipsis](Search.SearchItemOptions.Ellipsis.html)| If the description is
longer than the width of the search view, truncates the description and adds
an ellipsis.  
[RightToLeft](Search.SearchItemOptions.RightToLeft.html)| If the description
is longer than the search view, keeps the last characters.  
[Highlight](Search.SearchItemOptions.Highlight.html)| Highlights parts of the
description that match the Search Query.  
[FuzzyHighlight](Search.SearchItemOptions.FuzzyHighlight.html)| Highlights
parts of the description that match the Fuzzy Search Query.  
[Compacted](Search.SearchItemOptions.Compacted.html)| Uses Label instead of
description for shorter display.  
[AlwaysRefresh](Search.SearchItemOptions.AlwaysRefresh.html)| Indicates that
the item will always be refreshed.  
[FullDescription](Search.SearchItemOptions.FullDescription.html)| The item
description that is displayed in full mode. This is usually the case when the
description is displayed in the Preview Inspector as opposed to the Result
View.  
[CustomAction](Search.SearchItemOptions.CustomAction.html)| Indicates that the
item is used as a built-in or custom user action that should always be
displayed on top of result views.  
  
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

