[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
  * [中文](/cn/current/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
  * [日本語](/ja/current/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
  * [한국어](/kr/current/Manual/urp/post-processing/hdr-output-debug-views-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
  * [中文](/cn/current/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
  * [日本語](/ja/current/Manual/urp/post-processing/hdr-output-debug-views-urp.html)
  * [한국어](/kr/current/Manual/urp/post-processing/hdr-output-debug-views-urp.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Color](../../graphics-color.html)
  * [High dynamic range (HDR)](../../hdr-landing.html)
  * [HDR](../../urp/post-processing/hdr-in-urp.html)
  * HDR Output debug views in URP

[](../../urp/post-processing/hdr-output.html)

HDR Output in URP

[](../../urp/post-processing/enable-hdr-output-urp.html)

Enable HDR Output in URP

# HDR Output debug views in URP

URP offers three debug views for **HDR** high dynamic range  
See in [Glossary](../../Glossary.html#HDR) rendering.

These views are:

  * Gamut View
  * Gamut Clip
  * Values exceeding Paper White

To access them, navigate to **Window** > **Analysis** > **Render Pipeline
Debugger** > **Lighting** > **HDR Debug Mode**.

## Gamut View

![Gamut Debug View](../../../uploads/urp/post-proc/hdr/HDR-Output-
GamutView.png) Gamut Debug View

The triangles in this debug view indicate which parts of three specific color
gamuts this **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) covers. The small triangle
displays the [Rec709](https://en.wikipedia.org/wiki/Rec._709) gamut values,
the medium triangle displays the
[P3-D65](https://en.wikipedia.org/wiki/DCI-P3) gamut values, and the large
triangle displays the [Rec2020](https://en.wikipedia.org/wiki/Rec._2020) gamut
values. This enables you to check color plot changes while color grading. It
can also help you ensure that you benefit from the wider color gamut available
in HDR.

## Gamut Clip

![Gamut Clip Debug View](../../../uploads/urp/post-proc/hdr/HDR-Output-
GamutClip.png) Gamut Clip Debug View

This debug view indicates the relationship between scene values and specific
color gamuts. Areas of the screen with values within the Rec709 gamut are
green, areas outside of the Rec709 gamut but inside the P3-D65 gamut are blue,
and areas outside of both are red.

## Values exceeding Paper White

![Values Exceeding Paper White Debug View](../../../uploads/urp/post-
proc/hdr/HDR-Output-OverPaperWhite.png) Values Exceeding Paper White Debug
View

This debug view uses a color coded gradient to indicate parts of the Scene
that exceed the Paper White value and Max Nits. The gradient ranges from
yellow to red and blue. Yellow corresponds to **Paper White** +1, red
corresponds to **Max Nits** , and blue corresponds to **Max Nits** +1.

[](../../urp/post-processing/hdr-output.html)

HDR Output in URP

[](../../urp/post-processing/enable-hdr-output-urp.html)

Enable HDR Output in URP

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

