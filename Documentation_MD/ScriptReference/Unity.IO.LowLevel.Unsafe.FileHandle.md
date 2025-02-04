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

# FileHandle

struct in Unity.IO.LowLevel.Unsafe

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

A handle to an asynchronously opened file.

Opening a file with
[AsyncReadManager.OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html)
returns a FileHandle instance. You can use this handle to check the status of
the asynchronous open operation.  
  
Use
[AsyncReadManager.Read](Unity.IO.LowLevel.Unsafe.AsyncReadManager.Read.html)
to read the data in the file after the open operation is complete. This will
automatically wait for the open operation to complete, and give the ReadHandle
a WaitingOnJob ReadStatus while it does so. If using
[AsyncReadManager.ReadDeferred](Unity.IO.LowLevel.Unsafe.AsyncReadManager.ReadDeferred.html)
instead, you should make sure that the passed in JobHandle waits on this
[JobHandle](Unity.IO.LowLevel.Unsafe.FileHandle.JobHandle.html) to schedule
the read job after the open operation finishes.  
  
Always call [Close](Unity.IO.LowLevel.Unsafe.FileHandle.Close.html) on the
FileHandle when finished to avoid memory leaks and holding a file open. You
must call close even if the open operation failed, to dispose of the
FileHandle.  
  
To write to a file, use the standard .NET File APIs, such as
System.IO.StreamWriter. You must close this FileHandle before you can read or
write to the file with other APIs. (If a file is held open by the
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html)'s file
cache, you can use
[AsyncReadManager.CloseCachedFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.CloseCachedFileAsync.html)
to close it, but do not use that API to close files for which you have a
FileHandle as these are not in the cache.)

### Properties

[JobHandle](Unity.IO.LowLevel.Unsafe.FileHandle.JobHandle.html)| The JobHandle
of the asynchronous file open operation begun by the call to
AsyncReadManager.OpenFileAsync that returned this FileHandle instance.  
---|---  
[Status](Unity.IO.LowLevel.Unsafe.FileHandle.Status.html)| The current status
of this FileHandle.  
  
### Public Methods

[Close](Unity.IO.LowLevel.Unsafe.FileHandle.Close.html)| Asynchronously closes
the file referenced by this FileHandle and disposes the FileHandle instance.  
---|---  
[IsValid](Unity.IO.LowLevel.Unsafe.FileHandle.IsValid.html)| Reports whether
this FileHandle instance is valid.  
  
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

