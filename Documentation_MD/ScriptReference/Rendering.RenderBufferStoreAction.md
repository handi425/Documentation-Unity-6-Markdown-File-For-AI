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

# RenderBufferStoreAction

enumeration

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

This enum describes what should be done on the render target when the GPU is
done rendering into it.

When the GPU is done rendering into a render target, this setting specifies
the action that should be performed on the rendering results. Tile-based GPUs
may get performance advantage if the store action is DontCare. For example,
this setting can be useful if the depth buffer contents are not needed after
rendering the frame.  
  
Please note that not all platforms have load/store actions, so this setting
might be ignored at runtime. Generally mobile-oriented graphics APIs (OpenGL
ES, Metal) take advantage of these settings.  
  
If you use `RenderBufferLoadAction.DontCare`, rendering might fail or produce
artefacts because undefined pixels in the [depth texture](../Manual/SL-
CameraDepthTexture.html) cause depth testing to fail. You can use
[LoadStoreActionDebugModeSettings](Rendering.LoadStoreActionDebugModeSettings.html)
to highlight undefined pixels.

### Properties

[Store](Rendering.RenderBufferStoreAction.Store.html)| The RenderBuffer
contents need to be stored to RAM. If the surface has MSAA enabled, this
stores the non-resolved surface.  
---|---  
[Resolve](Rendering.RenderBufferStoreAction.Resolve.html)| Resolve the MSAA
surface.  
[StoreAndResolve](Rendering.RenderBufferStoreAction.StoreAndResolve.html)|
Resolve the MSAA surface, but also store the multisampled version.  
[DontCare](Rendering.RenderBufferStoreAction.DontCare.html)| The contents of
the RenderBuffer are not needed and can be discarded. Tile-based GPUs will
skip writing out the surface contents altogether, providing performance boost.  
  
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

