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

#  [CommandBuffer](Rendering.CommandBuffer.html).SetRenderTarget

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

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rt);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rt, [Rendering.RenderBufferLoadAction](Rendering.RenderBufferLoadAction.html)
loadAction,
[Rendering.RenderBufferStoreAction](Rendering.RenderBufferStoreAction.html)
storeAction);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rt, [Rendering.RenderBufferLoadAction](Rendering.RenderBufferLoadAction.html)
colorLoadAction,
[Rendering.RenderBufferStoreAction](Rendering.RenderBufferStoreAction.html)
colorStoreAction,
[Rendering.RenderBufferLoadAction](Rendering.RenderBufferLoadAction.html)
depthLoadAction,
[Rendering.RenderBufferStoreAction](Rendering.RenderBufferStoreAction.html)
depthStoreAction);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rt, int mipLevel);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rt, int mipLevel, [CubemapFace](CubemapFace.html) cubemapFace);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rt, int mipLevel, [CubemapFace](CubemapFace.html) cubemapFace, int
depthSlice);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
color,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
depth);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
color,
[Rendering.RenderBufferLoadAction](Rendering.RenderBufferLoadAction.html)
colorLoadAction,
[Rendering.RenderBufferStoreAction](Rendering.RenderBufferStoreAction.html)
colorStoreAction,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
depth,
[Rendering.RenderBufferLoadAction](Rendering.RenderBufferLoadAction.html)
depthLoadAction,
[Rendering.RenderBufferStoreAction](Rendering.RenderBufferStoreAction.html)
depthStoreAction);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
color,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
depth, int mipLevel);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
color,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
depth, int mipLevel, [CubemapFace](CubemapFace.html) cubemapFace);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
color,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
depth, int mipLevel, [CubemapFace](CubemapFace.html) cubemapFace, int
depthSlice);

## Declaration

public void SetRenderTarget(RenderTargetIdentifier[] colors,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
depth);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetBinding](Rendering.RenderTargetBinding.html)
binding);

## Declaration

public void
SetRenderTarget([Rendering.RenderTargetBinding](Rendering.RenderTargetBinding.html)
binding, int mipLevel, [CubemapFace](CubemapFace.html) cubemapFace, int
depthSlice);

## Declaration

public void SetRenderTarget(RenderTargetIdentifier[] colors,
[Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
depth, int mipLevel, [CubemapFace](CubemapFace.html) cubemapFace, int
depthSlice);

### Parameters

rt | Render target to set for both color & depth buffers.  
---|---  
color | Render target to set as a color buffer.  
colors | Render targets to set as color buffers (MRT).  
depth | Render target to set as a depth buffer.  
mipLevel | The mip level of the render target to render into.  
cubemapFace | The cubemap face of a cubemap render target to render into.  
depthSlice | Slice of a 3D or array render target to set.  
loadAction | Load action that is used for color and depth/stencil buffers.  
storeAction | Store action that is used for color and depth/stencil buffers.  
colorLoadAction | Load action that is used for the color buffer.  
colorStoreAction | Store action that is used for the color buffer.  
depthLoadAction | Load action that is used for the depth/stencil buffer.  
depthStoreAction | Store action that is used for the depth/stencil buffer.  
  
### Description

Add a "set active render target" command.

Render texture to use can be indicated in several ways: a RenderTexture
object, a temporary render texture created with
[GetTemporaryRT](Rendering.CommandBuffer.GetTemporaryRT.html), or one of
built-in temporary textures
([BuiltinRenderTextureType](Rendering.BuiltinRenderTextureType.html)). All
that is expressed by a
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html) struct, which
has implicit conversion operators to save on typing.  
  
You do not explicitly need to preserve active render targets during command
buffer execution (current render targets are saved & restored afterwards).  
  
Variations of this method are available which take extra arguments such as
mipLevel (int) and cubemapFace to enable rendering into a specific mipmap
level of a RenderTexture, or specific cubemap face of a cubemap RenderTexture.
Overloads setting a single RenderTarget and without explicit mipLevel,
cubemapFace and depthSlice respect the mipLevel, cubemapFace and depthSlice
values that were specified when creating the
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html). Overloads
setting multiple render targets will set mipLevel, cubemapFace, and depthSlice
to 0, Unknown, and 0 unless otherwise specified. If specified, it will use the
specified mipLevel, cubemapFace, and depthSlice for all targets.  
  
Note that in Linear color space, it is important to have the correct
sRGB<->Linear color conversion state set. Depending on what was rendered
previously, the current state might not be the one you expect. You should
consider setting [GL.sRGBWrite](GL-sRGBWrite.html) as you need it before doing
SetRenderTarget or any other manual rendering.  
  
Rendering.RenderTargetIdentifier.Clear is currently not supported. A
subsequent call to
[ClearRenderTarget](Rendering.CommandBuffer.ClearRenderTarget.html) has the
same effect and is optimized on graphics APIs that support `clear` load
actions.  
  
Additional resources:
[GetTemporaryRT](Rendering.CommandBuffer.GetTemporaryRT.html),
[ClearRenderTarget](Rendering.CommandBuffer.ClearRenderTarget.html),
[Blit](Rendering.CommandBuffer.Blit.html),
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html).

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

