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

#  [RadeonRaysContext](LightTransport.RadeonRaysContext.html).Wait

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

public bool Wait([LightTransport.EventID](LightTransport.EventID.html) id);

### Parameters

id | ID of the event.  
---|---  
  
### Returns

**bool** Returns true of the event completed successfully.

### Description

Wait for an asynchronous event.

This is a blocking method which stalls the current CPU thread until the
operation represented by the EventID is complete. Adding a stall can have a
significant performance impact during regular execution. To avoid stalls, call
[IDeviceContext.Wait](LightTransport.IDeviceContext.Wait.html) at the end of
your sequence of operations.

    
    
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
      
    // The event has completed.  
      
    input.Dispose();
    [Assert.IsTrue](Assertions.Assert.IsTrue.html)(ctx.IsCompleted(readEvent));
    ctx.DestroyEvent(readEvent);
    ctx.DestroyEvent(writeEvent);
    ctx.DestroyBuffer(id);
    for (int i = 0; i < length; ++i)
        [Assert.AreEqual](Assertions.Assert.AreEqual.html)((byte)i, output[i]);
    output.Dispose();
    ctx.Dispose();

How to use Wait.

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

