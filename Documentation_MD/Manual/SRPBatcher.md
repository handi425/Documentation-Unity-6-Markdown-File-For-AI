[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SRPBatcher.html)
  * [中文](/cn/current/Manual/SRPBatcher.html)
  * [日本語](/ja/current/Manual/SRPBatcher.html)
  * [한국어](/kr/current/Manual/SRPBatcher.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SRPBatcher.html)
  * [中文](/cn/current/Manual/SRPBatcher.html)
  * [日本語](/ja/current/Manual/SRPBatcher.html)
  * [한국어](/kr/current/Manual/SRPBatcher.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [Scriptable Render Pipeline (SRP) Batcher in URP](SRPBatcher-landing.html)
  * Scriptable Render Pipeline Batcher in URP

[](SRPBatcher-landing.html)

Scriptable Render Pipeline (SRP) Batcher in URP

[](SRPBatcher-Materials.html)

Check whether a GameObject is compatible with the SRP Batcher in URP

# Scriptable Render Pipeline Batcher in URP

The Scriptable **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (SRP) Batcher is a [draw call
optimization](optimizing-draw-calls.html) that significantly improves
performance for applications that use an SRP. The SRP Batcher reduces the CPU
time Unity requires to prepare and dispatch draw calls for materials that use
the same **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) variant.

![The Scriptable Render Pipeline \(SRP\) Batcher reduces the CPU time Unity
requires to render scenes with many materials that use the same shader
variant.](../uploads/Main/SRPBatcher.png) The Scriptable Render Pipeline (SRP)
Batcher reduces the CPU time Unity requires to render scenes with many
materials that use the same shader variant.

## Requirements and compatibility

This section includes information about the render pipeline compatibility of
the SRP Batcher.

### Render pipeline compatibility

**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**SRP Batcher** | Yes | Yes | Yes | No  
  
## How the SRP Batcher works

The traditional way to optimize draw calls is to reduce the number of them.
Instead, the SRP Batcher reduces render-state changes between draw calls. To
do this, the SRP Batcher combines a sequence of `bind` and `draw` GPU
commands. Each sequence of commands is called an SRP batch.

![The batching of bind and draw commands reduces the GPU setup between draw
calls.](../uploads/Main/SROShaderPass.png) The batching of bind and draw
commands reduces the GPU setup between draw calls.

To achieve optimal performance for your rendering, each SRP batch should
contain as many `bind` and `draw` commands as possible. To achieve this, use
as few shader variants as possible. You can still use as many different
materials with the same shader as you want.

When Unity detects a new material during the render loop, the CPU collects all
properties and binds them to the GPU in constant buffers. The number of GPU
buffers depends on how the shader declares its constant buffers.

The SRP Batcher is a low-level render loop that makes material data persist in
GPU memory. If the material content doesn’t change, theSRP Batcher doesn’t
make any render-state changes. Instead, the SRP Batcher uses a dedicated code
path to update the Unity Engine properties in a large GPU buffer, like this:

![The SRP Batcher rendering workflow. The SRP Batcher uses a dedicated code
path to update the Unity Engine properties in a large GPU
buffer.](../uploads/Main/SRP_Batcher_loop.png) The SRP Batcher rendering
workflow. The SRP Batcher uses a dedicated code path to update the Unity
Engine properties in a large GPU buffer.

Here, the CPU only handles the Unity Engine properties, labeled **Per Object
large buffer** in the above diagram. All materials have persistent constant
buffers located in GPU memory, which are ready to use. This speeds up
rendering because:

  * All material content now persists in GPU memory.
  * Dedicated code manages a large per-object GPU constant buffer for all per-object properties.

[](SRPBatcher-landing.html)

Scriptable Render Pipeline (SRP) Batcher in URP

[](SRPBatcher-Materials.html)

Check whether a GameObject is compatible with the SRP Batcher in URP

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

