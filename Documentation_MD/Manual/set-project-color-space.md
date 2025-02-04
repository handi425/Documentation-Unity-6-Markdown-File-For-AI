[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/set-project-color-space.html)
  * [中文](/cn/current/Manual/set-project-color-space.html)
  * [日本語](/ja/current/Manual/set-project-color-space.html)
  * [한국어](/kr/current/Manual/set-project-color-space.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/set-project-color-space.html)
  * [中文](/cn/current/Manual/set-project-color-space.html)
  * [日本語](/ja/current/Manual/set-project-color-space.html)
  * [한국어](/kr/current/Manual/set-project-color-space.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Color](graphics-color.html)
  * [Color spaces](color-spaces-landing.html)
  * Set a project's color space

[](linear-textures.html)

Linear textures

[](disable-srgb-sampling-textures.html)

Disable sRGB sampling for a texture

# Set a project’s color space

The Unity Editor offers both linear and gamma workflows. The linear workflow
has a color space crossover where [Textures](Textures.html)An image used when
rendering a GameObject, Sprite, or UI element. Textures are often applied to
the surface of a mesh to give it visual detail. [More info](class-
TextureImporter.html)  
See in [Glossary](Glossary.html#texture) that were authored in gamma color
space can be correctly and precisely rendered in linear color space. See
documentation on [Linear rendering overview](color-spaces-landing.html) for
more information about gamma and linear color space.

Textures tend to be saved in gamma color space, while Shaders expect linear
color space. As such, when Textures are sampled in Shaders, the gamma-based
values lead to inaccurate results. To overcome this, you can set Unity to use
an sRGB sampler to cross over from gamma to linear sampling. This ensures a
linear workflow with all inputs and outputs of a **Shader** A program that
runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) in the correct color space, resulting
in a correct outcome.

## Select the color space

Select the color space for your project with the following steps:

  1. Go to **Edit** > **Project Settings** , then select the **Player** category.
  2. Navigate to the **Other Settings** , open the **Rendering** section, and set the **Color Space** property to **Linear** or **Gamma** , depending on your preference.

[](linear-textures.html)

Linear textures

[](disable-srgb-sampling-textures.html)

Disable sRGB sampling for a texture

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

