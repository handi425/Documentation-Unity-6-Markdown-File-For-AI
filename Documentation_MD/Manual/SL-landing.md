[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-landing.html)
  * [中文](/cn/current/Manual/SL-landing.html)
  * [日本語](/ja/current/Manual/SL-landing.html)
  * [한국어](/kr/current/Manual/SL-landing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-landing.html)
  * [中文](/cn/current/Manual/SL-landing.html)
  * [日本語](/ja/current/Manual/SL-landing.html)
  * [한국어](/kr/current/Manual/SL-landing.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * Writing a custom shader in ShaderLab and HLSL

[](shader-objects.html)

Shader object fundamentals

[](class-Shader.html)

Create a shader file

# Writing a custom shader in ShaderLab and HLSL

Resources and techniques for writing **Shader** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) objects, subshaders and shader passes
in **ShaderLab** Unity’s language for defining the structure of Shader
objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) and HLSL.

**Page** | **Description**  
---|---  
[Create a shader file](class-Shader.html) | Create a customshader asset file either using the Unity Editor or manually.  
[Add a subshader in a custom shader](writing-shader-create-subshader-object.html) | Use a `SubShader` block to add one or more sections that define different GPU settings and shader programs for different hardware, **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), and runtime settings.  
[Add a shader pass in a custom shader](writing-shader-create-shader-pass.html) | Use a `Pass` block to write instructions for setting the state of the GPU, and the shader programs that run on the GPU.  
[Include a shader pass with the UsePass command](writing-shader-usepass.html) | Insert a named Pass from another **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject), to avoid reduce code
duplication in shader source files.  
[Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html) | Resources for writing HLSL shader programs inside a `Pass` block in a custom ShaderLab shader.  
[Setting the render state on the GPU](writing-shader-render-state-commands.html) | Resources for using commands in a subshader or shader pass that change the render state on the GPU.  
  
## Additional resources

  * [Shader languages reference](shaders-reference.html)
  * [Writing custom shaders in URP](urp/writing-custom-shaders-urp.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-In Render Pipeline](built-in-shader-examples.html)

[](shader-objects.html)

Shader object fundamentals

[](class-Shader.html)

Create a shader file

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

