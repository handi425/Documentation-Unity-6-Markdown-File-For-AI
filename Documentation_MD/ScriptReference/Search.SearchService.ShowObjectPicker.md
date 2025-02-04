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

#  [SearchService](Search.SearchService.html).ShowObjectPicker

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

public static [Search.ISearchView](Search.ISearchView.html)
ShowObjectPicker(Action<Object,bool> selectHandler, Action<Object>
trackingHandler, string searchText, string typeName, Type filterType, float
defaultWidth, float defaultHeight,
[Search.SearchFlags](Search.SearchFlags.html) flags);

### Parameters

selectHandler | Callback to trigger when a user selects an item.  
---|---  
trackingHandler | Callback to trigger when the user is modifying a Search selection (i.e. tracking the currently selected item).  
searchText | Initial search text.  
typeName | Type name of the object to select. Can be used to replace filterType.  
filterType | Type of the object to select.  
defaultWidth | Initial width of the window.  
defaultHeight | Initial height of the window.  
flags | Options defining how the query is performed.  
  
### Returns

**ISearchView** Returns the search view window instance.

### Description

Open a Search Picker window for Unity objects.

Use Search as an object picker to select any Unity object based on the
specified filter type. For a more generic picker, please use
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

