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
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html).CloseCachedFileAsync

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

public static [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
CloseCachedFileAsync(string fileName,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) dependency);

### Parameters

fileName | The path to the file to close.  
---|---  
dependency | (Optional) A JobHandle to wait on before performing the close.  
  
### Returns

**JobHandle** A JobHandle that completes when the asynchronous close operation
finishes.

### Description

Closes a file held open internally by the AsyncReadManager.

The AsyncReadManager has an internal cache of up to 10 open files, so use this
method if you experience a sharing violation when trying to access one of
these files that is held open.  
  
Note: Do not use this method for files opened with
[OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html),
as these files do not go into the AsyncReadManager's file cache. Use
[FileHandle.Close](Unity.IO.LowLevel.Unsafe.FileHandle.Close.html) instead.

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

