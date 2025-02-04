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

# ISearchView

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

Search view interface used by the search context to execute UI operations.

### Properties

[context](Search.ISearchView-context.html)| Returns the current view search
context.  
---|---  
[currentGroup](Search.ISearchView-currentGroup.html)| Indicates the current
group that is selected by the user.  
[displayMode](Search.ISearchView-displayMode.html)| Indicates how the data is
displayed in the UI.  
[filterCallback](Search.ISearchView-filterCallback.html)| Callback used to
filter items shown in the list.  
[itemIconSize](Search.ISearchView-itemIconSize.html)| Defines the size of
items in the search view.  
[multiselect](Search.ISearchView-multiselect.html)| Allows multi-selection of
items in the list/grid of items. If false, a user can only select a single
item.  
[position](Search.ISearchView-position.html)| Returns the absolute position of
the Search window.  
[results](Search.ISearchView-results.html)| Returns the list of all search
results.  
[searchInProgress](Search.ISearchView-searchInProgress.html)| Indicates that
the search view is currently running a query and it has not yet completed.  
[selectCallback](Search.ISearchView-selectCallback.html)| Callback used to
override a default Search behavior.  
[selection](Search.ISearchView-selection.html)| Returns the selected items in
the view.  
[state](Search.ISearchView-state.html)| Returns the view model state of the
Search Window.  
[trackingCallback](Search.ISearchView-trackingCallback.html)| Callback used to
override the tracking behavior.  
  
### Public Methods

[AddSelection](Search.ISearchView.AddSelection.html)| Adds new items to the
current selection.  
---|---  
[Close](Search.ISearchView.Close.html)| Closes the search view.  
[ExecuteAction](Search.ISearchView.ExecuteAction.html)| Executes a Search
action on a given list of items.  
[ExecuteSelection](Search.ISearchView.ExecuteSelection.html)| Execute the
default action of the active selection.  
[Focus](Search.ISearchView.Focus.html)| Make sure the Search window is now
selected to receive input from a user.  
[FocusSearch](Search.ISearchView.FocusSearch.html)| Focus the search text
field control.  
[IsPicker](Search.ISearchView.IsPicker.html)| Indicates if the search view is
being used as an advanced search picker.  
[Refresh](Search.ISearchView.Refresh.html)| Triggers a refresh of the search
view and refetches all the search items from enabled search providers.  
[Repaint](Search.ISearchView.Repaint.html)| Requests the search view to
repaint itself.  
[SelectSearch](Search.ISearchView.SelectSearch.html)| Puts focus in the
SearchView text field AND selects all the text inside the text field (if any).  
[SetColumns](Search.ISearchView.SetColumns.html)| Sets the search view
property table columns.  
[SetSearchText](Search.ISearchView.SetSearchText.html)| Sets the search query
text.  
[SetSelection](Search.ISearchView.SetSelection.html)| Updates the search view
with a new selection.  
[ShowItemContextualMenu](Search.ISearchView.ShowItemContextualMenu.html)|
Shows a contextual menu for the specified item.  
  
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

