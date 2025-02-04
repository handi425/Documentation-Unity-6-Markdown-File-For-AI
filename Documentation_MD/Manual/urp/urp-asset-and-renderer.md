[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/urp-asset-and-renderer.html)
  * [中文](/cn/current/Manual/urp/urp-asset-and-renderer.html)
  * [日本語](/ja/current/Manual/urp/urp-asset-and-renderer.html)
  * [한국어](/kr/current/Manual/urp/urp-asset-and-renderer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/urp-asset-and-renderer.html)
  * [中文](/cn/current/Manual/urp/urp-asset-and-renderer.html)
  * [日本語](/ja/current/Manual/urp/urp-asset-and-renderer.html)
  * [한국어](/kr/current/Manual/urp/urp-asset-and-renderer.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Graphics quality settings in URP](../urp/urp-quality-settings-landing.html)
  * Universal Render Pipeline asset

[](../urp/urp-quality-settings-landing.html)

Graphics quality settings in URP

[](../urp/urp-asset-additional-settings.html)

Display advanced properties in a URP Asset

# Universal Render Pipeline asset

Any Unity project that uses the Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) must have a URP Asset
to configure the settings. When you create a project using the URP template,
Unity creates the URP Assets in the **Settings** project folder and assigns
them in **Project Settings** A broad collection of settings which allow you to
configure how Physics, Audio, Networking, Graphics, Input and many other areas
of your project behave. [More info](../comp-ManagerGroup.html)  
See in [Glossary](../Glossary.html#ProjectSettings). If you are migrating an
existing project to URP, you need to [create a URP Asset and assign the asset
in the Graphics settings](InstallURPIntoAProject.html).

The URP Asset controls several graphical features and quality settings for the
Universal Render Pipeline. It is a scriptable object that inherits from
‘RenderPipelineAsset’. When you assign the asset in the Graphics settings,
Unity switches from the built-in render pipeline to the URP. You can then
adjust the corresponding settings directly in the URP, instead of looking for
them elsewhere.

You can have multiple URP assets and switch between them. For example, you can
have one with Shadows on and one with Shadows off. If you switch between the
assets to understand the effects, you don’t have to manually toggle the
corresponding settings for shadows every time. You cannot, however, switch
between HDRP/SRP and URP assets, as the render pipelines are incompatible.

## Additional resources

  * [URP Asset reference](universalrp-asset.html)

[](../urp/urp-quality-settings-landing.html)

Graphics quality settings in URP

[](../urp/urp-asset-additional-settings.html)

Display advanced properties in a URP Asset

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

