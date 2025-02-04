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

#  [Graphics](Graphics.html).SetRenderTarget

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

## Declaration

public static void SetRenderTarget([RenderTexture](RenderTexture.html) rt, int
mipLevel = 0, [CubemapFace](CubemapFace.html) face = CubemapFace.Unknown, int
depthSlice = 0);

## Declaration

public static void
SetRenderTarget([Rendering.GraphicsTexture](Rendering.GraphicsTexture.html)
rt, int mipLevel = 0, [CubemapFace](CubemapFace.html) face =
CubemapFace.Unknown, int depthSlice = 0);

## Declaration

public static void SetRenderTarget(RenderBuffer[] colorBuffers,
[RenderBuffer](RenderBuffer.html) depthBuffer);

## Declaration

public static void SetRenderTarget([RenderBuffer](RenderBuffer.html)
colorBuffer, [RenderBuffer](RenderBuffer.html) depthBuffer, int mipLevel = 0,
[CubemapFace](CubemapFace.html) face = CubemapFace.Unknown, int depthSlice =
0);

## Declaration

public static void SetRenderTarget([RenderTargetSetup](RenderTargetSetup.html)
setup);

### Parameters

rt |  [RenderTexture](RenderTexture.html) or [GraphicsTexture](Rendering.GraphicsTexture.html) to set as active render target.  
---|---  
mipLevel | Mipmap level to render into (use 0 if not mipmapped).  
face | Cubemap face to render into (use Unknown if not a cubemap).  
depthSlice | Depth slice to render into (use 0 if not a 3D or 2DArray render target).  
colorBuffer | Color buffer to render into.  
depthBuffer | Depth buffer to render into.  
colorBuffers | Color buffers to render into (for multiple render target effects).  
setup | Full render target setup information.  
  
### Description

Sets current render target.

This function sets which [RenderTexture](RenderTexture.html),
[GraphicsTexture](Rendering.GraphicsTexture.html), or a
[RenderBuffer](RenderBuffer.html) combination will be rendered into next. Use
it when implementing custom rendering algorithms, where you need to render
something into a render target texture manually.  
  
Variants with mipLevel and face arguments enable rendering into a specific
mipmap level of a texture, or specific cubemap face of a cubemap
RenderTexture/GraphicsTexture. Variants with depthSlice allow rendering into a
specific slice of a 3D or 2DArray render texture.  
  
The function call with colorBuffers array enables techniques that use Multiple
Render Targets (MRT), where fragment shader can output more than one final
color.  
  
Calling SetRenderTarget with just a RenderTexture or GraphicsTexture argument
is the same as setting the [RenderTexture.active](RenderTexture-active.html)
and [GraphicsTexture.active](Rendering.GraphicsTexture-active.html) property.
To set a GraphicsTexture as the render target, it must have
GraphicsTextureDescFlags.RenderTarget enabled in
GraphicsTexture.descriptor.flags.  
  
Note that in Linear color space, it is important to have the correct
sRGB<->Linear color conversion state set. Depending on what was rendered
previously, the current state might not be the one you expect. You should
consider setting [GL.sRGBWrite](GL-sRGBWrite.html) as you need it before doing
SetRenderTarget or any other manual rendering.  
  
Additional resources: [RenderTexture](RenderTexture.html),
[GraphicsTexture](Rendering.GraphicsTexture.html),
[Graphics.activeColorBuffer](Graphics-activeColorBuffer.html),
[Graphics.activeDepthBuffer](Graphics-activeDepthBuffer.html),
[SystemInfo.supportedRenderTargetCount](SystemInfo-
supportedRenderTargetCount.html).

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

