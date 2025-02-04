[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-UsePass.html)
  * [中文](/cn/current/Manual/SL-UsePass.html)
  * [日本語](/ja/current/Manual/SL-UsePass.html)
  * [한국어](/kr/current/Manual/SL-UsePass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-UsePass.html)
  * [中文](/cn/current/Manual/SL-UsePass.html)
  * [日本語](/ja/current/Manual/SL-UsePass.html)
  * [한국어](/kr/current/Manual/SL-UsePass.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [SubShader in ShaderLab reference](SL-SubShader-object.html)
  * UsePass directive in ShaderLab reference

[](SL-SubShaderTags.html)

SubShader tags in ShaderLab reference

[](SL-GrabPass.html)

GrabPass directive in ShaderLab reference

# UsePass directive in ShaderLab reference

For information on adding a name to a Pass in **ShaderLab** Unity’s language
for defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code, see [ShaderLab: adding a name
to a Pass](SL-Name.html).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**UsePass** | Yes | Yes | Yes | Yes  
  
## Syntax

**Signature** | **Function**  
---|---  
`UsePass "Shader object name/PASS NAME IN UPPERCASE"` | Inserts the named Pass from the named Shader object.  
  
If the named Shader object contains more than one SubShader, Unity iterates
over the SubShaders until it finds the first supported SubShader that contains
a Pass with the given name. For information on how Unity determines whether a
SubShader is supported, see [Shader objects introduction](shader-
objects.html).  
  
If the SubShader contains more than one Pass with the same name, Unity returns
the last Pass it finds.  
  
If Unity does not find a matching Pass, it shows the [error shader](shader-
error.html).  
  
## Additional resources

  * [Include a shader pass with the UsePass command](writing-shader-usepass.html)

[](SL-SubShaderTags.html)

SubShader tags in ShaderLab reference

[](SL-GrabPass.html)

GrabPass directive in ShaderLab reference

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

