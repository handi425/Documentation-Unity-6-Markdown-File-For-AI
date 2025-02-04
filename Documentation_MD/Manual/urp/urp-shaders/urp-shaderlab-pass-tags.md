[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [中文](/cn/current/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [日本語](/ja/current/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [한국어](/kr/current/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [中文](/cn/current/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [日本語](/ja/current/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [한국어](/kr/current/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)

  * [Materials and shaders](../../materials-and-shaders.html)
  * [Shaders](../../Shaders.html)
  * [Shaders in URP](../../urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](../../urp/writing-custom-shaders-urp.html)
  * [Shader methods in URP](../../urp/use-built-in-shader-methods.html)
  * ShaderLab Pass tags in URP reference

[](../../urp/use-built-in-shader-methods-shadows.html)

Use shadows in a custom URP shader

[](../../urp/shaders-in-universalrp-srp-batcher.html)

Make a URP shader compatible with the SRP Batcher

# ShaderLab Pass tags in URP reference

This section contains descriptions of URP-specific **ShaderLab** Unity’s
language for defining the structure of Shader objects. [More info](../../SL-
Shader.html)  
See in [Glossary](../../Glossary.html#ShaderLab) Pass tags.

> **Note** : URP does not support the following LightMode tags: `Always`,
> `ForwardAdd`, `PrepassBase`, `PrepassFinal`, `Vertex`, `VertexLMRGBM`,
> `VertexLM`.

##  LightMode

The value of this tag lets the pipeline determine which Pass to use when
executing different parts of the **Render Pipeline** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline).

If you do not set the `LightMode` tag in a Pass, URP uses the
`SRPDefaultUnlit` tag value for that Pass.

The `LightMode` tag can have the following values.

**Property** | **Description**  
---|---  
**UniversalForward** | The Pass renders object geometry and evaluates all light contributions. URP uses this tag value in the Forward **Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath).  
**UniversalGBuffer** | The Pass renders object geometry without evaluating any light contribution. Use this tag value in Passes that Unity must execute in the Deferred Rendering Path.  
**UniversalForwardOnly** | The Pass renders object geometry and evaluates all light contributions, similarly to when **LightMode** has the **UniversalForward** value. The difference from **UniversalForward** is that URP can use the Pass for both the Forward and the Deferred Rendering Paths.  
Use this value if a certain Pass must render objects with the Forward
Rendering Path when URP is using the Deferred Rendering Path. For example, use
this tag if URP renders a scene using the Deferred Rendering Path and the
scene contains objects with shader data that does not fit the GBuffer, such as
Clear Coat normals.  
If a shader must render in both the Forward and the Deferred Rendering Paths,
declare two Passes with the `UniversalForward` and `UniversalGBuffer` tag
values.  
If a shader must render using the Forward Rendering Path regardless of the
Rendering Path that the URP Renderer uses, declare only a Pass with the
`LightMode` tag set to `UniversalForwardOnly`.  
If you use the SSAO Renderer Feature, add a Pass with the `LightMode` tag set
to `DepthNormalsOnly`. For more information, check the `DepthNormalsOnly`
value.  
**DepthNormalsOnly** | Use this value in combination with `UniversalForwardOnly` in the Deferred Rendering Path. This value lets Unity render the **shader** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) in the Depth and normal prepass.
In the Deferred Rendering Path, if the Pass with the `DepthNormalsOnly` tag
value is missing, Unity does not generate the **ambient occlusion** A method
to approximate how much ambient light (light not coming from a specific
direction) can hit a point on a surface.  
See in [Glossary](../../Glossary.html#Ambientocclusion) around the **Mesh**
The main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More
info](../../mesh.html)  
See in [Glossary](../../Glossary.html#Mesh).  
**Universal2D** | The Pass renders objects and evaluates 2D light contributions. URP uses this tag value in the 2D Renderer.  
**ShadowCaster** | The Pass renders object depth from the perspective of lights into the Shadow map or a depth texture.  
**DepthOnly** | The Pass renders only depth information from the perspective of a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) into a depth texture.  
**Meta** | Unity executes this Pass only when baking **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](../../Lightmapping.html)  
See in [Glossary](../../Glossary.html#Lightmap) in the Unity Editor. Unity
strips this Pass from shaders when building a Player.  
**SRPDefaultUnlit** | Use this `LightMode` tag value to draw an extra Pass when rendering objects. Application example: draw an object outline. This tag value is valid for both the Forward and the Deferred Rendering Paths.  
URP uses this tag value as the default value when a Pass does not have a
`LightMode` tag.  
**MotionVectors** | Use this tag to add motion vector support to your shader. For more information, refer to [Motion vector pass for ShaderLab](../features/motion-vectors-custom-shader.html).  
  
##  UniversalMaterialType

Unity uses this tag in the Deferred Rendering Path.

The `UniversalMaterialType` tag can have the following values.

If this tag is not set in a Pass, Unity uses the `Lit` value.

**Property** | **Description**  
---|---  
**Lit** | This value indicates that the shader type is Lit. During the G-buffer Pass, Unity uses stencil to mark the pixels that use the Lit shader type (specular model is PBR).  
Unity uses this value by default, if the tag is not set in a Pass.  
**SimpleLit** | This value indicates that the shader type is SimpleLit. During the G-buffer Pass, Unity uses stencil to mark the **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../../ShadowPerformance.html)  
See in [Glossary](../../Glossary.html#pixel) that use the SimpleLit shader
type (specular model is Blinn-Phong).  
  
[](../../urp/use-built-in-shader-methods-shadows.html)

Use shadows in a custom URP shader

[](../../urp/shaders-in-universalrp-srp-batcher.html)

Make a URP shader compatible with the SRP Batcher

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

