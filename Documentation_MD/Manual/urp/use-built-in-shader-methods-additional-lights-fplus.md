[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Custom lighting in URP](../urp/lighting/custom-lighting-landing.html)
  * Render additional lights in a shader in URP

[](../urp/lighting/custom-lighting-introduction.html)

Introduction to custom lighting in URP

[](../urp/lighting/custom-lighting-change-light-falloff.html)

Change how lights fade using light falloff in URP

# Render additional lights in a shader in URP

Write a rendering loop that iterates over additional lights in the Forward+
and Forward **rendering paths** The technique that a render pipeline uses to
render graphics. Choosing a different rendering path affects how lighting and
shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath) in a URP **shader** A
program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader).

The shader example on this page is compatible with both the Forward+ and
**Forward rendering** A rendering path that renders each object in one or more
passes, depending on lights that affect the object. Lights themselves are also
treated differently by Forward Rendering, depending on their settings and
intensity. [More info](../RenderTech-ForwardRendering.html)  
See in [Glossary](../Glossary.html#ForwardRendering) paths. Unity handles
additional lights and non-main directional lights differently in the Forward+
and Forward rendering paths. The Forward+ rendering path does not have a limit
of the real-time lights per object, and the `GetAdditionalLightsCount` shader
method always returns 0 in Forward+. For a comparison of rendering paths,
refer to [Choose a rendering path in URP](rendering-paths-comparison.html).

## Add include directives to the shader file

Add the following include directives in the `HLSLPROGRAM` block in the shader
file:

    
    
    #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
    #include "Packages/com.unity.render-pipelines.core/ShaderLibrary/CommonMaterial.hlsl"
    #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/RealtimeLights.hlsl"
    

## Implement the light loop

  1. In a shader pass, add the following `multi_compile` directive to make the shader compatible with the Forward+ rendering path:
    
        #pragma multi_compile _ _FORWARD_PLUS
    

  2. In the Forward+ rendering path, the `LIGHT_LOOP_BEGIN` macro requires the `InputData` struct. Declare the struct in the fragment shader.
    
        InputData inputData = (InputData)0;
    inputData.positionWS = input.positionWS;
    inputData.normalWS = input.normalWS;
    inputData.viewDirectionWS = GetWorldSpaceNormalizeViewDir(input.positionWS);
    inputData.normalizedScreenSpaceUV = GetNormalizedScreenSpaceUV(input.positionCS);
    

  3. Use the `UNITY_LOOP` macro to implement the additional light loop including directional lights in the Forward+ rendering path:
    
        #if USE_FORWARD_PLUS
    UNITY_LOOP for (uint lightIndex = 0; lightIndex < min(URP_FP_DIRECTIONAL_LIGHTS_COUNT, MAX_VISIBLE_LIGHTS); lightIndex++)
    {
        Light additionalLight = GetAdditionalLight(lightIndex, inputData.positionWS, half4(1,1,1,1));
        lighting += MyLightingFunction(inputData.normalWS, additionalLight);
    }
    #endif
    

  4. Use the `LIGHT_LOOP_BEGIN` macro to iterate over lights:
    
        // Additional light loop. The GetAdditionalLightsCount method always returns 0 in Forward+.
    uint pixelLightCount = GetAdditionalLightsCount();
    LIGHT_LOOP_BEGIN(pixelLightCount)
        Light additionalLight = GetAdditionalLight(lightIndex, inputData.positionWS, half4(1,1,1,1));
        lighting += MyLightingFunction(inputData.normalWS, additionalLight);
    LIGHT_LOOP_END
    

## Example

The following URP shader iterates over the additional lights, including non-
main directional lights, and uses them in a custom lighting function.

The shader is compatible with both the Forward+ and Forward rendering paths.

    
    
    Shader "Custom/AdditionalLights"
    {
        Properties
        { 
        }
        
        SubShader
        {
            Tags 
            { 
                "RenderType" = "Opaque"
                "RenderPipeline" = "UniversalPipeline"
            }
            
            Cull Off
            ZWrite On
            Pass
            {
                // The LightMode tag matches the ShaderPassName set in UniversalRenderPipeline.cs.
                // The SRPDefaultUnlit pass and passes without the LightMode tag are also rendered by URP
                Name "ForwardLit"
                Tags
                {
                    "LightMode" = "UniversalForward"
                }
                
                HLSLPROGRAM
                            
                #pragma vertex vert
                #pragma fragment frag
    
                // This multi_compile declaration is required for the Forward rendering path
                #pragma multi_compile _ _ADDITIONAL_LIGHTS
                
                // This multi_compile declaration is required for the Forward+ rendering path
                #pragma multi_compile _ _FORWARD_PLUS
                
                #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
                #include "Packages/com.unity.render-pipelines.core/ShaderLibrary/CommonMaterial.hlsl"
                #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/RealtimeLights.hlsl"
                
                struct Attributes
                {
                    float4 positionOS   : POSITION;
                    float3 normalOS     : NORMAL;
                };
                
                struct Varyings
                {
                    float4 positionCS  : SV_POSITION;
                    float3 positionWS  : TEXCOORD1;
                    float3 normalWS    : TEXCOORD2;
                };
                
                Varyings vert(Attributes IN)
                {
                    Varyings OUT;
                    OUT.positionWS = TransformObjectToWorld(IN.positionOS.xyz);
                    OUT.positionCS = TransformWorldToHClip(OUT.positionWS);
                    OUT.normalWS = TransformObjectToWorldNormal(IN.normalOS);
                    
                    return OUT;
                }
                
                float3 MyLightingFunction(float3 normalWS, Light light)
                {
                    float NdotL = dot(normalWS, normalize(light.direction));
                    NdotL = (NdotL + 1) * 0.5;
                    return saturate(NdotL) * light.color * light.distanceAttenuation * light.shadowAttenuation;
                }
                
                // This function loops through the lights in the scene
                float3 MyLightLoop(float3 color, InputData inputData)
                {
                    float3 lighting = 0;
                    
                    // Get the main light
                    Light mainLight = GetMainLight();
                    lighting += MyLightingFunction(inputData.normalWS, mainLight);
                    
                    // Get additional lights
                    #if defined(_ADDITIONAL_LIGHTS)
    
                    // Additional light loop including directional lights. This block is specific to Forward+.
                    #if USE_FORWARD_PLUS
                    UNITY_LOOP for (uint lightIndex = 0; lightIndex < min(URP_FP_DIRECTIONAL_LIGHTS_COUNT, MAX_VISIBLE_LIGHTS); lightIndex++)
                    {
                        Light additionalLight = GetAdditionalLight(lightIndex, inputData.positionWS, half4(1,1,1,1));
                        lighting += MyLightingFunction(inputData.normalWS, additionalLight);
                    }
                    #endif
                    
                    // Additional light loop. The GetAdditionalLightsCount method always returns 0 in Forward+.
                    uint pixelLightCount = GetAdditionalLightsCount();
                    LIGHT_LOOP_BEGIN(pixelLightCount)
                        Light additionalLight = GetAdditionalLight(lightIndex, inputData.positionWS, half4(1,1,1,1));
                        lighting += MyLightingFunction(inputData.normalWS, additionalLight);
                    LIGHT_LOOP_END
                    
                    #endif
                    
                    return color * lighting;
                }
                
                half4 frag(Varyings input) : SV_Target0
                {
                    // The Forward+ light loop (LIGHT_LOOP_BEGIN) requires the InputData struct to be in its scope.
                    InputData inputData = (InputData)0;
                    inputData.positionWS = input.positionWS;
                    inputData.normalWS = input.normalWS;
                    inputData.viewDirectionWS = GetWorldSpaceNormalizeViewDir(input.positionWS);
                    inputData.normalizedScreenSpaceUV = GetNormalizedScreenSpaceUV(input.positionCS);
                    
                    float3 surfaceColor = float3(1, 1, 1);
                    float3 lighting = MyLightLoop(surfaceColor, inputData);
                    
                    half4 finalColor = half4(lighting, 1);
                    
                    return finalColor;
                }
                
                ENDHLSL
            }
        }
    }
    

## Additional resources

  * [Writing custom shaders](writing-custom-shaders-urp.html)
  * [Use lighting in a custom URP shader](use-built-in-shader-methods-lighting.html)
  * [Upgrade custom shaders for URP compatibility](urp-shaders/birp-urp-custom-shader-upgrade-guide.html)
  * [HLSL in Unity](../writing-shader-writing-shader-programs-hlsl.html)
  * [Rendering paths in Unity](../rendering-paths-introduction.html)

[](../urp/lighting/custom-lighting-introduction.html)

Introduction to custom lighting in URP

[](../urp/lighting/custom-lighting-change-light-falloff.html)

Change how lights fade using light falloff in URP

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

