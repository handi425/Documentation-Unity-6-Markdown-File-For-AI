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

# RenderTextureCreationFlags

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

Set of flags that control the state of a newly-created RenderTexture.

### Properties

[MipMap](RenderTextureCreationFlags.MipMap.html)| Set this flag to allocate
mipmaps in the RenderTexture. See RenderTexture.useMipMap for more details.  
---|---  
[AutoGenerateMips](RenderTextureCreationFlags.AutoGenerateMips.html)|
Determines whether or not mipmaps are automatically generated when the
RenderTexture is modified. This flag is set by default, and has no effect if
the RenderTextureCreationFlags.MipMap flag is not also set. See
RenderTexture.autoGenerateMips for more details.  
[SRGB](RenderTextureCreationFlags.SRGB.html)| When this flag is set, reads and
writes to this texture are converted to SRGB color space. See
RenderTexture.sRGB for more details.  
[EyeTexture](RenderTextureCreationFlags.EyeTexture.html)| Set this flag when
the Texture is to be used as a VR eye texture. This flag is cleared by
default. This flag is set on a RenderTextureDesc when it is returned from
GetDefaultVREyeTextureDesc or other VR functions returning a
RenderTextureDesc.  
[EnableRandomWrite](RenderTextureCreationFlags.EnableRandomWrite.html)| Set
this flag to enable random access writes to the RenderTexture from shaders.
Normally, pixel shaders only operate on pixels they are given. Compute shaders
cannot write to textures without this flag. Random write enables shaders to
write to arbitrary locations on a RenderTexture. See
RenderTexture.enableRandomWrite for more details, including supported
platforms.  
[CreatedFromScript](RenderTextureCreationFlags.CreatedFromScript.html)| This
flag is always set internally when a RenderTexture is created from script. It
has no effect when set manually from script code.  
[AllowVerticalFlip](RenderTextureCreationFlags.AllowVerticalFlip.html)| Clear
this flag when a RenderTexture is a VR eye texture and the device does not
automatically flip the texture when being displayed. This is platform specific
and It is set by default. This flag is only cleared when part of a
RenderTextureDesc that is returned from GetDefaultVREyeTextureDesc or other VR
functions that return a RenderTextureDesc. Currently, only Hololens eye
textures need to clear this flag.  
[NoResolvedColorSurface](RenderTextureCreationFlags.NoResolvedColorSurface.html)|
When this flag is set, the engine will not automatically resolve the color
surface.  
[DynamicallyScalable](RenderTextureCreationFlags.DynamicallyScalable.html)|
Set this flag to mark this RenderTexture for Dynamic Resolution should the
target platform/graphics API support Dynamic Resolution.  
[BindMS](RenderTextureCreationFlags.BindMS.html)| Setting this flag causes the
RenderTexture to be bound as a multisampled texture in a shader. The flag
prevents the RenderTexture from being resolved by default when
RenderTexture.antiAliasing is greater than 1.  
[DynamicallyScalableExplicit](RenderTextureCreationFlags.DynamicallyScalableExplicit.html)|
Set this flag to mark this RenderTexture for Dynamic Resolution, if the target
platform/graphics API supports Dynamic Resolution.  
  
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

