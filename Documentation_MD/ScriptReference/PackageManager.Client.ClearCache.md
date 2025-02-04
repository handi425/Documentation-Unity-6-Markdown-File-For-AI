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

#  [Client](PackageManager.Client.html).ClearCache

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

[Switch to Manual](../Manual/class-PackageManager.html "Go to PackageManager
Component in the Manual")

## Declaration

public static
[PackageManager.Requests.ClearCacheRequest](PackageManager.Requests.ClearCacheRequest.html)
ClearCache();

### Returns

**ClearCacheRequest** A
[ClearCacheRequest](PackageManager.Requests.ClearCacheRequest.html) instance,
which you can use to get the [StatusCode](PackageManager.StatusCode.html) to
know if the operation completed successfully.

### Description

Empties the package cache.

Empties the [global package cache](../Manual/upm-cache.html). Clearing the
cache will free disk space. However, if a package removed from the cache needs
to be installed in a project, it will be downloaded. As a result, reinstalling
the package will take longer.  
  
`ClearCache()` is an asynchronous operation. Before the operation is complete,
you can use the `ClearCacheRequest` instance to monitor the asynchronous
operation.  
  
**Note:** Make sure any other Client operations have completed before calling
this method. For more information, refer to the note on the
[Client](PackageManager.Client.html) class reference page.

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

