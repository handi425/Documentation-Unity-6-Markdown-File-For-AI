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

# SearchMonitor

class in UnityEditor.Search

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

The search monitor is responsible to track any changes that occurs in Unity in
order to update search indexes or other search data structure at runtime.

### Static Properties

[pending](Search.SearchMonitor-pending.html)| Indicates if the changes still
need to be processed by the search backend.  
---|---  
  
### Static Methods

[GetDiff](Search.SearchMonitor.GetDiff.html)| Returns the assets that changed
since a point in time.  
---|---  
[GetView](Search.SearchMonitor.GetView.html)| Returns a SearchMonitorView to
access Search's main PropertyDatabases.  
[RaiseContentRefreshed](Search.SearchMonitor.RaiseContentRefreshed.html)| Mark
content to be refreshed.  
[Reset](Search.SearchMonitor.Reset.html)| Reset the search property database
content, invalidating all caches.  
  
### Events

[contentRefreshed](Search.SearchMonitor-contentRefreshed.html)| Event invoked
when some content has changed.  
---|---  
[documentsInvalidated](Search.SearchMonitor-documentsInvalidated.html)| Event
raised when documents get invalidated.  
[objectChanged](Search.SearchMonitor-objectChanged.html)| Event raised when an
UnityEngine.Object changed.  
[sceneChanged](Search.SearchMonitor-sceneChanged.html)| Event raised when the
current loaded scene changes that might affect search results.  
  
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

