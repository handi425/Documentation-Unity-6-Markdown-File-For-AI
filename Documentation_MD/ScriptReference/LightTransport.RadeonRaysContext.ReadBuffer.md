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

#  [RadeonRaysContext](LightTransport.RadeonRaysContext.html).ReadBuffer

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

public void ReadBuffer(BufferSlice<T> src, NativeArray<T> dst);

## Declaration

public void ReadBuffer(BufferSlice<T> src, NativeArray<T> dst,
[LightTransport.EventID](LightTransport.EventID.html) id);

### Parameters

src | The buffer slice to read from.  
---|---  
dst | The array in the CPU memory that the contents of the buffer should be written to. The array must remain valid until the read operation is complete. Related content: [IDeviceContext.Wait](LightTransport.IDeviceContext.Wait.html).  
id | The ID of the event to use to track completion of the read.  
  
### Description

Read contents of a buffer from the context.

The memory that the [BufferSlice<T0>](LightTransport.BufferSlice_1.html)
points to can be transferred into a
[NativeArray<T0>](Unity.Collections.NativeArray_1.html). This is an
asynchronous operation. Pass an [EventID](LightTransport.EventID.html) created
with
[IDeviceContext.CreateEvent](LightTransport.IDeviceContext.CreateEvent.html)
to track the completion status, if desired. This method returns immediately
after enqueuing the command in the context.  
  
**Note:** [EventID](LightTransport.EventID.html) is single-use. Once an
[EventID](LightTransport.EventID.html) has been passed to this function, it
may not be passed to subsequent
[IDeviceContext.WriteBuffer](LightTransport.IDeviceContext.WriteBuffer.html)
or [IDeviceContext.ReadBuffer](LightTransport.IDeviceContext.ReadBuffer.html)
calls. Doing so will result in undefined behavior.

    
    
              [IDeviceContext](LightTransport.IDeviceContext.html) ctx = new [RadeonRaysContext](LightTransport.RadeonRaysContext.html)();
    ctx.Initialize();
    uint length = 8;
    var input = new NativeArray<byte>((int)length, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
    for (int i = 0; i < length; ++i)
        input[i] = (byte)i;
    var output = new NativeArray<byte>((int)length, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
    [BufferID](LightTransport.BufferID.html) id = ctx.CreateBuffer(8);
    var writeEvent = ctx.CreateEvent();
    ctx.WriteBuffer(id.Slice<byte>(), input, writeEvent);
    var readEvent = ctx.CreateEvent();
    ctx.ReadBuffer(id.Slice<byte>(), output, readEvent);
    bool flushOk = ctx.Flush();
    [Assert.IsTrue](Assertions.Assert.IsTrue.html)(flushOk);
    bool eventOk = ctx.Wait(writeEvent);
    [Assert.IsTrue](Assertions.Assert.IsTrue.html)(eventOk);  
      
    // Contents of the buffer is now available in the CPU side memory array output.  
      
    input.Dispose();
    [Assert.IsTrue](Assertions.Assert.IsTrue.html)(ctx.IsCompleted(readEvent));
    ctx.DestroyEvent(readEvent);
    ctx.DestroyEvent(writeEvent);
    ctx.DestroyBuffer(id);
    for (int i = 0; i < length; ++i)
        [Assert.AreEqual](Assertions.Assert.AreEqual.html)((byte)i, output[i]);
    output.Dispose();
    ctx.Dispose();

How to read back a buffer.

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

