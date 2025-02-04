[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-transformations.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-transformations.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-transformations.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-transformations.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-transformations.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-transformations.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-transformations.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-transformations.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](../urp/writing-custom-shaders-urp.html)
  * [Shader methods in URP](../urp/use-built-in-shader-methods.html)
  * Transform positions in a custom URP shader

[](../urp/use-built-in-shader-methods-import.html)

Import a file from the URP shader library

[](../urp/use-built-in-shader-methods-camera.html)

Use the camera in a custom URP shader

# Transform positions in a custom URP shader

To transform positions in a custom Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) **shader** A program
that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), follow these steps:

  1. Add `#include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"` inside the `HLSLPROGRAM` in your shader file. The `Core.hlsl` file imports the `ShaderVariablesFunction.hlsl` file.
  2. Use one of the following methods from the `ShaderVariablesFunction.hlsl` file.

**Method** | **Syntax** | **Description**  
---|---|---  
`GetNormalizedScreenSpaceUV` | `float2 GetNormalizedScreenSpaceUV(float2 positionInClipSpace)` | Converts a position in clip space to screen space.  
`GetObjectSpaceNormalizeViewDir` | `half3 GetObjectSpaceNormalizeViewDir(float3 positionInObjectSpace)` | Converts a position in object space to the normalized direction towards the viewer.  
`GetVertexNormalInputs` | `VertexNormalInputs GetVertexNormalInputs(float3 normalInObjectSpace)` | Converts the normal of a vertex in object space to a tangent, bitangent, and normal in world space. You can also input both the normal and a `float4` tangent in object space.  
`GetVertexPositionInputs` | `VertexPositionInputs GetVertexPositionInputs(float3 positionInObjectSpace)` | Converts the position of a vertex in object space to positions in world space, view space, clip space, and normalized device coordinates.  
`GetWorldSpaceNormalizeViewDir` | `half3 GetWorldSpaceNormalizeViewDir(float3 positionInWorldSpace)` | Returns the direction from a position in world space to the viewer, and normalizes the direction.  
`GetWorldSpaceViewDir` | `float3 GetWorldSpaceViewDir(float3 positionInWorldSpace)` | Returns the direction from a position in world space to the viewer.  
  
## Structs

### VertexPositionInputs

Use the `GetVertexNormalInputs` method to get this struct.

**Field** | **Description**  
---|---  
`float3 positionWS` | The position in world space.  
`float3 positionVS` | The position in view space.  
`float4 positionCS` | The position in clip space.  
`float4 positionNDC` | The position as normalized device coordinates (NDC).  
  
### VertexNormalInputs

Use the `GetVertexNormalInputs` method to get this struct.

**Field** | **Description**  
---|---  
`real3 tangentWS` | The tangent in world space.  
`real3 bitangentWS` | The bitangent in world space.  
`float3 normalWS` | The normal in world space.  
  
## Example

The following URP shader draws object surfaces with colors that represent
their position in screen space.

    
    
    Shader "Custom/ScreenSpacePosition"
    {
        SubShader
        {
            Tags { "RenderType" = "Opaque" "RenderPipeline" = "UniversalPipeline" }
    
            Pass
            {
                HLSLPROGRAM
    
                #pragma vertex vert
                #pragma fragment frag
    
                #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
    
                struct Attributes
                {
                    float4 positionOS : POSITION;
                    float2 uv: TEXCOORD0;
                };
    
                struct Varyings
                {
                    float4 positionCS  : SV_POSITION;
                    float2 uv: TEXCOORD0;
                    float3 positionWS : TEXCOORD2;
                };
    
                Varyings vert(Attributes IN)
                {
                    Varyings OUT;
                    OUT.positionCS = TransformObjectToHClip(IN.positionOS.xyz);
    
                    // Get the position of the vertex in different spaces
                    VertexPositionInputs positions = GetVertexPositionInputs(IN.positionOS);
    
                    // Set positionWS to the screen space position of the vertex
                    OUT.positionWS = positions.positionWS.xyz;
    
                    return OUT;
                }
    
                half4 frag(Varyings IN) : SV_Target
                {
                    // Set the fragment color to the screen space position vector
                    return float4(IN.positionWS.xy, 0, 1);
                }
                ENDHLSL
            }
        }
    }
    

## Additional resources

  * [Writing custom shaders](writing-custom-shaders-urp.html)
  * [Upgrade custom shaders for URP compatibility](urp-shaders/birp-urp-custom-shader-upgrade-guide.html)
  * [HLSL in Unity](https://docs.unity3d.com/Manual/SL-ShaderPrograms.html)
  * [Shader semantics](https://docs.unity3d.com/Manual/SL-VertexProgramInputs.html)

[](../urp/use-built-in-shader-methods-import.html)

Import a file from the URP shader library

[](../urp/use-built-in-shader-methods-camera.html)

Use the camera in a custom URP shader

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

