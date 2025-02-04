[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/upgrade-guide-10-0-x.html)
  * [中文](/cn/current/Manual/urp/upgrade-guide-10-0-x.html)
  * [日本語](/ja/current/Manual/urp/upgrade-guide-10-0-x.html)
  * [한국어](/kr/current/Manual/urp/upgrade-guide-10-0-x.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/upgrade-guide-10-0-x.html)
  * [中文](/cn/current/Manual/urp/upgrade-guide-10-0-x.html)
  * [日本語](/ja/current/Manual/urp/upgrade-guide-10-0-x.html)
  * [한국어](/kr/current/Manual/urp/upgrade-guide-10-0-x.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Get started with URP](../urp/introduction-landing.html)
  * [Installing and upgrading URP](../urp/InstallingAndConfiguringURP.html)
  * [Upgrade URP](../urp/upgrade-guides.html)
  * Upgrade to version 10.0.x of the Universal Render Pipeline

[](../urp/upgrade-guide-10-1-x.html)

Upgrade to version 10.1.x of the Universal Render Pipeline

[](../urp/upgrade-guide-9-0-x.html)

Upgrade to version 9.0.x of the Universal Render Pipeline

# Upgrade to version 10.0.x of the Universal Render Pipeline

This page describes how to upgrade from an older version of the Universal
**Render Pipeline** A series of operations that take the contents of a Scene,
and displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) to version 10.0.x.

## Upgrading from URP 7.2.x and later releases

  1. URP 10.x.x does not support the package **Post-Processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](../Glossary.html#post-processing) Stack v2. If your Project
uses the package Post-Processing Stack v2, migrate the effects that use that
package first.

### DepthNormals Pass

Starting from version 10.0.x, URP can generate a normal texture called
`_CameraNormalsTexture`. To render to this texture in your custom **shader** A
program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), add a Pass with the name
`DepthNormals`. For an example, check the implementation in `Lit.shader`.

### Screen Space Ambient Occlusion (SSAO)

URP 10.0.x implements the Screen Space **Ambient Occlusion** A method to
approximate how much ambient light (light not coming from a specific
direction) can hit a point on a surface.  
See in [Glossary](../Glossary.html#Ambientocclusion) (SSAO) effect.

If you intend to use the SSAO effect with your custom shaders, consider the
following entities related to SSAO:

  * The `_SCREEN_SPACE_OCCLUSION` keyword.

  * `Input.hlsl` contains the new declaration `float2 normalizedScreenSpaceUV` in the `InputData` struct.

  * `Lighting.hlsl` contains the `AmbientOcclusionFactor` struct with the variables for calculating indirect and direct occlusion:
    
        struct AmbientOcclusionFactor
    {
        half indirectAmbientOcclusion;
        half directAmbientOcclusion;
    };
    

  * `Lighting.hlsl` contains the following function for sampling the SSAO texture:
    
        half SampleAmbientOcclusion(float2 normalizedScreenSpaceUV)
    

  * `Lighting.hlsl` contains the following function:
    
        AmbientOcclusionFactor GetScreenSpaceAmbientOcclusion(float2
    normalizedScreenSpaceUV)
    

To support SSAO in custom shader, add the `DepthNormals` Pass and the
`_SCREEN_SPACE_OCCLUSION` keyword the the shader. For an example, check
`Lit.shader`.

If your custom shader implements custom lighting functions, use the function
`GetScreenSpaceAmbientOcclusion(float2 normalizedScreenSpaceUV)` to get the
`AmbientOcclusionFactor` value for your lighting calculations.

## Upgrading from URP 7.0.x–7.1.x

  1. Upgrade to URP 7.2.0 first. Refer to [Upgrading to version 7.2.0 of the Universal Render Pipeline](upgrade-guide-7-2-0.html).

  2. URP 8.x.x does not support the package Post-Processing Stack v2. If your Project uses the package Post-Processing Stack v2, migrate the effects that use that package first.

[](../urp/upgrade-guide-10-1-x.html)

Upgrade to version 10.1.x of the Universal Render Pipeline

[](../urp/upgrade-guide-9-0-x.html)

Upgrade to version 9.0.x of the Universal Render Pipeline

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

