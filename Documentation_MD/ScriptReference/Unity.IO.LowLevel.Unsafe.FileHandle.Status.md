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

#  [FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html).Status

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

public
[Unity.IO.LowLevel.Unsafe.FileStatus](Unity.IO.LowLevel.Unsafe.FileStatus.html)
Status;

### Description

The current status of this FileHandle.

After you call
[AsyncReadManager.OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html),
the FileHandle enters the
[FileStatus.Pending](Unity.IO.LowLevel.Unsafe.FileStatus.Pending.html) state.
Once the open operation completes, the status changes to either
[FileStatus.Open](Unity.IO.LowLevel.Unsafe.FileStatus.Open.html) or
[FileStatus.Closed](Unity.IO.LowLevel.Unsafe.FileStatus.Closed.html) (if the
file failed to open).  
  
Note: When the close operation completes, the FileHandle is disposed and
becomes invalid. You can use the JobHandle returned by
[Close](Unity.IO.LowLevel.Unsafe.FileHandle.Close.html) to check for close
operation completion.

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

