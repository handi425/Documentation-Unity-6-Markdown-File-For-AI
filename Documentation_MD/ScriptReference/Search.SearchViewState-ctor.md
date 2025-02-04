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

# SearchViewState Constructor

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

public SearchViewState([Search.SearchContext](Search.SearchContext.html)
context);

## Declaration

public SearchViewState([Search.SearchContext](Search.SearchContext.html)
context, [Search.SearchViewFlags](Search.SearchViewFlags.html) flags);

### Parameters

context | Initial search context.  
---|---  
flags | Initial search view flags.  
  
### Description

Create search view flags used to create a new Search window.

See [SearchService.ShowWindow](Search.SearchService.ShowWindow.html).

* * *

## Declaration

public SearchViewState([Search.SearchContext](Search.SearchContext.html)
context, [Search.SearchTable](Search.SearchTable.html) tableConfig,
[Search.SearchViewFlags](Search.SearchViewFlags.html) flags);

### Parameters

context | Initial search context.  
---|---  
tableConfig | Initial search table configuration.  
flags | Initial search view flags.  
  
### Description

Creates a search view that will be opened in table view.

* * *

## Declaration

public SearchViewState([Search.SearchContext](Search.SearchContext.html)
context, Action<Object,bool> selectObjectHandler, Action<Object>
trackingObjectHandler, string typeName, Type filterType);

### Parameters

context | Initial search context.  
---|---  
selectObjectHandler | Handler executed when the user has selected an object.  
trackingObjectHandler | Handler executed when the user clicks on an item in the search view.  
typeName | String type name used to filter items in the search results. This parameter can be defined if the concrete Type cannot be accessed.  
filterType | Concrete type used to filter items in the search results.  
  
### Description

Creates a search view state that will be used to open a search picker using
[SearchService.ShowPicker](Search.SearchService.ShowPicker.html).

* * *

## Declaration

public SearchViewState([Search.SearchContext](Search.SearchContext.html)
context, Action<SearchItem,bool> selectHandler);

### Parameters

context | Initial search context.  
---|---  
selectHandler | Handler executed when the user has selected an search result.  
  
### Description

Creates a search view state that will be used to open a search picker using
[SearchService.ShowPicker](Search.SearchService.ShowPicker.html).

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

