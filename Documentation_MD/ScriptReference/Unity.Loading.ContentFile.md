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

# ContentFile

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

This struct acts like a handle for accessing a file loaded by
[ContentLoadInterface.LoadContentFileAsync](Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html).
You can use it to access the status and results of the load operation.

### Static Properties

[GlobalTableDependency](Unity.Loading.ContentFile.GlobalTableDependency.html)|
This ContentFile can be passed as a dependency to
ContentLoadInterface.LoadContentFileAsync or
ContentLoadInterface.LoadSceneAsync to indicate that the external file
dependencies should be resolved through the global PersistentManager table.
For example, this could be used when the ContentFile references a file loaded
through the PersistentManager such as "unity default resources".  
---|---  
  
### Properties

[IsValid](Unity.Loading.ContentFile.IsValid.html)| Returns true if the
ContentFile handle is valid.  
---|---  
[LoadingStatus](Unity.Loading.ContentFile.LoadingStatus.html)| The loading
status of the ContentFile.  
  
### Public Methods

[GetObject](Unity.Loading.ContentFile.GetObject.html)| Used to access objects
within the ContentFile by local file identifier.  
---|---  
[GetObjects](Unity.Loading.ContentFile.GetObjects.html)| This function can be
used to access all the Objects loaded in the ContentFile.  
[UnloadAsync](Unity.Loading.ContentFile.UnloadAsync.html)| Begin an
asynchronous unload of the ContentFile.  
[WaitForCompletion](Unity.Loading.ContentFile.WaitForCompletion.html)| Blocks
on the main thread until the load operation completes. This function can be
slow and so should be used carefully to avoid frame rate stuttering.  
  
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

