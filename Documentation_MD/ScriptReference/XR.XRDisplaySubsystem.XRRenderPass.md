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

# XRRenderPass

struct in UnityEngine.XR

/

Implemented in:[UnityEngine.XRModule](UnityEngine.XRModule.html)

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

Contains configuration parameters about which view into the Scene the renderer
should rasterize, and a render target (which can be a texture array) for the
result of the rasterization.

An XRRenderPass can contain more than one
[XRRenderParameter](XR.XRDisplaySubsystem.XRRenderParameter.html) (viewpoints
that the render pipeline renders to the output texture as either different
viewports or texture array slices). The render pipeline must query each child
[XRRenderParameter](XR.XRDisplaySubsystem.XRRenderParameter.html) via
[GetRenderParameter](XR.XRDisplaySubsystem.XRRenderPass.GetRenderParameter.html).
The most optimal way to implement an XRRenderPass is to cull first, and then
submit draw calls once for the resulting objects. You can also use techniques
such as instanced rendering to optimize XRRenderPasses that contain more than
one [XRRenderParameter](XR.XRDisplaySubsystem.XRRenderParameter.html).  
  
XRRenderPass is typically consumed by a scriptable rendering pipeline.

### Properties

[cullingPassIndex](XR.XRDisplaySubsystem.XRRenderPass-cullingPassIndex.html)|
An index that a render pipeline can pass to
XRDisplaySubsystem.GetCullingParameters to obtain culling information.  
---|---  
[foveatedRenderingInfo](XR.XRDisplaySubsystem.XRRenderPass-
foveatedRenderingInfo.html)| A pointer to a native struct containing platform-
specific data for foveated rendering.  
[hasMotionVectorPass](XR.XRDisplaySubsystem.XRRenderPass-
hasMotionVectorPass.html)| A boolean indicating if this render pass contains a
motion-vector generation pass.  
[motionVectorRenderTarget](XR.XRDisplaySubsystem.XRRenderPass-
motionVectorRenderTarget.html)| The output render-texture target for the
motion-vector generation render pass.  
[motionVectorRenderTargetDesc](XR.XRDisplaySubsystem.XRRenderPass-
motionVectorRenderTargetDesc.html)| The render texture description for the
target texture for the motion-vector render pass.  
[renderPassIndex](XR.XRDisplaySubsystem.XRRenderPass-renderPassIndex.html)|
The index of the render pass (originally passed in to
XRDisplaySubsystem.GetRenderPass).  
[renderTarget](XR.XRDisplaySubsystem.XRRenderPass-renderTarget.html)| The
output target for the render pass.  
[renderTargetDesc](XR.XRDisplaySubsystem.XRRenderPass-renderTargetDesc.html)|
Descriptor that can be passed to RenderTexture.GetTemporary to create
temporary textures that match the XR Display render target.  
[shouldFillOutDepth](XR.XRDisplaySubsystem.XRRenderPass-
shouldFillOutDepth.html)| When this is false an optimal renderer can avoid
resolving the depth buffer.  
  
### Public Methods

[GetRenderParameter](XR.XRDisplaySubsystem.XRRenderPass.GetRenderParameter.html)|
Gets an XRRenderParameter for a specific XRRenderPass.  
---|---  
[GetRenderParameterCount](XR.XRDisplaySubsystem.XRRenderPass.GetRenderParameterCount.html)|
The number of XRRenderParameter entries for this XRRenderPass.  
  
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

