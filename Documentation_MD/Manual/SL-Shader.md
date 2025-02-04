[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Shader.html)
  * [中文](/cn/current/Manual/SL-Shader.html)
  * [日本語](/ja/current/Manual/SL-Shader.html)
  * [한국어](/kr/current/Manual/SL-Shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Shader.html)
  * [中文](/cn/current/Manual/SL-Shader.html)
  * [日本語](/ja/current/Manual/SL-Shader.html)
  * [한국어](/kr/current/Manual/SL-Shader.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [Shader in ShaderLab reference](SL-Shader-object.html)
  * Shader block in ShaderLab reference

[](SL-Shader-object.html)

Shader in ShaderLab reference

[](SL-Properties.html)

Properties block reference in ShaderLab

# Shader block in ShaderLab reference

A **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object is a Unity-specific concept; it
is a wrapper for shader programs and other information. It lets you define
multiple shader programs in the same file, and tell Unity how to use them.

A **Shader object** An instance of the Shader class, a Shader object is
container for shader programs and GPU instructions, and information that tells
Unity how to use them. Use them with materials to determine the appearance of
your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject) has a nested structure; it
organizes information into structures called SubShaders and Passes.

Inside the `Shader` block, you can:

  * Define material properties, using the `Properties` block. See [ShaderLab: defining material properties](SL-Properties.html).
  * Define one or more SubShaders, using the `SubShader` block. See [ShaderLab: defining a SubShader](SL-SubShader.html).
  * Assign a [custom editor](editor-CustomEditors.html), which determines how the shader asset appears in the Unity Editor. Optionally, you can assign different custom editors for different **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). See [ShaderLab: assigning
custom editors](SL-CustomEditor.html).

  * Assign a fallback Shader object, using the `Fallback` block. See [ShaderLab: assigning a fallback](SL-Fallback.html).

## Render pipeline compatibility

**Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
****ShaderLab** : Shader block** | Yes | Yes | Yes | Yes  
  
## Syntax

**Signature** | **Function**  
---|---  
`Shader "<name>"`  
`{`  
`<optional: Material properties>`  
`<One or more SubShader definitions>`  
`<optional: custom editor>`  
`<optional: fallback>`  
`}` | Defines a Shader object with a given name.  
  
## Additional resources

  * [Define a Shader object in ShaderLab](shader-objects.html)

[](SL-Shader-object.html)

Shader in ShaderLab reference

[](SL-Properties.html)

Properties block reference in ShaderLab

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

