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

# ReadHandle

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

You can use this handle to query the status of an asynchronous read operation.
Note: To avoid a memory leak, you must call Dispose.

### Properties

[JobHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.JobHandle.html)| JobHandle
that completes when the read operation completes.  
---|---  
[ReadCount](Unity.IO.LowLevel.Unsafe.ReadHandle.ReadCount.html)| The number of
read commands performed for this read operation. Will return zero until the
reads have begun.  
[Status](Unity.IO.LowLevel.Unsafe.ReadHandle.Status.html)| Current state of
the read operation.  
  
### Public Methods

[Cancel](Unity.IO.LowLevel.Unsafe.ReadHandle.Cancel.html)| Cancels the
AsyncReadManager.Read operation on this handle.  
---|---  
[Dispose](Unity.IO.LowLevel.Unsafe.ReadHandle.Dispose.html)| Disposes the
ReadHandle. Use this to free up internal resources for reuse.  
[GetBytesRead](Unity.IO.LowLevel.Unsafe.ReadHandle.GetBytesRead.html)| Returns
the total number of bytes read by all the ReadCommand operations the
asynchronous file read request.  
[GetBytesReadArray](Unity.IO.LowLevel.Unsafe.ReadHandle.GetBytesReadArray.html)|
Returns an array containing the number of bytes read by the ReadCommand
operations during the asynchronous file read request, where each index
corresponds to the ReadCommand index.  
[IsValid](Unity.IO.LowLevel.Unsafe.ReadHandle.IsValid.html)| Check if the
ReadHandle is valid.  
  
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

