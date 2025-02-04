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

# SearchQueryError Constructor

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

public SearchQueryError(int index, int length, string reason,
[Search.SearchContext](Search.SearchContext.html) context,
[Search.SearchProvider](Search.SearchProvider.html) provider, bool
fromSearchQuery,
[Search.SearchQueryErrorType](Search.SearchQueryErrorType.html) type);

### Parameters

index | Index where the error occurred.  
---|---  
length | Length of the block that was being parsed.  
reason | The reason for the error.  
context | The context in which this error was logged.  
provider | Which search provider logged this error.  
fromSearchQuery | Set to true if this error comes from parsing the searchQuery. This will correctly offset the index with respect to the raw text.  
type | The type of query error. See [SearchQueryErrorType](Search.SearchQueryErrorType.html). Defaults to [SearchQueryErrorType.Error](Search.SearchQueryErrorType.Error.html).  
  
### Description

Creates a new SearchQueryError.

* * *

## Declaration

public SearchQueryError([Search.QueryError](Search.QueryError.html) error,
[Search.SearchContext](Search.SearchContext.html) context,
[Search.SearchProvider](Search.SearchProvider.html) provider, bool
fromSearchQuery);

### Parameters

error | The original [QueryError](Search.QueryError.html).  
---|---  
context | The context in which this error was logged.  
provider | Which search provider logged this error.  
fromSearchQuery | Set to true if this error comes from parsing the searchQuery. This will correctly offset the index with respect to the raw text.  
  
### Description

Creates a new SearchQueryError from an existing
[QueryError](Search.QueryError.html).

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

