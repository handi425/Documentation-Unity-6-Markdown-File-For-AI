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

# ContentSceneFile

struct in Unity.Loading

/

Implemented
in:[UnityEngine.ContentLoadModule](UnityEngine.ContentLoadModule.html)

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

The handle returned from
[ContentLoadInterface.LoadSceneAsync](Unity.Loading.ContentLoadInterface.LoadSceneAsync.html).
You can use this handle to access the status and results of the load
operation.

### Properties

[IsValid](Unity.Loading.ContentSceneFile.IsValid.html)| Returns true if the
ContentSceneFile handle is valid. A handle becomes invalid after the file is
unloaded.  
---|---  
[Scene](Unity.Loading.ContentSceneFile.Scene.html)| The Scene object being
loaded. This is accessible both before and after the load operation completes.  
[Status](Unity.Loading.ContentSceneFile.Status.html)| The loading status of
the scene.  
  
### Public Methods

[IntegrateAtEndOfFrame](Unity.Loading.ContentSceneFile.IntegrateAtEndOfFrame.html)|
Calling this will cause the scene to integrate at the end of the frame.  
---|---  
[UnloadAtEndOfFrame](Unity.Loading.ContentSceneFile.UnloadAtEndOfFrame.html)|
Will trigger the scene to unload at the end of the frame.  
[WaitForLoadCompletion](Unity.Loading.ContentSceneFile.WaitForLoadCompletion.html)|
Blocks on the main thread until the load operation completes. This function
can be slow and so should be used carefully to avoid frame rate stuttering.  
  
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

