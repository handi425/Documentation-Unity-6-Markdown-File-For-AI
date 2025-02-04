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

# RenderTextureReadWrite

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

Color space conversion mode of a [RenderTexture](RenderTexture.html).

When using Gamma [color space](../Manual/LinearLighting.html), no conversions
are done of any kind, and this setting is not used.  
  
When Linear color space is used, then by default non-HDR render textures are
considered to contain sRGB data (i.e. "regular colors"), and fragment shaders
are considered to output linear color values. So by default the fragment
shader color value is converted into sRGB when rendering into a texture; and
when sampling the texture in the shader the sRGB colors are converted into
linear values. This is the [sRGB](RenderTextureReadWrite-sRGB.html) read-write
mode; and the [Default](RenderTextureReadWrite.Default.html) mode matches that
when linear color space is used. When this mode is set on a render texture,
[RenderTexture.sRGB](RenderTexture-sRGB.html) will return true.  
  
However, if your render texture will contain non-color data (normals,
velocities, other custom values) then you don't want Linear<->sRGB conversions
to happen. This is the [Linear](RenderTextureReadWrite.Linear.html) read-write
mode. When this mode is set on a render texture,
[RenderTexture.sRGB](RenderTexture-sRGB.html) will return false.  
  
Note that some [render texture formats](RenderTextureFormat.html) are always
considered to contain "linear" data and no sRGB conversions are ever performed
on them, no matter what is the read-write setting. This is true for all "HDR"
(floating point) formats, and other formats like Depth or Shadowmap.  
  
Additional resources: [Linear Color Space](../Manual/LinearLighting.html),
[RenderTexture.sRGB](RenderTexture-sRGB.html),
[PlayerSettings.colorSpace](PlayerSettings-colorSpace.html),
[GL.sRGBWrite](GL-sRGBWrite.html).

### Properties

[Default](RenderTextureReadWrite.Default.html)| Default color space conversion
based on project settings.  
---|---  
[Linear](RenderTextureReadWrite.Linear.html)| Render texture contains linear
(non-color) data; don't perform color conversions on it.  
[sRGB](RenderTextureReadWrite-sRGB.html)| Render texture contains sRGB (color)
data, perform Linear<->sRGB conversions on it.  
  
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

