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

#  [SearchUtils](Search.SearchUtils.html).CreateGroupProvider

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

public static [Search.SearchProvider](Search.SearchProvider.html)
CreateGroupProvider([Search.SearchProvider](Search.SearchProvider.html)
templateProvider, string groupId, int groupPriority, bool cacheProvider);

### Parameters

templateProvider | Search provider template to copy.  
---|---  
groupId | New group id. This id is also used as the display name for the group tab if displayed in the [ISearchView](Search.ISearchView.html).  
groupPriority | Priority used to order the group tab in the [ISearchView](Search.ISearchView.html).  
cacheProvider | Ask the system to cache the provider in case the function gets called with the same ID later.  
  
### Returns

**SearchProvider** A new search provider that can be used temporarily for a
given search session.

### Description

Copy of a search provider to create a new group copy.

This can be useful to base a new search provider on an existing one simply by
replacing a few handlers. Note that this search provider will not be globally
available, in example with
[SearchService.GetProvider](Search.SearchService.GetProvider.html).

    
    
    static [SearchProvider](Search.SearchProvider.html) CreateDecalProvider()
    {
        var assetProvider = [SearchService.GetProvider](Search.SearchService.GetProvider.html)("asset");
        var decalProvider = [SearchUtils.CreateGroupProvider](Search.SearchUtils.CreateGroupProvider.html)(assetProvider, "Decals", 0, true);
        decalProvider.fetchPropositions = EnumerateDecalPropositions;
        return decalProvider;
    }
    

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

