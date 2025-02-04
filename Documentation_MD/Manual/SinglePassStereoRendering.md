[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SinglePassStereoRendering.html)
  * [中文](/cn/current/Manual/SinglePassStereoRendering.html)
  * [日本語](/ja/current/Manual/SinglePassStereoRendering.html)
  * [한국어](/kr/current/Manual/SinglePassStereoRendering.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SinglePassStereoRendering.html)
  * [中文](/cn/current/Manual/SinglePassStereoRendering.html)
  * [日本語](/ja/current/Manual/SinglePassStereoRendering.html)
  * [한국어](/kr/current/Manual/SinglePassStereoRendering.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR graphics](xr-graphics.html)
  * Stereo rendering

[](xr-render-pipeline-compatibility.html)

Universal Render Pipeline compatibility in XR

[](SinglePassInstancing.html)

Single-pass instanced rendering and custom shaders

# Stereo rendering

VR and most **MR** Mixed Reality  
See in [Glossary](Glossary.html#MR) devices require rendering the Unity
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in stereo. Unity **XR** An umbrella
term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed
Reality (MR) applications. Devices supporting these forms of interactive
applications can be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) supports two stereo render modes:

  * **Multi-pass** : in this mode, Unity performs a render pass for each eye. Some parts of the render loop are shared between the two passes, so multi-pass rendering is faster than rendering the scene with two unique **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Multi-pass mode provides the widest
compatibility with existing **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) and rendering utilities, but is slower
than single pass instanced mode.

  * **Single-pass instanced** : in this mode, Unity renders the scene in a single pass using instanced draw calls. This mode greatly decreases CPU usage and slightly decreases GPU usage compared to the multi-pass mode.
  * **Multiview** : A variation of single-pass instanced rendering supported by some OpenGL and OpenGL ES devices. This option replaces single-pass instanced when available.

**Note:** The earlier technique of rendering the scene into a double-wide
texture using a single render pass is no longer available.

Single-pass instanced stereo rendering is now available on most **VR** Virtual
Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) platforms.

## Set the render mode

You can find the **Render mode** setting under **XR**Plug-in** A set of code
created outside of Unity that creates functionality in Unity. There are two
kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) Management** in ****Project
Settings** A broad collection of settings which allow you to configure how
Physics, Audio, Networking, Graphics, Input and many other areas of your
project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings)**. Each XR provider plug-in
provides its own setting, if supported.

To set a render mode:

  1. Open **Project Settings** (menu: **Edit > Project Settings**).

  2. Expand the **XR Plugin Management** section, if necessary.

  3. Select the settings page for the relevant provider plug-in.

  4. Choose a mode from the list.

![](../uploads/Main/SinglePassStereoRendering3.png)  
_Render mode options in the MockHMD provider plug-in_

**Note:** Some plug-ins name the setting **Stereo Rendering Mode**.

## Single-pass instanced render mode support

Single-pass instanced render mode is supported on the following platforms and
devices:

  * Android devices that support the Multiview extension
  * HoloLens
  * PlayStation VR
  * PC devices (tethered):
  * For DirectX on desktop, the GPU must support Direct3D 11 and the `VPAndRTArrayIndexFromAnyShaderFeedingRasterizer` extension.
  * For OpenGL on desktop, the GPU must support one of the following extensions: 
    * `GL_NV_viewport_array2`
    * `GL_AMD_vertex_shader_layer`
    * `GL_ARB_shader_viewport_layer_array`

If you set the **Render Mode** to **Single Pass Instanced** when that mode is
not supported, then rendering falls back to multi-pass mode.

**Notes:**

  * Unity doesn’t support single-pass instanced rendering in the built-in **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) when using Shader Graph.

  * Unity doesn’t support single-pass instanced rendering in the built-in render pipeline when using deferred rendering.

[](xr-render-pipeline-compatibility.html)

Universal Render Pipeline compatibility in XR

[](SinglePassInstancing.html)

Single-pass instanced rendering and custom shaders

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

