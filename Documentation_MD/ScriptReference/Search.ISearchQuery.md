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

# ISearchQuery

interface in UnityEditor.Search

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

This search query interface is used when handling search query objects. These
can be either assets saved in the user project or saved in the user
preferences.

### Properties

[creationTime](Search.ISearchQuery-creationTime.html)| Indicates the binary
long time of when the search query was created.  
---|---  
[details](Search.ISearchQuery-details.html)| Search query description.  
[displayName](Search.ISearchQuery-displayName.html)| Search query display name
used in the UI.  
[filePath](Search.ISearchQuery-filePath.html)| Indicates where the search
query is saved on disk.  
[guid](Search.ISearchQuery-guid.html)| Unique GUID of the search query.  
[isSearchTemplate](Search.ISearchQuery-isSearchTemplate.html)| Indicates if
the search query is displayed as a search template in the search view home
page.  
[itemCount](Search.ISearchQuery-itemCount.html)| Provides a preview of how
many results this query might yield if executed.  
[lastUsedTime](Search.ISearchQuery-lastUsedTime.html)| Indicates the last time
the query was executed.  
[searchText](Search.ISearchQuery-searchText.html)| Search query text.  
[thumbnail](Search.ISearchQuery-thumbnail.html)| Search query icon thumbnail
set by the user if any.  
  
### Public Methods

[GetName](Search.ISearchQuery.GetName.html)| Returns the formatted name of the
query depending on its source.  
---|---  
[GetProviderIds](Search.ISearchQuery.GetProviderIds.html)| Returns the list of
provider ids that search query is executed with.  
[GetProviderTypes](Search.ISearchQuery.GetProviderTypes.html)| Returns the
list of aggregated type ids the search query executes with.  
[GetSearchTable](Search.ISearchQuery.GetSearchTable.html)| Returns the query
search table configuration if any.  
[GetViewState](Search.ISearchQuery.GetViewState.html)| Returns the search
query view state.  
  
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

