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

#  [QueryEngine<T0>](Search.QueryEngine_1.html).TryGetFilter

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

public bool TryGetFilter(string token, out
[Search.IQueryEngineFilter](Search.IQueryEngineFilter.html) filter);

## Declaration

public bool TryGetFilter(Regex token, out
[Search.IQueryEngineFilter](Search.IQueryEngineFilter.html) filter);

### Parameters

token | The token used to create the filter.  
---|---  
filter | The existing [IQueryEngineFilter](Search.IQueryEngineFilter.html), or null if it does not exist.  
  
### Returns

**bool** Returns true if the filter is retrieved or false if the filter does
not exist.

### Description

Get a filter by its token.

This method tries to retrieve a filter by its token. If it exists, it will be
put in the output parameter "filter" and the function returns true. If the
filter does not exist, the parameter "filter" is set to null and the function
returns false.

    
    
    // Get the filter corresponding to the token "id"
    if (!queryEngine.TryGetFilter("id", out var idFilter))
        [Debug.LogError](Debug.LogError.html)("The filter \"id\" should have been found.");
    

See [GetAllFilters](Search.QueryEngine_1.GetAllFilters.html) for a complete
example.

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

