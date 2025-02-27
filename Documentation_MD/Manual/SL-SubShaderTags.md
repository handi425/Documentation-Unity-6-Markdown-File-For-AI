[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SubShaderTags.html)
  * [中文](/cn/current/Manual/SL-SubShaderTags.html)
  * [日本語](/ja/current/Manual/SL-SubShaderTags.html)
  * [한국어](/kr/current/Manual/SL-SubShaderTags.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SubShaderTags.html)
  * [中文](/cn/current/Manual/SL-SubShaderTags.html)
  * [日本語](/ja/current/Manual/SL-SubShaderTags.html)
  * [한국어](/kr/current/Manual/SL-SubShaderTags.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [SubShader in ShaderLab reference](SL-SubShader-object.html)
  * SubShader tags in ShaderLab reference

[](SL-ShaderLOD.html)

LOD directive in ShaderLab reference

[](SL-UsePass.html)

UsePass directive in ShaderLab reference

# SubShader tags in ShaderLab reference

This page contains information on using a `Tags` block in your **ShaderLab**
Unity’s language for defining the structure of Shader objects. [More info](SL-
Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code to assign tags to a SubShader.

For information on defining SubShader, see [ShaderLab: defining a
SubShader](SL-SubShader.html). For information on how a **Shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object works, and the relationship
between Shader objects, SubShaders and Passes, see [Shader objects](shader-
objects.html)An instance of the Shader class, a Shader object is container for
shader programs and GPU instructions, and information that tells Unity how to
use them. Use them with materials to determine the appearance of your scene.
[More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: SubShader Tags block** | Yes | Yes | Yes | Yes  
**ShaderLab: RenderPipeline SubShader tag** | Yes | Yes | No | No  
**ShaderLab: Queue SubShader tag** | Yes | Yes  
  
| Yes  
  
**Note:** in a custom SRP, you can define your own rendering order and choose whether or not to use render queues. For more information, see DrawingSettings and SortingCriteria. | Yes  
**ShaderLab: RenderType SubShader tag** | Yes | Yes | Yes | Yes  
**ShaderLab: DisableBatching SubShader tag** | Yes | Yes | Yes | Yes  
**ShaderLab: ForceNoShadowCasting SubShader tag** | Yes | Yes  
  
This disables regular shadows, but has no effect on contact shadows. | Yes | Yes  
**ShaderLab: CanUseSpriteAtlas SubShader tag** | Yes | Yes | Yes | Yes  
**ShaderLab: PreviewType SubShader tag** | Yes | Yes | Yes | Yes  
  
## Syntax

**Signature** | **Function**  
---|---  
Tags { “[name1]” = “[value1]” “[name2]” = “[value2]”} | Applies the given tags to the SubShader.  
  
You can define as many tags as you like.  
  
### RenderPipeline tag

**Signature** | **Function**  
---|---  
“RenderPipeline” = “[name]” | Tells Unity whether this SubShader is compatible with URP or HDRP.  
**Parameter** | **Value** | **Function**  
---|---|---  
[name] | `UniversalPipeline` | This SubShader is compatible with URP only.  
| `HDRenderPipeline` | This SubShader is compatible with HDRP only.  
| (any other value, or not declared) | This SubShader is not compatible with URP or HDRP.  
  
### Queue tag

**Signature** | **Function**  
---|---  
“Queue” = “[queue name]” | Use the named render queue.  
“Queue” = “[queue name] + [offset]” | Use an unnamed queue, at a given offset from the named queue.  
  
An example of when this is useful is in the case of transparent water, which
you should draw after opaque objects but before transparent objects.  
**Signature** | **Value** | **Function**  
---|---|---  
[queue name] | Background | Specifies the Background render queue.  
| Geometry | Specifies the Geometry render queue.  
| AlphaTest | Specifies the AlphaTest render queue.  
| Transparent | Specifies the Transparent render queue.  
| Overlay | Specifies the Overlay render queue.  
[offset] | integer | Specifies the index at which Unity renders the unnamed queue, relative to the named queue.  
  
### RenderType tag

**Signature** | **Function**  
---|---  
“RenderType” = “[renderType]” | Set the RenderType value for this SubShader.  
**Signature** | **Value** | **Function**  
---|---|---  
[renderType] | String | There are no set values for this parameter. To identify the RenderType value for any SubShader that you want to replace, open its shader source file.  
  
The `RenderType` SubShader tags for Unity’s legacy built-in shaders are listed
on the [shader replacement page](SL-ShaderReplacement.html).  
  
You can also create your own values for your custom SubShaders.  
  
### ForceNoShadowCasting tag

**Signature** | **Function**  
---|---  
“ForceNoShadowCasting” = “[state]” | Whether to prevent shadow casting (and sometimes receiving) for all geometry that uses this SubShader.  
**Signature** | **Value** | **Function**  
---|---|---  
[state] | True | Unity prevents the geometry in this SubShader from casting shadows.  
  
In the Built in Render Pipeline, with the Forward or Legacy Vertex Lit
rendering paths, Unity also prevents the geometry in this SubShader from
receiving shadows.  
  
In HDRP, this does not prevent the geometry from casting contact shadows.  
| False | Unity does not prevent the geometry in this SubShader from casting or receiving shadows. This is the default value.  
  
### DisableBatching tag

**Signature** | **Function**  
---|---  
“DisableBatching” = “[state]” | Whether Unity prevents **Dynamic Batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) for all geometry that uses
this SubShader.  
**Signature** | **Value** | **Function**  
---|---|---  
[state] | True | Unity prevents Dynamic Batching for geometry that uses this SubShader.  
| False | Unity does not prevent Dynamic Batching for geometry that uses this SubShader. This is the default value.  
| LODFading | Unity prevents Dynamic Batching for all geometry that is part of a [LODGroup](https://docs.unity3d.com/Manual/class-LODGroup.html) with a Fade Mode value that is not None. Otherwise, Unity does not prevent Dynamic Batching.  
  
## IgnoreProjector tag

**Signature** | **Function**  
---|---  
“IgnoreProjector” = “[state]” | Whether Unity ignores Projectors when rendering this geometry.  
**Signature** | **Value** | **Function**  
---|---|---  
[state] | True | Unity ignores Projectors when rendering this geometry.  
| False | Unity does not ignore Projectors when rendering this geometry. This is the default value.  
  
### PreviewType tag

The `PreviewType` SubShader Tag tells the Unity Editor how to display a
material that uses this SubShader in the Material **Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

**Signature** | **Function**  
---|---  
“PreviewType” = “[shape]” | Which shape the Unity Editor uses to display a preview of a material that uses this SubShader.  
**Signature** | **Value** | **Function**  
---|---|---  
[shape] | Sphere | Display the material on a sphere. This is the default value.  
| Plane | Display the material on a plane.  
| **Skybox** A special type of Material used to represent skies. Usually six-
sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) | Display the material on a skybox.  
  
## Additional resources

  * [Add a shader tag to a SubShader or Pass](add-shader-tag.html)
  * [Configure if or when Unity uses a shader](writing-shader-tags.html)

[](SL-ShaderLOD.html)

LOD directive in ShaderLab reference

[](SL-UsePass.html)

UsePass directive in ShaderLab reference

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

