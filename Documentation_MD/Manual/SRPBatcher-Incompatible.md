[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SRPBatcher-Incompatible.html)
  * [中文](/cn/current/Manual/SRPBatcher-Incompatible.html)
  * [日本語](/ja/current/Manual/SRPBatcher-Incompatible.html)
  * [한국어](/kr/current/Manual/SRPBatcher-Incompatible.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SRPBatcher-Incompatible.html)
  * [中文](/cn/current/Manual/SRPBatcher-Incompatible.html)
  * [日本語](/ja/current/Manual/SRPBatcher-Incompatible.html)
  * [한국어](/kr/current/Manual/SRPBatcher-Incompatible.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [Scriptable Render Pipeline (SRP) Batcher in URP](SRPBatcher-landing.html)
  * Remove SRP Batcher compatibility for GameObjects in URP

[](SRPBatcher-Profile.html)

Troubleshoot the SRP Batcher in URP

[](batch-renderer-group.html)

BatchRendererGroup API in URP

# Remove SRP Batcher compatibility for GameObjects in URP

In some rare cases, you might want to intentionally make particular
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) incompatible with the SRP Batcher.
For example, if you want to use [GPU instancing](GPUInstancing.html), which
isn’t compatible with the SRP Batcher. If you want to render many identical
meshes with the exact same material, GPU instancing can be more efficient than
the SRP Batcher. To use GPU instancing, you must either:

  * Use [Graphics.RenderMeshInstanced](../ScriptReference/Graphics.RenderMeshInstanced.html).
  * Manually remove SRP Batcher compatibility and enable GPU instancing for the material.

There are two ways to remove compatibility with the SRP Batcher from a
GameObject:

  * Make the **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) incompatible.

  * Make the renderer incompatible.

**Tip** : If you use GPU instancing instead of the SRP Batcher, use the
[Profiler](Profiler.html)A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) to make sure that GPU instancing is
more efficient for your application than the SRP Batcher.

## Removing shader compatibility

You can make both hand-written and Shader Graph shaders incompatible with the
SRP Batcher. However, for Shader Graph shaders, if you change and recompile
the Shader Graph often, it’s simpler to make the renderer incompatible
instead.

To make a Unity shader incompatible with the SRP Batcher, you need to make
changes to the shader source file:

  1. For hand-written shaders, open the shader source file. For Shader Graph shaders, copy the Shader Graph’s compiled shader source code into a new shader source file. Use the new shader source file in your application instead of the Shader Graph.
  2. Add a new [material property](SL-Properties.html) declaration into the shader’s `Properties` block. Don’t declare the new material property in the `UnityPerMaterial` constant buffer.

The material property doesn’t need to do anything; just having a material
property that doesn’t exist in the `UnityPerMaterial` constant buffer makes
the shader incompatible with the SRP Batcher.

**Warning** : If you use a Shader Graph, be aware that every time you edit and
recompile the Shader Graph, you must repeat this process.

## Removing renderer compatibility

You can make individual renderers incompatible with the SRP Batcher. To do
this, add a `MaterialPropertyBlock` to the renderer.

[](SRPBatcher-Profile.html)

Troubleshoot the SRP Batcher in URP

[](batch-renderer-group.html)

BatchRendererGroup API in URP

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

