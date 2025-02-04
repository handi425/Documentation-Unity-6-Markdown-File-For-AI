[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderTessellation.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderTessellation.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderTessellation.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderTessellation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderTessellation.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderTessellation.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderTessellation.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderTessellation.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Tessellation Surface Shader examples in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-GlobalIllumination.html)

Global illumination Surface Shader example in the Built-In Render Pipeline

[](surface-shaders-language-reference.html)

Surface Shader language reference for the Built-In Render Pipeline

# Tessellation Surface Shader examples in the Built-In Render Pipeline

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), [Surface Shaders](SL-
SurfaceShaders.html)A streamlined way of writing shaders for the Built-in
Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) have some support for DirectX
11 / OpenGL Core GPU Tessellation.

  * Tessellation is indicated by `tessellate:FunctionName` modifier. That function computes triangle edge and inside tessellation factors.
  * When tessellation is used, “vertex modifier” (`vertex:FunctionName`) is invoked _after_ tessellation, for each generated vertex in the domain **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). Here you’d typically to displacement
mapping.

  * Surface shaders can optionally compute [phong tessellation](https://www.google.lt/search?q=phong+tessellation) to smooth model surface even without any displacement mapping.

## Tessellation & geometry shaders

Surface Shaders have support for simple tessellation and displacement. When
you write custom [Shader programs](writing-shader-writing-shader-programs-
hlsl.html), you can use the full set of DX11 shader model 5.0 features,
including geometry, hull, and domain Shaders.

Current limitations of tessellation support:

  * Only triangle domain - no **quads** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](PrimitiveObjects.html)  
See in [Glossary](Glossary.html#Quad), no isoline tessellation.

  * When you use tessellation, the shader is automatically compiled into the Shader Model [4.6 target](SL-ShaderCompileTargets.html), which prevents support for running on older graphics targets.

## Render pipeline compatibility

**Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Surface Shaders** | No  
  
For a streamlined way of creating Shader objects in URP, see [Shader Graph](shader-graph.html). | No  
  
For a streamlined way of creating Shader objects in HDRP, see [Shader Graph](shader-graph.html). | No | Yes  
  
## Fixed amount of tessellation

If your model’s faces are roughly the same size on screen, add a fixed amount
of tesselation to the **Mesh** The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) (the same tessellation level over the
whole Mesh).

The following example script applies a fixed amount of tessellation.

    
    
        Shader "Tessellation Sample" {
            Properties {
                _Tess ("Tessellation", Range(1,32)) = 4
                _MainTex ("Base (RGB)", 2D) = "white" {}
                _DispTex ("Disp Texture", 2D) = "gray" {}
                _NormalMap ("Normalmap", 2D) = "bump" {}
                _Displacement ("Displacement", Range(0, 1.0)) = 0.3
                _Color ("Color", color) = (1,1,1,0)
                _SpecColor ("Spec color", color) = (0.5,0.5,0.5,0.5)
            }
            SubShader {
                Tags { "RenderType"="Opaque" }
                LOD 300
                
                CGPROGRAM
                #pragma surface surf BlinnPhong addshadow fullforwardshadows vertex:disp tessellate:tessFixed nolightmap
                #pragma target 4.6
    
                struct appdata {
                    float4 vertex : POSITION;
                    float4 tangent : TANGENT;
                    float3 normal : NORMAL;
                    float2 texcoord : TEXCOORD0;
                };
    
                float _Tess;
    
                float4 tessFixed()
                {
                    return _Tess;
                }
    
                sampler2D _DispTex;
                float _Displacement;
    
                void disp (inout appdata v)
                {
                    float d = tex2Dlod(_DispTex, float4(v.texcoord.xy,0,0)).r * _Displacement;
                    v.vertex.xyz += v.normal * d;
                }
    
                struct Input {
                    float2 uv_MainTex;
                };
    
                sampler2D _MainTex;
                sampler2D _NormalMap;
                fixed4 _Color;
    
                void surf (Input IN, inout SurfaceOutput o) {
                    half4 c = tex2D (_MainTex, IN.uv_MainTex) * _Color;
                    o.Albedo = c.rgb;
                    o.Specular = 0.2;
                    o.Gloss = 1.0;
                    o.Normal = UnpackNormal(tex2D(_NormalMap, IN.uv_MainTex));
                }
                ENDCG
            }
            FallBack "Diffuse"
        }
    

In the example above, the `tessFixed` tessellation function returns four
tessellation factors as a single float4 value: three factors for each edge of
the triangle, and one factor for the inside of the triangle.

The example returns a constant value that is set in the Material properties.

![](../uploads/Main/SurfaceShaderTess2-fixed.jpg)

* * *

## Distance-based tessellation

You can also change tessellation level based on distance from the **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). For example, you could define two
distance values:

  * The distance when tessellation is at maximum (for example, 10 meters).
  * The distance when the tessellation level gradually decreases (for example, 20 meters).

    
    
        Shader "Tessellation Sample" {
            Properties {
                _Tess ("Tessellation", Range(1,32)) = 4
                _MainTex ("Base (RGB)", 2D) = "white" {}
                _DispTex ("Disp Texture", 2D) = "gray" {}
                _NormalMap ("Normalmap", 2D) = "bump" {}
                _Displacement ("Displacement", Range(0, 1.0)) = 0.3
                _Color ("Color", color) = (1,1,1,0)
                _SpecColor ("Spec color", color) = (0.5,0.5,0.5,0.5)
            }
            SubShader {
                Tags { "RenderType"="Opaque" }
                LOD 300
                
                CGPROGRAM
                #pragma surface surf BlinnPhong addshadow fullforwardshadows vertex:disp tessellate:tessDistance nolightmap
                #pragma target 4.6
                #include "Tessellation.cginc"
    
                struct appdata {
                    float4 vertex : POSITION;
                    float4 tangent : TANGENT;
                    float3 normal : NORMAL;
                    float2 texcoord : TEXCOORD0;
                };
    
                float _Tess;
    
                float4 tessDistance (appdata v0, appdata v1, appdata v2) {
                    float minDist = 10.0;
                    float maxDist = 25.0;
                    return UnityDistanceBasedTess(v0.vertex, v1.vertex, v2.vertex, minDist, maxDist, _Tess);
                }
    
                sampler2D _DispTex;
                float _Displacement;
    
                void disp (inout appdata v)
                {
                    float d = tex2Dlod(_DispTex, float4(v.texcoord.xy,0,0)).r * _Displacement;
                    v.vertex.xyz += v.normal * d;
                }
    
                struct Input {
                    float2 uv_MainTex;
                };
    
                sampler2D _MainTex;
                sampler2D _NormalMap;
                fixed4 _Color;
    
                void surf (Input IN, inout SurfaceOutput o) {
                    half4 c = tex2D (_MainTex, IN.uv_MainTex) * _Color;
                    o.Albedo = c.rgb;
                    o.Specular = 0.2;
                    o.Gloss = 1.0;
                    o.Normal = UnpackNormal(tex2D(_NormalMap, IN.uv_MainTex));
                }
                ENDCG
            }
            FallBack "Diffuse"
        }
    

Here, the tessellation function takes the vertex data of the three triangle
corners before tessellation as its three parameters.

Unity needs this to compute tessellation levels, which depend on vertex
positions.

The example includes a built-in helper file, Tessellation.cginc, and calls the
`UnityDistanceBasedTess` function from the file to do all the work. This
function computes the distance of each vertex to the camera and derives the
final tessellation factors.

![](../uploads/Main/SurfaceShaderTess3-distance.jpg)

* * *

## Edge length based tessellation

Purely distance based tessellation is effective only when triangle sizes are
quite similar. In the image above, the **GameObjects** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that have small triangles are
tessellated too much, while GameObjects that have large triangles aren’t
tessellated enough.

One way to improve this is to compute tessellation levels based on triangle
edge length on the screen. Unity should apply a larger tessellation factor to
longer edges.

    
    
        Shader "Tessellation Sample" {
            Properties {
                _EdgeLength ("Edge length", Range(2,50)) = 15
                _MainTex ("Base (RGB)", 2D) = "white" {}
                _DispTex ("Disp Texture", 2D) = "gray" {}
                _NormalMap ("Normalmap", 2D) = "bump" {}
                _Displacement ("Displacement", Range(0, 1.0)) = 0.3
                _Color ("Color", color) = (1,1,1,0)
                _SpecColor ("Spec color", color) = (0.5,0.5,0.5,0.5)
            }
            SubShader {
                Tags { "RenderType"="Opaque" }
                LOD 300
                
                CGPROGRAM
                #pragma surface surf BlinnPhong addshadow fullforwardshadows vertex:disp tessellate:tessEdge nolightmap
                #pragma target 4.6
                #include "Tessellation.cginc"
    
                struct appdata {
                    float4 vertex : POSITION;
                    float4 tangent : TANGENT;
                    float3 normal : NORMAL;
                    float2 texcoord : TEXCOORD0;
                };
    
                float _EdgeLength;
    
                float4 tessEdge (appdata v0, appdata v1, appdata v2)
                {
                    return UnityEdgeLengthBasedTess (v0.vertex, v1.vertex, v2.vertex, _EdgeLength);
                }
    
                sampler2D _DispTex;
                float _Displacement;
    
                void disp (inout appdata v)
                {
                    float d = tex2Dlod(_DispTex, float4(v.texcoord.xy,0,0)).r * _Displacement;
                    v.vertex.xyz += v.normal * d;
                }
    
                struct Input {
                    float2 uv_MainTex;
                };
    
                sampler2D _MainTex;
                sampler2D _NormalMap;
                fixed4 _Color;
    
                void surf (Input IN, inout SurfaceOutput o) {
                    half4 c = tex2D (_MainTex, IN.uv_MainTex) * _Color;
                    o.Albedo = c.rgb;
                    o.Specular = 0.2;
                    o.Gloss = 1.0;
                    o.Normal = UnpackNormal(tex2D(_NormalMap, IN.uv_MainTex));
                }
                ENDCG
            }
            FallBack "Diffuse"
        }
    

In this example, you call the `UnityEdgeLengthBasedTess` function from
_Tessellation.cginc_ to do all the work.

![](../uploads/Main/SurfaceShaderTess4-edgelength.jpg)

For performance reasons, call the UnityEdgeLengthBasedTessCull function
instead, which performs patch frustum culling. This makes the shader a bit
more expensive, but saves a lot of GPU work for parts of meshes that are
outside of the Camera’s view.

* * *

## Phong Tessellation

[Phong Tessellation](https://www.google.lt/search?q=phong+tessellation)
modifies positions of the subdivided faces so that the resulting surface
follows the mesh normals a bit. It’s quite an effective way of making low-poly
meshes become more smooth.

Unity’s surface shaders can compute Phong tessellation automatically using
`tessphong:VariableName` compilation directive. Here’s an example shader:

    
    
        Shader "Phong Tessellation" {
            Properties {
                _EdgeLength ("Edge length", Range(2,50)) = 5
                _Phong ("Phong Strengh", Range(0,1)) = 0.5
                _MainTex ("Base (RGB)", 2D) = "white" {}
                _Color ("Color", color) = (1,1,1,0)
            }
            SubShader {
                Tags { "RenderType"="Opaque" }
                LOD 300
                
                CGPROGRAM
                #pragma surface surf Lambert vertex:dispNone tessellate:tessEdge tessphong:_Phong nolightmap
                #include "Tessellation.cginc"
    
                struct appdata {
                    float4 vertex : POSITION;
                    float3 normal : NORMAL;
                    float2 texcoord : TEXCOORD0;
                };
    
                void dispNone (inout appdata v) { }
    
                float _Phong;
                float _EdgeLength;
    
                float4 tessEdge (appdata v0, appdata v1, appdata v2)
                {
                    return UnityEdgeLengthBasedTess (v0.vertex, v1.vertex, v2.vertex, _EdgeLength);
                }
    
                struct Input {
                    float2 uv_MainTex;
                };
    
                fixed4 _Color;
                sampler2D _MainTex;
    
                void surf (Input IN, inout SurfaceOutput o) {
                    half4 c = tex2D (_MainTex, IN.uv_MainTex) * _Color;
                    o.Albedo = c.rgb;
                    o.Alpha = c.a;
                }
    
                ENDCG
            }
            FallBack "Diffuse"
        }
    

Here is a comparison between a regular shader (top row) and one that uses
Phong tessellation (bottom row). See that even without any displacement
mapping, the surface becomes more round.

![](../uploads/Main/SurfaceShaderPhongTess.jpg)

* * *

  * 2018–03–20 Page amended 
  * **Tessellation for Metal** added in 2018.1

[](SL-SurfaceShaderExamples-GlobalIllumination.html)

Global illumination Surface Shader example in the Built-In Render Pipeline

[](surface-shaders-language-reference.html)

Surface Shader language reference for the Built-In Render Pipeline

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

