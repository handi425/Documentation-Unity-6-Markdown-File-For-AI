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

#  [PanelSettings](UIElements.PanelSettings.html).forceGammaRendering

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

public bool forceGammaRendering;

### Description

Forces the UI shader to output colors in the gamma color space.

This is only applicable when the project is in linear color space and when the
panel is being rendered into a Render Texture with a compatible format (e.g.
R8G8B8A8_UNORM). It has no effect when the project color space is set to
gamma.  
  
You can use this feature to combine the SRGB Render Texture from your camera
with the UNORM Render Texture of the UI. In an on-screen UI panel, use an
ImmediateModeElement to draw a full-screen quad with a custom shader that
blends both.  
  
" Note 1: Render Texture read/write operations require additional bandwidth.
This could negatively impact performance. " Note 2: When a texture is sampled
in the fragment shader, the shader will perform a linear-to-gamma color space
conversion on the RGB channels. This could negatively impact performance. *
Note 3: When sampling from a texture, the interpolation between texels or mip
levels is still performed in linear color space. This might lead to some
visual differences between this mode and the same UI in a gamma project.

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

