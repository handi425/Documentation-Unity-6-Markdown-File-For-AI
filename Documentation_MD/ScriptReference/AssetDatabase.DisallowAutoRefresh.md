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

#  [AssetDatabase](AssetDatabase.html).DisallowAutoRefresh

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

public static void DisallowAutoRefresh();

### Description

Increments an internal counter which Unity uses to determine whether to allow
automatic AssetDatabase refreshing behavior.

Unity uses this method and the corresponding AssetDatabase.AllowAutoRefresh
together internally to prevent an auto-refresh from happening during certain
operations. For example, Unity's version control integration uses it to
prevent an auto-refresh from happening while it gets new changesets.  
  
This method is useful if you are building your own Editor tools and you want
to prevent auto-refreshing of Assets during your own operations (for example,
if you are building custom integration with a version control system).  
  
This method does not simply disable the auto-refresh feature. Instead it
increments a counter, and only allows auto-refresh when the counter is
returned to zero. Therefore, each time you call DisallowAutoRefresh, you must
make sure you also make a corresponding call to AllowAutoRefresh. For example:

    
    
     [AssetDatabase.DisallowAutoRefresh](AssetDatabase.DisallowAutoRefresh.html)();
     // your code here, performed while auto-refresh is not allowed
     [AssetDatabase.AllowAutoRefresh](AssetDatabase.AllowAutoRefresh.html)();

This internal counter is used so that if your code executes multiple nested
"disable" and "enable" pairs, the inner pairs do not accidentally re-enable
auto-refresh too early. Instead, each pair increments and decrements the
counter by one, and if your code is correctly nested, the final outer call to
AllowAutoRefresh sets the counter to zero.  
  
Important Notes:  
  
This method does not influence the behaviour of AssetDatabase.Refresh. The
Asset Database always performs a refresh if AssetDatabase.Refresh is called,
regardless of this method and its internal counter.  
  
This method is separate from the Auto Refresh setting in Unity's Preferences
window, which does not modify this internal counter. If Unity's Auto Refresh
preference setting is disabled, calling Allow and Disallow still modifies the
internal counter, however the Editor does not automatically refresh regardless
of whether the internal counter is at zero or not.  
  
Additional resources:
[AssetDatabase.AllowAutoRefresh](AssetDatabase.AllowAutoRefresh.html).

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

