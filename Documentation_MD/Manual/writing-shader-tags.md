[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-tags.html)
  * [中文](/cn/current/Manual/writing-shader-tags.html)
  * [日本語](/ja/current/Manual/writing-shader-tags.html)
  * [한국어](/kr/current/Manual/writing-shader-tags.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-tags.html)
  * [中文](/cn/current/Manual/writing-shader-tags.html)
  * [日本語](/ja/current/Manual/writing-shader-tags.html)
  * [한국어](/kr/current/Manual/writing-shader-tags.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * Configure when and if Unity uses a shader

[](SL-MultipleProgramVariants-shortcuts.html)

Add built-in keyword sets

[](writing-shader-tags-introduction.html)

Introduction to shader tags

# Configure when and if Unity uses a shader

Resources for using tags and blocks in a **shader** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) to configure if and when Unity uses
the shader.

**Page** | **Description**  
---|---  
[Introduction to shader tags](writing-shader-tags-introduction.html) | Understand creating tags, accessing their values in **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), and how tags vary by pipeline.  
[Add a shader tag to a SubShader or Pass](add-shader-tag.html) | Assign tags to a subshader or a shader pass by placing a `Tags` block.  
[Set a shader to require URP or HDRP](writing-shader-tags-pipeline.html) | Use a `RenderPipeline` tag to require the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) or the High Definition Render
Pipeline.  
[Set a shader to require a graphics API or platform](SL-ShaderCompilationAPIs.html) | Use a `#pragma` directive to target a graphics API or platform.  
[Set a shader to require a shader model or GPU feature](SL-ShaderCompileTargets.html) | Use a `#pragma` directive to target a shader model or GPU feature.  
[set a shader to require a package](writing-shader-tags-require-package.html) | Use a `PackageRequirements` block to add package requirements to a SubShader or Pass.  
[Set the render queue of a shader](writing-shader-tags-set-render-queue.html) | Use a `Queue` tag to set when Unity runs a shader.  
[Set when Unity runs a shader pass via a LightMode tag](writing-shader-tags-set-pass.html) | Use a `LightMode` tag to set when Unity runs a shader.  
[Prioritize lower quality shaders with the LOD command](writing-shader-prioritize-lower-quality-shaders.html) | Use a `LOD` command to fine-tune shader performance on different hardware.  
[Disable dynamic batching of a shader](writing-shader-tags-disable-dynamic-batching.html) | Use a `DisableBatching` tag to prevent Unity from applying **dynamic batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) to geometry.  
[Get tag values in C#](writing-shader-tags-get-tag-value.html) | Use APIs to get the value of tags in a subshader or a shader pass  
[Troubleshooting package requirement definitions](writing-shader-tags-require-package-troubleshooting.html) | Solve common issues with the `PackageRequirements` block, such as incorrect version values.  
  
[](SL-MultipleProgramVariants-shortcuts.html)

Add built-in keyword sets

[](writing-shader-tags-introduction.html)

Introduction to shader tags

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

