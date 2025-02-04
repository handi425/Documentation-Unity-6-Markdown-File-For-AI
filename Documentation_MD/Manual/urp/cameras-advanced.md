[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/cameras-advanced.html)
  * [中文](/cn/current/Manual/urp/cameras-advanced.html)
  * [日本語](/ja/current/Manual/urp/cameras-advanced.html)
  * [한국어](/kr/current/Manual/urp/cameras-advanced.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/cameras-advanced.html)
  * [中文](/cn/current/Manual/urp/cameras-advanced.html)
  * [日本語](/ja/current/Manual/urp/cameras-advanced.html)
  * [한국어](/kr/current/Manual/urp/cameras-advanced.html)

  * [Working in Unity](../working-in-unity.html)
  * [Cameras](../Cameras.html)
  * [Cameras in URP](../urp/urp-cameras-landing.html)
  * Camera render order in URP

[](../urp/User-Render-Requests.html)

Create a render request in URP

[](../urp/features/motion-vectors-landing.html)

Motion vectors in URP

# Camera render order in URP

This page describes when a Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) performs the following operations:

  * Clearing the color and depth buffers
  * Base Camera
  * Overlay Camera
  * Culling and rendering
  * Rendering order optimizations.

## Clearing the color and depth buffers

In the Universal Render Pipeline (URP), Camera clearing behavior depends on
the Camera’s [Render Type](camera-types-and-render-type.html).

### Base Camera

#### Color buffer

At the start of its render loop, a Camera with the [Base Render Type](camera-
types-and-render-type.html) can clear its color buffer to a **Skybox** A
special type of Material used to represent skies. Usually six-sided. [More
info](../sky-landing.html)  
See in [Glossary](../Glossary.html#Skybox), clear its color buffer to a solid
color, or use an uninitialized color buffer. You can define this behavior
using the **Background Type** property in the [Camera Inspector](camera-
component-reference.html) when **Render Type** is set to **Base**.

Note that the contents of the uninitialized color buffer vary by platform. On
some platforms, the unitialized color buffer will contain data from the
previous frame. On other platforms, the unitialized color buffer will contain
unintialized memory. You should choose to use an unitialized color buffer only
if your Camera draws to every **pixel** The smallest unit in a computer image.
Pixel size depends on your screen resolution. Pixel lighting is calculated at
every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) in the color buffer, and you do not
wish to incur the cost of an unnecessary clear operation.

#### Depth buffer

A Base Camera always clears its **depth buffer** A memory store that holds the
z-value depth of each pixel in an image, where the z-value is the depth for
each rendered pixel from the projection plane. [More info](../class-
RenderTexture.html)  
See in [Glossary](../Glossary.html#depthbuffer) at the start of each render
loop.

### Overlay Camera

#### Color buffer

At the start of its render loop, an [Overlay Camera](camera-types-and-render-
type-introduction.html#overlay-camera) receives a color buffer containing
color data from the previous Cameras in the Camera stack. It does not clear
the contents of the color buffer.

#### Depth buffer

At the start of its render loop, an Overlay Camera receives a depth buffer
containing depth data from the previous Cameras in the Camera Stack. You can
define this behavior using the **Clear Depth** property in the [Camera
Inspector](camera-component-reference.html) when **Render Type** is set to
**Overlay**.

When **Clear Depth** is set to true, the Overlay Camera clears the depth
buffer and draws its view to the color buffer on top of any existing color
data. When **Clear Depth** is set to false, the Overlay Camera tests against
the depth buffer before drawing its view to the color buffer.

## Culling and rendering

If your URP **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) contains multiple Cameras, Unity
performs their culling and rendering operations in a predictable order.

Once per frame, Unity performs the following operations:

  1. Unity gets the list of all active [Base Cameras](camera-types-and-render-type-introduction.html#base-camera) in the scene.
  2. Unity organises the active Base Cameras into 2 groups: Cameras that render their view to **Render Textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#RenderTexture), and Cameras that render
their view to the screen.

  3. Unity sorts the Base Cameras that render to Render Textures into **Priority** order, so that Cameras with a higher **Priority** value are drawn last.
  4. For each Base Camera that renders to a Render Texture, Unity performs the following steps: 
    1. Cull the Base Camera
    2. Render the Base Camera to the Render Texture
    3. For each [Overlay Camera](camera-types-and-render-type-introduction.html#overlay-camera) that is part of the Base Camera’s [Camera Stack](camera-stacking.html), in the order defined in the Camera Stack: 
      1. Cull the Overlay Camera
      2. Render the Overlay Camera to the Render Texture
  5. Unity sorts the Base Cameras that render to the screen into **Priority** order, so that Cameras with a higher **Priority** value are drawn last.
  6. For each Base Camera that renders to the screen, Unity performs the following steps: 
    1. Cull the Base Camera
    2. Render the Base Camera to the screen
    3. For each Overlay Camera that is part of the Base Camera’s Camera Stack, in the order defined in the Camera Stack: 
      1. Cull the Overlay Camera
      2. Render the Overlay Camera to the screen

Unity can render an Overlay Camera’s view multiple times during a frame -
either because the Overlay Camera appears in more than one Camera Stack, or
because the Overlay Camera appears in the same Camera Stack more than once.
When this happens, Unity does not reuse any element of the culling or
rendering operation. The operations are repeated in full, in the order
detailed above.

**Note:** In this version of URP, Overlay Cameras and Camera Stacking are
supported only when using the Universal Renderer. Overlay Cameras will not
perform any part of their rendering loop if using the 2D Renderer.

## Rendering order optimizations

URP performs several optimizations within a Camera, including rendering order
optimizations to reduce overdraw. However, when you use a Camera Stack, you
effectively define the order in which those Cameras are rendered. You must
therefore be careful not to order the Cameras in a way that causes excessive
overdraw.

When multiple Cameras in a Camera Stack render to the same render target,
Unity draws each pixel in the render target for each Camera in the Camera
Stack. Additionally, if more than one Base Camera or Camera Stack renders to
the same area of the same render target, Unity draws any pixels in the
overlapping area again, as many times as required by each Base Camera or
Camera Stack.

You can use Unity’s [Frame
Debugger](https://docs.unity3d.com/Manual/FrameDebugger.html), or platform-
specific frame capture and debugging tools, to understand where excessive
overdraw occurs in your scene. You can then optimize your Camera Stacks
accordingly.

## Additional resources

  * [Render a camera outside the rendering loop](User-Render-Requests.html)

[](../urp/User-Render-Requests.html)

Create a render request in URP

[](../urp/features/motion-vectors-landing.html)

Motion vectors in URP

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

