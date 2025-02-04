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

#  [AssetBundle](AssetBundle.html).memoryBudgetKB

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

public static uint memoryBudgetKB;

### Description

Controls the size of the shared AssetBundle loading cache. Default value is
1MB.

Depending on your AssetBundle build and load strategy, sections of the
AssetBundle file may be accessed multiple times. To improve loading
performance, the AssetBundle loading cache stores recently accessed pages of
the AssetBundle file. The default cache size should be sufficient in most
cases, but the optimal cache size may vary depending on your workload. The
optimal size can be determined by measuring how different cache sizes affect
the AssetBundle loading times of your specific workload. If you load lots of
small objects (e.g. 100 addressable prefabs) individually out of an
AssetBundle, a larger cache would likely improve performance since future
reads of other objects might reuse cached pages. If your AssetBundle consists
of fewer large objects, or if you read all your objects simultaneously with
functions like [AssetBundle.LoadAll](AssetBundle.LoadAll.html), a larger cache
may not help since the cached pages will likely not be revisited.

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

