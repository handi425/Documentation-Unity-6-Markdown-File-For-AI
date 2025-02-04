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

# RenderTargetBinding

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

Describes a render target with one or more color buffers, a depth/stencil
buffer and the associated load/store-actions that are applied when the render
target is active.

This data structure is similiar to
[RenderTargetSetup](RenderTargetSetup.html), but relies on a
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html) to ensure
compatability with
[CommandBuffer.SetRenderTarget](Rendering.CommandBuffer.SetRenderTarget.html).  
  
To render to a specific mipmap level, cubemap face or depth slice the
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html) should be
created accordingly.  
  
Note: the number of load- and store-actions specified for color buffers must
be equal to the number of color buffers.  
  
Additional resources: [CommandBuffer](Rendering.CommandBuffer.html).

### Properties

[colorLoadActions](Rendering.RenderTargetBinding-colorLoadActions.html)| Load
actions for color buffers.  
---|---  
[colorRenderTargets](Rendering.RenderTargetBinding-colorRenderTargets.html)|
Color buffers to use as render targets.  
[colorStoreActions](Rendering.RenderTargetBinding-colorStoreActions.html)|
Store actions for color buffers.  
[depthLoadAction](Rendering.RenderTargetBinding-depthLoadAction.html)| Load
action for the depth/stencil buffer.  
[depthRenderTarget](Rendering.RenderTargetBinding-depthRenderTarget.html)|
Depth/stencil buffer to use as render target.  
[depthStoreAction](Rendering.RenderTargetBinding-depthStoreAction.html)| Store
action for the depth/stencil buffer.  
[flags](Rendering.RenderTargetBinding-flags.html)| Optional flags.  
  
### Constructors

[RenderTargetBinding](Rendering.RenderTargetBinding-ctor.html)| Constructs
RenderTargetBinding.  
---|---  
  
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

