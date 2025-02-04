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

#  [ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html).GetBytesRead

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

public long GetBytesRead();

### Returns

**long** The total number of bytes read by the asynchronous file read request.

### Description

Returns the total number of bytes read by all the
[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) operations the
asynchronous file read request.

This may not be equal to the sum of all the requested
[ReadCommand.Size](Unity.IO.LowLevel.Unsafe.ReadCommand.Size.html) fields in
the case of a
[ReadStatus.Failed](Unity.IO.LowLevel.Unsafe.ReadStatus.Failed.html) error or
a [ReadStatus.Truncated](Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html)
status.  
  
A truncated read occurs when the
[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) describing the read
operation specifies a
[ReadCommand.Size](Unity.IO.LowLevel.Unsafe.ReadCommand.Size.html) and
[ReadCommand.Offset](Unity.IO.LowLevel.Unsafe.ReadCommand.Offset.html) that
extends past the end of the target file.

* * *

## Declaration

public long GetBytesRead(uint readCommandIndex);

### Parameters

readCommandIndex | The index of the [ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) for which to retrieve the number of bytes read.  
---|---  
  
### Returns

**long** The number of bytes read for the specified
[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html).

### Description

Returns the total number of bytes read for a specific
[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) index.

This may not be equal the requested
[ReadCommand.Size](Unity.IO.LowLevel.Unsafe.ReadCommand.Size.html) fields in
the case of a
[ReadStatus.Failed](Unity.IO.LowLevel.Unsafe.ReadStatus.Failed.html) error or
a [ReadStatus.Truncated](Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html)
status.  
  
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

