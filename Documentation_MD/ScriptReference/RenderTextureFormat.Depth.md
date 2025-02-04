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

#  [RenderTextureFormat](RenderTextureFormat.html).Depth

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

A depth render texture format.

Depth format is used to render high precision "depth" value into a render
texture. Which format is actually used depends on platform support and on the
number of depth bits you request through the constructor.  
  
You can also set an exact depth-stencil format with
[RenderTexture.depthStencilFormat](RenderTexture-depthStencilFormat.html) or a
[RenderTexture](RenderTexture.html) constructor that takes
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html). Use
[SystemInfo.IsFormatSupported](SystemInfo.IsFormatSupported.html) to check
your platform supports this.  
  
When writing shaders that use or render into a depth texture, care must be
taken to ensure that they work both on OpenGL and on Direct3D, see [depth
textures documentation](../Manual/SL-CameraDepthTexture.html).  
  
Note that not all graphics cards support depth textures. Use
[SystemInfo.SupportsRenderTextureFormat](SystemInfo.SupportsRenderTextureFormat.html)
to check for support.  
  
Additional resources: [RenderTexture](RenderTexture.html) class,
[SystemInfo.SupportsRenderTextureFormat](SystemInfo.SupportsRenderTextureFormat.html).

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

