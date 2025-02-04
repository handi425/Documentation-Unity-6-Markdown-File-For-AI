[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Cull.html)
  * [中文](/cn/current/Manual/SL-Cull.html)
  * [日本語](/ja/current/Manual/SL-Cull.html)
  * [한국어](/kr/current/Manual/SL-Cull.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Cull.html)
  * [中文](/cn/current/Manual/SL-Cull.html)
  * [日本語](/ja/current/Manual/SL-Cull.html)
  * [한국어](/kr/current/Manual/SL-Cull.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * Cull command in ShaderLab reference

[](SL-Conservative.html)

Conservative command in ShaderLab reference

[](SL-Offset.html)

Offset command in ShaderLab reference

# Cull command in ShaderLab reference

Sets which polygons the GPU should cull, based on the direction that they are
facing relative to the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Cull** | Yes | Yes | Yes | Yes  
  
## Syntax

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

**Signature** | **Example syntax** | **Function**  
---|---|---  
`Cull <state>` | `Cull Back` | Sets which polygons the GPU should cull, based on the direction that they face relative to the camera.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
**state** | `Back` | Cull polygons that face away from the camera. This is called back-face culling.  
  
This is the default value.  
| `Front` | Cull polygons that face towards the camera. This is called front-face culling.  
  
Use this for turning geometry inside-out.  
| `Off` | Do not cull polygons based on the direction that they face.  
  
Use this for special effects, such as transparent objects or double-sided
walls.  
  
## Additional resources

  * [Set the culling mode in a shader](set-culling-mode.html)

[](SL-Conservative.html)

Conservative command in ShaderLab reference

[](SL-Offset.html)

Offset command in ShaderLab reference

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

