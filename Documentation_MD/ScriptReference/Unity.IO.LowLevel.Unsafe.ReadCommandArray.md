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

# ReadCommandArray

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

An array of [ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) instances
to pass to
[AsyncReadManager.Read](Unity.IO.LowLevel.Unsafe.AsyncReadManager.Read.html)
and
[AsyncReadManager.ReadDeferred](Unity.IO.LowLevel.Unsafe.AsyncReadManager.ReadDeferred.html).

To create a ReadCommandArray object, use
[UnsafeUtility.Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)
to allocate an array of ReadCommands (or allocate a NativeArray) and populate
it with the commands to perform. You must set
[CommandCount](Unity.IO.LowLevel.Unsafe.ReadCommandArray.CommandCount.html) to
the number of commands in the array. Failure to do so is dangerous and could
lead to buffer overruns or skipping the read commands at the end.

### Properties

[CommandCount](Unity.IO.LowLevel.Unsafe.ReadCommandArray.CommandCount.html)|
The number of individual entries in the array of ReadCommands pointed to by
ReadCommands.  
---|---  
[ReadCommands](Unity.IO.LowLevel.Unsafe.ReadCommandArray.ReadCommands.html)|
Pointer to a NativeArray of ReadCommands.  
  
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

