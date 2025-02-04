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

# SearchProposition Constructor

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

public SearchProposition(string label, string replacement, string help, int
priority, [Texture2D](Texture2D.html) icon, object data, [Color](Color.html)
color);

## Declaration

public SearchProposition(string category, string label, string replacement,
string help, int priority,
[Search.TextCursorPlacement](Search.TextCursorPlacement.html) moveCursor,
[Texture2D](Texture2D.html) icon, Type type, object data, [Color](Color.html)
color);

## Declaration

public SearchProposition(string label, string replacement, string help, int
priority, [Search.TextCursorPlacement](Search.TextCursorPlacement.html)
moveCursor, [Texture2D](Texture2D.html) icon, [Color](Color.html) color);

### Parameters

category | Category text used to group propositions together in query builder mode.  
---|---  
label | Display text of the proposition.  
replacement | Text used to auto-complete the query when selected.  
help | Help text used to display additional information about the search proposition.  
priority | Value used to sort the propositions among other search propositions when displaying choices to the user.  
moveCursor | Indicates when the text cursor should be moved when auto-completing the query with the selected proposition.  
icon | Icon used to display the proposition.  
color | Color used in query builder mode to draw the block using a specific color.  
data | User data that the user can retrieve later to determine the nature of the proposition.  
type | Type of search proposition value. This information is used in the query builder mode.  
  
### Description

Create a new search proposition.

Used with [SearchProvider.fetchPropositions](Search.SearchProvider-
fetchPropositions.html).

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

