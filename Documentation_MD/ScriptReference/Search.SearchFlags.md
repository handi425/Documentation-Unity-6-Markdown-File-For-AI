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

# SearchFlags

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

Search options used to fetch items. Mostly with
[SearchContext](Search.SearchContext.html) to specify how a search should be
handled.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    public class SearchFlags_NoIndexing
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchFlags](Search.SearchFlags.html)/NoIndexing")]
        public static void RequestAll()
        {
            // Find all assets matching the word Search without using any indexed data (will rely on the Find Files provider).
            [SearchService.Request](Search.SearchService.Request.html)("p: Search", ([SearchContext](Search.SearchContext.html) context, IList<[SearchItem](Search.SearchItem.html)> items) =>
            {
                foreach (var item in items)
                    [Debug.Log](Debug.Log.html)(item);
            }, [SearchFlags.NoIndexing](Search.SearchFlags.NoIndexing.html));
        }
    }
    

### Properties

[None](Search.SearchFlags.None.html)| No specific search options. Result will
be unsorted.  
---|---  
[Synchronous](Search.SearchFlags.Synchronous.html)| Search items are fetched
synchronously. This can take a long time for some SearchProvider (like asset).
Use at your own risk.  
[Sorted](Search.SearchFlags.Sorted.html)| Fetched items are sorted by the
search service.  
[FirstBatchAsync](Search.SearchFlags.FirstBatchAsync.html)| Sends the first
items asynchronously.  
[WantsMore](Search.SearchFlags.WantsMore.html)| Sets the search to search for
all results. This might take longer than unusual if SearchProvider are using
multiple sources of items (files on disk, AssetDatabase...)  
[Debug](Search.SearchFlags.Debug.html)| Adds debugging information to
SearchItem while looking for results.  
[NoIndexing](Search.SearchFlags.NoIndexing.html)| Prevents the search from
using indexing. Asset Provider will use its builtin Find in Files provider.  
[Expression](Search.SearchFlags.Expression.html)| Indicates that the search
query will be evaluated as a search expression.  
[QueryString](Search.SearchFlags.QueryString.html)| Evaluate the search text
as a pure query string (do not evaluate the text as a search expression).  
[Packages](Search.SearchFlags.Packages.html)| The Object Picker window will
include any results from packages.  
[Default](Search.SearchFlags.Default.html)| Default Search Flag
(SearchFlags.Sorted).  
[AllProvidersAvailable](Search.SearchFlags.AllProvidersAvailable.html)| All
SearchProviders are available in the SearchWindow dropdown menu.  
[UseSessionSettings](Search.SearchFlags.UseSessionSettings.html)| Persist the
SearchContext state in between sessions using the SearchViewState.sessionName
as its data key.  
[ShowErrorsWithResults](Search.SearchFlags.ShowErrorsWithResults.html)| Always
show query errors even when there are results available. This flag is only
usable with internal API.  
[ReuseExistingWindow](Search.SearchFlags.ReuseExistingWindow.html)| Indicates
that the search view will find any existing window instances that are already
opened before creating a new one. This flag is only usable with internal API.  
[Multiselect](Search.SearchFlags.Multiselect.html)| Indicates that the search
view will allow multi-selection. This flag is only usable with internal API.  
[Dockable](Search.SearchFlags.Dockable.html)| Indicates that the search view
is dockable. This flag is only usable with internal API.  
[FocusContext](Search.SearchFlags.FocusContext.html)| Indicates that the
search view will focus on the first contextual search provider available when
it opens. This flag is only usable with internal API.  
[HidePanels](Search.SearchFlags.HidePanels.html)| Indicates that the search
view will hide its side panels when it opens. This flag is only usable with
internal API.  
[GeneralSearchWindow](Search.SearchFlags.GeneralSearchWindow.html)| This is a
general purpose search window that has access to all Providers in the
SearchService.  
[OpenDefault](Search.SearchFlags.OpenDefault.html)| Opens a search view with
default options. This flag is only usable with internal API.  
[OpenGlobal](Search.SearchFlags.OpenGlobal.html)| Opens a search view for a
global search. This flag is only usable with internal API.  
[OpenContextual](Search.SearchFlags.OpenContextual.html)| Opens a search view
with default contextual options. This flag is only usable with internal API.  
[OpenPicker](Search.SearchFlags.OpenPicker.html)| Opens a search view as an
object picker. This flag is only usable with internal API.  
  
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

