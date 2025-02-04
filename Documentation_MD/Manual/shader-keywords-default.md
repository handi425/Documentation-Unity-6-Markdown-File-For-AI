[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-keywords-default.html)
  * [中文](/cn/current/Manual/shader-keywords-default.html)
  * [日本語](/ja/current/Manual/shader-keywords-default.html)
  * [한국어](/kr/current/Manual/shader-keywords-default.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-keywords-default.html)
  * [中文](/cn/current/Manual/shader-keywords-default.html)
  * [日本語](/ja/current/Manual/shader-keywords-default.html)
  * [한국어](/kr/current/Manual/shader-keywords-default.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * [Built-in keywords](shaders-keywords-built-in.html)
  * Default shader keywords

[](shaders-keywords-built-in.html)

Built-in keywords

[](SL-MultipleProgramVariants-shortcuts.html)

Add built-in keyword sets

# Default shader keywords

Unity uses predefined sets of **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) keywords to generate shader variants
that enable common functionality.

Unity adds the following sets of shader variant keywords at compile time:

  * By default, Unity adds this set of keywords to all graphics shader programs: STEREO_INSTANCING_ON, STEREO_MULTIVIEW_ON, STEREO_CUBEMAP_RENDER_ON, UNITY_SINGLE_PASS_STEREO. You can strip these keywords using an Editor script. For more information, see [Shader variant stripping](shader-variant-stripping.html).
  * By default, Unity adds this set of keywords to the Standard Shader: LIGHTMAP_ON, DIRLIGHTMAP_COMBINED, DYNAMICLIGHTMAP_ON, LIGHTMAP_SHADOW_MIXING, SHADOWS_SHADOWMASK. You can strip these keywords using the [Graphics settings](class-GraphicsSettings.html) window.
  * In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), if your project uses [tier
settings](graphics-tiers-customize.html) that differ from each other, Unity
adds this set of keywords to all graphics shaders: UNITY_HARDWARE_TIER1,
UNITY_HARDWARE_TIER2, UNITY_HARDWARE_TIER3. For more information, see
[Graphics tiers: Graphics tiers and shader variants](graphics-
tiers.html#shader-variants).

[](shaders-keywords-built-in.html)

Built-in keywords

[](SL-MultipleProgramVariants-shortcuts.html)

Add built-in keyword sets

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

