[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/rendering-paths-comparison.html)
  * [中文](/cn/current/Manual/urp/rendering-paths-comparison.html)
  * [日本語](/ja/current/Manual/urp/rendering-paths-comparison.html)
  * [한국어](/kr/current/Manual/urp/rendering-paths-comparison.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/rendering-paths-comparison.html)
  * [中文](/cn/current/Manual/urp/rendering-paths-comparison.html)
  * [日本語](/ja/current/Manual/urp/rendering-paths-comparison.html)
  * [한국어](/kr/current/Manual/urp/rendering-paths-comparison.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Get started with URP](../urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](../urp/urp-concepts.html)
  * [Rendering paths in URP](../urp/rendering-paths-landing.html)
  * Choose a rendering path in URP

[](../urp/rendering-paths-introduction-urp.html)

Introduction to rendering paths in URP

[](../urp/rendering-paths-set.html)

Set the rendering path in URP

# Choose a rendering path in URP

Deciding on which [rendering path](rendering-paths-introduction-urp.html)The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath) is most suitable for your
Universal **Render Pipeline** A series of operations that take the contents of
a Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) project depends on
the type of project, and on the target hardware.

Use the default **Forward rendering** A rendering path that renders each
object in one or more passes, depending on lights that affect the object.
Lights themselves are also treated differently by Forward Rendering, depending
on their settings and intensity. [More info](../RenderTech-
ForwardRendering.html)  
See in [Glossary](../Glossary.html#ForwardRendering) path if you don’t have
many lights in the **scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) or you’re rendering on a mobile or
low-end platform, because Unity limits both the number of lights and the
number of per-pixel lights.

Choose the Forward+ rendering path in the following cases:

  * You have many lights in your scene, and the Deferred rendering path renders too slowly on the platform you build for.
  * You need to blend more than 2 **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](../class-ReflectionProbe.html)  
See in [Glossary](../Glossary.html#ReflectionProbe).

  * You use the [Entities package](https://docs.unity3d.com/Packages/com.unity.entities@1.3/manual/index.html).

Choose the Deferred rendering path in the following cases:

  * You don’t need to use [Rendering Layers](features/rendering-layers.html). URP renders an extra G-buffer render target if you use Rendering Layers in the Deferred rendering path, which might impact performance.
  * You don’t need accurate **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](../terrain-UsingTerrains.html)  
See in [Glossary](../Glossary.html#Terrain) blending. For more information,
refer to [Introduction to the deferred rendering path](rendering/deferred-
rendering-path-introduction.html).

Avoid using lights with a Subtractive or **Shadowmask** A Texture that shares
the same UV layout and resolution with its corresponding lightmap. [More
info](../lighting-mode.html#shadowmask)  
See in [Glossary](../Glossary.html#Shadowmask) [Lighting Mode](../lighting-
mode-landing.html) with the Deferred rendering path, because these lights are
optimized only for the Forward rendering path.

Unity falls back to a different rendering path in the following situations:

  * If you select the Deferred rendering path but a **shader** A program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) doesn’t support **deferred
shading** A rendering path in the Built-in Render Pipeline that places no
limit on the number of Lights that can affect a GameObject. All Lights are
evaluated per-pixel, which means that they all interact correctly with normal
maps and so on. Additionally, all Lights can have cookies and shadows. [More
info](../RenderTech-DeferredShading.html)  
See in [Glossary](../Glossary.html#Deferredshading). Unity renders the
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) using a Forward rendering path
at the end of rendering.

  * If the GPU on the device you build for doesn’t support the rendering path you select. Unity falls back to a different rendering path.

## Rendering path comparison

The following table lists the differences between the rendering paths in URP.

**Feature** | **Forward** | **Forward+** | **Deferred**  
---|---|---|---  
Mobile performance | Low performance impact. | Low performance impact. | High performance impact, because Unity adds extra render passes to render the G-buffer.  
Render passes per object | 1 | 1 | 1  
[Realtime lights per object](lighting/light-limits-in-urp.html) | 9 | Unlimited | Unlimited for opaque objects. 9 for transparent objects. |   
[Realtime lights per camera](lighting/light-limits-in-urp.html) | Up to 257 depending on the platform. | Up to 256 depending on the platform. The Forward+ Rendering Path treats the Main Light and Additional Lights the same way, so the per-camera limits are one light less. | Up to 257 depending on the platform.  
Per-vertex lights | Yes | No | No  
Disable the Main Light | Yes | No | No  
Per-pixel normals | Accurate, with no encoding. | Accurate, with no encoding. | Less accurate encoded normals, or you can select more accurate but slower normals. For more information, refer to [G-buffer layout in the Deferred rendering path](rendering/g-buffer-layout.html).  
[Multisample anti-aliasing (MSAA)](anti-aliasing.html) | Yes | Yes | No  
[Camera stacking](camera-stacking.html) | Yes | Yes | Yes, but the Base **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) uses the Deferred rendering path,
and Overlay Cameras use the Forward rendering path. For more information,
refer to [Introduction to camera render types](../camera-types-and-render-
type-introduction).  
  
## Additional resources

  * [Light limits in URP](lighting/light-limits-in-urp.html)
  * [Per-pixel and per-vertex lights](../PerPixelLights.html)
  * [Rendering paths in URP](rendering-paths-introduction-urp.html)

[](../urp/rendering-paths-introduction-urp.html)

Introduction to rendering paths in URP

[](../urp/rendering-paths-set.html)

Set the rendering path in URP

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

