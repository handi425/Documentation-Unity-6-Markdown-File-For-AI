[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-indirect-lighting.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](../urp/writing-custom-shaders-urp.html)
  * [Shader methods in URP](../urp/use-built-in-shader-methods.html)
  * Use indirect lighting in a custom URP shader

[](../urp/use-built-in-shader-methods-lighting.html)

Use lighting in a custom URP shader

[](../urp/use-built-in-shader-methods-shadows.html)

Use shadows in a custom URP shader

# Use indirect lighting in a custom URP shader

To use indirect lighting in a custom Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) **shader** A program
that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), follow these steps:

  1. Add an `#include` line inside the `HLSLPROGRAM` block in your shader file. Refer to the sections on this page for specific include file paths.
  2. Use any of the methods from the following sections.

## Use reflection probes in a custom URP shader

To use **reflection probes** A rendering component that captures a spherical
view of its surroundings in all directions, rather like a camera. The captured
image is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](../class-ReflectionProbe.html)  
See in [Glossary](../Glossary.html#ReflectionProbe) or the **skybox** A
special type of Material used to represent skies. Usually six-sided. [More
info](../sky-landing.html)  
See in [Glossary](../Glossary.html#Skybox), use the following `#include` line:

    
    
    #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/GlobalIllumination.hlsl"
    

**Method** | **Syntax** | **Description**  
---|---|---  
`GlossyEnvironmentReflection` | `half3 GlossyEnvironmentReflection(half3 reflectVector, float3 positionWS, half perceptualRoughness, half occlusion, float2 normalizedScreenSpaceUV)` | Samples reflection probes if the object is within a reflection probe volume. Samples the skybox otherwise. The function supports [reflection probe blending](lighting/reflection-probes-introduction.html).  
The `perceptualRoughness` argument selects the mip level of the sampled
texture. The higher the value, the more blurred the reflections look.  
The `occlusion` argument is the reflection probe attenuation factor.  
The `normalizedScreenSpaceUV` argument is the normalized screen space position
of the fragment.  
  
The `GlossyEnvironmentReflection` function has the following simpler overload,
which does not support blending:

    
    
    half3 GlossyEnvironmentReflection(half3 reflectVector, half perceptualRoughness, half occlusion)
    

## Sample Adaptive Probe Volumes

To sample Adaptive Probe Volumes (APV), use the following `#include` line:

    
    
    #include "Packages/com.unity.render-pipelines.core/Runtime/Lighting/ProbeVolume/ProbeVolume.hlsl"
    

**Method** | **Syntax** | **Description**  
---|---|---  
`EvaluateAdaptiveProbeVolume` | `void EvaluateAdaptiveProbeVolume(in float3 posWS, in float3 normalWS, in float3 viewDir, in float2 positionSS, in uint renderingLayer, out float3 bakeDiffuseLighting)` | Samples lighting from [Adaptive Probe Volumes]().  
The `positionSS` argument is the screen space position of a fragment that is
being rendered.  
The `renderingLayer` argument is the [rendering layer mask](probevolumes-
troubleshoot-light-leaks.html#layers).  
  
## Sample light probes

To sample light probes, use the following `#include` line:

    
    
    #include "Packages/com.unity.render-pipelines.core/ShaderLibrary/AmbientProbe.hlsl"
    

**Method** | **Syntax** | **Description**  
---|---|---  
`SampleSH` | `real3 SampleSH(real3 normalWS)` | Sample [light probes](../LightProbes-landing.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe).  
  
## Example

The following URP shader code computes diffuse and specular **ambient light**
Light that doesn’t come from any specific direction, and contributes equal
light in all directions to the Scene. [More info](../lighting-window.html)  
See in [Glossary](../Glossary.html#Ambientlight) using the
`GlossyEnvironmentReflection` function.

    
    
    float3 CustomLightingAmbient(float3 BaseColor, 
                                float3 NormalWS, 
                                float Metallic, 
                                float Smoothness, 
                                float Reflectance, 
                                float AmbientOcclusion, 
                                float PositionWS, 
                                float2 screenspaceUV, 
                                float3 ViewDirWS)
    {
        // Diffuse ambient lighting.
        // Sample the sky probe with high roughness and use a normal vector instead of
        // a reflection vector to approximate ambient light
        float3 DiffuseAmbient = GlossyEnvironmentReflection(NormalWS, PositionWS, 1, 1, screenspaceUV);
        // If the surface is metallic, set ambient to zero, otherwise multiply by BaseColor
        DiffuseAmbient *= lerp(BaseColor, float3(0,0,0), Metallic);
    
        // Specular ambient lighting - reflections
        // Surfaces are more reflective at glancing angles. Compute the fresnel value for reflectance.
        float Fresnel = pow((1 - dot(NormalWS, ViewDirWS)), 5);
        // Reflectance is 100% at the glancing angle
        Reflectance = lerp(Reflectance, 1, Fresnel);
        // If the object is metal, use the base color for reflectance instead.
        float3 ReflectionColor = lerp(float3(Reflectance, Reflectance, Reflectance), BaseColor, Metallic);
        // Compute the reflection vector and use it to sample the sky probe for reflections.
        float3 ReflectionVector = reflect(-ViewDirWS, NormalWS);
        float3 SpecularAmbient = GlossyEnvironmentReflection(ReflectionVector, PositionWS, 1 - Smoothness, 1, screenspaceUV);
        
        return (DiffuseAmbient + SpecularAmbient) * AmbientOcclusion;
    }
    

## Shader graph custom function node example

[Shader Graph Feature
Examples](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Shader-
Graph-Sample-Feature-Examples.html) contain examples of custom lighting
models.

To learn how to use the `GlossyEnvironmentReflection` function in a custom
function node:

  1. In the example **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene), open the **CustomLightingSimple**
shader graph.

  2. Navigate to the **SampleReflectionProbes** sub-graph.

  3. Inspect the **URPReflectionProbe** node. The node contains the HLSL code that uses the `GlossyEnvironmentReflection` function:
    
        #ifdef SHADERGRAPH_PREVIEW
        reflection = float3(0,0,0);
    #else
        reflection = GlossyEnvironmentReflection(reflectVector, positionWS, roughness, 1.0h, screenspaceUV);
    #endif
    

## Additional resources

  * [Writing custom shaders](writing-custom-shaders-urp.html)
  * [Upgrade custom shaders for URP compatibility](urp-shaders/birp-urp-custom-shader-upgrade-guide.html)
  * [Reflection probes in URP](lighting/reflection-probes-introduction.html)
  * [HLSL in Unity](../writing-shader-writing-shader-programs-hlsl.html)
  * [Adaptive Probe Volumes (APV) in URP](probevolumes.html)
  * [Light probes](../LightProbes-landing.html)
  * [Shader Graph Feature Examples](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Shader-Graph-Sample-Feature-Examples.html)

[](../urp/use-built-in-shader-methods-lighting.html)

Use lighting in a custom URP shader

[](../urp/use-built-in-shader-methods-shadows.html)

Use shadows in a custom URP shader

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

