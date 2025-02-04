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

#  [UnityWebRequest](Networking.UnityWebRequest.html).SendWebRequest

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

public
[Networking.UnityWebRequestAsyncOperation](Networking.UnityWebRequestAsyncOperation.html)
SendWebRequest();

### Description

Begin communicating with the remote server.

After calling this method, the
[UnityWebRequest](Networking.UnityWebRequest.html) will perform DNS resolution
(if necessary), transmit an HTTP request to the remote server at the target
URL and process the server’s response.  
  
This method can only be called once on any given
[UnityWebRequest](Networking.UnityWebRequest.html) object.  
  
Once this method is called, you cannot change any of the UnityWebRequest’s
properties. You cannot change
[UnityWebRequest](Networking.UnityWebRequest.html) properties after
[SendWebRequest](Networking.UnityWebRequest.SendWebRequest.html) is called.  
  
This method returns a WebRequestAsyncOperation object. Yielding the
WebRequestAsyncOperation inside a coroutine will cause the coroutine to pause
until the [UnityWebRequest](Networking.UnityWebRequest.html) encounters a
system error or finishes communicating.

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

