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

# Awaitable

class in UnityEngine

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

Custom Unity type that can be awaited and used as an async return type in the
C# asynchronous programming model.

`Awaitable` is usually a preferable alternative to .NET `Task` for
asynchronous code in Unity. It's important, however, to know the differences
between the two. Most notably, instances of the `Awaitable` class are pooled
and therefore not safe to `await` multiple times in the same method.  
  
For more information, refer to [Asynchronous programming with the Awaitable
class](../Manual/async-await-support.html) in the Manual.

    
    
    private async [Awaitable](Awaitable.html) DoSomethingAsync()
    {
       await LoadSceneAsync("SomeScene");
       await SomeApiReturningATask();
       await [Awaitable.NextFrameAsync](Awaitable.NextFrameAsync.html)();
       // <...>
    }
    

### Properties

[IsCompleted](Awaitable.IsCompleted.html)| Indicates if the awaitable has run
to completion.  
---|---  
  
### Public Methods

[Cancel](Awaitable.Cancel.html)| Cancels the awaitable. If the awaitable is
being awaited, the awaiter receives a System.OperationCanceledException.  
---|---  
  
### Static Methods

[BackgroundThreadAsync](Awaitable.BackgroundThreadAsync.html)| Resumes
execution on a ThreadPool background thread. Completes immediately when called
from a background thread.  
---|---  
[EndOfFrameAsync](Awaitable.EndOfFrameAsync.html)| Resumes execution after all
Unity subsystems have run for the current frame.  
[FixedUpdateAsync](Awaitable.FixedUpdateAsync.html)| Resumes execution on the
next fixed update frame.  
[FromAsyncOperation](Awaitable.FromAsyncOperation.html)| Creates an Awaitable
from an existing AsyncOperation object.  
[MainThreadAsync](Awaitable.MainThreadAsync.html)| Resumes execution on the
Unity main thread. Completes immediately when called from the main thread.  
[NextFrameAsync](Awaitable.NextFrameAsync.html)| Resumes execution on the next
frame.  
[WaitForSecondsAsync](Awaitable.WaitForSecondsAsync.html)| Resumes execution
after the specified number of seconds.  
  
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

