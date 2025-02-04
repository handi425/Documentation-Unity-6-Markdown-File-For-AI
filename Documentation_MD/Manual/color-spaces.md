[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/color-spaces.html)
  * [中文](/cn/current/Manual/color-spaces.html)
  * [日本語](/ja/current/Manual/color-spaces.html)
  * [한국어](/kr/current/Manual/color-spaces.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/color-spaces.html)
  * [中文](/cn/current/Manual/color-spaces.html)
  * [日本語](/ja/current/Manual/color-spaces.html)
  * [한국어](/kr/current/Manual/color-spaces.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Color](graphics-color.html)
  * [Color spaces](color-spaces-landing.html)
  * Color spaces in Unity

[](color-spaces-landing.html)

Color spaces

[](differences-linear-gamma-color-space.html)

Differences between linear and gamma color space

# Color spaces in Unity

The Unity Editor allows you to work in traditional gamma color space as well
as linear color space. While gamma color space is the historically standard
format, linear color space rendering gives more precise results.

## Linear and gamma color space

The human eye doesn’t have a linear response to light intensity. We see some
brightnesses of light more easily than others - a gradient that proceeds in a
linear fashion from black to white would not look like a linear gradient to
our eyes.

![Left: A linear gradient. Right: How our eyes perceive that gradient. Note
where the borders \(which are exactly mid-grey\) merge with the gradient in
each case](../uploads/Main/LinearLighting-LinearGradients.png) Left: A linear
gradient. Right: How our eyes perceive that gradient. Note where the borders
(which are exactly mid-grey) merge with the gradient in each case

For historical reasons, monitors and displays have the same characteristic.
Sending a monitor a linear signal results in something that looks like the
gradient to the right in the illustration above, and simply looks wrong to our
eyes. To compensate for this, a corrected signal is sent to make sure the
monitor shows an image that looks natural. This correction is known as gamma
correction.

The reason both gamma and linear color spaces exist is because lighting
calculations should be done in linear space in order to be mathematically
correct, but the result should be presented in gamma space to look correct to
our eyes.

When calculating lighting on older hardware restricted to 8 bits per channel
for the framebuffer format, using a gamma curve provides more precision in the
human-perceivable range. More bits are used in the range where the human eye
is the most sensitive.

Even though monitors today are digital, they still take a gamma-encoded signal
as input. Image files and video files are explicitly encoded to be in gamma
space (meaning they carry gamma-encoded values, not linear intensities). This
is the standard; everything is in gamma space.

The accepted standard for gamma space is called sRGB (see
[Wikipedia](https://en.wikipedia.org/wiki/SRGB)). This standard defines a
mapping to linear space that allows our eyes to make the most of the 8 bits
per channel of precision.

Linear rendering refers to the process of rendering a **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) with all inputs linear - that is to
say, not gamma corrected for viewing with human eyes or for output to a
display.

[](color-spaces-landing.html)

Color spaces

[](differences-linear-gamma-color-space.html)

Differences between linear and gamma color space

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

