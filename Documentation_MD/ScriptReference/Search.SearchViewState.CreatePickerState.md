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

#  [SearchViewState](Search.SearchViewState.html).CreatePickerState

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

public static [Search.SearchViewState](Search.SearchViewState.html)
CreatePickerState(string title,
[Search.SearchContext](Search.SearchContext.html) context, Action<Object,bool>
selectObjectHandler, Action<Object> trackingObjectHandler, string typeName,
Type filterType, [Search.SearchViewFlags](Search.SearchViewFlags.html) flags);

## Declaration

public static [Search.SearchViewState](Search.SearchViewState.html)
CreatePickerState(string title,
[Search.SearchContext](Search.SearchContext.html) context,
Action<SearchItem,bool> selectHandler, Action<SearchItem> trackingHandler,
Func<SearchItem,bool> filterHandler,
[Search.SearchViewFlags](Search.SearchViewFlags.html) flags);

### Parameters

title | Title of the picker window.  
---|---  
context | SearchContext used to setup whcih SearchProvider and initial query are setup for this Picker.  
selectObjectHandler | Selector Callback.  
trackingObjectHandler | Callbacks triggeeds when the select selects an item.  
typeName | Name of the type of assets or components we want to pick.  
filterType | Type of the items we want to pick.  
flags | Flags specifying how the picker view should be displayed.  
selectHandler | Selector Callback.  
trackingHandler | Callbacks triggeeds when the select selects an item.  
filterHandler | Filtering calback.  
  
### Returns

**SearchViewState** Returns a view state use to open an Object picker.

### Description

Create a SearchViewState specially setup to show an Object Picker.

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

