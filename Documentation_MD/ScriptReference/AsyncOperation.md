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

# AsyncOperation

class in UnityEngine

/

Inherits from:[YieldInstruction](YieldInstruction.html)

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

Asynchronous operation coroutine.

You can **yield** until asynchronous operation continues, or manually check
whether it's done ([isDone](AsyncOperation-isDone.html)) or progress
([progress](AsyncOperation-progress.html)).  
  
Additional resources:
[SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html),
[AssetBundle.LoadAssetAsync](AssetBundle.LoadAssetAsync.html),
[Resources.LoadAsync](Resources.LoadAsync.html).

### Properties

[allowSceneActivation](AsyncOperation-allowSceneActivation.html)| Allow Scenes
to be activated as soon as it is ready.  
---|---  
[isDone](AsyncOperation-isDone.html)| Has the operation finished? (Read Only)  
[priority](AsyncOperation-priority.html)| Priority lets you tweak in which
order async operation calls will be performed.  
[progress](AsyncOperation-progress.html)| What's the operation's progress.
(Read Only)  
  
### Events

[completed](AsyncOperation-completed.html)| Event that is invoked upon
operation completion. An event handler that is registered in the same frame as
the call that creates it will be invoked next frame, even if the operation is
able to complete synchronously. If a handler is registered after the operation
has completed and has already invoked the complete event, the handler will be
called synchronously.  
---|---  
  
### Inherited Members

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

