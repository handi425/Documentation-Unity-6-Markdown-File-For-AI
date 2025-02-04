[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/resolution-scale-introduction.html)
  * [中文](/cn/current/Manual/resolution-scale-introduction.html)
  * [日本語](/ja/current/Manual/resolution-scale-introduction.html)
  * [한국어](/kr/current/Manual/resolution-scale-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/resolution-scale-introduction.html)
  * [中文](/cn/current/Manual/resolution-scale-introduction.html)
  * [日本語](/ja/current/Manual/resolution-scale-introduction.html)
  * [한국어](/kr/current/Manual/resolution-scale-introduction.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Changing resolution scale](resolution-scale.html)
  * Introduction to changing resolution scale

[](resolution-scale.html)

Changing resolution scale

[](DynamicResolution-landing.html)

Dynamic Resolution

# Introduction to changing resolution scale

To reduce the amount of work for the GPU and speed up rendering, you can
change the resolution of the image Unity renders. For example, you can render
at a lower resolution when the frame rate of the application decreases.

When you change the resolution scale, Unity does the following:

  1. Renders at a lower resolution.
  2. Uses one of several upscaling technique to increases the resolution of the rendered image, so it matches the final image.

If you use the Universal Render Pipeline (URP) or the Built-In Render
Pipeline, you can only use dynamic resolution on some platforms.

For more information, refer to:

  * [Dynamic resolution](DynamicResolution-landing.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html)  
See in [Glossary](Glossary.html#dynamicresolution) if you use URP or the
Built-In Render Pipeline.

  * [Dynamic resolution in the High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Dynamic-Resolution.html)

## Upscaling techniques

The upscaling techniques depend on the [render pipeline](render-
pipelines.html)A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) you choose and the platform
you build for.

The Built-In Render Pipeline always uses a filtering technique the GPU
provides.

**Feature** | **What the feature uses to upscale the image** | **URP** | **HDRP**  
---|---|---|---  
Bilinear | The bilinear or linear filtering the graphics API provides. | Yes. Refer to [quality settings in the URP asset](urp/universalrp-asset.html#quality) | No.  
Nearest-neighbor | The nearest-neighbor or point sampling filtering the graphics API provides. | Yes. Refer to [quality settings in the URP asset](urp/universalrp-asset.html#quality) | No.  
Catmull-Rom | Four bilinear samples. | No | Yes. Refer to [Choose an upscale filter in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Dynamic-Resolution.html#choose-an-upscale-filter).  
AMD FidelityFX Contrast Adaptive Sharpen (CAS) | Contrast levels. | No | Yes. Refer to [Choose an upscale filter in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Dynamic-Resolution.html#choose-an-upscale-filter).  
Temporal Anti-Aliasing Upscaling (TAAU) | Data from previous frames. | No | Yes. Refer to [Choose an upscale filter in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Dynamic-Resolution.html#choose-an-upscale-filter).  
Spatial-Temporal **Post-processing** A process that improves product visuals
by applying filters and effects before the image appears on screen. You can
use post-processing effects to simulate physical camera and film properties,
for example Bloom and Depth of Field. [More info](PostProcessingOverview.html)
post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) (STP) | Multiple input textures. STP configures itself automatically to provide the best balance of performance and quality based on the platform. | Yes, but you can’t use STP together with dynamic resolution. Refer to [Upscaling resolution in URP with STP](urp/change-resolution-scale-urp.html). | Yes, but you can’t use STP together with software dynamic resolution. Refer to [STP in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/stp/stp-upscaler).  
AMD FidelityFX Super Resolution (FSR) 1 | The frame buffer. | Yes. Refer to Refer to [quality settings in the URP asset](urp/universalrp-asset.html#quality). | Yes. Refer to [Choose an upscale filter in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Dynamic-Resolution.html#choose-an-upscale-filter).  
AMD FidelityFX Super Resolution (FSR) 2 | Multiple input textures. | No | Yes. Refer to [Choose an upscale filter in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Dynamic-Resolution.html#choose-an-upscale-filter).  
NVIDIA Deep Learning Super Sampling (DLSS) | Multiple input textures. | No | Yes. Refer to [DLSS in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/deep-learning-super-sampling-in-hdrp.html).  
  
## Additional resources

  * [Choosing a render pipeline](choose-a-render-pipeline-landing.html)
  * [Graphics rendering: Getting the best performance with Unity 6](https://www.youtube.com/watch?v=Oc6T4hh5gaI)

[](resolution-scale.html)

Changing resolution scale

[](DynamicResolution-landing.html)

Dynamic Resolution

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

