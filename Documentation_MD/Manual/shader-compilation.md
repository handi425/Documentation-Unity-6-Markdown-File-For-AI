[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-compilation.html)
  * [中文](/cn/current/Manual/shader-compilation.html)
  * [日本語](/ja/current/Manual/shader-compilation.html)
  * [한국어](/kr/current/Manual/shader-compilation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-compilation.html)
  * [中文](/cn/current/Manual/shader-compilation.html)
  * [日本語](/ja/current/Manual/shader-compilation.html)
  * [한국어](/kr/current/Manual/shader-compilation.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Troubleshooting shaders](shader-troubleshooting.html)
  * [Reducing the size or number of shaders](shader-reducing.html)
  * Shader compilation

[](shader-reducing.html)

Reducing the size or number of shaders

[](shader-variants-landing.html)

Reducing shader variants

# Shader compilation

Every time you build your project, the Unity Editor compiles all the shaders
that your build requires: every required **shader** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) variant, for every required graphics
API.

When you’re working in the Unity Editor, the Editor does not compile
everything upfront. This is because compiling every variant for every graphics
API can take a very long time.

Instead, Unity Editor does this:

  * When it imports a shader asset, it performs some minimal processing (such as Surface Shader generation).
  * When it needs to show a shader variant, it checks the `Library/ShaderCache` folder.
  * If it finds a previously compiled shader variant that uses identicial source code, it uses that.
  * If it does not find a match, it compiles the required shader variant and saves the result to the cache. 
    * **Note:** If you enable [Asynchronous shader compilation](AsynchronousShaderCompilation.html), it does this in the background and shows a placeholder shader in the meantime.

Shader compilation is carried out using a process called
`UnityShaderCompiler`. Multiple `UnityShaderCompiler` processes can be started
(generally one per CPU core in your machine), so that at player build time
shader compilation can be done in parallel. While the Editor is not compiling
shaders, the compiler processes do nothing and do not consume computer
resources.

The shader cache folder can become quite large, if you have a lot of shaders
that are changed often. It is safe to delete this folder; it just causes Unity
to recompile the shader variants.

At player build time, all the “not yet compiled” shader variants are compiled,
so that they are in the game data even if the editor did not happen to use
them.

## Different shader compilers

Different platforms use different shader compilers for [shader
program](writing-shader-writing-shader-programs-hlsl.html) compilation as
follows:

  * Platforms that use DirectX use Microsoft’s FXC HLSL compiler.
  * Platforms that use OpenGL (Core & ES) use Microsoft’s FXC HLSL compiler, followed by bytecode translation into GLSL using [HLSLcc](https://github.com/Unity-Technologies/HLSLcc).
  * Platforms that use Metal use Microsoft’s FXC HLSL compiler, followed by bytecode translation into Metal, using [HLSLcc](https://github.com/Unity-Technologies/HLSLcc).
  * Platforms that use Vulkan use Microsoft’s FXC HLSL compiler, followed by bytecode translation into SPIR-V, using [HLSLcc](https://github.com/Unity-Technologies/HLSLcc).
  * Other platforms, such as console platforms, use their respective compilers.
  * [Surface Shaders](SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) use HLSL and
[MojoShader](https://icculus.org/mojoshader/) for code generation analysis
step.

You can configure various shader compiler settings using [pragma
directives](SL-PragmaDirectives.html).

## The Caching Shader Preprocessor

Shader compilation involves several steps. One of the first steps is
preprocessing. During this step, a program called a **preprocessor** prepares
the shader source code for the compiler.

In previous versions of Unity, the Editor used the preprocessor provided by
the shader compiler for the current platform. Now, Unity uses its own
preprocessor, also called the Caching Shader Preprocessor.

The Caching Shader Preprocessor is optimized for faster shader import and
compilation. It works by caching intermediate preprocessing data, so the
Editor only needs to parse include files when their contents change, which
makes compiling multiple variants of the same shader more efficient.

For detailed information on the differences between the Caching Shader
Preprocessor and the previous behavior, see the Unity forum: [New shader
preprocessor](https://forum.unity.com/threads/new-shader-
preprocessor.790328/).

## Build time stripping

While building the game, Unity can detect that some of the internal shader
variants are not used by the game, and exclude (“strip”) them from build data.
For more information, see [Shader variants](shader-variants.html)A verion of a
shader program that Unity generates according to a specific combination of
shader keywords and their status. A Shader object can contain multiple shader
variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant).

[](shader-reducing.html)

Reducing the size or number of shaders

[](shader-variants-landing.html)

Reducing shader variants

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

