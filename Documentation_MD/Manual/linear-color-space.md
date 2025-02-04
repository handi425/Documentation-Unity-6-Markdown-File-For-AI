[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/linear-color-space.html)
  * [中文](/cn/current/Manual/linear-color-space.html)
  * [日本語](/ja/current/Manual/linear-color-space.html)
  * [한국어](/kr/current/Manual/linear-color-space.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/linear-color-space.html)
  * [中文](/cn/current/Manual/linear-color-space.html)
  * [日本語](/ja/current/Manual/linear-color-space.html)
  * [한국어](/kr/current/Manual/linear-color-space.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Color](graphics-color.html)
  * [Color spaces](color-spaces-landing.html)
  * [Linear color space](linear-color-space-landing.html)
  * Introduction to linear color space in Unity

[](linear-color-space-landing.html)

Linear color space

[](gamma-textures-linear-color-space.html)

Gamma Textures in linear color space

# Introduction to linear color space in Unity

Working in linear color space gives more accurate rendering than working in
gamma color space.

You can work in linear color space if your Textures were created in linear or
gamma color space. Gamma color space Texture inputs to the linear color space
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) program are supplied to the Shader
with gamma correction removed from them.

For information on how to set the color space of your project, refer to [Set a
project’s color space](set-project-color-space.html).

**Note** : The **Texture preview** window in [Texture Import
Settings](../ScriptReference/TextureImporter.html) displays Textures using
gamma blending even if you are working in linear color space.

## Linear Textures

Selecting **Color Space: Linear** assumes your Textures are in gamma color
space. Unity uses your GPU’s sRGB sampler by default to crossover from gamma
to linear color space. If your Textures are authored in linear color space,
you need to bypass the sRGB sampling. For more information, refer to [Disable
sRGB sampling for a texture](disable-srgb-sampling-textures.html).

## Gamma Textures

Crossing over from gamma color space to linear color space requires some
tweaking. For more information, refer to [Gamma Textures in linear color
space](gamma-textures-linear-color-space.html).

### Gamma to linear conversion

For colors, this conversion is applied implicitly, because the Unity Editor
already converts the values to floating point before passing them to the GPU
as constants. When sampling Textures, the GPU automatically removes the gamma
correction, converting the result to linear space.

These inputs are then passed to the Shader, with lighting calculations taking
place in linear space as they normally do. When writing the resulting value to
a framebuffer, it is either gamma-corrected straight away or left in linear
space for later gamma correction - this depends on the current rendering
configuration. For example, in high dynamic range (HDR), rendering results are
left in linear space and gamma corrected later.

[](linear-color-space-landing.html)

Linear color space

[](gamma-textures-linear-color-space.html)

Gamma Textures in linear color space

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

