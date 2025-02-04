[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UsingDX11GL3Features.html)
  * [中文](/cn/current/Manual/UsingDX11GL3Features.html)
  * [日本語](/ja/current/Manual/UsingDX11GL3Features.html)
  * [한국어](/kr/current/Manual/UsingDX11GL3Features.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UsingDX11GL3Features.html)
  * [中文](/cn/current/Manual/UsingDX11GL3Features.html)
  * [日本語](/ja/current/Manual/UsingDX11GL3Features.html)
  * [한국어](/kr/current/Manual/UsingDX11GL3Features.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * [Graphics API support](GraphicsAPIs.html)
  * DirectX

[](configure-graphicsAPIs.html)

Configure graphics APIs

[](Metal.html)

Metal

# DirectX

Unity supports the DirectX graphics API including both DirectX 11 and DirectX
12. However, not all features are available in DirectX 11. For more
information, refer to Feature comparison of DirectX 11 and DirectX 12 in
Unity.

## Set your default graphics API to DirectX

You can choose to set DirectX 11 (DX11) or DirectX 12 (DX12) as your default
Graphics API in the Editor or Standalone Player:

  1. Open the [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) (menu: **Edit** > **Project
Settings** > **Player**).

  2. In the **Other Settings** > **Rendering** section, disable the **Auto Graphics API for a platform (Windows/Mac/Linux)** option. 

  3. Select the **Add** (**+**) button, then select **Direct3D11** or **Direct3D12** from the list of the supported Graphics APIs.

## Feature comparison of DirectX 11 and DirectX 12 in Unity

The following lists include the features introduced with the DirectX 12
graphics API, which are unavailable in DirectX 11.

**APIs** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Dynamic resolution](DynamicResolution-introduction.html)A Camera setting that
allows you to dynamically scale individual render targets to reduce workload
on the GPU. [More info](DynamicResolution-landing.html)  
See in [Glossary](Glossary.html#dynamicresolution) | Unsupported | Supported  
[Asynchronous compute](../ScriptReference/Graphics.ExecuteCommandBufferAsync.html) | Unsupported | Supported  
[Native render pass](../ScriptReference/Rendering.ScriptableRenderContext.BeginRenderPass.html) | Unsupported | Supported  
[Ray tracing acceleration](../ScriptReference/Rendering.RayTracingAccelerationStructure.html) | Unsupported | Supported  
[Graphics state collection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) | Unsupported | Supported  
[XR foveated rendering](xr-foveated-rendering.html) | Unsupported | Supported  
**Render Threading Mode** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Direct](../ScriptReference/Rendering.RenderingThreadingMode.Direct.html) | Supported | Supported  
[Single threaded](../ScriptReference/Rendering.RenderingThreadingMode.SingleThreaded.html) | Supported | Supported  
[Main + render thread](../ScriptReference/Rendering.RenderingThreadingMode.MultiThreaded.html) | Supported | Supported  
[Legacy jobified](../ScriptReference/Rendering.RenderingThreadingMode.LegacyJobified.html) | Supported | Supported  
[Native graphics jobs](../ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobs.html) | Unsupported | Supported  
[Split graphics jobs](../ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobsSplitThreading.html) | Unsupported | Supported  
****Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) features** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Ray tracing shader](../ScriptReference/Rendering.RayTracingShader.html) | Unsupported | Supported  
[Inline ray tracing](../ScriptReference/ComputeShader.SetRayTracingAccelerationStructure.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_INLINE_RAY_TRACING`) | Unsupported | Supported  
[Native 16-bit](SL-ShaderCompileTargets.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_NATIVE_16BIT`) | Unsupported | Supported  
[Wave function](SL-ShaderCompileTargets.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_WAVE_ANY`) | Unsupported | Supported  
**Universal**Render Pipeline** A series of operations that take the contents
of a Scene, and displays them on a screen. Unity lets you choose from pre-
built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline)** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Raster pass merging](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/manual/render-graph-introduction.html) | Unsupported | Supported (Windows on ARM)  
[Native RenderPass](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/manual/urp-universal-renderer.html#native-renderpass) | Unsupported | Supported (Windows on ARM)  
[Framebuffer fetch](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/manual/render-graph-framebuffer-fetch.html) | Unsupported | Supported (Windows on ARM)  
**High Definition Render Pipeline** | **DirectX 11** | **DirectX 12**  
---|---|---  
[Hardware dynamic resolution](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Dynamic-Resolution.html) | Unsupported | Supported  
[Asynchronous Compute Shaders](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/frame-settings-reference.html#asynchronous-compute-shaders) | Unsupported | Supported  
[Ray traced ambient occlusion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Ambient-Occlusion.html) | Unsupported | Supported  
[Ray traced contact shadows](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Contact-Shadows.html) | Unsupported | Supported  
[Ray traced global illumination](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Global-Illumination.html) | Unsupported | Supported  
[Ray traced reflections](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Reflections.html) | Unsupported | Supported  
[Ray traced shadows](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Shadows.html) | Unsupported | Supported  
[Ray traced recursion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Tracing-Recursive-Rendering.html) | Unsupported | Supported  
[Ray traced subsurface scattering](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Subsurface-Scattering.html) | Unsupported | Supported  
  
## Additional resources

  * [Configure graphics APIs](configure-graphicsAPIs.html)
  * [Surface Shaders with DX11 / OpenGL Core Tessellation](SL-SurfaceShaderTessellation.html)
  * [Surface shaders and DirectX 11 HLSL syntax](SL-SurfaceShaders.html#surface-shaders-directX)

[](configure-graphicsAPIs.html)

Configure graphics APIs

[](Metal.html)

Metal

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

