[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SRPBatcher-Materials.html)
  * [中文](/cn/current/Manual/SRPBatcher-Materials.html)
  * [日本語](/ja/current/Manual/SRPBatcher-Materials.html)
  * [한국어](/kr/current/Manual/SRPBatcher-Materials.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SRPBatcher-Materials.html)
  * [中文](/cn/current/Manual/SRPBatcher-Materials.html)
  * [日本語](/ja/current/Manual/SRPBatcher-Materials.html)
  * [한국어](/kr/current/Manual/SRPBatcher-Materials.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [Scriptable Render Pipeline (SRP) Batcher in URP](SRPBatcher-landing.html)
  * Check whether a GameObject is compatible with the SRP Batcher in URP

[](SRPBatcher.html)

Scriptable Render Pipeline Batcher in URP

[](SRPBatcher-Enable.html)

Enable the SRP Batcher in URP

# Check whether a GameObject is compatible with the SRP Batcher in URP

## GameObject compatibility

In any given **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), some **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) are compatible with the SRP
Batcher, and some aren’t. Compatible GameObjects use the SRP Batcher code
path, and non-compatible GameObjects use the standard SRP code path. For more
information, see [How the SRP Batcher works](SRPBatcher.html#how-the-srp-
batcher-works).

A GameObject must meet the following requirements to be compatible with the
SRP Batcher code path:

  * The GameObject must contain either a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) or a skinned mesh. It can’t be a
particle.

  * The GameObject mustn’t use [MaterialPropertyBlocks](../ScriptReference/MaterialPropertyBlock.html).
  * The **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that the GameObject uses must be
compatible with the SRP Batcher. For more information, see Shader
compatibility.

## Shader compatibility

All lit and unlit shaders in the the Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) and the High Definition
Render Pipeline (HDRP) fit this requirement (except for the particle versions
of these shaders).

For a custom shader to be compatible with the SRP Batcher it must meet the
following requirements:

  * The shader must declare all built-in engine properties in a single constant buffer named `UnityPerDraw`. For example, `unity_ObjectToWorld`, or `unity_SHAr`.
  * The shader must declare all material properties in a single constant buffer named `UnityPerMaterial`.

You can check the compatibility status of a shader in the **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) panel.

![You can check the compatibility of your shaders in the Inspector panel for
the specific shader.](../uploads/Main/SRP_batcher_shader_compatibility.png)
You can check the compatibility of your shaders in the Inspector panel for the
specific shader.

[](SRPBatcher.html)

Scriptable Render Pipeline Batcher in URP

[](SRPBatcher-Enable.html)

Enable the SRP Batcher in URP

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

