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

#  [SearchProvider](Search.SearchProvider.html).CreateItem

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

public [Search.SearchItem](Search.SearchItem.html)
CreateItem([Search.SearchContext](Search.SearchContext.html) context, string
id, int score, string label, string description, [Texture2D](Texture2D.html)
thumbnail, object data);

**Obsolete** Use CreateItem which take a SearchContext.

## Declaration

public [Search.SearchItem](Search.SearchItem.html) CreateItem(string id, int
score, string label, string description, [Texture2D](Texture2D.html)
thumbnail, object data);

## Declaration

public [Search.SearchItem](Search.SearchItem.html)
CreateItem([Search.SearchContext](Search.SearchContext.html) context, string
id);

**Obsolete** Use CreateItem which take a SearchContext.

## Declaration

public [Search.SearchItem](Search.SearchItem.html) CreateItem(string id);

**Obsolete** Use CreateItem which take a SearchContext.

## Declaration

public [Search.SearchItem](Search.SearchItem.html) CreateItem(string id,
string label);

## Declaration

public [Search.SearchItem](Search.SearchItem.html) CreateItem(string id,
string label, string description, [Texture2D](Texture2D.html) thumbnail,
object data);

## Declaration

public [Search.SearchItem](Search.SearchItem.html)
CreateItem([Search.SearchContext](Search.SearchContext.html) context, string
id, string label, string description, [Texture2D](Texture2D.html) thumbnail,
object data);

### Parameters

context | Search context from the query that generates this item.  
---|---  
id | Unique ID of the search item. This is used to remove duplicates in the user view.  
score | Relevance score of the search item. The relevance score is used to sort all the results per search provider. Lower relevance scores indicate more relevance and are shown first.  
label | Relevance score of the search item. The relevance score is used to sort all the results per search provider. Lower relevance scores indicate more relevance and are shown first.  
description | The search item description is displayed on the second line of the search item UI widget.  
thumbnail | The search item thumbnail is displayed to the left of the item label and description as a preview.  
data | The search item thumbnail is displayed to the left of the item label and description as a preview.  
  
### Returns

**SearchItem** The newly created search item attached to the current search
provider.

### Description

Helper function to create a new search item for the current search provider.

For different use cases see [SearchProvider](Search.SearchProvider.html),
[SearchProvider.id](Search.SearchProvider-id.html),
[SearchProvider.isExplicitProvider](Search.SearchProvider-
isExplicitProvider.html), [SearchProvider.priority](Search.SearchProvider-
priority.html).

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

