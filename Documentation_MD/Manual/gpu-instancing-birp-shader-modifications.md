[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gpu-instancing-birp-shader-modifications.html)
  * [中文](/cn/current/Manual/gpu-instancing-birp-shader-modifications.html)
  * [日本語](/ja/current/Manual/gpu-instancing-birp-shader-modifications.html)
  * [한국어](/kr/current/Manual/gpu-instancing-birp-shader-modifications.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gpu-instancing-birp-shader-modifications.html)
  * [中文](/cn/current/Manual/gpu-instancing-birp-shader-modifications.html)
  * [日本語](/ja/current/Manual/gpu-instancing-birp-shader-modifications.html)
  * [한국어](/kr/current/Manual/gpu-instancing-birp-shader-modifications.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in the Built-In Render Pipeline](graphics-performance-birp.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
  * GPU instancing shader reference for the Built-In Render Pipeline

[](gpu-instancing-strip-variants.html)

Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline

[](profiling-landing.html)

Graphics performance and profiling reference

# GPU instancing shader reference for the Built-In Render Pipeline

This section contains information about **shader** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) additions that relate to GPU
instancing.

Addition | Description  
---|---  
`#pragma multi_compile_instancing` | Generates instancing variants. This is required for fragment and **vertex shaders** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader). It is optional for **Surface
Shaders** A streamlined way of writing shaders for the Built-in Render
Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader).  
`#pragma instancing_options` | Specifies options that Unity uses for instances. For information on the option switches available, see `#pragma instancing_options`.  
`UNITY_VERTEX_INPUT_INSTANCE_ID` | Defines an instance ID in the vertex shader input/output structure. To use this macro, enable the INSTANCING_ON shader keyword. Otherwise, Unity doesn’t set up the instance ID.  
To access the instance ID, use `vertexInput.instanceID` inside an #ifdef
INSTANCING_ON block. If you don’t use this block, variants fail to compile.  
`UNITY_INSTANCING_BUFFER_START(bufferName)` | Declares the start of a per-instance constant buffer named `bufferName`. Use this macro with `UNITY_INSTANCING_BUFFER_END` to wrap declarations of the properties that you want to be unique to each instance. Declare properties inside the buffer using`UNITY_DEFINE_INSTANCED_PROP`.  
`UNITY_INSTANCING_BUFFER_END(bufferName)` | Declares the end of a per-instance constant buffer named `bufferName`. Use this macro with `UNITY_INSTANCING_BUFFER_START` to wrap declarations of the properties that you want to be unique to each instance. Declare properties inside the buffer using`UNITY_DEFINE_INSTANCED_PROP`.  
`UNITY_DEFINE_INSTANCED_PROP(type, propertyName)` | Defines a per-instance shader property with the specified type and name. In the examples below, the `_Color` property is unique.  
`UNITY_SETUP_INSTANCE_ID(v);` | Allows shader functions to access the instance ID. For vertex shaders, this macro is required at the beginning. For fragment shaders, this addition is optional. For an example, see [Vertex and fragment shader](gpu-instancing-vertex-fragment-shader-example.html).  
`UNITY_TRANSFER_INSTANCE_ID(v, o);` | Copies the instance ID from the input structure to the output structure in the vertex shader. Use this macro if you need to access per-instance data in the fragment shader.  
`UNITY_ACCESS_INSTANCED_PROP(bufferName, propertyName)` | Accesses a per-instance shader property in an instancing constant buffer. Unity uses the instance ID to index into the instance data array.`bufferName` must match the name of the constant buffer that contains the specified property.This macro compiles differently for INSTANCING_ON and non-instancing variants.  
  
## Instancing_options switches

The [#pragma instancing_options](#pragma-instancing_options) directive can use
the following switches:

**Switch** | **Description**  
---|---  
`forcemaxcount:batchSize` and `maxcount:batchSize` | On most platforms, Unity automatically calculates the instancing data array size. It divides the maximum constant buffer size on the target device with the size of the structure that contains all per-instance properties. Generally, you don’t need to worry about the batch size. However, some platforms require a fixed array size. To specify the batch size for those platforms, use the `maxcount` option. Other platforms ignore this option. If you want to force a batch size for all platforms, use `forcemaxcount`. This is useful when, for example, your project uses RenderMeshInstanced to issue draw calls with 256 instanced **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite). The default value for the two options
is 500.  
`assumeuniformscaling` | Instructs Unity to assume that all the instances have uniform scalings (the same scale for all X, Y, and Z axes).  
`nolodfade` | Makes Unity not apply GPU instancing to [LOD](LevelOfDetail.html)The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) fade values.  
`nolightprobe` | Prevents Unity from applying GPU instancing to [Light Probe](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) values and their occlusion data.
Setting this option to `ON` can improve performance if your project doesn’t
contain **GameObjects** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that use both GPU instancing and
Light Probes.  
`nolightmap` | Prevents Unity from applying GPU instancing to **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) atlas information values. Setting
this option to `ON` can improve performance if your project doesn’t contain
GameObjects that use both GPU instancing and lightmaps.  
`procedural:FunctionName` | Generates an additional variant for use with [Graphics.RenderMeshIndirect](../ScriptReference/Graphics.RenderMeshIndirect.html). At the beginning of the vertex shader stage, Unity calls the function specified after the colon. To set up the instance data manually, add per-instance data to this function in the same way you would normally add per-instance data to a shader. Unity also calls this function at the beginning of a fragment shader if any of the fetched instance properties are included in the fragment shader.  
  
[](gpu-instancing-strip-variants.html)

Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline

[](profiling-landing.html)

Graphics performance and profiling reference

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

