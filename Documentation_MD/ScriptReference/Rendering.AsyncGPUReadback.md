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

# AsyncGPUReadback

class in UnityEngine.Rendering

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

Allows the asynchronous read back of GPU resources.

This class is used to copy resource data from the GPU to the CPU without any
stall (GPU or CPU), but adds a few frames of latency. Additional resources:
[AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html).  
  
Additional resources: [SystemInfo.supportsAsyncGPUReadback](SystemInfo-
supportsAsyncGPUReadback.html),
[SystemInfo.supportsAsyncGPUReadback](Device.SystemInfo-
supportsAsyncGPUReadback.html).

### Static Methods

[Request](Rendering.AsyncGPUReadback.Request.html)| Retrieves data
asynchronously from a GPU resource.  
---|---  
[RequestAsync](Rendering.AsyncGPUReadback.RequestAsync.html)| Retrieves data
asynchronously from a GPU resource.  
[RequestIntoNativeArray](Rendering.AsyncGPUReadback.RequestIntoNativeArray.html)|
Retrieves data asynchronously from a GPU Texture resource.  
[RequestIntoNativeArrayAsync](Rendering.AsyncGPUReadback.RequestIntoNativeArrayAsync.html)|
Retrieves data asynchronously from a GPU Texture resource.  
[RequestIntoNativeSlice](Rendering.AsyncGPUReadback.RequestIntoNativeSlice.html)|
Retrieves data asynchronously from a GPU Texture resource.  
[RequestIntoNativeSliceAsync](Rendering.AsyncGPUReadback.RequestIntoNativeSliceAsync.html)|
Retrieves data asynchronously from a GPU Texture resource.  
[WaitAllRequests](Rendering.AsyncGPUReadback.WaitAllRequests.html)| Waits
until the completion of every request.  
  
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

