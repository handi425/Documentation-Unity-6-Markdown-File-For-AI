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

#  [CommandBuffer](Rendering.CommandBuffer.html).GetTemporaryRTArray

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

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format, int antiAliasing, bool enableRandomWrite, bool useDynamicScale);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format, int antiAliasing, bool enableRandomWrite);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format, int antiAliasing);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[RenderTextureFormat](RenderTextureFormat.html) format,
[RenderTextureReadWrite](RenderTextureReadWrite.html) readWrite, int
antiAliasing);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[RenderTextureFormat](RenderTextureFormat.html) format,
[RenderTextureReadWrite](RenderTextureReadWrite.html) readWrite);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[RenderTextureFormat](RenderTextureFormat.html) format);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int
slices);

## Declaration

public void GetTemporaryRTArray(int nameID, int width, int height, int slices,
int depthBuffer, [FilterMode](FilterMode.html) filter,
[RenderTextureFormat](RenderTextureFormat.html) format,
[RenderTextureReadWrite](RenderTextureReadWrite.html) readWrite, int
antiAliasing, bool enableRandomWrite);

### Parameters

nameID | Shader property name for this texture.  
---|---  
width | Width in pixels, or -1 for "camera pixel width".  
height | Height in pixels, or -1 for "camera pixel height".  
slices | Number of slices in texture array.  
depthBuffer | Depth buffer bits (0, 16 or 24).  
filter | Texture filtering mode (default is Point).  
format | Format of the render texture (default is ARGB32).  
readWrite | Color space conversion mode.  
antiAliasing | Anti-aliasing (default is no anti-aliasing).  
enableRandomWrite | Should random-write access into the texture be enabled (default is false).  
useDynamicScale | Whether to enable [DynamicResolution](../Manual/DynamicResolution.html) for the texture array.  
  
### Description

Add a "get a temporary render texture array" command.

This creates a temporary render texture array with given parameters, and sets
it up as a global shader property with nameID. Use
[Shader.PropertyToID](Shader.PropertyToID.html) to create the integer name.  
  
Release the temporary render texture array using
[ReleaseTemporaryRT](Rendering.CommandBuffer.ReleaseTemporaryRT.html), passing
the same nameID. Any temporary textures that were not explicitly released will
be removed after camera is done rendering, or after
[Graphics.ExecuteCommandBuffer](Graphics.ExecuteCommandBuffer.html) is done.  
  
After getting a temporary render texture array, you can set it as active
([SetRenderTarget](Rendering.CommandBuffer.SetRenderTarget.html)) or blit
to/from it ([Blit](Rendering.CommandBuffer.Blit.html)). You do not explicitly
need to preserve active render targets during command buffer execution
(current render targets are saved & restored afterwards).  
  
Additional resources:
[ReleaseTemporaryRT](Rendering.CommandBuffer.ReleaseTemporaryRT.html),
[SetRenderTarget](Rendering.CommandBuffer.SetRenderTarget.html),
[Blit](Rendering.CommandBuffer.Blit.html).

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

