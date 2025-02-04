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

#  [SearchUtils](Search.SearchUtils.html).MatchSearchGroups

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

public static bool
MatchSearchGroups([Search.SearchContext](Search.SearchContext.html) context,
string content, bool ignoreCase);

### Parameters

context | Search context containing the searchQuery that search tries to match.  
---|---  
content | String content that is tokenized and used to match the search query.  
ignoreCase | Perform matching while ignoring letter casing.  
  
### Returns

**bool** If a match has occurred.

### Description

Helper function to match a string against the SearchContext. This will try to
match the search query against each token of content (similar to the
AddComponent menu workflow).

    
    
    private static IEnumerable<[SearchItem](Search.SearchItem.html)> SearchLogs([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider)
    {
        lock (s_Logs)
        {
            if (!s_Initialized)
            {
                s_Initialized = true;
                [Application.logMessageReceived](Application-logMessageReceived.html) -= HandleLog;
                [Application.logMessageReceived](Application-logMessageReceived.html) += HandleLog;
            }
            for (int logIndex = 0; logIndex < s_Logs.Count; ++logIndex)
                yield return SearchLogEntry(context, provider, s_Logs[logIndex]);
        }
    }
    

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

