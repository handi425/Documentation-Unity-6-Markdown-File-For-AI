[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gamma-color-space.html)
  * [中文](/cn/current/Manual/gamma-color-space.html)
  * [日本語](/ja/current/Manual/gamma-color-space.html)
  * [한국어](/kr/current/Manual/gamma-color-space.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gamma-color-space.html)
  * [中文](/cn/current/Manual/gamma-color-space.html)
  * [日本語](/ja/current/Manual/gamma-color-space.html)
  * [한국어](/kr/current/Manual/gamma-color-space.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Color](graphics-color.html)
  * [Color spaces](color-spaces-landing.html)
  * Gamma color space

[](differences-linear-gamma-color-space.html)

Differences between linear and gamma color space

[](linear-color-space-landing.html)

Linear color space

# Gamma color space

While a linear workflow ensures more precise rendering, sometimes you may want
a gamma workflow (for example, on some platforms the hardware only supports
the gamma format).

For information on how to set the color space of your project, refer to [Set a
project’s color space](set-project-color-space.html).

Unity uses the gamma color space for color calculations, and keeps imported
textures in the gamma color space. Unity also makes sure **shaders** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) keep textures in gamma color space,
calculate in gamma color space, and write to a framebuffer that doesn’t
reapply gamma correction.

[Texture Import Settings](class-TextureImporter.html) might show textures as
being in linear format, because this avoids shaders recognising the textures
as being in gamma color space and automatically removing the gamma correction.

**Note** : You can choose to bypass sRGB sampling in **Color Space: Gamma**
mode. For more information on how to do this, refer to [Disable sRGB sampling
for a texture](disable-srgb-sampling-textures.html).

[](differences-linear-gamma-color-space.html)

Differences between linear and gamma color space

[](linear-color-space-landing.html)

Linear color space

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

