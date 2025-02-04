[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/stp/stp-upscaler.html)
  * [中文](/cn/current/Manual/urp/stp/stp-upscaler.html)
  * [日本語](/ja/current/Manual/urp/stp/stp-upscaler.html)
  * [한국어](/kr/current/Manual/urp/stp/stp-upscaler.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/stp/stp-upscaler.html)
  * [中文](/cn/current/Manual/urp/stp/stp-upscaler.html)
  * [日本語](/ja/current/Manual/urp/stp/stp-upscaler.html)
  * [한국어](/kr/current/Manual/urp/stp/stp-upscaler.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Upscaling resolution in URP with Spatial-Temporal Post-Processing](../../urp/change-resolution-scale-urp.html)
  * Introduction to Spatial-Temporal Post-processing in URP

[](../../urp/change-resolution-scale-urp.html)

Upscaling resolution in URP with Spatial-Temporal Post-Processing

[](../../urp/stp/stp-enable.html)

Enable Spatial-Temporal Post-processing in URP

# Introduction to Spatial-Temporal Post-processing in URP

Spatial-Temporal **Post-Processing** A process that improves product visuals
by applying filters and effects before the image appears on screen. You can
use post-processing effects to simulate physical camera and film properties,
for example Bloom and Depth of Field. [More
info](../../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../../Glossary.html#post-processing) (STP) uses spatial and
temporal upsampling techniques to produce a high quality, anti-aliased image.

STP is a software-based upscaler.

## Requirements

STP uses compute **shaders** A program that runs on the GPU. [More
info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader), so target platforms must
support [Shader Model 5.0](https://learn.microsoft.com/en-
us/windows/win32/direct3dhlsl/d3d11-graphics-reference-sm5).

STP doesn’t support OpenGL ES, even if the platform supports compute shaders.

STP requires [temporal anti-aliasing (TAA)](../anti-aliasing.md) pre-
processing, it will implicitly enable it if not selected already.

## STP performance

STP configures itself automatically to provide the best balance of performance
and quality based on the platform your application runs on. You don’t need to
configure it for each different platform.

On high-performance platforms, like PCs and consoles, STP uses higher quality
image filtering logic and additional deringing logic to improve image quality
when it upscales images. These techniques require additional processing power
and Unity uses them on high-performance devices where the performance impact
is not significant.

On mobile devices, STP uses more performant image filtering logic to provide a
balance between performance and image quality. This minimizes the performance
impact of STP on less powerful devices, while still delivering a high quality
image.

## Additional resources

  * [Enable Spatial Temporal Post-processing](stp-enable.html)
  * [Spatial Temporal Post-processing debug views](stp-debug-views.html)

[](../../urp/change-resolution-scale-urp.html)

Upscaling resolution in URP with Spatial-Temporal Post-Processing

[](../../urp/stp/stp-enable.html)

Enable Spatial-Temporal Post-processing in URP

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

