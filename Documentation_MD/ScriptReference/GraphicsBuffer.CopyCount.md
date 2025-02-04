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

#  [GraphicsBuffer](GraphicsBuffer.html).CopyCount

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

## Declaration

public static void CopyCount([GraphicsBuffer](GraphicsBuffer.html) src,
[ComputeBuffer](ComputeBuffer.html) dst, int dstOffsetBytes);

## Declaration

public static void CopyCount([ComputeBuffer](ComputeBuffer.html) src,
[GraphicsBuffer](GraphicsBuffer.html) dst, int dstOffsetBytes);

## Declaration

public static void CopyCount([GraphicsBuffer](GraphicsBuffer.html) src,
[GraphicsBuffer](GraphicsBuffer.html) dst, int dstOffsetBytes);

### Parameters

src | The source GraphicsBuffer.  
---|---  
dst | The destination GraphicsBuffer.  
dstOffsetBytes | The destination buffer offset in bytes.  
  
### Description

Copy the counter value of a GraphicsBuffer into another buffer.

Append/consume buffers (see
[GraphicsBuffer.Target.Append](GraphicsBuffer.Target.Append.html) and counter
buffers [GraphicsBuffer.Target.Counter](GraphicsBuffer.Target.Counter.html))
keep track of the number of elements in them with a special counter variable.
CopyCount takes such a buffer as `src`, and copies its counter value into
`dst` buffer at given byte offset.  
  
This is most commonly used in conjunction with
[Graphics.RenderPrimitivesIndirect](Graphics.RenderPrimitivesIndirect.html),
to render an arbitrary number of primitives without reading their count back
to the CPU.  
  
The `src` buffer must have been created with a usage target of
[GraphicsBuffer.Target.Append](GraphicsBuffer.Target.Append.html) or
[GraphicsBuffer.Target.Counter](GraphicsBuffer.Target.Counter.html).  
  
On DirectX 11 and 12, the `dst` buffer must have been created with a usage
target of [GraphicsBuffer.Target.Raw](GraphicsBuffer.Target.Raw.html) or
[GraphicsBuffer.Target.IndirectArguments](GraphicsBuffer.Target.IndirectArguments.html).
For other graphics APIs, there is no such restriction.  
  
Additional resources: [SetCounterValue](GraphicsBuffer.SetCounterValue.html).

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

