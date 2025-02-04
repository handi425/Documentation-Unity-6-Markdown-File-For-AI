[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/post-processing/enable-hdr-output-urp.html)
  * [中文](/cn/current/Manual/urp/post-processing/enable-hdr-output-urp.html)
  * [日本語](/ja/current/Manual/urp/post-processing/enable-hdr-output-urp.html)
  * [한국어](/kr/current/Manual/urp/post-processing/enable-hdr-output-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/post-processing/enable-hdr-output-urp.html)
  * [中文](/cn/current/Manual/urp/post-processing/enable-hdr-output-urp.html)
  * [日本語](/ja/current/Manual/urp/post-processing/enable-hdr-output-urp.html)
  * [한국어](/kr/current/Manual/urp/post-processing/enable-hdr-output-urp.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Color](../../graphics-color.html)
  * [High dynamic range (HDR)](../../hdr-landing.html)
  * [HDR](../../urp/post-processing/hdr-in-urp.html)
  * Enable HDR Output in URP

[](../../urp/post-processing/hdr-output-debug-views-urp.html)

HDR Output debug views in URP

[](../../urp/post-processing/hdr-output-implement-custom-overlay.html)

Implement an HDR Output compatible custom overlay in URP

# Enable HDR Output in URP

HDR Output in URP requires you to enable multiple properties to work. These
properties allow URP to render **scenes** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) correctly with **HDR** high
dynamic range  
See in [Glossary](../../Glossary.html#HDR) Rendering and then output the HDR
values to a display.

To activate HDR output, follow these steps.

  1. Locate the [URP Asset](./../universalrp-asset.html) in the Project window under **Assets** > **Settings**.

  2. Navigate to **Quality** > **HDR** and enable the checkbox to enable **HDR**.

  3. Navigate to **Edit** > **Project Settings** > **Player** > **Other Settings** and enable the following settings:

     * **Allow HDR Display Output**
     * **Use HDR Display Output**

**Note** : Only enable **Use HDR Display Output** if you need the main display
to use HDR Output.

If you switch to a URP Asset that does not have HDR enabled, URP disables HDR
Output until you change to a URP Asset with HDR enabled.

**Note** : When HDR Output is active the color grading mode is HDR by default,
even if a different Color Grading Mode is active in the URP Asset.

[](../../urp/post-processing/hdr-output-debug-views-urp.html)

HDR Output debug views in URP

[](../../urp/post-processing/hdr-output-implement-custom-overlay.html)

Implement an HDR Output compatible custom overlay in URP

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

