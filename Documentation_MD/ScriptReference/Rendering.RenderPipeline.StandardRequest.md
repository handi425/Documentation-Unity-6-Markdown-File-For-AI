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

# StandardRequest

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

Standard request type for RenderPipeline.SubmitRenderRequest.

Default render request type. Renders the active render pipeline into the given
destination and specified face, mip and/or slice.  
  
SRP Compatibility:

  * URP: Renders a full URP camera stack. Only works on base cameras. To render a single camera in a stack, use UniversalRenderPipeline.SingleCameraRequest.
  * HDRP: Renders an HDRP camera without [Arbitrary Output Variables](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/AOVs.html) (AOVs).

Refer to [Render requests](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@latest/index.html?subfolder=/manual/User-Render-Requests.html)
for more information about render requests in scriptable render pipelines
(SRPs).  
  
Additional resources:
[RenderPipeline.SubmitRenderRequest](Rendering.RenderPipeline.SubmitRenderRequest.html),
[RenderPipeline.SupportsRenderRequest](Rendering.RenderPipeline.SupportsRenderRequest.html).

### Properties

[destination](Rendering.RenderPipeline.StandardRequest-destination.html)|
RenderTexture to store the rendering result of the request.  
---|---  
[face](Rendering.RenderPipeline.StandardRequest-face.html)| Target Cubemap
face to store the rendering result.  
[mipLevel](Rendering.RenderPipeline.StandardRequest-mipLevel.html)| Target
mipLevel to store the rendering output.  
[slice](Rendering.RenderPipeline.StandardRequest-slice.html)| Target slice to
store the rendering output.  
  
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

