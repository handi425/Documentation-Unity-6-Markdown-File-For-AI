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

# RenderTargetIdentifier Constructor

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

public
RenderTargetIdentifier([Rendering.BuiltinRenderTextureType](Rendering.BuiltinRenderTextureType.html)
type);

## Declaration

public RenderTargetIdentifier(string name);

## Declaration

public RenderTargetIdentifier(int nameID);

## Declaration

public RenderTargetIdentifier([Texture](Texture.html) tex);

## Declaration

public
RenderTargetIdentifier([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
renderTargetIdentifier, int mipLevel, [CubemapFace](CubemapFace.html)
cubeFace, int depthSlice);

### Parameters

type | Built-in temporary render texture type.  
---|---  
name | Temporary render texture name.  
nameID | Temporary render texture name (as integer, see [Shader.PropertyToID](Shader.PropertyToID.html)).  
tex | RenderTexture or Texture object to use.  
mipLevel | MipLevel of the RenderTexture to use.  
cubemapFace | Cubemap face of the Cubemap RenderTexture to use.  
depthSlice | Depth slice of the Array RenderTexture to use. The symbolic constant [RenderTargetIdentifier.AllDepthSlices](Rendering.RenderTargetIdentifier.AllDepthSlices.html) indicates that all slices should be bound for rendering. The default value is 0.  
renderTargetIdentifier | An existing render target identifier.  
  
### Description

Creates a render target identifier.

Textures can be identified in a number of ways, for example a
[RenderTexture](RenderTexture.html) object, or a [Texture](Texture.html)
object, or one of built-in render textures
([BuiltinRenderTextureType](Rendering.BuiltinRenderTextureType.html)), or a
temporary render texture with a name (that was created using
[CommandBuffer.GetTemporaryRT](Rendering.CommandBuffer.GetTemporaryRT.html)).  
  
RenderTargetIdentifier can be implicitly created from a RenderTexture
reference, or a Texture reference, or a BuiltinRenderTextureType, or a name.  
  
A RenderTargetIdentifier created from Texture reference is only valid when
passed to
[CommandBuffer.SetGlobalTexture](Rendering.CommandBuffer.SetGlobalTexture.html)  
  
See Also:
[CommandBuffer.SetRenderTarget](Rendering.CommandBuffer.SetRenderTarget.html),
[CommandBuffer.SetGlobalTexture](Rendering.CommandBuffer.SetGlobalTexture.html).

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

