[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/upgrade-guide-7-2-0.html)
  * [中文](/cn/current/Manual/urp/upgrade-guide-7-2-0.html)
  * [日本語](/ja/current/Manual/urp/upgrade-guide-7-2-0.html)
  * [한국어](/kr/current/Manual/urp/upgrade-guide-7-2-0.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/upgrade-guide-7-2-0.html)
  * [中文](/cn/current/Manual/urp/upgrade-guide-7-2-0.html)
  * [日本語](/ja/current/Manual/urp/upgrade-guide-7-2-0.html)
  * [한국어](/kr/current/Manual/urp/upgrade-guide-7-2-0.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Get started with URP](../urp/introduction-landing.html)
  * [Installing and upgrading URP](../urp/InstallingAndConfiguringURP.html)
  * [Upgrade URP](../urp/upgrade-guides.html)
  * Upgrade to version 7.2.0 of the Universal Render Pipeline

[](../urp/upgrade-guide-7-3-0.html)

Upgrade to version 7.3.0 of the Universal Render Pipeline

[](../urp/upgrade-lwrp-to-urp.html)

Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline

# Upgrade to version 7.2.0 of the Universal Render Pipeline

On this page, you will find information about upgrading from an older version
of the Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) to the current
version.

## Building your Project for consoles

To build a Project for a console, you need to install an additional package
for each platform you want to support.

## Require Depth Texture

In previous versions of URP, if **post-processing** A process that improves
product visuals by applying filters and effects before the image appears on
screen. You can use post-processing effects to simulate physical camera and
film properties, for example Bloom and Depth of Field. [More
info](../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../Glossary.html#post-processing) was enabled it would cause
the pipeline to always require depth. We have improved the post-processing
integration to only require depth from the pipeline when **Depth of Field** A
post-processing effect that simulates the focus properties of a camera lens.
[More info](../PostProcessingOverview.html)  
See in [Glossary](../Glossary.html#DepthofField), Motion Blur or SMAA effects
are enabled. This improves performance in many cases.

Because **Cameras** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) that use post-processing no longer
require depth by default, you must now manually indicate that Cameras require
depth if you are using it for other effects, such as **soft particles**
Particles that create semi-transparent effects like smoke, fog or fire. Soft
particles fade out as they approach an opaque object, to prevent intersections
with the geometry. [More info](../shader-StandardParticleShaders.html)  
See in [Glossary](../Glossary.html#SoftParticles).

To make all Cameras require depth, enable the the `Depth Texture` option in
the [Pipeline Asset](universalrp-asset.html). To make an individual Camera
require depth, set `Depth Texture` option to `On` in the [Camera
Inspector](camera-component-reference.html).

## Sampling shadows from the Main Light

In previous versions of URP, if shadow cascades were enabled for the main
Light, shadows would be resolved in a screen space pass. The pipeline now
always resolves shadows while rendering opaque or transparent objects. This
allows for consistency and solved many issues regarding shadows.

If have custom HLSL **shaders** A program that runs on the GPU. [More
info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) and sample
`_ScreenSpaceShadowmapTexture` texture, you must upgrade them to sample
shadows by using the `GetMainLight` function instead.

For example:

    
    
    float4 shadowCoord = TransformWorldToShadowCoord(positionWorldSpace);
    Light mainLight = GetMainLight(inputData.shadowCoord);
    
    // now you can use shadow to apply realtime occlusion
    half shadow = mainLight.shadowAttenuation;
    

You must also define the following in your .shader file to make sure your
custom shader can receive shadows correctly:

    
    
    #pragma multi_compile _ _MAIN_LIGHT_SHADOWS
    #pragma multi_compile _ _MAIN_LIGHT_SHADOWS_CASCADE
    

## Transparent receiving shadows

Transparent objects can now receive shadows when using shadow cascades. You
can also optionally disable shadow receiving for transparent to improve
performance. To do so, disable `Transparent Receive Shadows` in the Forward
Renderer asset.

[](../urp/upgrade-guide-7-3-0.html)

Upgrade to version 7.3.0 of the Universal Render Pipeline

[](../urp/upgrade-lwrp-to-urp.html)

Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline

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

