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

# SearchMonitorView

struct in UnityEditor.Search

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

Scoped search monitor view.

This struct provides a view on Search's main
[PropertyDatabases](Search.PropertyDatabase.html). Search offers some
convenient [PropertyDatabases](Search.PropertyDatabase.html) to cache data. If
this data comes from scenes or assets, those will be invalidated automatically
whenever the scene or asset changes. If it comes from another source, you need
to manage the invalidation process yourself with
[Invalidate](Search.SearchMonitorView.Invalidate.html) and
[InvalidateDocument](Search.SearchMonitorView.InvalidateDocument.html).

### Public Methods

[Invalidate](Search.SearchMonitorView.Invalidate.html)| Mark a document
property to be invalided.  
---|---  
[InvalidateDocument](Search.SearchMonitorView.InvalidateDocument.html)| Mark a
document to be invalidated.  
[StoreAlias](Search.SearchMonitorView.StoreAlias.html)| Store a property alias
in the property string table.  
[StoreProperty](Search.SearchMonitorView.StoreProperty.html)| Store a property
value.  
[TryLoadAlias](Search.SearchMonitorView.TryLoadAlias.html)| Gets a property
alias if any.  
[TryLoadProperty](Search.SearchMonitorView.TryLoadProperty.html)| Loads a
property if any.  
  
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

