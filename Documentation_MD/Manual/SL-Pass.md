[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Pass.html)
  * [中文](/cn/current/Manual/SL-Pass.html)
  * [日本語](/ja/current/Manual/SL-Pass.html)
  * [한국어](/kr/current/Manual/SL-Pass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Pass.html)
  * [中文](/cn/current/Manual/SL-Pass.html)
  * [日本語](/ja/current/Manual/SL-Pass.html)
  * [한국어](/kr/current/Manual/SL-Pass.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [Pass in ShaderLab reference](SL-SubShader-pass.html)
  * Pass block in ShaderLab reference

[](SL-SubShader-pass.html)

Pass in ShaderLab reference

[](SL-Name.html)

Name directive in ShaderLab reference

# Pass block in ShaderLab reference

To define a Pass in **ShaderLab** Unity’s language for defining the structure
of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab), use a `Pass` block. This page
contains information on using `Pass` blocks. For information on how a
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object works, and the relationship
between **Shader objects** An instance of the Shader class, a Shader object is
container for shader programs and GPU instructions, and information that tells
Unity how to use them. Use them with materials to determine the appearance of
your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject), SubShaders and Passes, see
[Shader object fundamentals](Shaders.html).

Inside the `Pass` block, you can:

  * Assign a name to the Pass, using a Name block. See [ShaderLab: assigning a name to a Pass](SL-Name.html).
  * Assign key-value pairs of data to the Pass, using a Tags block. See [ShaderLab: assigning tags to a Pass](SL-PassTags.html).
  * Perform operations using ShaderLab commands. See [ShaderLab: using commands](SL-Reference.html).
  * Add shader code to the Pass, using a shader code block. See [ShaderLab: shader code blocks](shader-shaderlab-code-blocks.html).
  * Specify package requirements using the `PackageRequirements` block. This makes Unity only run the Pass if the required packages are installed. See [ShaderLab: specifying package requirements](SL-PackageRequirements.html).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: Pass block** | Yes | Yes | Yes | Yes  
  
## Syntax

**Signature** | **Function**  
---|---  
`Pass`  
`{`  
`<optional: name>`  
`<optional: tags>`  
`<optional: commands>`  
`<optional: shader code>`  
`}` | Defines a Pass.  
  
## Additional resources

  * [Add a shader pass in a custom shader](writing-shader-create-shader-pass.html)

[](SL-SubShader-pass.html)

Pass in ShaderLab reference

[](SL-Name.html)

Name directive in ShaderLab reference

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

