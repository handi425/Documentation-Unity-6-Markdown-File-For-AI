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

# AsyncGPUReadbackRequest

struct in UnityEngine.Rendering

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

Represents an asynchronous request for a GPU resource.

Use [AsyncGPUReadback.Request](Rendering.AsyncGPUReadback.Request.html) to
retrieve an asynchronous request for a GPU resource. Pending requests are
automatically updated each frame. The result is accessible only for a single
frame once is successfully fulfilled and this request is then disposed of in
the following frame. Common uses for this are to query
[AsyncGPUReadbackRequest.done](Rendering.AsyncGPUReadbackRequest-done.html)
each frame (or within a coroutine) and then call
[AsyncGPUReadbackRequest.GetData](Rendering.AsyncGPUReadbackRequest.GetData.html)
if the [AsyncGPUReadbackRequest.hasError](Rendering.AsyncGPUReadbackRequest-
hasError.html) is false. You don't have to manage the request lifetime as this
is managed internally. A request that has been disposed of will result in the
[AsyncGPUReadbackRequest.hasError](Rendering.AsyncGPUReadbackRequest-
hasError.html) property being true. Additional
resources:[AsyncGPUReadback](Rendering.AsyncGPUReadback.html).

### Properties

[depth](Rendering.AsyncGPUReadbackRequest-depth.html)| When reading data from
a ComputeBuffer, depth is 1, otherwise, the property takes the value of the
requested depth from the texture.  
---|---  
[done](Rendering.AsyncGPUReadbackRequest-done.html)| Checks whether the
request has been processed.  
[forcePlayerLoopUpdate](Rendering.AsyncGPUReadbackRequest-
forcePlayerLoopUpdate.html)| In the Editor, defines whether the Player loop is
updated while the GPU request is in flight.  
[hasError](Rendering.AsyncGPUReadbackRequest-hasError.html)| This property is
true if the request has encountered an error.  
[height](Rendering.AsyncGPUReadbackRequest-height.html)| When reading data
from a ComputeBuffer, height is 1, otherwise, the property takes the value of
the requested height from the texture.  
[layerCount](Rendering.AsyncGPUReadbackRequest-layerCount.html)| Number of
layers in the current request.  
[layerDataSize](Rendering.AsyncGPUReadbackRequest-layerDataSize.html)| The
size in bytes of one layer of the readback data.  
[width](Rendering.AsyncGPUReadbackRequest-width.html)| The width of the
requested GPU data.  
  
### Public Methods

[GetData](Rendering.AsyncGPUReadbackRequest.GetData.html)| Fetches the data of
a successful request.  
---|---  
[Update](Rendering.AsyncGPUReadbackRequest.Update.html)| Triggers an update of
the request.  
[WaitForCompletion](Rendering.AsyncGPUReadbackRequest.WaitForCompletion.html)|
Waits for completion of the request.  
  
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

