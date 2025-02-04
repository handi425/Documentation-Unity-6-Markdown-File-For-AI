[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SubShader.html)
  * [中文](/cn/current/Manual/SL-SubShader.html)
  * [日本語](/ja/current/Manual/SL-SubShader.html)
  * [한국어](/kr/current/Manual/SL-SubShader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SubShader.html)
  * [中文](/cn/current/Manual/SL-SubShader.html)
  * [日本語](/ja/current/Manual/SL-SubShader.html)
  * [한국어](/kr/current/Manual/SL-SubShader.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [SubShader in ShaderLab reference](SL-SubShader-object.html)
  * SubShader block in ShaderLab reference

[](SL-SubShader-object.html)

SubShader in ShaderLab reference

[](SL-ShaderLOD.html)

LOD directive in ShaderLab reference

# SubShader block in ShaderLab reference

To define a SubShader in **ShaderLab** Unity’s language for defining the
structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab), you use a `SubShader` block. This
page contains information on using SubShader blocks.

Inside the `SubShader` block, you can:

  * Assign a **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) (level of detail) value to the SubShader,
using the `LOD` block. See [assigning a LOD value to a SubShader](SL-
ShaderLOD.html).

  * Assign key-value pairs of data to the SubShader, using the `Tags` block. See [ShaderLab: assigning tags to a SubShader](SL-SubShaderTags.html).
  * Add GPU instructions or **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code to the SubShader, using ShaderLab
commands. See [ShaderLab: using commands](SL-Reference.html).

  * Define one or more Passes, using the `Pass` block. See [ShaderLab: defining a Pass](SL-Pass.html).
  * Specify package requirements using the `PackageRequirements` block. This makes Unity only run the SubShader if the required packages are installed. See [ShaderLab: specifying package requirements](SL-PackageRequirements.html).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: SubShader block** | Yes | Yes | Yes | Yes  
  
## Syntax

**Signature** | **Function**  
---|---  
`SubShader`  
`{`  
`<optional: LOD>`  
`<optional: tags>`  
`<optional: commands>`  
`<One or more Pass definitions>`  
`}` | Defines a SubShader.  
  
You can define as many Passes as you like within a SubShader.  
  
## Additional resources

  * [Add a subshader in a custom shader](writing-shader-create-subshader-object.html)
  * [Add a shader pass in a custom shader](writing-shader-create-shader-pass.html)

[](SL-SubShader-object.html)

SubShader in ShaderLab reference

[](SL-ShaderLOD.html)

LOD directive in ShaderLab reference

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

