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

#  [UnityWebRequest](Networking.UnityWebRequest.html).redirectLimit

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

public int redirectLimit;

### Description

Indicates the number of redirects that this
[UnityWebRequest](Networking.UnityWebRequest.html) follows before halting with
a `Redirect Limit Exceeded` system error.

If you want to disable redirects altogether, set this property to zero - this
`UnityWebRequest` will then refuse to follow redirects. If a redirect is
encountered while redirects are disabled, the request will halt with a
`Redirect Limit Exceeded` system error.  
  
If you don't want to limit the number of redirects, you can set this property
to any negative number. **Note:** **This is not recommended**. If the redirect
limit is disabled and the `UnityWebRequest` encounters a redirect loop, the
`UnityWebRequest` will consume processor time until
[Abort](Networking.UnityWebRequest.Abort.html) is called.  
  
**Note:** On WebGL platforms, the `UnityWebRequest` API behaves differently.
It only supports a redirect limit of `0` where the request fails on a
redirect, and for anything above `0`, it uses the browser-default redirect
limit. This applies to Unity 2021.3 and later versions.  
  
  
  
_Default value:_ `32`.

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

