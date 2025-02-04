[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RenderTech-HardwareRequirements.html)
  * [中文](/cn/current/Manual/RenderTech-HardwareRequirements.html)
  * [日本語](/ja/current/Manual/RenderTech-HardwareRequirements.html)
  * [한국어](/kr/current/Manual/RenderTech-HardwareRequirements.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RenderTech-HardwareRequirements.html)
  * [中文](/cn/current/Manual/RenderTech-HardwareRequirements.html)
  * [日本語](/ja/current/Manual/RenderTech-HardwareRequirements.html)
  * [한국어](/kr/current/Manual/RenderTech-HardwareRequirements.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * Hardware requirements for the Built-in Render Pipeline

[](built-in-render-pipeline.html)

Using the Built-In Render Pipeline

[](built-in-graphics-quality-settings.html)

Graphics quality settings in the Built-In Render Pipeline

# Hardware requirements for the Built-in Render Pipeline

## Summary

|  |  |  |   
---|---|---|---|---  
| Win/Mac/Linux | iOS/Android | Consoles  
**Forward rendering** A rendering path that renders each object in one or more
passes, depending on lights that affect the object. Lights themselves are also
treated differently by Forward Rendering, depending on their settings and
intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) | Yes | Yes | Yes  
Vertex Lit rendering | Yes | Yes | -  
Realtime Shadows | GPU support | GPU support | Yes  
Image Effects | Yes | Yes | Yes  
Programmable **Shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) | Yes | Yes | Yes  
Fixed Function Shaders | Yes | Yes | -  
  
## Realtime Shadows

Realtime Shadows work on most PC, console & mobile platforms. On Windows
(Direct3D), the GPU also needs to support shadow mapping features; most
discrete GPUs support that since 2003 and most integrated GPUs support that
since 2007. Technically, on Direct3D 10, the GPU should support [D16/D24X8 or
DF16/DF24](http://aras-p.info/texts/D3D9GPUHacks.html) **texture formats** A
file format for handling textures during real-time rendering by 3D graphics
hardware, such as a graphics card or mobile device. [More info](class-
TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat); and on OpenGL it should
support the `GL_ARB_depth_texture` extension.

## Post-processing Effects

[Post-processing effects](PostProcessingOverview.html) require render-to-
texture functionality, which is generally supported on anything made in this
millenium.

## Shaders

You can write programmable or fixed function shaders. Programmable shaders are
supported everywhere, and default to Shader Model 2.0 (desktop) and OpenGL ES
3.0. (mobile). You can target higher shader models if you want to add more
functionality. Fixed function is supported everywhere except consoles.

## Additional resources

  * [Render pipeline feature comparison reference](render-pipelines-feature-comparison.html)
  * [Hardware requirements for the Univeral Render Pipeline](urp/requirements.html)

[](built-in-render-pipeline.html)

Using the Built-In Render Pipeline

[](built-in-graphics-quality-settings.html)

Graphics quality settings in the Built-In Render Pipeline

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

