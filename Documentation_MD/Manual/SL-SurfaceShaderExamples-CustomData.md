[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-CustomData.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-CustomData.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-CustomData.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-CustomData.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-CustomData.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-CustomData.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-CustomData.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-CustomData.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Custom data Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-VertexModifier.html)

Vertex modifier Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-FinalColor.html)

Final color modifier Surface Shader example in the Built-In Render Pipeline

# Custom data Surface Shader example in the Built-In Render Pipeline

Using a vertex modifier function, it is also possible to compute custom data
in a vertex **Shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), which then will be passed to the
**Surface Shader** A streamlined way of writing shaders for the Built-in
Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) function per-pixel. The same
compilation directive `vertex:functionName` is used, but the function should
take two parameters: `inout appdata_full` and `out Input`. You can fill in any
Input member that is not a built-in value there.

**Note:** Custom Input members used in this way must not have names beginning
with ‘uv’ or they won’t work properly.

The example below defines a custom `float3 customColor` member, which is
computed in a vertex function:

    
    
      Shader "Example/Custom Vertex Data" {
        Properties {
          _MainTex ("Texture", 2D) = "white" {}
        }
        SubShader {
          Tags { "RenderType" = "Opaque" }
          CGPROGRAM
          #pragma surface surf Lambert vertex:vert
          struct Input {
              float2 uv_MainTex;
              float3 customColor;
          };
          void vert (inout appdata_full v, out Input o) {
              UNITY_INITIALIZE_OUTPUT(Input,o);
              o.customColor = abs(v.normal);
          }
          sampler2D _MainTex;
          void surf (Input IN, inout SurfaceOutput o) {
              o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
              o.Albedo *= IN.customColor;
          }
          ENDCG
        } 
        Fallback "Diffuse"
      }
    

In this example `customColor` is set to the absolute value of the normal:

![](../uploads/Main/SurfaceShaderCustomVertexData.jpg)

More practical uses could be computing any per-vertex data that is not
provided by built-in Input variables; or optimizing Shader computations. For
example, it’s possible to compute Rim lighting at the **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)’s vertices, instead of doing that
in the Surface Shader per-pixel.

[](SL-SurfaceShaderExamples-VertexModifier.html)

Vertex modifier Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-FinalColor.html)

Final color modifier Surface Shader example in the Built-In Render Pipeline

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

