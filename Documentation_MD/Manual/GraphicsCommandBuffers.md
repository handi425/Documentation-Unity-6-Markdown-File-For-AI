[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/GraphicsCommandBuffers.html)
  * [中文](/cn/current/Manual/GraphicsCommandBuffers.html)
  * [日本語](/ja/current/Manual/GraphicsCommandBuffers.html)
  * [한국어](/kr/current/Manual/GraphicsCommandBuffers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/GraphicsCommandBuffers.html)
  * [中文](/cn/current/Manual/GraphicsCommandBuffers.html)
  * [日本語](/ja/current/Manual/GraphicsCommandBuffers.html)
  * [한국어](/kr/current/Manual/GraphicsCommandBuffers.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * [Custom rendering in the Built-In Render Pipeline](GraphicsCommandBuffers-landing.html)
  * CommandBuffer fundamentals in the Built-In Render Pipeline

[](GraphicsCommandBuffers-landing.html)

Custom rendering in the Built-In Render Pipeline

[](GraphicsCommandBuffers-order.html)

CameraEvent and LightEvent events order reference for the Built-In Render
Pipeline

# CommandBuffer fundamentals in the Built-In Render Pipeline

A [CommandBuffer](../ScriptReference/Rendering.CommandBuffer.html) holds a
list of rendering commands (such as setting the render target, or drawing a
given mesh). You can instruct Unity to schedule and execute those commands at
various points in the Built-in **Render Pipeline** A series of operations that
take the contents of a Scene, and displays them on a screen. Unity lets you
choose from pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), which allows you to customize
and extend Unity’s rendering functionality.

![Blurry refraction, using Command
Buffers.](../uploads/Main/RenderingCommandBufferBlurryRefraction.jpg) Blurry
refraction, using Command Buffers.

You can execute CommandBuffers immediately using the
[Graphics.ExecuteCommandBuffer](../ScriptReference/Graphics.ExecuteCommandBuffer.html)
API, or you can schedule them so that they occur at a given point in the
render pipeline. To schedule them, use the
[Camera.AddCommandBuffer](../ScriptReference/Camera.AddCommandBuffer.html) API
with the [CameraEvent enum](../ScriptReference/Rendering.CameraEvent.html),
and the
[Light.AddCommandBuffer](../ScriptReference/Light.AddCommandBuffer.html) API
with the [LightEvent enum](../ScriptReference/Rendering.LightEvent.html). To
see when Unity executes CommandBuffers that you schedule in this way, see
[CameraEvent and LightEvent order of execution](built-in-rendering-order-
landing.html).

For a full list of the commands that you can execute using CommandBuffers, see
the [CommandBuffer API
documentation](../ScriptReference/Rendering.CommandBuffer.html). Note that
some commands are supported only on certain hardware; for example, the
commands relating to **ray tracing** The process of generating an image by
tracing out rays from the Camera through each pixel and recording the color
contribution at the hit point. This is an alternative to rasterization.
raytracing  
See in [Glossary](Glossary.html#Raytracing) are supported only in DX12.

  * [Introduction to render pipelines](render-pipelines-overview.html)
  * [Execute rendering commands in a Scriptable Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/index.html)
  * [Custom rendering and post-processing in URP](urp/customizing-urp.html)

[](GraphicsCommandBuffers-landing.html)

Custom rendering in the Built-In Render Pipeline

[](GraphicsCommandBuffers-order.html)

CameraEvent and LightEvent events order reference for the Built-In Render
Pipeline

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

