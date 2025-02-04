[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/rendering/render-passes-deferred.html)
  * [中文](/cn/current/Manual/urp/rendering/render-passes-deferred.html)
  * [日本語](/ja/current/Manual/urp/rendering/render-passes-deferred.html)
  * [한국어](/kr/current/Manual/urp/rendering/render-passes-deferred.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/rendering/render-passes-deferred.html)
  * [中文](/cn/current/Manual/urp/rendering/render-passes-deferred.html)
  * [日本語](/ja/current/Manual/urp/rendering/render-passes-deferred.html)
  * [한국어](/kr/current/Manual/urp/rendering/render-passes-deferred.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Get started with URP](../../urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](../../urp/urp-concepts.html)
  * [Rendering paths in URP](../../urp/rendering-paths-landing.html)
  * [Deferred rendering path in URP](../../urp/rendering/deferred-rendering-path-landing.html)
  * Render passes in the Deferred rendering path in URP

[](../../urp/rendering/deferred-rendering-path-introduction.html)

Introduction to the deferred rendering path

[](../../urp/rendering/g-buffer-layout.html)

G-buffer layout in the Deferred rendering path in URP

# Render passes in the Deferred rendering path in URP

The following table lists the render passes the Deferred **rendering path**
The technique that a render pipeline uses to render graphics. Choosing a
different rendering path affects how lighting and shading are calculated. Some
rendering paths are more suited to different platforms and hardware than
others. [More info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath) uses.

**Render event** | **Render pass that occurs after the render event** | **Description**  
---|---|---  
**BeforeRendering** | - | -  
**BeforeRenderingShadows** | - | -  
**AfterRenderingShadows** | - | -  
**BeforeRenderingPrePasses** |  **DepthPrepass** , or **DepthPrepass** and **DepthNormalPrepass**. | Render depth and normal textures in a prepass, for materials that Unity renders in a Forward pass.  
**AfterRenderingPrePasses** | - | -  
**BeforeRenderingGbuffer** | **GBufferPass** | Render the G-Buffer, then copy the G-Buffer depth texture.  
**AfterRenderingGbuffer** | **SSAO** | Calculate the screen space **ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](../../Glossary.html#Ambientocclusion) (SSAO) texture. Unity
calculates this here only if you [enable SSAO](../post-processing-ssao.html),
and disable **After Opaque**.  
**BeforeRenderingDeferredLights** | **Deferred Pass** | Deferred rendering. Unity uses the SSAO texture during this render pass, if it was created.  
**AfterRenderingDeferredLights** | - | -  
**BeforeRenderingOpaques** | - | Render opaque forward-only materials.  
**AfterRenderingOpaques** | - | Calculate and blend the screen space ambient occlusion (SSAO) texture. Unity calculates this here only if you [enable SSAO](../post-processing-ssao.html), and enable **After Opaque**.  
**BeforeRenderingSkybox** | - | -  
**AfterRenderingSkybox** | - | -  
**BeforeRenderingTransparents** | - | -  
**AfterRenderingTransparents** | - | -  
**BeforeRenderingPostProcessing** | - | -  
**AfterRenderingPostProcessing** | - | -  
**AfterRendering** | - | -  
  
For the full list of render events, and injection points for custom render
passes, refer to [Injection points reference for URP](../customize/custom-
pass-injection-points.html).

## Source code reference

The following table lists the files that contain code related to the Deferred
rendering path, located in the `com.unity.render-pipelines.universal` folder.

**File path** | **Description**  
---|---  
`Runtime\DeferredLights.cs` | The main class that handles the Deferred rendering path.  
`Runtime\Passes\GBufferPass.cs` |  `ScriptableRenderPass` for the G-Buffer pass.  
`Runtime\Passes\DeferredPass.cs` |  `ScriptableRenderPass` for the **deferred shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](../../RenderTech-DeferredShading.html)  
See in [Glossary](../../Glossary.html#Deferredshading) pass.  
`Shaders\Utils\Deferred.hlsl` | Utility functions for deferred shading.  
`Shaders\Utils\StencilDeferred.shader` | **Shader** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) asset for deferred shading.  
`Shaders\Utils\UnityGBuffer.hlsl` | Utility functions for storing and loading material properties from the G-Buffer.  
  
## Additional resources

  * [Custom rendering and post-processing in URP](../customizing-urp.html)

[](../../urp/rendering/deferred-rendering-path-introduction.html)

Introduction to the deferred rendering path

[](../../urp/rendering/g-buffer-layout.html)

G-buffer layout in the Deferred rendering path in URP

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

