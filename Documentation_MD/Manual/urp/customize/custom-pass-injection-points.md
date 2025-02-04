[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/customize/custom-pass-injection-points.html)
  * [中文](/cn/current/Manual/urp/customize/custom-pass-injection-points.html)
  * [日本語](/ja/current/Manual/urp/customize/custom-pass-injection-points.html)
  * [한국어](/kr/current/Manual/urp/customize/custom-pass-injection-points.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/customize/custom-pass-injection-points.html)
  * [中文](/cn/current/Manual/urp/customize/custom-pass-injection-points.html)
  * [日本語](/ja/current/Manual/urp/customize/custom-pass-injection-points.html)
  * [한국어](/kr/current/Manual/urp/customize/custom-pass-injection-points.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](../../urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](../../urp/inject-a-render-pass.html)
  * Injection points reference for URP

[](../../urp/customize/inject-render-pass-via-script.html)

Inject a render pass via scripting in URP

[](../../urp/compatibility-mode.html)

Compatibility Mode in URP

# Injection points reference for URP

URP contains multiple injection points that let you inject render passes into
the frame rendering loop and execute them upon different events.

Injection points give a custom render pass access to URP buffers. A render
pass has read and write access to all buffers at each injection point.

Unity provides the following events in the rendering loop. You can use these
events to inject your custom passes.

**Injection point** | **Description**  
---|---  
BeforeRendering | Executes a `ScriptableRenderPass` instance before rendering any other passes in the pipeline for the current **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera). Camera matrices and stereo
rendering are not setup at this point. You can use this injection point to
draw to custom input textures used later in the pipeline, for example, LUT
textures.  
BeforeRenderingShadows | Executes a `ScriptableRenderPass` instance before rendering shadow maps (**MainLightShadow** , **AdditionalLightsShadow** passes).  
Camera matrices and stereo rendering are not set up at this point.  
AfterRenderingShadows | Executes a `ScriptableRenderPass` instance after rendering shadow maps (**MainLightShadow** , **AdditionalLightsShadow** passes).  
Camera matrices and stereo rendering are not set up this point.  
BeforeRenderingPrePasses | Executes a `ScriptableRenderPass` instance before rendering prepasses (**DepthPrepass** , **DepthNormalPrepass** passes).  
Camera matrices and stereo rendering are already set up at this point.  
AfterRenderingPrePasses | Executes a `ScriptableRenderPass` instance after rendering prepasses (**DepthPrepass** , **DepthNormalPrepass** passes).  
Camera matrices and stereo rendering are set up at this point.  
BeforeRenderingGbuffer | Executes a `ScriptableRenderPass` instance before rendering the **GBuffer** pass.  
AfterRenderingGbuffer | Executes a `ScriptableRenderPass` instance after rendering the **GBuffer** pass.  
BeforeRenderingDeferredLights | Executes a `ScriptableRenderPass` instance before rendering the **Deferred** pass.  
AfterRenderingDeferredLights | Executes a `ScriptableRenderPass` instance after rendering the **Deferred** pass.  
BeforeRenderingOpaques | Executes a `ScriptableRenderPass` instance before rendering opaque objects (**DrawOpaqueObjects** pass).  
AfterRenderingOpaques | Executes a `ScriptableRenderPass` instance after rendering opaque objects (**DrawOpaqueObjects** pass).  
BeforeRenderingSkybox | Executes a `ScriptableRenderPass` instance before rendering the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](../../sky-landing.html)  
See in [Glossary](../../Glossary.html#Skybox) (**Camera.RenderSkybox** pass).  
AfterRenderingSkybox | Executes a `ScriptableRenderPass` instance after rendering the skybox (**Camera.RenderSkybox** pass).  
BeforeRenderingTransparents | Executes a `ScriptableRenderPass` instance before rendering transparent objects (**DrawTransparentObjects** pass).  
AfterRenderingTransparents | Executes a `ScriptableRenderPass` instance after rendering transparent objects (**DrawTransparentObjects** pass).  
BeforeRenderingPostProcessing | Executes a `ScriptableRenderPass` instance before rendering **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../../PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](../../Glossary.html#post-processing) effects (**Render
PostProcessing Effects** pass).  
AfterRenderingPostProcessing | Executes a `ScriptableRenderPass` instance after rendering post-processing effects but before the final **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](../../Glossary.html#blit), post-processing anti-aliasing
effects, and color grading.  
AfterRendering | Executes `ScriptableRenderPass` instance after rendering all other passes.  
  
The following diagram shows the passes and the flow of frame resources in a
URP frame:

![URP frame rendering graph and pases](../../../uploads/urp/customizing-
urp/urp-frame-graph-passes.png) URP frame rendering graph and pases

[](../../urp/customize/inject-render-pass-via-script.html)

Inject a render pass via scripting in URP

[](../../urp/compatibility-mode.html)

Compatibility Mode in URP

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

