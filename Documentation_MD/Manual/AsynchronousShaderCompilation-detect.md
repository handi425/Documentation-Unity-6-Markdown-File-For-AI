[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AsynchronousShaderCompilation-detect.html)
  * [中文](/cn/current/Manual/AsynchronousShaderCompilation-detect.html)
  * [日本語](/ja/current/Manual/AsynchronousShaderCompilation-detect.html)
  * [한국어](/kr/current/Manual/AsynchronousShaderCompilation-detect.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AsynchronousShaderCompilation-detect.html)
  * [中文](/cn/current/Manual/AsynchronousShaderCompilation-detect.html)
  * [日本語](/ja/current/Manual/AsynchronousShaderCompilation-detect.html)
  * [한국어](/kr/current/Manual/AsynchronousShaderCompilation-detect.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Troubleshooting shaders](shader-troubleshooting.html)
  * [Fixing hitches or stalls](shader-reduce-stalling.html)
  * [Asynchronous shader compilation in the Editor](AsynchronousShaderCompilation.html)
  * Detect asynchronous shader compilation

[](AsynchronousShaderCompilation-enable-or-disable.html)

Enable or disable asynchronous shader compilation

[](AsynchronousShaderCompilation-avoid-cyan-placeholder-shaders.html)

Troubleshooting asynchronous shader compilation

# Detect asynchronous shader compilation

You can use C# APIs to monitor the state of asynchronous **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) compilation, and perform operations
when this state changes.

This is most likely useful in [advanced
rendering](AsynchronousShaderCompilation-avoid-cyan-placeholder-shaders.html);
if the placeholder shader pollutes your generated data, you can wait until
compilation is complete, discard the polluted data, and regenerate a new set
with the correct shader variants.

If you already know which material you are interested in, you can use
`ShaderUtil.IsPassCompiled` to check the compilation status of the shader
variant. When the status changes _Uncompiled_ to _Compiled_ , compilation is
complete.

If you do not know which material you are interested in, or if you are
interested in more than one material, you can use
`ShaderUtil.anythingCompiling` to detect whether Unity is compiling any shader
variants asynchronously. When this changes from `true` to `false`, all current
compilation is complete.

[](AsynchronousShaderCompilation-enable-or-disable.html)

Enable or disable asynchronous shader compilation

[](AsynchronousShaderCompilation-avoid-cyan-placeholder-shaders.html)

Troubleshooting asynchronous shader compilation

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

