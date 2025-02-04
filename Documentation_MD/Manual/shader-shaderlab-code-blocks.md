[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-shaderlab-code-blocks.html)
  * [中文](/cn/current/Manual/shader-shaderlab-code-blocks.html)
  * [日本語](/ja/current/Manual/shader-shaderlab-code-blocks.html)
  * [한국어](/kr/current/Manual/shader-shaderlab-code-blocks.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-shaderlab-code-blocks.html)
  * [中文](/cn/current/Manual/shader-shaderlab-code-blocks.html)
  * [日本語](/ja/current/Manual/shader-shaderlab-code-blocks.html)
  * [한국어](/kr/current/Manual/shader-shaderlab-code-blocks.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [Pass in ShaderLab reference](SL-SubShader-pass.html)
  * Shader code blocks in ShaderLab reference

[](SL-PassTags.html)

Pass tags in ShaderLab reference

[](SL-Commands.html)

GPU render state commands in ShaderLab reference

# Shader code blocks in ShaderLab reference

This page contains information about using **shader** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code blocks. For information about
writing HLSL itself, see [Using HLSL in Unity](writing-shader-writing-shader-
programs-hlsl.html).

## HLSLPROGRAM and CGPROGRAM

### Render pipeline compatibility

Feature | Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) | High Definition Render Pipeline (HDRP) | Custom Scriptable Render Pipeline | Built-in Render Pipeline  
---|---|---|---|---  
HLSLPROGRAM | Yes | Yes | Yes | Yes  
CGPROGRAM | No | No | Yes  
  
Not compatible with custom render pipelines that use the [SRP Core](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest) package. | Yes  
  
### Syntax

**Signature** | **Function**  
---|---  
`HLSLPROGRAM`  
`[source code for shader programs, written in HLSL]`  
`ENDHLSL` | Adds the HLSL shader program to the Pass that includes this shader program block. Does not include Unity’s built-in shader include files.  
`CGPROGRAM`  
`[source code for shader programs, written in HLSL]`  
`ENDCG` | Adds the HLSL shader program to the Pass that includes this shader program block. Includes several of Unity’s [built-in shader include files](SL-BuiltinIncludes.html) by default, enabling you to use built-in variables and functions.  
  
## HLSLINCLUDE and CGINCLUDE

Feature | Universal Render Pipeline (URP) | High Definition Render Pipeline (HDRP) | Custom Scriptable Render Pipeline | Built-in Render Pipeline  
---|---|---|---|---  
HLSLINCLUDE | Yes | Yes | Yes | Yes  
CGINCLUDE | No | No | Yes  
  
Not compatible with custom render pipelines that use the [SRP Core](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest) package. | Yes  
  
## Syntax

**Signature** | **Function**  
---|---  
`HLSLINCLUDE`  
`[HLSL code that you want to share]`  
`ENDHLSL` | Unity includes this code in all shader programs that are defined in `HLSLPROGRAM` blocks, anywhere in this source file.  
`CGINCLUDE`  
`[HLSL code that you want to share]`  
`ENDCG` | Unity includes this code in all shader programs that are defined in `CGPROGRAM` blocks, anywhere in this source file.  
  
### HLSL and CG prefixes

The difference between the blocks that begin with `HLSL` or `CG` is:

  * The shader code blocks prefixed with `CG` are older. They include several of Unity’s [built-in shader include files](SL-BuiltinIncludes.html) by default, which can be convenient if you need this functionality. The built-in includes are only compatible with the Built-in Render Pipeline.
  * The shader code blocks prefixed with `HLSL` are newer. They do not include Unity’s built-in shader include files by default, so you must manually include any library code that you want to use. They are suitable for use with any render pipeline.

For information on Unity’s built-in shader include files, see [Built-in shader
include files](SL-BuiltinIncludes.html).

### PROGRAM and INCLUDE suffixes

The difference between the blocks that end with `PROGRAM` or `INCLUDE` is:

  * The shader code blocks that end with `PROGRAM` are called **shader program blocks**. You use them to write shader programs. You write your HLSL shader code inside these blocks, and then place them inside a Pass block in your **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code.

  * The shader code blocks that end with `INCLUDE` are called **shader include blocks**. You use them to share common code between shader program blocks in the same source file. You write HLSL shader code that you want to share inside these blocks, and then place them inside a Pass, SubShader or Shader block in your ShaderLab code. It works in a similar way to using an include in your HLSL code.

## Additional resources

  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)

[](SL-PassTags.html)

Pass tags in ShaderLab reference

[](SL-Commands.html)

GPU render state commands in ShaderLab reference

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

