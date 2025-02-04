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

# SearchQueryError

class in UnityEditor.Search

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

Represents a query parsing error.

This class is only used in the context of
[SearchProviders](Search.SearchProvider.html), when performing a search. It
allows a [SearchProvider](Search.SearchProvider.html) to report error during
the parsing of the search query. Here is an example of a
[SearchProvider](Search.SearchProvider.html) that uses a
[QueryEngine](Search.QueryEngine_1.html) and reports parsing errors:

    
    
    public IEnumerable<T> Search([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider, IEnumerable<T> subset = null)
    {
        var query = m_QueryEngine.ParseQuery(context.searchQuery, true);
        if (!query.valid)
        {
            if (reportError)
                context.AddSearchQueryErrors(query.errors.Select(e => new [SearchQueryError](Search.SearchQueryError.html)(e, context, provider)));
            return Enumerable.Empty<T>();
        }
    
        m_DoFuzzyMatch = query.HasToggle("fuzzy");
        IEnumerable<T> gameObjects = subset ?? m_Objects;
        return query.Apply(gameObjects, false);
    }
    

In the previous example, the function "Search" would be called by the
provider's [fetchItem](Search.SearchProvider.fetchItem.html).  
  
In the Search window, the errors are shown when there is no result available.
![](../StaticFiles/ScriptRefImages/Example_SearchQueryError.png).

### Properties

[context](Search.SearchQueryError-context.html)| The context in which this
error was logged.  
---|---  
[index](Search.SearchQueryError-index.html)| Index where the error occurred.  
[length](Search.SearchQueryError-length.html)| Length of the block that was
being parsed.  
[provider](Search.SearchQueryError-provider.html)| Which search provider
logged this error.  
[reason](Search.SearchQueryError-reason.html)| The reason for the error.  
[type](Search.SearchQueryError-type.html)| The type of query error.  
  
### Constructors

[SearchQueryError](Search.SearchQueryError-ctor.html)| Creates a new
SearchQueryError.  
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

