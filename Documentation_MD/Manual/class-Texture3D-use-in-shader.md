[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Texture3D-use-in-shader.html)
  * [中文](/cn/current/Manual/class-Texture3D-use-in-shader.html)
  * [日本語](/ja/current/Manual/class-Texture3D-use-in-shader.html)
  * [한국어](/kr/current/Manual/class-Texture3D-use-in-shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Texture3D-use-in-shader.html)
  * [中文](/cn/current/Manual/class-Texture3D-use-in-shader.html)
  * [日本語](/ja/current/Manual/class-Texture3D-use-in-shader.html)
  * [한국어](/kr/current/Manual/class-Texture3D-use-in-shader.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [3D textures](class-Texture3D.html)
  * Sample a 3D texture in a shader

[](class-Texture3D-preview.html)

Preview a 3D texture

[](class-Texture3D-create.html)

Create a 3D texture via script

# Sample a 3D texture in a shader

To use a 3D texture in a custom **shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), you can use the following:

  * The `3D` material property declaration to add a 3D texture property. For example `_MainTex ("Example 3D texture", 3D) = "white" {};`
  * The `sampler3D` sampler state to use the 3D texture as a shader input. For example `sampler3D _MainTex;`
  * The `tex3D` HLSL method to sample the 3D texture. For example `float4 color = tex3D(_MainTex, float3(0.5f, 0.5f, 0.5f));`

## Example

The following is an example of a shader that uses raymarching to sample a 3D
texture and render it as a semi-transparent volume.

To use the example, follow these steps:

  1. In the **Project** window, use **Add** > **Shader** > **Unlit Shader** to create a new basic shader.
  2. Replace the shader code with the example code.
  3. Right-click the shader in the **Project** window and select **Create** > **Material** to create a new material from the shader.
  4. Import or create a 3D texture. For example, use the example code from the [Create a 3D texture in a script](class-Texture3D-create.html) page.
  5. Drag the 3D texture asset from the **Project** window to the **Texture 3D** property of the material.
  6. Attach the material to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

    
    
    Shader "Unlit/VolumeShader"
    {
        Properties
        {
            _MainTex ("Texture", 3D) = "white" {}
            _Alpha ("Alpha", float) = 0.02
            _StepSize ("Step Size", float) = 0.01
        }
        SubShader
        {
            Tags { "Queue" = "Transparent" "RenderType" = "Transparent" }
            Blend One OneMinusSrcAlpha
            LOD 100
    
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
    
                #include "UnityCG.cginc"
    
                // Maximum number of raymarching samples
                #define MAX_STEP_COUNT 128
    
                // Allowed floating point inaccuracy
                #define EPSILON 0.00001f
    
                struct appdata
                {
                    float4 vertex : POSITION;
                };
    
                struct v2f
                {
                    float4 vertex : SV_POSITION;
                    float3 objectVertex : TEXCOORD0;
                    float3 vectorToSurface : TEXCOORD1;
                };
    
                sampler3D _MainTex;
                float4 _MainTex_ST;
                float _Alpha;
                float _StepSize;
    
                v2f vert (appdata v)
                {
                    v2f o;
    
                    // Vertex in object space. This is the starting point for the raymarching.
                    o.objectVertex = v.vertex;
    
                    // Calculate vector from camera to vertex in world space
                    float3 worldVertex = mul(unity_ObjectToWorld, v.vertex).xyz;
                    o.vectorToSurface = worldVertex - _WorldSpaceCameraPos;
    
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    return o;
                }
    
                float4 BlendUnder(float4 color, float4 newColor)
                {
                    color.rgb += (1.0 - color.a) * newColor.a * newColor.rgb;
                    color.a += (1.0 - color.a) * newColor.a;
                    return color;
                }
    
                fixed4 frag(v2f i) : SV_Target
                {
                    // Start raymarching at the front surface of the object
                    float3 rayOrigin = i.objectVertex;
    
                    // Use vector from camera to object surface to get ray direction
                    float3 rayDirection = mul(unity_WorldToObject, float4(normalize(i.vectorToSurface), 1));
    
                    float4 color = float4(0, 0, 0, 0);
                    float3 samplePosition = rayOrigin;
    
                    // Raymarch through object space
                    for (int i = 0; i < MAX_STEP_COUNT; i++)
                    {
                        // Accumulate color only within unit cube bounds
                        if(max(abs(samplePosition.x), max(abs(samplePosition.y), abs(samplePosition.z))) < 0.5f + EPSILON)
                        {
                            float4 sampledColor = tex3D(_MainTex, samplePosition + float3(0.5f, 0.5f, 0.5f));
                            sampledColor.a *= _Alpha;
                            color = BlendUnder(color, sampledColor);
                            samplePosition += rayDirection * _StepSize;
                        }
                    }
    
                    return color;
                }
                ENDCG
            }
        }
    }
    

![ ](../uploads/Main/3DTexture-shader-example.png)  
The volume Unity renders if you use the example shader with the 3D texture
from the [Create a 3D texture in a script](class-Texture3D-create.html) page.

## Additional resources

  * [Writing shaders](shader-writing.html)
  * [ShaderLab: defining material properties](SL-Properties.html)
  * [Sampler states](SL-SamplerStates.html)

[](class-Texture3D-preview.html)

Preview a 3D texture

[](class-Texture3D-create.html)

Create a 3D texture via script

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

