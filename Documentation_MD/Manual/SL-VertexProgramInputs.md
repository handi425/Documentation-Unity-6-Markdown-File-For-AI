[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-VertexProgramInputs.html)
  * [中文](/cn/current/Manual/SL-VertexProgramInputs.html)
  * [日本語](/ja/current/Manual/SL-VertexProgramInputs.html)
  * [한국어](/kr/current/Manual/SL-VertexProgramInputs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-VertexProgramInputs.html)
  * [中文](/cn/current/Manual/SL-VertexProgramInputs.html)
  * [日本語](/ja/current/Manual/SL-VertexProgramInputs.html)
  * [한국어](/kr/current/Manual/SL-VertexProgramInputs.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * [Shader input](writing-shader-shader-input.html)
  * Input vertex data into a shader

[](SL-Use16BitPrecisionInShaders.html)

Use 16-bit precision in shaders

[](SL-SamplerStates.html)

Texture samplers

# Input vertex data into a shader

For Cg/HLSL [vertex programs](writing-shader-writing-shader-programs-
hlsl.html), the [Mesh](class-Mesh.html)The main graphics primitive of Unity.
Meshes make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) vertex data is passed as inputs to the
vertex shader function. Each input needs to have a [semantic](SL-
VertexProgramInputs.html) specified for it: for example, `POSITION` input is
the vertex position, and `NORMAL` is the vertex normal.

Often, vertex data inputs are declared in a structure, instead of listing them
one by one.

## Input a built-in vertex structure

Several commonly used vertex structures are defined in [UnityCG.cginc include
file](SL-BuiltinIncludes.html), and in most cases it’s enough just to use
those. The structures are:

  * `appdata_base`: position, normal and one texture coordinate.
  * `appdata_tan`: position, tangent, normal and one texture coordinate.
  * `appdata_full`: position, tangent, normal, four texture coordinates and color.
  * `appdata_img`: vertex **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) input with position and one texture
coordinate.

### Example

This shader colors the mesh based on its normals, and uses `appdata_base` as
vertex program input:

    
    
    Shader "VertexInputSimple" {
        SubShader {
            Pass {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #include "UnityCG.cginc"
             
                struct v2f {
                    float4 pos : SV_POSITION;
                    fixed4 color : COLOR;
                };
                
                v2f vert (appdata_base v)
                {
                    v2f o;
                    o.pos = UnityObjectToClipPos(v.vertex);
                    o.color.xyz = v.normal * 0.5 + 0.5;
                    o.color.w = 1.0;
                    return o;
                }
    
                fixed4 frag (v2f i) : SV_Target { return i.color; }
                ENDCG
            }
        } 
    }
    

## Input a custom vertex structure

To access different vertex data, you need to declare the vertex structure
yourself, or add input parameters to the vertex shader. Vertex data is
identified by Cg/HLSL [semantics](SL-VertexProgramInputs.html), and must be
from the following list:

  * `POSITION` is the vertex position, typically a `float3` or `float4`.
  * `NORMAL` is the vertex normal, typically a `float3`.
  * `TEXCOORD0` is the first UV coordinate, typically `float2`, `float3` or `float4`.
  * `TEXCOORD1`, `TEXCOORD2` and `TEXCOORD3` are the 2nd, 3rd and 4th UV coordinates, respectively.
  * `TANGENT` is the tangent vector (used for normal mapping), typically a `float4`.
  * `COLOR` is the per-vertex color, typically a `float4`.

When the mesh data contains fewer components than are needed by the vertex
shader input, the rest are filled with zeroes, except for the `.w` component
which defaults to 1. For example, mesh texture coordinates are often 2D
vectors with just x and y components. If a vertex shader declares a `float4`
input with `TEXCOORD0` semantic, the value received by the **vertex shader** A
program that runs on each vertex of a 3D model when the model is being
rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader) will contain (x,y,0,1).

For best cross platform support, label vertex outputs and fragment inputs as
`TEXCOORDn` semantics.

Unity also supports the following:

  * `VPOS`\- the position of the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) being rendered. The shader must have a
`#pragma target 3.0` compilation directive, and should output the clip space
position as a separate “out” variable. For maximum portability use the
`UNITY_VPOS_TYPE` type for it, which is `float4` on most platforms.

  * `VFACE` \- whether the rendered surface is facing the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), or facing away from the camera. The
shader must have a `#pragma target 3.0` compilation directive.

  * `SV_VertexID` \- the index of the vertex being processed. The shader must have a `#pragma target 3.5` compilation directive.

For examples of using these techniques to visualize vertex data in the Built-
in **Render Pipeline** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), see [Visualizing vertex
data](built-in-shader-examples-vertex-data.html).

### Constant buffer macros

Direct3D 11 groups all Shader variables into “constant buffers”. Most of
Unity’s built-in variables are already grouped, but for variables in your own
Shaders it might be more optimal to put them into separate constant buffers
depending on expected frequency of updates.

Use `CBUFFER_START(name)` and `CBUFFER_END` macros for that:

    
    
    CBUFFER_START(MyRarelyUpdatedVariables)
        float4 _SomeGlobalValue;
    CBUFFER_END
    

If you use a GPU [compute buffer](../ScriptReference/ComputeBuffer.html) or
[graphics buffer](../ScriptReference/GraphicsBuffer.html) to set the value of
the variables, make sure the buffer and the constant buffer have matching data
layouts on all graphics APIs you build for. See [Using constant buffers with
GPU buffers](SL-PlatformDifferences.html#cbuffers) for more information.

**Note:** You can’t add structs to constant buffers.

## Interpolator count limits

There are limits to how many interpolator variables can be used in total to
pass the information from the vertex into the fragment shader. The limit
depends on the platform and GPU, and the general guidelines are:

  * **Up to 8 interpolators** : Direct3D 11 9.x level (Windows Phone) . Since the interpolator count is limited, but each interpolator can be a 4-component vector, some shaders pack things together to stay within limits. For example, you can pass two texture coordinates in one `float4` variable (.xy for one coordinate, .zw for the second coordinate).
  * **Up to 10 interpolators** : Shader model 3.0 (`#pragma target 3.0`).
  * **Up to 16 interpolators** : OpenGL ES 3.0 (Android), Metal (iOS).
  * **Up to 32 interpolators** : Direct3D 10 shader model 4.0 (`#pragma target 4.0`).

Regardless of your particular target hardware, it’s generally a good idea to
use as few interpolators as possible for performance reasons.

## Additional resources

  * [Built-in shader variables reference](SL-UnityShaderVariables.html)
  * [Customize how shaders contribute lightmap data in the Built-In Render Pipeline](MetaPass.html)
  * [HLSL shader examples in the Built-In Render Pipeline](built-in-shader-examples.html)
  * [Semantics](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-semantics) in the Microsoft HLSL documentation

[](SL-Use16BitPrecisionInShaders.html)

Use 16-bit precision in shaders

[](SL-SamplerStates.html)

Texture samplers

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

