[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-CustomEditor.html)
  * [中文](/cn/current/Manual/SL-CustomEditor.html)
  * [日本語](/ja/current/Manual/SL-CustomEditor.html)
  * [한국어](/kr/current/Manual/SL-CustomEditor.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-CustomEditor.html)
  * [中文](/cn/current/Manual/SL-CustomEditor.html)
  * [日本語](/ja/current/Manual/SL-CustomEditor.html)
  * [한국어](/kr/current/Manual/SL-CustomEditor.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [Shader in ShaderLab reference](SL-Shader-object.html)
  * Custom Editor block in ShaderLab reference

[](SL-Fallback.html)

Fallback block in ShaderLab reference

[](SL-SubShader-object.html)

SubShader in ShaderLab reference

# Custom Editor block in ShaderLab reference

This page contains information on using a `CustomEditor` or
`CustomEditorForRenderPipeline` block in your **ShaderLab** Unity’s language
for defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code to assign [custom
editors](editor-CustomEditors.html).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: CustomEditor block** | Yes | Yes | Yes | Yes  
**ShaderLab: CustomEditorForRenderPipeline block** | Yes | Yes | Yes | No  
  
## Syntax

**Signature** | **Function**  
---|---  
`CustomEditor "[custom editor class name]"` | Unity uses the custom editor defined in the named class, unless this is overridden by a `CustomEditorForRenderPipeline` block.  
`CustomEditorForRenderPipeline "[custom editor class name]" "[render pipeline asset class name]"` | When the active Render Pipeline Asset is the named type, Unity uses the custom editor defined in the named class.  
  
## Additional resources

  * [Adding material properties to shaders](writing-shader-change-properties.html)

[](SL-Fallback.html)

Fallback block in ShaderLab reference

[](SL-SubShader-object.html)

SubShader in ShaderLab reference

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

