[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/upgrading-your-shaders.html)
  * [中文](/cn/current/Manual/urp/upgrading-your-shaders.html)
  * [日本語](/ja/current/Manual/urp/upgrading-your-shaders.html)
  * [한국어](/kr/current/Manual/urp/upgrading-your-shaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/upgrading-your-shaders.html)
  * [中文](/cn/current/Manual/urp/upgrading-your-shaders.html)
  * [日本語](/ja/current/Manual/urp/upgrading-your-shaders.html)
  * [한국어](/kr/current/Manual/urp/upgrading-your-shaders.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Get started with URP](../urp/introduction-landing.html)
  * [Installing and upgrading URP](../urp/InstallingAndConfiguringURP.html)
  * [Upgrading from the Built-In Render Pipeline to URP](../urp/upgrading-from-birp.html)
  * [Upgrading shaders to URP from the Built-In Render Pipeline](../urp/upgrade-shaders-landing.html)
  * Convert shaders to URP with the Render Pipeline Converter

[](../urp/upgrade-shaders-landing.html)

Upgrading shaders to URP from the Built-In Render Pipeline

[](../urp/urp-shaders/birp-urp-custom-shader-upgrade-guide.html)

Upgrade custom shaders for URP compatibility

# Convert shaders to URP with the Render Pipeline Converter

Use the [Render Pipeline Converter](features/rp-converter.html) to convert any
of Unity’s built-in Built-In **Render Pipeline** A series of operations that
take the contents of a Scene, and displays them on a screen. Unity lets you
choose from pre-built render pipelines, or write your own. [More
info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) materials and shaders to a
URP material and **shader** A program that runs on the GPU. [More
info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader). Refer to [Shader
mappings](upgrade-shaders-landing.html) for more information.

> **Note** : The Render Pipeline Converter makes irreversible changes to the
> project. Back up your project before the conversion.

If the preview thumbnails in the Project view are not shown correctly after
the conversion, try right-clicking anywhere in the Project view and selecting
**Reimport All**.

For [SpeedTree](https://docs.unity3d.com/Manual/SpeedTree.html) Shaders, Unity
does not re-generate Materials when you re-import them, unless you click the
**Generate Materials** or **Apply & Generate Materials** button.

## Shader mappings

The following table shows which URP shaders the Built-in Render Pipeline
shaders convert to when you use the Render Pipeline Converter.

Unity built-in shader | Universal Render Pipeline shader  
---|---  
Standard | Universal Render Pipeline/Lit  
Standard (Specular Setup) | Universal Render Pipeline/Lit  
Standard **Terrain** The landscape in your scene. A Terrain GameObject adds a
large flat plane to your scene and you can use the Terrain’s Inspector window
to create a detailed landscape. [More info](../terrain-UsingTerrains.html)  
See in [Glossary](../Glossary.html#Terrain) | Universal Render Pipeline/Terrain/Lit  
Particles/Standard Surface | Universal Render Pipeline/Particles/Lit  
Particles/Standard Unlit | Universal Render Pipeline/Particles/Unlit  
Mobile/Diffuse | Universal Render Pipeline/Simple Lit  
Mobile/Bumped Specular | Universal Render Pipeline/Simple Lit  
Mobile/Bumped Specular(1 Directional Light) | Universal Render Pipeline/Simple Lit  
Mobile/Unlit (Supports Lightmap) | Universal Render Pipeline/Simple Lit  
Mobile/VertexLit | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Specular | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Bumped Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Bumped Specular | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Self-Illumin/Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Self-Illumin/Bumped Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Self-Illumin/Specular | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Self-Illumin/Bumped Specular | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Specular | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Bumped Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Bumped Specular | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Cutout/Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Cutout/Specular | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Cutout/Bumped Diffuse | Universal Render Pipeline/Simple Lit  
Legacy Shaders/Transparent/Cutout/Bumped Specular | Universal Render Pipeline/Simple Lit  
  
[](../urp/upgrade-shaders-landing.html)

Upgrading shaders to URP from the Built-In Render Pipeline

[](../urp/urp-shaders/birp-urp-custom-shader-upgrade-guide.html)

Upgrade custom shaders for URP compatibility

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

