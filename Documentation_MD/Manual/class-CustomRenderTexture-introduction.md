[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-CustomRenderTexture-introduction.html)
  * [中文](/cn/current/Manual/class-CustomRenderTexture-introduction.html)
  * [日本語](/ja/current/Manual/class-CustomRenderTexture-introduction.html)
  * [한국어](/kr/current/Manual/class-CustomRenderTexture-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-CustomRenderTexture-introduction.html)
  * [中文](/cn/current/Manual/class-CustomRenderTexture-introduction.html)
  * [日本語](/ja/current/Manual/class-CustomRenderTexture-introduction.html)
  * [한국어](/kr/current/Manual/class-CustomRenderTexture-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Rendering to a texture](render-texture-landing.html)
  * [Drawing to textures with shaders via Custom Render Textures](class-CustomRenderTexture-landing.html)
  * Introduction to Custom Render Textures

[](class-CustomRenderTexture-landing.html)

Drawing to textures with shaders via Custom Render Textures

[](class-CustomRenderTexture-create.html)

Create a Custom Render Texture

# Introduction to Custom Render Textures

**Custom Render Textures** are a special type of texture that allow you to
update a texture with a **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). They are an extension to [Render
Textures](class-RenderTexture.html)A special type of Texture that is created
and updated at runtime. To use them, first create a new Render Texture and
designate one of your Cameras to render into it. Then you can use the Render
Texture in a Material just like a regular Texture. [More info](class-
RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture). You can use Custom Render
Textures to create complex simulations like caustics, ripple simulation for
rain effects, and liquid splatters.

The Custom Render Textures feature provides a scripting and Shader framework
to help with complicated configuration like varying update frequency, partial
or multi-pass updates.

To use this framework you need to assign a Material to the Custom Render
Texture asset. Custom Render Textures require a compatible Material. For more
information, see [Writing a shader for a Custom Render Texture](class-
CustomRenderTexture-write-shader.html).

## Render Pipeline Compatibility

The following table describes the compatibility between the **Custom Render
Textures** feature and each **render pipeline** A series of operations that
take the contents of a Scene, and displays them on a screen. Unity lets you
choose from pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline):

Feature | Universal Render Pipeline (URP) | High Definition Render Pipeline (HDRP) | Custom Scriptable Render Pipeline (SRP) | Built-in Render Pipeline  
---|---|---|---|---  
Custom Render Textures | Yes (1) | Yes (1) | Yes (1) | Yes (1)  
  
**Note:**

  1. To create Materials that update and initialize **Custom Render Textures** in [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest), selecting **Custom Render Texture** as the target of the shader graph.

[](class-CustomRenderTexture-landing.html)

Drawing to textures with shaders via Custom Render Textures

[](class-CustomRenderTexture-create.html)

Create a Custom Render Texture

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

