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

#  [ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html).GetBytesReadArray

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

public ulong* GetBytesReadArray();

### Returns

**ulong*** An unsafe pointer to the array storing the number of bytes read for
each ReadCommand in the request.

### Description

Returns an array containing the number of bytes read by the
[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) operations during the
asynchronous file read request, where each index corresponds to the
ReadCommand index.

It is not safe to retain the pointer after the ReadHandle has been disposed,
as it will have been freed internally.  
  
The number of entries in the array is equal to
[ReadHandle.ReadCount](Unity.IO.LowLevel.Unsafe.ReadHandle.ReadCount.html), so
this can be used to find the maximum size of the array. This field (and the
array itself) is resized at the start of the read.  
  
A truncated read occurs when the
[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) describing the read
operation specifies a
[ReadCommand.Size](Unity.IO.LowLevel.Unsafe.ReadCommand.Size.html) and
[ReadCommand.Offset](Unity.IO.LowLevel.Unsafe.ReadCommand.Offset.html) that
extends past the end of the target file.

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

