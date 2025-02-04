[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/static-batching-enable.html)
  * [中文](/cn/current/Manual/static-batching-enable.html)
  * [日本語](/ja/current/Manual/static-batching-enable.html)
  * [한국어](/kr/current/Manual/static-batching-enable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/static-batching-enable.html)
  * [中文](/cn/current/Manual/static-batching-enable.html)
  * [日本語](/ja/current/Manual/static-batching-enable.html)
  * [한국어](/kr/current/Manual/static-batching-enable.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [Batching draw calls](DrawCallBatching-landing.html)
  * [Batching static GameObjects](static-batching-landing.html)
  * Enable static batching

[](static-batching.html)

Introduction to static batching

[](dynamic-batching-landing.html)

Batching moving GameObjects

# Enable static batching

Unity can perform **static batching** A technique Unity uses to draw
GameObjects on the screen that combines static (non-moving) GameObjects into
big Meshes, and renders them in a faster way. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching) at build time and at runtime.
As a general rule, if the **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) exist in a **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) before you build your application, use
the Editor to batch your GameObjects at build time. If you create the
GameObjects and their meshes at runtime, use the runtime API.

When you use the runtime API, you can change the transform properties of the
root of a static batch. This means that you can move, rotate, or scale the
entire combination of meshes that make up a static batch. You can’t change the
transform properties of the individual meshes.

To use static batching for a set of GameObjects, the GameObjects must be
eligible for static batching. In addition to the criteria described in the
[common usage information](DrawCallBatching-Enable.html), make sure that:

  * The GameObject is active.
  * The GameObject has a [Mesh Filter](class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](class-MeshFilter.html)  
See in [Glossary](Glossary.html#MeshFilter) component, and that component is
enabled.

  * The Mesh Filter component has a reference to a [Mesh](class-Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh).

  * The mesh has a vertex count greater than 0.
  * The mesh has not already been combined with another Mesh.
  * The GameObject has a [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) component, and that component is
enabled.

  * The Mesh Renderer component does not use any Material with a **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that has the `DisableBatching` tag set
to true.

  * Meshes you want to batch together use the same vertex attributes. For example Unity can batch meshes that use vertex position, vertex normal, and one UV with one another, but not with meshes that use vertex position, vertex normal, UV0, UV1, and vertex tangent.

**Note** : To use runtime static batching you must also set the mesh to have
read/write enabled.

For information about the performance implications for static batching, see
[Performance implications](static-batching.html#performance-implications).

## Static batching at build time

You can enable static batching at build time in the Editor.

To perform static batching at build time:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , enable **Static Batching**.
  3. In the Scene view or Hierarchy, select the GameObject that you want to batch and view it in the Inspector.  
**Tip** : You can select multiple GameObjects at the same time to enable
static batching for all of them.

  4. In the GameObject’s [Static Editor Flags](StaticObjects.html), enable **Batching Static**.

Unity automatically batches the specified static meshes into the same draw
call if they fulfill the criteria described in the [common usage
information](DrawCallBatching-Enable.html).

![The Static Editor Flags checkbox in the Inspector for a
GameObject.](../uploads/Main/StaticTagInspector.png) The Static Editor Flags
checkbox in the Inspector for a GameObject.

**Note** : If you perform static batching at build time, Unity doesn’t use any
CPU resources at runtime to generate the mesh data for the static batch.

## Static batching at runtime

To batch static meshes at runtime, Unity provides the
[StaticBatchingUtility](../ScriptReference/StaticBatchingUtility.html) class.
The static
[StaticBatchingUtility.Combine](../ScriptReference/StaticBatchingUtility.Combine.html)
method combines the GameObjects you pass in and prepares them for static
batching. This is especially useful for meshes that you procedurally generate
at runtime.

Unlike static batching at build time, batching at runtime doesn’t require you
to enable the **Static Batching** Player Setting. For information on how to
use this API, see
[StaticBatchingUtility](../ScriptReference/StaticBatchingUtility.html).

[](static-batching.html)

Introduction to static batching

[](dynamic-batching-landing.html)

Batching moving GameObjects

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

