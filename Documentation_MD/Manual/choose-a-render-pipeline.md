[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/choose-a-render-pipeline.html)
  * [中文](/cn/current/Manual/choose-a-render-pipeline.html)
  * [日本語](/ja/current/Manual/choose-a-render-pipeline.html)
  * [한국어](/kr/current/Manual/choose-a-render-pipeline.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/choose-a-render-pipeline.html)
  * [中文](/cn/current/Manual/choose-a-render-pipeline.html)
  * [日本語](/ja/current/Manual/choose-a-render-pipeline.html)
  * [한국어](/kr/current/Manual/choose-a-render-pipeline.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Choosing a render pipeline](choose-a-render-pipeline-landing.html)
  * Choose a render pipeline

[](choose-a-render-pipeline-landing.html)

Choosing a render pipeline

[](render-pipelines-feature-comparison.html)

Render pipeline feature comparison reference

# Choose a render pipeline

It’s important to choose the right [Unity render pipeline](render-pipelines-
overview.html) for your project when you’re early in development.

Different **render pipelines** A series of operations that take the contents
of a Scene, and displays them on a screen. Unity lets you choose from pre-
built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) have different capabilities
and perform differently, so they work best for different games, applications,
and platforms.

It can be very time-consuming to switch a project from one render pipeline to
another, especially if the project is far along in development. Different
render pipelines use different **shaders** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) and might not have the same features.

The table shows some high-level differences between the pipelines to help you
choose the right pipeline for your project at the start.

**Note:** You can’t use the Universal Render Pipeline and the High Definition
Render Pipeline (HDRP) at the same time. They’re both built with the
Scriptable Render Pipeline (SRP), but their render paths and light models are
different.

**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Built-In Render Pipeline**  
---|---|---|---  
Target uses | Projects that need rendering scalability across all platforms, especially tile-based deferred rendering (TBDR) platforms, and untethered VR platforms.  
  
Projects that need to extend and customize the rendering pipeline.  
  
2D and 3D projects. | Projects that need photorealism and high-fidelity rendering on high-end platforms  
  
3D projects | Projects that need rendering scalability across all platforms.  
  
2D and 3D projects.  
Platform support | Supports all Unity-supported platforms  
  
Focuses on efficiency on tile-based deferred rendering (TBDR) platforms, and untethered VR platforms | Supports desktop, Xbox and PlayStation platforms  
  
Focuses on efficiently using advanced GPU hardware capabilities such as async compute shaders, and ray tracing if the hardware supports it.  | Supports all Unity-supported platforms   
Source code access | Mostly C#  
  
Public access to [the URP source code on GitHub](https://github.com/Unity-
Technologies/Graphics/tree/master/Packages/com.unity.render-
pipelines.universal). You can also create a custom pipeline using URP as a
base  
  
Easier to read, change, and extend the source code than the Built-In Render Pipeline | Mostly C#  
  
Public access to [the HDRP source code on GitHub](https://github.com/Unity-
Technologies/Graphics/tree/master/Packages/com.unity.render-pipelines.high-
definition). You can also create a custom pipeline using HDRP as a base  
  
Easier to read, change, and extend the source code than the Built-In Render Pipeline | Mostly C++  
  
Private access by [purchasing source code
access](https://unity.com/products/source-code)  
Pipeline extension | The API and injection points the pipeline provides, or you can modify the publicly available source code  
  
Easier to extend than the Built-In Render Pipeline | The API and injection points the pipeline provides, or you can modify the publicly available source code  
  
Easier to extend than the Built-In Render Pipeline, but more difficult than URP because HDRP is complex and has advanced features | The API and injection points the pipeline provides   
Customization through artist tooling |  [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.0/manual/index.html), which you can use to customize shading, materials, and screen space effects   
  
[Built-in Particle System](PartSysUsage.html), which you can use to customize
visual effects.Limited customization  
  
[VFX Graph](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@17.0/manual/index.html), which you can use to design visual effects, from simple common particle behaviors to complex simulations running on the GPU.  |  [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.0/manual/index.html), which you can use to customize shading, materials, and screen space effects   
  
[Built-in Particle System](PartSysUsage.html), which you can use to customize
visual effects. Limited customization  
  
[VFX Graph](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@17.0/manual/index.html), which you can use to design visual effects, from simple common particle behaviors to complex simulations running on the GPU.  |  [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.0/manual/index.html), which you can use to customize shading, materials, and screen space effects  
  
Shader Graph doesn’t receive updates for Built-In Render Pipeline support,
aside from bug fixes for existing features  
  
[Built-in Particle System](PartSysUsage.html), which you can use to customize
visual effects. Limited customization  
Customization through hand-coded shaders  | HLSL shaders, and URP shaders in the source code that you can customize | HLSL shaders, and HDRP shaders in the source code that you can customize  
  
Hand-coded shaders are recommended for advanced users only, because HDRP shaders are complex and have advanced features | HLSL shaders and [surface shaders](SL-SurfaceShaders.html)  
Lighting | Designed for both realistic and stylized lighting  
  
Basic PBR, and some advanced PBR such as clear coat  
  
Easier to customize for custom lighting models such as cel shading | Focuses on photorealism and physically accurate lighting with built-in support for physical light units  
  
Basic and advanced PBR. For example clear coat, skin, hair, eyes, subsurface
scattering and water  
  
Advanced screen space and volumetric effects  
  
Harder to customize for custom lighting models such as cel shading | Designed for both realistic and stylized lighting  
  
Basic physically-based rendering (PBR)  
  
Easier to customize for custom lighting models such as cel shading  
Performance | Supports [static batching](static-batching.html) and [dynamic batching](dynamic-batching.html)   
  
Advanced draw call batching with the [Scriptable Render Pipeline (SRP)
Batcher](SRPBatcher.html)  
  
Compatible with the [BatchRenderer Group](batch-renderer-group.html) API, and [Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/index.html) | Supports [static batching](static-batching.html)  
  
Advanced draw call batching with the [Scriptable Render Pipeline (SRP)
Batcher](SRPBatcher.html)  
  
Compatible with the [BatchRenderer Group](batch-renderer-group.html) API, and [Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/index.html) | Supports [static batching](static-batching.html) and [dynamic batching](dynamic-batching.html)  
  
Refer to [Render pipeline feature comparison](render-pipelines-feature-
comparison.html) for detailed information about which pipeline is compatible
with which features, to help you choose the right pipeline for your project.

## Additional resources

  * [Universal Render Pipeline](universal-render-pipeline.html)
  * [High Definition Render Pipeline](high-definition-render-pipeline.html)
  * [Creating Believable Visuals tutorial](https://unity3d.com/learn/tutorials/s/creating-believable-visuals) for the Built-In Render Pipeline
  * [Creating a custom render pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/srp-custom.html)

[](choose-a-render-pipeline-landing.html)

Choosing a render pipeline

[](render-pipelines-feature-comparison.html)

Render pipeline feature comparison reference

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

