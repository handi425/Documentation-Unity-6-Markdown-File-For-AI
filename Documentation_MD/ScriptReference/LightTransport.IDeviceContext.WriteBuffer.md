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

#  [IDeviceContext](LightTransport.IDeviceContext.html).WriteBuffer

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

public void WriteBuffer(BufferSlice<T> dst, NativeArray<T> src);

## Declaration

public void WriteBuffer(BufferSlice<T> dst, NativeArray<T> src,
[LightTransport.EventID](LightTransport.EventID.html) id);

### Parameters

dst | The buffer slice to write to.  
---|---  
src | The array in the CPU memory that should be written to the buffer. The array must remain valid until the write operation is complete.  
id | The ID of the event to use to track completion of the write.  
  
### Description

Write data into the memory buffer allocated by the context.

This is an asynchronous operation. Pass an
[EventID](LightTransport.EventID.html) created with
[IDeviceContext.CreateEvent](LightTransport.IDeviceContext.CreateEvent.html)
to track the completion status, if desired. The
[IDeviceContext.WriteBuffer](LightTransport.IDeviceContext.WriteBuffer.html)
method returns immediately after enqueuing the command in the context.  
  
**Note:** [EventID](LightTransport.EventID.html) is single-use. Once an
[EventID](LightTransport.EventID.html) has been passed to this function, it
may not be passed to subsequent
[IDeviceContext.WriteBuffer](LightTransport.IDeviceContext.WriteBuffer.html)
or [IDeviceContext.ReadBuffer](LightTransport.IDeviceContext.ReadBuffer.html)
calls. Doing so will result in undefined behavior.

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

