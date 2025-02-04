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
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html).GetFileInfo

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

public static
[Unity.IO.LowLevel.Unsafe.ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html)
GetFileInfo(string filename, FileInfoResult* result);

### Parameters

filename | The name of the file to query.  
---|---  
result | A struct that this function fills in with information about the file upon completion of this asynchronous request.  
  
### Returns

**ReadHandle** A read handle that you can use to monitor the progress and
status of this GetFileInfo command.

### Description

Gets information about a file.

This function gets information about the specified file asynchronously without
opening the file. On completion of the asynchronous operation, the `result`
parameter's
[FileInfoResult.FileState](Unity.IO.LowLevel.Unsafe.FileInfoResult.FileState.html)
member reports whether the file exists
([FileState.Exists](Unity.IO.LowLevel.Unsafe.FileState.Exists.html)) or not
([FileState.Absent](Unity.IO.LowLevel.Unsafe.FileState.Absent.html)). If the
file exists, the `result` parameter's
[FileInfoResult.FileSize](Unity.IO.LowLevel.Unsafe.FileInfoResult.FileSize.html)
member reports the size of the file in bytes. If the file is absent, the size
is reported as zero.

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

