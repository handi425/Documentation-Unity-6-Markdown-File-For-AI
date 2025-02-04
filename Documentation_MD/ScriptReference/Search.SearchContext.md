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

# SearchContext

class in UnityEditor.Search

Leave feedback

  

Implements
interfaces:[ISerializationCallbackReceiver](ISerializationCallbackReceiver.html)

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

The search context includes all the data necessary to perform a query. It
allows the full customization of how a query may be performed.

### Properties

[empty](Search.SearchContext-empty.html)| Indicates of the search query is
empty. This exclude the search filter id. In example if the search text is h:
, then this property will still return true.  
---|---  
[filterId](Search.SearchContext-filterId.html)| Explicit filter ID. Usually it
is the first search token like h:, p: to do an explicit search for a given
search provider. Can be null.  
[options](Search.SearchContext-options.html)| Search context options.  
[progressId](Search.SearchContext-progressId.html)| Progress handle to display
the progress bar for the search currently in progress.  
[providers](Search.SearchContext-providers.html)| Which search providers are
active for this particular context.  
[searchInProgress](Search.SearchContext-searchInProgress.html)| Indicates if
an asynchronous search is currently in progress for this context.  
[searchPhrase](Search.SearchContext-searchPhrase.html)| Returns a phrase that
contains only words separated by spaces.  
[searchQuery](Search.SearchContext-searchQuery.html)| Processed search query
(no filterId, no textFilters).  
[searchQueryOffset](Search.SearchContext-searchQueryOffset.html)| Character
offset of the processed search query in the raw search text.  
[searchText](Search.SearchContext-searchText.html)| Raw search text (what is
in the Search text box).  
[searchView](Search.SearchContext-searchView.html)| The search view presenting
the search results.  
[searchWords](Search.SearchContext-searchWords.html)| Search query tokenized
by words. All text filters are discarded and all words are in lowercase.  
[selection](Search.SearchContext-selection.html)| Returns the search result
selection if any.  
[textFilters](Search.SearchContext-textFilters.html)| All tokens containing a
colon (':').  
[wantsMore](Search.SearchContext-wantsMore.html)| Indicates if the search
should return all the results instead of only the most relevant.  
  
### Constructors

[SearchContext](Search.SearchContext-ctor.html)| Creates a new search context.  
---|---  
  
### Public Methods

[AddSearchQueryError](Search.SearchContext.AddSearchQueryError.html)| Adds a
new query error on this context.  
---|---  
[AddSearchQueryErrors](Search.SearchContext.AddSearchQueryErrors.html)| Adds
new query errors on this context.  
[Dispose](Search.SearchContext.Dispose.html)| Dispose of the Search Context.  
[IsEnabled](Search.SearchContext.IsEnabled.html)| Checks if a search provider
is available to process a query.  
[SetFilter](Search.SearchContext.SetFilter.html)| Enables or disables a single
search provider. A disabled search provider won't be asked to provide items to
resolve the query.  
  
### Events

[asyncItemReceived](Search.SearchContext-asyncItemReceived.html)| This event
is used to receive any asynchronous search result.  
---|---  
[sessionEnded](Search.SearchContext-sessionEnded.html)| Invoked when a Search
has ended.  
[sessionStarted](Search.SearchContext-sessionStarted.html)| Invoked when a
Search is started.  
  
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

