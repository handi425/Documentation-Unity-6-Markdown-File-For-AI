[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)
  * [中文](/cn/current/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)
  * [日本語](/ja/current/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)
  * [한국어](/kr/current/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)
  * [中文](/cn/current/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)
  * [日本語](/ja/current/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)
  * [한국어](/kr/current/Manual/urp/birp-onboarding/birp-light-falloff-in-urp.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Get started with URP](../../urp/introduction-landing.html)
  * [Installing and upgrading URP](../../urp/InstallingAndConfiguringURP.html)
  * [Upgrading from the Built-In Render Pipeline to URP](../../urp/upgrading-from-birp.html)
  * Change how lights fade to match the Built-In Render Pipeline

[](../../urp/urp-shaders/birp-urp-custom-shader-upgrade-guide.html)

Upgrade custom shaders for URP compatibility

[](../../urp/birp-onboarding/quality-presets.html)

Convert quality settings from the Built-In Render Pipeline to URP

# Change how lights fade to match the Built-In Render Pipeline

After converting the necessary **project settings** A broad collection of
settings which allow you to configure how Physics, Audio, Networking,
Graphics, Input and many other areas of your project behave. [More
info](../../comp-ManagerGroup.html)  
See in [Glossary](../../Glossary.html#ProjectSettings) and materials from the
Built-In **Render Pipeline** A series of operations that take the contents of
a Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) to URP, the overall look
of the **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) might still not match the look of
the original project.

One reason for this is that the light falloff functions in the Built-In Render
Pipeline and URP are different. URP implements inverse square light falloff,
while the Built-In Render Pipeline uses quadratic falloff. Changes in quality
or light component settings might not be enough to achieve the same look in
URP.

To change the light falloff function in URP and make it look similar to the
Built-In Render Pipeline falloff, refer to [Change the light falloff function
in URP](../lighting/custom-lighting-change-light-falloff.html).

## Additional resources

  * [Custom lighting in URP](../lighting/custom-lighting-landing.html)

[](../../urp/urp-shaders/birp-urp-custom-shader-upgrade-guide.html)

Upgrade custom shaders for URP compatibility

[](../../urp/birp-onboarding/quality-presets.html)

Convert quality settings from the Built-In Render Pipeline to URP

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

