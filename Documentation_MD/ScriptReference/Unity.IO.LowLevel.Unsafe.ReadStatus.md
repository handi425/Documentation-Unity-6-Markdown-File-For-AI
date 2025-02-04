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

# ReadStatus

enumeration

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

The state of an asynchronous file request.

These enumerations represent the raw underlying states of an asynchronous file
request.  
  
When submitted, all requests enter the
[ReadStatus.InProgress](Unity.IO.LowLevel.Unsafe.ReadStatus.InProgress.html)
state while they are pending execution or in progress. On completion, the
state changes to
[ReadStatus.Complete](Unity.IO.LowLevel.Unsafe.ReadStatus.Complete.html),
[ReadStatus.Truncated](Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html) or
[ReadStatus.Failed](Unity.IO.LowLevel.Unsafe.ReadStatus.Failed.html). If the
read is canceled before completion, the state becomes
[ReadStatus.Canceled](Unity.IO.LowLevel.Unsafe.ReadStatus.Canceled.html).  
  
A truncated read occurs when attempting to access beyond the end of a file.

### Properties

[Complete](Unity.IO.LowLevel.Unsafe.ReadStatus.Complete.html)| The
asynchronous file request completed successfully and all read operations
within it were completed in full.  
---|---  
[InProgress](Unity.IO.LowLevel.Unsafe.ReadStatus.InProgress.html)| The
asynchronous file request is in progress.  
[Failed](Unity.IO.LowLevel.Unsafe.ReadStatus.Failed.html)| One or more of the
asynchronous file request's read operations have failed.  
[Truncated](Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html)| The
asynchronous file request has completed but one or more of the read operations
were truncated.  
[Canceled](Unity.IO.LowLevel.Unsafe.ReadStatus.Canceled.html)| The
asynchronous file request was canceled before the read operations were
completed.  
  
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

