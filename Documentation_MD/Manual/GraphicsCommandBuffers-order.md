[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/GraphicsCommandBuffers-order.html)
  * [中文](/cn/current/Manual/GraphicsCommandBuffers-order.html)
  * [日本語](/ja/current/Manual/GraphicsCommandBuffers-order.html)
  * [한국어](/kr/current/Manual/GraphicsCommandBuffers-order.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/GraphicsCommandBuffers-order.html)
  * [中文](/cn/current/Manual/GraphicsCommandBuffers-order.html)
  * [日本語](/ja/current/Manual/GraphicsCommandBuffers-order.html)
  * [한국어](/kr/current/Manual/GraphicsCommandBuffers-order.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * [Custom rendering in the Built-In Render Pipeline](GraphicsCommandBuffers-landing.html)
  * CameraEvent and LightEvent events order reference for the Built-In Render Pipeline

[](GraphicsCommandBuffers.html)

CommandBuffer fundamentals in the Built-In Render Pipeline

[](post-processing-and-full-screen-effects.html)

Post-processing and full-screen effects

# CameraEvent and LightEvent events order reference for the Built-In Render
Pipeline

## CameraEvent

The order of execution for CameraEvents depends on the [rendering
path](RenderingPaths.html)The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) that your Project uses.

### Deferred rendering path

  * [BeforeGBuffer](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeGBuffer.html): Unity renders opaque geometry
  * [AfterGBuffer](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterGBuffer.html): Unity resolves depth.
  * [BeforeReflections](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeReflections.html): Unity renders default reflections, and **Reflection Probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) reflections.

  * [AfterReflections](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterReflections.html): Unity copies reflections to the Emissive channel of the G-buffer.
  * [BeforeLighting](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeLighting.html): Unity renders shadows. See LightEvent order of execution.
  * [AfterLighting](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterLighting.html)
  * [BeforeFinalPass](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeFinalPass.html): Unity processes the final pass.
  * [AfterFinalPass](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterFinalPass.html)
  * [BeforeForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardOpaque.html) (only called if there is opaque geometry that cannot be rendered using deferred): Unity renders opaque geometry that cannot be rendered with deferred rendering.
  * [AfterForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardOpaque.html) (only called if there is opaque geometry that cannot be rendered using deferred)
  * [BeforeSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeSkybox.html): Unity renders the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox).

  * [AfterSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterSkybox.html): Unity renders halos.
  * [BeforeImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffectsOpaque.html): Unity applies opaque-only **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effects.

  * [AfterImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffectsOpaque.html)
  * [BeforeForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardAlpha.html): Unity renders transparent geometry, and **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Canvases with a Rendering Mode of **Screen
Space -**Camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)**.

  * [AfterForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardAlpha.html): [BeforeHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeHaloAndLensFlares.html): Unity renders **lens flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](class-LensFlare.html)  
See in [Glossary](Glossary.html#LensFlare).

  * [AfterHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterHaloAndLensFlares.html)
  * [BeforeImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffects.html): Unity applies post-processing effects.
  * [AfterImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffects.html)
  * [AfterEverything](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterEverything.html): Unity renders UI Canvases with a Rendering Mode that is not **Screen Space - Camera**.

### Forward rendering path

  * [BeforeDepthTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeDepthTexture.html): Unity renders depth for opaque geometry.
  * [AfterDepthTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterDepthTexture.html)
  * [BeforeDepthNormalsTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeDepthNormalsTexture.html): Unity renders depth normals for opaque geometry.
  * [AfterDepthNormalsTexture](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterDepthNormalsTexture.html): Unity renders shadows. See LightEvent order of execution.
  * [BeforeForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardOpaque.html): Unity renders opaque geometry.
  * [AfterForwardOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardOpaque.html)
  * [BeforeSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeSkybox.html): Unity renders the skybox.
  * [AfterSkybox](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterSkybox.html): Unity renders halos.
  * [BeforeImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffectsOpaque.html): Unity applies opaque-only post-processing effects.
  * [AfterImageEffectsOpaque](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffectsOpaque.html)
  * [BeforeForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeForwardAlpha.html): Unity renders transparent geometry, and UI Canvases with a Rendering Mode of **Screen Space - Camera**.
  * [AfterForwardAlpha](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterForwardAlpha.html)
  * [BeforeHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeHaloAndLensFlares.html): Unity renders lens flares.
  * [AfterHaloAndLensFlares](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterHaloAndLensFlares.html)
  * [BeforeImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.BeforeImageEffects.html): Unity applies post-processing effects.
  * [AfterImageEffects](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterImageEffects.html)
  * [AfterEverything](https://docs.unity3d.com/ScriptReference/Rendering.CameraEvent.AfterEverything.html): Unity renders UI Canvases with a Rendering Mode that is not **Screen Space - Camera**.

## LightEvent order of execution

During the “render shadows” stage above, for each shadow-casting Light, Unity
performs these steps:

  * [BeforeShadowMap](../ScriptReference/Rendering.LightEvent.BeforeShadowMap.html)
  * [BeforeShadowMapPass](../ScriptReference/Rendering.LightEvent.BeforeShadowMapPass.html): Unity renders all shadow casters for the current Pass
  * [AfterShadowMapPass](../ScriptReference/Rendering.LightEvent.AfterShadowMapPass.html): Unity repeats the last three steps, for each Pass
  * [AfterShadowMap](../ScriptReference/Rendering.LightEvent.AfterShadowMap.html)
  * [BeforeScreenSpaceMask](../ScriptReference/Rendering.LightEvent.BeforeScreenSpaceMask.html): Unity gathers the shadow map into a screen space buffer and performs filtering
  * [AfterScreenSpaceMask](../ScriptReference/Rendering.LightEvent.AfterScreenSpaceMask.html)

[](GraphicsCommandBuffers.html)

CommandBuffer fundamentals in the Built-In Render Pipeline

[](post-processing-and-full-screen-effects.html)

Post-processing and full-screen effects

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

