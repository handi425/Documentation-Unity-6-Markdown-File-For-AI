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

#  [Texture2D](Texture2D.html).Compress

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

public void Compress(bool highQuality);

### Description

Compress texture at runtime to DXT/BCn or ETC formats.

Use this to compress textures at runtime. Compressed textures use less
graphics memory and are faster to render. For more information on texture
compression, see [Texture compression](../Manual/texture-compression-
formats.html).  
  
The format that Unity compresses the texture to depends on the platform, and
the properties of the texture.  
  
texture will be in [DXT1](TextureFormat.DXT1.html) (BC1) format if the
original texture had no alpha channel, and in [DXT5](TextureFormat.DXT5.html)
(BC3) format if it had alpha channel. If the original texture was
[R8](TextureFormat.R8.html), the compressed format will be
[BC4](TextureFormat.BC4.html). If the original texture was
[RG16](TextureFormat.RG16.html), the compressed format will be
[BC5](TextureFormat.BC5.html).  
  
On Android, iOS and tvOS, this will compress the texture to the ETC/EAC family
of formats.  
  
Passing `true` for `highQuality` parameter will dither the source texture
during compression, which helps to reduce compression artifacts but is
slightly slower. This parameter is ignored for ETC compression.  
  
If the graphics card does not support compression or the texture is already in
compressed format, then Compress does nothing.  
  
In the Editor scripts, you probably want to use
[EditorUtility.CompressTexture](EditorUtility.CompressTexture.html), which
compresses using slower, but higher quality compression. It can also compress
into other compressed formats.  
  
You can also load already precompressed data into a texture using
[LoadRawTextureData](Texture2D.LoadRawTextureData.html) function.  
  
Additional resources: [SetPixels](Texture2D.SetPixels.html),
[EditorUtility.CompressTexture](EditorUtility.CompressTexture.html),
[LoadRawTextureData](Texture2D.LoadRawTextureData.html).

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

