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

#  [ComputeBuffer](ComputeBuffer.html).CopyCount

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

public static void CopyCount([ComputeBuffer](ComputeBuffer.html) src,
[ComputeBuffer](ComputeBuffer.html) dst, int dstOffsetBytes);

### Parameters

src | Append/consume buffer to copy the counter from.  
---|---  
dst | A buffer to copy the counter to.  
dstOffsetBytes | Target byte offset in `dst`.  
  
### Description

Copy counter value of append/consume buffer into another buffer.

Append/consume and counter buffers (see
[ComputeBufferType.Append](ComputeBufferType.Append.html),
[ComputeBufferType.Counter](ComputeBufferType.Counter.html)) keep track of the
number of elements in them with a special counter variable. CopyCount takes a
buffer as `src`, and copies its counter value into `dst` buffer at given byte
offset.  
  
This is most commonly used in conjunction with
[Graphics.DrawProceduralIndirect](Graphics.DrawProceduralIndirect.html), to
render arbitrary number of primitives without reading their count back to the
CPU.  
  
On DX11 there is a restriction on the `dst` buffer - it must have been created
with [ComputeBufferType.Raw](ComputeBufferType.Raw.html) or
[ComputeBufferType.IndirectArguments](ComputeBufferType.IndirectArguments.html)
type. On other platforms `dst` can be any type.  
  
Additional resources: [SetCounterValue](ComputeBuffer.SetCounterValue.html).

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

