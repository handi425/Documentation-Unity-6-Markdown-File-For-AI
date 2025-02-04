[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-UnityShaderVariables.html)
  * [中文](/cn/current/Manual/SL-UnityShaderVariables.html)
  * [日本語](/ja/current/Manual/SL-UnityShaderVariables.html)
  * [한국어](/kr/current/Manual/SL-UnityShaderVariables.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-UnityShaderVariables.html)
  * [中文](/cn/current/Manual/SL-UnityShaderVariables.html)
  * [日本語](/ja/current/Manual/SL-UnityShaderVariables.html)
  * [한국어](/kr/current/Manual/SL-UnityShaderVariables.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * Built-in shader variables reference

[](SL-Pragma-require.html)

HLSL pragma require command reference

[](Materials.html)

Materials

# Built-in shader variables reference

Unity’s built-in include files contain global variables for your **shaders** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader): things like current object’s
transformation matrices, light parameters, current time and so on. You use
them in [shader programs](writing-shader-writing-shader-programs-hlsl.html)
like any other variable, but if you include the relevant include file, you
don’t have to declare them.

For more information on include files, see [Built-in include files](SL-
BuiltinIncludes.html).

## Transformations

All these matrices are `float4x4` type, and are column major.

|  
---|---  
**Name** | **Value**  
UNITY_MATRIX_MVP | Current model * view * projection matrix.  
UNITY_MATRIX_MV | Current model * view matrix.  
UNITY_MATRIX_V | Current view matrix.  
UNITY_MATRIX_P | Current projection matrix.  
UNITY_MATRIX_VP | Current view * projection matrix.  
UNITY_MATRIX_T_MV | Transpose of model * view matrix.  
UNITY_MATRIX_IT_MV | Inverse transpose of model * view matrix.  
unity_ObjectToWorld | Current model matrix.  
unity_WorldToObject | Inverse of current world matrix.  
  
## Camera and screen

These variables will correspond to the [Camera](class-Camera.html)A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) that is rendering. For example during
shadowmap rendering, they will still refer to the Camera component values, and
not the “virtual camera” that is used for the shadowmap projection.

**Name** | **Type** | **Value**  
---|---|---  
_WorldSpaceCameraPos | float3 | World space position of the camera.  
_ProjectionParams | float4 |  `x` is 1.0 (or –1.0 if currently rendering with a [flipped projection matrix](SL-PlatformDifferences.html)), `y` is the camera’s near plane, `z` is the camera’s far plane and `w` is 1/FarPlane.  
_ScreenParams | float4 |  `x` is the width of the camera’s target texture in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel), `y` is the height of the camera’s
target texture in pixels, `z` is 1.0 + 1.0/width and `w` is 1.0 + 1.0/height.  
_ZBufferParams | float4 | Used to linearize Z buffer values.  
| `x` |  |  `1-far/near`, or `-1+far/near` if `UNITY_REVERSED_Z` is set to 1. For more information about `UNITY_REVERSED_Z`, refer to [Branch based on platform features](shader-branching-platform.html)  
| `y` |  |  `far/near`, or `1` if `UNITY_REVERSED_Z` is set to 1. For more information about `UNITY_REVERSED_Z`, refer to [Branch based on platform features](shader-branching-platform.html)  
| `z` |  | `x/far`  
| `w` |  | `y/far`  
unity_OrthoParams | float4 |  `x` is orthographic camera’s width, `y` is orthographic camera’s height, `z` is unused and `w` is 1.0 when camera is orthographic, 0.0 when perspective.  
unity_CameraProjection | float4x4 | Camera’s projection matrix.  
unity_CameraInvProjection | float4x4 | Inverse of camera’s projection matrix.  
unity_CameraWorldClipPlanes[6] | float4 | Camera frustum plane world space equations, in this order: left, right, bottom, top, near, far.  
  
## Time

Time is measured in seconds, and is scaled by the Time multiplier in your
Project’s [Time settings](class-TimeManager.html). There is no built-in
variable that provides access to unscaled time.

|  |   
---|---|---  
**Name** | **Type** | **Value**  
_Time | float4 | Time since level load (t/20, t, t*2, t*3), use to animate things inside the shaders.  
_SinTime | float4 | Sine of time: (t/8, t/4, t/2, t).  
_CosTime | float4 | Cosine of time: (t/8, t/4, t/2, t).  
unity_DeltaTime | float4 | Delta time: (dt, 1/dt, smoothDt, 1/smoothDt).  
  
## Lighting

Light parameters are passed to shaders in different ways depending on which
[Rendering Path](RenderingPaths.html)The technique that a render pipeline uses
to render graphics. Choosing a different rendering path affects how lighting
and shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) is used, and which LightMode
[Pass Tag](SL-PassTags.html) is used in the shader.

[Forward rendering](RenderTech-ForwardRendering.html)A rendering path that
renders each object in one or more passes, depending on lights that affect the
object. Lights themselves are also treated differently by Forward Rendering,
depending on their settings and intensity. [More info](RenderTech-
ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) (`ForwardBase` and
`ForwardAdd` pass types):

|  |   
---|---|---  
**Name** | **Type** | **Value**  
_LightColor0 _(declared in UnityLightingCommon.cginc)_ | fixed4 | Light color.  
_WorldSpaceLightPos0 | float4 | Directional lights: (world space direction, 0). Other lights: (world space position, 1).  
unity_WorldToLight _(declared in AutoLight.cginc)_ | float4x4 | World-to-light matrix. Used to sample cookie & attenuation textures.  
unity_4LightPosX0, unity_4LightPosY0, unity_4LightPosZ0 | float4 |  _(ForwardBase pass only)_ world space positions of first four non-important point lights.  
unity_4LightAtten0 | float4 |  _(ForwardBase pass only)_ attenuation factors of first four non-important point lights.  
unity_LightColor | half4[4] |  _(ForwardBase pass only)_ colors of of first four non-important point lights.  
unity_WorldToShadow | float4x4[4] | World-to-shadow matrices. One matrix for Spot Lights, up to four for directional light cascades.  
  
Deferred shading, used in the lighting pass shader (all declared in
UnityDeferredLibrary.cginc):

|  |   
---|---|---  
**Name** | **Type** | **Value**  
_LightColor | float4 | Light color.  
unity_WorldToLight | float4x4 | World-to-light matrix. Used to sample cookie & attenuation textures.  
unity_WorldToShadow | float4x4[4] | World-to-shadow matrices. One matrix for Spot Lights, up to four for directional light cascades.  
  
Spherical harmonics coefficients (used by ambient and light probes) are set up
for `ForwardBase` and `Deferred` pass types. They contain 3rd order SH to be
evaluated by world space normal (see `ShadeSH9` from [UnityCG.cginc](SL-
BuiltinIncludes.html)). The variables are all half4 type, `unity_SHAr` and
similar names.

[Vertex-lit rendering](RenderTech-VertexLit.html) (`Vertex` pass type):

Up to 8 lights are set up for a `Vertex` pass type; always sorted starting
from the brightest one. So if you want to render objects affected by two
lights at once, you can just take first two entries in the arrays. If there
are fewer than eight lights affecting the object, the rest will have their
color set to black.

|  |   
---|---|---  
**Name** | **Type** | **Value**  
unity_LightColor | half4[8] | Light colors.  
unity_LightPosition | float4[8] | View-space light positions. (-direction,0) for directional lights; (position,1) for Point or Spot Lights.  
unity_LightAtten | half4[8] | Light attenuation factors. _x_ is cos(spotAngle/2) or –1 for non-Spot Lights; _y_ is 1/cos(spotAngle/4) or 1 for non-Spot Lights; _z_ is quadratic attenuation; _w_ is squared light range.  
unity_SpotDirection | float4[8] | View-space Spot Lights positions; (0,0,1,0) for non-Spot Lights.  
  
## Lightmaps

|  |   
---|---|---  
**Name** | **Type** | **Value**  
unity_Lightmap | Texture2D | Contains **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) information.  
unity_LightmapST | float4[8] | Scales and translates the UV information to the correct range to sample the lightmap texture.  
  
## Fog and Ambient

|  |   
---|---|---  
**Name** | **Type** | **Value**  
unity_AmbientSky | fixed4 | Sky ambient lighting color in gradient ambient lighting case.  
unity_AmbientEquator | fixed4 | Equator ambient lighting color in gradient ambient lighting case.  
unity_AmbientGround | fixed4 | Ground ambient lighting color in gradient ambient lighting case.  
unity_IndirectSpecColor | fixed4 | If you use a [skybox](skyboxes-using.html)A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox), this is the average color of the
skybox, which Unity calculates using the `DC` component of the [spherical
harmonics data](LightProbes-TechnicalInformation.html) in the [ambient
probe](../ScriptReference/RenderSettings-ambientProbe.html). Otherwise this is
black.  
UNITY_LIGHTMODEL_AMBIENT | fixed4 | Ambient lighting color (sky color in gradient ambient case). Legacy variable.  
unity_FogColor | fixed4 | Fog color.  
unity_FogParams | float4 | Parameters for fog calculation: (density / sqrt(ln(2)), density / ln(2), –1/(end-start), end/(end-start)). _x_ is useful for Exp2 fog mode, _y_ for Exp mode, _z_ and _w_ for Linear mode.  
  
## Various

|  |   
---|---|---  
**Name** | **Type** | **Value**  
unity_LODFade | float4 | Level-of-detail fade when using [LODGroup](class-LODGroup.html). _x_ is fade (0..1), _y_ is fade quantized to 16 levels, _z_ and _w_ unused.  
_TextureSampleAdd | float4 | Set automatically by Unity **for**UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) only** based on whether the texture being
used is in Alpha8 format (the value is set to (1,1,1,0)) or not (the value is
set to (0,0,0,0)).  
  
[](SL-Pragma-require.html)

HLSL pragma require command reference

[](Materials.html)

Materials

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

