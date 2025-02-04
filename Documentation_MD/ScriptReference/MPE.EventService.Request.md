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

#  [EventService](MPE.EventService.html).Request

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

public static void Request(string eventType, Action<Exception,object[]>
promiseHandler, object args, long timeoutInMs,
[MPE.EventDataSerialization](MPE.EventDataSerialization.html)
eventDataSerialization);

## Declaration

public static void Request(string eventType, Action<Exception,object[]>
promiseHandler, object[] args, long timeoutInMs,
[MPE.EventDataSerialization](MPE.EventDataSerialization.html)
eventDataSerialization);

### Parameters

eventType | The request's event type name.  
---|---  
promiseHandler | The handler called when the Request is either fulfilled or cancelled, or times out.  
args | Arguments sent with the request event.  
timeoutInMs | The timeout value in milliseconds. After this amount of time passes the Request is considered to be cancelled.  
eventDataSerialization | Specifies how to serialize the request's arguments. This can be standard JSON, or JSON annotated with JsonUtility. You can use the latter to convert the argument to a concrete Unity object that supports [JsonUtility.FromJson](JsonUtility.FromJson.html).  
  
### Description

Sends a request to all connected clients on the "events" channel.

Any client can attempt fulfill the request but only the first client that
acknowledges the request can actually fulfill it.

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

