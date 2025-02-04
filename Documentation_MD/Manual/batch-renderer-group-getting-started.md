[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/batch-renderer-group-getting-started.html)
  * [中文](/cn/current/Manual/batch-renderer-group-getting-started.html)
  * [日本語](/ja/current/Manual/batch-renderer-group-getting-started.html)
  * [한국어](/kr/current/Manual/batch-renderer-group-getting-started.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/batch-renderer-group-getting-started.html)
  * [中文](/cn/current/Manual/batch-renderer-group-getting-started.html)
  * [日本語](/ja/current/Manual/batch-renderer-group-getting-started.html)
  * [한국어](/kr/current/Manual/batch-renderer-group-getting-started.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](batch-renderer-group.html)
  * Set up your project for the BatchRendererGroup API in URP

[](batch-renderer-group-how.html)

Introduction to the BatchRendererGroup API in URP

[](batch-renderer-group-creating-a-renderer.html)

Creating a renderer with the BatchRendererGroup API in URP

# Set up your project for the BatchRendererGroup API in URP

Before you use BRG, your project must support it. BRG requires your project
to:

  * Use the SRP Batcher. To enable the SRP Batcher, see [Using the SRP Batcher](SRPBatcher-Enable.html).
  * Keep BRG [shader variants](shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant). To do this, select **Edit** >
**Project Settings** > **Graphics** , and set **BatchRendererGroup variants**
to **Keep all**.

  * If your project uses URP, it’s best practice to disable the **Strip Unused Variants** [Global Setting](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@13.1/manual/urp-global-settings.html). This helps to avoid problems with Unity stripping necessary DOTS Instancing variants. For more information, see [DOTS Instancing shaders](dots-instancing-shaders.html). To find this setting, select **Edit** > **Project Settings** > **URP Global Settings**.
  * Allow [unsafe code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code). To do this, enable the **Allow ‘unsafe’ Code** [Player Setting](class-PlayerSettings.html).

**Note:** The BatchRendererGroup uses [DOTS Instancing shaders](dots-
instancing-shaders.html), but it doesn’t require any DOTS packages. The name
reflects the new data-oriented way to load instance data, and also helps with
backward compatibility with existing Hybrid Renderer compatible **shaders** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

For information on how to use BRG to create a basic renderer, see [Creating a
renderer with BatchRendererGroup](batch-renderer-group-creating-a-
renderer.html).

[](batch-renderer-group-how.html)

Introduction to the BatchRendererGroup API in URP

[](batch-renderer-group-creating-a-renderer.html)

Creating a renderer with the BatchRendererGroup API in URP

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

