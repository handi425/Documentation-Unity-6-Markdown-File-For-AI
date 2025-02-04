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

#  [GL](GL.html).sRGBWrite

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

public static bool sRGBWrite;

### Description

Controls whether Linear-to-sRGB color conversion is performed while rendering.

This property is only relevant when [Linear Color
Space](../Manual/LinearLighting.html) rendering is used. Typically when linear
color space is used, non-HDR render textures are treated as sRGB data (i.e.
"regular colors"), and fragment shaders outputs are treated as linear color
values. So by default the fragment shader color value is converted into sRGB.  
  
However, if you know your fragment shader already outputs sRGB color value for
some reason and want to temporarily turn off Linear-to-sRGB write color
conversion, you can use this property to achieve that.  
  
Note that the ability to turn off sRGB writes is not supported on all
platforms (typically mobile "tile based" GPUs can not do it), so this is
considered a "feature of last resort". Usually it is better to create
[RenderTextures](RenderTexture.html) with appropriate color space flag (linear
vs sRGB) and not switch the conversions in the middle of rendering into it.  
  
Additional resources: [Linear Color Space](../Manual/LinearLighting.html),
[RenderTexture.sRGB](RenderTexture-sRGB.html),
[RenderTextureReadWrite](RenderTextureReadWrite.html),
[PlayerSettings.colorSpace](PlayerSettings-colorSpace.html).

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

