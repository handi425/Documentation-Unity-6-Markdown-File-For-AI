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

#
[GraphicsBuffer.UsageFlags](GraphicsBuffer.UsageFlags.html).LockBufferForWrite

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

### Description

Enable the LockBufferForWrite and UnlockBufferAfterWrite methods on the
GraphicsBuffer. CAUTION: when using this flag, ensure that you do not
introduce memory read/write hazards.

With this flag, the buffer can be updated at any time using
[GraphicsBuffer.SetData](GraphicsBuffer.SetData.html) and equivalent functions
that write data from the CPU.  
The GPU can only read from the buffer, including using it as a copy source. No
writes from the GPU are allowed, including using the GPU as a copy destination
or a UAV. This means that when using
[GraphicsBuffer.Target.Raw](GraphicsBuffer.Target.Raw.html), for example, you
can use `ByteAddressBuffer` but not `RWByteAddressBuffer` in an HLSL shader.
Using `RWByteAddressBuffer` allows writes into the buffer.  
The buffer can be written to directly from the CPU using
[GraphicsBuffer.LockBufferForWrite](GraphicsBuffer.LockBufferForWrite.html).
For more information, see
[GraphicsBuffer.LockBufferForWrite](GraphicsBuffer.LockBufferForWrite.html).  
This mode might place the buffer in the CPU visible GPU memory or in GPU
visible CPU memory depending on a platform.  
Additional resources: [GraphicsBuffer](GraphicsBuffer.html)
[GraphicsBuffer.LockBufferForWrite](GraphicsBuffer.LockBufferForWrite.html).

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

