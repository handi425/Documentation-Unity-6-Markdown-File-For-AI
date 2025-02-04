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

#  [UnityWebRequest](Networking.UnityWebRequest.html).Abort

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

public void Abort();

### Description

If in progress, halts the UnityWebRequest as soon as possible.

This method may be called at any time. If the UnityWebRequest has not already
completed, the UnityWebRequest will halt uploading or downloading data as soon
as possible. Aborted UnityWebRequests are considered to have encountered a
system error. Depending upon the type of error, the
[result](Networking.UnityWebRequest-result.html) property will return one of
the error values:
[ConnectionError](Networking.UnityWebRequest.Result.ConnectionError.html),
[ProtocolError](Networking.UnityWebRequest.Result.ProtocolError.html), or
[DataProcessingError](Networking.UnityWebRequest.Result.DataProcessingError.html).
The [error](Networking.UnityWebRequest-error.html) property will be `Request
Aborted`.  
  
If this method is called prior to calling
[Send](Networking.UnityWebRequest.Send.html), then the UnityWebRequest will
abort immediately after the call to
[Send](Networking.UnityWebRequest.Send.html).  
  
Calls to this method have no effect after this UnityWebRequest has encountered
a different error, or has successfully finished communicating with the remote
server.

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

