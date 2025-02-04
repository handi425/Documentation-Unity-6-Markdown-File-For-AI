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

#  [ISearchEngineBase](SearchService.ISearchEngineBase.html).EndSession

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

public void
EndSession([SearchService.ISearchContext](SearchService.ISearchContext.html)
context);

### Parameters

context | The search context.  
---|---  
  
### Description

A function called at the end of a search session.

Depending on the type of engine
([ISceneSearchEngine](SearchService.ISceneSearchEngine.html),
[IProjectSearchEngine](SearchService.IProjectSearchEngine.html),
[IObjectSelectorEngine](SearchService.IObjectSelectorEngine.html)), a search
session ends at different times. For
[ISceneSearchEngine](SearchService.ISceneSearchEngine.html) and
[IProjectSearchEngine](SearchService.IProjectSearchEngine.html), a search
session ends when the query is cleared.  
  
For [IObjectSelectorEngine](SearchService.IObjectSelectorEngine.html), there
are two possibilities:

  1. The session ends when the selector is closed (see [ISelectorEngine.SelectObject](SearchService.ISelectorEngine.SelectObject.html)).
  2. The session ends forcefully because another selector will be opened, in which case the current selector needs to be closed because the [ObjectSelector](EditorGUIUtility.ShowObjectPicker.html) API does not support concurrent selectors. See [ObjectSelectorSearchEndSessionModes.CloseSelector](SearchService.ObjectSelectorSearchEndSessionModes.CloseSelector.html) for an example.

This function is not called again until the next search session ends.  
  
Additional resources:
[ISearchEngineBase.BeginSession](SearchService.ISearchEngineBase.BeginSession.html),
[ISearchEngineBase.BeginSearch](SearchService.ISearchEngineBase.BeginSearch.html),
[ISearchEngineBase.EndSearch](SearchService.ISearchEngineBase.EndSearch.html).

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

